#!/usr/bin/env python3
"""Exhaustive independent finite G-set nilpotence checks.
Run: python3 check_nilpotent.py
"""
from itertools import permutations,product
from math import prod

def group_symmetric(n):
    E=tuple(range(n))
    G=list(permutations(range(n)))
    def mul(p,q):return tuple(p[q[i]] for i in range(n))
    return G,E,mul

def group_cyclic(n):
    G=list(range(n));return G,0,lambda x,y:(x+y)%n

def make_example(G,E,mul,types):
    # types=[(subgroup, copies)] where subgroup is a set of group elements
    cosetlist=[]; coset_action=[]; orbit_types=[]
    for H,copies in types:
        seen=set();cosets=[]
        for g in G:
            c=frozenset(mul(g,h) for h in H)
            if c not in seen:
                cosets.append(c);seen.add(c)
        assert len(cosets)*len(H)==len(G)
        for k in range(copies):
            offset=sum(len(c) for c in cosetlist)
            cosetlist.append(cosets)
            act={}
            for g in G:
                act[g]=[cosets.index(frozenset(mul(g,z) for z in coset)) for coset in cosets]
            coset_action.append(act)
            orbit_types.append(H)
    sizes=[len(c) for c in cosetlist]
    offsets=[];s=1
    for sz in sizes:offsets.append(s);s+=sz
    def global_action(g,j):
        if j==0:return 0
        for oi,off in enumerate(offsets):
            if off<=j<off+sizes[oi]:return off+coset_action[oi][g][j-off]
        raise AssertionError
    # for orbit o, each destination fixed by H gives one equivariant restriction
    images=[]
    for oi,H in enumerate(orbit_types):
        rep=offsets[oi]
        opts=[]
        for target in range(s):
            if any(global_action(h,target)!=target for h in H):continue
            im=[]
            for c in cosetlist[oi]:
                g=next(x for x in G if frozenset(mul(x,h) for h in H)==c)
                im.append(global_action(g,target))
            opts.append(tuple(im))
        assert len(set(opts))==len(opts)
        images.append(opts)
    count=0
    for choices in product(*images):
        f=[0]
        for ch in choices:f.extend(ch)
        assert len(f)==s
        # Test actual iterates of points, not orbit-graph cycle oracle
        is_nil=all((lambda a: a==0)(iterate(f,x,s)) for x in range(s))
        count+=is_nil
    # Independent computation of h_{ij} from actual fixed target points
    typelist=[]; multiplicities=[]
    for H,_ in types:
        typelist.append(H)
    for H,m in types:
        multiplicities.append(m)
    factors=[]
    for i,(H,m) in enumerate(types):
        if m==0:continue
        own=sum(all(global_action(h,t)==t for h in H) for t in range(offsets[sum(z[1] for z in types[:i])], offsets[sum(z[1] for z in types[:i])]+sizes[sum(z[1] for z in types[:i])]))
        R=1
        for j,(K,mm) in enumerate(types):
            if i==j or mm==0:continue
            idx=sum(z[1] for z in types[:j]);off=offsets[idx]
            hj=sum(all(global_action(h,t)==t for h in H) for t in range(off,off+sizes[idx]))
            R+=mm*hj
        factors.append(R*(R+m*own)**(m-1))
    formula=prod(factors)
    assert count==formula,(count,formula)
    print('EXHAUSTIVE_PASS', 'group_order',len(G),'orbit_types',[(len(h),m) for h,m in types], 'points',s,'choices',prod(map(len,images)),'nilpotents',count, 'product',formula)
    return count

def iterate(f,x,k):
    for _ in range(k):x=f[x]
    return x

def main():
    for order in (2,3,4):
        G,E,mul=group_cyclic(order)
        H0={E};HG=set(G)
        for a,b in [(1,1),(2,1),(2,2),(3,0)]:
            make_example(G,E,mul,[(H0,a),(HG,b)])
    G,E,mul=group_symmetric(3)
    a=(1,0,2); b=(1,2,0)
    H0={E};H2={E,a}; H3={E,b,mul(b,b)}; HG=set(G)
    assert len(H3)==3
    for a0,b0,c0,d0 in [(1,1,1,1),(2,1,1,1),(1,2,1,1),(1,1,0,2)]:
        make_example(G,E,mul,[(H0,a0),(H2,b0),(H3,c0),(HG,d0)])
    # Reconstruct all S_3 table-of-marks entries from two-orbit probes.
    subgroups=[H0,H2,H3,HG]
    orbit_sizes=[len(G)//len(H) for H in subgroups]
    matrix=[]
    for i,H in enumerate(subgroups):
        row=[]
        for j,K in enumerate(subgroups):
            if i==j:
                nu=make_example(G,E,mul,[(H,2)])
                hij=(nu-1)//2
                assert 1+2*hij==nu
            else:
                nu=make_example(G,E,mul,[(H,1),(K,1)])
                hij=nu-1 if orbit_sizes[i]>orbit_sizes[j] else 0
            row.append(hij)
        matrix.append(row)
    expected=[[6,3,2,1],[0,1,0,1],[0,0,2,1],[0,0,0,1]]
    assert matrix==expected,(matrix,expected)
    print('INVERSE_MARKS_S3_PASSED',matrix)
    # Same-size but nonisomorphic V_4 orbits admit no maps.
    V,E,add=(list(product(range(2),repeat=2)),(0,0),lambda a,b:((a[0]+b[0])%2,(a[1]+b[1])%2))
    Ha={E,(1,0)};Hb={E,(0,1)}
    assert make_example(V,E,add,[(Ha,1),(Hb,1)])==1
    print('SAME_ORDER_DISTINCT_TYPE_V4_PASSED')
    print('POINTED_G_SET_NILPOTENCE_CHECKS_PASSED')

if __name__=='__main__':main()
