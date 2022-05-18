from app import create_app ,db
from app.models import Users
from flask_migrate import Migrate

app = create_app('dev')

if __name__ == '__main__':
    app.run()
