#!/usr/bin/env python3
"""Independent Pappus incidence/matching verification (stdlib only)."""
import collections
import itertools
import json
import sys
from pathlib import Path

# The nine blocks of a Pappus 9_3 incidence configuration, point labels 0..8.
BLOCKS = ((0,1,4),(1,2,5),(0,2,3),(3,4,7),(4,5,8),
          (3,5,6),(1,6,7),(2,7,8),(0,6,8))


def incidence_graph():
    # Relabel points to even integers, blocks to odd integers.
    edges = sorted(tuple(sorted((2*p, 2*j+1))) for j,block in enumerate(BLOCKS) for p in block)
    assert len(edges)==27
    around=[[] for _ in range(18)]
    for e,(u,v) in enumerate(edges):
        around[u].append(e)
        around[v].append(e)
    assert all(len(a)==3 for a in around)
    # No pair of points lies together on two blocks (girth >= 6).
    pairs=[tuple(sorted(pair)) for block in BLOCKS for pair in itertools.combinations(block,2)]
    assert len(set(pairs))==len(pairs)
    return edges,around


def perfect_matchings(edges, around):
    output=[]
    # Descend on unmatched vertex rather than assigning edge colors.
    def dfs(free, selected):
        if not free:
            output.append(frozenset(selected))
            return
        v=min(free)
        for e in around[v]:
            u,w=edges[e]
            other=w if u==v else u
            if other in free:
                dfs(free-{v,other},selected+(e,))
    dfs(set(range(18)),())
    assert len(output)==42 and len(set(output))==42
    return output


def colorings_from_factorizations(edges, matchings):
    all_edges=frozenset(range(len(edges)))
    matching_set=set(matchings)
    found=set()
    for a in matchings:
        for b in matchings:
            if a & b:
                continue
            c=all_edges-(a|b)
            if c not in matching_set:
                continue
            s=tuple(0 if i in a else 1 if i in b else 2 for i in range(27))
            found.add(''.join(map(str,s)))
    assert len(found)==120
    return sorted(found)


def bichromatic_cycles(s, pair, edges):
    a,b=pair
    # Each vertex has exactly two selected incident edges; trace vertex cycles.
    neigh=[[] for _ in range(18)]
    for e,(u,v) in enumerate(edges):
        if int(s[e]) in pair:
            neigh[u].append((v,e));neigh[v].append((u,e))
    assert all(len(adj)==2 for adj in neigh)
    free=set(range(18));cycles=[]
    while free:
        first=min(free)
        cur=first;prev=None;arc=[]
        while True:
            free.discard(cur)
            opts=[(w,e) for w,e in neigh[cur] if w!=prev]
            assert len(opts)==1 if prev is not None else len(opts)==2
            nxt,e=opts[0]
            arc.append(e)
            if nxt==first:break
            prev,cur=cur,nxt
        assert len(arc)%2==0
        assert len(set(arc))==len(arc)
        cycles.append(tuple(arc))
    return cycles


def independent_graph(states, edges):
    ids={s:i for i,s in enumerate(states)}
    adjacency=[]
    shapes=collections.Counter()
    for s in states:
        out=set();cycle_patterns=[]
        for a,b in itertools.combinations(range(3),2):
            cycles=bichromatic_cycles(s,(a,b),edges)
            cycle_patterns.append(tuple(sorted(len(c) for c in cycles)))
            for cyc in cycles:
                new=list(s)
                for e in cyc:
                    new[e]=str(b if int(s[e])==a else a)
                out.add(ids[''.join(new)])
        shapes[tuple(sorted(cycle_patterns))]+=1
        adjacency.append(sorted(out))
    assert shapes[((6,6,6),(18,),(18,))]==108
    assert shapes[((6,6,6),)*3]==12
    assert len(shapes)==2
    return adjacency


def independent_metrics(states, adj):
    unseen=set(range(len(states)));results=[]
    while unseen:
        root=min(unseen);D={root:0};q=collections.deque([root]);unseen.remove(root)
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in D:
                    assert v in unseen
                    D[v]=D[u]+1
                    unseen.remove(v);q.append(v)
        C=sorted(D)
        assert len(C)==60
        dist_counts=collections.Counter();sphere=collections.Counter();bip_color={}
        for r in C:
            bfs={r:0};queue=collections.deque([r])
            while queue:
                u=queue.popleft()
                for v in adj[u]:
                    if v not in bfs:
                        bfs[v]=bfs[u]+1;queue.append(v)
            assert len(bfs)==60 and max(bfs.values())==4
            shape=tuple(sum(d==i for d in bfs.values()) for i in range(5))
            sphere[(len(adj[r]),shape)]+=1
            for v,d in bfs.items():
                if v>r:dist_counts[d]+=1
            if not bip_color:
                bip_color={v:d%2 for v,d in bfs.items()}
        assert all(bip_color[u]!=bip_color[v] for u in C for v in adj[u])
        results.append((C,sphere,dist_counts))
    assert len(results)==2
    assert all(x[1]==collections.Counter({(5,(1,5,17,25,12)):54,(9,(1,9,27,21,2)):6}) for x in results)
    assert all(x[2]==collections.Counter({1:162,2:540,3:738,4:330}) for x in results)
    return results


def independent_quotient(states, adjacency):
    # Quotient named factorizations by the six orderings of three 1-factors.
    perms=list(itertools.permutations('012'))
    representative=lambda s:min(''.join(q[int(c)] for c in s) for q in perms)
    labels=sorted({representative(s) for s in states})
    group={s:labels.index(representative(s)) for s in states}
    assert len(labels)==20
    neighbors=[set() for _ in labels]
    for i,s in enumerate(states):
        for j in adjacency[i]:
            u,v=group[s],group[states[j]]
            if u!=v:neighbors[u].add(v)
    unseen=set(range(20));parts=[]
    while unseen:
        root=min(unseen);seen={root};q=[root];unseen.remove(root)
        for u in q:
            for v in neighbors[u]:
                if v not in seen:seen.add(v);unseen.remove(v);q.append(v)
        parts.append(sorted(seen))
    assert len(parts)==2
    for comp in parts:
        assert len(comp)==10
        hub=[u for u in comp if len(neighbors[u])==9]
        leaves=[u for u in comp if len(neighbors[u])==3]
        assert len(hub)==1 and len(leaves)==9
        assert neighbors[hub[0]]==set(leaves)
        leaf_components=[];left=set(leaves)
        while left:
            root=min(left);reach={root};q=[root];left.remove(root)
            for u in q:
                for v in neighbors[u]&set(leaves):
                    if v not in reach:reach.add(v);left.remove(v);q.append(v)
            leaf_components.append(reach)
        assert sorted(map(len,leaf_components))==[3,3,3]
        assert all(all(len(neighbors[v]&triangle)==2 for v in triangle) for triangle in leaf_components)
    return labels,[sorted(xs) for xs in neighbors],parts

def main():
    edges,around=incidence_graph()
    matches=perfect_matchings(edges,around)
    states=colorings_from_factorizations(edges,matches)
    adj=independent_graph(states,edges)
    classes=independent_metrics(states,adj)
    qlabels,qadj,qparts=independent_quotient(states,adj)
    assert sum(len(a) for a in adj)//2==324
    assert len(states)//6==20
    if len(sys.argv)==2:
        certificate=json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        assert edges==[tuple(e) for e in certificate['graph_edges_sorted']]
        assert states==certificate['named_colorings_in_sorted_edge_order']
        assert adj==certificate['kempe_adjacency_indices']
        assert sorted(C for C,_,_ in classes)==certificate['component_indices']
        assert qlabels==certificate['unlabelled_palette_orbit_representatives']
        assert qadj==certificate['unlabelled_quotient_adjacency']
        assert qparts==certificate['unlabelled_quotient_components']
    print('INCIDENCE_MATCHING_INDEPENDENT_PASS 9_3_blocks=9 matchings=42 colorings=120 factorizations=20')
    print('INCIDENCE_KEMPE_METRIC_PASS 2x60 components 324 edges radius=4 diameter=4 quotient=2xK1_join_3K3')

if __name__=='__main__':main()
