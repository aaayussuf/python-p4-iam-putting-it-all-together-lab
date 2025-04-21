#!/usr/bin/env python3

from flask_migrate import MigrateCommand
from flask_script import Manager
from config import app, db

manager = Manager(app)

# Add the migrate command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
