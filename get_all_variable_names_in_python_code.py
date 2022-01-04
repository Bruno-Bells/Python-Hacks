import builtins

dict_vars1 = [ i for i, a in locals().items() if id(i)] # Get names of initial builtins

# declare some variables
x = 7
my_name = 'Bruno'
u = 3

dict_vars2 = [ i for i, a in locals().items() if id(i)] # Get names of both initial builtins and variables acros the code

# remove builtins from variable names
res = list(set(dict_vars1)^set(dict_vars2))

variables_in_code = [i for i in res if not i.startswith('_')]
