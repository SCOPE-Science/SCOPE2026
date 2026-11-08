"""Exact finite reproducibility checks for fourth-centered-moment Lipschitz extremizers.

Run: python verify_multipartite_m4.py. Uses Python integers only.
"""
from itertools import product


def integer_partitions(n,lo=1):
    if n==0:
        yield ()
        return
    for k in range(lo,n+1):
        for tail in integer_partitions(n-k,k):
            yield (k,)+tail


def numer(values):
    n=len(values)
    total=sum(values)
    return sum((n*x-total)**4 for x in values)


def formula(n,m):
    b=max(n*k*(n-k)*(n*n-3*k*(n-k)) for k in range(n+1))
    def tri(t):
        return m*n**4+(6*m-4*n)*n*n*t*t-3*n*t**4
    tvals=list(range(m%2,m+1,2))
    best_tri=max(tri(t) for t in tvals)
    return max(b,best_tri),b,best_tri,[t for t in tvals if tri(t)==best_tri]


def check_one(parts):
    n=sum(parts)
    groups=sum(([i]*s for i,s in enumerate(parts)),[])
    m=max(parts)
    target,b,tr,tts=formula(n,m)
    for tup in product(range(-2,3),repeat=n-1):
        v=(0,)+tup
        if any(abs(v[i]-v[j])>1 for i in range(n) for j in range(i+1,n) if groups[i]!=groups[j]):
            continue
        q=numer(v)
        if q>target:
            raise AssertionError(('value exceeds formula',parts,v,q,target))
        if q==target:
            a=min(v); z=max(v)
            if z-a==1:
                assert q==b
            elif z-a==2:
                assert q==tr
                lows={groups[i] for i,x in enumerate(v) if x==a}
                highs={groups[i] for i,x in enumerate(v) if x==z}
                assert len(lows)==len(highs)==1 and lows==highs
                group=next(iter(lows))
                assert parts[group]==m
                assert all(x in (a,z) for i,x in enumerate(v) if groups[i]==group)
                assert all(x==a+1 for i,x in enumerate(v) if groups[i]!=group)
                assert abs(sum(1 if x==z else -1 for i,x in enumerate(v) if groups[i]==group)) in tts
            else:
                raise AssertionError(('unexpected maximizing span',parts,v))
    # Binary and ternary values attaining formula are feasible on this graph.
    k=max(range(n+1),key=lambda k:n*k*(n-k)*(n*n-3*k*(n-k)))
    assert numer([1]*k+[0]*(n-k))==b
    mi=parts.index(m)
    best_t=tts[0]; a=(m+best_t)//2
    z=[]
    for i,p in enumerate(parts):
        if i==mi:z.extend([1]*a+[-1]*(m-a))
        else:z.extend([0]*p)
    assert numer(z)==tr
    return 1


def main():
    count=0
    for n in range(2,9):
        for p in integer_partitions(n):
            if len(p)<2:continue
            count+=check_one(p)
        print('EXHAUSTIVE_MULTIPARTITE_ALL_POTENTIALS_OK',n)
    assert count>0
    print('EXHAUSTIVE_PARTITIONS_OK',count)
    for n in range(2,301):
        tri=[]
        for m in range(1,n):
            _,_,v,_=formula(n,m)
            tri.append(v)
        assert all(x<y for x,y in zip(tri,tri[1:])),n
    print('STRICT_PART_SIZE_MONOTONICITY_SAMPLED_OK',299)
    for n in range(3,301):
        for m in range(1,n):
            _,_,_,tset=formula(n,m)
            s=(m%2)
            # Exact first skew transition (strict, equality ties, or stable parity-minimal).
            threshold=(4*n*n+3*(s*s+(s+2)**2))
            lhs=6*m*n
            if m>=s+2:
                assert (s not in tset)==(lhs>threshold)
    print('EXACT_SKEW_TRANSITION_SAMPLED_OK')
    print('ALL_MULTIPARTITE_FOURTH_MOMENT_CHECKS_OK')

if __name__=='__main__':main()
