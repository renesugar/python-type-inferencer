# All builtin types

from program_graph import *
from typ import *
from environment import *

## Templates for types:
# Numeric
float_typ = TBuiltin("float", float)
int_typ = TBuiltin("int", int)
# Strings
str_typ = TBuiltin("str", str)
# None
none_typ = TBuiltin("None",type(None))
# Booleans
bool_typ = TBuiltin("bool",bool)

env = Environment({})
#	# Arithmetic
#	("*",float_typ,int_typ)  : float_typ,
#	("/",float_typ,int_typ)  : float_typ,
#	("%",float_typ,int_typ)  : float_typ,
#	("//",float_typ,int_typ) : float_typ,
#	("+",int_typ,int_typ)    : int_typ,
#	("+",int_typ,float_typ)  : float_typ,
#	("+",str_typ,str_typ)    : str_typ,
#
#	# Constants
#	"None"                   : none_typ,
#	"True"                   : bool_typ,
#	"False"                  : bool_typ,
#
#	# IO
#	"print"                  : none_typ
#})
