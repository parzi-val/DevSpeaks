# middleware.py

import time

class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        
        # Calculate response time
        response_time = end_time - start_time

        # Write response time data to a text file
        with open('response_times.txt', 'a') as file:
            file.write(f'Response Time: {response_time} seconds\n')

        return response
