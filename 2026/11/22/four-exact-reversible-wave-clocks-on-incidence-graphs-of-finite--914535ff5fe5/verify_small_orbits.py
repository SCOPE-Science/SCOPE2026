"""Independent exhaustive state-iteration checks on two smallest examples.

No matrix operations: update is direct vertex-neighbor parity plus the past state.
"""
from collections import Counter

def direct(graph,expected):
    n=len(graph); masks=[sum(1<<j for j in nbrs) for nbrs in graph]
    def update(pair):
        now=pair & ((1<<n)-1);past=pair>>n
        nxt=0
        for i,nb in enumerate(masks):
            if (now&nb).bit_count()%2:nxt|=1<<i
        return (now<<n)|(nxt^past)
    population=Counter()
    for start in range(1<<(2*n)):
        x=update(start);p=1
        while x!=start:
            x=update(x);p+=1
            assert p<=max(expected)
        population[p]+=1
    assert dict(population)==expected, (population,expected)
    print(f'PASS: {n} vertices, {1<<(2*n)} labelled states, primitive period census {dict(sorted(population.items()))}')

if __name__=='__main__':
    # Three points and three two-point lines: the six-cycle incidence graph.
    direct([[3,5],[3,4],[4,5],[0,1],[1,2],[0,2]],
           {1:4,2:12,3:60,6:4020})
    # Four points in a 2x2 grid, with its four rows/columns as lines.
    direct([[4,6],[4,7],[5,6],[5,7],[0,1],[2,3],[0,2],[1,3]],
           {1:4,2:12,4:240,8:65280})
