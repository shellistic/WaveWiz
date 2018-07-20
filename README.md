PyConductor
===========


Background
----------
This was a project inspired by a university EE assignment given to a colleague of mine, and I am using it (along with other projects) as valuable and dynamic learning tools for Python development (and, unintentionally, electrical engineering). It started just being a simple script that provided functionality on a pre-defined set of materials; now, it also allows you to define and add custom materials to run custom calculations for potential *real world* scenarios!

*(Double-check the math if you actually use this)*

I plan on adding additional features to this and cleaning up this project in general over time- accept my apologies for the lack of proper documentation, lack of structure, and other bells and whistles that should definitely be here.


What this script actually does
------------------------------

First, you are prompted to type a **material** *name*.

A **help** option is available to see the pre-loaded  materials available to test out.

An **add** option is also available so that you can add custom materials to the dictionary for use in calculations.

***Hint**: if a material name given while using 'add' **matches** an **already existing material** within the dictionary, it will simply **update** the values for the key. This means that you can assign custom values to any pre-populated material!*

Once a valid material is given, a function runs that uses the selected material as an argument. Inside the function, conditionals execute different formulas for specific scenarios. The math formulas access the following key values contained in a dictionary, where your selected material is the *key*, and the *values paired* are as follows:

{"material_name": [0] = εᵣ (Relative Permittivity), [1] = σ (Conductivity Constant), [2] = μᵣ (Relative Permeability)}

   *Comes pre-loaded with the following materials:*

   *Air, Fresh Water, Sea Water, Ice, Clay, Saturated Sand, Barium Titanate, Cold Rolled Steel, Purified Iron, Mu Metal, 2-81
   Permalloy, Copper, Gold, Aluminum, Tungsten, Graphite, Diamond, Silicon, Glass, Kiln Dried Wood & PTFE (Teflon).*

Once a **material** has been given, the next prompt will ask you to specify the operating frequency the material is running at. The calculations then process, and **return the relevant results**.

You can then chose to run another calculation by typing (Y)es, or, (N)o to quit the script (gracefully).


Changelog
---------

- Latest cleanup and fixes:

        - Removed unnecessary string interpolation from print function on lines 176, 185, 195.
        - Changed __repr__ method on class MaterialDict to more accurately 'represent' MaterialDicts to Python.
        - Added __str__ method to 'represent' MaterialDicts to others
        - FIXED: Users can enter blank material names by providing an empty string value using the update() method.
        - FIXED: If an empty string is given when asked 'Is this correct [Y]es or [N]o?', Python will throw "IndexError: string index out of range".
        - FIXED: If an empty string is given when asked 'Would you like to add a material...' using the 'add' update() method, Python will throw "IndexError: string index out of range".
        - Added a 'quit' option to gracefully quit from the main entry loop.
        - Clarified responses if blank input given to 'main_prompt'.
        - Clarified main welcome banner and instructions, and cleaned it up by separating the banner text from the input prompt text in the script.
        - Cleanup of extra spaces/whitespace.

- Removed 'project' from title and changed project name to just 'PyConductor' (I'm terrible with naming things)

- Implemented a new '**add**' option that allows you to add a custom material to the material dictionary, which is now a subclass of the built-in **dict** type.

- You can now make custom calculations using custom defined materials & values by using the new '**add**' feature.

Future Plans
------------
- Looking into implementing **Decimal()** (from the decimal module) for more precise arithmatic with floating point numbers.

- Would like to see the entire script shortened/refactored where possible.

***
*Please Note*

I am but a novice coder, and my project(s) will definitely reflect as such.

***
