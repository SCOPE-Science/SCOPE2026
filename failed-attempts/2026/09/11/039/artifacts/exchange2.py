import itertools, sys
sys.path.insert(0, 'output/artifacts')
from engine import is_fano_free, bipartite_edge_set, b_n, min_edit_distance
n=8; nx=4
X=set(range(nx))
B=bipartite_edge_set(n, X)
T=(0,1,2)
cross=list(B)
free2=[]; free3=[]
for a in range(len(cross)):
    for b in range(a+1,len(cross)):
        H2=set(B); H2.add(T); H2.discard(cross[a]); H2.discard(cross[b])
        ff2,_=is_fano_free(n,H2)
        if ff2:
            d2,_=min_edit_distance(n,H2)
            free2.append((d2,(cross[a],cross[b])))
print(f"Fano-free 2-deletion exchanges: {len(free2)}")
for d2,pair in sorted(free2,reverse=True)[:8]:
    print(f"  dist={d2} defect=1 ratio={d2} dels={pair}")
