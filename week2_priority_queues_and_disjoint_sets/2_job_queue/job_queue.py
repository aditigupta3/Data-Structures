# python3

from collections import namedtuple
from heapq import heappush, heappop

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # We use a heap implementation for this.
    heaptimes = [(0, i) for i in range(n_workers)]
    result = list()
    for j, job in enumerate(jobs):
        free_time = heappop(heaptimes)
        heappush(heaptimes, (free_time[0]+job, free_time[1]))
        result.append(AssignedJob(free_time[1], free_time[0]))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
