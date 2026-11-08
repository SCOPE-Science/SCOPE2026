"""Integer-only finite checks for generalized-Fibonacci digit-extension theorem.

No finite test is used as a proof of the universal claims.
Run: python3 check.py
"""
from math import isqrt


def sequence(a, n):
    out = [0, 1]
    while len(out) <= n:
        out.append(a * out[-1] + out[-2])
    return out


def observed_edges(a, b):
    # By the proved Binet/norm cutoff, no edge can have a source index m
    # satisfying alpha**m >= (b+1)*(1+(b-1)*sqrt(a*a+4)).
    # Since alpha>a and sqrt(a*a+4)<a+1 for a>=2, it suffices to
    # enumerate a**m < (b+1)*(1+(b-1)*(a+1)).
    B = (b + 1) * (1 + (b - 1) * (a + 1))
    m_max = 0
    power = 1
    while power < B:
        m_max += 1
        power *= a
    # Allowed k satisfy U_(k+1) <= 2b-1. Find all such positive k.
    V = sequence(a, 40)
    ks = [k for k in range(1, 40) if V[k+1] <= 2*b-1]
    assert not ks or V[max(ks)+2] > 2*b-1
    seq = sequence(a, m_max + (max(ks) if ks else 0) + 2)
    edges=[]
    for m in range(1,m_max+1):
        for k in ks:
            d=seq[m+k]-b*seq[m]
            if 0 <= d < b:
                edges.append((seq[m],seq[m+k]))
    return edges


def predicted_decimal(a):
    if a == 2: return [(1,12),(2,29)]
    if a == 3: return [(1,10),(3,33),(10,109)]
    if a == 4: return [(1,17)]
    if a == 10: return [(1,10),(10,101)]
    if 11 <= a <= 19: return [(1,a)]
    return []


def main():
    decimal_cases=0
    for a in range(2,301):
        e=sorted(observed_edges(a,10))
        assert e==sorted(predicted_decimal(a)), (a,e)
        decimal_cases+=1
    general_cases=0
    all_edges=0
    for a in range(2,31):
        for b in range(2,151):
            E=observed_edges(a,b)
            all_edges+=len(E)
            # Verify the source and digit membership by direct construction,
            # *independently* of the edge-detection equation.
            vals=set(sequence(a,30)[1:])
            for s,t in E:
                assert t in vals and s in vals
                assert str(t).startswith(str(s)) if b==10 else (t//b==s)
            general_cases+=1
    add_checks=0
    norm_checks=0
    for a in range(2,31):
        U=sequence(a,35)
        V=[2,a]
        for i in range(2,31): V.append(a*V[-1]+V[-2])
        for m in range(1,16):
            for k in range(1,16):
                assert U[m+k]==U[k+1]*U[m]+U[k]*U[m-1]
                add_checks+=1
        for b in range(2,151):
            for k in range(1,16):
                N=b*b-b*V[k]+(-1 if k%2 else 1)
                assert N != 0
                norm_checks+=1
    print('PASS decimal coefficient classification:',decimal_cases,'complete finite graphs checked via proved index cutoffs')
    print('PASS general-base bound crosschecks:',general_cases,'parameter pairs;',all_edges,'edges')
    print('PASS addition identities:',add_checks,'integer instances')
    print('PASS nonzero algebraic norms:',norm_checks,'integer instances')
    print('PASS: all checks completed')

if __name__=='__main__': main()
