from re import findall
from time import time
from json import loads, dumps
from base64 import b64encode, b64decode
from random import choice
from tls_client import Session
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

class Roblox:
    def __init__(self):
        self.infos = {
            "username": "botxtegaprime23",
            "password": "S4l0m0n2o25@",
        }

        self.session = Session(
            client_identifier = "firefox_121",
            random_tls_extension_order = True
        )

        self.csrf_token = self.get_cookies()
        self.server_nonce = self.get_server_nonce()
        self.public_key_spki, self.saiSignature = self.get_signatures()

        self.signup()

    def get_cookies(self):
        csrf = str(self.session.get(
            url = "https://www.roblox.com/",
            headers = {
                "host": "www.roblox.com",
                "connection": "keep-alive",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "sec-fetch-site": "none",
                "sec-fetch-mode": "navigate",
                "sec-fetch-user": "?1",
                "sec-fetch-dest": "document",
                "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "\"Windows\"",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
            }
        ).text)
        csrf = findall(r'<meta name="csrf-token" data-token="(.*?)" />', csrf)[0]
        
        self.session.get(
            url = "https://www.roblox.com/timg/rbx",
            headers = {
                "host": "www.roblox.com",
                "connection": "keep-alive",
                "sec-ch-ua-platform": "\"Windows\"",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
                "sec-ch-ua-mobile": "?0",
                "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "no-cors",
                "sec-fetch-dest": "image",
                "referer": "https://www.roblox.com/fr",
                "accept-encoding": "gzip, deflate, br, zstd",
                "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            }
        )

        return csrf

    def get_server_nonce(self):
        res = self.session.get(
            url = "https://apis.roblox.com/hba-service/v1/getServerNonce",
            headers = {
                "host": "apis.roblox.com",
                "connection": "keep-alive",
                "sec-ch-ua-platform": "\"Windows\"",
                "accept-language": "fr;q=0.01",
                "accept": "application/json, text/plain, */*",
                "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
                "sec-ch-ua-mobile": "?0",
                "origin": "https://www.roblox.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.roblox.com/",
                "accept-encoding": "gzip, deflate, br, zstd",
            }
        )

        return str(res.text).split("\"")[1].split("\"")[0]
    
    def get_signatures(self):
        private_key = ec.generate_private_key(
            ec.SECP256R1(),
            default_backend()
        )
        public_key = private_key.public_key()
        public_key_spki = b64encode(public_key.public_bytes(
            encoding = serialization.Encoding.PEM,
            format = serialization.PublicFormat.SubjectPublicKeyInfo
        )).decode()

        payload = f"{public_key_spki}|{int(time())}|{self.server_nonce}".encode()

        saiSignature = b64encode(private_key.sign(
            payload,
            ec.ECDSA(hashes.SHA256())
        )).decode()

        return public_key_spki, saiSignature
    
    def signup(self, roblox_challenge = None):
        headers = {
            "host": "auth.roblox.com",
            "connection": "keep-alive",
            "sec-ch-ua-platform": "\"Windows\"",
            "x-csrf-token": self.csrf_token,
            "accept-language": "fr;q=0.01",
            "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://www.roblox.com",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.roblox.com/",
            "accept-encoding": "gzip, deflate, br, zstd",
        }

        if roblox_challenge:
            headers["roblox-challenge"] = roblox_challenge

        res = self.session.post(
            url = "https://auth.roblox.com/v2/signup",
            json = {
                "username": self.infos["username"],
                "password": self.infos["password"],
                "birthday": "1998-12-22T23:00:00.000Z",
                "gender": choice([1, 2]),
                "isTosAgreementBoxChecked": True,
                "agreementIds": [
                    "460f3c21-e306-4de0-949f-8e263b7210d0",
                    "b354f748-8bb4-4859-9b71-c61a63e140dc"
                ],
                "secureAuthenticationIntent": {
                    "clientPublicKey": self.public_key_spki,
                    "clientEpochTimestamp": int(time()),
                    "serverNonce": self.server_nonce,
                    "saiSignature": self.saiSignature
                }
            },
            headers = headers
        )

        if res.status_code != 200:
            print(res.text)
            roblox_challenge = loads(b64decode(str(res.headers["Rblx-Challenge-Metadata"]).encode()).decode())
            challenge_id = roblox_challenge["unifiedCaptchaId"]
            data_blob = roblox_challenge["dataExchangeBlob"]

            # Solver Logic
            captcha_token = ""

            self.signup(b64encode(dumps({
                "unifiedCaptchaId": challenge_id,
                "captchaToken": captcha_token,
                "actionType": "Signup"
            }).encode()).decode())

        print(res.text)
    
if __name__ == "__main__":
    rbx = Roblox()
