# -*- coding: utf-8 -*-
from fastapi import Request, HTTPException
from fastapi.responses import PlainTextResponse


def make_view(robot):
    """
    为一个 BaseRoBot 生成 FastAPI view。

    Usage ::

        from werobot import WeRoBot

        robot = WeRoBot(token='token')


        @robot.handler
        def hello(message):
            return 'Hello World!'

        from fastapi import FastAPI
        from werobot.contrib.fastapi import make_view

        app = FastAPI()
        app.add_api_route(
            "/{path:path}",  # WeRoBot 挂载地址
            make_view(robot),
            methods=["GET", "POST"]
        )


    :param robot: 一个 BaseRoBot 实例
    :return: 一个标准的 FastAPI view
    """

    async def werobot_view(request: Request):
        # 检查签名
        query_params = request.query_params

        timestamp = query_params.get("timestamp", None)
        nonce = query_params.get("nonce", None)
        signature = query_params.get("signature", None)
        if not robot.check_signature(timestamp, nonce, signature):
            raise HTTPException(status_code=403, detail="Signature verification failed")

        if request.method == 'GET':
            # 返回echostr
            echostr = query_params.get("echostr", "hello")
            return PlainTextResponse(echostr)
        elif request.method == 'POST':
            # 读取消息体
            body = await request.body()
            message = robot.parse_message(
                body,
                timestamp=timestamp,
                nonce=nonce,
                msg_signature=query_params.get("msg_signature", None)
            )
            # 获取加密回复
            response = await robot.get_encrypted_reply(message)
            return PlainTextResponse(response)

    return werobot_view
