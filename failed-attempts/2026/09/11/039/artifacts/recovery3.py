import itertools, sys
sys.path.insert(0, 'output/artifacts')
from engine import is_fano_free, bipartite_edge_set, b_n, min_edit_distance
n=8; nx=4
X=set(range(nx))
B=bipartite_edge_set(n, X)
T=(0,1,2)
cross=list(B)
# Candidate hitting pairs from tradeoff universe: try all pairs is too big with third loop (1128*46).
# Bounded recovery: fix the min-hitting pair P={(2,6,7),(1,3,5)} found for one copy family, scan third deletion.
P=[(2,6,7),(1,3,5)]
found=None
for d in cross:
    if d in P: continue
    H=set(B); H.add(T)
    for p in P: H.discard(p)
    H.discard(d)
    ff,_=is_fano_free(n,H)
    if ff:
        dd,_=min_edit_distance(n,H)
        found=(d,dd); break
print(f"recovery scan with fixed hitting pair: first Fano-free third deletion: {found}")
if found:
    d,dd=found
    defect=3-1  # 3 dels, 1 add vs B
    print(f"defect={defect} dist={dd} ratio={dd/defect}")
# Also: greedy extend over 5 random hitting pairs? keep bounded: try 6 specific pairs from universe scan
