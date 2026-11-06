"""Pytest runner for cocotb tests. All cocotb tests must be placed in $ROOT/tests/verilog"""

import os
from pathlib import Path

import pytest
from cocotb_test.simulator import run

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VERILOG_TEST_DIR = PROJECT_ROOT / "tests"
VERILOG_SRC_DIR = PROJECT_ROOT / "verilog"


@pytest.mark.parametrize("sim", ["verilator"])
def test_mux2(sim):
    os.environ["SIM"] = sim

    run(
        verilog_sources=[os.path.join(VERILOG_SRC_DIR, "mux.v")],
        toplevel="mux2",
        module="verilog.test_mux2",
        python_search=[str(VERILOG_TEST_DIR)],
        always=False,
    )
