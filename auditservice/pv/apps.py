from django.apps import AppConfig


class PvConfig(AppConfig):
    name = 'pv'

    def ready(self):
    	import pv.signals