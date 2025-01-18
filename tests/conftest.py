import pytest
from app import create_app

# if:: from app import create_app ModuleNotFoundError: No module named 'app'
# run pytest as >>> python -m pytest

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    # app = create_app()
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
