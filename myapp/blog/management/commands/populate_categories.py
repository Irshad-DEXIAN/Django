from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Category



class Command(BaseCommand):
    help = "This command inserts the Command data"

    def handle(self, *args: Any, **options: Any):
        
        Category.objects.all().delete()

        categories = ['Sports','Technology','Science' ,'Art' ,'Food' ]


        for category in categories:
            Category.objects.create(name=category)

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))

