"""Exact ninth-cyclotomic enumeration for a four-sample Fourier determinant.
No floating-point arithmetic and no third-party dependencies are used.
Run: python3 CHECK.py
"""
from itertools import combinations, permutations
from collections import Counter

# In Q[z]/(Phi_9), z^6 = -z^3 - 1 and z^9 = 1.
ZERO = (0,) * 6
ONE = (1, 0, 0, 0, 0, 0)

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def minus(a): return tuple(-x for x in a)
def sub(a,b): return add(a,minus(b))
def monomial(k):
    k %= 9
    r = [0]*6
    if k < 6: r[k] = 1
    elif k == 6: r[0],r[3] = -1,-1
    elif k == 7: r[1],r[4] = -1,-1
    else: r[2],r[5] = -1,-1
    return tuple(r)
def mul(a,b):
    r = ZERO
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    p = monomial(i+j)
                    r = tuple(r[k]+x*y*p[k] for k in range(6))
    return r
def conj(a):
    r = ZERO
    for k,x in enumerate(a):
        if x:
            p=monomial(-k)
            r=tuple(r[j]+x*p[j] for j in range(6))
    return r

def determinant_direct(T):
    # Leibniz expansion, independent of the Vandermonde-Schur factorization.
    S=(0,2,6,8)
    ans=ZERO
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        term=monomial(sum(S[i]*T[p[i]] for i in range(4)))
        ans=add(ans,minus(term) if inv%2 else term)
    return ans

def determinant_factored(T):
    w=[monomial(2*j) for j in T]
    v=ONE
    for i in range(4):
        for j in range(i+1,4):
            v=mul(v,sub(w[j],w[i]))
    e=ZERO
    for i in range(4):
        for j in range(i+1,4):e=add(e,mul(w[i],w[j]))
    return mul(v,e)

def square_to_triple(det):
    # |det(A_unscaled)|^2 = a+b*t+c*(t^2-2), t=z+z^{-1}.
    x=mul(det,conj(det))
    a,b,c=x[0],-x[5],-x[4]
    t=add(monomial(1),monomial(-1))
    t2minus2=add(monomial(2),monomial(-2))
    calc=tuple(a*ONE[k]+b*t[k]+c*t2minus2[k] for k in range(6))
    assert x == calc
    return (a,b,c)

def canonical(T):
    return min(tuple(sorted((j+k)%9 for j in T)) for k in range(9))

EXPECTED={
    (0,0,0):18,
    (54,-27,0):27,
    (54,0,-27):27,
    (81,0,0):27,
    (54,27,27):27,
}

def main():
    counts=Counter(); reps={}
    # All 126 four-subsets: no untested representatives.
    for T in combinations(range(9),4):
        direct=determinant_direct(T)
        schur=determinant_factored(T)
        assert direct==schur, (T,direct,schur)
        v=square_to_triple(direct)
        counts[v]+=1
        reps.setdefault(canonical(T),v)
    assert counts==EXPECTED,(counts,EXPECTED)
    assert len(reps)==14
    orbit_counts=Counter(reps.values())
    assert orbit_counts == Counter({(0,0,0):2,(54,-27,0):3,(54,0,-27):3,(81,0,0):3,(54,27,27):3})
    print('EXACT_CANTOR_9_FOURIER_DETERMINANT_CENSUS_PASSED')
    print('total_sets',sum(counts.values()),'translation_orbits',len(reps))
    for key in sorted(counts):
        print('unscaled_squared_triple',key,'frequency_sets',counts[key])
    for T,v in sorted(reps.items()):
        print('orbit_rep',','.join(map(str,T)),'triple',','.join(map(str,v)))

if __name__=='__main__':main()
