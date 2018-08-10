PyConductor
===========
Background
----------
This project was inspired by a university EE assignment given to a colleague of mine, and I am using it (along with other projects) as dynamic learning tools for Python development (and, unintentionally, electrical engineering).

What started as a simple script that calculated conductance and propagation parameters on a pre-defined set of materials has now turned into a module that allows you to define and add custom materials for *real world* applications!

**Please note:** I, along with my colleague, have verified the calculations within for accuracy; you should always independently verify functionality of any third-party software first before download/use.

Contents
--------
#####pyconductor.py
######Module containing Material and MaterialDict class definitions and methods - Useful in conductivity testing
#####conductor_calculator.py
######Example conductance calculation script that imports and uses 'pyconductor'.

conductor_calculator.py
------------------------------

First, you are prompted to type either an **option number** or **material** *name*.

Select *Option [1]* to see the pre-loaded  materials available to test out.

Select *Option [2]* to add custom materials to the dictionary for use in calculations.

Select *Option [3]* to quit the script.

***Hint**: if a material name given while using 'add' **matches** an **already existing material** within the dictionary, it will simply **update** the values for the key. This means that you can assign custom values to any pre-populated material!*

Once a valid material is given, a function runs that uses the selected material as an argument. Inside the function, conditionals execute different formulas for specific scenarios. The math formulas access the following key values contained in a dictionary, where your selected material is the *key*, and the *values paired* are as follows:

{"material_name": [0] = εᵣ (Relative Permittivity), [1] = σ (Conductivity Constant), [2] = μᵣ (Relative Permeability)}

   *Comes pre-loaded with the following materials:*

   *Air, Fresh Water, Sea Water, Ice, Clay, Saturated Sand, Barium Titanate, Cold Rolled Steel, Purified Iron, Mu Metal, 2-81
   Permalloy, Copper, Gold, Aluminum, Tungsten, Graphite, Diamond, Silicon, Glass, Kiln Dried Wood & PTFE (Teflon).*

Once a **material** has been given, the next prompt will ask you to specify the operating frequency the material is running at. The calculations then process, and **print out the relevant results**.

You can then chose to run another calculation by typing (Y)es, or, (N)o to quit the script (gracefully).


Changelog
---------

######Latest cleanup and fixes:

- Finished refactoring pyconductor into a stand-alone module

- Created new file: *conductor_calculator.py*

- Moved calculation logic into conductor_calculator.py

- Whitespace cleanup & minor optimizations

Future Plans
------------
- Looking into implementing **Decimal()** (from the decimal module) for potentially more precise arithmetic with floating point numbers.


