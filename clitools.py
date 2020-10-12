#! /usr/bin/env python3

"""
CLI (command line interface) management tools and utilities
  normalize / automate  cli (command line interface) argument's (option / flag) menu
    create / remove options and option groups
    create standart default options and actions for
      help
        if any argument is not valid display simple usage message and exit 2
        if help is optioned display complete usage message and exit 0
      manual
        if manual is optioned display module's manual page and exit 0
      version
        if version is optioned display module's version and exit 0
      testing and benchmarking
        if test|TEST is optioned execute silent|verbose unit test suite
        if both test and TEST are optioned, verbose mode is executed
        benchmark takes an integer as argument, this indicates the quantity of executions to run
      logging
      inspecting and debugging


Examples:
    >>> import clitools
    >>> type(clitools)
    <class 'module'>

    
Notes:
    parser to Python Standard Library argparse and doctest

    functions / methods and variables / atributes initialized as _ (e.g.: _var; _fun())
      are for internal use and may be changed without previous warning


See Also:
    https://docs.python.org/3/library/argparse.html
    https://docs.python.org/3/library/doctest.html

Todo:
    update tests
    test option must accept one optional argument
    benchmark option must accept one optional argument, default's to 1 when not optioned
    add option stdio group w/ -I --inputfile -O --outputfile -E --errorfile

"""

__epilog__ = {
  'author': "Sergio Ferreira",
  'version': '0.1',
  'date': "2020-10-11",
}


import os, sys, argparse


class OptionsMenu():
    """
    creates an options / arguments menu object

    Attributes:
        - program    : calling program name
        - module     : calling module identifier
        - arg_val:   : calling program arguments
        - description: calling program summary description to show in the help usage message
        - usage      : default usage message
        - author     : calling program original author
        - version    : calling program version
        - date       : calling program last version date
        - help       : enable help as an option / flag
        - epilog     : a normalized message displaying program, version and author
        - manual     : enable manual page option
        - tbgroup    : enable group test and benchmark options - disables test and benchmark single options
        - test       : enable test option
        - benchmark  : enable benchmark option
        - standard   : create a standard cli menu (help, man, epilog, tbgroup)
        - default    : execute default actions for the option / flag
        TODO:
        - debug      : enable debug option
        - verbose    : enable verbosity options group menu
        - log        : enable logging options group menu
        - config     : enable configuraton options sub-menu

    Methods:
      - __init__     : construtor; creates the OptionsMenu argument parser and sets default properties

    Examples:
      >>> menu = OptionsMenu(standard = False, default = False, description = 'Class Instatiation')
      >>> type(menu)
      <class 'clitools.OptionsMenu'>
      >>> print(menu.description)
      Class Instatiation

    """

    def __init__(
      self,
      description = 'insert a description of your program / class here',
      modinfo = {},
      help = True,
      arg_val = (),
      manual = True,
      tbgroup = True,
      test = True,
      benchmark = False,
      debug = False,
      verbose = False,
      log = False,
      config = False,
      standard = True,
      default = True
    ):

      """
      creates the cli_menu argument parser and 
        sets default properties for the OptionsMenu menu object

      Arguments:
        - description: <class 'str'>;
                       program summary description
        - modinfo    : <class 'dict'>;
                       epilog information (kwargs: author, date, version)
        - help       : <class 'bool'>;
                       enables /disables help option, default True
        - arg_val    : <class 'tuple'>;
                       a list with all the client line arguments
        - manual     : <class 'bool'>;
                       enables /disables manual page option, default True
        - tbgroup    : <class 'bool'>;
                       enables /disables tbgroup option group, default True
        - test       : <class 'bool'>;
                       enables /disables test option, default True
        - benchmark  : <class 'bool'>;
                       enables /disables benchmark option, default False
        - debug      : <class 'bool'>;
                       enables /disables debug option, default False
        - verbose    : <class 'bool'>;
                       enables /disables verbosiness option group, default False
        - log        : <class 'bool'>;
                       enables /disables logging option group, default False
        - config     : <class 'bool'>;
                       enables /disables configuration option group, default False
        - standard   : <class 'bool'>;
                       flag to create the standard menu object, default True
        - default    : <class 'bool'>;
                       flag to execute default actions based on the optioned arguments, default True

      Returns:
        - cli_menu; a basic cli argument parser object

      Examples:
        >>> menu = OptionsMenu(description = "Construtor examples and tests", default = False)
        >>> type(menu)
        <class 'clitools.OptionsMenu'>
        >>> print(menu.program)
        clitools.py
        >>> print(menu.module) #doctest: +ELLIPSIS
        <module 'clitools' from '...'>
        >>> print(menu.arg_val)
        ()
        >>> print(menu.description)
        Construtor examples and tests
        >>> print(menu.help)
        True
        >>> print(menu.usage)
        usage: clitools.py [OPTIONS] [ARGUMENTS]
        >>> print(menu.epilog)
        clitools.py vN/A; by N/A [N/A]
        >>> print(menu.version)
        N/A
        >>> print(menu.author)
        N/A
        >>> print(menu.date)
        N/A
        >>> print(menu.manual)
        True
        >>> print(menu.tbgroup)
        True
        >>> print(menu.test)
        True
        >>> print(menu.benchmark)
        False
        >>> print(menu.standard)
        True
        >>> print(menu.default)
        False
        >>> type(menu.cli_menu)
        <class 'argparse.ArgumentParser'>
        >>> print(menu.cli_menu)
        ArgumentParser(prog='clitools.py', usage=None, description='Construtor examples and tests', formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
        >>> print(menu.cli_menu.prog)
        clitools.py
        >>> print(menu.cli_menu.usage)
        None
        >>> print(menu.cli_menu.description)
        Construtor examples and tests
        >>> print(menu.cli_menu.formatter_class)
        <class 'argparse.HelpFormatter'>
        >>> print(menu.cli_menu.conflict_handler)
        error
        >>> print(menu.cli_menu.add_help)
        True
        >>> print(menu.__dict__)
        
      """
      # calling program name
      self.program = os.path.basename(sys._getframe(1).f_globals['__file__'])
      # module's id
      globals()['_my_module'] = __import__(os.path.splitext(self.program)[0])
      self.module = globals()['_my_module'] 
      # calling program arguments
      self.arg_val = arg_val
      # descrition message
      self.description = description
      
      # setting help optional argument and generic usage message
      self.help = help
      self.usage = 'usage: ' + self.program + ' [OPTIONS] [ARGUMENTS]'

      # other info about the module / program
      self.author = modinfo.get('author', "N/A")
      self.date = modinfo.get('date', "N/A")
      self.version = modinfo.get('version', "N/A")
      self.epilog = self.program + " v" + self.version + "; by " + self.author + " [" + self.date + "]"
            
      # options / flags to enable disable
      self.manual = manual
      self.tbgroup = tbgroup
      self.test = test
      self.benchmark = benchmark
      self.debug = debug
      self.verbose = verbose
      self.log = log
      self.config = config

      # aditional atributes
      self.standard = standard
      self.default = default

      # create the cli_menu object
      self.cli_menu = argparse.ArgumentParser(
        prog = self.program, 
        add_help = self.help,
        description = self.description, 
        epilog = self.epilog
      )

      # create the standard menu object; to disable set self.standard = False
      if self.standard:
        self.standardMenu()
        self.create()
        


    def addOption(self, *flags, **kwargs):
      """
      adds an option to menu main group, defining how a single command-line argument should be parsed.

      Arguments:
      *flags: <class 'list'>
          a name or a list of names or flags; e.g. 'foo' '-foo' '-f'

      **kwargs: <class 'dict'>
          action:
              the basic type of action to be taken when this argument is encountered at the command line.
          nargs:
              the number of command-line arguments that should be consumed. 
          const:
              a constant value required by some action and nargs selections. 
          default:
              the value produced if the argument is absent from the command line.
          type:
              the type to which the command-line argument should be converted. 
          choices:
              a container of the allowable values for the argument. 
          required:
              whether or not the command-line option may be omitted (optionals only). 
          help:
              a brief description of what the argument does. 
          metavar:
               a name for the argument in usage messages.
          dest:
                the name of the attribute to be added to the object returned by parse_args(). 

      Returns: updates the cli_menu.Namespace with a new option

      Raises:  N/A

      Examples:
        >>> menu = OptionsMenu(description = "addOption examples and tests", standard = False, default = False)
        >>> type(menu)
        <class 'clitools.OptionsMenu'>
        >>> print(menu.description)
        addOption examples and tests
        >>> menu.addOption('-t', '--t', '--test', dest = '_btest', action = 'store_true', default = False, help = 'to enable test flags')
        >>> menu.addOption('-T', '--T', '--TEST', dest = '_bTest', action = 'store_true', default = False, help = 'to enable test flags')
        >>> menu.addOption('-i', '--I', '--iflag', dest = '_iflag', type = int, action = 'store', default = 1, metavar = '<int>', help = 'an integer')
        >>> menu.addOption('-f', '--F', '--fflag', dest = '_fflag', type = float, action = 'store', default = 1.1, metavar = '<float>', help = 'a float')
        >>> menu.addOption('-s', '--S', '--sflag', dest = '_sflag', type = str, action = 'store', default = 'xxx', metavar = '<str>', help = 'a string')
        >>> menu.create()
        >>> type(menu.arguments)
        <class 'argparse.Namespace'>
        >>> print(menu.arguments) #doctest: +ELLIPSIS
        Namespace(_bTest=..., _btest=..., _fflag=1.1, _iflag=1, _sflag='xxx')
        >>> type(menu.arguments._btest)
        <class 'bool'>
        >>> print(menu.arguments._iflag)
        1
        >>> type(menu.arguments._iflag)
        <class 'int'>
        >>> print(menu.arguments._fflag)
        1.1
        >>> type(menu.arguments._fflag)
        <class 'float'>
        >>> print(menu.arguments._sflag)
        xxx
        >>> type(menu.arguments._sflag)
        <class 'str'>

      """
      self.cli_menu.add_argument(*flags, **kwargs)



    def addGroup(self, title = None, description = None):
      """
      creates an option group.
        
      Arguments:
        title:
          title for the sub-parser group in help output;
          by default "subcommands" if description is provided, otherwise uses title for positional arguments 
        description:
          description for the sub-parser group in help output,
          by default None

      Returns: updates the cli_menu.Namespace with a new group
            
      Raises: N/A

      Examples:
        >>> menu = OptionsMenu(description = "addGroup examples and tests", standard = False, default = False)
        >>> type(menu)
        <class 'clitools.OptionsMenu'>
        >>> print(menu.description)
        addGroup examples and tests
        >>> menu.addGroup(title='group 1', description="group 1 description here")
        >>> type(menu.group)
        <class 'argparse._ArgumentGroup'>
        >>> print(menu.group)  #doctest: +ELLIPSIS
        <argparse._ArgumentGroup object at ...>
        >>> print(menu.group.title)
        group 1
        >>> print(menu.group.description)
        group 1 description here

      """
      self.group = self.cli_menu.add_argument_group(title = title, description = description)


    def addGroupOption(self, *flags, **kwargs): 
      """
      adds an option to the current option group

      Arguments: the same as in addOption() method; check addOption() documentation below

      Returns: updates the cli_menu.group.Namespace with a new option

      Raises: N/A

      Examples:
        >>> menu = OptionsMenu(description = "addGroupOption examples and tests", standard = False, default = False)
        >>> type(menu)
        <class 'clitools.OptionsMenu'>
        >>> print(menu.description)
        addGroupOption examples and tests
        >>> menu.addGroup(title='group 1', description="allow tests")
        >>> type(menu.group)
        <class 'argparse._ArgumentGroup'>
        >>> print(menu.group)  #doctest: +ELLIPSIS
        <argparse._ArgumentGroup object at ...>
        >>> print(menu.group.title)
        group 1
        >>> print(menu.group.description)
        allow tests
        >>> menu.addGroupOption('-t', '--t', '--test', dest = '_btest', action = 'store_true', default = False, help = 'to enable test flags')
        >>> menu.addGroupOption('-T', '--T', '--TEST', dest = '_bTest', action = 'store_true', default = False, help = 'to enable test flags')
        >>> menu.addGroupOption('-q', dest = '_q', action = 'store', type = int, default = 0, help = 'opt v stores an integer')
        >>> menu.addGroup(title='group 2', description="area")
        >>> type(menu.group)
        <class 'argparse._ArgumentGroup'>
        >>> print(menu.group)  #doctest: +ELLIPSIS
        <argparse._ArgumentGroup object at ...>
        >>> print(menu.group.title)
        group 2
        >>> print(menu.group.description)
        area
        >>> menu.addGroupOption('--length', default = 5, type = int)
        >>> menu.addGroupOption('--width', default = 10, type = int)
        >>> menu.create()
        >>> type(menu.arguments)
        <class 'argparse.Namespace'>
        >>> print(menu.arguments) #doctest: +ELLIPSIS
        Namespace(_bTest=..., _btest=..., _q=0, length=5, width=10)
        >>> type(menu.arguments._btest)
        <class 'bool'>
        >>> type(menu.arguments._q)
        <class 'int'>
        >>> print(menu.arguments._q)
        0
        >>> type(menu.arguments.length)
        <class 'int'>
        >>> print(menu.arguments.length)
        5
        >>> type(menu.arguments.width)
        <class 'int'>
        >>> print(menu.arguments.width)
        10

      """
      self.group.add_argument(*flags, **kwargs)


    def create(self):
      """
      creates and returns cli menu object
      
      Arguments: enable / disable default options
        manual:  manual page option
        version: program version option
        epilog:  epilog line
        tbgroup: test and benchmark options as a group (disables test and benchmark single options)
        test:    test page option
        benchmark: benchmark page option
        verbose: verbosity sub-menu
        log:     logging sub-menu
        debug:   debugging sub-menu
        config:  configuraton sub-menu

      Returns: updates the cli_menu.arguments.Namespace; can be inspected through self.arguments.<dest>

      Raises: N/A

      Examples:
        
      """
      self.arguments = self.cli_menu.parse_args()
      if self.default:
          self.defaultActions()


    def defaultActions(self):
      """
      calls predefined actions for some options / flags

      Arguments: N/A; parameters in object atributes

      Returns: updates the cli_menu.Namespace

      Raises: N/A

      Examples:
      
      """

      if self.arguments._manual:
        help(self.module)
        exit(0)

      if self.arguments._test_s:
        import doctest
        _tests = doctest.testmod(self.module, verbose=False)
        exit(_tests.failed)
      if self.arguments._test_v:
        import doctest
        _tests = doctest.testmod(self.module, verbose=True)
        exit(_tests.failed)


    def standardMenu(self):
      """
      creates and returns a standard cli menu object with default options / flags
      this method runs on OptionsMenu object creation by default, to disable set self.standard = False

      Arguments: N/A; parameters in object atributes

      Returns: updates the cli_menu.Namespace

      Raises: N/A

      Examples:
        
      """
      if self.manual:
        self.addOption(
          '-m', '--m', '--manual',
          dest = '_manual', action = 'store_true', default = False, help = 'show manual page'
        )

      if self.version:
        self.addOption(
          '-V', '--version',
          action = 'version', version = '%(prog)s ' + self.version
        )

      if not self.epilog:
          self.cli_menu.epilog = None

      if self.tbgroup:
        self.addGroup(title = 'Testing and Benchmarking', description = 'test and benchmark options')
        self.addGroupOption(
          '-t', '--t', '--test',
          dest = '_test_s', action = 'store_true', default = False,
          help = 'run module unit test: silent mode'
        )
        self.addGroupOption(
          '-T', '--T', '--TEST',
          dest = '_test_v', action = 'store_true', default = False,
          help = 'run module unit test: verbose mode'
        )
        self.addGroupOption(
          '-b', '--b', '--benchmark',
          dest = '_benchmark', action = 'store', type = int, metavar = '<int>',
          help = 'run the module <int> times'
        )
      else:
        if self.test:
          self.addOption(
            '-t', '--t', '--test',
            dest = '_test_s', action = 'store_true', default = False,
            help = 'run module unit test: silent mode'
          )
          self.addOption(
            '-T', '--T', '--TEST',
            dest = '_test_v', action = 'store_true', default = False,
            help = 'run module unit test: verbose mode'
          )
        if self.benchmark:
          self.addOption(
            '-b', '--b', '--benchmark',
            dest = '_benchmark', action = 'store', type = int, metavar = '<int>',
            help = 'run the module <int> times'
          )




def __main__():
  """
  called from cli
  """
  menu = OptionsMenu(
    description = "meppy standard cli menu options.",
    modinfo = __epilog__,
  )
  menu.create()


if __name__ == '__main__':
  __main__()


