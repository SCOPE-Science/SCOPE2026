import itertools, networkx as nx
exec(open('output/artifacts/whitehead.py').read().split("# Validation")[0])

def all_min_cuts(G):
    edges=list(G.edges(keys=True))
    out=[]
    for k in range(1,len(edges)+1):
        for combo in itertools.combinations(range(len(edges)),k):
            H=G.copy()
            for idx in sorted(combo,reverse=True):
                u,v,kk=edges[idx]; H.remove_edge(u,v,kk)
            if not nx.is_connected(H):
                return k, combo  # first k with any cut; but want ALL of size k
        # none found at k -> continue
    return None,None

def all_cuts_of_size(G,k):
    edges=list(G.edges(keys=True)); out=[]
    for combo in itertools.combinations(range(len(edges)),k):
        H=G.copy()
        for idx in sorted(combo,reverse=True):
            u,v,kk=edges[idx]; H.remove_edge(u,v,kk)
        if not nx.is_connected(H):
            comps=[set(c) for c in nx.connected_components(H)]
            out.append((combo,sorted([len(c) for c in comps])))
    return out

for n in [5,6]:
    adj=[(i,(i+1)%n) for i in range(n)]
    G=whitehead(n,adj)
    cuts=all_cuts_of_size(G,3)
    print(f"wheel W{n}: num min(3)-edge-cuts = {len(cuts)}")
    from collections import Counter
    print("  component-size histogram:",Counter(tuple(c[1]) for c in cuts))
    # show the cuts as edge labels
    edges=list(G.edges(keys=True))
    for combo,sizes in cuts[:40]:
        print("   ",sorted([ (edges[i][0],edges[i][1]) for i in combo]),"comps",sizes)
