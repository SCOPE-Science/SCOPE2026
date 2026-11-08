"""Independent finite checks of subgroup fixed loci for cyclic scale-two Rips strips."""
from itertools import combinations

def faces(n):
    result=set()
    for k in (1,2,3):
        for tup in combinations(range(n), k):
            if all(min((u-v)%n, (v-u)%n)<=2 for u,v in combinations(tup,2)):
                result.add(frozenset(tup))
    return result

def components_of_reflection(n, a, allfaces):
    fixed={s for s in allfaces if frozenset((a-v)%n for v in s)==s}
    parent={s:s for s in fixed}
    def find(x):
        while parent[x]!=x:
            x=parent[x]
        return x
    for u in fixed:
        for v in fixed:
            if u<v: parent[find(u)]=find(v)
    counts={}
    for u in fixed:
        root=find(u)
        counts[root]=counts.get(root,0)+1
    return len(counts), sorted(counts.values())

def run():
    checked=0
    for n in range(7,31):
        F=faces(n)
        assert len([x for x in F if len(x)==3])==n
        assert len([x for x in F if len(x)==2])==2*n
        assert len([x for x in F if len(x)==1])==n
        boundary=[x for x in F if len(x)==2 and sum(x<t for t in F if len(t)==3)==1]
        assert len(boundary)==n
        for step in range(1,n):
            assert not any(frozenset((v+step)%n for v in face)==face for face in F), (n,step)
            checked+=1
        for a in range(n):
            nc, sizes=components_of_reflection(n,a,F)
            assert nc==2, (n,a,sizes)
            assert sizes==([1,3] if n%2 else ([3,3] if a%2==0 else [1,1])), (n,a,sizes)
            checked+=1
    print('CHECKED',checked,'nonidentity rotations and reflections on n=7,...,30')
    print('ALL_VERIFY_OK')

if __name__=='__main__':run()
