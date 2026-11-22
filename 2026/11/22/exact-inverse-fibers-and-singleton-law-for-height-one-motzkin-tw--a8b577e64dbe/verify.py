"""Independent direct readout enumeration and arithmetic check for a height-one Motzkin source."""
from collections import Counter, defaultdict
from math import comb


def words(n, height=0, prefix=''):
    if n == 0:
        if height == 0:
            yield prefix
        return
    for letter, increment in (('F', 0), ('U', 1), ('D', -1)):
        y = height + increment
        if 0 <= y <= 1:
            yield from words(n - 1, y, prefix + letter)


def observation(w):
    one = Counter(w)
    pair = Counter(w[i:i+2] for i in range(len(w)-1))
    return tuple(one[a] for a in 'FUD') + tuple(pair[a+b] for a in 'FUD' for b in 'FUD')


def expected_fibers(n):
    counts = Counter()
    counts[(n, 0, 0, 0, 0, 0)] = 1  # all flats
    for t in range(1, n//2+1):
        f = n-2*t
        for h in range(1, t+1):
            for leading in (0, 1):
                for trailing in (0, 1):
                    g=h-1+leading+trailing
                    for q in range(t+1):
                        s=q+g
                        if (s == 0 and f != 0) or (s > 0 and f < s):
                            continue
                        c = comb(t-1,h-1)*comb(t,q)
                        c *= comb(f-1,s-1) if s else 1
                        counts[(f,t,h,q,leading,trailing)] = c
    return counts


def params(obs):
    f,t,d,ff,fu,fd,uf,uu,ud,df,du,dd=obs
    assert t==d and not uu and not dd
    if t==0:
        return (f,0,0,0,0,0)
    h=t-du
    q=uf
    lead=fu-(h-1)
    tail=df-(h-1)
    assert lead in (0,1) and tail in (0,1)
    assert fd==q and ud==t-q
    assert ff==f-(q+h-1+lead+tail)
    return (f,t,h,q,lead,tail)


def singleton_count(n):
    return sum(v==1 for v in expected_fibers(n).values())


def rational_singleton_coeffs(N):
    # Expand the independently derived rational decomposition using integer power series.
    a=[0]*(N+1)
    def geo(start,period,coefficient=1):
        for j in range(start,N+1,period): a[j]+=coefficient
    def prod_poly_geo(poly, start, period, coefficient=1):
        for shift,c in enumerate(poly):
            if c: geo(start+shift,period,c*coefficient)
    geo(0,1) # all flat paths
    geo(2,0 if False else N+1) # isolated length 2 term
    geo(3,1,3)
    if N>=4: a[4]+=3
    if N>=5: a[5]+=1
    poly=[1,2,1]
    prod_poly_geo(poly,4,2)
    # 2 z^6/((1-z)(1-z^2))
    for i in range(6,N+1):
        a[i]+=2*((i-6)//2+1)
    prod_poly_geo(poly,6,3)
    prod_poly_geo(poly,5,3)
    geo(6,1)
    prod_poly_geo(poly,7,4)
    return a


def verify(N=16):
    for n in range(N+1):
        observed=defaultdict(int)
        for w in words(n):
            observed[params(observation(w))]+=1
        assert dict(observed)==dict(expected_fibers(n)), (n, 'mismatch')
        assert sum(observed.values())==(1 if n==0 else 2**(n-1)), n
        print('direct',n,'words',sum(observed.values()),'profiles',len(observed),'singletons',sum(v==1 for v in observed.values()))
    cs=rational_singleton_coeffs(65)
    for n in range(66):
        assert singleton_count(n)==cs[n],(n,singleton_count(n),cs[n])
    print('singleton rational series passed for lengths 0..65')
    print('all checks passed')

if __name__=='__main__':verify()
