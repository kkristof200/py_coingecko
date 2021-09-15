import time

from kcu import ktime

def s_to_int(s: str) -> int:
    base_val = int(''.join([c for c in s if c.isdigit()]))

    if 'hour' in s:
        return int(time.time()) - base_val * ktime.seconds_in_hour

    if 'day' in s:
        return int(time.time()) - base_val * ktime.seconds_in_day

    return int(time.time()) - base_val * ktime.seconds_in_day * 30

print(s_to_int('about 2 hours'))
print(s_to_int('about 27 days'))
print(s_to_int('about 5 months'))