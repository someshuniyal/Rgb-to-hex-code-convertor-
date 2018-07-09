"""This module is to do the convertion of rgb to hex code"""
class convertion:
    def convertor(self,red,green,blue):
        hex_red=hex(red)[2:].upper()
        if len(hex_red)==1:
            hex_red="0"+hex_red
        hex_green=hex(green)[2:].upper()
        if len(hex_green)==1:
            hex_green="0"+hex_green
        hex_blue=hex(blue)[2:].upper()
        if len(hex_blue)==1:
            hex_blue="0"+hex_blue
        return "#{}{}{}".format(hex_red,hex_green,hex_blue)
