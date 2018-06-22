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


test1 = MaterialDict({
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
test1 #preloaded dictionary
test1.count()
test2 = MaterialDict() #empty dictionary
test2
test2.count()
test1.items()
test2.update({"TEST": (5, 5, 5)})
