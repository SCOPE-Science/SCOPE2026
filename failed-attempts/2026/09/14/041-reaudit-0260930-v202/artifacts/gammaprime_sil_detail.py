"""Deeper probe of Gamma'(Lambda): for each SIL-pair (x,y), record
  |lk(x) cap lk(y)|, #components of G-(lk cap lk), and comp-membership of x,y.
  Distinguishes: (i) no SIL at all (Cor 3.2 regime, if also no transvections);
  (ii) SILs but joined outside (no-maximal regime); (iii) admits maximal system.
Also record support-graph forest status and transvections.
"""
import itertools, json
import networkx as nx
from gammaprime_scan import build_gamma_prime

def link(G,v): return set(G.neighbors(v))

def sil_detail(G):
    det=[]
    for a,b in itertools.combinations(sorted(G.nodes()),2):
        if G.has_edge(a,b): continue
        S=link(G,a)&link(G,b)
        H=G.copy(); H.remove_nodes_from(S)
        comps=list(nx.connected_components(H))
        wit=[sorted(C) for C in comps if a not in C and b not in C]
        if wit:
            det.append({"pair":[a,b],"cap":len(S),
                        "ncomp":len(comps),"witness":wit,
                        "joined_outside":any(nx.has_path(H,a,b) for _ in [0]) if (H.has_node(a) and H.has_node(b)) else False})
    return det

tests = {"empty3":nx.empty_graph(3),"path3":nx.path_graph(3),
 "complete3":nx.complete_graph(3),"empty4":nx.empty_graph(4),
 "cycle4":nx.cycle_graph(4),"path4":nx.path_graph(4),
 "complete4":nx.complete_graph(4),"disconn4":nx.Graph([(0,1),(2,3)]),
 "empty5":nx.empty_graph(5),"tree5":nx.path_graph(5)}
out={}
for label,L in tests.items():
    L=nx.convert_node_labels_to_integers(L)
    G=build_gamma_prime(L)
    d=sil_detail(G)
    print("="*70); print(label, "nsil=",len(d))
    for e in d[:12]: print("  ",e["pair"],"cap=",e["cap"],"ncomp=",e["ncomp"],"joined=",e["joined_outside"])
    out[label]=d
with open("output/artifacts/gammaprime_sil_detail.json","w") as f: json.dump(out,f,indent=1)
print("saved")
