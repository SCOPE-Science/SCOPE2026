"""Independent direct edge-pattern search in triangular graphs.

For each t=4,...,9, the selected graph pattern is a matching of t/2
vertices when t is even, or one adjacent pair and all other vertices
pairwise nonadjacent when t is odd. Here each graph vertex is an edge
of the hidden complete graph. The pattern must consume t hidden points.
"""
from itertools import combinations

def exists_pattern(n, t):
    r = (t + 1)//2
    graph_vertices = tuple(combinations(range(n), 2))
    for chosen in combinations(graph_vertices, r):
        intersections = [int(bool(set(a)&set(b))) for a,b in combinations(chosen, 2)]
        if sum(intersections) == (t % 2):
            return True
    return False

if __name__ == '__main__':
    checks=0
    for t in range(4, 10):
        absent=exists_pattern(t-1,t)
        present=exists_pattern(t,t)
        assert not absent and present, (t, absent, present)
        print(f't={t}: no witness on {t-1} ground points; witness on {t} ground points')
        checks += 2
    print(f'PASS: {checks} direct witness-existence checks.')
