# VALUES.md

If you don't understand the use of this file, that's okay, it allows me to list the values ​​I need in the code and indicate how to have them.

-   Salomon

## Sign Up Requests

URL: https://auth.roblox.com/v2/signup

### Payload

```json
{
    "username": "s4lomon", # Username
    "password": "S4l0m0n2o25@", # Password
    "birthday": "1998-12-22T23:00:00.000Z", # Datetime (date of birth)
    "gender": 2, # 1 = F | 2 = M
    "isTosAgreementBoxChecked": true, # Definitely yes
    "agreementIds": [
        "460f3c21-e306-4de0-949f-8e263b7210d0", # Terms Of Use
        "b354f748-8bb4-4859-9b71-c61a63e140dc" # Privacy Policy
    ],
    "secureAuthenticationIntent": {
        "clientPublicKey": "", # B64 of ECDSA public key exported as spki
        "clientEpochTimestamp": 1738602391, # Timestamp (w/o miliseconds)
        "serverNonce": "", # JWT token
        "saiSignature": "" # B64 of "public_key_spki:timestamp:serverNonce" signed by ECDSA
    }
}
```

## Captcha Solver

Roblox FunCaptcha ID: `A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F`

```json
{
    "bda": "", # idk
    "public_key": "A2A14B1D-1AF3-C791-9BBC-EE33CC7A0A6F", # public key
    "site": "https://www.roblox.com", # website url
    "userbrowser": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36", # useragent
    "capi_version": "2.11.4", # static
    "capi_mode": "inline", # static
    "style_theme": "default", # static
    "rnd": "0.23544934971043574", # Math.random()
    "data[blob]": "" Data Blob
}
```