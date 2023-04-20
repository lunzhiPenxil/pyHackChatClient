import os
import importlib
import webview
# pillow
from PIL import Image

url = 'https://beta.hack.chat/'
title = 'HackChat'

if __name__ == '__main__':
    if '_PYIBoot_SPLASH' in os.environ and importlib.util.find_spec("pyi_splash"):
        import pyi_splash
        pyi_splash.close()
    webview.create_window(
        title=title,
        url=url,
        background_color='#2A2A49'
    )
    webview.start(
        private_mode=False
    )
