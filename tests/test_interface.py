import requests


def test_post_xml_to_server():
    url = "http://127.0.0.1:8888/chat"  # 替换为你的接口地址
    headers = {"Content-Type": "application/xml"}  # 设置请求头
    xml_data = """
    <xml>
        <ToUserName><![CDATA[toUser]]></ToUserName>
        <FromUserName><![CDATA[fromUser]]></FromUserName>
        <CreateTime>1348831860</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[帮助]]></Content>
        <MsgId>1234567890123456</MsgId>
    </xml>
    """

    # 发送 POST 请求
    response = requests.post(url, data=xml_data, headers=headers)

    # 输出服务器响应
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
