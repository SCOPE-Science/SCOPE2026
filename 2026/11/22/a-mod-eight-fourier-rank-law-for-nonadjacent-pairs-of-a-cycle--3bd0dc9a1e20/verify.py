"""Integer Walsh verification for nonadjacent pairs on labelled cycles."""
from math import comb

def fmask(n):
    a=[0]*(1<<n)
    for i in range(n):
        for j in range(i+1,n):
            if j != i+1 and (i,j)!=(0,n-1):
                a[(1<<i)|(1<<j)]=1
    return a

def walsh_inplace(a):
    b=a[:]
    step=1
    while step<len(b):
        for st in range(0,len(b),2*step):
            for j in range(step):
                x,y=b[st+j],b[st+step+j]
                b[st+j],b[st+step+j]=x+y,x-y
        step*=2
    return b

def predicted(n,mask):
    neg=mask.bit_count()
    changes=sum(((mask>>j)&1)!=((mask>>((j+1)%n))&1) for j in range(n))
    return ((n-2*neg)**2-3*n+4*changes)//2

def formula_nullity(n):
    z=0
    for k in range(1,n):
        numerator=3*n-(n-2*k)**2
        if numerator>0 and numerator%8==0:
            j=numerator//8
            if 1<=j<=min(k,n-k):
                val=n*comb(k-1,j-1)*comb(n-k-1,j-1)
                assert val%j==0
                z+=val//j
    return z

def check():
    tests=0
    table=[]
    for n in range(4,16):
        vals=walsh_inplace(fmask(n))
        for x,w in enumerate(vals):
            assert w==predicted(n,x),(n,x,w,predicted(n,x))
            tests+=1
        observed=vals.count(0)
        assert observed==formula_nullity(n)
        assert (observed>0)==(n%4==0 or n%8==3)
        table.append((n,2**n-observed,observed))
    for n in range(4,400):
        z=formula_nullity(n)
        assert (z>0)==(n%4==0 or n%8==3), (n,z)
    assert table[:5]==[(4,8,8),(5,32,0),(6,64,0),(7,128,0),(8,216,40)]
    print('verified',tests,'full integer Walsh coefficients, n=4..15; rank/zeros 4..399')
    print(table)
if __name__=='__main__':check()
