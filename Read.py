from harvesters.core import Harvester
from genicam.gentl import TimeoutException

h=Harvester()
h.add_file("/home/user/Senv/lib/python3.8/site-packages/genicam/TLSimu.cti")

h.update()
# print(h.device_info_list)

ia=h.create({'serial_number':'SN_InterfaceA_0'})
# print(DeviceInfo.search_keys)

ia.start()
with ia.fetch() as buffer:
    print(buffer)
buffer=ia.fetch()
print(buffer)
buffer.queue()

buffer=ia.try_fetch(timeout=3)
if buffer:
    print(123)