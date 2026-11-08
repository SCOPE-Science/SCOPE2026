"""Independent all-permutation enumeration for the 231-avoiding adjacent-swap metric.
Usage: python3 verify_bruteforce.py
"""
from collections import deque
from itertools import permutations

def avoids_231(p):
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            for k in range(j + 1, len(p)):
                if p[k] < p[i] < p[j]:
                    return False
    return True

def inversions(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def bfs(n):
    states = set(p for p in permutations(range(1,n+1)) if avoids_231(p))
    a = tuple(range(n-1,0,-1)) + (n,)
    b = tuple(range(n,0,-1))
    assert a in states and b in states
    distance = {a:0}; pending = deque([a])
    while pending:
        state=pending.popleft()
        for i in range(n-1):
            nxt=list(state)
            nxt[i],nxt[i+1]=nxt[i+1],nxt[i]
            nxt=tuple(nxt)
            if nxt in states and nxt not in distance:
                distance[nxt]=distance[state]+1
                pending.append(nxt)
    return len(states), len(distance), distance[b], inversions(a), inversions(b)

if __name__ == '__main__':
    expected=[1,2,5,14,42,132,429,1430]
    for n in range(1,9):
        v,conn,d,ia,ib=bfs(n)
        assert v==expected[n-1] and conn==v, (n,v,conn)
        assert d==(n-1)**2 and ia+ib==d, (n,d)
        print(f'n={n} states={v} connected={conn} distance={d} ambient={n-1}')
    print('BRUTEFORCE_PASS')
