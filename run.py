from flask_migrate import Migrate
from blog import create_app
from blog import db

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
