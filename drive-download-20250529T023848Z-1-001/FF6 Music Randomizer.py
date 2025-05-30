# Import required libraries
import os
import random
import shutil
import ntpath
import subprocess

# Reads the Filenames list
rompath = raw_input ("Please drag your ROM into this window:\n").strip('\"')
rombase = ntpath.basename(rompath)
rom = os.path.splitext(rombase)
pcmExt = ".pcm"
configpath = "Configs"
# Set the root path
root = os.curdir

# Path to copy files from
inputFolder = os.path.join(root, "Music")

# Path to copy files to
outputFolder = os.path.join(root, rom[0])
print "Outputting to: " + outputFolder.strip(".")

# Store the copied file names here
copiedFiles = []
rType = input ("Please select what type of Randomizer you would like:\n"
                   "1. Categorized\n"
                   "2. Chaos\n")
catInput = "Music Categories"

# Clear the output folder first
for dir in os.listdir(os.curdir):
    if os.path.exists(outputFolder):
        shutil.rmtree(outputFolder)
#Create the output folder
os.makedirs(outputFolder)
shutil.copy(rompath, outputFolder)

if rType == 1:
    battle_file = open(os.path.join (configpath, "Final Fantasy VI\Battle.txt"))
    battle_names = list(line.rstrip('\n') for line in battle_file.readlines())
    battle_file.close()
    boss_file = open(os.path.join (configpath, "Final Fantasy VI\Boss.txt"))
    boss_names = list(line.rstrip('\n') for line in boss_file.readlines())
    boss_file.close()
    char_file = open(os.path.join (configpath, "Final Fantasy VI\Character.txt"))
    char_names = list(line.rstrip('\n') for line in char_file.readlines())
    char_file.close()
    event_file = open(os.path.join (configpath, "Final Fantasy VI\Event.txt"))
    event_names = list(line.rstrip('\n') for line in event_file.readlines())
    event_file.close()
    field_file = open(os.path.join (configpath, "Final Fantasy VI\Field.txt"))
    field_names = list(line.rstrip('\n') for line in field_file.readlines())
    field_file.close()
    inputFolder = os.path.join(root, "Music")
    battleFolder = os.path.join(catInput, "Battle")
    charFolder = os.path.join(catInput, "Character")
    fieldFolder = os.path.join(catInput, "Field")
    eventFolder = os.path.join(catInput, "Event")
    bossFolder = os.path.join(catInput, "Boss")
    
    for root, dirs, files in os.walk(charFolder):

        for name in char_names:
            # Validation flag
            validFile = False

            # Validate the file that will be picked
            while not validFile:

                # Get a random index
                index = random.choice(range(len(files)))

                # Get the path and file from the picked index
                path = os.path.join(root, files[index])
                file = files[index]


                # It must be a file and not be already picked
                if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                    # File is valid
                    validFile = True

                    # Copy the name to the new list
                    copiedFiles.append(file)

                    # Copy the file to the output folder
                    shutil.copy(path, outputFolder)

                    # Rename the file
                    os.chdir(outputFolder)
                    print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                    f = open("Output.txt", "a+")
                    for i in range(1):                
                        f.write("Character Music - "+rom[0]+"-"+name + " is " + file + "\r\n")
                    f.close()
                    os.rename(file, rom[0]+"-"+name)
                    msu = open(rom[0]+'.msu', 'w')
                    os.chdir("..")
                
    for root, dirs, files in os.walk(battleFolder):

        for name in battle_names:
            # Validation flag
            validFile = False

            # Validate the file that will be picked
            while not validFile:

                # Get a random index
                index = random.choice(range(len(files)))

                # Get the path and file from the picked index
                path = os.path.join(root, files[index])
                file = files[index]


                # It must be a file and not be already picked
                if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                    # File is valid
                    validFile = True

                    # Copy the name to the new list
                    copiedFiles.append(file)

                    # Copy the file to the output folder
                    shutil.copy(path, outputFolder)

                    # Rename the file
                    os.chdir(outputFolder)
                    print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                    f = open("Output.txt", "a+")
                    for i in range(1):                
                        f.write("Battle Music - "+rom[0]+"-"+name + " is " + file + "\r\n")
                    f.close()
                    os.rename(file, rom[0]+"-"+name)
                    msu = open(rom[0]+'.msu', 'w')
                    os.chdir("..")

    for root, dirs, files in os.walk(fieldFolder):

        for name in field_names:
            # Validation flag
            validFile = False

            # Validate the file that will be picked
            while not validFile:

                # Get a random index
                index = random.choice(range(len(files)))

                # Get the path and file from the picked index
                path = os.path.join(root, files[index])
                file = files[index]


                # It must be a file and not be already picked
                if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                    # File is valid
                    validFile = True

                    # Copy the name to the new list
                    copiedFiles.append(file)

                    # Copy the file to the output folder
                    shutil.copy(path, outputFolder)

                    # Rename the file
                    os.chdir(outputFolder)
                    print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                    f = open("Output.txt", "a+")
                    for i in range(1):                
                        f.write("Field Music - "+rom[0]+"-"+name + " is " + file + "\r\n")
                    f.close()
                    os.rename(file, rom[0]+"-"+name)
                    msu = open(rom[0]+'.msu', 'w')
                    os.chdir("..")

    for root, dirs, files in os.walk(eventFolder):

        for name in event_names:
            # Validation flag
            validFile = False

            # Validate the file that will be picked
            while not validFile:

                # Get a random index
                index = random.choice(range(len(files)))

                # Get the path and file from the picked index
                path = os.path.join(root, files[index])
                file = files[index]


                # It must be a file and not be already picked
                if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                    # File is valid
                    validFile = True

                    # Copy the name to the new list
                    copiedFiles.append(file)

                    # Copy the file to the output folder
                    shutil.copy(path, outputFolder)

                    # Rename the file
                    os.chdir(outputFolder)
                    print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                    f = open("Output.txt", "a+")
                    for i in range(1):                
                        f.write("Event Music - "+rom[0]+"-"+name + " is " + file + "\r\n")
                    f.close()
                    os.rename(file, rom[0]+"-"+name)
                    msu = open(rom[0]+'.msu', 'w')
                    os.chdir("..")

    for root, dirs, files in os.walk(bossFolder):

        for name in boss_names:
            # Validation flag
            validFile = False

            # Validate the file that will be picked
            while not validFile:

                # Get a random index
                index = random.choice(range(len(files)))

                # Get the path and file from the picked index
                path = os.path.join(root, files[index])
                file = files[index]


                # It must be a file and not be already picked
                if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                    # File is valid
                    validFile = True

                    # Copy the name to the new list
                    copiedFiles.append(file)

                    # Copy the file to the output folder
                    shutil.copy(path, outputFolder)

                    # Rename the file
                    os.chdir(outputFolder)
                    print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                    f = open("Output.txt", "a+")
                    for i in range(1):                
                        f.write("Boss Music - "+rom[0]+"-"+name + " is " + file + "\r\n")
                    f.close()
                    os.rename(file, rom[0]+"-"+name)
                    msu = open(rom[0]+'.msu', 'w')
                    os.chdir("..")

# Read the files in the directory
else:
    if rType == 2:
        musiccfg = raw_input ("Please drag your MSU-1 configuration text file into this window:\n").strip('\"')
        names_file = open(musiccfg)
        names = list(line.rstrip('\n') for line in names_file.readlines())
        names_file.close()
        for root, subdirs, files in os.walk("Music Categories"):

            for name in names:
                # Validation flag
                validFile = False

                # Validate the file that will be picked
                while not validFile:

                    # Get a random index
                    index = random.choice(range(len(files)))

                    # Get the path and file from the picked index
                    path = os.path.join(root, files[index])
                    file = files[index]


                    # It must be a file and not be already picked
                    if os.path.isfile(path) and file not in copiedFiles and file.endswith(pcmExt):
                        # File is valid
                        validFile = True
    
                        # Copy the name to the new list
                        copiedFiles.append(file)

                        # Copy the file to the output folder
                        shutil.copy(path, outputFolder)

                        # Rename the file
                        os.chdir(outputFolder)
                        print "Copied " + file + ", renamed it to " + rom[0]+"-"+name + "!"
                        f = open("Output.txt", "a+")
                        for i in range(1):                
                            f.write(rom[0]+"-"+name + " is " + file + "\r\n")
                        f.close()
                        os.rename(file, rom[0]+"-"+name)
                        msu = open(rom[0]+'.msu', 'w')
                        os.chdir("..")

ipsQ = raw_input ("\nWould you like to apply an IPS patch to your ROM? y/n: ")

if ipsQ == "y" or ipsQ == "Y":
    ipsP = "Patches\Final Fantasy VI.ips"
    subprocess.call(["liteips.exe", "-f", ipsP, outputFolder+"/"+rom[0]+rom[1]])
scExit = raw_input ("\nPlease press enter to quit.")


