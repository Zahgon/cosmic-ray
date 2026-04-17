"Tools for querying ASTs."

import parso.python.tree


class ASTQuery:
    """
    Allowing to navigate into any object and test attribute of any object:

    Examples:
    >>> ASTQuery(node).parent.match(Node, type='node').ok

    Test if node.parent isinstance of Node and node.parent.type == 'node'
    At each step (each '.' (dot)) you receive an ObjTest object, then

    Navigation:
    You can call any properties or functions of the base object
    >>> ASTQuery(node).parent.children[2].get_next_sibling()

    Test:
    >>> ASTQuery(node).match(attr='value').match(Class)
    All in once:
    >>> ASTQuery(node).match(Class, attr='value')

    Conditional navigation:
    >>> ASTQuery(node).IF.match(attr='intermediate').parent.FI

    Final result:
    >>> ASTQuery(node).ok
    >>> bool(ASTQuery(node))

    """

    def __init__(self, obj):
        self.obj = obj

    def _clone(self, obj) -> "ASTQuery":
        "Clone this query."
        pass

    def match(self, cls=None, **kwargs) -> "ASTQuery":
        "Check if node matches a class."
        pass

    @property
    def ok(self):
        "Is the query ok."
        pass

    def __bool__(self):
        return self.ok

    def __getattr__(self, item) -> "ASTQuery":
        obj = self.obj
        if obj is None:
            return self
        return self._clone(getattr(obj, item))

    @property
    def IF(self):
        "Conditional navigation."
        pass

    def __call__(self, *args, **kwargs) -> "ASTQuery":
        if self.obj is None:
            return self
        return self._clone(self.obj(*args, **kwargs))

    def __getitem__(self, item) -> "ASTQuery":
        if self.obj is None:
            return self
        return self._clone(self.obj[item])

    def get_definition_name(self):
        "Get the name of the function or class enclosing the current node."
        obj = self.obj
        while obj:
            if isinstance(obj, parso.python.tree.Lambda):
                obj = obj.parent
                continue
            if isinstance(obj, (parso.python.tree.Function, parso.python.tree.Class)):
                return obj.name.value
            obj = obj.parent
        return None


class ASTQueryOptional(ASTQuery):
    "Manages conditional navigation."

    def __init__(self, obj, obj_test=None):
        super().__init__(obj)
        self._initial = obj_test

    def _clone(self, obj):
        pass

    @property
    def FI(self):
        "End of conditional navigation."
        pass
