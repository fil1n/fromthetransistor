import cocotb
from cocotb.triggers import Timer

BOOLEAN_TEST_VECTORS = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # s = 000 -> selects r1
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],  # s = 001 -> selects r2
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # s = 010 -> selects r3
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],  # s = 011 -> selects r4
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],  # s = 100 -> selects r5
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],  # s = 101 -> selects r6
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],  # s = 110 -> selects r7
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],  # s = 111 -> selects r8
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # s = 000 -> selects r1 (0)
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],  # s = 111 -> selects r8 (0)
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],  # s = 010 -> selects r3 (1)
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0],  # s = 011 -> selects r4 (0)
]


@cocotb.test()
async def test_mux8_basic(dut):
    for vector in BOOLEAN_TEST_VECTORS:
        (
            dut.r1.value,
            dut.r2.value,
            dut.r3.value,
            dut.r4.value,
            dut.r5.value,
            dut.r6.value,
            dut.r7.value,
            dut.r8.value,
            dut.s1.value,
            dut.s2.value,
            dut.s3.value,
            expected,
        ) = vector

        await Timer(1, units="ns")
        assert dut.y.value == expected
