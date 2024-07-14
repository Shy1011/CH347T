from ch347 import *
import time
"""
两个问题 SPI 16/8bit如何切换
"""
dev = CH347()

"""List the device"""
dev.list_devices()

"""open device"""
print(dev.open_device())

"""close device"""
# print(dev.close_device())

"""device info"""
print(dev.get_device_info())

"""driver version"""
print(dev.get_version())

# """Test if USB is connected"""
# # dev.set_device_notify('HID\\VID_1A86&PID_55DC&MI_01#7&5D28A11&0&0000#')
while(1):
    # spiCon = SPIConfig()
    # spiCon.Mode = 0
    # spiCon.Clock = 5
    # spiCon.ByteOrder = 1
    # spiCon.SPIWriteReadInterval = 1
    # spiCon.SPIOutDefaultData = 0x0000
    # spiCon.ChipSelect = 0X80
    # spiCon.CS1Polarity = 0
    # spiCon.CS1Polarity = 0
    # spiCon.IsAutoDeativeCS = 1
    # spiCon.ActiveDelay = 2
    # spiCon.ActiveDelay = 2

    spiCo = SPIConfig()
    spiCo.Mode = 2
    spiCo.Clock = 5
    spiCo.ByteOrder = 1
    spiCo.SPIWriteReadInterval = 1
    spiCo.SPIOutDefaultData = 0x0000
    spiCo.ChipSelect = 0X81
    spiCo.CS1Polarity = 0
    spiCo.CS1Polarity = 0
    spiCo.IsAutoDeativeCS = 0
    spiCo.ActiveDelay = 2
    spiCo.ActiveDelay = 2

    """SPI init"""
    print("SPI init")
    # print(dev.spi_init(spiCon))


    # """SPI Config"""
    # print("SPI Config")
    # print(dev.spi_get_cfg())

    """SPI Write"""
    # print("SPI Write")
    # print(dev.spi_write(0x80, bytes([0x00,0xFF])))
    # 如果这里出现问题就可能是因为CS pin没选对 或者chip_select写的不对
    # 另外还有一些延时
    # 另外这里还要测试一下这是发16 还是8 位,以及18 / 8 位发送设置怎么选
    # device_index = 0 是什么意思
    dev.spi_init(spiCo)
    print(dev.spi_write(0x91, bytes([0x00, 0xFF])))
    # dev.spi_change_cs(1)


    # """SPI read"""
    # print("SPI Read")
    # print(dev.spi_read(0X80, bytes([0x00,0x00]), 4))

    time.sleep(0.1)
# """Speed Set"""
# print("IIC Set")
# print(dev.i2c_set(0))

# """IIC Stream"""
# print("IIC Stream")
# print(dev.stream_i2c(bytes([0xFF,0x88]), 2))

# """GPIO Get"""
# print("GPIO Get")
# print(dev.CH347GPIO_Get())




"""close device"""
print("Close Device")
print(dev.close_device())