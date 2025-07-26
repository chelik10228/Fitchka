#!/usr/bin/python3
import time;
import random;
import os;
import pygame;
import subprocess;
pygame.mixer.init();
os.chdir("ptichkaos");

clear = "\033[H\033[2J";
welcome = "Welcome to \033[31mP\033[32mt\033[33mi\033[34mc\033[35mh\033[36mk\033[37ma\033[31mO\033[32mS\033[0m";
print(clear+welcome);
while True:
    com = input("# ").split();
    if not com:
        pass;
    elif (com[0] == "help"):
        print("a menu of the all commands:");
        print("  1. help - this menu");
        print("  2. sleep - the time sleep");
        print("  3. pifetch - the information of system");
        print("  4. date - showing date and time");
        print("  5. rnum - outputing the random number 1 to 10 for test");
        print("  6. echo - outputing the text on screen");
        print("  7. clear - clear the terminal");
        print("  8. calc - calculator");
        print("  9. music-test - play the test of music");
        print("  10. music-play - play the music");
        print("  11. music-list - show all musics");
        print("  12. music-pause - pause the music");
        print("  13. music-unpause - unpause the music");
        print("  14. music-stop - stop the music");
        print("  15. ls - show files in vdisk (folder)");
        print("  16. cd - go to folder");
        print("  17. write - write text in file, using: 'write text'");
        print("  18. over-write - the overwriting file, using: 'over-write file_name'");
        print("  19. rm - remove file");
        print("  20. ptichkaweb - run ptichka web browser");
        print("  21. ptichkampv - the video player using default mpv");
        print("  22. lsvdk - show all folders and all files");
        print("  23. exit - exit from ptichkaos");
    elif (com[0] == "sleep"):
        sleep = input("Enter the number for time sleep: ");
        time.sleep(int(sleep));
    elif (com[0] == "pifetch"):
        print(" _   | Name: PtichkaOS");
        print("('=  | Version: 1.3");
        print("/_)  | Lang: Python 3");
        print("/||  | Developer: Luxidev");
        print("     | Release date: 2025-07-24\n");
        print("     \033[41m  \033[42m  \033[43m  \033[44m  \033[45m  \033[46m  \033[47m  \033[0m");
    elif (com[0] == "exit"):
        exit();
    elif (com[0] == "date"):
        print(time.ctime());
    elif (com[0] == "rnum"):
        print(random.randint(1, 10));
    elif (com[0] == "echo"):
        print(" ".join(com[1:]));
    elif (com[0] == "clear"):
        print(clear, end="\r");
    elif (com[0] == "calc"):
        print("Welcome to Calculator 1.0!");
        print("Enter 'exit' for exit from calculator"); 
        num1 = int(input("Enter the first number: "));
        num2 = int(input("Enter the second number: ")); 
        oper = input("Enter the operation (+,-,*,/): ");
        if oper == "+":
            print(num1+num2);
        elif oper == "-":
            print(num1-num2);
        elif oper == "*":
            print(num1*num2);
        elif oper == "/":
            print(num1/num2);
    elif (com[0] == "music-test"):
        pygame.mixer.music.load("music/test.mp3");
        pygame.mixer.music.play();
        print("Playing the 'test.mp3'");
    elif (com[0] == "music-play"):
        pygame.mixer.music.load("".join(com[1:]));
        pygame.mixer.music.play();
        print("Playing the", "".join(com[1:]));
    elif (com[0] == "music-list"):
        os.system("find * -name '*.mp3'");
    elif (com[0] == "music-pause"):
        pygame.mixer.music.pause();
        print("Paused the music");
    elif (com[0] == "music-unpause"):
        pygame.mixer.music.unpause();
        print("Unpaused the music");
    elif (com[0] == "music-stop"):
        pygame.mixer.music.stop();
        print("Stopped the music");
    elif (com[0] == "ls"):
        os.system("dir");
    elif (com[0] == "cd"):
        os.chdir("".join(com[1:]));
    elif (com[0] == "cat"):
        f = open("".join(com[1:]), "r");
        print(f.read());
    elif (com[0] == "write"):
        file = input("Enter the filename: ");
        f = open(file, "a");
        f.write(" ".join(com[1:]));
    elif (com[0] == "over-write"):
        f = open("".join(com[1:]), "w");
        f;
    elif (com[0] == "rm"):
        if os.path.exists("".join(com[1:])):
            os.remove("".join(com[1:]));
        else:
            print("The file does not exist");
    elif (com[0] == "ptichkaweb"):
        subprocess.run(["xterm", "./ptichkaweb"]);
    elif (com[0] == "ptichkampv"):
        subprocess.run(["mpv", "".join(com[1:])]);
    elif (com[0] == "lsvdk"):
        print("Virtual Disk: vdisk/");
        print("Files & Folders: ");
        os.system("dir");
        print("Folder music: ");
        os.system("dir music/");
        print("Folder video:");
        os.system("dir video/");
    else:
        print("Bad command.");
