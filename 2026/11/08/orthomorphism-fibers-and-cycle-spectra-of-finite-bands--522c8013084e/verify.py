"""Direct finite-semigroup checks for orthomorphism fiber and cycle-index theorem.
Usage: python verify.py
No third-party packages are required.
"""
from itertools import permutations, product
from collections import Counter, defaultdict
from math import factorial

def table_rect(a,b):
    elements=list(product(range(a),range(b)))
    loc={v:i for i,v in enumerate(elements)}
    table=[[loc[(x[0],y[1])] for y in elements] for x in elements]
    dblocks=[(list(range(a*b)),a,b)]
    rblocks=[[loc[(i,j)] for j in range(b)] for i in range(a)]
    return table,dblocks,rblocks

def table_two_levels(a,b):
    # Semilattice product of a rectangular band with the 2-element meet semilattice.
    elements=list(product(range(a),range(b),range(2)))
    loc={v:i for i,v in enumerate(elements)}
    table=[[loc[(x[0],y[1],min(x[2],y[2]))] for y in elements] for x in elements]
    dblocks=[]; rblocks=[]
    for h in range(2):
        dblocks.append(([loc[(i,j,h)] for i in range(a) for j in range(b)],a,b))
        rblocks += [[loc[(i,j,h)] for j in range(b)] for i in range(a)]
    return table,dblocks,rblocks

def table_glued():
    # A nontrivial two-level semilattice of rectangular bands:
    # top = left-zero band of two elements, bottom = 2x2 rectangular band;
    # top-to-bottom connecting homomorphism t_i |-> (i,0).
    elements=[('t',i) for i in range(2)]+[('b',i,j) for i in range(2) for j in range(2)]
    ix={x:i for i,x in enumerate(elements)}
    def mul(x,y):
        xx=('b',x[1],0) if x[0]=='t' and y[0]=='b' else x
        yy=('b',y[1],0) if y[0]=='t' and x[0]=='b' else y
        if xx[0]==yy[0]=='t':return xx
        return ('b',xx[1], yy[2])
    table=[[ix[mul(x,y)] for y in elements] for x in elements]
    return table,[([0,1],2,1),([2,3,4,5],2,2)],[[0],[1],[2,3],[4,5]]

def table_free_left_regular_band():
    # Ordered words without repeated letters, multiplied by first occurrence.
    words=['', 'a', 'b', 'ab', 'ba']
    ix={w:i for i,w in enumerate(words)}
    def mul(u,v):
        ans=list(u)
        for c in v:
            if c not in ans:ans.append(c)
        return ''.join(ans)
    table=[[ix[mul(x,y)] for y in words] for x in words]
    return table,[([0],1,1),([1],1,1),([2],1,1),([3,4],2,1)],[[i] for i in range(5)]

def cycl(p):
    vis=set();out=Counter()
    for i in range(len(p)):
        if i in vis:continue
        j=i; size=0
        while j not in vis:
            vis.add(j);size+=1;j=p[j]
        out[size]+=1
    return tuple(sorted(out.items()))

def verify(table,dblocks,rblocks,name):
    n=len(table)
    assert all(table[x][x]==x for x in range(n))
    assert all(table[table[x][y]][z]==table[x][table[y][z]] for x in range(n) for y in range(n) for z in range(n))
    all_results=Counter(); fibers=Counter(); good=0
    for p in permutations(range(n)):
        theta=tuple(table[x][p[x]] for x in range(n))
        if len(set(theta))!=n:continue
        good+=1;fibers[theta]+=1;all_results[cycl(theta)]+=1
    dcm=1
    for block,a,b in dblocks:dcm*=factorial(a)**b * factorial(b)**a
    image=set()
    group_expected=1
    for rb in rblocks:group_expected*=factorial(len(rb))
    for rb_perms in product(*(permutations(rb) for rb in rblocks)):
        t=list(range(n))
        for rb,p in zip(rblocks,rb_perms):
            for src,dst in zip(rb,p):t[src]=dst
        image.add(tuple(t))
    assert len(image)==group_expected
    fiber_expected=dcm//group_expected
    assert good==dcm,(name,good,dcm)
    assert set(fibers)==image,(name,'image')
    assert set(fibers.values())=={fiber_expected},(name,'fibers',fibers)
    cycle_expected=Counter(cycl(p) for p in image)
    assert all_results==Counter({k:v*fiber_expected for k,v in cycle_expected.items()})
    print(f'{name}: n={n}; permutations={factorial(n)}; complete_mappings={good}; orthomorphisms={len(image)}; constant_fiber={fiber_expected}; cycle_types={len(all_results)} PASS')

if __name__=='__main__':
    verify(*table_rect(2,2),'rectangular_2x2')
    verify(*table_rect(3,2),'rectangular_3x2')
    verify(*table_two_levels(2,2),'two_levels_2x2')
    verify(*table_glued(),'glued_nonuniform_levels')
    verify(*table_rect(1,4),'right_zero_4')
    verify(*table_rect(4,1),'left_zero_4')
    verify(*table_free_left_regular_band(),'free_left_regular_band_2')
    print('VERIFY_OK cases=7 exhaustive_permutations=41952')
