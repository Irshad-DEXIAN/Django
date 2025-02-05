from typing import Any
from django.core.management.base import BaseCommand
from blog.models import Post, Category
import random


class Command(BaseCommand):
    help = "This command inserts the post data"

    def handle(self, *args: Any, **options: Any):
        
        Post.objects.all().delete()

        titles = [
            "The Future of Renewable Energy",
            "10 Tips for Learning Django Fast",
            "How AI is Changing the World",
            "Exploring the Depths of the Ocean",
            "The Ultimate Guide to Python Web Development",
            "Mastering Machine Learning in 30 Days",
            "Hidden Gems: Underrated Travel Destinations",
            "The Rise of Electric Vehicles",
            "A Beginner's Guide to Investing",
            "Understanding Quantum Computing",
            "How to Build a Personal Brand Online",
            "The Psychology of Habit Formation",
            "Secrets of the Universe: Black Holes Explained",
            "The Power of Mindfulness and Meditation",
            "Space Exploration: What's Next for Humanity?",
            "The History and Evolution of the Internet",
            "Cybersecurity Trends to Watch in 2025",
            "The Science Behind a Healthy Diet",
            "How Blockchain is Revolutionizing Finance",
            "The Art of Storytelling in the Digital Age"
        ]

        contents = [
            "Renewable energy is shaping the future. This post explores solar, wind, and hydro power innovations.",
            "Want to learn Django quickly? Here are 10 practical tips to master the framework efficiently.",
            "Artificial Intelligence is transforming industries. Discover its impact on healthcare, finance, and more.",
            "Oceans cover 70% of our planet, yet we know so little. Let's dive into the mysteries of the deep sea.",
            "Python is a powerful language for web development. This guide covers Django, Flask, and backend strategies.",
            "Machine learning can be daunting, but this 30-day plan breaks it into simple, actionable steps.",
            "Love to travel? Here are some breathtaking but underrated destinations you should explore.",
            "Electric vehicles are the future of transportation. Learn about advancements, trends, and challenges.",
            "Investing can be overwhelming for beginners. This guide explains stocks, crypto, and mutual funds.",
            "Quantum computing is complex but fascinating. Understand qubits, superposition, and real-world applications.",
            "Building a personal brand is crucial in today's digital world. Here's how to create a strong online presence.",
            "Habits shape our lives. Learn the psychology behind habit formation and how to build better ones.",
            "Black holes are among the universe's biggest mysteries. This post explains their formation and effects.",
            "Mindfulness and meditation can boost focus and reduce stress. Here's how to incorporate them into daily life.",
            "Space exploration is advancing rapidly. From Mars missions to space tourism, here's what's next.",
            "The internet has come a long way. Explore its history from ARPANET to Web 3.0.",
            "Cybersecurity threats are increasing. Stay ahead with these key trends and protection strategies.",
            "A healthy diet is essential for well-being. Learn the science behind nutrition and meal planning.",
            "Blockchain is disrupting finance. Understand how decentralized systems are changing transactions.",
            "Storytelling is a powerful skill. Here's how to craft compelling stories in the digital age."
        ]

        img_urls = [
            "https://picsum.photos/id/10/800/400",
            "https://picsum.photos/id/20/800/400",
            "https://picsum.photos/id/30/800/400",
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/60/800/400",
            "https://picsum.photos/id/70/800/400",
            "https://picsum.photos/id/80/800/400",
            "https://picsum.photos/id/90/800/400",
            "https://picsum.photos/id/100/800/400",
            "https://picsum.photos/id/110/800/400",
            "https://picsum.photos/id/120/800/400",
            "https://picsum.photos/id/130/800/400",
            "https://picsum.photos/id/140/800/400",
            "https://picsum.photos/id/150/800/400",
            "https://picsum.photos/id/160/800/400",
            "https://picsum.photos/id/170/800/400",
            "https://picsum.photos/id/180/800/400",
            "https://picsum.photos/id/190/800/400",
            "https://picsum.photos/id/200/800/400"
        ]

        categories = Category.objects.all()

        for title,content,img_url in zip(titles,contents,img_urls):
            category = random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("Completed Inserting Data!"))

