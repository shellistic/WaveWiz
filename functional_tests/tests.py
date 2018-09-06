# Mark has been given an electrical engineering assignment.

# He needs to write a python program that will determine if a material is a
# Lossless Medium, a Low-Loss Medium, a Good Conductor, or in general Any Medium.

# It also needs to figure and provide the value of alpha, beta, nc, up & lamb

# The inputs provided by the user will be:
#  material (selected from lookup table) | ω (Operating Frequency)

# The outputs given to the user will be:
# Lossless | Low-Loss | Good Conductor | General -
# alpha | beta | nc | up | lamb (after the type of medium is determined)
#
# The program will also need to include a lookup table of the following
# materials and their resepective properties for the user to use:
# -----------------------------------------------------------------------------
# "Mat Name" : (εᵣ (Relative Permit.), σ (Cond. Const.), μᵣ (Relative Permea.))
# ---------|-----------------------|------------------|------------------------
# "air": (1, 0, 1.00000037)
# "fresh water": (80, 5e-4, 0.999992),
# "sea water": (80, 3, 1),
# "ice": (3.5, 1e-5, 1),
# "clay": (20, 5, 1),
# "saturated sand": (30, 1e-4, 1),
# "barium titanate": (3279, 1e-6, 1),
# "cold rolled steel": (1, 1e-7, 100),
# "purified iron": (1, 1e-7, 5e3),
# "mu metal": (1, 1.6e6, 2e5),
# "2-81 permalloy": (1, 1e2, 1e6),
# "copper": (1, 5.96e7, 0.999994),
# "gold": (1, 4.1e7, 1),
# "aluminium": (1, 3.5e7, 1.000022),
# "tungsten": (1, 1.79e7, 1),
# "graphite": (12.5, 2e5, 1),
# "diamond": (7.5, 1e-13, 0.99999975),
# "silicon": (11.68, 1.56e-3, 1),
# "glass": (65, 1e-15, 1),
# "kiln dried wood": (4, 1e-15, 1.000000435),
# "ptfe": (2.1, 1e-25, 1)
#
# He needs to test the following five cases:
# 1. Air at the wifi frequency of 2.4GHz (2.4E9Hz)
# 2. Sea water at a submarine communication frequency of 74 Hz
# 3. 2-81 Permalloy at the wifi frequency of 2.4 GHz (2.4E9Hz)
# 4. Diamond at the frequency of a green laser pointer, 5.73E14 Hz
