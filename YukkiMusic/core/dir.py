#
# Copyright (C) 2021-2022 by DEVIL-BOTS@Github, < https://github.com/DEVIL-BOTS >.
#
# This file is part of < https://github.com/DEVIL-BOTS/Devil-X-Music > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DEVIL-BOTS/Devil-X-Music/blob/master/LICENSE >
#
# All rights reserved.

import os
import sys
from os import listdir, mkdir

from ..logging import LOGGER


def dirr():
    if "assets" not in listdir():
        LOGGER(__name__).warning(
            f"Assets Folder not Found. Please clone repository again."
        )
        sys.exit()
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
    for file in os.listdir():
        if file.endswith(".jpeg"):
            os.remove(file)
    if "downloads" not in listdir():
        mkdir("downloads")
    if "cache" not in listdir():
        mkdir("cache")
    LOGGER(__name__).info("Directories Updated.")
