from django.core.management.base import BaseCommand
from entries.models import DataEntry
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the database with mock entries'

    def handle(self, *args, **options):
        categories = ['text', 'image_url']
        text_contents = [
            "This is a sample text entry.",
            "Important meeting notes from today.",
            "Remember to follow up with the team.",
            "Project status update: On track",
            "Key points from the presentation.",
        ]
        
        image_urls = [
            "https://picsum.photos/800/600",
            "https://picsum.photos/600/400",
            "https://picsum.photos/400/300",
            "https://picsum.photos/500/500",
            "https://picsum.photos/700/500",
        ]

        # Generate 75 entries
        for i in range(75):
            category = random.choice(categories)
            content = random.choice(text_contents) if category == 'text' else random.choice(image_urls)
            
            random_days = random.randint(0, 30)
            random_hours = random.randint(0, 23)
            random_minutes = random.randint(0, 59)
            timestamp = timezone.now() - timedelta(
                days=random_days,
                hours=random_hours,
                minutes=random_minutes
            )

            DataEntry.objects.create( 
                content=content,
                category=category,
                timestamp=timestamp,
                is_reviewed=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded 75 entries'))