# Project to implement an OOP approach - ! DO NOT USE !
#
#[0] = εᵣ = u"\u03B5\u1D63" = "Relative Permittivity"
#  [1] = σ = u"\u03C3" = "Conductivity Constant"
#    [2]= μᵣ = u"\u03BC\u1D63" = "Relative Permeability"


class MaterialDict(dict):

    def __init__(self, *arg, **kw):
        super().__init__(*arg, **kw)

    def __repr__(self):
        if len(self) == 0:
            return "empty material dictionary"
        else:
            return f"material dictionary containing {len(self)} material(s)"

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

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
    'air': (1, 0, 1.00000037),
    'fresh water': (80, 5e-4, 0.999992),
    'sea water': (80, 3, 1),
    'ice': (3.5, 1e-5, 1),
    'clay': (20, 5, 1),
    'saturated sand': (30, 1e-4, 1),
    'barium titanate': (3279, 1e-6, 1),
    'cold rolled steel': (1, 1e-7, 100),
    'purified iron': (1, 1e-7, 5e3),
    'mu metal': (1, 1.6e6, 2e5),
    '2-81 permalloy': (1, 1e2, 1e6),
    'copper': (1, 5.96e7, 0.999994),
    'gold': (1, 4.1e7, 1),
    'aluminium': (1, 3.5e7, 1.000022),
    'tungsten': (1, 1.79e7, 1),
    'graphite': (12.5, 2e5, 1),
    'diamond': (7.5, 1e-13, 0.99999975),
    'silicon': (11.68, 1.56e-3, 1),
    'glass': (65, 1e-15, 1),
    'kiln dried wood': (4, 1e-15, 1.000000435),
    'ptfe': (2.1, 1e-25, 1)
})


prompt1 = input("Would you like to add a material "
                "to the current material dictionary?\n"
                "[Y]es or [N]o ").lower()

if prompt1[0] == "y":
    while True:
        mat_name = input("OK!\nWhat is your material named? ")
        mat_rpermit = input("What is its relative permittivity (εᵣ) value? ")
        mat_cconst = input("What is its conductivity constant (σ) value? ")
        mat_rpermea = input("What is its relative permeability (μᵣ) value? ")
        is_valid = input("You are wanting to add "
                         f"{mat_name} with a εᵣ at {mat_rpermit}, "
                         f"σ at {mat_cconst}, and a μᵣ at {mat_rpermea}--\n"
                         "Is this correct ([Y]es or [N]o)? ").lower()
        if is_valid[0] == 'y':
            print("Added your new material to the dictionary!")
            preloaded_dict.update(
            {mat_name: (mat_rpermit, mat_cconst, mat_rpermea)}
            )
            break

print(preloaded_dict.values())
preloaded_dict.count()
preloaded_dict
