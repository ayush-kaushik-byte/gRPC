import os
import sys
import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc
import calculator


def main():
    os.environ['GRPC_VERBOSITY'] = 'debug'
    a = "unused variable."
    class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

        def SquareRoot(self, request, context):
            response = calculator_pb2.Number()
            response.value = calculator.square_root(request.value)
            return response

        def Multiply(self, request, context):
            response = calculator_pb2.Number()
            response.value = calculator.multiply(request.val1, request.val2)
            return response

    #server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server = grpc.server(futures.ThreadPoolExecutor())
    server_creds = grpc.alts_server_credentials()
    print(f'printing server credentials : {server_creds}')

    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    #server.add_secure_port('localhost:50051', server_creds)
    server.start()

    b = False
    if b:
        print("hey this is a dead code block!!!")

    return 1
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    
    main()