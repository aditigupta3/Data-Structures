# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def buffer_avlbl(self):
        return len(self.finish_time) < self.size


def process_requests(requests, buffer):
    """
    Function to process all requests given the buffer using deque.
    """
    if not requests:
        return []
    result = list()
    for i in range(len(requests)):
        start_time = requests[i].arrived_at
        while buffer.finish_time:
            # remove all requests from the deque that have
            # already been processed by the time this request arrives
            if buffer.finish_time[0] <= start_time:
                buffer.finish_time.popleft()
            else:
                break
        if buffer.buffer_avlbl():
            # If there is space available in the buffer, the request will be processed
            if len(buffer.finish_time) > 0:
                # if there is something in the queue, processing of the packet will 
                # start ony when processing of the previous request has been completed
                start_time = buffer.finish_time[-1] #, requests[i].arrived_at)
            buffer.finish_time.append(start_time + requests[i].time_to_process)
            result.append(Response(False, start_time))
        else:
            # If there is no space in the buffer, the request will not be processed
            result.append(Response(True, start_time))
    return result


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
