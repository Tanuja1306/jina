import os

from .base import get_logger

default_logger = get_logger('JINA')  #: a logger at the global-level

if 'JINA_LOG_PROFILING' in os.environ:
    profile_logger = get_logger('PROFILE', log_profile=True)  #: a logger for profiling
    default_logger.success('profiling is enabled')
else:
    profile_logger = default_logger
