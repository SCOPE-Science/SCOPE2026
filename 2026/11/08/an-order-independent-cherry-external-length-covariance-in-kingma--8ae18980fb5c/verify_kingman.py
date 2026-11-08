from fractions import Fraction as Q
from math import comb


def exact_dp(n):
    states={(n,0):(Q(1),Q(0))} # (singletons,cherries) : probability, expected rewarded length mass
    for k in range(n,1,-1):
        nxt={}
        for (s,c),(p,e) in states.items():
            e=e+p*Q(s,comb(k,2))
            choices=[(s-2,c+1,comb(s,2)),(s-1,c,s*(k-s)),(s,c,comb(k-s,2))]
            for ss,cc,num in choices:
                if not num: continue
                pp=Q(num,comb(k,2))
                a,b=nxt.get((ss,cc),(Q(0),Q(0)))
                nxt[(ss,cc)]=(a+p*pp,b+e*pp)
        states=nxt
    pc=sum((p for p,e in states.values()),Q(0))
    EC=sum((c*p for (s,c),(p,e) in states.items()),Q(0))
    EL=sum((e for p,e in states.values()),Q(0))
    ECL=sum((c*e for (s,c),(p,e) in states.items()),Q(0))
    return pc,EC,EL,ECL-EC*EL


def hist_exhaust(n):
    from itertools import combinations
    h=0; total_C=0; total_L=Q(0); total_CL=Q(0)
    observed={k:[0,0] for k in range(2,n+1)}
    def go(blocks,c,l,profile):
        nonlocal h,total_C,total_L,total_CL
        k=len(blocks)
        if k==1:
            h+=1;total_C+=c;total_L+=l;total_CL+=c*l
            for kk,s in profile.items():
                observed[kk][0]+=s
                observed[kk][1]+=s*c
            return
        s=sum(len(b)==1 for b in blocks)
        profile[k]=s
        l=l+Q(s,comb(k,2))
        for a,b in combinations(range(k),2):
            b0,b1=blocks[a],blocks[b]
            nb=[blocks[j] for j in range(k) if j!=a and j!=b]
            nb.append(b0|b1)
            go(nb,c+int(len(b0)==len(b1)==1),l,profile)
    go([frozenset([i]) for i in range(n)],0,Q(0),{})
    C=Q(total_C,h);L=total_L/h;cov=total_CL/h-C*L
    checks=[]
    for k,(es,ecs) in observed.items():
        got=Q(ecs,h)-C*Q(es,h)
        want=-Q(k*(k-1)*(n-k)*(n-k-1),3*(n-3)*(n-2)*(n-1)) if n>=4 else Q(0)
        checks.append((k,got,want))
        assert got==want,(n,k,got,want)
    return h,C,L,cov,checks

if __name__=='__main__':
    for n in range(2,31):
        p,c,l,cov=exact_dp(n)
        assert p==1,(n,p)
        assert c==Q(n,3) if n>=3 else c==1,(n,c)
        assert l==2,(n,l)
        assert cov==(-Q(2,9) if n>=4 else 0),(n,cov)
        print('DP',n,'meanC',c,'meanE',l,'cov',cov)
    for n in range(4,9):
        h,c,l,cov,profile=hist_exhaust(n)
        assert c==Q(n,3) and l==2 and cov==-Q(2,9)
        print('HISTORY',n,'histories',h,'profile',[(k,str(x)) for k,x,_ in profile])
    print('All independent checks passed.')
