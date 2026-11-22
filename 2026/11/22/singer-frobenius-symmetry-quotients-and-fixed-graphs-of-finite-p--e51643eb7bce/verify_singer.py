"""Exact finite-field and orbit-graph checks for Singer-normalizer quotients.

All calculations use Python's standard library.  They independently
construct incidence edges from finite-field trace and enumerate group orbits.
"""
from math import gcd


def prime_factors(n):
    out=[]
    k=2
    while k*k<=n:
        if n%k==0:
            out.append(k)
            while n%k==0: n//=k
        k+=1
    if n>1: out.append(n)
    return out


def extension_field(p,d):
    """Find a polynomial for which x generates all nonzero residues."""
    size=p**d
    def mult(a,b,coef):
        A=[(a//p**i)%p for i in range(d)]
        B=[(b//p**i)%p for i in range(d)]
        tmp=[0]*(2*d-1)
        for i in range(d):
            if A[i]:
                for j in range(d):
                    if B[j]:tmp[i+j]=(tmp[i+j]+A[i]*B[j])%p
        for k in range(2*d-2,d-1,-1):
            c=tmp[k]
            if c:
                for j in range(d):tmp[k-d+j]=(tmp[k-d+j]-c*coef[j])%p
        return sum(tmp[i]*p**i for i in range(d))
    def pw(a,n,coef):
        res=1
        while n:
            if n&1:res=mult(res,a,coef)
            a=mult(a,a,coef); n>>=1
        return res
    M=size-1
    factors=prime_factors(M)
    # All nonzero residues being powers of x certifies that this is a field.
    for poly in range(1,size):
        co=[(poly//p**i)%p for i in range(d)]
        if co[0]==0:continue
        if pw(p,M,co)==1 and all(pw(p,M//r,co)!=1 for r in factors):
            powers=[1]
            for i in range(1,M):powers.append(mult(powers[-1],p,co))
            assert len(set(powers))==M and mult(powers[-1],p,co)==1
            return co,mult,pw,powers
    raise AssertionError('primitive polynomial not found')


def singer_difference_set(q):
    p=next(p for p in range(2,q+1) if q%p==0)
    e=0;v=q
    while v%p==0:v//=p;e+=1
    assert v==1
    N=q*q+q+1
    coef,mult,pw,powers=extension_field(p,3*e)
    D=[]
    for t in range(N):
        x=powers[t]
        def add(a,b):
            return sum((((a//p**i)%p+(b//p**i)%p)%p)*p**i for i in range(3*e))
        tr=add(add(x,pw(x,q,coef)),pw(x,q*q,coef))
        if tr==0:D.append((-t)%N)
    assert len(D)==q+1 and {q*t%N for t in D}==set(D)
    assert len({(t-u)%N for t in D for u in D if t!=u})==N-1
    return N,D,coef


def orbit_count(objects,gens):
    remain=set(objects)
    count=0
    while remain:
        count+=1
        seed=next(iter(remain));remain.remove(seed);todo=[seed]
        while todo:
            x=todo.pop()
            for g in gens:
                y=g(x)
                if y in remain:remain.remove(y);todo.append(y)
    return count


def divisors(n):return [d for d in range(1,n+1) if n%d==0]


def expected(q,m,semilinear):
    if not semilinear:return 1+m*(q-1)
    if q%3==1:return 1+m*(q-1)//3
    if q%3==0:
        assert (m*(q-1)-2)%3==0
        return 1+(m*(q-1)-2)//3
    assert (m*(q-1)-4)%3==0
    return 1+(m*(q-1)-4)//3


def test_q(q):
    N,D,coef=singer_difference_set(q)
    D=set(D)
    points=list(range(2*N))
    edges=[(i,t) for i in range(N) for t in sorted(D)]
    def rotate_v(m):return lambda v: (v//N)*N+(v%N+m)%N
    def frob_v(a):return lambda v: (v//N)*N+(a+q*(v%N))%N
    def rotate_e(m):return lambda z: ((z[0]+m)%N,z[1])
    def frob_e(a):return lambda z: ((a+q*z[0])%N,q*z[1]%N)
    checked=0
    for d in divisors(N):
        m=N//d
        # Representatives include both conjugacy classes for q=1 mod 3.
        for a in (None,0,1,2):
            if a is not None and a>=m:continue
            vg=[rotate_v(m)]; eg=[rotate_e(m)]
            if a is not None:
                vg.append(frob_v(a));eg.append(frob_e(a))
            V=orbit_count(points,vg)
            E=orbit_count(edges,eg)
            b=E-V+1
            assert b==expected(q,m,a is not None),(q,d,m,a,E,V,b)
            checked+=1
    fD=sum(q*t%N==t for t in D)
    assert fD==({0:1,1:2,2:0}[q%3])
    fix=[]
    for a in range(min(N,3)):
        fv=[v for v in points if frob_v(a)(v)==v]
        fe=[(i,t) for i,t in edges if frob_e(a)((i,t))==(i,t)]
        graph={v:set() for v in fv}
        for i,t in fe:
            v=i;w=N+(i+t)%N
            assert v in graph and w in graph
            graph[v].add(w);graph[w].add(v)
        components=0;unseen=set(graph)
        while unseen:
            components+=1;v=unseen.pop();stack=[v]
            while stack:
                w=stack.pop()
                for z in graph[w]:
                    if z in unseen:unseen.remove(z);stack.append(z)
        assert len(fv)==(2*(3 if q%3==1 and a%3==0 else 0) if q%3==1 else 2)
        assert len(fe)==({0:1,1:6,2:0}[q%3] if a==0 or q%3!=1 else 0)
        types={(0,2,0,2):'two points',(0,2,1,1):'interval',
               (0,6,6,1):'circle',(0,0,0,0):'empty'}
        label=types.get((0,len(fv),len(fe),components))
        assert label is not None,(q,a,len(fv),len(fe),components)
        if label=='circle':assert all(len(s)==2 for s in graph.values())
        fix.append(label)
    print('q=%-2d N=%-4d polynomial=%-23s subgroup-cases=%-3d full-normalizer-b1=%-3d fixed=%s' %
          (q,N,str(coef),checked,expected(q,1,True),','.join(fix)))


if __name__=='__main__':
    for q in (2,3,4,5,7,8,9,11,13,16):test_q(q)
    print('PASS: field, difference-set, full vertex/edge-orbit and fixed-graph checks')
