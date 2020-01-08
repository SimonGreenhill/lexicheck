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
    sys.stdout.write("\r%s %s" % (message.ljust(60), status))
    if end:
        sys.stdout.write("\n")
    sys.stdout.flush()


def check(dataset, args):
    print(dataset)
    print(dir(dataset))
    functions = {
        f[0]: f[1] for f in inspect.getmembers(checkers)
        if inspect.isfunction(f[1])
    }
    for name in sorted(functions):
        funct = functions[name]
        message = " - %s" % (funct.__doc__ if funct.__doc__ else name)
        log(message, '....')
        rv = funct(dataset)
        log(message, rv, True)




