import sys
import random
import time
import argparse
from typing import List, Tuple

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
NOTES_NO_SHARP = [note for note in NOTES if len(note) == 1]

def parse_args() -> Tuple[List[str], float]:
    """Parses command line arguments and returns the selected notes and interval."""
    parser = argparse.ArgumentParser(description="Guitar note practice helper.")
    parser.add_argument(
        "--time", 
        type=float, 
        default=1.0, 
        help="Time between prompts in seconds (default: 1.0)"
    )
    parser.add_argument(
        "--no-sharps", 
        action="store_true", 
        help="Use only natural notes (no sharps)"
    )
    
    args = parser.parse_args()
    
    using_notes = NOTES_NO_SHARP if args.no_sharps else NOTES
    return using_notes, args.time

def print_note(note: str) -> None:
    """Prints the note with a simple border."""
    print("====================")
    print(f"\t\t{note}")

def loop() -> None:
    """Main loop for displaying random notes at set intervals."""
    using_notes, using_time = parse_args()
    
    print("~~~~~~~~~~~~Settings~~~~~~~~~~~~")
    print(f"Notes Selected: {using_notes}")
    print(f"Time Between: {using_time}s")
    print("Press Ctrl+C to stop.")
    
    try:
        while True:
            random_note = random.choice(using_notes)
            print_note(random_note)
            time.sleep(using_time)
    except KeyboardInterrupt:
        print("\nPractice session ended.")

def main() -> None:
    loop()

if __name__ == "__main__":
    main()
