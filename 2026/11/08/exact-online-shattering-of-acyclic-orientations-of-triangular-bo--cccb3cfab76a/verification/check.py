"""Finite checks for acyclic-orientation online ranks of triangular books.

Uses only Python 3 standard library. For the unrestricted theorem, consult RESULT.md.
"""
from functools import lru_cache
from itertools import product


def rank_of_masks(concepts, number_of_queries):
    concepts = tuple(sorted(set(concepts)))
    one_bits = tuple(
        sum((1 << idx) for idx, value in enumerate(concepts) if (value >> j) & 1)
        for j in range(number_of_queries)
    )
    @lru_cache(None)
    def online_rank(pool):
        if pool & (pool-1) == 0:
            return 0
        highest = 0
        for ones in one_bits:
            yes = pool & ones
            no = pool & ~ones
            if yes and no:
                highest = max(highest, 1+min(online_rank(yes), online_rank(no)))
        return highest
    return online_rank((1 << len(concepts)) - 1)


def book_orientations(b):
    # A binary 1 represents an arc from an anchor to its page vertex.
    # Under spine orientation e=0, columns are 00,10,11; under e=1: 00,01,11.
    result = set()
    for e in (0,1):
        columns = ((0,0),(1,0),(1,1)) if e == 0 else ((0,0),(0,1),(1,1))
        for choices in product(columns,repeat=b):
            value = e << (2*b)
            for j,(x,y) in enumerate(choices):
                value |= x << (2*j)
                value |= y << (2*j+1)
            result.add(value)
    return result


def no_directed_cycle(mask,b):
    vertices=b+2
    edges=[(0,1)]+[(0,j+2) for j in range(b)]+[(1,j+2) for j in range(b)]
    outgoing=[[] for _ in range(vertices)]
    # Spine is the final bit; page edge bits are interleaved.
    for e,(x,y) in enumerate(edges):
        if e==0:
            bit=1-((mask>>(2*b))&1)
        elif e<=b:
            bit=(mask>>(2*(e-1)))&1
        else:
            bit=(mask>>(2*(e-b-1)+1))&1
        if bit:
            outgoing[x].append(y)
        else:
            outgoing[y].append(x)
    state=[0]*vertices
    def visit(v):
        if state[v]==1: return False
        if state[v]==2: return True
        state[v]=1
        for w in outgoing[v]:
            if not visit(w):return False
        state[v]=2
        return True
    return all(visit(v) for v in range(vertices) if not state[v])


def partially_queried_class(u,a,c):
    result=[]
    for spine in (0,1):
        full=((0,0),(1,0),(1,1)) if spine==0 else ((0,0),(0,1),(1,1))
        domains=[full for _ in range(u)]
        domains += [((0,),(1,)) if spine==0 else ((0,),) for _ in range(a)]
        domains += [((0,),(1,)) if spine==1 else ((0,),) for _ in range(c)]
        for choices in product(*domains):
            bits=0; position=0
            for item in choices:
                for digit in item:
                    bits |= digit<<position
                    position+=1
            bits |= spine<<position
            result.append(bits)
    return result,2*u+a+c+1


def formula(u,a,c):
    return max(u+a,u+c,1+(3*u+a+c)//2)


def forest_on_edges(selected,b):
    parent=list(range(b+2))
    def root(x):
        while x!=parent[x]:
            x=parent[x]
        return x
    edges=[(anchor,j+2) for j in range(b) for anchor in (0,1)]+[(0,1)]
    for k,(x,y) in enumerate(edges):
        if selected>>k&1:
            x,y=root(x),root(y)
            if x==y:return False
            parent[x]=y
    return True


def shattered_support(support, concepts, num_queries):
    selected=[j for j in range(num_queries) if support>>j&1]
    traces=set(sum(((v>>j)&1)<<i for i,j in enumerate(selected)) for v in concepts)
    return len(traces)==(1<<len(selected))


def main():
    for b in range(0,7):
        predicted=book_orientations(b)
        assert len(predicted)==2*3**b,(b,len(predicted))
        actual={mask for mask in range(1<<(2*b+1)) if no_directed_cycle(mask,b)}
        assert actual==predicted,('acyclic orientation mismatch',b)
        rank=rank_of_masks(actual,2*b+1)
        assert rank==formula(b,0,0),('online-rank mismatch',b,rank)
        if b<=4:
            for support in range(1<<(2*b+1)):
                assert shattered_support(support,actual,2*b+1)==forest_on_edges(support,b),('shattering',b,support)
    triples=0
    for total in range(0,7):
        for u in range(total+1):
            for a in range(total-u+1):
                c=total-u-a
                concepts,queries=partially_queried_class(u,a,c)
                if len(concepts)>3000:
                    continue
                observed=rank_of_masks(concepts,queries)
                assert observed==formula(u,a,c),(u,a,c,observed)
                triples+=1
    for u in range(0,40):
        for a in range(0,40):
            for c in range(0,40):
                f=formula(u,a,c)
                candidates=[1+min(u+a,u+c)]
                if u:
                    candidates.append(1+min(formula(u-1,a+1,c),formula(u-1,a,c+1)))
                if a:
                    candidates.append(1+min(u+a-1,formula(u,a-1,c)))
                if c:
                    candidates.append(1+min(u+c-1,formula(u,a,c-1)))
                assert f==max(candidates),(u,a,c,f,candidates)
    print('BOOK_ORIENTATION_ONLINE_PASS b=0..6 conditional_states='+str(triples)+' recurrence_triples=64000')


if __name__=='__main__':
    main()
