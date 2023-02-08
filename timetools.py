#! /usr/bin/env python3

"""
auxiliary tools and utils for date and time manipulation


Examples:
    >>> import timetools
    >>> type(timetools)
    <class 'module'>


Notes:
    tools for timestamping and benchmarking execution times
    tools for date and time arithmetic
    tools for date and time conversion

See Also:
    add some references (links, bibliography)

Todo:
    improve unit tests 
    date / time conversion functions

"""

__version__ = '0.1'
__author__ = "Sergio Ferreira"
__date__ = "2020-10-09"


import time


def timeBench(func):
    """
    decorator to calculate the running time of a function

    Arguments:
      func: function and arguments

    Returns: float
        running time in seconds.miliseconds of function func

    Raises: N/A

    Examples:
      >>> type(timeBench)
      <class 'function'>
      >>> timeBench(time.sleep(1.1)) #doctest: +ELLIPSIS
      <function timeBench.<locals>.funcAux at ...
    """
    def funcAux(*args, **kwargs):
        start = now()
        res = func(*args, **kwargs)
        end = now()

        str_args = ', '.join([str(arg) for arg in args])
        str_kwargs = str(kwargs)
        time_diff=timeDiff(start, end)

        print("file %s function %s(%s %s) \n\t--> time: %f" % (__file__, func.__name__, str_args, str_kwargs, time_diff))
        return res

    return funcAux


def timeDiff(start_time, end_time):
  """
  return the time difference between two timestamps in epoch format

  Arguments:
    start_time: seconds since the epoch as a floating point number
    end_time: seconds since the epoch as a floating point number

  Returns: float
    the time difference between start_time and end_time

  Raises: N/A

  Examples:
    >>> type(timeDiff)
    <class 'function'>
    >>> type(timeDiff(1, 2))
    <class 'int'>
    >>> timeDiff(1.6, 3.6)
    2.0
  """
  return end_time - start_time


def now():
  """
  a parser to time.time(), returns the current epoch time as a floating point number

  Arguments: N/A

  Returns: float
    current epoch time as a floating point number

  Raises: N/A

  Examples:
    >>> type(now)
    <class 'function'>
    >>> n = now()
    >>> type(n)
    <class 'float'>
  """
  return time.time()


@timeBench
def _test(time_, *args, **kwargs):
  import doctest
  doctest.testmod(name='now')
  doctest.testmod(name='timeDiff')
  doctest.testmod(name='timeBench')
  print(now())
  time.sleep(time_)
  print(now())


def __main__():
    """
    called from cli
    """
    import clitools
    menu = clitools.OptionsMenu(
      description = "meppy date and time tools and utils",
      help = True)
#      version = __version__,
#      author = __author__,
#      data = __date__
    _test(5)
    menu.create()





if __name__ == '__main__':
    __main__()


