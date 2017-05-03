from git import Repo
from enum import Enum
import os
import string
'''
Created on Mar 21, 2017
@author: mikem
'''

class STREAMS(Enum):
    work = 'work'
    stage='stage'
    test='test'
    prod='master'
    

''' 
API that created and manages content files
through git
'''  
class GDAM(object):
    #
    # Constructor
    #
    def __init__(self, akey, root, rname, rmoniker):
        self.apikey = akey
        self.folder = root
        self.rname = rname
        self.rmoniker = rmoniker

    #
    # Constructor
    #
    def initClient(self):        
        self.master_location = os.path.join(self.folder, self.apikey, STREAMS.prod.value)
        # check the apikey folder first if does not exist create one
        f = os.path.join(self.folder, self.apikey)
        if not os.path.isdir(f) :
            os.mkdir(f)
            os.mkdir(os.path.join(f, STREAMS.prod.value))
            self.repo = Repo()
            self.repo.git.clone(self.rmoniker, "-q", self.master_location)
        elif  not os.path.isdir(self.master_location) :
            os.mkdir(self.master_location)
            self.repo = Repo()
            self.repo.git.clone(self.rmoniker, "-q", self.master_location)
           
           
        self.repo = Repo(self.master_location)            
        fname = os.path.join(self.master_location, 'README')
        f = open(fname,'w')
        f.write(self.rname)
        f.close()
        
        self.repo.git.add(fname)       
        self.repo.git.commit("-m", fname, "--all")
        self.repo.git.push("origin", STREAMS.prod.value)
            
        self.repo.git.checkout(STREAMS.prod.value) 
        self.repo.git.pull('origin', STREAMS.prod.value)        

    #
    # Constructor
    #
    def initUser(self, user):
        self.user_location = os.path.join(self.folder, self.apikey, 'users', str(user.id))
        rloc = os.path.join(self.user_location, self.rname)
        # check the apikey folder first if does not exist create one
        f = os.path.join(self.folder, self.apikey)
        if not os.path.isdir(f) :
            raise ValueError('E_NoClientInit', user.clientId)
        elif  not os.path.isdir(self.user_location) :
            os.makedirs(self.user_location)
            self.repo = Repo()
            self.repo.git.clone(self.rmoniker, "-q", rloc)
   
        self.repo = Repo(rloc)
        self.repo.git.branch(STREAMS.work.value)
        self.repo.git.branch(STREAMS.stage.value)
        self.repo.git.branch(STREAMS.test.value)
        
        self.repo.git.checkout(STREAMS.work.value) 
    
    '''
     Returns top level commit log hex value
    '''  
    def getCommitLog(self, fn) :
        logResult = self.repo.git.log("--pretty=format:'%H %f %ct'", fn)
        names_list = logResult.splitlines()
        res = []
        for x in names_list : 
            lines = x.replace("'", "").split(" ")
            res.append(lines)
        return res[0][0]
        
    """
        Set target env for which we want to 
        create content files.
    """    
    def setEnv(self, s=STREAMS.work):
        try:
            self.repo.git.checkout(s.value) 
            self.repo.git.pull('origin', s.value)
        except ValueError:
            pass
        
    '''
      Move document 
    '''  
    def moveDocument(self, fn, frm, to):
            self.repo.git.checkout(frm.value) 
            self.repo.git.pull('origin', frm.value)
            hex = self.getCommitLog(fn)
            self.repo.git.checkout(to.value) 
            self.repo.git.pull('origin', to.value)
            try:
                self.repo.git._call_process("cherry-pick", "-x", hex)
            except ValueError:
                pass
            
            self.repo.git.push('origin', to.value)

    """git show 27cf8e84bb88e24ae4b4b3df2b77aab91a3735d8:full/repo/path/to/my_file.txt"""                
    def createDocument(self, doc, name):
        try:
            self.repo.git.checkout(STREAMS.work.value) 
            fname = os.path.join(self.user_location, self.rname, name);
            f = open(fname,'w')
            f.write(doc)
            f.close()
            self.repo.git.add(fname)       
            self.repo.git.commit("-m", fname, "--all")
            self.repo.git.push("origin", STREAMS.work.value)
            return self.getCommitLog(name)
        except ValueError:
            pass

    """git show 27cf8e84bb88e24ae4b4b3df2b77aab91a3735d8:full/repo/path/to/my_file.txt"""                
    def updateDocument(self, doc, name, stream = STREAMS.work):
        try:
            self.repo.git.checkout(stream.value) 
            fname = os.path.join(self.user_location, self.rname, name);
            f = open(fname,'w')
            f.write(doc)
            f.close()
            self.repo.git.commit("-m", fname, "--all")
            self.repo.git.push("origin", stream.value)
            return self.getCommitLog(name)
        except ValueError:
            pass

    def getDocument(self, name, stream=STREAMS.work):
        try:
            self.repo.git.checkout(stream.value) 
            self.repo.git.pull('origin', stream.value)
            f = open(os.path.join(self.user_location, self.rname, name),'r')
            doc = f.read()
            f.close()
            return doc
        except ValueError:
            pass

    def getDocumentByVer(self, name, ver):
        try:
            f = self.repo.git.show(ver+":"+name) 
            return f
        except ValueError:
            pass
        