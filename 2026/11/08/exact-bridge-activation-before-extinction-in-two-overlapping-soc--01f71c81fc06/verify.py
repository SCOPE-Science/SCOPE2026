from fractions import Fraction as Q
from math import comb, factorial
from itertools import product

def formula(a,c,k,rateA,rateB,delta):
    if c<k: return Q(0)
    assert 1<=k<=c<=a and a>=2
    r=c-k+1; s=rateA+rateB
    ps=Q(0); pe=Q(0)
    for j in range(r,a-k+2):
        if j-1<r-1 or a-j<c-r: continue
        w=Q(comb(j-1,r-1)*comb(a-j,c-r),comb(a,c))
        lapB=Q(1)
        for i in range(1,j+1):
            v=(a-i+1)*delta
            lapB*=v/(v+s)
        lapRest=Q(1)
        for i in range(j+1,a+1):
            v=(a-i+1)*delta
            lapRest*=v/(v+rateA)
        ps+=w*(rateB/s)*(1-lapB)
        pe+=w*lapB*lapRest
    assert ps>0 and pe>0 and ps+pe<=1
    return ps/(ps+pe)

def markov(a,c,k,rateA,rateB,delta):
    # states count live bridge j and live outside h; absorbing success and failure
    # first eB event success if j>=k; eA reset to (c,a-c) when total>=1
    states=[(j,h) for j in range(c+1) for h in range(a-c+1) if j+h>=1]
    n=len(states)
    # Gauss Jordan with exact fractions
    mat=[]
    for j,h in states:
        total= j*delta+h*delta+rateA+(rateB if j>=k else 0)
        row=[Q(0) for _ in range(n+1)]
        row[states.index((j,h))]=total
        if j>0 and (j-1,h) in states: row[states.index((j-1,h))]-=j*delta
        if h>0 and (j,h-1) in states: row[states.index((j,h-1))]-=h*delta
        row[states.index((c,a-c))]-=rateA
        row[-1]=rateB if j>=k else Q(0)
        mat.append(row)
    for z in range(n):
        i=next(i for i in range(z,n) if mat[i][z])
        mat[z],mat[i]=mat[i],mat[z]
        x=mat[z][z]
        mat[z]=[v/x for v in mat[z]]
        for i in range(n):
            if i==z:continue
            x=mat[i][z]
            if x: mat[i]=[p-x*q for p,q in zip(mat[i],mat[z])]
    return mat[states.index((c,a-c))][-1]

def full_microstate(a,c,k,rateA,rateB,delta):
    # Independent check on all 2**a opinion microstates (not occupancy counts).
    states=list(range(1,1<<a))
    loc={mask:i for i,mask in enumerate(states)}
    n=len(states)
    mat=[]
    target=(1<<a)-1
    for mask in states:
        active=mask.bit_count()
        in_bridge=(mask&((1<<c)-1)).bit_count()
        row=[Q(0) for _ in range(n+1)]
        row[loc[mask]]=delta*active+rateA+(rateB if in_bridge>=k else Q(0))
        for bit in range(a):
            if mask&(1<<bit):
                new_mask=mask&~(1<<bit)
                if new_mask:
                    row[loc[new_mask]]-=delta
        row[loc[target]]-=rateA
        row[-1]=rateB if in_bridge>=k else Q(0)
        mat.append(row)
    for z in range(n):
        piv=next(i for i in range(z,n) if mat[i][z])
        mat[z],mat[piv]=mat[piv],mat[z]
        mul=mat[z][z]
        mat[z]=[v/mul for v in mat[z]]
        for i in range(n):
            if i!=z and mat[i][z]:
                mul=mat[i][z]
                mat[i]=[u-mul*v for u,v in zip(mat[i],mat[z])]
    return mat[loc[target]][-1]

if __name__=='__main__':
    count=0
    for a in range(2,7):
        for c in range(1,a+1):
            for k in range(1,c+1):
                for ra,rb,d in [(Q(1),Q(2),Q(1)),(Q(3,4),Q(5,3),Q(2)),(Q(4),Q(1,7),Q(5,4))]:
                    f=formula(a,c,k,ra,rb,d)
                    g=markov(a,c,k,ra,rb,d)
                    assert f==g,(a,c,k,ra,rb,d,f,g)
                    count+=1
    print('compressed exact checks',count)
    raw=0
    for a in range(3,6):
        for c in range(1,a):
            for k in range(1,c+2):
                for ra,rb,d in [(Q(2),Q(1),Q(1)),(Q(4,3),Q(5,2),Q(2))]:
                    f=formula(a,c,k,ra,rb,d)
                    g=full_microstate(a,c,k,ra,rb,d)
                    assert f==g,(a,c,k,ra,rb,d,f,g)
                    raw+=1
    print('full-microstate exact checks',raw)
    for a,c,k in [(2,1,1),(3,2,2),(5,3,2),(6,6,1)]:
        for ra in [Q(10**3),Q(10**5)]:
            pr=formula(a,c,k,ra,Q(2),Q(1))
            scal=(1-pr)*ra**(a-1)
            print(a,c,k,ra, 'scaled failure',float(scal),'target',factorial(a)/2)
