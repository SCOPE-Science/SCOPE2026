"""Exact finite boundary checks for the robust clique complexes of a star-deficient biclique.
Run with python3 verify.py. Python stdlib only.
"""
from itertools import combinations
from math import comb
import json

def c(n,r):
    return comb(n,r) if 0<=r<=n else 0

def faces_bruteforce(a,b,k,t):
    # Directly test independence of EVERY k-subset in each candidate face.
    # A vertices [0,a), hub=0, B vertices [a,a+b); absent edges (0,a),...,(0,a+t-1).
    n=a+b
    edges={(x,y) for x in range(a) for y in range(a,a+b) if x!=0 or y>=a+t}
    indep_k=[]
    for C in combinations(range(n),k):
        if all((min(x,y),max(x,y)) not in edges for x,y in combinations(C,2)):
            indep_k.append(sum(1<<z for z in C))
    by_dim={}
    for bitmask in range(1,1<<n):
        if not any((bitmask&bad)==bad for bad in indep_k):
            dim=bitmask.bit_count()-1
            by_dim.setdefault(dim,[]).append(bitmask)
    return by_dim

def gf2_rank(cols):
    pivots={}
    for x in cols:
        while x:
            pivot=x.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=x;break
            x^=pivots[pivot]
    return len(pivots)

def modp_rank(columns,p):
    pivots={}
    for col in columns:
        col=dict(col)
        while col:
            q=max(col)
            if q not in pivots:
                factor=pow(col[q],-1,p)
                pivots[q]={j:(v*factor)%p for j,v in col.items() if v%p}
                break
            z=col[q]
            for j,v in pivots[q].items():
                nv=(col.get(j,0)-z*v)%p
                if nv: col[j]=nv
                elif j in col: del col[j]
    return len(pivots)

def homology(faces,p):
    maxd=max(faces)
    ranks={}
    for d in range(1,maxd+1):
        lower={s:i for i,s in enumerate(faces.get(d-1,[]))}
        if p==2:
            cols=[]
            for m in faces.get(d,[]):
                x=0
                for v in range(m.bit_length()):
                    if (m>>v)&1: x^=1<<lower[m^(1<<v)]
                cols.append(x)
            ranks[d]=gf2_rank(cols)
        else:
            cols=[]
            for m in faces.get(d,[]):
                vs=[v for v in range(m.bit_length()) if (m>>v)&1]
                col={lower[m^(1<<v)]: (1 if i%2==0 else p-1) for i,v in enumerate(vs)}
                cols.append(col)
            ranks[d]=modp_rank(cols,p)
    bettis={}
    for d in range(0,maxd+1):
        bettis[d]=len(faces.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
    return {d:v for d,v in bettis.items() if v}

def predicted(a,b,k,t):
    high=c(a-2,k-1)*c(b-1,k-1)
    if t<b:
        high+=c(a-2,k-2)*(c(b-1,k-1)-c(t,k-1))
        return {2*k-3:high} if high else {}
    low=c(a-2,k-2)*c(b-1,k-2)
    return {2*k-4:low,2*k-3:high}

def main():
    tests=[]
    for a,b,k in [(4,4,3),(4,5,3),(5,4,3),(5,5,3),(5,5,4),(5,6,4),(6,5,4)]:
        for t in range(b+1):
            f=faces_bruteforce(a,b,k,t)
            expected=predicted(a,b,k,t)
            for p in [2,3]:
                observed=homology(f,p)
                assert observed==expected,(a,b,k,t,p,observed,expected)
            tests.append({'a':a,'b':b,'k':k,'deleted':t,'face_count':sum(map(len,f.values())),'homology':expected})
    print(json.dumps({'status':'PASS','cases':len(tests),'prime_fields':[2,3],'samples':tests},sort_keys=True))
if __name__=='__main__': main()
