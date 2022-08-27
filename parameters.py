# Screen resolution
WIDTH = 1280
HEIGHT = 720
CAPTURE_OFFSET = 30

# Edge detection
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 50

# Data logging (note: all keys have to be uppercase)
KEYS_TO_LOG = ["W", "A", "S", "D", "KEY.SPACE", "KEY.SHIFT", "KEY.CTRL_L"]
PLAYER_STATS_PTRS = {
    "HP": [0x100, "int"],
    "Armor": [0x117CC, "int"],
    "Helmet": [0x117C0, 'bool'],
    "Weapon": [12040, "int"],
    "Team": [0xF4, "int"],
    "EyeAngleX": [0x117D0, "float"],
    "EyeAngleY": [0x117D4, "float"]
}
RESIZED_WIDTH = 80
RESIZED_HEIGHT = 60

# ML parameters
LEARNING_RATE = 1e-3
EPOCH=8
MODEL_NAME = "csgo-{}-{}-{}epochs-{}.model".format("walk", "alexnetv2", EPOCH, 1)