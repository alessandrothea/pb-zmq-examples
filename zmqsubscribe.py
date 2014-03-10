import zmq
import sys

if len(sys.argv) < 2:
    print "usage: python %s <target ip address>" % sys.argv[0]
    sys.exit(1)

print "ZMQ=%s pyzmq=%s" % (zmq.zmq_version(), zmq.pyzmq_version())

dest = sys.argv[1]
port = 4711
topics = ["demo", "foo"]


context = zmq.Context()
socket = context.socket(zmq.XSUB)
socket.connect("tcp://%s:%d" % (dest, port))

# subscribe XSUB-style to all topics of interest
for t in topics:
    socket.send("\001%s" % t)

while True:
    (topic, msg) = socket.recv_multipart()
    print "topic='%s' content='%s'" % (topic, msg)
