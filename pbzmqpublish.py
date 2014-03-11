import zmq
import time
import sys
import binascii
import google.protobuf.text_format

# protoc output for testmsg.proto:
from testmsg_pb2 import *

if len(sys.argv) < 2:
    print "usage: python %s <ip address to listen on>" % sys.argv[0]
    sys.exit(1)

print "ZMQ=%s pyzmq=%s" % (zmq.zmq_version(), zmq.pyzmq_version())

# adapt as needed
listen = sys.argv[1]
port = 4711
topic = "demo"


context = zmq.Context()
socket = context.socket(zmq.XPUB)
socket.bind("tcp://%s:%d" % (listen, port))

i = 0
# create example protobuf message:
c = Container()
c.type = MT_TEST1
c.note.append("beipacktext zeile 1")
c.note.append("beipacktext zeile 2")

p = c.pin.add()
p.name = "pi"
p.type = HAL_FLOAT
p.halfloat = 3.14

p = c.pin.add()
p.name = "e"
p.type = HAL_FLOAT
p.halfloat = 2.71828

print "payload:", c.ByteSize()
print "text format:", str(c)
buffer = c.SerializeToString()
print "wire format length=%d %s" % (len(buffer), binascii.hexlify(buffer))

while True:

    i += 1
    msg = "message %d" % (i)
    socket.send_multipart([topic, buffer])
    time.sleep(1)
