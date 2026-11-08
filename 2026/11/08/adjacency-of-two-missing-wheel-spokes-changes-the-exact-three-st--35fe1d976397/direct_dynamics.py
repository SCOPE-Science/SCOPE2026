"""Independent finite-state check of three-state excitation on a wheel with two adjacent omitted spokes.
Run: python3 direct_dynamics.py
Python standard library only.
"""
from collections import Counter
from itertools import product
from fractions import Fraction


def graph(n):
    # Rim vertices 0,...,n-1, central vertex n. Missing spokes (n,0),(n,1).
    adj=[set() for _ in range(n+1)]
    for i in range(n):
        j=(i+1)%n
        adj[i].add(j);adj[j].add(i)
        if i>=2:
            adj[i].add(n);adj[n].add(i)
    return [tuple(sorted(a)) for a in adj]


def update(s,adj,model):
    z=[]
    for v,x in enumerate(s):
        if model=='CCA':
            y=(x+1)%3 if any(s[u]==(x+1)%3 for u in adj[v]) else x
        else:
            y=(x+1)%3 if x!=0 or 1 in [s[u] for u in adj[v]] else 0
        z.append(y)
    return tuple(z)


def orbit_activity(s,adj,model,cache):
    seen={}
    seq=[]
    while s not in seen and s not in cache:
        seen[s]=len(seq)
        seq.append(s)
        s=update(s,adj,model)
    if s in cache:
        ans=cache[s]
    else:
        start=seen[s]
        period=seq[start:]
        changed=sum(1 for v in period if update(v,adj,model)[0]!=v[0])
        if model=='GHM':
            changed=sum(1 for v in period if v[0]==0 and update(v,adj,model)[0]==1)
        ans=Fraction(changed,len(period))
    for v in seq: cache[v]=ans
    return ans


def recurrence_counts(n):
    q0,q1=2,2
    for _ in range(2,n):q0,q1=q1,2*q1+q0
    # q1 is q_{n-1} after n-2 updates (n=5 -> q4=34).
    high=3**(n+1)-27*q1//2
    # T_k = trace(M^k N), T0=6,T1=18,T2=50, and recurrence with char poly lambda^3-3lambda^2+lambda+1.
    ts=[6,18,50]
    for _ in range(3,n-2):ts.append(3*ts[-1]-ts[-2]-ts[-3])
    mid=3*ts[n-3]
    zero=3**(n+1)-high-mid
    return {Fraction(0):zero,Fraction(3,5):mid,Fraction(1):high}


def main():
    total=0
    for n in range(5,9):
        adj=graph(n)
        counts={}
        for model in ('CCA','GHM'):
            cache={};count=Counter()
            for s in product(range(3),repeat=n+1):
                ans=orbit_activity(s,adj,model,cache)
                count[ans]+=1
            counts[model]=count
        expected=recurrence_counts(n)
        assert dict(counts['CCA'])==expected,(n,counts['CCA'],expected)
        assert {3*r:k for r,k in counts['GHM'].items()}==expected,(n,counts['GHM'],expected)
        assert sum(expected.values())==3**(n+1)
        total+=3**(n+1)
        print('rim',n,'states',3**(n+1),'CCA',[(str(k),v) for k,v in sorted(counts['CCA'].items())], 'GHM',[(str(k),v) for k,v in sorted(counts['GHM'].items())])
    print('PASS: independently simulated',total,'configurations under each dynamic')
if __name__=='__main__':main()
