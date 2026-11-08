#!/usr/bin/env python3
"""Independent elementary finite checks for explicit analytic branch/conductor formulas.
The universal theorem is proved mathematically; these are finite consistency checks.
Requires Python 3, standard library only.
"""
for m in range(4, 101):
    e = m - 3
    if m % 2 == 0:
        r = 4
        c = (2, 3, 3, m + 2)
        xord, yord, zord = (3*m-5, 2, m-1)
        assert e % 2 == 1 and zord % 2 == 1
        assert xord + yord == 3*zord
        assert yord + 2*zord == m*yord < xord + zord
        assert zord + 2*yord - 1 == m + 2
    else:
        r = 5
        c = (2, 3, 3, (m+3)//2, (m+3)//2)
        xord, yord, zord = ((3*m-5)//2, 1, (m-1)//2)
        assert e % 2 == 0
        assert xord + yord == 3*zord
        assert yord + 2*zord == m*yord < xord + zord
        assert zord + yord + 1 == (m+3)//2
    assert all(v > 0 for v in c)
    delta = sum(c)//2
    assert sum(c) == 2*delta
    assert 2*delta-r+1 == m+7
    assert sum(k-1 for k in c) == m+6
print('PFISTER_BRANCH_PARITY_AND_CONDUCTOR_CHECK_OK 97 m=4..100')
