#!/usr/bin/env python3
"""Independent exact point-count check of four p-ranks over F5 in extensions F5^n, 1<=n<=4."""
from itertools import product
P=5
MOD={1:(0,1),2:(2,0,1),3:(1,1,0,1),4:(2,0,0,0,1)}
# MOD[1] unused except to denote F5 directly.
def extension(n):
    Q=5**n
    digits=[tuple((x//5**j)%5 for j in range(n)) for x in range(Q)]
    def add(x,y):
        return sum(((digits[x][i]+digits[y][i])%5)*5**i for i in range(n))
    def mul(x,y):
        if n==1:return (x*y)%5
        xs=digits[x];ys=digits[y]
        prod=[0]*(2*n-1)
        for i in range(n):
            for j in range(n):prod[i+j]=(prod[i+j]+xs[i]*ys[j])%5
        mod=MOD[n]
        for k in range(2*n-2,n-1,-1):
            t=prod[k]
            if t:
                for j in range(n):prod[k-n+j]=(prod[k-n+j]-t*mod[j])%5
        return sum(prod[i]*5**i for i in range(n))
    def powr(x,exp):
        v=1
        while exp:
            if exp&1:v=mul(v,x)
            x=mul(x,x);exp//=2
        return v
    sq={mul(y,y):y for y in range(Q)}
    assert len(sq)==(Q+1)//2
    return Q,add,mul,powr,sq

def count_curve(n,a,b):
    Q,add,mul,power,squares=extension(n)
    count=2 # two points at infinity: degree ten, monic, even hyperelliptic model.
    for x in range(Q):
        f=add(add(power(x,10),power(x,7)),add(mul(a,power(x,4)),mul(b,x)))
        if f==0:count+=1
        elif f in squares:count+=2
    return count

def inferred_p_rank(a,b):
    c=[1];counts=[]
    for n in range(1,5):
        N=count_curve(n,a,b);counts.append(N)
        sn=(5**n+1-N)%5
        # Newton's identities in F5: n*c[n] = -sum_{j=1}^n c[n-j]*S[j]
        # Compute all using existing traces.
        if n==1: traces=[0]
        traces.append(sn)
        cn=(-sum(c[n-j]*traces[j] for j in range(1,n+1))*pow(n,-1,5))%5
        c.append(cn)
    return max((j for j in range(1,5) if c[j]),default=0),counts,c

witnesses={0:(4,2),1:(0,1),2:(1,2),3:(0,2)}
for rank,(a,b) in witnesses.items():
    found,counts,coeff=inferred_p_rank(a,b)
    assert found==rank,(rank,found,a,b,counts,coeff)
    print('RANK',rank,'parameters',(a,b),'N_1..4',counts,'L(T) mod5 head',coeff)
print('GENUS4_P5_POINTCOUNTS_PASS')
