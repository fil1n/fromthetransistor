import os

import pytest


@pytest.fixture(autouse=True)
def set_simulator():
    os.environ["SIM"] = "verilator"
