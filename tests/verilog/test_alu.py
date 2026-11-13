import cocotb
from cocotb.triggers import Timer

ALU_TEST_VECTORS = [
    [10, 20, 0, 30],
    [0, 0, 0, 0],
    [0xFFFFFFFF, 1, 0, 0],
    [0x7FFFFFFF, 1, 0, 0x80000000],
    [20, 10, 1, 10],
    [10, 20, 1, 0xFFFFFFF6],
    [0, 0, 1, 0],
    [0, 1, 1, 0xFFFFFFFF],
    [0b1100, 0b1010, 2, 0b1000],
    [0xFFFFFFFF, 0, 2, 0],
    [0xFFFFFFFF, 0xAAAAAAAA, 2, 0xAAAAAAAA],
    [0b1100, 0b1010, 3, 0b1110],
    [0, 0, 3, 0],
    [0xAAAAAAAA, 0x55555555, 3, 0xFFFFFFFF],
    [0b1100, 0b1010, 4, 0b0110],
    [0xFFFFFFFF, 0xFFFFFFFF, 4, 0],
    [0xAAAAAAAA, 0x55555555, 4, 0xFFFFFFFF],
    [1, 1, 5, 2],
    [5, 2, 5, 20],
    [1, 31, 5, 0x80000000],
    [1, 32, 5, 1],
    [16, 2, 6, 4],
    [0x80000000, 31, 6, 1],
    [0xFFFFFFFF, 4, 6, 0x0FFFFFFF],
    [16, 32, 6, 16],
    [0xFFFFFFF0, 2, 7, 0xFFFFFFFC],
    [0x80000000, 31, 7, 0xFFFFFFFF],
    [0x7FFFFFFF, 1, 7, 0x3FFFFFFF],
    [0xFFFFFFFF, 4, 7, 0xFFFFFFFF],
    [1, 2, 8, 1],
    [2, 1, 8, 0],
    [0xFFFFFFFF, 1, 8, 1],
    [1, 0xFFFFFFFF, 8, 0],
    [0x80000000, 0, 8, 1],
    [5, 5, 8, 0],
    [1, 2, 9, 1],
    [2, 1, 9, 0],
    [0xFFFFFFFF, 1, 9, 0],
    [1, 0xFFFFFFFF, 9, 1],
    [0x80000000, 0, 9, 0],
    [5, 5, 9, 0],
]


@cocotb.test()
async def test_alu_basic(dut):
    for vector in ALU_TEST_VECTORS:
        (
            dut.a.value,
            dut.b.value,
            dut.op.value,
            expected,
        ) = vector

        await Timer(1, unit="ns")
        assert int(dut.y.value) == expected