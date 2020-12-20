# LinearEqnss
Linear Eqnss Generation for Graphene Surfaces

CompiledFams and CompiledFamsRecursive output the same results but get there in different ways. Both enable the user to generate a series of linear equations to calculate the average number of steps to reach a single active site given both a closed or non-closed system. Compiled Fams contains very primitive code as a user interface. 

The premise of the code is to take a variety of different shapes and sites, identify their patterns, and then generate code to input into linear equation calculators. The code itself does not execute the linear equations but simply generates them for use. These sets of codes resolves the previously hand done pattern search required to generate these random-walk equations in the first place, making the process to generate equations for sites n>400 much quicker.

Better UI and visualizations of what the code is attempting to accomplish will surely be useful. I attach an Excel sheet used to identify the patterns that are captured in the code.
