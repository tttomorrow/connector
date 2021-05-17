##
# .test.testall
##
import unittest
from sys import stderr

from ..installation import default

from .test_exceptions import *
from .test_bytea_codec import *
from .test_iri import *
from .test_protocol import *
from .test_configfile import *
from .test_pgpassfile import *
from .test_python import *

from .test_installation import *
from .test_cluster import *

# Expects PGINSTALLATION to be set. Tests may be skipped.
from .test_connect import *
from .test_ssl_connect import *

try:
	from .test_optimized import *
except ImportError:
	stderr.write("NOTICE: port.optimized could not be imported\n")

from .test_driver import *
from .test_alock import *
from .test_notifyman import *
from .test_copyman import *
from .test_lib import *
from .test_dbapi20 import *
from .test_types import *

if __name__ == '__main__':
	unittest.main()
