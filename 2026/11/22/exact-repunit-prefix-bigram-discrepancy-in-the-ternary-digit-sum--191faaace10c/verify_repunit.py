#!/usr/bin/env python3
"""Independent finite checks for ternary digit-sum adjacency-prefix theorem."""
from fractions import Fraction


def digit_sum_mod3(n):
    a = 0
    while n:
        n, d = divmod(n, 3)
        a = (a + d) % 3
    return a


def closed_count(r):
    n = (3**r-1)//2
    k, s = divmod(r, 3)
    if s == 0:
        return Fraction(3*n,13)-k
    if s == 1:
        return Fraction(3*n,13)+k+Fraction(10,13)
    return Fraction(3*n,13)+Fraction(1,13)


def digit_partition(r):
    total = 0
    for j in range(r):
        for c in range(0, j-1, 3):
            total += 2*3**(j-c-2)
        if j % 3 == 1 and r % 3 != 0:
            total += 1
        if j % 3 == 0 and r % 3 == 1:
            total += 1
    return total


s = [digit_sum_mod3(i) for i in range(3**12+1)]
f = [int(s[i]==0 and s[i+1]==1) for i in range(len(s)-1)]
prefix = [0]
for x in f:
    prefix.append(prefix[-1]+x)
for r in range(1,13):
    n = (3**r-1)//2
    a, b, c = prefix[n], digit_partition(r), closed_count(r)
    assert a == b == c, (r, n, a, b, c)
    print('r=%d N=%d A=%d 13*A-3*N=%d' % (r,n,a,13*a-3*n))
assert f[0]==1
assert any(s[i:i+2]==[0,0] for i in range(100))
assert any(s[i:i+2]==[1,1] for i in range(100))
for letter in range(3):
    for length in range(1,100):
        cnt = sum(s[j]==letter for j in range(length))
        vals=[cnt]
        for j in range(1, 2000-length+1):
            cnt += int(s[j+length-1]==letter)-int(s[j-1]==letter)
            vals.append(cnt)
        assert max(vals)-min(vals)<=2, (letter,length)
print('PASS: 12 exact large prefixes (up to 265720 adjacency starts), 297 window-letter checks, explicit sharp pair factors')
