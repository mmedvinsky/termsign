from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = 'services'
    
    def ready(self):
        from services.termsign import TermSign
        assert TermSign.instance("7813628736487236487236482", '/var/tmp/termsign') != None