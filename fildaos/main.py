#!/usr/bin/python3
welcome = "Welcome to \033[32mFildaOS\033[0m";
clear = "\033[H\033[2J";
print(clear+welcome);
while True:
    com = input("> ").split();
    if (not com):
        pass;
    elif (com[0] == "help"):
        print("all commands of fildaos: ");
        print("  1. help - show help menu");
        print("  2. fifetch - show info of system");
        print("  3. echo - output the text in terminal");
        print("  4. exit - exit");
    elif (com[0] == "fifetch"):
        print("name: fildaos");
        print("version: 1.0");
        print("developer: luxidev");
        print("release date: 2025-07-24");
    elif (com[0] == "echo"):
        print(" ".join(com[1:]));
    elif (com[0] == "exit"):
        exit();
    else:
        print("Bad command.");
