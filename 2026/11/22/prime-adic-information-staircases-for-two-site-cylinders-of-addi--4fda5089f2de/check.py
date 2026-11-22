"""Independent finite verification of a two-site information persistence theorem.

No external packages. Enumerative tests are diagnostics only, not an infinite proof.
"""
from itertools import product
from math import comb


def valuation(n, p):
    if n == 0:
        raise ValueError('valuation of zero')
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def exponent(p, r, d, t):
    if t < 1:
        raise ValueError('positive time required')
    if t == 1:
        return r
    a = valuation(d, p)
    j = 0
    h = t - 1
    while h >= p:
        h //= p
        j += 1
    return min(r, max(a - j, 0))


def quotient_remainder(A, divisor):
    """Polynomial division of integer ascending coefficient arrays by monic polynomial."""
    rem = A[:]
    while len(rem) > 1 and rem[-1] == 0:
        rem.pop()
    n = len(divisor) - 1
    if len(rem) <= n:
        return [0], rem
    q = [0] * (len(rem) - n)
    for k in range(len(q) - 1, -1, -1):
        v = rem[k + n]
        q[k] = v
        for j in range(n + 1):
            rem[k + j] -= v * divisor[j]
    assert all(v == 0 for v in rem[n:])
    return q, rem[:n]


def quotient_B(d, t):
    assert 1 <= t <= d
    A = [0] * (d + 1)
    A[0] = -(-1)**d
    A[d] = 1
    return quotient_remainder(A, [comb(t,j) for j in range(t+1)])


def direct_index(p, r, d, t):
    modulus = p ** r
    divisor = [comb(t,j) for j in range(t + 1)]
    allowed = 0
    for c in range(modulus):
        A = [0] * (d+1)
        A[0] = -((-1)**d)*c
        A[d] = c
        _, rem = quotient_remainder(A, divisor)
        if all(v % modulus == 0 for v in rem):
            allowed += 1
    return allowed


def check_modular_division():
    cases = 0
    for p in [2, 3, 5]:
        for r in [1,2,3]:
            if p**r > 125: continue
            for d in range(1, 22):
                for t in range(1, d + 3):
                    got = direct_index(p, r, d, t)
                    expected = p ** exponent(p,r,d,t)
                    assert got == expected, ('index mismatch', p,r,d,t,got,expected)
                    cases += 1
    return cases


def check_kernel_projection():
    cases = 0
    for p,r in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)]:
        m=p**r
        for d in range(1,11):
            for t in range(1,min(d+2,5)):
                if m**t > 10000: continue
                seen=set()
                for init in product(range(m),repeat=t):
                    x=list(init)
                    for i in range(max(d-t+1,0)):
                        x.append(-sum(comb(t,j)*x[i+j] for j in range(t)) % m)
                    seen.add((x[0], x[d] if d < len(x) else x[d]))
                expected=m*m//(p**exponent(p,r,d,t))
                assert len(seen)==expected, ('kernel projection',p,r,d,t,len(seen),expected)
                cases+=1
    return cases


def check_explicit_decoders():
    cases=0
    for p,r in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)]:
        m=p**r
        for d in range(1,15):
            for t in range(1,d+1):
                e=exponent(p,r,d,t)
                if not e:continue
                q,rem=quotient_B(d,t)
                assert len(q)==d-t+1
                assert q[-1] == 1
                assert all(v%(p**e)==0 for v in rem)
                for k in range(6):
                    x=[(k+3*i*i+5*i+2*i*k)%m for i in range(d+1)]
                    y=[sum(comb(t,j)*x[i+j] for j in range(t+1))%m for i in range(d-t+1)]
                    lhs=sum(a*b for a,b in zip(q,y))%(p**e)
                    rhs=(x[d]-((-1)**d)*x[0])%(p**e)
                    assert lhs==rhs,(p,r,d,t,k,lhs,rhs)
                    cases+=1
    return cases


def run():
    a=check_modular_division()
    b=check_kernel_projection()
    c=check_explicit_decoders()
    print('PASS: %d direct polynomial-divisibility index tests'%a)
    print('PASS: %d independent finite-kernel projection tests'%b)
    print('PASS: %d explicit decoding identities'%c)
    print('Total independent diagnostic instances:',a+b+c)

if __name__=='__main__':
    run()
