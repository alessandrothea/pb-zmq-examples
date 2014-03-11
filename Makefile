
all: testmsg_pb2.py testmsg.pb.cc testmsg.pb.hh


testmsg_pb2.py: 	testmsg.proto
	protoc --python_out=. testmsg.proto

testmsg.pb.cc testmsg.pb.hh:		testmsg.proto
	protoc --cpp_out=. testmsg.proto


