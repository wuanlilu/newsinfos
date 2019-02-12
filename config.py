# -*- coding: UTF-8 -*-

class Config(object):
    DEBUG = True
    #数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/information_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #数据库内容发送改变之后,自动提交


class ProductConfig(object):
    DEBUG = False
    #数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/information_test1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #数据库内容发送改变之后,自动提交


dict_config = {'config':Config,'product':ProductConfig}