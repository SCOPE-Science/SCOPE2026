"""Independent exact-coloring reconstruction from two Fano-side partitions.

Python 3.10+, standard library only. No fixed list of accepted colorings is supplied.
This checker enumerates all partitions on each bipartition side, all possible
nonincident merges, and all valid single-vertex recoloring transitions.
"""
from collections import Counter, deque

N = 7
LINES = tuple(frozenset((j+d)%N for d in (0, 1, 3)) for j in range(N))
INC = tuple(tuple(i in LINES[j] for j in range(N)) for i in range(N))


def partitions(n):
    names = [0]*n
    def visit(pos, used):
        if pos == n:
            blocks = [0]*used
            for v, col in enumerate(names):
                blocks[col] |= 1 << v
            yield tuple(blocks)
            return
        for c in range(used + 1):
            names[pos] = c
            yield from visit(pos+1, max(used, c+1))
    yield from visit(1, 1)


def side_witnesses(part, rows_are_points):
    witnesses = []
    for block in part:
        witnesses.append(sum(1 << w for w in range(N) if all(
            not (block >> u & 1) or (INC[u][w] if rows_are_points else INC[w][u])
            for u in range(N))))
    return tuple(witnesses)


def matching_extensions(points, lines, p_witness, l_witness):
    """Enumerate cross-side class mergers. Two merged classes lack all witnesses."""
    required = len(points) + len(lines) - 8
    if required < 0:
        return
    def dfs(pos, used, matches):
        if len(matches) > required or len(matches) + len(points)-pos < required:
            return
        if pos == len(points):
            if len(matches) != required:
                return
            omitted_p = {i for i,j in matches}
            omitted_l = {j for i,j in matches}
            pw = 0
            lw = 0
            for i,m in enumerate(p_witness):
                if i not in omitted_p: pw |= m
            for j,m in enumerate(l_witness):
                if j not in omitted_l: lw |= m
            if pw != (1<<N)-1 or lw != (1<<N)-1:
                return
            paired = dict(matches)
            whole = [b | (lines[paired[i]] << N if i in paired else 0)
                     for i,b in enumerate(points)]
            whole += [b<<N for j,b in enumerate(lines) if j not in omitted_l]
            yield tuple(sorted(whole))
            return
        yield from dfs(pos+1, used, matches)
        p = points[pos]
        for j,l in enumerate(lines):
            if used & (1<<j):
                continue
            # A color class can join two sides only if there is no incidence.
            if any(p >> i & 1 and l >> k & 1 and INC[i][k]
                   for i in range(N) for k in range(N)):
                continue
            yield from dfs(pos+1, used | (1<<j), matches+((pos,j),))
    yield from dfs(0, 0, ())


def find_all():
    all_partitions = list(partitions(N))
    p_list = [(p,side_witnesses(p,True)) for p in all_partitions]
    l_list = [(p,side_witnesses(p,False)) for p in all_partitions]
    p_list = [(p,w) for p,w in p_list if len(p)>=4 and __import__('functools').reduce(int.__or__,w,0)==127]
    l_list = [(p,w) for p,w in l_list if len(p)>=4 and __import__('functools').reduce(int.__or__,w,0)==127]
    assert Counter(map(lambda z:len(z[0]),p_list)) == {4:49,5:140,6:21,7:1}
    assert Counter(map(lambda z:len(z[0]),l_list)) == {4:49,5:140,6:21,7:1}
    for side in (p_list, l_list):
        profiles = Counter(tuple(sorted(b.bit_count() for b in blocks))
                           for blocks, _ in side if len(blocks)==4)
        assert profiles == {(1,1,1,4):7, (1,1,2,3):42}
    states=set()
    for p,pw in p_list:
        for l,lw in l_list:
            for state in matching_extensions(p,l,pw,lw):
                assert state not in states
                states.add(state)
    return sorted(states)


def one_move_graph(states):
    lookup={s:i for i,s in enumerate(states)}
    edges=[set() for _ in states]
    for i,state in enumerate(states):
        for c,block in enumerate(state):
            if block.bit_count()==1:
                continue
            for v in range(2*N):
                if not block>>v & 1:
                    continue
                for d in range(8):
                    if d==c:continue
                    changed=list(state)
                    changed[c]^=1<<v
                    changed[d]|=1<<v
                    target=lookup.get(tuple(sorted(changed)))
                    if target is not None:
                        edges[i].add(target)
    return edges


def main():
    states=find_all()
    mixed=Counter(sum(bool(s&127 and s>>7) for s in state) for state in states)
    assert len(states)==2751 and mixed=={0:2401,1:322,2:28}
    graph=one_move_graph(states)
    assert all(i in graph[j] for i in range(len(graph)) for j in graph[i])
    assert sum(map(len,graph))//2==11662
    degrees=Counter(map(len,graph))
    assert degrees == {0:21,2:56,5:224,6:476,7:168,10:1806}
    seen=set()
    sizes=[]
    components=[]
    for i in range(len(states)):
        if i in seen:continue
        queue=deque([i]); seen.add(i); nodes=[]
        while queue:
            v=queue.popleft();nodes.append(v)
            for u in graph[v]:
                if u not in seen: seen.add(u);queue.append(u)
        sizes.append(len(nodes));components.append(nodes)
    assert Counter(sizes)=={1:21,966:1,1764:1}
    def is_flag_partition(state):
        pb=[b for b in state if b & 127 and not b >> 7]
        lb=[b >> 7 for b in state if b >> 7 and not (b & 127)]
        if sorted(map(int.bit_count,pb)) != [1,1,1,4]: return False
        if sorted(map(int.bit_count,lb)) != [1,1,1,4]: return False
        point_singles={v for b in pb if b.bit_count()==1 for v in range(7) if b>>v&1}
        line_singles={j for b in lb if b.bit_count()==1 for j in range(7) if b>>j&1}
        supports=[j for j in range(7) if point_singles==set(LINES[j])]
        centers=[v for v in range(7) if line_singles=={j for j in range(7) if INC[v][j]}]
        return len(supports)==len(centers)==1 and INC[centers[0]][supports[0]]
    isolated=[C[0] for C in components if len(C)==1]
    assert len(isolated)==21 and all(is_flag_partition(states[i]) for i in isolated)
    pure_large=next(C for C in components if len(C)==1764)
    for i in pure_large:
        point_sizes=sorted(x.bit_count() for x in states[i] if x & 127)
        line_sizes=sorted((x>>7).bit_count() for x in states[i] if x>>7)
        assert point_sizes==line_sizes==[1,1,2,3]
    assert any(Counter(sum(bool(s&127 and s>>7) for s in states[i]) for i in C)=={0:616,1:322,2:28}
               for C in components)
    print('One-sided witness partitions: 49,140,21,1 at block counts 4,5,6,7')
    print('Optimal total-dominator partitions:',len(states))
    print('Mixed-class counts:',dict(sorted(mixed.items())))
    print('Recoloring edges:',sum(map(len,graph))//2)
    print('Components:',dict(sorted(Counter(sizes).items())))
    print('Degrees:',dict(sorted(degrees.items())))
    print('PASS')

if __name__=='__main__':main()
