# Import required libraries
import os
import random
import shutil
import ntpath
import subprocess
import sys

# Function to get absolute path to resources (works for both development and PyInstaller)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Function to process each music category
def process_category(category_folder, names_list, category_type, output_folder, rom_base_name, pcmExt):
    # Collect all PCM files in the category
    all_files = []
    for root, _, files in os.walk(category_folder):
        for f in files:
            if f.lower().endswith(pcmExt.lower()):
                all_files.append(os.path.join(root, f))
    
    if not all_files:
        print(f"ERROR: No files found in {category_folder}")
        return
    
    # Shuffle files
    random.shuffle(all_files)
    
    # Process each name in the list
    for i, name in enumerate(names_list):
        if i >= len(all_files):
            print(f"WARNING: More names than files in {category_folder}")
            break
            
        src = all_files[i]
        filename = os.path.basename(src)
        dest_name = f"{rom_base_name}-{name}"
        dest_path = os.path.join(output_folder, dest_name)
        
        # Copy file
        shutil.copy(src, output_folder)
        # Rename copied file
        os.rename(os.path.join(output_folder, filename), dest_path)
        
        # Log result
        log_msg = f"{category_type} Music - {dest_name} is {filename}\n"
        output_log = os.path.join(output_folder, "Output.txt")
        with open(output_log, "a", encoding="utf-8") as f:
            f.write(log_msg)
        print(f"Copied {filename}, renamed to {dest_name}!")

# Main settings
pcmExt = ".pcm"

# Get ROM path
rompath = input("Please drag your ROM file here:\n").strip('"')
rombase = ntpath.basename(rompath)
rom_base_name = os.path.splitext(rombase)[0]
rom_ext = os.path.splitext(rombase)[1]

# Configure paths
root_dir = os.getcwd()
outputFolder = os.path.join(root_dir, rom_base_name)

print(f"Outputting to: {outputFolder}")

# Clean output folder if exists
if os.path.exists(outputFolder):
    shutil.rmtree(outputFolder)
os.makedirs(outputFolder)
shutil.copy(rompath, outputFolder)

# Get randomization type
rType = input("Select randomization type:\n"
              "1. Categorized\n"
              "2. Chaos\n").strip()

# Process Categorized mode
if rType == "1":
    # Load name lists using resource_path
    config_dir = resource_path("Configs")
    ff6_config_dir = os.path.join(config_dir, "Final Fantasy VI")
    
    # Read configuration files
    with open(os.path.join(ff6_config_dir, "Battle.txt"), 'r', encoding='utf-8') as f:
        battle_names = [line.strip() for line in f.readlines()]
    with open(os.path.join(ff6_config_dir, "Boss.txt"), 'r', encoding='utf-8') as f:
        boss_names = [line.strip() for line in f.readlines()]
    with open(os.path.join(ff6_config_dir, "Character.txt"), 'r', encoding='utf-8') as f:
        char_names = [line.strip() for line in f.readlines()]
    with open(os.path.join(ff6_config_dir, "Event.txt"), 'r', encoding='utf-8') as f:
        event_names = [line.strip() for line in f.readlines()]
    with open(os.path.join(ff6_config_dir, "Field.txt"), 'r', encoding='utf-8') as f:
        field_names = [line.strip() for line in f.readlines()]
    
    # Configure category paths using resource_path
    catInput = resource_path("Music Categories")
    charFolder = os.path.join(catInput, "Character")
    battleFolder = os.path.join(catInput, "Battle")
    fieldFolder = os.path.join(catInput, "Field")
    eventFolder = os.path.join(catInput, "Event")
    bossFolder = os.path.join(catInput, "Boss")
    
    # Process each category
    process_category(charFolder, char_names, "Character", outputFolder, rom_base_name, pcmExt)
    process_category(battleFolder, battle_names, "Battle", outputFolder, rom_base_name, pcmExt)
    process_category(fieldFolder, field_names, "Field", outputFolder, rom_base_name, pcmExt)
    process_category(eventFolder, event_names, "Event", outputFolder, rom_base_name, pcmExt)
    process_category(bossFolder, boss_names, "Boss", outputFolder, rom_base_name, pcmExt)

# Process Chaos mode
elif rType == "2":
    musiccfg = input("Please drag your MSU-1 configuration file here:\n").strip('"')
    with open(musiccfg, 'r', encoding='utf-8') as f:
        names = [line.strip() for line in f.readlines()]
    
    # Collect all PCM files from all categories
    all_files = []
    catInput = resource_path("Music Categories")
    for root, _, files in os.walk(catInput):
        for f in files:
            if f.lower().endswith(pcmExt.lower()):
                all_files.append(os.path.join(root, f))
    
    if not all_files:
        print("ERROR: No PCM files found in Music Categories!")
    else:
        random.shuffle(all_files)
        for i, name in enumerate(names):
            if i >= len(all_files):
                print("WARNING: More names than available files")
                break
                
            src = all_files[i]
            filename = os.path.basename(src)
            dest_name = f"{rom_base_name}-{name}"
            dest_path = os.path.join(outputFolder, dest_name)
            
            shutil.copy(src, outputFolder)
            os.rename(os.path.join(outputFolder, filename), dest_path)
            
            log_msg = f"{dest_name} is {filename}\n"
            output_log = os.path.join(outputFolder, "Output.txt")
            with open(output_log, "a", encoding="utf-8") as f:
                f.write(log_msg)
            print(f"Copied {filename}, renamed to {dest_name}!")

# Apply IPS patch if requested
ipsQ = input("\nApply an IPS patch to the ROM? (y/n): ").strip().lower()
if ipsQ == "y":
    # Use resource_path to locate patch
    ipsP = resource_path(os.path.join("Patches", "Final Fantasy VI.ips"))
    rom_target = os.path.join(outputFolder, rombase)
    
    if os.path.exists(ipsP) and os.path.exists(rom_target):
        try:
            # Use resource_path to find liteips.exe
            liteips_exe = resource_path("liteips.exe")
            
            if os.path.exists(liteips_exe):
                subprocess.call([liteips_exe, "-f", ipsP, rom_target])
                print("Patch applied successfully!")
            else:
                print("ERROR: liteips.exe not found!")
        except Exception as e:
            print(f"Error applying patch: {str(e)}")
    else:
        print("ERROR: Patch file or ROM not found!")

input("\nPress Enter to exit.")
