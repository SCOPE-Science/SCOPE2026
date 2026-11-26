"""Reproducible finite checks for the complete bipartite two-point homology character."""
from itertools import combinations, permutations, product
from math import comb

P=1000003

def cpairs(xs): return list(combinations(xs,2))

def setup(m,n):
    vertices=tuple(range(m+n))
    edges=tuple((i,j) for i in range(m) for j in range(n))
    endpoints=lambda e:(e[0],m+e[1])
    c0=cpairs(vertices)
    c1=[(v,e) for e in edges for v in vertices if v not in endpoints(e)]
    c2=[(e,f) for e,f in combinations(edges,2) if set(endpoints(e)).isdisjoint(endpoints(f))]
    d0={v:i for i,v in enumerate(c0)}
    d1={e:i for i,e in enumerate(c1)}
    d2={e:i for i,e in enumerate(c2)}
    def bc1(c):
        v,e=c;a,b=endpoints(e)
        return [(d0[tuple(sorted((v,b)))],1),(d0[tuple(sorted((v,a)))],-1)]
    def bc2(c):
        e,f=c; a,b=endpoints(e);c,d=endpoints(f)
        return [(d1[(b,f)],1),(d1[(a,f)],-1),(d1[(d,e)],-1),(d1[(c,e)],1)]
    return vertices,edges,c0,c1,c2,bc1,bc2

def rank_mod(columns):
    pivots={}
    for column in columns:
        v={}
        for i,c in column:v[i]=(v.get(i,0)+c)%P
        v={i:c for i,c in v.items() if c}
        while v:
            i=min(v)
            if i not in pivots:
                inv=pow(v[i],P-2,P)
                pivots[i]={j:c*inv%P for j,c in v.items()}
                break
            fac=v[i];p=pivots[i]
            for j,c in p.items():
                nxt=(v.get(j,0)-fac*c)%P
                if nxt:v[j]=nxt
                else:v.pop(j,None)
    return len(pivots)

def cyc(p):
    seen=set();f=t=0
    for i in range(len(p)):
        if i not in seen:
            length=0;j=i
            while j not in seen:seen.add(j);j=p[j];length+=1
            f+=(length==1);t+=(length==2)
    return f,t

def chars(p):
    f,t=cyc(p)
    return comb(f,2)+t-f, comb(f,2)-t-f+1

def action(m,n,p,q,swap=False):
    if not swap:
        return lambda v:p[v] if v<m else m+q[v-m], lambda e:(p[e[0]],q[e[1]]),1
    # Balanced side swap maps L_i to R_{p(i)} and R_j to L_{q(j)}.
    assert m==n
    return lambda v:m+p[v] if v<m else q[v-m], lambda e:(q[e[1]],p[e[0]]),-1

def cellular_traces(m,n,C,p,q,swap=False):
    verts,edges,c0,c1,c2,*_=C
    vp,ep,orientation=action(m,n,p,q,swap)
    z0=sum(tuple(sorted((vp(a),vp(b))))==(a,b) for a,b in c0)
    z1=sum(orientation for v,e in c1 if vp(v)==v and ep(e)==e)
    z2=0
    for e,f in c2:
        a,b=ep(e),ep(f)
        if {a,b}=={e,f}:
            z2+=1 if (a,b)==(e,f) else -1
    return z0,z1,z2

def check(m,n,all_actions=True):
    C=setup(m,n);vertices,edges,c0,c1,c2,bc1,bc2=C
    for e in c2:
        dd={}
        for i,s in bc2(e):
            for j,t in bc1(c1[i]): dd[j]=dd.get(j,0)+s*t
        assert all(z==0 for z in dd.values()),e
    r1=rank_mod(map(bc1,c1));r2=rank_mod(map(bc2,c2))
    b1=len(c1)-r1-r2;b2=len(c2)-r2
    B=lambda k:(k*(k-3))//2 # dim of (k-2,2) for k>=3, zero at k=3
    D=lambda k:(k-1)*(k-2)//2 # dim of (k-2,1,1)
    pred=B(m)*D(n)+D(m)*B(n)
    assert r1==len(c0)-1 and b1==(m-1)*(n-1) and b2==pred,(m,n,b1,b2,pred)
    actions=0
    if all_actions:
        for p,q in product(permutations(range(m)),permutations(range(n))):
            z0,z1,z2=cellular_traces(m,n,C,p,q)
            # Graph first homology is U_m \otimes U_n - U_m - U_n + 1.
            fp,tp=cyc(p);fq,tq=cyc(q)
            h1=fp*fq-fp-fq+1
            actual=z0-z1+z2-1+h1
            Bp,Dp=chars(p);Bq,Dq=chars(q)
            expected=Bp*Dq+Dp*Bq
            assert actual==expected,(m,n,p,q,(z0,z1,z2),actual,expected)
            actions+=1
        if m==n:
            for p,q in product(permutations(range(m)),permutations(range(n))):
                z0,z1,z2=cellular_traces(m,n,C,p,q,swap=True)
                fp,tp=cyc(tuple(q[p[i]] for i in range(m)))
                h1=1-fp
                assert z0-z1+z2-1+h1==0,(m,n,p,q,(z0,z1,z2),h1)
                actions+=1
    print(f'K_{{{m},{n}}}: (c0,c1,c2)={(len(c0),len(c1),len(c2))}; (rank_d1,rank_d2)={(r1,r2)}; (b1,b2)={(b1,b2)}; actions_tested={actions}')

if __name__=='__main__':
    for m,n in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)]:
        check(m,n,all_actions=(m,n) in [(3,3),(3,4),(4,4)])
    print('VERIFY_OK')
