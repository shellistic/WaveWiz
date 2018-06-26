from math import pi, sqrt


class MaterialDict(dict):

    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)

    def __repr__(self):
        if len(self) == 0:
            return "empty material dictionary"
        else:
            return f"material dictionary containing {len(self)} material(s)"

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 1:
                raise TypeError("update expected at most 1 arguments, "
                                f"received {len(args)}")
            other = dict(args[0])
            for key in other:
                self[key] = other[key]
        for key in kwargs:
            self[key] = kwargs[key]

    def count(self):
        return len(self)


preloaded_dict = MaterialDict({
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
})


def main_funct(mat):
    """
    Main Function [main_funct()] takes the material provided in 'main_prompt'
    and uses it as an argument for this function.
    * Example:
    If 'main_prompt' is 'air', the function will run as main_funct('air') and
    will plug-in its key values for use in the relevant math.
    """
    while True:
        try:
            freq = float(input('\nWhat frequency (in Hertz) is the material'
                               ' operating at? '))
        except ValueError:
            print('Please type in only numbers for operating frequency...')
        else:
            break

    eo = 8.854 * 10 ** -12
    uo = 1.26 * 10 ** -6
    w = 2 * pi * freq * mat[0] * eo
    test = mat[1] / w
    if test == 0:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as a Lowless Medium!')
        alpha = 0
        print('\n  The attenuation constant, alpha, '
              f'has a value of {round(alpha, 3)} Np/m, and ')
        beta = (w / (sqrt(uo * mat[2] * eo * mat[0])))
        print(f'  beta has a value of {round(beta, 3)} rad/m.')
        nc = ((mat[2] * uo) / (eo * mat[0]))
        print('  The intrinsic impedance of this lowless'
              f' medium is {round(nc, 3)} ohms.')
        up = (1 / (mat[0] * eo * mat[2] * uo))
        lam = float(up / freq)
        print(f'\n  The phase velocity is {round(up, 3)} meters per second\n'
              f'  with a wavelength of {round(lam, 3)} meters.\n')
        input('Press Enter to continue... \n')
    elif test <= 0.01:
        print(f'\n  While operating at {freq}Hz, {main_prompt} '
              f'acts as a Low-Less Medium!')
        alpha = ((mat[1] / 2) * sqrt((uo * mat[2])/(eo * mat[0])))
        print('\n  The attenuation constant, alpha, '
              f'has a value of {round(alpha, 3)} Np/m, and ')
        beta = (w / (sqrt(uo * mat[2] * eo * mat[0])))
        print(f'  beta has a value of {round(beta, 3)} rad/m.')
        nc = ((mat[2] * uo) / (eo * mat[0]))
        print('  The intrinsic impedance of this low-less '
              f'medium is {round(nc, 3)} ohms.')
        up = (1 / (mat[0] * eo * mat[2] * uo))
        lam = float(up / freq)
        print(f'\n  The phase velocity is {round(up, 3)} meters per second\n'
              f'  with a wavelength of {round(lam, 3)} meters.\n')
        input('Press Enter to continue... \n')
    elif test >= 100:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as a Good Conductor!')
        alpha = sqrt(pi * freq * uo * mat[2] * mat[1])
        print('\n  The attenuation constant, alpha, '
              f'has a value of {round(alpha, 3)} Np/m, and ')
        beta = sqrt(pi * freq * uo * mat[2] * mat[1])
        print(f'  beta has a value of {round(beta, 3)} rad/m.')
        nc = complex((1 + 1j) * (alpha / mat[1]))
        print('  The intrinsic impedance of this '
              f'good conductor is {nc} ohms.')
        up = sqrt(4 * pi * freq * uo * mat[2] * mat[1])
        lam = up / freq
        print(f'\n  The phase velocity is {round(up, 3)} meters per second\n'
              f'  with a wavelength of {round(lam, 3)} meters.\n')
        input('Press Enter to continue...\n')
    else:
        print(f'\n  While operating at {freq}Hz, {main_prompt}'
              f' acts as an Any Medium!')
        alpha = (w * (sqrt((uo * mat[2] * eo * mat[0]) *
                           sqrt(1 + (test ** 2)) - 1)))
        print('\n  The attenuation constant, alpha, '
              f'has a value of {round(alpha, 3)} Np/m, and ')
        beta = (w * (sqrt((uo * mat[2] * eo * mat[0]) *
                          sqrt(1 + (test ** 2)) + 1)))
        print(f'  beta has a value of {round(beta, 3)} rad/m.')
        nc = complex((sqrt((uo * mat[2]) / (eo * mat[0]))) *
                     sqrt((1 - (1j * test))))
        print('  The intrinsic impedance of this any medium is '
              f'{nc} ohms.')
        up = (w / beta)
        lam = ((2 * pi) / beta)
        print(f'\n  The phase velocity is {round(up, 3)} meters per second\n'
              f'  with a wavelength of {round(lam, 3)} meters.\n')
        input('Press Enter to continue...\n')


while True:
    main_prompt = (input("\nWelcome to the Conductor Calculator!\n\n"
                         "A dictionary of sample materials at sample values "
                         "to test out has been pre-loaded. To see them, type "
                         "'help'.\n\n"
                         "To test your own custom material and values, enter "
                         "'add' to add it to the dictionary of materials.\n\n"
                         "To try a material, ensure it is available in the "
                         "dictionary and type its name in the prompt below.\n"
                         "What material are you working with? ").lower())
    if main_prompt == "help":
        print("\nCurrently contains the following materials:\n\n")
        print(preloaded_dict.keys())
        print("Type one of the provided material names when prompted.\n")
    elif main_prompt == "add":
        prompt1 = input("Would you like to add a material "
                        "to the current material dictionary?\n"
                        "[Y]es or [N]o ").lower()

        if prompt1[0] == "y":
            while True:
                mat_name = input("OK!\nWhat is your material named? ").lower()
                while True:
                    try:
                        mat_rpermit = float(input("What is its relative "
                                                  "permittivity "
                                                  "(\u03B5\u1D63) value? "))
                    except ValueError:
                        print(f"That is not a valid value...\n"
                              "Please use only numbers for this value.")
                    else:
                        break
                while True:
                    try:
                        mat_cconst = float(input("What is its conductivity "
                                                 "constant (\u03C3) value? "))
                    except ValueError:
                        print(f"That is not a valid value...\n"
                              "Please use only numbers for this value.")
                    else:
                        break
                while True:
                    try:
                        mat_rpermea = float(input("What is its relative "
                                                  "permeability "
                                                  "(\u03BC\u1D63) value? "))
                    except ValueError:
                        print(f"That is not a valid value...\n"
                              "Please use only numbers for this value.")
                    else:
                        break
                is_valid = input("You are trying to add:\n"
                                 f"{mat_name}\n"
                                 f"with a \u03B5\u1D63 of {mat_rpermit},\n"
                                 f"\u03C3 of {mat_cconst},\n"
                                 f"and a \u03BC\u1D63 of {mat_rpermea}\n"
                                 "Is this correct ([Y]es or [N]o)?\n").lower()
                if is_valid[0] == "y":
                    print("Added your new material to the dictionary!")
                    preloaded_dict.update(
                        {mat_name: (mat_rpermit, mat_cconst, mat_rpermea)}
                    )
                    break
    else:
        try:
            main_funct(preloaded_dict[main_prompt])
            while True:
                again_prompt = input("Would you like to try another "
                                     "calculation?\n"
                                     "Please type either "
                                     "Yes or No:\n\n").lower()
                if again_prompt == "":
                    print("No input given. Please type either Yes or No:\n\n")
                elif again_prompt[0] == "n":
                    print("\nGoodbye!\n\n\n\n")
                    quit()
                elif again_prompt[0] == "y":
                    break
                else:
                    print("\nI didn't quite understand that...")
        except KeyError:
            if main_prompt == '':
                print("\nYou did not specify a material.\n"
                      "Please use a valid material listed in the "
                      "'help' command.\n")
            else:
                print(f"\n{main_prompt} is not a valid material or command.\n"
                      "Please use a valid material listed in the "
                      "'help' command.\n")
