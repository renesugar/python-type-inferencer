# Usage
 * jython main.py <source_code.py>
 * eg: jython main.py tests/src/functions.py
 * The output will go in logs/pytown.log

# Structure
* The main program code is in pytown.py
* The type objects with methods such as unify, apply_subst, and
free_type_vars are in inftype.py
* builtins.py has some pre-written builtin types and the builtin environment
* parser.py is the parsing module

# Testing
* Unit testing is in tests/.
* Run them all with 'tests/test_all.sh'
* Run them individually with 'jython tests/something_tests.py'
* Sample source code we can try type-inferring is in tests/src/

# Short-term todo
* make sure inference with builtins is working as desired
* clean up the traverse() method in pytown.py
* class types
* more tests?

# Long-term todo
* Constraint generation and type graph analysis.