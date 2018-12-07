import zmq
import socket
import zmq_tools
import json
ctx = zmq.Context()
requester = ctx.socket(zmq.REQ)
# ip = '10.16.3.140'
ip = 'localhost'
port = 50020 
requester.connect('tcp://%s:%s'%(ip,port))
requester.send_string('SUB_PORT')
sub_port = requester.recv_string()

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
ipc_sub_url = 'tcp://%s:%s'%(ip, sub_port)
print(ipc_sub_url)
pupil_sub = zmq_tools.Msg_Receiver(ctx, ipc_sub_url, topics=('gaze',))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while True:
    try:
        print('Socket established. Waiting for connection...')
        conn, addr = s.accept()
        print('Connection address:', addr)
        while True:
            topic, pupil_datum = pupil_sub.recv()
            str_data = json.dumps(pupil_datum) + "\n"
            print(topic,':', str_data)
            conn.send(str_data.encode())
    except KeyboardInterrupt:
        raise
    except:
        print("Close connection, waiting for next connection...")
        conn.close()
