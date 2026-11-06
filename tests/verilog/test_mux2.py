import cocotb


@cocotb.test()
async def test_mux_basic(dut):
    dut.r1.value = 1
    dut.r2.value = 0
    dut.s1.value = 0
    assert dut.y.value == 0
