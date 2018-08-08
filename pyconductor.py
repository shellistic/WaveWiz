from math import pi, sqrt


class MaterialDict(dict):

    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)

    def __repr__(self):
        return "MaterialDict object"

    def __str__(self):
        if len(self) == 0:
            return "empty material dictionary"
        else:
            return f"material dictionary containing {len(self)} material(s)"

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError(
                    f"update expected at most 1 arguments, received {len(args)}")
            other = dict(args[0])
            for key in other:
                self[key] = other[key]
        for key in kwargs:
            self[key] = kwargs[key]

    def count(self):
        return len(self)


preloaded_dict = MaterialDict(
    {
        "air": (1, 0, 1.00000037),
        "fresh water": (80, 5e-4, 0.999992),
        "sea water": (80, 3, 1),
        "ice": (3.5, 1e-5, 1),
        "clay": (20, 5, 1),
        "saturated sand": (30, 1e-4, 1),
        "barium titanate": (3279, 1e-6, 1),
        "cold rolled steel": (1, 1e-7, 100),
        "purified iron": (1, 1e-7, 5e3),
        "mu metal": (1, 1.6e6, 2e5),
        "2-81 permalloy": (1, 1e2, 1e6),
        "copper": (1, 5.96e7, 0.999994),
        "gold": (1, 4.1e7, 1),
        "aluminium": (1, 3.5e7, 1.000022),
        "tungsten": (1, 1.79e7, 1),
        "graphite": (12.5, 2e5, 1),
        "diamond": (7.5, 1e-13, 0.99999975),
        "silicon": (11.68, 1.56e-3, 1),
        "glass": (65, 1e-15, 1),
        "kiln dried wood": (4, 1e-15, 1.000000435),
        "ptfe": (2.1, 1e-25, 1)
    }
)


def main_funct(mat):
    """
    Takes a material as an argument;
    Prints the results of the defined equations based on operating frequency.
    """
    while True:
        try:
            freq = float(input(
                f"At what frequency (Hz) is {main_prompt} operating? "))
        except ValueError:
            print("Please type in only numbers for operating frequency...")
        else:
            break

    eo = 8.854 * 10 ** -12
    uo = 1.26 * 10 ** -6
    w = 2 * pi * freq * mat[0] * eo
    test = mat[1] / w
    if test == 0:
        alpha = 0
        beta = (w / (sqrt(uo * mat[2] * eo * mat[0])))
        nc = ((mat[2] * uo) / (eo * mat[0]))
        up = (1 / (mat[0] * eo * mat[2] * uo))
        lam = float(up / freq)
        print(
            f"\n  While operating at {freq}Hz, {main_prompt} acts as a Lowless Medium!\n\n"
            f"The attenuation constant, alpha, has a value of {round(alpha, 3)} Np/m, and "
            f"beta has a value of {round(beta, 3)} rad/m.\nThe intrinsic impedance of this "
            f"lowless medium is {round(nc, 3)} ohms.\nThe phase velocity is {round(up, 3)} "
            f"meters per second with a wavelength of {round(lam, 3)} meters.\n")
        input('Press any key to continue...')
    elif test <= 0.01:
        alpha = ((mat[1] / 2) * sqrt((uo * mat[2]) / (eo * mat[0])))
        beta = (w / (sqrt(uo * mat[2] * eo * mat[0])))
        nc = ((mat[2] * uo) / (eo * mat[0]))
        up = (1 / (mat[0] * eo * mat[2] * uo))
        lam = float(up / freq)
        print(
            f"\n  While operating at {freq}Hz, {main_prompt} acts as a Low-Less Medium!\n\n"
            f"The attenuation constant, alpha, has a value of {round(alpha, 3)} Np/m, and "
            f"beta has a value of {round(beta, 3)} rad/m.\nThe intrinsic impedance of this "
            f"low-less medium is {round(nc, 3)} ohms.\nThe phase velocity is {round(up, 3)} "
            f"meters per second with a wavelength of {round(lam, 3)} meters.\n")
        input('Press any key to continue...')
    elif test >= 100:
        alpha = sqrt(pi * freq * uo * mat[2] * mat[1])
        beta = sqrt(pi * freq * uo * mat[2] * mat[1])
        nc = complex((1 + 1j) * (alpha / mat[1]))
        up = sqrt(4 * pi * freq * uo * mat[2] * mat[1])
        lam = up / freq
        print(
            f"\n  While operating at {freq}Hz, {main_prompt} acts as a "
            "Good Conductor!\n\n  The attenuation constant, alpha, has a "
            f"value of {round(alpha, 3)} Np/m, and beta has a value of "
            f"{round(beta, 3)} rad/m.\n  The intrinsic impedance of this "
            f"good conductor is {nc} ohms.\n  The phase velocity is "
            f"{round(up, 3)} meters per second with a wavelength of "
            f"{round(lam, 3)} meters.\n")
        input('Press any key to continue...')
    else:
        alpha = (w * (sqrt((uo * mat[2] * eo * mat[0]) * sqrt(1 + (test ** 2)) - 1)))
        beta = (w * (sqrt((uo * mat[2] * eo * mat[0]) * sqrt(1 + (test ** 2)) + 1)))
        nc = complex((sqrt((uo * mat[2]) / (eo * mat[0]))) * sqrt((1 - (1j * test))))
        up = (w / beta)
        lam = ((2 * pi) / beta)
        print(
            f"\n  While operating at {freq}Hz, {main_prompt} acts as an "
            "Any Medium!\n  The attenuation constant, alpha, has a value "
            f"of {round(alpha, 3)} Np/m,\n  and beta has a value of "
            f"{round(beta, 3)} rad/m.\n  The intrinsic impedance of this "
            f"any medium is {nc} ohms.\n  The phase velocity is "
            f"{round(up, 3)} meters per second\n  with a wavelength of "
            f"{round(lam, 3)} meters.\n")
        input('Press any key to continue...')


while True:
    print(
        "Welcome to the Conductor Calculator!\n"
        "A dictionary of sample materials at sample values to test out has been pre-loaded. "
        "To see it, type 'help'.\nThis will also list any custom materials that you have added "
        "to the dictionary using 'add'; they will be added to the end of the dictionary.\n\n"
        "To test your own custom material and values, enter 'add' to add it to the dictionary "
        "of materials.\nTo try a material, ensure it is available in the dictionary and type "
        "its name in the prompt below.\n\nTo exit, simply type 'quit'.\n")

    yes_or_no_error = "Please type/enter 'yes' or 'no', or simply 'y' or 'n'"
    main_prompt = input("Please input a material name or a command: ").lower()

    if main_prompt == "help":
        print("\nCurrently contains the following materials:\n")
        print(preloaded_dict.keys())
        print("\nType one of the provided material names when prompted.")

    elif main_prompt == "add":
        while True:
            prompt1 = input(
                "Would you like to add a material to the current material dictionary?\n"
                "[Y]es or [N]o ").lower()
            if prompt1 in ("y", "yes"):
                while True:
                    while True:
                        mat_name = input(
                            "Adding a material...\nWhat is your material named? ").lower()
                        if mat_name == "":
                            print("\nPlease type in a material name\n")
                        else:
                            break
                    while True:
                        try:
                            mat_rpermit = float(input(
                                f"What is the relative permittivity (\u03B5\u1D63) of {mat_name}? "))
                        except ValueError:
                            print(f"You did not specify a relative permittivity, or it is invalid...\n"
                                  "Please use only numbers for (\u03B5\u1D63)")
                        else:
                            break
                    while True:
                        try:
                            mat_cconst = float(input(
                                f"What is the conductivity constant (\u03C3) of {mat_name}? "))
                        except ValueError:
                            print(f"You did not specify a conductivity constant, or it is invalid...\n"
                                  "Please use only numbers for (\u03C3)")
                        else:
                            break
                    while True:
                        try:
                            mat_rpermea = float(input(
                                f"What is the relative permeability (\u03BC\u1D63) of {mat_name}? "))
                        except ValueError:
                            print(f"You did not specify a relative permeability, or it is invalid...\n"
                                  "Please use only numbers for (\u03BC\u1D63)")
                        else:
                            break
                    while True:
                        is_valid = input(
                            f"You are adding:\n{mat_name}\nwith a \u03B5\u1D63 of {mat_rpermit},\n"
                            f"\u03C3 of {mat_cconst},\nand a \u03BC\u1D63 of {mat_rpermea}\n"
                            "Is this correct ([Y]es or [N]o)?\n").lower()
                        if is_valid == "":
                            print(f"{yes_or_no_error}\n")
                        else:
                            break
                    if is_valid in ("y", "yes"):
                        print(f"\nAdded {mat_name} to the current material dictionary!\n")
                        preloaded_dict.update({mat_name: (mat_rpermit, mat_cconst, mat_rpermea)})
                        break
                break
            elif prompt1 in ("n", "no"):
                break
            else:
                print(f"{yes_or_no_error}\n")

    elif main_prompt == "quit":
        print("\nGoodbye!\n")
        quit()
    else:
        try:
            main_funct(preloaded_dict[main_prompt])
            while True:
                again_prompt = input(
                    "Would you like to try another calculation? [Y]es or [N]o: ").lower()
                if again_prompt in ("y", "yes"):
                    break
                elif again_prompt in ("n", "no"):
                    print("\nGoodbye!\n")
                    quit()
                elif again_prompt == "":
                    print(yes_or_no_error)
                else:
                    print(f"I didn't quite understand what you meant by '{again_prompt}'...")
        except KeyError:
            if main_prompt == "":
                print("\nNo material specified.\nPlease enter a valid material name "
                      "listed in the 'help' command, or use 'add' to add your own.\n")
            else:
                print(f"\n{main_prompt} is not a valid material or command.\nPlease use a valid "
                      "material listed in the 'help' command, or use 'add' to add your own.\n")
