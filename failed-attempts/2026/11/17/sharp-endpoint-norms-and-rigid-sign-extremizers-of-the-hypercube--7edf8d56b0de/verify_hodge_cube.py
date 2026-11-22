"""Exact independent checks of hypercube cut-space projection and its norm.
Run with Python 3.10+, standard library only.
"""
from fractions import Fraction as Q
from math import comb

def integral_a(d,k):
    # Integrate (1+s)^(d-1-k) (1-s)^k / 2^d via binomial convolution.
    m=d-1-k
    return sum((Q(comb(m,i)*comb(k,j)*(-1)**j, i+j+1)
                for i in range(m+1) for j in range(k+1)), Q()) / 2**d

def edge_list(d):
    return [(j,x) for j in range(d) for x in range(1<<d) if not (x>>j)&1]

def transfer_by_walsh(d, e, f):
    i,x=e; j,y=f
    out=Q()
    for S in range(1,1<<d):
        if S&(1<<i) and S&(1<<j):
            sign=(-1)**((S&(x^y)).bit_count())
            out += Q(sign, S.bit_count())
    return out * Q(2,1<<d)

def transfer_by_green(d, e, f):
    i,x=e; j,y=f
    # Source-target antisymmetric potential. Encode a_k at side i=0,
    # and -a_k at side i=1, with k the Hamming distance to x off i.
    def potential(v):
        k=((v^x)&~(1<<i)).bit_count()
        a=integral_a(d,k)
        return -a if (v>>i)&1 else a
    return potential(y)-potential(y^(1<<j))

def witness(d, e, f):
    i,x=e; j,y=f
    if j==i: return 1
    return 1 if ((y>>i)&1)==((x>>j)&1) else -1

def run():
    cases=0; comparisons=0; unique=0
    for d in range(1,8):
        edges=edge_list(d)
        e=(0,0)
        per=[Q() for _ in range(d)]
        row=[]
        for f in edges:
            a=transfer_by_walsh(d,e,f)
            b=transfer_by_green(d,e,f)
            assert a==b,(d,f,a,b)
            assert a!=0,(d,f)
            assert (1 if a>0 else -1)==witness(d,e,f),(d,f,a)
            per[f[0]]+=abs(a)
            row.append(a)
            comparisons+=1
        assert per==[Q(1)]+[Q(1,2)]*(d-1),(d,per)
        assert sum(per)==Q(d+1,2)
        assert sum(a*witness(d,e,f) for a,f in zip(row,edges))==Q(d+1,2)
        # Directly check potential's Poisson equation at every vertex
        a=[integral_a(d,k) for k in range(d)]
        for k in range(d):
            lhs=2*a[k]+(d-1-k)*(a[k]-(a[k+1] if k+1<d else Q()))+k*(a[k]-(a[k-1] if k else Q()))
            assert lhs==(1 if k==0 else 0),(d,k,lhs)
        print(f'd={d}: edges={len(edges)}, exact row-sum norm={sum(per)}, per-direction={per}')
        cases+=1
        if d<=4:
            for source in edges:
                for target in edges:
                    a=transfer_by_walsh(d,source,target)
                    b=transfer_by_green(d,source,target)
                    assert a==b
                    assert a!=0
                    assert (1 if a>0 else -1)==witness(d,source,target)
                    unique+=1
    print('GREEN_VS_WALSH_CROSSCHECKS_PASSED',comparisons+unique)
    print('RIGID_SIGN_WITNESS_CHECKS_PASSED',cases)
    print('ALL_EXACT_HYPERCUBE_HODGE_PROJECTION_CHECKS_PASSED')
if __name__=='__main__': run()
