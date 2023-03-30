"""
WaveWiz
-------------------------

This module provides functions for calculating the propagation
parameters of various materials at specific frequencies.
It can also classify the material as a Lossless Medium,
Low-Loss Medium, Good Conductor, or Any Medium based on the given
parameters.

Functions
---------
get_material_properties()
    Prompts the user to select a material from a predefined dictionary
    and returns its properties.

get_frequency()
    Prompts the user to enter the angular frequency (ω) in rad/s.

calc_prop_params(er, sigma, ur, omega)
    Calculates the propagation parameters α, β, γ, wavelength, and
    skin depth for the given material properties and frequency.

classify_medium(er, sigma, omega)
    Classifies the material as a Lossless Medium, Low-Loss Medium,
    Good Conductor, or Any Medium based on the given parameters.

run_application()
    Runs the application as a standalone script, prompting the user
    to select a material and enter a frequency, then displays the
    calculated propagation parameters and material classification.
"""


import cmath

MATERIALS = {
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

def get_material_properties():
    """
    Prompts the user to select a material from a
    predefined dictionary and returns its properties.

    Returns
    -------
    float
        Relative permittivity (εr) of the selected material.
    float
        Conductivity (σ) of the selected material in S/m.
    float
        Relative permeability (μr) of the selected material.
    """
    print("Available materials:")
    for material in MATERIALS.keys():
        print(material)

    selected_material = input("Select a material from the list: ").lower()
    while selected_material not in MATERIALS:
        print("Invalid material. Please try again.")
        selected_material = input("Select a material from the list: ").lower()

    return MATERIALS[selected_material]

def get_frequency():
    """
    Prompts the user to enter the angular frequency (ω) in rad/s.

    Returns
    -------
    float
        Angular frequency (ω) in rad/s.
    """
    while True:
        try:
            omega = float(input("Enter the angular frequency ω (rad/s): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return omega

def calc_prop_params(
        er: float, sigma: float, ur: float, omega: float) -> complex:
    """
    Calculates the propagation parameters α, β, γ, wavelength, and
    skin depth for the given material properties and frequency.

    Parameters
    ----------
    er : float
        Relative permittivity (εr) of the material.
    sigma : float
        Conductivity (σ) of the material in S/m.
    ur : float
        Relative permeability (μr) of the material.
    omega : float
        Angular frequency (ω) in rad/s.

    Returns
    -------
    complex
        Attenuation constant (α) in Np/m.
    complex
        Phase constant (β) in rad/m.
    complex
        Propagation constant (γ).
    complex
        Wavelength in meters.
    complex
        Skin depth in meters.
    """
    epsilon_0 = 8.8541878128e-12  # Vacuum permittivity in F/m
    mu_0 = 4 * cmath.pi * 1e-7  # Vacuum permeability in H/m

    epsilon_r = er * epsilon_0
    mu_r = ur * mu_0

    alpha = omega * cmath.sqrt(
        (epsilon_r * mu_r) / 2
        ) * cmath.sqrt(cmath.sqrt(1 + (sigma / (omega * epsilon_r))**2) - 1)

    beta = omega * cmath.sqrt(
        (epsilon_r * mu_r) / 2
        ) * cmath.sqrt(cmath.sqrt(1 + (sigma / (omega * epsilon_r))**2) + 1)

    gamma = alpha + 1j * beta

    wavelength = 2 * cmath.pi / beta

    if alpha.real == 0:
        skin_depth = float('inf')
    else:
        skin_depth = 1 / alpha

    return alpha, beta, gamma, wavelength, skin_depth

def classify_medium(er: float, sigma: float, omega: float) -> str:
    """
    Classifies the material as a Lossless Medium, Low-Loss Medium,
    Good Conductor, or Any Medium based on the given parameters.

    Parameters
    ----------
    er : float
        Relative permittivity (εr) of the material.
    sigma : float
        Conductivity (σ) of the material in S/m.
    omega : float
        Angular frequency (ω) in rad/s.

    Returns
    -------
    str
        Classification of the material: Lossless Medium,
        Low-Loss Medium, Good Conductor, or Any Medium.
    """
    epsilon_0 = 8.8541878128e-12  # Vacuum permittivity in F/m
    epsilon_r = er * epsilon_0

    if sigma / (omega * epsilon_r) < 1e-3:
        return "Lossless Medium"
    if sigma / (omega * epsilon_r) >= 1e-3 and sigma / (omega * epsilon_r) < 1e-1:
        return "Low-Loss Medium"
    if sigma / (omega * epsilon_r) >= 1e1:
        return "Good Conductor"

    return "Any Medium"

def add_material():
    print("Enter the new material properties:")
    name = input("Material name: ")
    er = float(input("Relative permittivity (εr): "))
    sigma = float(input("Conductivity (σ) in S/m: "))
    ur = float(input("Relative permeability (μr): "))
    MATERIALS[name] = (er, sigma, ur)

def run_application():
    er, sigma, ur = get_material_properties()
    omega = get_frequency()

    alpha, beta, gamma, wavelength, skin_depth = calc_prop_params(er, sigma, ur, omega)
    medium_type = classify_medium(er, sigma, omega)

    print(f"\nThe material at the specified frequency is a {medium_type}.")
    print("Propagation Parameters:")
    print(f"α (attenuation constant): {alpha.real:.4e} Np/m")
    print(f"β (phase constant): {beta.real:.4e} rad/m")
    print(f"γ (propagation constant): {gamma:.4e}")
    print(f"Wavelength: {wavelength:.4e} m")
    print(f"Skin depth: {skin_depth:.4e} m")

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Calculate propagation parameters and classify medium")
        print("2. Add a new material")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            run_application()
        elif choice == "2":
            add_material()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
