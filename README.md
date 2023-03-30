# WaveWhiz

WaveWhiz is a Python application that calculates the propagation parameters
of various materials at specific frequencies. It can also classify the
material as a Lossless Medium, Low-Loss Medium, Good Conductor, or
Any Medium based on the given parameters.

## Purpose and Intended Uses

WaveWhiz is designed to help engineers, physicists, and researchers analyze
the propagation properties of different materials in the context of
electromagnetic wave propagation.

The application can be used for various purposes, including:

- Designing antennas and waveguides
- Evaluating materials for shielding applications
- Analyzing radio frequency propagation and communication systems

## How It Works

WaveWhiz uses the following equations to calculate the propagation parameters:

1. Complex permittivity (ε)
   ```math
   (ε) = εr * ε0 + j * σ / ω
   ```
2. Complex permeability (μ)
   ```math
   (μ) = μr * μ0
   ```
3. Propagation constant (γ)
   ```math
   (γ) = √(ω² * μ * ε)
   ```
4. Attenuation constant (α)
   ```math
   (α) = Re(γ)
   ```
5. Phase constant (β)
   ```math
   (β) = Im(γ)
   ```
6. Wavelength (λ)
   ```math
   (λ) = 2π / β
   ```
7. Skin depth (δ)
   ```math
   (δ) = 1 / α
   ```

## How to Use

### As a Standalone Script

1. Clone the repository or download the `wavewiz.py` file.
2. Run the script from the command line or an IDE.
3. Follow the prompts to select a material,
   enter the frequency, or add a new material.
4. View the calculated propagation parameters and material classification.

### As a Module

1. Import the `wavewiz.py` module into your Python script.
2. Use the provided functions to calculate the propagation parameters
   and classify the material as needed.

Example usage:

```python
import wavewiz

# Run the application interactively
wavewiz.run_application()

# Use the module's functions as needed
er, sigma, ur = 80, 3, 1
omega = 1e7
alpha, beta, gamma, wavelength, skin_depth = wavewiz.calc_prop_params(er, sigma, ur, omega)
medium_type = wavewiz.classify_medium(er, sigma, omega)

print(f"Medium type: {medium_type}")
print(f"α: {alpha}, β: {beta}, γ: {gamma}, Wavelength: {wavelength}, Skin depth: {skin_depth}")
