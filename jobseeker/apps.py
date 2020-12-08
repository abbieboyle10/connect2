from django.apps import AppConfig


class JobseekerConfig(AppConfig):
    name = 'jobseeker'

    def ready(self):
        import jobseeker.signals
