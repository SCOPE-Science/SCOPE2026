"""Independent finite enumeration and explicit witness verification for 2x2 rectangles."""
from itertools import combinations
from functools import lru_cache

def concepts(m,n):
    return tuple(sum(1 << (r*n+c) for r in rows for c in cols)
                 for rows in combinations(range(m),2)
                 for cols in combinations(range(n),2))

def vc(C,N):
    maximum=0
    for k in range(1,4):
        exists=any(len({tuple((x>>a)&1 for a in S) for x in C})==(1<<k)
                   for S in combinations(range(N),k))
        if not exists: break
        maximum=k
    return maximum

def ld(C,N):
    @lru_cache(None)
    def f(S):
        if len(S)<2:return 0
        best=0
        for q in range(N):
            yes=tuple(x for x in S if (x>>q)&1)
            no=tuple(x for x in S if not ((x>>q)&1))
            if yes and no:
                best=max(best,1+min(f(yes),f(no)))
        return best
    return f(tuple(C))

TREE={'query':[1,1],'zero':{'query':[1,2],'zero':{'query':[2,1],'zero':{'witness':432},'one':{'witness':216}},'one':{'query':[2,2],'zero':{'witness':390},'one':{'witness':54}}},'one':{'query':[1,2],'zero':{'query':[2,1],'zero':{'witness':325},'one':{'witness':45}},'one':{'query':[2,1],'zero':{'witness':195},'one':{'witness':27}}}}

def verify_tree(t,C,m,n,trace=()):
    if 'witness' in t:
        assert t['witness'] in C
        assert all((t['witness']>>(r*n+c))&1==bit for r,c,bit in trace)
        return (0,1)
    r,c=(u-1 for u in t['query'])
    assert all((rr,cc)!=(r,c) for rr,cc,_ in trace)
    a,b=verify_tree(t['zero'],C,m,n,trace+((r,c,0),)),verify_tree(t['one'],C,m,n,trace+((r,c,1),))
    assert a[0]==b[0]
    return (a[0]+1,a[1]+b[1])

def main():
    expected={(2,2):(0,0),(2,3):(1,1),(2,4):(2,2),(2,5):(2,2),(3,3):(2,3),(3,4):(2,3)}
    for (m,n),(v,l) in expected.items():
        C=concepts(m,n)
        assert len(C)==(m*(m-1)//2)*(n*(n-1)//2)
        assert vc(C,m*n)==v and ld(C,m*n)==l,(m,n)
        print('PASS',m,n,'concepts',len(C),'VC',v,'Ldim',l)
    assert verify_tree(TREE,concepts(3,3),3,3)==(3,8)
    assert len({x['witness'] for x in collect_leaves(TREE)})==8
    print('FULL_DEPTH_3_CERTIFICATE_PASS',8)
    print('ALL_FIXED_RECTANGLE_CHECKS_PASS')

def collect_leaves(t):
    if 'witness' in t:return [t]
    return collect_leaves(t['zero'])+collect_leaves(t['one'])

if __name__=='__main__':main()
