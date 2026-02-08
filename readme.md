# MicroPython SPI & I2C ADVANCED Display Driver for SSD1309 monochrome OLED

This repository is based on the great work of [rdagger/micropython-ssd1309](https://github.com/rdagger/micropython-ssd1309) !

![HS242L03 ssd1309 2.42" wired over I2C to a Pico](docs/_static/ssd1309-example.jpg)

The library is truly full of features, it can: 

* Work over SPI and I2C
* draw lines, shapes, 
* draw text with on the fly font loading, 
* draw sprites,
* draw images,  
* Scroll content (hardware support).

Features have a cost, the library make 38 Ko in size (44.8 Ko with font support)

All code is documented and there are demo examples. This version of the library have been reorganiszed and and main class renamed SSD1309. Code and examples have been tested with Hardware I2C on Raspberry-Pi Pico.

## about fonts
Sample XGLCD fonts are included in the fonts folder.  Additional fonts can generated from TTF fonts using a free utility called MikroElektronika [GLCD Font Creator](https://www.mikroe.com/glcd-font-creator).

The folder [fonts/](fonts/) contains font files that can be copied on the MicroPython plateform (preference in a `fonts` subfolder). 

Remarks: 

* fonts are c files parsed on the fly by the library to creates a binary representation in memory.
* fonts file may be very large in size!

## about images

The library can load monochrome images at monoHMSB format. The library contains several samples images are available in the [images/](images/) folder.

The [utils/img2monoHMSB.py](utils/img2monoHMSB.py) utility converts images in common formats such as JPEG and PNG to monoHMSB.

# Library

The library must be copied on the MicroPython board before using the examples.

On a WiFi capable plateform:

```
>>> import mip
>>> mip.install("github:mchobby/micropython-ssd1309")
```

Or via the mpremote utility :

```
mpremote mip install github:mchobby/micropython-ssd1309
```

## Fonts & images

Driver installation does not copy images or fonts files to your MicroPython plateform.

__You have to copy manually such ressources on purpose.__

# Wiring 
## I2C Wiring with Pico

![SSD1309 I2C to Pico](docs/_static/ssd1309-i2c-to-pico.jpg)

# Examples

## Demo Shapes
The [examples/demo_shape.py](examples/demo_shapes.py) script draw various shapes thank to the methods supported by the SSD1309. 

![Drawing shapes](docs/_static/demo_shapes.jpg)

## Demo Scroll Manual
The [examples/demo_scroll_manual.py](examples/demo_scroll_manual.py) script demonstrate the hardware scrolling. 

This update enables smooth, efficient scrolling with minimal processor usage—here's a short video from the demo.

The first part of the script make an image scrolling from left to right on the screen.
![hardware scrolling between left and right](docs/_static/demo_scroll_manual-00.jpg)

The second section of the script make the background montains scrolling under the space ship.

![hardware scrolling of montains](docs/_static/demo_scroll_manual-01.jpg)

https://github.com/user-attachments/assets/14209ff1-a0f7-4997-b1d5-76dab3f15c07

## Demo Scroll
The [examples/demo_scroll.py](examples/demo_scroll.py) script load a font draw text and graphical object THEN organise various scroll operation (including some Split Scroll).

## Demo Flip
The [examples/demo_flip.py](examples/demo_flip.py) script load a font and the a wifi image to display the following content and flip it over.

![demo_flip.py capture](docs/_static/demo_flip-00.jpg) ![demo_flip.py capture](docs/_static/demo_flip-01.jpg) 

## Demo fonts
The [examples/demo_fonts.py](examples/demo_fonts.py) script load several fonts and display text (with all the fonts together) on a single screen.

Load the following fonts:

* Bitstream_Vera35x32.c
* Bally7x9.c
* Robotron13x21.c
* Wendy7x8.c

## Demo Images
The [examples/demo_images.py](examples/demo_images.py) script load monochrome HMSB images and display them on the screen.

Load the following images:

* eyes_128x42.mono
* doggy_jet128x64.mono
* invaders_48x36.mono

## Demo Sprite
The [examples/demo_sprite.py](examples/demo_sprite.py) script load the `saucer_48x26.mono` monochrome HMSB image, wrap it into the `BouncingSprite` class then make it bouncing on the screen.

## Demo Bouncing Boxes
The [examples/demo_bouncing_boxes.py](examples/demo_bouncing_boxes.py) script shows several boxes in various size bouncing into the screen. 

# Ressources

* Tutorial about the original library on [Rototron website](https://www.rototron.info/projects/wi-fi-caller-id-blocking/). See also the [YouTube video](https://youtu.be/GhXtQNxpKeo)
* another [tutorial](https://www.rototron.info/projects/wi-fi-caller-id-blocking/) using the origial library. See also the attached [YouTube video](https://youtu.be/b63ZPafPQVM)

Hardware scrolling is now supported. This update enables smooth, efficient scrolling with minimal processor usage—here's a short video from the demo.

https://github.com/user-attachments/assets/14209ff1-a0f7-4997-b1d5-76dab3f15c07
