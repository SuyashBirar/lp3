
def job_sequencing(jobs):
    # Sort jobs by descending profit
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Initialize time slots
    slots = [None] * max_deadline

    total_profit = 0
    selected_jobs = []

    # Schedule jobs
    for job in jobs:
        job_id, deadline, profit = job

        # Find the latest available slot
        for t in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[t] is None:
                slots[t] = job_id
                total_profit += profit
                selected_jobs.append(job_id)
                break

    # Display results
    print("Scheduled Jobs:", end=" ")

    for job in slots:
        if job is not None:
            print(job, end=" ")

    print("\nMaximum Profit:", total_profit)


# Main program
n = int(input("Enter the number of jobs: "))

jobs = []

for i in range(n):
    job_id = input("Enter Job ID: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append((job_id, deadline, profit))

job_sequencing(jobs)
