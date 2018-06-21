project-IdentiPyConductor
=========================


A simple calculator that takes a material and its operating frequency as input and provides output related to its conductive properties.


Background
----------
This was a project inspired by a university EE assignment given to a colleague of mine, and I am using it (along with other projects) as valuable and dynamic learning tools for Python development (and, unintentionally, electrical engineering).
In its current state, it provides limited functionality on a decent variety of materials; however, I plan to implement changes and improvements as I move on.


What this script actually does
------------------------------

First, you are prompted to select a material. A help option is available to see the currently supported materials.
Once a valid material is provided, a function runs that uses the selected material as an argument. Inside the function, conditionals execute different formulas for specific scenarios. The math formulas access the following key values contained in a dictionary, where your selected material is the *key*, and the *values paired* are as follows:

{material: [0] = εᵣ (Relative Permittivity), [1] = σ (Conductivity Constant), [2] = μᵣ (Relative Permeability)}

Currently, it only supports the below listed materials as defined within the script; however, I plan to eventually add functionality to allow users to add additional materials with specified εᵣ, σ, and μᵣ values:

   Air, Fresh Water, Sea Water, Ice, Clay, Saturated Sand, Barium Titanate, Cold Rolled Steel, Purified Iron, Mu Metal, 2-81
   Permalloy, Copper, Gold, Aluminum, Tungsten, Graphite, Diamond, Silicon, Glass, Kiln Dried Wood & PTFE (Teflon).

Once a material has been given, the next prompt will ask you to specify the operating frequency the material is running at. The calculations then process, and return the relevant results.

You can then chose to run another calculation by typing (Y)es, or, (N)o to quit the script (gracefully).



***
*Please Note*

I am but a novice coder, and my project(s) will definitely reflect as such.
Questions and comments are appreciated and welcomed- however, please try to be as helpful/informative as possible if you decide to make a suggestion/comment!

*I found the relevant equations for the assignment, and will update this with them soon...*
***
