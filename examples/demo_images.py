"""SSD1309 demo (images)."""
from time import sleep
from machine import Pin, I2C  # type: ignore
from ssd1309enh import SSD1309


def test():
    """Test code."""
    #spi = SPI(1, baudrate=10000000, sck=Pin(14), mosi=Pin(13))
    #display = SSD1309(spi, dc=Pin(4), cs=Pin(5), rst=Pin(2))
    i2c = I2C(1, freq=400000, scl=Pin(7), sda=Pin(6))  # Pico I2C bus 1
    display = SSD1309(i2c=i2c)

    display.draw_bitmap("images/eyes_128x42.mono", 0, display.height // 2 - 21,
                        128, 42)
    display.present()
    sleep(5)

    display.clear_buffers()
    display.draw_bitmap("images/doggy_jet128x64.mono", 0, 0, 128, 64,
                        invert=True)
    display.present()
    sleep(5)

    display.clear_buffers()
    display.draw_bitmap("images/invaders_48x36.mono", 0, 14, 48, 36, rotate=90)
    display.draw_bitmap("images/invaders_48x36.mono", 40, 14, 48, 36)
    display.draw_bitmap("images/invaders_48x36.mono", 92, 14, 48, 36,
                        rotate=270)
    display.present()

    sleep(10)
    display.cleanup()
    print('Done.')


test()
