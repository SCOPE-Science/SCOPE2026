from itertools import combinations
from collections import Counter
EDGES=[(i,j) for i in range(8) for j in range(i+1,8)]
def value(indices):
    adj=[[] for _ in range(8)]
    for k in indices:
        a,b=EDGES[k];adj[a].append(b);adj[b].append(a)
    seen=[False]*8
    tdiff=[];u=0
    for start in range(8):
        if seen[start]:continue
        stack=[start];seen[start]=True;colors={start:0};nc=[0,0];v=0;ends=0;bip=True
        while stack:
            a=stack.pop();v+=1;ends+=len(adj[a]);nc[colors[a]]+=1
            for b in adj[a]:
                if b not in colors:colors[b]=1-colors[a]
                elif colors[b]==colors[a]:bip=False
                if not seen[b]:seen[b]=True;stack.append(b)
        edges=ends//2
        if bip:
            if edges!=v-1:return 0
            tdiff.append(abs(nc[0]-nc[1]))
        else:
            if edges!=v:return 0
            u+=1
    return 2**u*tdiff[0] if len(tdiff)==1 else 0
if __name__=='__main__':
    counts=Counter(value(indices) for indices in combinations(range(28),7))
    print('graph determinant magnitudes:', sorted(counts.items()))
    assert counts=={0:662760,2:508896,4:12096,6:288}
    print('GRAPH_ENUMERATION_OK')
