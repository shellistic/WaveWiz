from math import pi, sqrt


PERMITTIVITY = 8.854e-12
PERMEABILITY = 1.26e-06


class Material:   # TODO: implement getters and setters for numerical values
    """
    Class defining Material objects for the purpose of electrical conductivity testing.

    Materials need to be instantiated with the following parameters:

    name == Name for the material
    rel_permit == εᵣ == Relative Permittivity
    cond_const == σ  == Conductivity Constant
    rel_permea == μᵣ == Relative Permeability
    """

    def __init__(self, name, rel_permit, cond_const, rel_permea):
        self.name = name
        self.rel_permit = rel_permit
        self.cond_const = cond_const
        self.rel_permea = rel_permea

    def __repr__(self):
        return f"Material.{self.name}"

    def __str__(self):
        return f"{self.name}: ({self.rel_permit}, {self.cond_const}, {self.rel_permea})"


class MaterialDict(dict):   # TODO: Enhance this class to add functionality on Material Objects
    """
    Class defining Material Dictionaries and their methods for storing groups of Material objects.
    """

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
        """Logic to store MaterialDict object"""
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
        """Returns a count of materials currently inside the MaterialDict object."""
        return len(self)

    def addmat(self):
        """
        Gathers required material values from user;
        Uses update() class method to add the material based on the values provided.
        """
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
                    print(
                        f"You are adding:\n{mat_name}\nwith a \u03B5\u1D63 of {mat_rpermit},\n"
                        f"\u03C3 of {mat_cconst},\nand a \u03BC\u1D63 of {mat_rpermea}\n")
                    while True:
                        is_correct = input("Is this correct ([Y]es or [N]o)?\n").lower()
                        if is_correct in ("y", "yes"):
                            self.update({mat_name: (mat_rpermit, mat_cconst, mat_rpermea)})
                            print(f"\nAdded {mat_name} to the current material dictionary!\n")
                            break
                        elif is_correct in ("n", "no"):
                            break
                    break
            elif prompt1 in ("n", "no"):
                break


def frequency():
    """Returns a user specified operating frequency floating point value."""
    while True:
        try:
            freq = float(input(
                f"At what frequency (Hz) is the material operating? "))
        except ValueError:
            print("Please type in only numbers for operating frequency...")
        else:
            return freq


def calculate_conductance(mat):
    """
    Takes a material as an argument;
    Prints the results of the defined equations based on operating frequency.
    """
    freq = frequency()
    omega = 2 * pi * freq * mat[0] * PERMITTIVITY  # w
    alpha_test = mat[1] / omega
    if alpha_test == 0:
        conductor_type = "lowless medium"
        alpha = 0
        beta = (omega / (sqrt(PERMEABILITY * mat[2] * PERMITTIVITY * mat[0])))
        nc = ((mat[2] * PERMEABILITY) / (PERMITTIVITY * mat[0]))
        up = (1 / (mat[0] * PERMITTIVITY * mat[2] * PERMEABILITY))
        lam = float(up / freq)
    elif alpha_test <= 0.01:
        conductor_type = "low-less medium"
        alpha = ((mat[1] / 2) * sqrt((PERMEABILITY * mat[2]) / (PERMITTIVITY * mat[0])))
        beta = (omega / (sqrt(PERMEABILITY * mat[2] * PERMITTIVITY * mat[0])))
        nc = ((mat[2] * PERMEABILITY) / (PERMITTIVITY * mat[0]))
        up = (1 / (mat[0] * PERMITTIVITY * mat[2] * PERMEABILITY))
        lam = float(up / freq)
    elif alpha_test >= 100:
        conductor_type = "good conductor"
        alpha = sqrt(pi * freq * PERMEABILITY * mat[2] * mat[1])
        beta = sqrt(pi * freq * PERMEABILITY * mat[2] * mat[1])
        nc = complex((1 + 1j) * (alpha / mat[1]))
        up = sqrt(4 * pi * freq * PERMEABILITY * mat[2] * mat[1])
        lam = up / freq
    else:
        conductor_type = "any medium"
        alpha = (omega *
                 (sqrt((PERMEABILITY * mat[2] * PERMITTIVITY * mat[0]) *
                       sqrt(1 + (alpha_test ** 2)) - 1)))
        beta = (omega *
                (sqrt((PERMEABILITY * mat[2] * PERMITTIVITY * mat[0]) *
                      sqrt(1 + (alpha_test ** 2)) + 1)))
        nc = complex((sqrt((PERMEABILITY * mat[2]) /
                           (PERMITTIVITY * mat[0]))) * sqrt((1 - (1j * alpha_test))))
        up = (omega / beta)
        lam = ((2 * pi) / beta)
    print(   # TODO: Add material name back to final print statement
        f"\n  While operating at {freq}Hz, your specified material acts as a(n) {conductor_type}!"
        f"\n\n  The attenuation constant, alpha, has a value of {round(alpha, 3)} Np/m, and "
        f"beta has a value of {round(beta, 3)} rad/m.\n  The intrinsic impedance of this "
        f"{conductor_type} is {nc} ohms.\n  The phase velocity is {round(up, 3)} "
        f"meters per second with a wavelength of {round(lam, 3)} meters.\n")
    input('Press any key to continue...')


def load_test_values():
    """Generates a sample MaterialDict with sample Material objects."""
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
    return preloaded_dict
