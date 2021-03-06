from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from bot import app, db
import bot.model

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()