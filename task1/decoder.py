import base64
from Crypto.Cipher import AES

DATA = "bVRHZWxqaERSS0FTS0toUSxGTHJzU0V2ZVFRaWxvUFJuLFhlZFhIWUJVSHBJWERCSlAsSU9HUEVyam9zeE5pUXJOTSxSenZwYkVVUkxkRmZhR0ZNLHZkQlZEQ3ZpeGpTaENRdnksRVFsY3NuVXR6Q0h5RlBITSxKa0RpamdBRmlWQldKYUx6LGdoY1BJT1NxQ2RDVHFPcEQsRG5lQ3dia0RIa29qcHBIbSxsVlJaUmVBbGFJekhnaXNjLE5kamNnVlZqaWlueGZ0Q0MsUmtnTHBSQ3FybmlicnFzTixremV3dGVBZ1BFWmRrelFKLEhucEdvVWVxY2tFcXhwUW0sTFNOV1JhclRoUmRpUExwTQ=="

def key_from_data():
    b64_decoded_data = base64.b64decode(DATA)
    b64_key = b64_decoded_data[-16:]
    return b64_key.decode('ascii')

def decode_key(key):
    with open('secrets.txt.enc', 'rb') as file:
        d = file.read()
        decipher = AES.new(key.encode("utf8"), AES.MODE_ECB)
        print(decipher.decrypt(d))

if __name__ == '__main__':
    key = key_from_data()
    print (key)
    decode_key(key)

