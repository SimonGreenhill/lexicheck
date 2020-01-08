"""
Runs checks on a specified dataset.
"""
import sys
import inspect
from cldfbench.cli_util import with_dataset
from pylexibank.cli_util import add_dataset_spec
from lexicheck import checkers

def register(parser):
    add_dataset_spec(parser)


def run(args):
    with_dataset(args, check)


def log(message, status, end=False):
    sys.stdout.write("\r%s %s" % (message.ljust(70), status))
    if end:
        sys.stdout.write("\n")
    sys.stdout.flush()


def check(dataset, args):
    checks = {
        f[0]: f[1] for f in inspect.getmembers(checkers)
        if inspect.isclass(f[1])
        and f[1].__module__.startswith("lexicheck.checkers")
    }
    
    cldf = dataset.cldf_reader()
    for name, checker in checks.items():
        c = checker(dataset, cldf)
        message = "%s" % (c.__doc__ if c.__doc__ else name)
        log(message, '....')
        rv = c.check()
        log(message, rv, True)
        if not rv:
            for e in c.errors:
                print(" - %s" % e)




