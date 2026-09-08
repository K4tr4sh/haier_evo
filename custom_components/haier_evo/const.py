DOMAIN = "haier_evo"
COMMON_LIMIT_CALLS = 5
COMMON_LIMIT_PERIOD = 60
LOGIN_LIMIT_CALLS = 1
LOGIN_LIMIT_PERIOD = 15
LOGIN_LIMIT_MAX = 900
LOGIN_LIMIT_429 = 60
LOGIN_LIMIT_500 = 60
REFRESH_LIMIT_CALLS = 1
REFRESH_LIMIT_PERIOD = 15
REFRESH_LIMIT_MAX = 900
REFRESH_LIMIT_429 = 60
REFRESH_LIMIT_500 = 60
API_HTTP_ROUTE = True
API_TIMEOUT = 15
API_PATH = "https://evo.haieronline.ru"
API_LOGIN = "v2/{region}/users/auth/sign-in"
API_TOKEN_REFRESH = "v2/{region}/users/auth/refresh"
API_DEVICES = "v2/{region}/pages/sduiRawPaginated/smartHome?part=1&partitionWeight=6"
# Новый формат страницы умного дома (используется мобильным приложением и
# рабочим homebridge-haier-evo): компонент smartHomeSpacesV1 с комнатами
API_DEVICES_SPACES = "v2/{region}/pages/sduiRawPaginated/smartHome/spaces/house?part=1&partitionWeight=6"
API_STATUS = "https://iot-platform.evo.haieronline.ru/mobile-backend-service/api/v1/config/{mac}?type=DETAILED"
API_WS_PATH = "wss://iot-platform.evo.haieronline.ru/gateway-ws-service/ws/"
# Заголовки, имитирующие актуальную версию мобильного приложения.
# Без них сервер отвечает "Авторизация недоступна. Обновите приложение."
# Актуальная версия приложения "evo: умный дом от Haier" — 4.53.0.
# ВАЖНО: by/kz-бэкенд пропускает только актуальную версию (проверено:
# VersionCode 14500-15000 проходит гейт, 13766/14200/15500+ — нет),
# ru-бэкенд лояльнее, но с 4.53.0 работает на всех регионах.
APP_VERSION = "4.53.0"
APP_VERSION_CODE = "15000"
APP_PLATFORM = "ios"
APP_DEVICE_MODEL = "iPhone17,1"
APP_TIMEZONE = "Europe/Moscow"
APP_GAID = "D4232F12-7C00-46EB-83A9-4BC6C23B988A"
