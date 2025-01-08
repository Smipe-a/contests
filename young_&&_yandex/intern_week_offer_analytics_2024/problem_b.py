def get_minutes(time: str) -> int:
    hours, minutes = map(int, time.split(':'))
    return hours * 60 + minutes

if __name__ == '__main__':
    n, times = int(input()), input().split()
    minutes = sorted([get_minutes(time) for time in times])

    arrival = 1440 - minutes[-1] + minutes[0]
    for i in range(1, n):
        arrival = min(arrival, minutes[i] - minutes[i - 1])
    
    print(arrival)
