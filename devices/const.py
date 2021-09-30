#Common RestApi status values
API_RESPONSE_STATUS_OK = "ok"
API_RESPONSE_STATUS_FAIL = "false"
API_RESPONSE_STATUS_INVALID = "invalid_action_name"

#Common RestApi methods
API_METHOD_COMMON_GET_STATE = "get_state/"
API_METHOD_COMMON_SET_STATE = "set_state/"
API_METHOD_COMMON_GET_DEVICE_INFO = "get_device_info/"

#Device model
DEVICE_MODEL_DIM1S2 = "DIM1S2"
DEVICE_MODEL_GATE = "GATE"
DEVICE_MODEL_LED2S2 = "LED2S2"
DEVICE_MODEL_POWER = "POWER"
DEVICE_MODEL_R1S1 = "R1S1"
DEVICE_MODEL_R2S2 = "R2S2"
DEVICE_MODEL_RGBW = "RGBW"
DEVICE_MODEL_STR1S2= "STR1S2"
DEVICE_MODEL_SUN1 = "SUN1"

#Device state values
DEVICE_OFF = "off"
DEVICE_ON = "on"

#Device type
DEVICE_TYPE_DIM1S2 = 9
DEVICE_TYPE_GATE = 1
DEVICE_TYPE_LED2S2 = 7
DEVICE_TYPE_POWER = 0 #T0D0
DEVICE_TYPE_R1S1 = 8
DEVICE_TYPE_R2S2 = 4
DEVICE_TYPE_RGBW = 6
DEVICE_TYPE_STR1S2 = 2
DEVICE_TYPE_SUN1 = 10

#Device model dictionary, key: device type
DEVICES = {
    DEVICE_TYPE_GATE: DEVICE_MODEL_GATE,
    DEVICE_TYPE_STR1S2: DEVICE_MODEL_STR1S2,
    DEVICE_TYPE_R2S2: DEVICE_MODEL_R2S2,
    DEVICE_TYPE_RGBW: DEVICE_MODEL_RGBW,
    DEVICE_TYPE_LED2S2: DEVICE_MODEL_LED2S2,
    DEVICE_TYPE_R1S1: DEVICE_MODEL_R1S1,
    DEVICE_TYPE_DIM1S2: DEVICE_MODEL_DIM1S2,
    DEVICE_TYPE_SUN1: DEVICE_MODEL_SUN1
}

#Manufacturer info
MANUFACTURER_NAME = "F&F Filipowski Sp.j"

#F&F Fox device supporting platform
SUPPORTED_PLATFORM_LIGHT = "light"
SUPPORTED_PLATFORM_SWITCH = "switch"
SUPPORTED_PLATFORM_SENSOR = "sensor"
SUPPORTED_PLATFORM_COVER = "cover"
SUPPORTED_PLATFORM_GATE = "gate"

#Device platform map
DEVICE_PLATFORM = {
    DEVICE_TYPE_DIM1S2: SUPPORTED_PLATFORM_LIGHT,
    DEVICE_TYPE_LED2S2: SUPPORTED_PLATFORM_LIGHT,
    DEVICE_TYPE_RGBW: SUPPORTED_PLATFORM_LIGHT,
    DEVICE_TYPE_R1S1: SUPPORTED_PLATFORM_SWITCH,
    DEVICE_TYPE_R2S2: SUPPORTED_PLATFORM_SWITCH,
    DEVICE_TYPE_STR1S2: SUPPORTED_PLATFORM_COVER
}