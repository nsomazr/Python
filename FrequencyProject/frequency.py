from argparse import ArgumentParser
from math import  log2
import sys


def get_pitch(freq, a4=440.0):
        number = round(12*(log2(freq / a4) % 1))
        pitches = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        return pitches.pop(number)


def get_octave(freq, a4 = 440.0):
    return round((round(12*(log2(freq / a4))) + 57) // 12)


def check_intonation(freq, a4=440.0):
    return round(1200*(log2(freq / a4)) + 50) % 100 - 50


def who_can_hear(freq, a4=440.0):
    if 20 <= freq <= 20_000:
        return "human"
    elif 0.5 <= freq < 20:
        return "pegeon"
    elif 20_000 < freq <= 44_000:
        return "dog"
    elif 44_000 < freq <= 77_000:
        return "cat"
    elif 77_000 < freq < 150_000:
        return "porpoise"
    elif 150_000 <freq <= 300_000:
        return "greater wax moth"
    else:
        return None


def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("freq", type=float, help="a frequency in Hz")
    parser.add_argument("-a4", type=float, default=440.0, help="frequency to use for A4")
    args = parser.parse_args(arglist)
    return args


def main(freq, a4=440.0):
    print("{} Hz is {}{}.".format(freq, get_pitch(freq, a4), get_octave(freq, a4)))
    if freq < 440.0:
        print("It is {} cents flat if A4={} Hz ".format(check_intonation(freq, a4), a4))
    elif freq > 440.0:
        print("It is {} cents sharp if A4={} Hz ".format(check_intonation(freq, a4), a4))
    else:
        print("It is in tune if A4={} Hz ".format(a4))

    if who_can_hear(freq) is None:
        print("It is within the hearing range of a {}".format(who_can_hear(freq)))
    else:
        print("I don't know a species that can hear this frequency")


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args.freq, a4=args.a4)




