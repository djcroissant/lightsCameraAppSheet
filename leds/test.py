import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 360)
#pixels[15]=(255,255,255)
pixels.fill((255, 255, 255))