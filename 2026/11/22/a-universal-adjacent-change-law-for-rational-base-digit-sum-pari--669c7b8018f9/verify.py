"""Independent finite checks for rational-base parity transition identities.

Run with Python 3: python verify.py
This is finite verification only; the proof is in RESULT.md.
"""
from math import gcd


def digit_parity(n, a, b):
    """Parity of digit sum for rational radix b/a, 1 <= a < b."""
    z = 0
    while n:
        n, d = divmod(a * n, b)
        z ^= d & 1
    return z


def recurrence_parities(a, b, maximum):
    vals = [0] * (maximum + 1)
    for n in range(1, maximum + 1):
        k, d = divmod(a * n, b)
        assert k < n
        vals[n] = vals[k] ^ (d & 1)
    return vals


def run():
    cases = 0
    exacts = 0
    for b in range(2, 23):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            vals = recurrence_parities(a, b, 3000)
            for n in range(0, 3000, 31):
                assert vals[n] == digit_parity(n, a, b)
                exacts += 1
            diff = [int(vals[n] != vals[n+1]) for n in range(3000)]
            prefix = [0]
            for d in diff:
                prefix.append(prefix[-1] + d)
            for N in (0, 1, 2, 3, 5, 13, 29, 71, 113):
                if (a & 1) and (b & 1):
                    assert prefix[N] == N
                    assert all(vals[n] == (n & 1) for n in range(3000))
                else:
                    t = a if not (a & 1) else b
                    assert prefix[b*N] + prefix[a*N] == t*N
                    # Directly enumerate every edge in b-blocks and compare
                    # its jump status and corresponding input edge.
                    for r in range(b):
                        u, v = (a*r)//b, (a*(r+1))//b
                        assert v-u in (0, 1)
                        x_l = vals[b*N+r] if b*N+r < len(vals) else None
                        x_r = vals[b*N+r+1] if b*N+r+1 < len(vals) else None
                        if x_l is not None and x_r is not None:
                            z0 = vals[a*N+u] ^ ((a*r-b*u)&1)
                            z1 = vals[a*N+v] ^ ((a*(r+1)-b*v)&1)
                            assert (z0,z1) == (x_l,x_r)
                    exacts += 1
            cases += 1
    # Larger complete, independent computations across different rational bases.
    for a,b,N in ((2,3,25000),(3,4,18000),(4,5,20000),(2,7,18000),
                   (5,6,15000),(7,8,15000)):
        vals=recurrence_parities(a,b,N)
        flips=sum(vals[k]!=vals[k+1] for k in range(N))
        beta=(a if a%2==0 else b)/(a+b)
        assert abs(flips-beta*N)<b*(3+N.bit_length())
        exacts+=1
    print(f'PASS {cases} coprime bases; {exacts} independent identities and checks')

if __name__ == '__main__':
    run()
