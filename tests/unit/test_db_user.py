def test_user_create(client, app):
    from app import db, User

    # Create a new user instance
    user = User(email="test@test.test", username="testuser")
    db.session.add(user)
    db.session.commit()

    # Verify the user was added to the database
    created_user = user.query.filter_by(username="testuser").first()
    assert created_user is not None
    assert created_user.username == "testuser"
