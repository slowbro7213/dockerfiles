import re


def hex_str_to_bytes(hex_str):
    hex_str = hex_str.strip()
    
    if re.search("\s", hex_str):
        hex_str = re.sub(r"\s+", " ", hex_str)
    return bytearray.fromhex(hex_str)
