import cocotb


@cocotb.test()
async def tb_helloworld(dut):
    dut._log.info("See below message!")
