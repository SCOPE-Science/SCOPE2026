"""Independent direct enumeration of edge-open packings in two line graphs.

The Petersen graph uses its outer/inner pentagons and five spokes rather than
its Kneser realization. Every 5-subset of the 30 candidate edges is tested,
so the absence of 5-packings rules out all larger packings by heredity.
"""
from itertools import combinations
from collections import Counter


def edge(a,b):
    return tuple(sorted((a,b)))


def cubic_edges(kind):
    if kind == "petersen":
        return sorted({edge(i,(i+1)%5) for i in range(5)} |
                      {edge(i+5,(i+2)%5+5) for i in range(5)} |
                      {edge(i,i+5) for i in range(5)})
    if kind == "prism":
        return sorted({edge(5*r+i,5*r+(i+1)%5) for i in range(5) for r in (0,1)} |
                      {edge(i,i+5) for i in range(5)})
    raise ValueError(kind)


def run(kind):
    original = cubic_edges(kind)
    assert len(original) == 15
    # Edge endpoints in line graph are original-graph edge IDs.
    line = [(a,b) for a,b in combinations(range(15),2)
            if set(original[a]) & set(original[b])]
    assert len(line) == 30
    line_lookup = set(line)
    # Deliberately determine each incompatible pair by testing the original
    # definition against the *entire* list of 30 line-graph edges.
    incompatible = [[False]*30 for _ in range(30)]
    for i,j in combinations(range(30),2):
        a,b = line[i]; c,d = line[j]
        incompatible[i][j] = incompatible[j][i] = any(
            g not in (line[i],line[j]) and
            ((g[0] in (a,b) and g[1] in (c,d)) or
             (g[1] in (a,b) and g[0] in (c,d)))
            for g in line)
    count=[1]
    for k in range(1,6):
        found=0
        for group in combinations(range(30),k):
            if all(not incompatible[i][j] for i,j in combinations(group,2)):
                found+=1
        count.append(found)
    expected=([1,30,225,530,330,0] if kind=="petersen"
              else [1,30,235,580,415,0])
    assert count==expected, (kind,count)
    print(f"{kind}: degree counts {Counter(sum(row) for row in incompatible)}; exhaustive sizes 0..5 = {count}")

if __name__ == '__main__':
    run('petersen');run('prism')
    print('DIRECT_ENUMERATION_OK')
