"""Exhaustive wheel NOR basin verification, independent of the Lucas recurrence."""
from collections import Counter

def analyze(n):
    assert 3 <= n <= 13
    vertices = n+1
    edges = {(i,(i+1)%n) for i in range(n)} | {(i,n) for i in range(n)}
    neighbor = [0]*vertices
    for u,v in edges:
        neighbor[u] |= 1 << v
        neighbor[v] |= 1 << u
    total = 1 << vertices
    nxt = [sum(1 << v for v in range(vertices) if (s & neighbor[v]) == 0)
           for s in range(total)]
    assert all(nxt[nxt[nxt[s]]] == nxt[s] for s in range(total))
    zero = 0
    full = total-1
    assert nxt[zero] == full and nxt[full] == zero
    basin = sum(1 for s in range(total) if nxt[s] in (zero,full))
    # F^3=F proves all states reach a periodic orbit in at most one update.
    T = sum(1 for x in range(1 << n)
            if all((x >> ((i-1)%n)) & 1 or (x >> ((i+1)%n)) & 1
                   for i in range(n)))
    assert basin == (1 << n) + T
    recurrent = sum(nxt[nxt[s]] == s for s in range(total))
    fixed = sum(nxt[s] == s for s in range(total))
    print(f'n={n} total={total} giant_basin={basin} total_dominating={T} '
          f'fixed={fixed} recurrent={recurrent}')
    return T,basin

if __name__ == '__main__':
    L=[2,1]
    for k in range(2,14): L.append(L[-1]+L[-2])
    for n in range(3,14):
        T,B=analyze(n)
        assert T == (L[n] if n%2 else L[n//2]**2)
        assert B > (1 << n)
    print('PASS: 11 complete finite-state spaces; all claimed formulas.')
