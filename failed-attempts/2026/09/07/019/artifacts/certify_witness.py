"""Detailed certification for primary witness rep 8 (|Aut|=1 minimal)."""
import sys, time, json, hashlib
sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts')
from pipeline_lib import *
from gen_cands import invariant_key
import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher
from networkx import weisfeiler_lehman_graph_hash

with open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-23/output/artifacts/census.json') as f:
    data=json.load(f)
rec=[r for r in data if r['rep_index']==8][0]
adj=adj_from_edgelist(26,[tuple(e) for e in rec['edgelist']])
print("witness rep 8 edgelist:", rec['edgelist'])
print("meta:", rec['meta_example'])
# hashes
Gnx=to_networkx(adj)
wl=weisfeiler_lehman_graph_hash(Gnx)
print("WL hash:", wl)
print("invariant_key:", invariant_key(adj))
h=hashlib.sha256(str(sorted(rec['edgelist'])).encode()).hexdigest()
print("sha256(edgelist):", h)
# girth, bridges, aut, coloring
print("girth:", bfs_girth(adj))
print("bridges:", list(nx.bridges(Gnx)))
auts=list(GraphMatcher(Gnx,Gnx).isomorphisms_iter())
print("|Aut|:", len(auts))
print("3-edge-colorable?", is_3_edge_colorable(adj, time_limit=30))
# G non-Ham with node counts: instrument naive + A/B with counters
# For A/B, wrap to count? We'll just time + report; for naive we counted 102206 nodes.
# Re-run A/B decisions + get cycles for G-v (both solvers) to store
print("G ham A:", ham_cycle_A(adj, time_limit=30))
print("G ham B:", ham_cycle_B(adj, time_limit=30))
# all G-v cycles via both solvers, verify
for v in range(26):
    Gv=delete_vertex(adj,v)
    cA=ham_cycle_A(Gv, time_limit=30, return_cycle=True)
    cB=ham_cycle_B(Gv, time_limit=30, return_cycle=True)
    assert cA is not None and cB is not None, f"v {v} failed"
    assert verify_ham_cycle(Gv,cA) and verify_ham_cycle(Gv,cB)
print("all 26 G-v Hamiltonian via both solvers: OK")
# hypotraceability: G has hampath, each G-v has hampath? (G-v Hamiltonian => has path)
print("G has hampath?", ham_path_solver(adj, time_limit=15))
# check a few G-v paths (should be True since Hamiltonian)
# edge list for DRAFT: print adjacency
print("adjacency:")
for u in range(26):
    print(f" {u}: {sorted(adj[u])}")
