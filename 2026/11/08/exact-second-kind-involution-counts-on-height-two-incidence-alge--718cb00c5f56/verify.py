"""Reproduce exhaustive tests for semilinear anti-involutions of height-two incidence algebras.
Usage: python verify.py
No external dependencies.
"""
from itertools import product

def make_field(p):
    # Construct F_{p^2}; for p=2 use x^2+x+1, for p=3 use x^2+1.
    assert p in (2,3)
    Q=p*p
    def add(a,b):
        return (a%p+b%p)%p + p*((a//p+b//p)%p)
    def neg(a):return ((-a%p)+p*(-(a//p)%p))
    def mul(a,b):
        a0,a1=a%p,a//p; b0,b1=b%p,b//p
        if p==2:return ((a0*b0+a1*b1)%p)+p*((a0*b1+a1*b0+a1*b1)%p)
        return ((a0*b0-a1*b1)%p)+p*((a0*b1+a1*b0)%p)
    def power(x,n):
        z=1
        while n:
            if n&1:z=mul(z,x)
            x=mul(x,x);n//=2
        return z
    star=lambda x:power(x,p)
    assert all(power(a,Q-1)==1 for a in range(1,Q))
    assert sum(star(a)==a for a in range(Q))==p
    return Q,add,neg,mul,star

def experiment(p,n):
    Q,add,neg,mul,star=make_field(p)
    # Complete bipartite poset (A_i<B_j), tau(A_i)=B_i, tau(B_i)=A_i.
    verts=2*n; edges=[(i,n+j) for i in range(n) for j in range(n)]
    bases=[('v',i) for i in range(verts)]+[('e',u,v) for u,v in edges]
    dim=len(bases); edge_id={e:i+verts for i,e in enumerate(edges)}
    def reversed_edge(e):
        u,v=e; return (v-n,n+u)
    def Bmul(i,j):
        a,b=bases[i],bases[j]
        if a[0]=='v' and b[0]=='v':return i if a==b else None
        if a[0]=='v' and b[0]=='e':return j if a[1]==b[1] else None
        if a[0]=='e' and b[0]=='v':return i if a[2]==b[1] else None
        return None
    def vmul(x,y):
        out=[0]*dim
        for i,a in enumerate(x):
            if a:
                for j,b in enumerate(y):
                    if b:
                        k=Bmul(i,j)
                        if k is not None:out[k]=add(out[k],mul(a,b))
        return tuple(out)
    def vadd(x,y):return tuple(add(a,b) for a,b in zip(x,y))
    def vneg(x):return tuple(neg(a) for a in x)
    def vc(x):return tuple(star(a) for a in x)
    unit=lambda i:tuple(1 if j==i else 0 for j in range(dim))
    E=[unit(i) for i in range(dim)]
    tau=lambda i:i+n if i<n else i-n
    edge_orbits=[];seen=set()
    for e in edges:
        if e not in seen:
            f=reversed_edge(e)
            edge_orbits.append((e,) if f==e else (e,f))
            seen.update((e,f))
    coptions=[]
    for orb in edge_orbits:
        if len(orb)==1:
            coptions.append([{orb[0]:c} for c in range(1,Q) if mul(c,star(c))==1])
        else:
            coptions.append([{orb[0]:c,orb[1]:power_inv(c,mul,Q)} for c in range(1,Q)])
    # c_reverse = inverse(star(c))
    scalar_sets=[]
    for entries in product(*coptions):
        d={}
        for entry in entries:d.update(entry)
        scalar_sets.append(d)
    expected_scalar=(p+1)**n*(Q-1)**(n*(n-1)//2)
    assert len(scalar_sets)==expected_scalar
    fixed_sizes=set(); seen_maps=set();count=0
    for c in scalar_sets:
        target=[None]*dim
        for i in range(verts):target[i]=E[tau(i)]
        for e in edges:
            col=edge_id[e]; row=edge_id[reversed_edge(e)]
            target[col]=tuple(c[e] if j==row else 0 for j in range(dim))
        def rho(x):
            out=[0]*dim
            for i,a in enumerate(x):
                if a:
                    for j,b in enumerate(target[i]):
                        if b:out[j]=add(out[j],mul(star(a),b))
            return tuple(out)
        for i in range(dim):
            assert rho(rho(E[i]))==E[i]
            for j in range(dim):
                k=Bmul(i,j); basisprod=E[k] if k is not None else (0,)*dim
                assert rho(basisprod)==vmul(rho(E[j]),rho(E[i]))
        # Solve v=rho(v) by direct enumeration of radical coordinates (Q^4 at n=2).
        fixed=[]
        for coords in product(range(Q),repeat=len(edges)):
            v=(0,)*verts+coords
            if rho(v)==v:fixed.append(v)
        fixed_sizes.add(len(fixed))
        for v in fixed:
            # conjugation (1+v) y (1-v) = y+vy-yv, J^2=0
            def conj(y):
                return vadd(y,vadd(vmul(v,y),vneg(vmul(y,v))))
            cols=tuple(conj(t) for t in target)
            assert cols not in seen_maps
            seen_maps.add(cols)
            count+=1
            def phi(x):return conj(rho(x))
            for i in range(dim):
                assert phi(phi(E[i]))==E[i]
                for j in range(dim):
                    k=Bmul(i,j);prod=E[k] if k is not None else (0,)*dim
                    assert phi(prod)==vmul(phi(E[j]),phi(E[i]))
    expected=p**(n*n)*expected_scalar
    assert count==expected and fixed_sizes=={p**(n*n)}
    print(f'F_{Q}, K_{{{n},{n}}}: tau-normalized scalars={expected_scalar}; fixed-radical choices={p**(n*n)}; distinct involutions={count}')
    return count

def power_inv(x,mul,Q):
    # output = inverse(star(x))=x^(-p), where p=sqrt(Q)
    p=int(Q**.5)
    z=1
    for _ in range((Q-1-p)%(Q-1)):
        z=mul(z,x)
    return z

if __name__=='__main__':
    for p,n in [(2,1),(3,1),(2,2),(3,2)]:experiment(p,n)
    print('VERIFY_OK')
