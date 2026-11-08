"""Direct labelled Kneser-graph domination census, independent of patterns."""
from itertools import combinations
from math import comb
C={4:720,5:33120,6:257040,7:655200,8:624960,9:181440}
import sys
limit = 10 if "--extended" in sys.argv else 9
for n in range(5,limit):
    graph_vertices=list(combinations(range(n),2))
    neighbours=[]
    for u in graph_vertices:
        neighbours.append(sum(1<<i for i,v in enumerate(graph_vertices) if set(u).isdisjoint(v)))
    full=(1<<len(graph_vertices))-1
    count=[0]; maxdepth=[0]
    def explore(used,dominated,depth):
        maxdepth[0]=max(maxdepth[0],depth)
        if dominated==full:
            if depth==6:count[0]+=1
            return
        if depth>=6:return
        for i,bits in enumerate(neighbours):
            if not (used>>i)&1 and bits&~dominated:
                explore(used|(1<<i),dominated|bits,depth+1)
    explore(0,0,0)
    pred=sum(v*comb(n,k) for k,v in C.items() if n>=k)
    assert count[0]==pred,(n,count[0],pred)
    assert maxdepth[0]==6
    print(f'PASS KG({n},2) maximal ordered sequences {count[0]}',flush=True)
