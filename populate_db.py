import asyncio
from datetime import UTC, datetime, timedelta
from pathlib import Path

import httpx
from sqlalchemy import delete, select, update

import models
from database import AsyncSessionLocal, engine
from image_utils import PROFILE_PICS_DIR
from main import app

POPULATE_IMAGES_DIR = Path("populate_images")

USERS = [
    {
        "username": "JohnTechWriter",
        "email": "JohnTechWriter@gmail.com",
        "password": "SecurePass123!",
        "image": "corey.png",
    },
    {
        "username": "SarahCoder",
        "email": "SarahCode@test.com",
        "password": "SecurePass123!",
        # No image - uses default
    },
    {
        "username": "MikeBackend",
        "email": "MikeBackend@test.com",
        "password": "SecurePass123!",
        "image": "willow.png",
    },
    {
        "username": "LisaFrontend",
        "email": "LisaFrontend@test.com",
        "password": "SecurePass123!",
        "image": "farmdogs.png",
    },
    {
        "username": "ChrisDevOps",
        "email": "ChrisDevOps@test.com",
        "password": "SecurePass123!",
        "image": "poppy.png",
    },
    {
        "username": "EmilyFullStack",
        "email": "EmilyFullStack@test.com",
        "password": "SecurePass123!",
        "image": "bronx.png",
    },
]

POSTS = [
    {
        "title": "Getting Started with Modern Web Development",
        "content": "Web development has evolved dramatically over the past decade. Today's frameworks offer incredible tooling and performance improvements. Whether you're building with React, Vue, or any modern framework, the learning curve has never been more manageable.",
    },
    {
        "title": "Database Design Best Practices",
        "content": "Database architecture matters more than most developers realize. Proper normalization, indexing strategies, and query optimization can make or break your application. Take time to plan your schema before building.",
    },
    {
        "title": "Understanding REST API Principles",
        "content": "REST has become the standard for API design because it works. Learn the fundamentals of HTTP methods, status codes, and resource organization. Mastering REST principles will improve your API design significantly.",
    },
    {
        "title": "Security in Web Applications",
        "content": "Security should never be an afterthought. CORS, CSRF protection, password hashing, and HTTPS are not optional extras. Invest in security from day one and your users will appreciate it.",
    },
    {
        "title": "Microservices vs Monoliths",
        "content": "The great architectural debate continues. Both approaches have merits and drawbacks. Start with what you understand, and refactor when complexity demands it. Don't optimize for scalability you don't have yet.",
    },
    {
        "title": "Asynchronous Programming Fundamentals",
        "content": "Async programming is not magic - it's about efficiently using resources. Learn the difference between concurrency and parallelism. Understanding event loops and callbacks will transform how you write responsive applications.",
    },
    {
        "title": "Testing Strategies That Actually Work",
        "content": "Unit tests, integration tests, and end-to-end tests each serve a purpose. Write tests that give you confidence, not just coverage percentages. Quality tests are an investment in your future peace of mind.",
    },
    {
        "title": "DevOps Tools Every Developer Should Know",
        "content": "Docker, Kubernetes, and CI/CD pipelines are no longer exotic tools. Understanding containerization and deployment workflows makes you a better developer. Modern development requires DevOps literacy.",
    },
    {
        "title": "Code Quality and Refactoring",
        "content": "Readable code is maintainable code. Spend time on code reviews, establish linting rules, and don't fear refactoring. Technical debt compounds quickly if left unchecked.",
    },
    {
        "title": "API Authentication Methods",
        "content": "JWT, OAuth, API keys - each authentication method has use cases. Understand when to use each approach. Security and usability both matter in authentication design.",
    },
    {
        "title": "Performance Optimization Techniques",
        "content": "Premature optimization is the root of all evil, but so is ignoring performance. Use profiling tools to identify bottlenecks. Focus on the 20% of code that matters.",
    },
    {
        "title": "Handling Errors Gracefully",
        "content": "Error handling is often overlooked but crucial. Provide meaningful error messages and appropriate HTTP status codes. Your users and other developers will thank you.",
    },
    {
        "title": "Data Validation Best Practices",
        "content": "Never trust user input. Validate early, validate often. Use libraries and frameworks that make validation easy. Automation beats manual checking every time.",
    },
    {
        "title": "Logging and Monitoring",
        "content": "Logs are your window into production. Structured logging makes debugging easier. Set up monitoring and alerts before you need them desperately.",
    },
    {
        "title": "Building Scalable Architecture",
        "content": "Scalability starts with good design. Load balancing, horizontal scaling, and stateless services enable growth. Plan for scale before problems emerge.",
    },
    {
        "title": "Working with Third-Party APIs",
        "content": "Integrating external APIs is common work. Handle rate limiting, timeouts, and errors carefully. Always implement retry logic with exponential backoff.",
    },
    {
        "title": "Documentation That Teams Actually Use",
        "content": "Good documentation saves time and frustration. Keep docs close to code. Automated documentation tools help maintain accuracy as code evolves.",
    },
    {
        "title": "Development Environment Setup",
        "content": "A smooth development environment speeds productivity. Use containerization for consistency. Automate setup processes so new developers get productive quickly.",
    },
    {
        "title": "Version Control Best Practices",
        "content": "Git has become standard for good reason. Meaningful commit messages, feature branches, and code reviews prevent chaos. Treat your repository like professional code.",
    },
    {
        "title": "Caching Strategies for Performance",
        "content": "Caching is not optional for modern applications. Understand cache invalidation, TTLs, and when to cache. Proper caching can reduce load significantly.",
    },
    {
        "title": "Building Real-Time Applications",
        "content": "WebSockets enable interactive experiences. Polling is dead. Learn real-time technologies to build engaging applications.",
    },
    {
        "title": "Message Queues and Event-Driven Architecture",
        "content": "Decoupling services with message queues improves reliability. Event-driven systems scale differently. Learn RabbitMQ, Kafka, or similar tools.",
    },
    {
        "title": "Data Migration Strategies",
        "content": "Migrating data is always risky. Plan carefully, test extensively, and have rollback plans. Data integrity is non-negotiable.",
    },
    {
        "title": "API Rate Limiting and Throttling",
        "content": "Rate limiting protects your service. Implement it thoughtfully to prevent abuse while respecting legitimate users. Clear error messages help clients understand limits.",
    },
    {
        "title": "Internationalization and Localization",
        "content": "Building globally accessible applications requires planning. Translations, date formats, and currency handling matter. Don't build i18n as an afterthought.",
    },
    {
        "title": "Backup and Disaster Recovery",
        "content": "Backups are insurance you hope never to use. Test recovery procedures regularly. A backup that doesn't restore is worse than no backup.",
    },
    {
        "title": "Accessibility in Web Development",
        "content": "Web accessibility benefits everyone. WCAG guidelines are not suggestions - they're standards. Build inclusive applications.",
    },
    {
        "title": "Progressive Enhancement Principles",
        "content": "Start with core functionality. Enhance progressively. Your app should work when JavaScript breaks. Basic HTML is your foundation.",
    },
    {
        "title": "Debugging Complex Systems",
        "content": "Debugging skills separate good developers from great ones. Use debuggers, logs, and systematic approaches. Patience and curiosity matter.",
    },
    {
        "title": "Code Review Process",
        "content": "Code reviews improve code quality and spread knowledge. Be respectful but thorough. Understand it's about the code, not the person.",
    },
    {
        "title": "Technical Debt Management",
        "content": "Technical debt is real debt with interest. Address it regularly. Communicate its cost to stakeholders. Prevention is cheaper than rescue.",
    },
    {
        "title": "Building Resilient Systems",
        "content": "Failure is inevitable. Build for resilience. Implement circuit breakers, timeouts, and graceful degradation. Expect things to fail.",
    },
]

# The 44th post - always the oldest (easter egg for pagination tutorial)
POST_44 = {
    "title": "My Journey Into Software Development",
    "content": "If you've paginated all the way to this post, the 44th one... you get to learn how I started my journey in tech. From learning to code in college to my first job, the path wasn't always clear. Every challenge taught me something valuable. Keep pushing forward, and you'll surprise yourself with what you can accomplish.",
}


async def clear_existing_data() -> None:
    # Delete profile pictures from local storage
    if PROFILE_PICS_DIR.exists():
        for file in PROFILE_PICS_DIR.iterdir():
            if file.is_file() and file.name != ".gitkeep":
                file.unlink()
        print(f"Deleted profile pictures from {PROFILE_PICS_DIR}")

    # Clear database tables (order respects foreign keys)
    async with AsyncSessionLocal() as db:
        await db.execute(delete(models.Post))
        await db.execute(delete(models.User))
        await db.commit()
    print("Cleared existing data")


async def update_post_dates() -> None:
    now = datetime.now(UTC)

    async with AsyncSessionLocal() as db:
        result = await db.execute(select(models.Post).order_by(models.Post.id))
        posts = result.scalars().all()

        if not posts:
            return

        # First post (POST_44) is the oldest - ~90 days ago
        await db.execute(
            update(models.Post)
            .where(models.Post.id == posts[0].id)
            .values(date_posted=now - timedelta(days=90)),
        )

        # Remaining posts: each ~1.5 days newer than previous
        for i, post in enumerate(posts[1:], start=1):
            days_ago = (len(posts) - i) * 1.5
            hours_offset = (i * 7) % 24
            post_date = now - timedelta(days=days_ago, hours=hours_offset)
            await db.execute(
                update(models.Post)
                .where(models.Post.id == post.id)
                .values(date_posted=post_date),
            )

        await db.commit()
    print("Updated post dates")


async def populate() -> None:
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://localhost",
    ) as client:
        # Clear existing data (local images first, then database)
        await clear_existing_data()

        users: list[dict] = []

        print(f"\nCreating {len(USERS)} users...")
        for user_data in USERS:
            response = await client.post(
                "/api/users",
                json={
                    "username": user_data["username"],
                    "email": user_data["email"],
                    "password": user_data["password"],
                },
            )
            response.raise_for_status()
            user = response.json()
            print(f"  Created: {user['username']}")

            response = await client.post(
                "/api/users/token",
                data={
                    "username": user_data["email"],
                    "password": user_data["password"],
                },
            )
            response.raise_for_status()
            token = response.json()["access_token"]

            if image_name := user_data.get("image"):
                image_path = POPULATE_IMAGES_DIR / image_name
                if image_path.exists():
                    response = await client.patch(
                        f"/api/users/{user['id']}/picture",
                        files={
                            "file": (
                                image_name,
                                image_path.read_bytes(),
                                "image/png",
                            ),
                        },
                        headers={"Authorization": f"Bearer {token}"},
                    )
                    response.raise_for_status()
                    print(f"    Uploaded: {image_name}")

            users.append(
                {"id": user["id"], "username": user["username"], "token": token},
            )

        print(f"\nCreating {len(POSTS) + 1} posts...")

        # First create POST_44 (will become oldest after date update)
        response = await client.post(
            "/api/posts",
            json={"title": POST_44["title"], "content": POST_44["content"]},
            headers={"Authorization": f"Bearer {users[0]['token']}"},
        )
        response.raise_for_status()
        print(f"  Created: '{POST_44['title']}'")

        # Create remaining posts in reverse (last in list = oldest, first = newest)
        for i, post_data in enumerate(reversed(POSTS)):
            user = users[i % len(users)]
            response = await client.post(
                "/api/posts",
                json={
                    "title": post_data["title"],
                    "content": post_data["content"],
                },
                headers={"Authorization": f"Bearer {user['token']}"},
            )
            response.raise_for_status()
            title = post_data["title"]
            print(
                f"  Created: '{title[:50]}...'"
                if len(title) > 50
                else f"  Created: '{title}'",
            )

        print("\nUpdating post dates...")
        await update_post_dates()

    await engine.dispose()

    print("\nDone!")
    print(f"  {len(USERS)} users")
    print(f"  {len(POSTS) + 1} posts")
    print("  Profile pictures saved locally")


if __name__ == "__main__":
    asyncio.run(populate())
