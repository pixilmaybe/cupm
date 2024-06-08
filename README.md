# cupm (Computed Unload Package Manager)
## An extended use terminal that supports cmd, cupm and all cupm installations and external modules.

### Current version: **beta 1.9.0** 


Welcome to the **cupm** terminal! cupm is a Python-based single-line console that inherits from cmd. cupm (use using prefix '-cup ') offers various functions like *direct pip*, *atomic variables*, 
*math*,  *Python (all versions)* and more! Let's take a look at the syntax:

Basic hello world statement (prints 'Hello, world!' to the terminal):

`echo Hello, world!` (i) This command inherits from cmd. Let's see how to do it using cupm:

`-cup @basic print "Hello, world!"`
 ^^^^ ^^^^^^ ^^^^^ ^^^^^^^^^^^^^^^
  A     B      C          D

  A - prefix, required to call cupm commands
  B - sector, always starts with '@', tells cupm where the function <C> is located to avoid overlap
  C - function, self-explanatory, tells cupm what we want to do
  D - argument, arguments are separated with a space ' '

  __Sectors__

  (i) This repository already has all external sectors installed

  - `@basic` - basic sector with functions like print
  - `@atomic` - various functions for variables
  - `@basic.math` - math functions
  - `@external.python` - external sector, includes functions to run and configure your python. Supports all released python versions
  - `@external.cmd` - external sector, includes functions for cmd, like ping, cat, and writing files
  - `@external.pip` - external secotr, functions for pip, like install, show, and upgrade pip
  - `@cupm` - internal functions for configuring cupm
