#!/usr/bin/env python
#-*-coding: utf-8

# Serdar Ipsum Generator

import sys, random, argparse

if __name__ != '__main__':
    print("Not a module!")
    sys.exit(1)

parser = argparse.ArgumentParser(description='To tell me how many verses or words')
parser = argparse.ArgumentParser(description='To tell me if it is a poem or paragraph')

parser.add_argument('length', type=int, help='Verses count to generate')
parser.add_argument('type', type=str, help='Type')
args = parser.parse_args()

PLENGTH = args.length
PTYPE = args.type

song_file = "songs.txt"
MIN_WORDS_PER_LINE = 3
MAX_WORDS_PER_LINE = 6
words = []

global word_count
word_count = 0

with open(song_file) as f:
    lines = f.readlines()

for line in lines:
    line = line.replace("\n", "")
    if line != "-----":
        words_per_line = line.split(' ')
        for word in words_per_line:
            word.replace("\n", "")
            words.append(word.lower())

def generate_a_line():
    random_line_length = random.randint(MIN_WORDS_PER_LINE, MAX_WORDS_PER_LINE)
    song_line = ""
    for i in range(0, random_line_length):
        random_word = random.randint(0, len(words) - 1)
        song_line += words[random_word] + " "
    global word_count
    word_count += random_line_length
    return song_line[:1].upper() + song_line[1:len(song_line) - 1]


def generate_verse():
    for i in range(0, 4):
        print(generate_a_line())
    print(" ")

def generate_paragraph():
    song_paragrapgh = ""
    for i in range(0,PLENGTH):
        song_paragrapgh += generate_a_line() + '. '
        global word_count
        i += word_count
        if i >= PLENGTH:
            break
    return song_paragrapgh


def generate_song():
    if PTYPE == "P":
        for i in range(0, PLENGTH):
            generate_verse()
    elif PTYPE == "p":
        print(generate_paragraph())

def song_title():
    title = words[random.randint(0, len(words) - 1)] + " " + words[random.randint(0, len(words) - 1)] + " " + words[random.randint(0, len(words) - 1)]
    return title.upper()


print(">> Serdar Ipsum Generator\n")
print(song_title() + "\n")
generate_song()
print(" - Serdar Ortaç\n")