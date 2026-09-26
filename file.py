#!/usr/bin/env python3
import time
import os


def print_ascii_art():
    art = r"""
     /\_/\
    ( o.o )
     > ^ <
    /     \
   (       )
    """.strip("\n")
    print(art)


def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def main():
    slow_print("Привет, Аня!", 0.08)
    time.sleep(0.5)

    print_ascii_art()
    time.sleep(0.5)

    slow_print("\nТы только что запустила мой скрипт.", 0.05)
    time.sleep(0.5)
    slow_print("А значит...", 0.1)
    time.sleep(0.8)

    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.7)
    print()

    slow_print("\nТЫ ОФИЦИАЛЬНО МОЙ ДОЛЖНИК!", 0.03)
    print()
    slow_print("С тебя кофе ☕ (или пиво 🍺, я не придирчивая)")
    print()

if __name__ == "__main__":
    main()