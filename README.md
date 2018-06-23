project-OOP (for IdentiPyConductor)
=========================

Changelog
---------

- Currently testing implementation of a new subclass of *dict* called MaterialDict that allows you to add a custom material and specify custom values for εᵣ, σ, and μᵣ.


What this script actually does
------------------------------

First, you are prompted to select a material. A help option is available to see the pre-loaded  materials to test out.
Once a valid material is given, a function runs that uses the selected material as an argument. Inside the function, conditionals execute different formulas for specific scenarios. The math formulas access the following key values contained in a dictionary, where your selected material is the *key*, and the *values paired* are as follows:

{"material": [0] = εᵣ (Relative Permittivity), [1] = σ (Conductivity Constant), [2] = μᵣ (Relative Permeability)}

   *Comes pre-loaded with the following materials:*

   *Air, Fresh Water, Sea Water, Ice, Clay, Saturated Sand, Barium Titanate, Cold Rolled Steel, Purified Iron, Mu Metal, 2-81
   Permalloy, Copper, Gold, Aluminum, Tungsten, Graphite, Diamond, Silicon, Glass, Kiln Dried Wood & PTFE (Teflon).*

Once a material has been given, the next prompt will ask you to specify the operating frequency the material is running at. The calculations then process, and return the relevant results.

You can then chose to run another calculation by typing (Y)es, or, (N)o to quit the script (gracefully).

TESTING: You can now add a custom material to the pre-loaded values and use it for custom calculations!

***
*Please Note*

I am but a novice coder, and my project(s) will definitely reflect as such.
Questions and comments are appreciated and welcomed- however, please try to be as helpful/informative as possible if you decide to make a suggestion/comment!
***
