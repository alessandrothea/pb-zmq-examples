import zmq
import time
import sys

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
while True:
    i += 1
    msg = "message %d" % (i)
    socket.send_multipart([topic, msg])
    time.sleep(1)
