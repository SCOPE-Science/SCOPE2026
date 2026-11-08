from itertools import product
from math import comb

def field(q):
    assert q in (2,3)
    a0,a1=(1,1) if q==2 else (1,0)
    elements=[(a,b) for a in range(q) for b in range(q)]
    d={x:i for i,x in enumerate(elements)}
    Q=q*q
    add=[[d[((a[0]+b[0])%q,(a[1]+b[1])%q)] for b in elements] for a in elements]
    mul=[]
    for a in elements:
        row=[]
        for b in elements:
            c0=(a[0]*b[0]-a0*a[1]*b[1])%q
            c1=(a[0]*b[1]+a[1]*b[0]-a1*a[1]*b[1])%q
            row.append(d[(c0,c1)])
        mul.append(row)
    def pow_e(a,k):
        out=d[(1,0)]
        while k:
            if k&1: out=mul[out][a]
            a=mul[a][a];k>>=1
        return out
    sigma=[pow_e(i,q) for i in range(Q)]
    fix=[i for i in range(Q) if sigma[i]==i]
    z=d[(0,0)];one=d[(1,0)]
    return elements,add,mul,sigma,fix,z,one

def check(q,n):
    elems,add,mul,sigma,fix,z,one=field(q)
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    orbit=[]; seen=set()
    for ij in pairs:
        if ij in seen: continue
        i,j=ij;flip=(n-1-j,n-1-i)
        seen|={ij,flip}
        orbit.append((ij,flip,fix if ij==flip else range(q*q)))
    tally={}
    for half_diag in product((0,1),repeat=(n+1)//2):
        diag=[half_diag[min(i,n-1-i)] for i in range(n)]
        rank=sum(diag)
        cnt=0
        for vals in product(*(o[2] for o in orbit)):
            A=[[z]*n for _ in range(n)]
            for i in range(n): A[i][i]=one if diag[i] else z
            for (ij,flip,options),v in zip(orbit,vals):
                A[ij[0]][ij[1]]=v
                A[flip[0]][flip[1]]=sigma[v]
            good=True
            for i in range(n):
                for j in range(i,n):
                    dot=z
                    for k in range(i,j+1): dot=add[dot][mul[A[i][k]][A[k][j]]]
                    if dot!=A[i][j]:good=False;break
                if not good:break
            cnt+=good
        tally[rank]=tally.get(rank,0)+cnt
    m=n//2
    predicted={}
    if n%2==0:
        for k in range(m+1):
            r=2*k
            predicted[r]=comb(m,k)*q**(r*(n-r))
    else:
        for r in range(n+1):
            predicted[r]=comb(m,r//2)*q**(r*(n-r))
    assert tally==predicted,(q,n,tally,predicted)
    print('OK',q,n,tally)
if __name__=='__main__':
    for q,n in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4)]: check(q,n)
    print('VERIFY_OK')
