"""Delayer strategy for Tseitin on the fixed 60-vertex 3-regular Ramanujan graph.
Game rules (Pudlak-Impagliazzo Prover-Delayer for Resolution width):
- Prover queries unqueried edges; Delayer answers 0/1 or defers ('*', scores 1 point, Prover then picks the value).
- Delayer must never falsify a clause (vertex parity constraint); game ends when some vertex has all 3 incident edges assigned with wrong parity.
- Certified width lower bound = min over all Prover strategies of Delayer's score.
Delayer rule R (bridge-avoidance + forced parity):
- Let U = set of unqueried edges (including queried one e).
- If e is NOT a bridge of the graph (V,U): defer ('*').
- Else (bridge): if exactly one of {0,1} keeps all completed vertices consistent, answer it (0 pts); if both keep consistency, defer; if neither, answer 0 (game already lost).
Validity: a deferred non-bridge query can never complete a vertex (last edge of a vertex is always a bridge), and a deferred both-feasible bridge query keeps completed vertices consistent under either Prover value; so Delayer itself never falsifies. Hence score accumulates until Prover engineers a parity trap.
"""
from collections import deque
import json

def load():
    g = json.load(open("output/artifacts/graph.json"))
    return g["adj"]

def build(adj):
    n = len(adj)
    edges = []
    for u in range(n):
        for v in adj[u]:
            if u < v: edges.append((u, v))
    emap = {e: i for i, e in enumerate(edges)}
    return n, edges, emap

def components(n, adj, emap, unset):
    comp = [-1]*n; nc = 0
    uset = set(unset)
    for s in range(n):
        if comp[s] >= 0: continue
        comp[s] = nc; dq = deque([s])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                ei = emap[(min(u,v),max(u,v))]
                if ei not in uset: continue
                if comp[v] < 0: comp[v] = nc; dq.append(v)
        nc += 1
    return comp, nc

def is_bridge(n, adj, emap, unset, ei):
    rest = set(unset); rest.discard(ei)
    comp, _ = components(n, adj, emap, unset)
    # count components before/after on the affected part: e is bridge iff endpoints connected in unset but not in rest
    c0, _ = components(n, adj, emap, unset)
    c1, _ = components(n, adj, emap, rest)
    u, v = None, None
    # find endpoints
    return c0 is not None and _bridge_check(n, adj, emap, unset, rest, ei)

def _bridge_check(n, adj, emap, unset, rest, ei):
    c0, _ = components(n, adj, emap, unset)
    c1, _ = components(n, adj, emap, rest)
    # endpoints of ei
    for (a,b),i in emap.items():
        if i == ei: u,v = a,b; break
    return c0[u]==c0[v] and c1[u]!=c1[v]

def consistent(n, adj, emap, edges, tau, assign, unset):
    """No completed vertex (no unqueried incident edges) has wrong parity."""
    uset = set(unset)
    rem = list(tau)
    for ei, val in assign.items():
        u, v = edges[ei]; rem[u] ^= val; rem[v] ^= val
    for w in range(n):
        if all(emap[(min(w,v),max(w,v))] not in uset for v in adj[w]):
            if rem[w] & 1: return False
    return True

def delayer_move(n, adj, emap, edges, tau, assign, unset, ei):
    rest = set(unset); rest.discard(ei)
    if not _bridge_check(n, adj, emap, unset, rest, ei):
        return '*'
    a0 = dict(assign); a0[ei]=0
    a1 = dict(assign); a1[ei]=1
    ok0 = consistent(n, adj, emap, edges, tau, a0, rest)
    ok1 = consistent(n, adj, emap, edges, tau, a1, rest)
    if ok0 and ok1: return '*'
    if ok0: return 0
    if ok1: return 1
    return 0

def simulate(n, adj, emap, edges, tau, order, prover):
    assign={}; unset=set(range(len(edges))); score=0; transcript=[]
    for ei in order:
        if ei in assign: continue
        mv = delayer_move(n, adj, emap, edges, tau, assign, unset, ei)
        if mv=='*':
            val = prover(ei, assign, unset); score+=1
            assign[ei]=val; transcript.append((ei,'*',val))
        else:
            assign[ei]=mv; transcript.append((ei,mv,None))
        unset.discard(ei)
        if not consistent(n, adj, emap, edges, tau, assign, unset):
            break
    return score, transcript
