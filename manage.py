
from modules.admin.admin import admin_bule
from modules.web.index import index_bule
from modules.web.user import user_bule
from modules import *
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_wtf import CSRFProtect
from apps import app,db
#注册后台管理员蓝图 url_prefix指定访问url不加时直接访问
app.register_blueprint(admin_bule,url_prefix='/admin')

#注册前台首页蓝图 url_prefix指定访问url不加时直接访问
app.register_blueprint(index_bule,url_prefix='/index')

app.register_blueprint(user_bule,url_prefix='/user')
CSRFProtect(app)
manage = Manager(app)
migrate = Migrate(app,db)
manage.add_command('db',MigrateCommand)
if __name__ == '__main__':
    app.run()
    # manage.run()





