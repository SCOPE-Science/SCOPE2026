"""Exact length-four constant-GC DNA codebook census for one adjacent swap.
Standard library only; run: python verify.py
"""
from itertools import product, combinations
from collections import deque

ALPH = 'ACGT'
COMP = dict(zip(ALPH, 'TGCA'))

def reverse_complement(word):
    return ''.join(COMP[char] for char in reversed(word))

def adjacent_swap_ball(word):
    result = {word}
    for pos in range(3):
        copy = list(word)
        copy[pos], copy[pos + 1] = copy[pos + 1], copy[pos]
        result.add(''.join(copy))
    return frozenset(result)

def components(adjacency):
    unseen = set(range(len(adjacency)))
    out = []
    while unseen:
        first = min(unseen)
        unseen.remove(first)
        queue = deque([first])
        block = [first]
        while queue:
            vertex = queue.popleft()
            for next_vertex in sorted(adjacency[vertex] & unseen):
                unseen.remove(next_vertex)
                queue.append(next_vertex)
                block.append(next_vertex)
        out.append(sorted(block))
    return out

def local_census(block, adjacency):
    optimal_size = -1
    count = 0
    witness = None
    m = len(block)
    for mask in range(1 << m):
        selected = tuple(block[j] for j in range(m) if mask >> j & 1)
        if len(selected) < optimal_size:
            continue
        if any(b in adjacency[a] for a, b in combinations(selected, 2)):
            continue
        if len(selected) > optimal_size:
            optimal_size = len(selected)
            count = 0
            witness = selected
        count += 1
    return optimal_size, count, witness

def main():
    balanced = [''.join(chars) for chars in product(ALPH, repeat=4)
                if sum(char in 'CG' for char in chars) == 2]
    assert len(balanced) == 96
    fixed = [word for word in balanced if reverse_complement(word) == word]
    assert len(fixed) == 8
    orbits = sorted({tuple(sorted((word, reverse_complement(word))))
                     for word in balanced if word != reverse_complement(word)})
    assert len(orbits) == 44
    legal_orbits = [pair for pair in orbits
                    if adjacent_swap_ball(pair[0]).isdisjoint(adjacent_swap_ball(pair[1]))]
    assert len(legal_orbits) == 40
    shadows = [set().union(*(adjacent_swap_ball(word) for word in pair))
               for pair in legal_orbits]
    adjacency = [set() for _ in legal_orbits]
    for a,b in combinations(range(len(legal_orbits)), 2):
        if not shadows[a].isdisjoint(shadows[b]):
            adjacency[a].add(b)
            adjacency[b].add(a)
    edges = sum(map(len, adjacency)) // 2
    assert edges == 100
    blocks = components(adjacency)
    assert sorted(map(len, blocks)) == [4, 6, 6, 12, 12]
    local = [local_census(block, adjacency) for block in blocks]
    assert sorted((len(block), size, number)
                  for block, (size, number, _) in zip(blocks, local)) == [
                  (4,1,4),(6,2,3),(6,2,3),(12,3,12),(12,3,12)]
    maximum_pairs = sum(size for size, _, _ in local)
    optimal_codebooks = 1
    for _, count, _ in local:
        optimal_codebooks *= count
    assert maximum_pairs == 11
    assert optimal_codebooks == 5184
    selected = [v for _, _, witness in local for v in witness]
    code = sorted({word for v in selected for word in legal_orbits[v]})
    assert len(code) == 22
    assert set(map(reverse_complement, code)) == set(code)
    assert all(sum(letter in 'CG' for letter in word) == 2 for word in code)
    assert all(word != reverse_complement(word) for word in code)
    assert all(adjacent_swap_ball(a).isdisjoint(adjacent_swap_ball(b))
               for a,b in combinations(code,2))
    print('GC_BALANCED_WORDS',len(balanced))
    print('SELF_RC_WORDS',len(fixed))
    print('NONTRIVIAL_RC_ORBITS',len(orbits))
    print('ADMISSIBLE_RC_ORBITS',len(legal_orbits))
    print('CONFLICT_EDGES',edges)
    print('COMPONENTS',[(len(b),s,c) for b,(s,c,_) in zip(blocks,local)])
    print('MAXIMUM_PAIRS',maximum_pairs)
    print('MAXIMUM_CODEWORDS',len(code))
    print('LABELED_OPTIMA',optimal_codebooks)
    print('WITNESS',' '.join(code))
    print('PASS_ALL_EXHAUSTIVE_CERTIFICATES')

if __name__ == '__main__':
    main()
