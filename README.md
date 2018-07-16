PyConductor
===========


Background
----------
This was a project inspired by a university EE assignment given to a colleague of mine, and I am using it (along with other projects) as valuable and dynamic learning tools for Python development (and, unintentionally, electrical engineering). It started just being a simple script that provided functionality on a pre-defined set of materials; now, it includes a bit of OOP that allows you to add custom materials to run custom calculations for *real world* scenarios!

*(Double-check the math if you actually use this)*

I plan on adding additional features to this and cleaning up this project in general over time- accept my apologies for the lack of proper documentation, lack of structure, and other bells and whistles that should definitely be here.


What this script actually does
------------------------------

First, you are prompted to type a **material** *name*.

A **help** option is available to see the pre-loaded  materials available to test out.

An **add** option is also available so that you can add custom materials to the dictionary for use in calculations.

Once a valid material is given, a function runs that uses the selected material as an argument. Inside the function, conditionals execute different formulas for specific scenarios. The math formulas access the following key values contained in a dictionary, where your selected material is the *key*, and the *values paired* are as follows:

{"material_name": [0] = εᵣ (Relative Permittivity), [1] = σ (Conductivity Constant), [2] = μᵣ (Relative Permeability)}

   *Comes pre-loaded with the following materials:*

   *Air, Fresh Water, Sea Water, Ice, Clay, Saturated Sand, Barium Titanate, Cold Rolled Steel, Purified Iron, Mu Metal, 2-81
   Permalloy, Copper, Gold, Aluminum, Tungsten, Graphite, Diamond, Silicon, Glass, Kiln Dried Wood & PTFE (Teflon).*

Once a **material** has been given, the next prompt will ask you to specify the operating frequency the material is running at. The calculations then process, and **return the relevant results**.

You can then chose to run another calculation by typing (Y)es, or, (N)o to quit the script (gracefully).


Changelog
---------

- Removed 'project' from title and changed project name to just 'PyConductor' (I'm terrible with naming things)

- Implemented a new '**add**' option that allows you to add a custom material to the material dictionary, which is now a subclass of the built-in **dict** type.

- You can now make custom calculations using custom defined materials & values by using the new '**add**' feature.

- Typo fixes, readme corrections and additions

***
*Please Note*

I am but a novice coder, and my project(s) will definitely reflect as such.

***
