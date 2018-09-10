from pyconductor import load_test_values, calculate_conductance


def conductance_calc():
    preloaded_dict = load_test_values()
    while preloaded_dict:
        print(
            "[1] - Show currently available materials in Material Dictionary\n"
            "[2] - Add a material (will not be saved upon restart)\n"
            "[3] - Quit\n"
            "To test the conductive properties of a material, simply type in its name.\n"
            "Otherwise, type the corresponding number for an option above.\n"
        )
        main_prompt = input(">>> ").lower()
        if main_prompt == "1":
            print(f"\nCurrently contains the following materials:\n{preloaded_dict.keys()}\n")
        elif main_prompt == "2":
            preloaded_dict.addmat()
        elif main_prompt == "3":
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
            except KeyError:
                if main_prompt == "":
                    print("\nNo material specified.\nPlease enter a valid material name "
                          "listed in option [1], or use option [2] to add your own.\n")
                else:   # TODO: add logic handling whether user wants to add missing material
                    print(f"\n{main_prompt} is not a valid material or command!\n")
            else:
                pass

if __name__ == "__main__":
    conductance_calc()
