"""Independent direct graph-state check; no use of sector or page polynomials."""
from itertools import product


def exact_by_graph(m):
    n = 2 + 2*m
    adj = [[] for _ in range(n)]
    def connect(i,j):
        adj[i].append(j); adj[j].append(i)
    connect(0, 1)
    for i in range(m):
        x, y = 2+2*i, 3+2*i
        connect(0,x); connect(1,y); connect(x,y)
    agreed = disagreed = 0
    for state in product((0,1,2), repeat=n):
        stable = True
        for v in range(n):
            tally = [0,0,0]
            for u in adj[v]:
                tally[state[u]] += 1
            winner = max(tally)
            if tally.count(winner)==1 and tally[state[v]]!=winner:
                stable = False
                break
        if stable:
            if state[0] == state[1]:agreed += 1
            else:disagreed += 1
    return agreed, disagreed, agreed+disagreed

if __name__ == '__main__':
    expected = [(15,24,39),(39,54,93),(183,348,531),(879,4230,5109),(3003,17976,20979)]
    for m in range(1,6):
        got = exact_by_graph(m)
        assert got == expected[m-1], (m,got)
        print(m,*got)
    print('GRAPH_BRUTEFORCE_OK')
