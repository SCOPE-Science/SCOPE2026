"""Independent finite proof of the first prism perfect-matching adaptive gap.
Only standard-library Python. Run beside prism6_certificate.json.
"""
from itertools import combinations
import json
from functools import lru_cache
from pathlib import Path

def make_graph(n):
    edges = [(2*i,2*i+1) for i in range(n)]
    for i in range(n):
        j=(i+1)%n
        for row in (0,1):
            edges.append((2*i+row,2*j+row))
    assert len(edges)==3*n and len(set(tuple(sorted(e)) for e in edges))==3*n
    return edges

def perfect_matchings(n, edges):
    # Independent of the usual tiling decomposition: inspect every n-edge set.
    all_m=[]
    for es in combinations(range(3*n),n):
        # Degree vector counts, not tiling recurrence or dynamic programming.
        degrees=[0]*(2*n)
        for e in es:
            u,v=edges[e]; degrees[u]+=1;degrees[v]+=1
        if all(d==1 for d in degrees):
            all_m.append(sum(1<<e for e in es))
    return all_m

def shattering_counts(n,edges,matchings):
    ans=[]
    for k in range(5):
        good=0
        for S in combinations(range(3*n),k):
            signatures=set()
            for m in matchings:
                signatures.add(sum(((m>>e)&1)<<i for i,e in enumerate(S)))
            if len(signatures)==2**k:
                good+=1
        ans.append(good)
    return ans

def full_version_space_littlestone(matchings, edges):
    """Exact minimax of all legal edge-query splits on every concept subset."""
    full=(1<<len(matchings))-1
    cuts=[sum(1<<i for i,m in enumerate(matchings) if (m>>e)&1)
          for e in range(len(edges))]
    @lru_cache(None)
    def depth(s):
        best=0
        for p in cuts:
            a=s&p
            b=s^a
            if a and b:
                best=max(best,1+min(depth(a),depth(b)))
        return best
    return depth(full)

def verify_tree(tree,matchings,edges):
    leaves=[]
    def visit(node, survivors, depth):
        if not depth:
            assert set(node)=={'matching_index'}
            j=node['matching_index']
            assert j in survivors
            leaves.append(j)
            return
        assert set(node)=={'edge_index','absent','present'}
        e=node['edge_index']
        assert 0<=e<len(edges)
        left=[j for j in survivors if not (matchings[j]>>e)&1]
        right=[j for j in survivors if (matchings[j]>>e)&1]
        assert left and right
        visit(node['absent'],left,depth-1)
        visit(node['present'],right,depth-1)
    visit(tree,list(range(len(matchings))),4)
    assert len(leaves)==16 and len(set(leaves))==16
    return len(leaves)

def main():
    c=json.loads(Path('prism6_certificate.json').read_text('utf-8'))
    assert c['n']==6 and c['littlestone_dimension']==4
    measurements={}
    for n in range(3,7):
        edges=make_graph(n)
        ms=perfect_matchings(n,edges)
        faces=shattering_counts(n,edges,ms)
        adaptive=full_version_space_littlestone(ms,edges)
        measurements[n]=(len(ms),faces,adaptive)
    assert measurements=={
        3:(4,[1,9,3,0,0],2),
        4:(9,[1,12,42,0,0],2),
        5:(11,[1,15,60,5,0],3),
        6:(20,[1,18,117,138,0],4),
    },measurements
    # The archived certificate uses rung-first, each horizontal layer separately.
    assert make_graph(6)==[tuple(x) for x in c['vertices']]
    six=perfect_matchings(6,make_graph(6))
    assert set(six)==set(c['matchings']) and len(six)==20
    # The certificate specifies an explicit bijective concept-index mapping.
    witness=verify_tree(c['tree'],c['matchings'],c['vertices'])
    assert c['face_counts_through_4']==measurements[6][1]
    # No 5-query support can be shattered: 20 hypotheses < 32 traces.
    # No 4-query support is shattered by the exhaustive 3060-support census.
    # The explicit tree realizes all 16 adaptive paths.
    print('HEXAGONAL_PRISM_ADAPTIVE_GAP_PASS finite_orders=3..6 matchings_6=20 '+
          'support_quadruples_6=3060 tree_leaves=16 vc6=3 littlestone6=4')
if __name__=='__main__':main()
