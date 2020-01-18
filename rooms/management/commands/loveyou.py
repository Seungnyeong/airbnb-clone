from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "loveyou command add"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="hosw many times do you want me to tell you tha I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I LOVE YOU"))

    print("hello")

