#! /usr/bin/env python3

"""
template with syntax rules and coding conventions
contains meepy sugar ready to use


Examples:
    >>> import template
    >>> type(template)
    <class 'module'>

    
Notes:
    put help notes and useful documentation here

    functions / methods and variables / atributes initialized as _ (e.g.: _var; _fun())
    are for internal use and may be changed without previous warning

See Also:
    add some references (links, bibliography) here

Todo:
    fixes and bugs

"""

__epilog__ = {
  'author': "Sergio Ferreira",
  'version': '0.1',
  'date': "2020-10-11",
}


class ClassName():
    """
    class description

    Attributes:
      - attribute name: description

    Methods:
      - method name   : description

    Examples:
      >>> instance = ClassName()
      start ClassName
      >>> type(instance)
      <class 'template.ClassName'>

    """

    def __init__(self, *args, **kwargs):
      """
      construtor

      Arguments:
        - describe atributes / arguments here

      Returns:
        - 

      Examples:
        >>> instance = ClassName(1, 2, 3, a = "A", b = "B")
        start ClassName
        >>> print(instance.args)
        (1, 2, 3)
        >>> print(instance.args[:])
        (1, 2, 3)
        >>> print(instance.args[0])
        1
        >>> print(instance.kwargs)
        {'a': 'A', 'b': 'B'}
        >>> print(instance.kwargs['b'])
        B

      """
      print("start ClassName")

      self.args = args
      self.kwargs = kwargs


    def methodName(self, *args, **kwargs):
      """
      method description

      Arguments:
        arg: type
          argument description
      
      Returns: type
          return description

      Raises:
          error handling

      Examples:
        >>> instance = ClassName(11, 12, 13, X = "x", Y = "y")
        start ClassName
        >>> print(instance.args)
        (11, 12, 13)
        >>> print(instance.kwargs)
        {'X': 'x', 'Y': 'y'}
        >>> instance.methodName(14, 15, Z = "z")
        (11, 12, 13, 14, 15) {'X': 'x', 'Y': 'y', 'Z': 'z'}
        >>> print(instance.args[0])
        11
        >>> print(instance.args[-1])
        15
        >>> print(instance.kwargs['Z'])
        z

      """
      if kwargs:
        self.kwargs.update(kwargs)
      if args:
        self.args = self.args + args

      print(self.args, self.kwargs)




def functionName(*args, **kwargs):
    """
    function description

    Arguments:
      arg: type
        argument description
      
    Returns: type
        return description

    Raises:
        error handling

    Examples:
      >>> type(functionName)
      <class 'function'>
      >>> var = functionName("fa", "fb", "fc", fa = "b", fb = "c")
      ('fa', 'fb', 'fc') {'fa': 'b', 'fb': 'c'}
      >>> print(var)
      0
    """
    print(args, kwargs)
    return 0


def __main__():
    """
    called from cli
    """

    import sys
    import clitools
    menu = clitools.OptionsMenu(modinfo = __epilog__, arg_val = sys.argv[1:], description = "meppy template with syntax rules and coding conventions")
    menu.create()

    print("name: ", __name__)
    print("main: ", __main__)


if __name__ == '__main__':
  __main__()


