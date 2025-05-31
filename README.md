# Final Fantasy VI MSU-1 Music Randomizer

Randomizes the music for Final Fantasy VI (SNES) using MSU-1 technology. Creates a custom playable ROM with shuffled music tracks from your collection.

## Requirements
- Python 3.7-3.11 (64-bit recommended)
- Original FF6 ROM (**.smc** format)
- SNES emulator with MSU-1 support (Snes9x, bsnes)

## Music Preparation Guide
- Step 1: Convert your music
Place your music files (MP3) in converter/Music/

Run converter.exe

Collect generated .pcm files from output folder

- Step 2: Categorize PCM files
Organize your .pcm files into these category folders with minimum requirements:

Category	Folder Path	Min Files:
- Battle	Music Categories/Battle	- 1
- Boss	Music Categories/Boss	- 7
- Character	Music Categories/Character	- 14
- Events	Music Categories/Event	- 25
- Field	Music Categories/Field	- 22

Important: Each category must meet its minimum file requirement!

# Randomization Process
Run FF6 Music Randomizer.py

When prompted, drag and drop your FF6 ROM (.smc file) into the window

Select randomization type:

1. Categorized (shuffles within categories)

Let the program process (takes 1-3 minutes)

When asked to apply IPS patch, press Y then Enter

Press Enter to exit when completed

# Finding Your Randomized ROM
Your customized ROM will be at:
[Randomizer Folder]/[Your ROM Name]/

Example:
FFVI-Music-Randomizer/Final Fantasy VI/

Playing Your Randomized Game
Open your SNES emulator

Load the ROM from the new folder

Enable MSU-1 audio in emulator settings

Enjoy your new musical experience!

## Troubleshooting
- "ERROR: No files found in...":

Verify you have enough PCM files in each category

Check files have .pcm extension (case insensitive)

- Patch application fails:

Ensure original ROM is clean (unmodified)

- Verify ROM has .smc extension

Try different emulator if issues persist

- Python errors:

Reinstall Python and check "Add to PATH"

Use Python 3.7-3.11 (64-bit recommended)

Run script from command line to see full error:

bash
python "FF6 Music Randomizer.py"
Tips
Backup your music collection - original files won't be modified

For best results, use high-quality source audio (44.1kHz recommended)

Chaos mode requires an MSU-1 config file (auto-generated if missing)

Check Output.txt in your ROM folder for track mapping details


## Have fun! 👌
