#!/usr/bin/env python3
"""Exact integer certificate for the eventual complete symmetry cutoff of (17,18,19)."""

def coefficient_table(N):
    r=[0]*(N+1);r[0]=1
    for a in (17,18,19):
        for n in range(a,N+1): r[n]+=r[n-a]
    return r

def poly(v):
    out=[0]*(max(v)+1)
    for k,x in v.items():out[k]=x
    return out

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        if u:
            for j,v in enumerate(b):
                if v:c[i+j]+=u*v
    return c

def minus(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]-=x
    return c

def main():
    L=17*18*19
    r=coefficient_table(2*L+2)
    # Direct independent triple counting for 101 small indices and the terminal obstruction.
    for n in list(range(101))+[2394,2395]:
        direct=sum(1 for z in range(n//19+1) for y in range((n-19*z)//18+1)
                   if (n-19*z-18*y)%17==0)
        assert r[n]==direct, (n, direct, r[n])
    d=[r[j+1]-r[j] for j in range(L)]
    assert min(d)==-1
    drops=[j for j,v in enumerate(d) if v<0]
    assert len(drops)==120 and drops[-1]==2394
    assert d[2394]==-1 and (r[2394],r[2395])==(505,504)
    assert max((r[j],j) for j in drops)==(505,2394)
    B=[1]
    for a in (17,18,19):B=multiply(B,poly({0:1,a:-1}))
    # D(x)=sum_{n>=0}(r(n+1)-r(n))x^n=((1-x)-B)/(xB).
    # Certificate: (1-x)(1-x^L)((1-x)-B) = xB((1-x)Q+x^L),
    # with Q=sum_{j=0}^{L-1} d(j)x^j.
    left=multiply(multiply(poly({0:1,1:-1}),poly({0:1,L:-1})),
                  minus(poly({0:1,1:-1}),B))
    c=multiply(poly({0:1,1:-1}),d)
    c += [0]*max(0,L+1-len(c))
    c[L]+=1
    right=multiply(poly({1:1}),multiply(B,c))
    residual=minus(left,right)
    assert not any(residual)
    for j in range(L):
        assert r[j+L+1]-r[j+L]==d[j]+1
    # All negative d(n) occur in the first full period; maximum predecessor 505.
    # A decreasing step from r(n)>505 would contradict the certified maximum.
    for p in (44,100,504,505,600,1000):
        S=[v>p for v in r]
        if p >= 505:
            first=S.index(True)
            assert all(S[first:])
    assert r[2394]>504 and r[2395]<=504
    print('VERIFY_OK')
    print('generators=17,18,19')
    print('independent_direct_coefficient_checks=103')
    print('lcm_period=' + str(L))
    print('integer_polynomial_identity=EXACT_ZERO')
    print('polynomial_residual_length=' + str(len(residual)))
    print('negative_first_period_differences=' + str(len(drops)))
    print('smallest_first_period_difference=-1')
    print('last_drop_index=' + str(max(drops)))
    print('maximum_pre_drop_count=' + str(max(r[j] for j in drops)))
    print('witness_r2394=' + str(r[2394]) + ',r2395=' + str(r[2395]))
    print('least_universal_complete_symmetry_threshold=505')
    print('all_levels_p_ge_505_have_Sp_a_consecutive_suffix=PROVED')

if __name__=='__main__':main()
