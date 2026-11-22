"""Exhaustive standard zero-forcing and exchange metric checker for the Herschel graph.
Python 3 standard library only: python verify_direct.py
"""
from collections import Counter, deque
from itertools import combinations
from pathlib import Path
import json

N=11
ADJ={0:(1,3,4),1:(2,5,6),2:(3,7),3:(8,9),4:(5,9),5:(10,),6:(7,10),7:(8,),8:(10,),9:(10,)}
EDGES=sorted({tuple(sorted((a,b))) for a,nb in ADJ.items() for b in nb})
assert len(EDGES)==18
NB=[0]*N
for u,v in EDGES:NB[u]|=1<<v; NB[v]|=1<<u
assert sorted(x.bit_count() for x in NB)==[3]*8+[4]*3
X=1<<N
LEFT=sum(1<<i for i in (0,2,5,6,8,9))
RIGHT=(X-1)^LEFT
assert all((LEFT>>u&1)!=(LEFT>>v&1) for u,v in EDGES)

def closure(start):
    s=start
    while True:
        t=s
        for v in range(N):
            if s>>v&1:
                rem=NB[v]&~s
                if rem!=0 and not(rem&(rem-1)):t|=rem
        if s==t:return s
        s=t

def distances(edges,starts):
    adj={s:[] for s in starts}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    answer={}
    for s in starts:
        d={s:0};Q=deque([s])
        while Q:
            a=Q.popleft()
            for b in adj[a]:
                if b not in d:d[b]=d[a]+1;Q.append(b)
        answer[s]=d
    return answer

def measure():
    forcing=[s for s in range(X) if closure(s)==X-1]
    z=min(s.bit_count() for s in forcing)
    minima=sorted(s for s in forcing if s.bit_count()==z)
    edges=sorted((a,b) for i,a in enumerate(minima) for b in minima[i+1:] if (a^b).bit_count()==2)
    slides=[(a,b) for a,b in edges if any((a^b)==((1<<u)|(1<<v)) for u,v in EDGES)]
    D=distances(edges,minima)
    assert all(len(d)==len(minima) for d in D.values())
    hist=Counter();excess=Counter();exceptions=[]
    for i,a in enumerate(minima):
        for b in minima[i+1:]:
            k=(a^b).bit_count()//2
            d=D[a][b]
            hist[d]+=1; excess[d-k]+=1
            if d-k==2:exceptions.append([a,b])
    return {'n':N,'base_edges':[list(e) for e in EDGES],
            'bipartition_left':[0,2,5,6,8,9],
            'zero_forcing_number':z,'minimum_masks':minima,
            'jump_edges':[list(e) for e in edges],
            'slide_edges':[list(e) for e in slides],
            'minimum_left_count_hist':dict(sorted(Counter((m&LEFT).bit_count() for m in minima).items())),
            'distance_hist':dict(sorted(hist.items())),
            'johnson_excess_hist':dict(sorted(excess.items())),
            'max_excess_pairs':exceptions,
            'eccentricity_hist':dict(sorted(Counter(max(d.values()) for d in D.values()).items()))}

if __name__=='__main__':
    c=json.loads(Path(__file__).with_name('certificate.json').read_text())
    assert measure()=={**c,'minimum_left_count_hist':{int(k):v for k,v in c['minimum_left_count_hist'].items()},'distance_hist':{int(k):v for k,v in c['distance_hist'].items()},'johnson_excess_hist':{int(k):v for k,v in c['johnson_excess_hist'].items()},'eccentricity_hist':{int(k):v for k,v in c['eccentricity_hist'].items()}}
    assert c['zero_forcing_number']==5 and len(c['minimum_masks'])==114
    assert len(c['jump_edges'])==540 and not c['slide_edges']
    assert c['minimum_left_count_hist']=={'3':114}
    assert c['johnson_excess_hist']=={'0':6183,'1':252,'2':6}
    print('DIRECT_PASS 2048 candidates; minimum 5; 114 optima; 540 jumps; zero slides; all ecc 5; excess 0:6183 1:252 2:6')
