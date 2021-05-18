import grpc

import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
# channel_creds = grpc.alts_channel_credentials()
# channel = grpc.secure_channel('localhost:50051', channel_creds)


stub = calculator_pb2_grpc.CalculatorStub(channel)

number = calculator_pb2.Number(value=39)
response = stub.SquareRoot(number)
print(response.value)

numbers = calculator_pb2.Numbers(val1=10, val2=20)
response = stub.Multiply(numbers)
print(response.value)
