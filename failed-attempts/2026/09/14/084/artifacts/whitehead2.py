import itertools, networkx as nx
exec(open('output/artifacts/whitehead.py').read().split("# Validation")[0])

# Wheel patterns: rank n = rim count; adj = cycle C_n
for n in [5,6]:
    adj=[(i,(i+1)%n) for i in range(n)]
    G=whitehead(n,adj)
    print(f"wheel W{n}: rank={n} edges={G.number_of_edges()}")
    import time
    t=time.time()
    print("  min edge cut:",min_edge_cut_size(G), f"({time.time()-t:.1f}s)")
    # also vertex connectivity & min degree
    print("  min degree:",min(dict(G.degree()).values()))
