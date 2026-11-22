#!/usr/bin/env python3
"""Exact finite tests of the one-point metric-amalgam matching.
No external dependencies. Python 3.9+.
"""
from itertools import product
from collections import defaultdict, deque
from random import Random


def glued(factors):
    # factors: integer distance matrices with common distinguished index 0
    sizes=[len(a) for a in factors]
    labels=[(0,0)]
    labels += [(j,i) for j,M in enumerate(factors) for i in range(1,len(M))]
    def dist(x,y):
        i,a=labels[x]; j,b=labels[y]
        if x==0: return factors[j][0][b]
        if y==0: return factors[i][a][0]
        if i==j: return factors[i][a][b]
        return factors[i][a][0]+factors[j][0][b]
    return labels,dist


def nerve(labels,dist,r):
    out={0:[(i,) for i in range(len(labels))]}
    for n in range(1,r+1):
        out[n]=[]
        for tup in out[n-1]:
            length=sum(dist(x,y) for x,y in zip(tup,tup[1:]))
            for v in range(len(labels)):
                if v!=tup[-1] and length+dist(tup[-1],v)<=r:
                    out[n].append(tup+(v,))
        if not out[n]:break
    return out


def pair(t, labels):
    # Returns (lower,higher) or None for a critical all-one-factor cell.
    prior=None
    for j,x in enumerate(t):
        factor,idx=labels[x]
        if idx==0:continue
        if prior is None:prior=factor
        elif prior!=factor:
            if t[j-1]==0:
                return t[:j-1]+t[j:],t
            return t,t[:j]+(0,)+t[j:]
    return None


def mod2_ranks(cells):
    def faces(t):
        for j in range(len(t)):
            q=t[:j]+t[j+1:]
            if len(q)==1 or all(a!=b for a,b in zip(q,q[1:])):
                yield q
    ranks=[]
    for k in range(1,len(cells)):
        lower={s:i for i,s in enumerate(cells[k-1])}
        pivots={}
        for t in cells[k]:
            val=0
            for s in faces(t):val ^= 1<<lower[s]
            while val:
                q=val.bit_length()-1
                if q not in pivots:
                    pivots[q]=val;break
                val^=pivots[q]
        ranks.append(len(pivots))
    bettis=[]
    for k in range(len(cells)):
        below=ranks[k-1] if k else 0
        above=ranks[k] if k<len(ranks) else 0
        bettis.append(len(cells[k])-below-above)
    return tuple(bettis)


def verify(factors,r, do_ranks=True):
    labels,dist=glued(factors)
    c=nerve(labels,dist,r)
    allcells={s for layer in c.values() for s in layer}
    matched={}
    critical=0
    for t in allcells:
        p=pair(t,labels)
        if p is None:
            critical+=1
            assert len({labels[x][0] for x in t if x!=0})<=1
        else:
            low,high=p
            assert low in allcells and high in allcells
            assert len(high)==len(low)+1
            assert sum(dist(x,y) for x,y in zip(low,low[1:])) == sum(dist(x,y) for x,y in zip(high,high[1:]))
            assert pair(low,labels)==(low,high) and pair(high,labels)==(low,high)
            matched[low]=high
    # All matched pairs have unique lower/upper and no critical mixed cells.
    assert len(set(matched.values()))==len(matched)
    assert 2*len(matched)+critical==len(allcells)
    # Directed gradient graph: lower -> matched upper; all other edges upper -> lower
    directed=defaultdict(list)
    indeg={t:0 for t in allcells}
    for top in allcells:
        if len(top)<2:continue
        for j in range(len(top)):
            face=top[:j]+top[j+1:]
            if not face or any(a==b for a,b in zip(face,face[1:])):continue
            if matched.get(face)==top:
                u,v=face,top
            else:
                u,v=top,face
            directed[u].append(v);indeg[v]+=1
    queue=deque([s for s,d in indeg.items() if d==0]); done=0
    while queue:
        u=queue.popleft();done+=1
        for v in directed[u]:
            indeg[v]-=1
            if indeg[v]==0:queue.append(v)
    assert done==len(allcells), (factors,r,'cycle',done,len(allcells))
    if do_ranks:
        W={k:[t for t in v if pair(t,labels) is None] for k,v in c.items()}
        bfull=mod2_ranks(c); bwedge=mod2_ranks(W)
        assert bfull==bwedge,(factors,r,bfull,bwedge)
    return len(allcells),len(matched),critical,mod2_ranks(c) if do_ranks else ()


def main():
    # All symmetric equilateral multiarm spaces, and asymmetric / irregular quasi-metrics.
    q1=[[0,1,3],[2,0,2],[1,2,0]]
    q2=[[0,2,1],[1,0,1],[3,2,0]]
    # These are shortest path metrics from directed weighted edges; triangle holds.
    for M in (q1,q2):
        for i in range(len(M)):
            for j in range(len(M)):
                for k in range(len(M)):
                    assert M[i][j]<=M[i][k]+M[k][j]
    cases=[
      [[[0,1],[1,0]],[[0,1],[1,0]]],
      [[[0,1,1],[1,0,1],[1,1,0]],[[0,1],[1,0]]],
      [[[0,1],[2,0]],[[0,2],[1,0]],[[0,1],[1,0]]],
      [q1,q2],
    ]
    count=total=0
    for factors in cases:
        for r in range(0,6):
            # bounded to keep exact elimination quick
            nr, np, nc, h=verify(factors,r,do_ranks=(r<=4))
            count+=1;total+=nr
            print('case',len(factors),'sizes',tuple(map(len,factors)),'r',r,'cells',nr,'pairs',np,'critical',nc,'betti',h)
    # Additional reproducible asymmetric shortest-path quasi-metric tests.
    rng=Random(20261118)
    for trial in range(12):
        factors=[]
        for idx in range(2+trial%2):
            n=2+(idx+trial)%2
            M=[[0 if a==b else rng.randint(1,4) for b in range(n)] for a in range(n)]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        M[i][j]=min(M[i][j],M[i][k]+M[k][j])
            assert all(M[a][b]<=M[a][c]+M[c][b] for a in range(n) for b in range(n) for c in range(n))
            factors.append(M)
        for r in range(4):
            nr,np,nc,h=verify(factors,r,do_ranks=True)
            count+=1;total+=nr
            print('random',trial,'r',r,'cells',nr,'pairs',np,'critical',nc,'betti',h)
    # A graph-geodesic illustration with two four-cycles attached at one point.
    M=[[min((i-j)%4,(j-i)%4) for j in range(4)] for i in range(4)]
    for r in range(4):
        nr,np,nc,h=verify([M,M],r)
        count+=1;total+=nr
        print('two-four-cycles','r',r,'cells',nr,'pairs',np,'critical',nc,'betti',h)
    print('PASS',count,'finite parameter instances;',total,'cells verified')
if __name__=='__main__':main()
