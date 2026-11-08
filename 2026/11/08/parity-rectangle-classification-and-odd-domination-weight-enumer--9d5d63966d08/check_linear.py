"""Independent GF(2) affine-system solver checking all weights through 7 x 7."""
from collections import Counter
from math import comb

def calculate(m,n):
    size=m*n
    rows=[]
    for i in range(m):
        for j in range(n):
            coeff=0
            for ii in range(m):
                for jj in range(n):
                    if ii==i or jj==j:
                        coeff ^= 1<<(ii*n+jj)
            rows.append(coeff|(1<<size))
    pivots=[]
    rr=0
    for col in range(size):
        k=next((k for k in range(rr,size) if rows[k] & (1<<col)),None)
        if k is None:continue
        rows[rr],rows[k]=rows[k],rows[rr]
        for t in range(size):
            if t!=rr and (rows[t] & (1<<col)):
                rows[t] ^= rows[rr]
        pivots.append(col)
        rr+=1
    assert all(not (rows[k]&((1<<size)-1)) and not(rows[k]&(1<<size)) for k in range(rr,size))
    free=[j for j in range(size) if j not in pivots]
    result=Counter()
    for sel in range(1<<len(free)):
        sol=sum((1<<c) for k,c in enumerate(free) if (sel>>k)&1)
        for p,col in reversed(list(enumerate(pivots))):
            rhs=(rows[p]>>size)&1
            rhs^=(rows[p]&sol).bit_count()%2
            if rhs:sol |=1<<col
        assert all((sol & row&((1<<size)-1)).bit_count()%2 == (row>>size)&1 for row in rows)
        result[sol.bit_count()]+=1
    return result,len(free)

def expected(m,n):
    h=Counter()
    for a in range(m+1):
        for b in range(n+1):
            if m%2==0 and n%2==0:
                if a==m and b==n:h[m*n]=1
            elif m%2==0 and n%2==1:
                if a%2==1 and b==0:h[a*n]+=comb(m,a)
            elif m%2==1 and n%2==0:
                if a==0 and b%2==1:h[b*m]+=comb(n,b)
            elif a%2==1 and b%2==1:
                h[a*b+(m-a)*(n-b)]+=comb(m,a)*comb(n,b)
    return h

def main():
    for m in range(2,8):
        for n in range(2,8):
            got, nullity=calculate(m,n)
            exp=expected(m,n)
            assert got==exp,(m,n,got,exp)
            target=(0 if m%2==0 and n%2==0 else (m-1 if m%2==0 else n-1 if n%2==0 else m+n-2))
            assert nullity==target,(m,n,nullity,target)
            print(f'{m}x{n}: rank={m*n-nullity}, nullity={nullity}, size={sum(got.values())}, min={min(got)}, polynomial={sorted(got.items())}')
    print('AFFINE_GAUSS: PASS')
if __name__=='__main__':main()
