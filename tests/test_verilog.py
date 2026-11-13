"""
Pytest runner for cocotb tests. All cocotb tests must be placed in $ROOT/tests/verilog
"""

import os
from pathlib import Path

from cocotb_test.simulator import run

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VERILOG_TEST_DIR = PROJECT_ROOT / "tests"
VERILOG_SRC_DIR = PROJECT_ROOT / "verilog"


def test_mux2to1():
    run(
        verilog_sources=[os.path.join(VERILOG_SRC_DIR, "mux.sv")],
        toplevel="mux2to1",
        module="verilog.test_mux2",
        python_search=[str(VERILOG_TEST_DIR)],
        always=False,
    )


def test_mux8to1():
    run(
        verilog_sources=[os.path.join(VERILOG_SRC_DIR, "mux.sv")],
        toplevel="mux8to1",
        module="verilog.test_mux8",
        python_search=[str(VERILOG_TEST_DIR)],
        always=False,
    )
