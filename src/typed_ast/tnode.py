from typed_ast import *
from tnode import *
from .. import substitution as sub
from .. import typ

class TNode(object):
	"""
	This serves as a superclass for all the other typed nodes.

	It also serves as a generic node when the traverser doesn't know what kind of
	node we have.
	"""
	def __init__(self, n):
		self.node = n;
		self.name = "Node"
		self.typ = typ.TObj({})

	def traverse(self, env): return (self.node, sub.Substitution(), env)

	def format_tree(self, indents):
		return "  "*indents + self.name + "\n"
	return "  "*indents + "Type: " + str(self.typ)
