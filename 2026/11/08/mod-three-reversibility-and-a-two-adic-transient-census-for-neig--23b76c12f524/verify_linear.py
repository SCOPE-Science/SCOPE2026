"""Independent GF(2) finite-matrix verification of parity dynamics on ladder graphs.
Runs without third-party dependencies: python verify_linear.py
"""

def rows_for_ladder(n):
    rows=[]
    for side in range(2):
        for j in range(n):
            mask=1<<((1-side)*n+j)
            if j>0:mask ^= 1<<(side*n+j-1)
            if j<n-1:mask ^= 1<<(side*n+j+1)
            rows.append(mask)
    return rows

def apply(rows,x):
    out=0
    for k,r in enumerate(rows):
        if ((r&x).bit_count()&1):out|=1<<k
    return out

def rank(vectors):
    piv={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i not in piv:
                piv[i]=v
                break
            v^=piv[i]
    return len(piv)

def rank_kernel_power(rows,t):
    size=len(rows)
    images=[1<<k for k in range(size)]
    for _ in range(t): images=[apply(rows,z) for z in images]
    return size-rank(images)

def predicted(n,t):
    if (n+1)%3: return 0
    m=2**(((n+1)&-(n+1)).bit_length()) # = 2^(v2(n+1)+1)
    return 2*min(m,t)

def main():
    cases=0
    maxdim=0
    for n in range(2,85):
        rows=rows_for_ladder(n)
        m=2**(((n+1)&-(n+1)).bit_length()) if (n+1)%3==0 else 0
        ts=sorted(set([0,1,2,3,4,m-1,m,m+1, min(2*n,50)]))
        for t in ts:
            if t<0:continue
            got=rank_kernel_power(rows,t)
            expect=predicted(n,t)
            assert got==expect,(n,t,got,expect)
            cases+=1
        maxdim=max(maxdim,2*n)
    print('PASS exact kernel nullities', cases,'cases; n=2..84, dimension <=',maxdim)
    for n in [2,3,4,5,8,11,17,23,47,71]:
        m=2**(((n+1)&-(n+1)).bit_length()) if (n+1)%3==0 else 0
        print('n=',n,'invertible=',m==0,'max entrance=',m,'periodic dimension=',2*n-2*m)

if __name__=='__main__':main()
