from flaskblog import app, db
from flaskblog.models import User

with app.app_context():
    users = [
        User(username="ethanclark", email="ethan.clark@example.com", password="password"),
        User(username="gracehall", email="grace.hall@example.com", password="password"),
        User(username="lucasyoung", email="lucas.young@example.com", password="password"),
        User(username="charlotteking", email="charlotte.king@example.com", password="password"),
        User(username="henrywright", email="henry.wright@example.com", password="password"),
        User(username="ameliabaker", email="amelia.baker@example.com", password="password"),
        User(username="jackturner", email="jack.turner@example.com", password="password"),
        User(username="chloescott", email="chloe.scott@example.com", password="password"),
        User(username="masongreen", email="mason.green@example.com", password="password"),
        User(username="harperadams", email="harper.adams@example.com", password="password"),
        User(username="owenhill", email="owen.hill@example.com", password="password"),
        User(username="ellacarter", email="ella.carter@example.com", password="password"),
        User(username="loganmitchell", email="logan.mitchell@example.com", password="password"),
        User(username="zoeperez", email="zoe.perez@example.com", password="password"),
        User(username="aidanfoster", email="aidan.foster@example.com", password="password"),
        User(username="lilybrooks", email="lily.brooks@example.com", password="password"),
        User(username="sebastianross", email="sebastian.ross@example.com", password="password"),
        User(username="victoriacook", email="victoria.cook@example.com", password="password"),
        User(username="nathanreed", email="nathan.reed@example.com", password="password"),
        User(username="hannahbell", email="hannah.bell@example.com", password="password"),
    ]

    db.session.add_all(users)
    db.session.commit()

    print("20 users added!")