from itertools import permutations,product

def group(kind):
    if kind.startswith('C'):
        d=int(kind[1:]); elems=list(range(d)); mul=lambda a,b:(a+b)%d
    elif kind=='S3':
        elems=list(permutations(range(3)))
        def mul(a,b): return tuple(a[b[i]] for i in range(3))
    elif kind=='D8':
        elems=list(product(range(4),range(2)))
        def mul(a,b):return ((a[0]+(-1)**a[1]*b[0])%4,(a[1]+b[1])%2)
    else:raise ValueError(kind)
    unit=next(a for a in elems if all(mul(a,b)==b and mul(b,a)==b for b in elems))
    return elems,mul,unit

def check(kind,P):
    G,mul,u=group(kind);nr=len(P);nc=len(P[0]);assert all(any(x>=0 for x in row) for row in P) and all(any(P[r][c]>=0 for r in range(nr)) for c in range(nc));
    # rows are Lambda, columns I. A nonzero entry is group index, -1 means zero
    g0=G[0];gs={v:i for i,v in enumerate(G)}; gg=[G[i] for i in range(len(G))];mt=[[gs[mul(a,b)] for b in G] for a in G]
    nG=len(G);zero=0;el=[None]+[(i,a,j) for i in range(nc) for a in range(nG) for j in range(nr)]
    idx={v:i for i,v in enumerate(el)}; N=len(el); one=N
    def prod(x,y):
        if x==one:return y
        if y==one:return x
        if x==0 or y==0:return 0
        i,a,j=el[x];k,b,l=el[y]
        if P[j][k]<0:return 0
        return idx[(i,mt[mt[a][P[j][k]]][b],l)]
    mult=[[prod(x,y) for y in range(N+1)] for x in range(N+1)]
    # Check associativity for sampled complete table
    for a,b,c in product(range(N+1),repeat=3):
        assert mult[mult[a][b]][c]==mult[a][mult[b][c]]
    gen=set()
    for g in range(N+1):
        for h in range(N+1):
            gh=mult[g][h]
            dom=[x for x in range(N) if mult[gh][x]==x and mult[x][gh]==x]
            M=tuple((x,mult[mult[h][x]][g]) for x in dom)
            assert len(set(y for _,y in M))==len(M)
            gen.add(M)
    # Predicted generators include full identity; maps between regular H-classes and zero map.
    Z=next(t for t in gen if t==((0,0),))
    identity=tuple((x,x) for x in range(N));assert identity in gen
    reg=[(i,j) for i in range(nc) for j in range(nr) if P[j][i]>=0]
    center=[a for a in G if all(mul(a,b)==mul(b,a) for b in G)]
    inn_size=nG//len(center);m=len(reg)
    expected= m*m*inn_size+1+(m!=1)
    print(kind, 'shape',nr,nc, 'nonzero-entries',m, 'group-order',nG,'center',len(center),'expected',expected,'generators',len(gen))
    assert len(gen)==expected,(kind,P, len(gen),expected)
    for M in gen:
        if M==identity or M==Z: continue
        dom={x for x,y in M};ran={y for x,y in M};assert len(dom)==nG+1 and len(ran)==nG+1 and 0 in dom and 0 in ran
        assert len({(el[x][0],el[x][2]) for x in dom if x})==1
        assert len({(el[y][0],el[y][2]) for y in ran if y})==1
    # Directly check closure and expected group of blocks
    for A,B in product(gen,repeat=2):
        dB=dict(B);C=tuple((x,dB[y]) for x,y in A if y in dB)
        assert C in gen,('not closed',A,B,C)
    return len(gen)

if __name__=='__main__':
    tests=[('C1',[[0]]),('C2',[[0]]),('C1',[[0,0],[0,-1]]),('C2',[[0,0],[0,-1]]),('C3',[[0,-1],[0,0]]),('S3',[[0,-1],[0,0]]),('S3',[[2,-1],[4,1]]),('D8',[[0,-1],[1,3]]),('C1',[[0,0,0],[0,-1,-1],[-1,0,0]]),('C1',[[0,0,-1],[0,-1,0],[-1,0,-1]]),('C1',[[0,0,0],[-1,0,-1],[-1,-1,0]]),('C2',[[0],[1]]),('S3',[[0,1],[2,3]])]
    for name,p in tests:check(name,p)
    print('VERIFY_OK')
