from django.core.management.base import BaseCommand
import silly
from expenses.models import Expense


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, n, *args, **options):
        for i in range(n):
            o = Expense(
                date="2018-12-13",
                amount="11.3",
                title=silly.title(),
                description=silly.paragraph()
            )
            o.save()
