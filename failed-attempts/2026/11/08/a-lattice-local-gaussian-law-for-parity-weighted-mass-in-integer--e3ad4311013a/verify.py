"""Exact rational/integer checks for the odd-minus-even partition mass law.
Run with python3 verify.py. Requires only Python's standard library.
"""
from math import exp, pi, sqrt

MAX_N = 1600


def ordinary_partitions(nmax):
    p = [0] * (nmax + 1)
    p[0] = 1
    for n in range(1, nmax + 1):
        s = 0
        k = 1
        while k*(3*k - 1)//2 <= n:
            e1 = k*(3*k - 1)//2
            e2 = k*(3*k + 1)//2
            sign = 1 if k % 2 else -1
            s += sign * p[n - e1]
            if e2 <= n:
                s += sign * p[n - e2]
            k += 1
        p[n] = s
    return p


def odd_parts_partitions(nmax):
    q = [0] * (nmax + 1)
    q[0] = 1
    for k in range(1, nmax+1, 2):
        for n in range(k, nmax+1):
            q[n] += q[n-k]
    return q


def direct_hist(n):
    ans = {}
    def visit(left, top, difference):
        if left == 0:
            ans[difference] = ans.get(difference, 0) + 1
            return
        for part in range(min(left, top), 0, -1):
            visit(left-part, part, difference + (part if part & 1 else -part))
    visit(n,n,0)
    return ans


def exact_hist(n, p, q):
    return {d: p[(n-d)//4]*q[(n+d)//2]
            for d in range(-n, n+1) if (n-d)%4 == 0}


def test():
    p = ordinary_partitions(MAX_N)
    q = odd_parts_partitions(MAX_N)
    tested = 0
    for n in range(1, 201):
        h = exact_hist(n, p, q)
        assert sum(h.values()) == p[n], (n, 'mass identity')
        assert all(z > 0 for z in h.values())
        tested += len(h)
    for n in range(1, 23):
        h = exact_hist(n, p, q)
        assert h == direct_hist(n), (n,'direct enumeration')
    print('EXACT_FIBERS_OK n=1..200 direct_enumeration=1..22 lattice_cells=', tested)
    sig2 = 2*sqrt(6)/pi
    normal0 = 4/sqrt(2*pi*sig2)
    prev_error = 1.0
    for n in (200,400,800,1600):
        h=exact_hist(n,p,q)
        sum1=sum(d*a for d,a in h.items())
        sum2=sum(d*d*a for d,a in h.items())
        mean=float(sum1/p[n]); variance=float(sum2/p[n] - (sum1/p[n])**2)
        center = n%4
        if center > 2: center -= 4
        mass = h[center]/p[n]
        ratio = (mass*n**0.75/normal0)
        assert 0.7 < ratio < 1.2, (n, ratio)
        assert 0.7 < variance/(sig2*n**1.5)<1.2
        print('MOMENT n={} expected_mass={:.8f} var_over_n^1.5={:.8f} local_ratio={:.8f}'.format(n,mean,variance/n**1.5,ratio))
    assert abs(float(exact_hist(4,p,q)[0]/p[4]) - 0.2)<1e-12
    print('VERIFY_OK exact_arithmetic=yes independent_partition_enumeration=yes normal_scale=',sig2)

if __name__ == '__main__':
    test()
