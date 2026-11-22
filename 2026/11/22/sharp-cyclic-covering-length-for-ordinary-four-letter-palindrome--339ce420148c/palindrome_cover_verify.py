"""Independent exact checks for circular covers of ordinary four-symbol palindromes.

No external dependencies. Run: python palindrome_cover_verify.py
"""
from collections import defaultdict


def words(q):
    return [f'{a}{b}{b}{a}' for a in range(q) for b in range(q)]


def cover(q):
    if q == 2:
        return '011001111000'
    pairs = []
    if q % 2:
        pairs = [(a, b) for a in range(q) for b in range(a+1, q)]
    else:
        pairs = [(a, b) for a in range(q) for b in range(a+1, q)
                 if not (a % 2 == 0 and b == a+1)]
    adjacency = defaultdict(list)
    for i, (a, b) in enumerate(pairs):
        adjacency[a].append((b, i))
        adjacency[b].append((a, i))
    used = set()
    stack = [(0, None)]
    reverse_tour = []
    while stack:
        v = stack[-1][0]
        while adjacency[v] and adjacency[v][-1][1] in used:
            adjacency[v].pop()
        if adjacency[v]:
            nxt, edge = adjacency[v].pop()
            assert edge not in used
            used.add(edge)
            stack.append((nxt, edge))
        else:
            reverse_tour.append(stack.pop())
    route = list(reversed(reverse_tour))
    assert len(used) == len(pairs) and len(route) == len(pairs)+1
    targets = []
    touched = set()
    for i in range(len(route)-1):
        a, b = route[i][0], route[i+1][0]
        if a not in touched:
            targets.append(f'{a}{a}{a}{a}')
            if q % 2 == 0:
                partner = a+1 if a % 2 == 0 else a-1
                targets.append(f'{a}{partner}{partner}{a}')
            touched.add(a)
        targets.extend((f'{a}{b}{b}{a}',f'{b}{a}{a}{b}'))
    assert len(targets) == q*q and set(targets) == set(words(q))
    output = []
    for i, w in enumerate(targets):
        nxt = targets[(i+1) % len(targets)]
        shift = next((d for d in range(1,5) if w[d:]==nxt[:4-d]), None)
        assert shift is not None,(q,i,w,nxt,targets)
        assert shift == (2 if i+1 < len(targets) and
                             targets[i+1] == f'{w[-1]}{w[0]}{w[0]}{w[-1]}' and
                             w[0] != w[-1] else shift)
        assert shift in (2,3)
        output.append(w[:shift])
    return ''.join(output)


def overlaps(p, q):
    return min(d for d in range(1,5) if p[d:] == q[:4-d])


def held_karp_cost(q):
    """Exact Hamiltonian tour DP; q<=4 (16 targets at most)."""
    ws = words(q)
    n = len(ws)
    assert n <= 16
    distances = [[overlaps(x,y) for y in ws] for x in ws]
    inf=10**9
    # Fix the first palindrome, permitted by cyclic rotation of target order.
    dp = [[inf]*n for _ in range(1<<n)]
    dp[1][0]=0
    for mask in range(1,1<<n,2):
        if mask == 1:
            pass
        for last in range(n):
            best=dp[mask][last]
            if best==inf:continue
            remain=((1<<n)-1)^mask
            while remain:
                bit=remain&-remain
                nxt=bit.bit_length()-1
                nm=mask|bit
                candidate=best+distances[last][nxt]
                if candidate<dp[nm][nxt]:dp[nm][nxt]=candidate
                remain^=bit
    return min(dp[(1<<n)-1][i]+distances[i][0] for i in range(1,n))


def check():
    for q in range(2,11):
        s=cover(q)
        expected=(5*q*q+q)//2 if q%2 else (5*q*q+2*q)//2
        assert len(s)==expected,(q, len(s),expected)
        allwindows={(s+s[:3])[i:i+4] for i in range(len(s))}
        assert set(words(q)).issubset(allwindows),(q,set(words(q))-allwindows)
    for q in (2,3,4):
        answer=held_karp_cost(q)
        expected=(5*q*q+q)//2 if q%2 else (5*q*q+2*q)//2
        assert answer==expected,(q,answer,expected)
    print('VERIFY_OK constructions q=2..10; exact independent tours q=2..4')

if __name__=='__main__':check()
