"""Standalone exact-coefficient checks for coloured directed star forests.
No external dependencies. Python 3.10+.
"""
from math import comb, pi, sqrt

def types_by_size(q,n):
    return [0]+[q*comb(m+q-2,q-1) for m in range(1,n+1)]

def weighted_partition_counts(q,n):
    a=types_by_size(q,n)
    b=[0]*(n+1)
    for d in range(1,n+1):
        for k in range(d,n+1,d): b[k]+=d*a[d]
    p=[0]*(n+1);p[0]=1
    for k in range(1,n+1):
        x=sum(b[j]*p[k-j] for j in range(1,k+1))
        assert x%k==0,(q,k,x)
        p[k]=x//k
    return p

def enumerate_stars(q,n):
    """Explicit stars: (root_colour, leaf_colour_multiplicities)."""
    out=[]
    def parts(total,k):
        if k==1:
            yield (total,)
        else:
            for v in range(total+1):
                for t in parts(total-v,k-1):yield (v,)+t
    for size in range(1,n+1):
        for c in range(q):
            for vector in parts(size-1,q):
                out.append((size,c,vector))
    return out

def explicit_counts(q,n):
    stars=enumerate_stars(q,n)
    v=[0]*(n+1);v[0]=1
    for size,colour,vector in stars:
        for s in range(size,n+1):v[s]+=v[s-size]
    return v

def explicit_event_counts(q,n,chosen_size,threshold):
    """Check insertion/deletion bijection on finite multisets."""
    stars=enumerate_stars(q,n)
    target=next(t for t in stars if t[0]==chosen_size)
    counts=0;total=0
    def rec(i,rem,chosen):
        nonlocal counts,total
        if rem==0:
            total+=1
            counts+=(chosen>=threshold)
            return
        if i==len(stars):return
        size=stars[i][0]
        for x in range(rem//size+1):
            rec(i+1,rem-x*size,chosen+x*(stars[i]==target))
    rec(0,n,0)
    return counts,total

def run():
    for q in range(1,5):
        n=8
        a=types_by_size(q,n)
        assert a[1]==q
        assert a[2]==q*q
        p=weighted_partition_counts(q,n)
        e=explicit_counts(q,n)
        assert p==e,(q,p,e)
        for size in range(1,4):
            for threshold in (1,2):
                if size*threshold>6:continue
                got,total=explicit_event_counts(q,6,size,threshold)
                assert total==p[6]
                assert got==p[6-size*threshold],(q,size,threshold,got,p[6-size*threshold])
        print('q=',q,'coefficients=',p[:8])
    for q in (1,2,3):
        N=400
        p=weighted_partition_counts(q,N)
        # independently approximate the constant from an integral; q=1 exact value
        zeta=(pi*pi/6 if q==1 else sum(1.0/k**(q+1) for k in range(1,100001)))
        kappa=(q*q*zeta)**(1/(q+1))
        estimate=(1-p[N-1]/p[N])*(N**(1/(q+1)))
        assert 0.4*kappa<estimate<1.8*kappa,(q,kappa,estimate)
        print('q=',q,'limit constant=',kappa,'finite-n=',estimate)
    print('ALL_CHECKS_OK')

if __name__=='__main__':run()
