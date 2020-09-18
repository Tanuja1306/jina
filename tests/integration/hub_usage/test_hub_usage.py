import os
import subprocess

import pytest

from jina.docker.hubio import HubIO
from jina.excepts import PeaFailToStart
from jina.executors import BaseExecutor
from jina.flow import Flow
from jina.main.parser import set_pod_parser, set_hub_build_parser
from jina.peapods import Pod

cur_dir = os.path.dirname(os.path.abspath(__file__))


def test_simple_use_abs_import_shall_fail():
    with pytest.raises(ModuleNotFoundError):
        from .testhub_abs_import import ImageResizer
        ImageResizer()

    with pytest.raises(PeaFailToStart):
        with Flow().add(uses='ImageResizer'):
            pass


def test_simple_use_relative_import():
    from .testhub_relative_import import ImageResizer
    ImageResizer()

    with Flow().add(uses='ImageResizer'):
        pass


def test_use_from_hub_dir():
    with Flow().add(uses='jina/hub/crafters/image/ImageResizer/config.yml'):
        pass


def test_use_from_local_dir_exe_level():
    with BaseExecutor.load_config('testhub/config.yml'):
        pass


def test_use_from_local_dir_pod_level():
    a = set_pod_parser().parse_args(['--uses', 'testhub/config.yml'])
    with Pod(a):
        pass


def test_use_from_local_dir_flow_level():
    with Flow().add(uses='testhub/config.yml'):
        pass


def test_use_from_local_dir_flow_container_level():
    args = set_hub_build_parser().parse_args(
        [os.path.join(cur_dir, 'testhub'), '--test-uses', '--raise-error'])
    HubIO(args).build()

    with Flow().add(uses='jinahub/pod.crafter.imageresizer:0.0.0'):
        pass


def test_use_from_cli_level():
    subprocess.check_call(['jina', 'pod', '--uses',
                           os.path.join(cur_dir, 'testhub/config.yml'),
                           '--shutdown-idle', '--max-idle-time', '5'])
