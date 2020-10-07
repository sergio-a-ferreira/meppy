#! /usr/bin/env python3

"""
template with syntax rules and coding conventions


Notes:
    put help notes and useful documentation here

See Also:
    add some references (links, bibliography)

Todo:
    fixes and bugs

"""

class className():
    """
    class description

    Usage:
    >>> instance = className("a", "b", "c", a="b", b="c")
    start className
    >>> type(instance)
    <class '__main__.className'>
    >>> print(instance.args)
    ('a', 'b', 'c')
    >>> print(instance.kwargs)
    {'a': 'b', 'b': 'c'}
    
    attributes:
        - attribute name: description

    """

    def __init__(self, *args, **kwargs):
          """construtor"""
          print("start className")

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
        >>> instance = className()
        start className
        >>> method = instance.methodName("a", "b", "c", a="b", b="c")
        ('a', 'b', 'c')
        {'a': 'b', 'b': 'c'}
        >>> type(method)
        <class 'NoneType'>
      """
      self.l = args
      self.d = kwargs
      print(self.l)
      print(self.d)



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
      >>> functionName("a", "b", "c", a="b", b="c")
      ('a', 'b', 'c')
      {'a': 'b', 'b': 'c'}
    """
    l = args
    d = kwargs
    print(l)
    print(d)



def __main__():
    """
    called as script
    """
    #help(__name__)
    import doctest
    doctest.testmod(name='className().methodName("a", "b", "c", a="b", b="c")')
    instance = className("a", "b", "c", a="b", b="c")
    print(instance.args)
    print(instance.kwargs)

    doctest.testmod(name='functionName("a", "b", "c", a="b", b="c")')
    functionName("a", "b", "c", a="b", b="c")   


if __name__ == '__main__':
    __main__()


