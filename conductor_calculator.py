import pyconductor

preloaded_dict = pyconductor.load_test_values()

while True:
    print(
        "Welcome to the Conductor Calculator!\n"
        "A dictionary of sample materials at sample values to test out has been pre-loaded. "
        "To see it, type 'help'.\nThis will also list any custom materials that you have added "
        "to the dictionary using 'add'; they will be added to the end of the dictionary.\n\n"
        "To test your own custom material and values, enter 'add' to add it to the dictionary "
        "of materials.\nTo try a material, ensure it is available in the dictionary and type "
        "its name in the prompt below.\n\nTo exit, simply type 'quit'.\n")

    yes_or_no = "Please type/enter 'yes' or 'no', or simply 'y' or 'n'"
    main_prompt = input("Please input a material name or a command: ").lower()

    if main_prompt == "help":
        print("\nCurrently contains the following materials:\n")
        print(preloaded_dict.keys())
        print("\nType one of the provided material names when prompted.")

    elif main_prompt == "add":
        preloaded_dict.addmat()

    elif main_prompt == "quit":
        print("\nGoodbye!\n")
        quit()

    else:
        try:
            calculate_conductance(preloaded_dict[main_prompt])
            while True:
                again_prompt = input(
                    "Would you like to try another calculation? [Y]es or [N]o: ").lower()
                if again_prompt in ("y", "yes"):
                    break
                elif again_prompt in ("n", "no"):
                    print("\nGoodbye!\n")
                    quit()
                elif again_prompt == "":
                    print(yes_or_no)
                else:
                    print(f"I didn't quite understand what you meant by '{again_prompt}'...")
        except KeyError:
            if main_prompt == "":
                print("\nNo material specified.\nPlease enter a valid material name "
                      "listed in the 'help' command, or use 'add' to add your own.\n")
            else:
                print(f"\n{main_prompt} is not a valid material or command.\nPlease use a valid "
                      "material listed in the 'help' command, or use 'add' to add your own.\n")
