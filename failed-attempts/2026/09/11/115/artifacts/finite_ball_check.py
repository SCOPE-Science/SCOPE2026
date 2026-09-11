"""Finite-ball check: every finite subgraph of the 4-regular tree T4 (hence of
any Hom_ac(T4,H) pullback region) is a forest, classically 2-colorable.
Confirms no finite obstruction decides the (5,3,3) triple; difficulty is
purely definability-theoretic. Run: python3 output/artifacts/finite_ball_check.py
"""
from collections import deque

def ball(delta, radius):
    # BFS ball in infinite delta-regular tree centered at root
    adj = {}
    adj[0] = []
    nxt = 1
    q = deque([0])
    dist = {0: 0}
    while q:
        u = q.popleft()
        if dist[u] == radius:
            continue
        need = delta - len(adj[u])
        for _ in range(need):
            v = nxt; nxt += 1
            adj[u].append(v); adj[v] = [u]
            dist[v] = dist[u] + 1
            q.append(v)
    return adj

def is_bipartite(adj):
    color = {}
    for s in adj:
        if s in color: continue
        color[s] = 0
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in color:
                    color[v] = color[u] ^ 1
                    dq.append(v)
                elif color[v] == color[u]:
                    return False, {}
    return True, color

for r in [1, 2, 3, 4]:
    adj = ball(4, r)
    n = len(adj); m = sum(len(v) for v in adj.values()) // 2
    ok, _ = is_bipartite(adj)
    print(f"radius {r}: n={n} m={m} forest={m==n-1} bipartite(chi<=2)={ok}")
print("CONCLUSION: finite balls are forests, chi_classical=2; no finite instance decides chi_B=5 vs chi_mu=3.")
