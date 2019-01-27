#!/usr/bin/env python3
import random
def generate_bits():
    return random.randint(0,1)

def main():
    while True:
        r = generate_bits()
        print(str(r), end='\r')

main()
