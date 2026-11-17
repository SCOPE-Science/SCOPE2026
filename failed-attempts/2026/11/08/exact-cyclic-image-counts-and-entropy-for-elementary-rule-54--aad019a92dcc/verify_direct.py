#!/usr/bin/env python3
"""Independent finite-image enumeration using a cellular local-rule bit formula."""

def direct_count(n):
    limit = 1 << n
    mask = limit - 1
    seen = bytearray(limit)
    for x in range(limit):
        # At site i the two adjacent bits are the rotated copies of x.
        left = ((x << 1) | (x >> (n-1))) & mask
        right = ((x >> 1) | (x << (n-1))) & mask
        y = x ^ (left | right)  # rule-54 truth table
        seen[y] = 1
    return sum(seen)

def recurrence():
    # A_n is the number of indexed attainable outputs, n>=1.
    a = [1,1,2,5,14,22,41,79]
    for n in range(8,19):
        a.append(2*a[n-1]-a[n-2]+a[n-3]+a[n-4]-a[n-5]+a[n-6])
    return a

def run():
    a=recurrence()
    for n in range(1,19):
        actual=direct_count(n)
        assert actual==a[n], (n,actual,a[n])
    print('DIRECT_IMAGE_ENUMERATION_OK',18,'ring lengths')
    print('IMAGE_COUNTS',a[1:19])

if __name__ == '__main__':
    run()
