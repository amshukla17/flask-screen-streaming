import time
from base_camera import BaseCamera
import tempfile
import pyscreenshot as ImageGrab


class Camera(BaseCamera):
    """An emulated camera implementation that streams a repeated sequence of
    screenshots."""

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            screen = ImageGrab.grab()
            screen.save('latest.JPEG', format='JPEG')
            with open('latest.JPEG', 'rb') as fp:
                yield fp.read()

