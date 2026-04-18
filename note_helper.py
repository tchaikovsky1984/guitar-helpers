import sys
import random
import time

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
notes_no_sharp = list(filter(lambda note: len(note) == 1, notes))

def define_vars():
    using_notes = None #notes to be used
    using_time = None #time between prompt (in seconds)
    return [using_notes, using_time]

def parse_args():
    using_notes, using_time = define_vars()
    args = sys.argv
    time_flag = False
    if(len(args) == 1):
        using_notes = notes
        using_time = 1
    else:
        for arg in args[1:]:
            if(time_flag):
                try:
                    using_time = float(arg)
                except ValueError as ve:
                    print("Time not set: Pass time in seconds after --time")
                    exit(1)
                time_flag = False
                continue
            if(arg == '--time'):
                time_flag = True
                continue
            if(arg == '--no-sharps'):
                using_notes = notes_no_sharp
        if(using_notes == None):
            using_notes = notes
        if(using_time == None):
            using_time = float(1)
    return [using_notes, using_time]

def print_note(note: str):
    print("====================", end = "\n")
    print("\t\t" + note, end = "\n")
    return

def loop():
    using_notes, using_time = parse_args()
    print("~~~~~~~~~~~~Settings~~~~~~~~~~~~")
    print(f"Notes Selected: {using_notes}")
    print(f"Time Between: {using_time}")
    while(True):
        random_idx = random.randint(0, len(using_notes) - 1)
        random_note = using_notes[random_idx]
        print_note(random_note)
        time.sleep(using_time)

def main():
    loop()

if __name__ == "__main__":
    main()
