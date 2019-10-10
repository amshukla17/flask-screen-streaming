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
            with tempfile.TemporaryFile('rwb') as fp:
                screen = ImageGrab.grab()
                screen.save(fp, format='JPEG')
                fp.seek(0)
                yield fp.read()

