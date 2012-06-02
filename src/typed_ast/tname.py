
from typed_ast import *
from tnode import *
from .. import substitution as sub
from .. import typ

class TName(TNode):
	"""
	A node representing variable assignment
	"""

	def __init__(self, n):
		super(TName,self).__init__(n)
		self.name = "Namement"

	def format_tree(self,indents):
		s = super(TName,self).format_tree(indents)
		s += "  "*indents + "id = " + self.id + "\n"
		return s

	def traverse(self, env):
		self.id = self.node.id
		self.typ = env.get_type(node.id)
		if self.typ == None:
			self.typ = typ.TError("Undefined")
			env.add_type(t, node.id)
		return (self, sub.Substitution(), env)

