#!/usr/bin/env python3
"""Standalone exact small-order checks for the Latin-square autotopism character identity.
No external dependencies. Ordinary simplicial Lefschetz numbers use oriented fixed cliques.
"""
from itertools import combinations, permutations

def xor(a,b):return a^b

def make_group(name):
    if name.startswith('C'):
        n=int(name[1:]); A=list(range(n)); plus=lambda x,y:(x+y)%n
        units=[u for u in range(n) if __import__('math').gcd(u,n)==1]
        maps=[lambda x,u=u:(u*x)%n for u in units]
    elif name=='V4':
        n=4; A=list(range(n)); plus=xor
        maps=[]
        for a,b in ((a,b) for a in (1,2,3) for b in (1,2,3) if a!=b):
            maps.append(lambda x,a=a,b=b: (a if x&1 else 0)^(b if x&2 else 0))
    else:raise ValueError(name)
    return A,plus,maps

def list_cliques(N, adj):
    out=[]
    def rec(sub, options):
        if sub:out.append(sub)
        while options:
            bit=options&-options;options^=bit;v=bit.bit_length()-1
            rec(sub|bit, options&adj[v])
    rec(0,(1<<N)-1)
    return out

def sign(v):
    return -1 if sum(x>y for i,x in enumerate(v) for y in v[i+1:])%2 else 1

def run(name):
    A,plus,maps=make_group(name);n=len(A)
    cells=[(r,c) for r in A for c in A];idx={v:i for i,v in enumerate(cells)}
    symbol={(r,c):plus(r,c) for r,c in cells}
    N=n*n
    adj=[sum(1<<j for j,(rr,cc) in enumerate(cells)
             if i!=j and (rr==r or cc==c or symbol[(rr,cc)]==symbol[(r,c)]))
         for i,(r,c) in enumerate(cells)]
    cliques=list_cliques(N,adj)
    faces=[([i for i in range(N) if mask>>i&1], mask.bit_count()) for mask in cliques]
    inter=[]
    for rs in combinations(A,2):
        for cs in combinations(A,2):
            r1,r2=rs;c1,c2=cs
            if plus(r1,c1)==plus(r2,c2) and plus(r1,c2)==plus(r2,c1):
                inter.append((rs,cs))
    unique_rainbow={}
    for rs,cs in inter:
        vv=[idx[(r,c)] for r in rs for c in cs]
        for tri in combinations(vv,3):
            # Every boundary triangle of an intercalate is rainbow, unique to it
            types=[]
            for i,j in combinations(tri,2):
                x,y=cells[i],cells[j]
                typ=(x[0]==y[0],x[1]==y[1],symbol[x]==symbol[y])
                assert sum(typ)==1
                types.append(typ)
            assert len(set(types))==3
            assert tri not in unique_rainbow
            unique_rainbow[tri]=(rs,cs)
    checks=0
    for linear in maps:
        for a in A:
            for b in A:
                rr={r:plus(linear(r),a) for r in A}
                cc={c:plus(linear(c),b) for c in A}
                ss={s:plus(linear(s),plus(a,b)) for s in A}
                perm=[idx[(rr[r],cc[c])] for r,c in cells]
                signed_sum=0
                for inds,size in faces:
                    moved=[perm[i] for i in inds]
                    if set(moved)==set(inds):
                        signed_sum+=((-1)**(size-1))*sign(moved)
                actual=signed_sum-1
                nfix=lambda m:sum(m[x]==x for x in A)
                base=(nfix(rr)-1)*(nfix(cc)-1)*(nfix(ss)-1)
                ifix=sum({rr[r] for r in rs}==set(rs) and {cc[c] for c in cs}==set(cs)
                          for rs,cs in inter)
                predicted=base-ifix
                assert actual==predicted, (name,a,b,actual,predicted)
                checks+=1
    assert sum(1 for rs,cs in inter)==len(inter)
    return name,n,len(cliques),len(inter),len(unique_rainbow),checks

def nongroup_order_five():
    # A reduced order-five Latin square with four genuine intercalates.
    M=((0,1,2,3,4),(1,0,3,4,2),(2,3,4,0,1),
       (3,4,1,2,0),(4,2,0,1,3))
    n=5;cells=[(r,c) for r in range(n) for c in range(n)]
    adj=[sum(1<<j for j,(rr,cc) in enumerate(cells)
             if i!=j and (r==rr or c==cc or M[r][c]==M[rr][cc]))
         for i,(r,c) in enumerate(cells)]
    cliques=list_cliques(n*n,adj)
    by_dim={d:[] for d in range(5)}
    for v in cliques:by_dim[v.bit_count()-1].append(v)
    assert len(by_dim[4])==3*n
    def rank(cols):
        pivots={}
        for column in cols:
            v=column
            while v:
                key=v.bit_length()-1
                if key in pivots:v^=pivots[key]
                else:pivots[key]=v;break
        return len(pivots)
    bd={0:0}
    for d in (1,2,3,4):
        ix={f:i for i,f in enumerate(by_dim[d-1])}
        bd[d]=rank([sum(1<<ix[f^(1<<v)] for v in range(n*n) if f>>v&1)
                    for f in by_dim[d]])
    inter=[]
    for r1,r2 in combinations(range(n),2):
        for c1,c2 in combinations(range(n),2):
            if M[r1][c1]==M[r2][c2] and M[r1][c2]==M[r2][c1]:
                inter.append((frozenset((r1,r2)),frozenset((c1,c2))))
    assert len(inter)==4
    betti2=len(by_dim[2])-bd[2]-bd[3]
    assert betti2==(n-1)**3-len(inter)==60
    assert len(by_dim[1])-bd[1]-bd[2]==0
    assert len(by_dim[3])-bd[3]-bd[4]==0
    assert len(by_dim[4])-bd[4]==0
    face_vertices=[[i for i in range(n*n) if mask>>i&1] for mask in cliques]
    checks=0
    for rr in permutations(range(n)):
        for cc in permutations(range(n)):
            ss={M[0][c]:M[rr[0]][cc[c]] for c in range(n)}
            if len(set(ss.values()))!=n:continue
            if not all(M[rr[r]][cc[c]]==ss[M[r][c]] for r,c in cells):continue
            perm=[rr[r]*n+cc[c] for r,c in cells]
            L=0
            for inds in face_vertices:
                image=[perm[i] for i in inds]
                if set(image)==set(inds):L+=(-1)**(len(inds)-1)*sign(image)
            fixed=lambda p:sum(i==p[i] for i in range(n))
            ifix=sum({rr[r] for r in rs}==set(rs) and {cc[c] for c in cs}==set(cs)
                     for rs,cs in inter)
            pred=(fixed(rr)-1)*(fixed(cc)-1)*(sum(i==ss[i] for i in range(n))-1)-ifix
            assert L-1==pred,(rr,cc,L-1,pred)
            checks+=1
    assert checks>1
    print(f'non-group order-five: nonempty_cliques={len(cliques)}, intercalates={len(inter)}, mod2_betti2={betti2}, autotopisms_checked={checks}, all_traces=PASS')

if __name__=='__main__':
    for name in ('C4','V4','C5','C6'):
        label,n,faces,inter,unique,checks=run(name)
        print(f'{label}: order={n}, nonempty_cliques={faces}, intercalates={inter}, distinct_rainbow_facets={unique}, autotopisms_checked={checks}, all_traces=PASS')
    nongroup_order_five()
    print('All exact small-order checks passed.')
