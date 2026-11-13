import cocotb
from cocotb.triggers import Timer

# req1, req2, s1, y
BOOLEAN_TEST_VECTORS = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
]


@cocotb.test()
async def test_mux2_basic(dut):
    for vector in BOOLEAN_TEST_VECTORS:
        dut.r1.value, dut.r2.value, dut.s1.value, expected = vector
        await Timer(1, units="ns")
        assert dut.y.value == expected
