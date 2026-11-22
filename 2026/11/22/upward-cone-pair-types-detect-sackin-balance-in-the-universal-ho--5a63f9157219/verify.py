"""Standalone finite-diagram check for binary semilinear-order marked antichains.
Constructs discrete edge-subdivision witnesses and compares full (<,C) diagrams.
"""
from functools import lru_cache
from itertools import permutations

@lru_cache(None)
def shapes(n):
    if n == 1: return (0,)
    out = {}
    for a in range(1, n):
        b=n-a
        if a>b: continue
        for A in shapes(a):
            for B in shapes(b):
                s=tuple(sorted((A, B), key=repr))
                out[repr(s)]=s
    return tuple(out.values())

def make_nodes(shape):
    parent={}; leaves=[]; depths={}
    def rec(sh, p, depth):
        k=len(parent); parent[k]=p; depths[k]=depth
        if isinstance(sh, int): leaves.append(k)
        else:
            rec(sh[0], k,depth+1);rec(sh[1], k,depth+1)
        return k
    root=rec(shape,None,0)
    return parent,tuple(leaves),depths,root

def realize(parent, leaves, root, e1,e2, first_lower):
    pa=parent.copy()
    top=max(pa)+1;x=top+1;y=top+2
    pa[top]=None;pa[root]=top
    if e1!=e2:
        for edge, point in [(e1,x),(e2,y)]:
            pa[point]=pa[edge];pa[edge]=point
    else:
        edge=e1;old_parent=pa[edge]
        lower,upper=(x,y) if first_lower else (y,x)
        pa[edge]=lower;pa[lower]=upper;pa[upper]=old_parent
    return pa,x,y

def above(pa, u, v):
    """Whether u is strict ancestor of v."""
    cur=pa[v]
    while cur is not None:
        if cur==u:return True
        cur=pa[cur]
    return False

def lca(pa,u,v):
    aset=set();cur=u
    while cur is not None:
        aset.add(cur);cur=pa[cur]
    cur=v
    while cur not in aset: cur=pa[cur]
    return cur

def signature(pa, leaves,x,y):
    labs=leaves+(x,y)
    less=lambda u,v: above(pa,v,u)
    def C(z,a,b):
        if less(a,b) or less(b,a): return False
        p=lca(pa,a,b)
        return not (p==z or above(pa,p,z) or above(pa,z,p))
    return tuple(int(less(a,b)) for a,b in permutations(labs,2))+tuple(int(C(c,a,b)) for a,b,c in permutations(labs,3))

def test(shape):
    pa,leaves,depths,root=make_nodes(shape)
    n=len(leaves);m=2*n-1
    unique={};channels={'<':set(),'>':set(),'perp':set()}
    for e1 in pa:
        for e2 in pa:
            for lower in ((True,False) if e1==e2 else (True,)):
                ext,x,y=realize(pa,leaves,root,e1,e2,lower)
                sig=signature(ext,leaves,x,y)
                relation='<' if above(ext,y,x) else '>' if above(ext,x,y) else 'perp'
                unique[sig]=relation
                channels[relation].add(sig)
    L=sum(depths[i] for i in leaves)
    predicted=2*L+1
    actual=tuple(len(channels[r]) for r in ('<','>','perp'))
    want=(predicted,predicted,2*n*(2*n-1)-2*predicted)
    assert actual==want, (shape,actual,want)
    assert len(unique)==2*n*(2*n-1), (shape,len(unique))
    return n,L,actual

def main():
    count=0
    for n in range(1,9):
        mn=10**9;mx=-1;forms=0
        for sh in shapes(n):
            res=test(sh);count+=1;forms+=1
            mn=min(mn,res[1]);mx=max(mx,res[1])
        h=n.bit_length()-1
        expected_min=n*h+2*(n-2**h)
        expected_max=n*(n+1)//2-1
        assert (mn,mx)==(expected_min,expected_max),(n,mn,mx,expected_min,expected_max)
        print('n',n,'shapes',forms,'Sackin range',mn,mx,'< type range',2*mn+1,2*mx+1)
    print('PASS: full (<, C) signature enumeration,',count,'unlabelled binary shapes')
if __name__=='__main__':main()
