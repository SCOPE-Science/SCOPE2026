"""Independent direct finite-state attractor-basin verification."""
from collections import defaultdict,Counter
from math import comb

def update(a,b,s):
    bits=[(s>>i)&1 for i in range(a+b)]
    first=sum(bits[:a]);second=sum(bits[a:]); out=[]
    if second*2!=b:
        out.extend([int(second*2<b)]+[int(second*2>b)]*(a-1))
    else:out.extend(bits[:a])
    if first*2!=a:out.extend([int(first*2>a)]*b)
    else:out.extend(bits[a:])
    return sum(v<<i for i,v in enumerate(out))

def att(a,b,s):
    seen={};hist=[]
    while s not in seen:
        seen[s]=len(hist);hist.append(s);s=update(a,b,s)
    return tuple(sorted(hist[seen[s]:]))

def check():
    for a in range(1,9):
        for b in range(1,9):
            basins=defaultdict(int)
            for s in range(1<<(a+b)):
                basins[att(a,b,s)]+=1
            sz=Counter({})
            for cyc,n in basins.items():sz[(len(cyc),n)]+=1
            if a==1:
                assert sz==Counter({(4,2**(b+1)):1}),(a,b,sz)
            elif a==2:
                tb=comb(b,b//2) if b%2==0 else 0
                exp=Counter()
                exp[(1,2**b+2)]+=2
                if 2**b-tb-2:exp[(1,2)]+=2**b-tb-2
                if 2*tb:exp[(1,1)]+=2*tb
                assert sz==exp,(a,b,sz,exp)
            else:
                ta=comb(a,a//2) if a%2==0 else 0
                tb=comb(b,b//2) if b%2==0 else 0
                osc=(2**a-ta)*(2**b-tb)//2
                exp=Counter()
                exp[(2,osc)]+=1
                exp[(1,(2**(a+b)-osc-ta*tb)//2)]+=2
                if ta*tb:exp[(1,1)]+=ta*tb
                assert sz==exp,(a,b,sz,exp)
    print('BASINS PASS: independent bit-vector transitions, all individual attractor basin sizes on 64 parameter pairs')
if __name__=='__main__':check()
