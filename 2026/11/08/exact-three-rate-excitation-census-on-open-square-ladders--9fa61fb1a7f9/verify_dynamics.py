#!/usr/bin/env python3
"""Independent direct synchronous dynamics, no cycle-integral theorem invoked."""
from itertools import product
from fractions import Fraction

def neighbors(n):
    a=[]
    for v in range(2*n):
        i=v%n;row=v//n
        a.append(tuple([n+i if row==0 else i]+([v-1] if i else [])+([v+1] if i<n-1 else [])))
    return a

def update(x,adj,model):
    y=[]
    for i,nb in enumerate(adj):
        a=x[i]
        if model=='CCA':y.append((a+1)%3 if (a+1)%3 in (x[j] for j in nb) else a)
        else:y.append((a+1)%3 if a in (1,2) or 1 in (x[j] for j in nb) else 0)
    return tuple(y)

def rate(x,adj,model):
    visited={};states=[]
    while x not in visited:
        visited[x]=len(states);states.append(x)
        x=update(x,adj,model)
        assert len(states)<=2000,'Unexpectedly long trajectory; increase bound after inspection'
    cyc=states[visited[x]:]
    counts=[0]*len(x)
    for a in cyc:
        b=update(a,adj,model)
        for j in range(len(x)):
            if model=='CCA':counts[j]+=(a[j]!=b[j])
            else:counts[j]+=(a[j]==0 and b[j]==1)
    assert len(set(counts))==1,(model,cyc,counts)
    return Fraction(counts[0],len(cyc))

def main():
    tested=0
    for n in range(2,6):
        adj=neighbors(n);obs={x:0 for x in (Fraction(0),Fraction(3,4),Fraction(1))}
        for x in product(range(3),repeat=2*n):
            c=rate(x,adj,'CCA');g=rate(x,adj,'GHM')
            assert c==3*g,(n,x,c,g)
            assert c in obs,(n,x,c)
            obs[c]+=1;tested+=1
        print(f'n={n} zero={obs[Fraction(0)]} intermediate={obs[Fraction(3,4)]} maximal={obs[Fraction(1)]}')
    print(f'PASS: direct trajectories of both automata on all {tested} labelled states for n=2..5.')
if __name__=='__main__':main()
