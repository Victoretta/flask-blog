from flaskblog import app, db
from flaskblog.models import User, Post

with app.app_context():
    users = User.query.all()

    posts = [
        Post(title="Learning REST APIs", content="Today I built my first REST API using Flask and learned how endpoints work.", author=users[10]),
        Post(title="Python Tips", content="Using list comprehensions has made my code much cleaner and easier to read.", author=users[11]),
        Post(title="A Day at the Beach", content="Spent the afternoon relaxing by the beach and watching the sunset.", author=users[12]),
        Post(title="First Open Source Contribution", content="I submitted my first pull request on GitHub today. It felt great!", author=users[13]),
        Post(title="Database Design", content="Designing a database schema carefully saves a lot of headaches later.", author=users[14]),
        Post(title="Flask Blueprints", content="I'm starting to understand how Blueprints keep larger Flask apps organized.", author=users[15]),
        Post(title="Working from Home", content="Having a dedicated workspace has really improved my productivity.", author=users[16]),
        Post(title="Book Recommendation", content="I'm reading Clean Code and it's changing how I think about programming.", author=users[17]),
        Post(title="Weekend Coding", content="Spent the weekend adding new features to my Flask blog project.", author=users[18]),
        Post(title="Learning Git", content="Branches and pull requests make collaborating on projects much easier.", author=users[19]),
        Post(title="Bootstrap Components", content="Cards, modals, and alerts are some of my favorite Bootstrap components.", author=users[20]),
        Post(title="SQLAlchemy Relationships", content="Relationships make it simple to connect users with their blog posts.", author=users[21]),
        Post(title="Debugging Skills", content="Every bug I fix teaches me something new about programming.", author=users[22]),
        Post(title="Morning Routine", content="A short walk before coding helps me stay focused throughout the day.", author=users[23]),
        Post(title="Why I Love Flask", content="Flask is lightweight, flexible, and perfect for learning web development.", author=users[24]),
        Post(title="Trying Linux", content="I'm experimenting with Ubuntu to improve my development workflow.", author=users[25]),
        Post(title="Coffee Break", content="Sometimes stepping away from the keyboard is the fastest way to solve a bug.", author=users[26]),
        Post(title="My Coding Goals", content="My goal this year is to build and deploy several full-stack web applications.", author=users[27]),
        Post(title="Learning Never Stops", content="Technology changes quickly, so I try to learn something new every week.", author=users[28]),
        Post(title="Finishing My Flask Blog", content="I'm proud of how much I've learned while building this project from scratch.", author=users[29]),
    ]

    db.session.add_all(posts)
    db.session.commit()

    print("20 posts added!")