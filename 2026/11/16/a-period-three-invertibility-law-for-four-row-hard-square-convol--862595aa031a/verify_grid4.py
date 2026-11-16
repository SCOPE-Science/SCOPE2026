"""Exact reproducibility checks for four-row grid independence-convolution theorem.

Python 3 standard library, no external dependencies.
"""
from itertools import product

STATES=(0,1,2,4,5,8,9,10)
N=len(STATES)
ZERO=(1,0,0,0,0,0,0,0)
ONES=(1,)*N

def mat(sign):
    return tuple(tuple(((-1)**((a&sign).bit_count())) if not(a&b) else 0 for b in STATES) for a in STATES)

def mv(A,v):
    return tuple(sum(x*y for x,y in zip(row,v)) for row in A)

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)) for i in range(N))

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))

def pow_action(A,v,k):
    for _ in range(k):v=mv(A,v)
    return v

def row_act(u,A):
    return tuple(sum(u[i]*A[i][j] for i in range(N)) for j in range(N))

def signing_sum(signs):
    v=ZERO
    for t in signs:v=mv(mat(t),v)
    return sum(v)

def all_signs(period,n):
    return (period*(n//len(period)+1))[:n]

def parity_test():
    A=mat(0);v=ZERO
    a=[]
    for i in range(11):
        a.append(sum(v)%2)
        v=mv(A,v)
    assert a[:11]==[1,0,1,1,0,1,1,0,1,1,0]
    # The scalar difference vanishes in eight successive indices;
    # Cayley-Hamilton for the dimension-eight matrix extends it to every index.
    assert all(a[i]==a[i+3] for i in range(8))

def zeros_test():
    P=mm(mm(mat(14),mat(0)),mat(11))
    r=row_act(ONES,mat(11))
    K=[pow_action(P,ZERO,i) for i in range(5)]
    assert all(dot(r,K[i])==0 for i in range(4))
    assert K[4]==tuple(K[0][j]+2*K[1][j]+2*K[2][j] for j in range(N))
    for n in range(1,61,3):
        assert signing_sum(all_signs((11,0,14),n))==0

def unit_test():
    Q=mm(mat(3),mat(15))
    assert pow_action(Q,ZERO,6)==ZERO
    values=[signing_sum(all_signs((15,3),n)) for n in range(1,13)]
    assert values==[0,1,-1,2,-1,1,0,1,1,0,1,1],values
    for n in range(1,97):
        w=signing_sum(all_signs((15,3),n))
        assert w==values[(n-1)%12]
        if n%3!=1:assert abs(w)==1

def direct_all(n):
    # Independent construction using four-row grid edge adjacency,
    # not the column-state transfer. Transform the indicator in-place.
    d=4*n
    assert n<=4
    sz=1<<d
    edges=[]
    for c in range(n):
        for r in range(4):
            v=4*c+r
            if r<3:edges.append((v,v+1))
            if c<n-1:edges.append((v,v+4))
    values=[1]*sz
    for bits in range(sz):
        for a,b in edges:
            if ((bits>>a)&1) and ((bits>>b)&1):
                values[bits]=0
                break
    # Crucial: transform need not rely on the transfer recurrence.
    count=sum(values)
    assert count%2==(0 if n%3==1 else 1)
    h=1
    while h<sz:
        for st in range(0,sz,h*2):
            for j in range(st,st+h):
                x,y=values[j],values[j+h]
                values[j]=x+y
                values[j+h]=x-y
        h*=2
    assert values[0]==count
    assert all(v%2==count%2 for v in values)
    nzeros=values.count(0)
    if n%3==1:
        assert nzeros>0
    else:
        assert nzeros==0 and min(map(abs,values))==1
    for period in [(11,0,14),(15,3)]:
        frequency=sum((s<<(4*j)) for j,s in enumerate(all_signs(period,n)))
        assert values[frequency]==signing_sum(all_signs(period,n))
    return (n,count,nzeros,min((abs(v) for v in values if v),default=None))

def main():
    parity_test();zeros_test();unit_test()
    stats=[direct_all(n) for n in range(1,5)]
    assert stats[:2]==[(1,8,5,2),(2,41,0,1)],stats
    print('GRID4_WALSH_PERIOD3_PASS',stats,'all_order_transfer_identities=3')

if __name__=='__main__': main()
