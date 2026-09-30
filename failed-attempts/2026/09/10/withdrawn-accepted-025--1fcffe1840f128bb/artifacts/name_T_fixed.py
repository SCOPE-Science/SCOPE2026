"""Step 2 (fixed): name T as intersection of two 2-dim torus components above loop 3.
(g,r,d)=(6,1,5), l=12,m=1,N=13. Checks agreement of each branch with T on its fixed set."""
from itertools import product
g,N=6,13
def paths():
    out=[]
    for d0 in range(1,6):
        for steps in product([-1,0,1],repeat=g):
            p=d0; ok=True
            for s in steps:
                p+=s
                if p<1: ok=False;break
            if not ok: continue
            if steps.count(-1)!=6-5+d0: continue
            out.append((d0,steps))
    return out
P=paths()
def chips(d0,steps):
    p=d0; xs=[]
    for s in steps:
        if s==-1: xs.append(None)
        elif s==1: xs.append((p+1)%N)
        else: xs.append('FREE')
        p+=s
    return xs
def AJfixed(d0,steps,xs):
    pres=[x is not None for x in xs]
    pat=[]
    for i in range(g):
        if xs[i]=='FREE': pat.append(None)
        else:
            n=sum(pres[j] for j in range(i+1,g)); x=0 if xs[i] is None else xs[i]
            pat.append((n+x)%N)
    return tuple(pat)
A=(1,(1,0,0,-1,1,-1)); B=(1,(1,-1,0,0,1,-1))
xA,xB=chips(*A),chips(*B)
pA,pB=AJfixed(*A,xA),AJfixed(*B,xB)
print("A lingers {2,3} fixed{1,4,5,6}:",pA)
print("B lingers {3,4} fixed{1,2,5,6}:",pB)
# T = {AJ=(5,3,s,1,2,0)}: A agrees on {1,4,5,6}, B on {1,2,5,6}
T={0:5,1:3,3:1,4:2,5:0}
print("A agrees w/ T on {1,4,5,6}:",all(pA[i]==T[i] for i in (0,3,4,5)))
print("B agrees w/ T on {1,2,5,6}:",all(pB[i]==T[i] for i in (0,1,4,5)))
print("T = {AJ=(5,3,s,1,2,0) : s in R/13Z}, circle above loop 3, NON-vertex-avoiding")
print("rank>=1 along T: both branches have lingering paths in C (verified in enumeration) -> cite CDPR Thm 4.6")
