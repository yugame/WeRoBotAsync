# -*- coding: utf-8 -*-

import werobot

robot = werobot.WeRoBot(token='formmtest')


@robot.filter("帮助")
async def show_help(message):
    return """
    帮助
    notice
    """


@robot.text
async def hello_world(message):
    return 'Hello World!'


robot.run()
