# Sage: Open Source Mathematical Software (Game Theory Dev Repo)

> "Creating a Viable Open Source Alternative to
>     Magma, Maple, Mathematica, and MATLAB"

Copyright (C) 2005-2014 The Sage Development Team

[http://www.sagemath.org](http://www.sagemath.org)

The Sage Library is GPLv2+, included packages have compatible OSS
licenses (see COPYING.txt). Over 400 people have contributed code to
Sage. Please see the following web page for a list:

[http://www.sagemath.org/development-map.html](http://www.sagemath.org/development-map.html)

In many cases, documentation for modules and functions list the
authors.

**This is the working repository for game theoretical development in Sage. For the main Sage repository see [https://github.com/sagemath/sage](https://github.com/sagemath/sage).**

The current open tickets for game theory can be found (which correspond to branches in this repository) below:

- 16331: Build capacity to solve matching games in to Sage: [http://trac.sagemath.org/ticket/16331](http://trac.sagemath.org/ticket/16331)
- 16332: Build capacity to calculate Shapley value of cooperative games: [http://trac.sagemath.org/ticket/16332](http://trac.sagemath.org/ticket/16332)
- 16333: Build class for normal form games as well as ability to obtain Nash equilibria: [http://trac.sagemath.org/ticket/16333](http://trac.sagemath.org/ticket/16333)

If you would like to contribute, please see the discussions at the relevant tickets above and/or fork this repository.

Current contributors:

- James Campbell (Cardiff)
- Vincent Knight (Cardiff)


In order to use some of our code, you must have Gambit installed within Sage. After cloning this repo, download the tarball file from [here](http://sourceforge.net/projects/gambit/files/gambit13/).
Move the tarball to ``SAGE_ROOT/upstream/`` and then from ``SAGE_ROOT`` run ``sage -i package_name``.
You should now be able to ``import gambit`` from within sage.
