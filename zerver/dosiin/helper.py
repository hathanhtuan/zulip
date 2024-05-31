import requests

DOSIIN_TRANSLATION_DOMAIN = "https://translate.dosi-in.com/"
DOSIIN_TRANSLATION_AUTH = f"{DOSIIN_TRANSLATION_DOMAIN}api/v1/auth/login"
DOSIIN_TRANSLATION_MULTIPLE = f"{DOSIIN_TRANSLATION_DOMAIN}api/v1/translations/multiple"
DOSIIN_TRANSLATION_AUTH_TOKEN = "oat_Ng.WGVmdy16ZlhwZVQ3bmJEcDRHY3l0YV9ucU9FQkxtWUdqc1ZWZkFtMDM3ODEzNDM1Mzc"


def dosiin_translate(message):

    result = requests.post(
        url=DOSIIN_TRANSLATION_MULTIPLE,
        headers={
            "Authorization": f"Bearer {DOSIIN_TRANSLATION_AUTH_TOKEN}"
        },
        json={
            "content": message,
            "language": "Vietnamese,Korean,Chinese,English"
        }
    )

    result = result.json()
    print(result)
    return result

