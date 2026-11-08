"""Finite verification of an exact quartic-graph additive-energy recurrence."""
from math import prod


def legendre(a, p):
    b = pow(a % p, (p-1)//2, p)
    return 0 if b == 0 else (1 if b == 1 else -1)


def predicted(p, k):
    assert p >= 5 and all(p % d for d in range(2, int(p**.5)+1))
    chi = legendre(-3, p)
    n2 = (p-1) * (3 + 2*chi)
    n1 = 3*(p*p-1) - 2*n2
    seq = {0: 1}
    for i in range(1, k+1):
        origin = p**(3*i-3) if i <= 4 else p**9 * seq[i-4]
        other = p**(2*i-2) * (n1 + n2*(p + (i-2)*(p-1)))
        seq[i] = origin + other
    return seq[k]


def direct(p, k):
    q = p**k
    xsq = [(a*a) % q for a in range(q)]
    r = 0
    for s in range(q):
        w = (12*s*s) % q
        for u in range(q):
            if u == 0:
                r += q
                continue
            uu = xsq[u]
            for v in range(q):
                if (u*v*(uu+xsq[v]+w)) % q == 0:
                    r += 1
    return r


def direct_graph(q):
    reps = {}
    for x in range(q):
        for y in range(q):
            key = ((x+y) % q, (pow(x,4,q) + pow(y,4,q)) % q)
            reps[key] = reps.get(key, 0) + 1
    return sum(v*v for v in reps.values())


def main():
    cases = [(5,1),(5,2),(5,3),(7,1),(7,2),(11,1),(11,2),(13,1),(17,1),(19,1)]
    for p,k in cases:
        expected=predicted(p,k)
        observed=direct(p,k)
        assert observed==expected,(p,k,observed,expected)
        if p**k<=49:
            assert direct_graph(p**k)==expected,(p,k)
    # Consecutive squarefree products satisfy exact CRT multiplicativity.
    for q, factors in [(35,[(5,1),(7,1)]),(55,[(5,1),(11,1)]),(77,[(7,1),(11,1)]),(65,[(5,1),(13,1)])]:
        assert direct_graph(q)==prod(predicted(p,k) for p,k in factors)
    for p in (5,7,11,13,17,19):
        c=legendre(-3,p)
        n2=(p-1)*(3+2*c)
        n1=3*(p*p-1)-2*n2
        z0=z1=z2=0
        for s in range(p):
            for u in range(p):
                for v in range(p):
                    if not (s or u or v):
                        z0+=1
                        continue
                    zeros=(u==0)+(v==0)+((u*u+v*v+12*s*s)%p==0)
                    if zeros==1: z1+=1
                    elif zeros==2: z2+=1
                    else: assert zeros in (0,)
        assert (z0,z1,z2)==(1,n1,n2),(p,(z0,z1,z2),(1,n1,n2))
    print(f'VERIFY_OK prime_power_cases={len(cases)} squarefree_cases=4 primitive_strata=6 max_prime_power=125')

if __name__=='__main__': main()
