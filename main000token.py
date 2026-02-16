# -*- coding: utf-8 -*-

import logging
from api.examples_user.auth.auth_functions import auth_token
from api.examples_user.auth.auth_functions import auth_ws_token
import api.examples_user.kis_auth as ka

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    print("Hello from kis!")

    # 인증
    ka.auth()
    trenv = ka.getTREnv()

    ##############################################################################################
    # [인증] OAuth 접근토큰 발급
    ##############################################################################################

    df = auth_token(grant_type="client_credentials", appkey=trenv.my_app, appsecret=trenv.my_sec, env_dv="real")
    print(df)

    ##############################################################################################
    # [인증] WebSocket 웹소켓 접속키 발급
    ##############################################################################################

    df = auth_ws_token(grant_type="client_credentials",  appkey=trenv.my_app, appsecret=trenv.my_sec, env_dv="real")
    print(df)


if __name__ == "__main__":
    main()
