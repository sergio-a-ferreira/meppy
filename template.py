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
    >>> instance = className()
    >>> type(instance)
    <class '__main__.className'>

    attributes:
        - attribute name: description

    """

    def __init__(self):
          """construtor"""
          pass


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
        >>> method = instance.methodName("a", "b", "c", a="b", b="c")
        ('a', 'b', 'c')
        {'a': 'b', 'b': 'c'}
        >>> type(method)
        <class 'NoneType'>
      """
      l = args
      d = kwargs
      print(l)
      print(d)



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
    print(args)
    print(kwargs)



def __main__():
    """
    called as script
    """
    #help(__name__)
    import doctest
    doctest.testmod(name='functionName')
    


if __name__ == '__main__':
    __main__()


