"""Direct finite-field checks for rectangular-band algebra commuting tuples.

Pure Python, standard library only.  No symbolic assumptions are used to decide
whether two literal algebra elements commute.
"""
from itertools import product


def rows_cols(a, m, n, q):
    r=tuple(sum(a[i*n+j] for j in range(n))%q for i in range(m))
    c=tuple(sum(a[i*n+j] for i in range(m))%q for j in range(n))
    return r,c


def multiply(a,b,m,n,q):
    out=[0]*(m*n)
    # Product of basis elements e_(i,j)e_(k,l)=e_(i,l).
    for i in range(m):
        for j in range(n):
            aa=a[i*n+j]
            if aa:
                for k in range(m):
                    for ell in range(n):
                        out[i*n+ell]=(out[i*n+ell]+aa*b[k*n+ell])%q
    return tuple(out)


def commute_direct(a,b,m,n,q):
    return multiply(a,b,m,n,q)==multiply(b,a,m,n,q)


def commute_profile(h,g,q):
    r,c=h
    s,d=g
    return all((r[i]*d[j]-s[i]*c[j])%q==0
               for i in range(len(r)) for j in range(len(c)))


def predicted(m,n,q,t):
    w=(m-1)*(n-1)
    mixed=(q**(m+n-1)-q**(m-1)-q**(n-1)+1)//(q-1)
    hcount=q**(t*(n-1))+q**(t*(m-1))-1+mixed*(q**t-1)
    return (q**(w*t))*hcount


def finite_check(m,n,q,t,check_literal=False):
    elems=list(product(range(q),repeat=m*n))
    profiles=[rows_cols(a,m,n,q) for a in elems]
    unique_h=sorted(set(profiles))
    if check_literal:
        # Build actual algebra table independently, then compare with profile
        # criterion for every ordered pair.
        for i,a in enumerate(elems):
            for j,b in enumerate(elems):
                assert commute_direct(a,b,m,n,q)==commute_profile(profiles[i],profiles[j],q), (m,n,q,i,j)
    good=0
    for tup in product(unique_h,repeat=t):
        if all(commute_profile(tup[i],tup[j],q)
               for i in range(t) for j in range(i+1,t)):
            good+=1
            # Independently decide membership in three proposed pieces.
            zr=all(all(v==0 for v in h[0]) for h in tup)
            zc=all(all(v==0 for v in h[1]) for h in tup)
            # A column-rank-one test on row+col coordinates.
            vals=[h[0]+h[1] for h in tup]
            det1=all((vals[i][a]*vals[j][b]-vals[i][b]*vals[j][a])%q==0
                for i in range(t) for j in range(i+1,t)
                for a in range(m+n) for b in range(a+1,m+n))
            assert zr or zc or det1,(m,n,q,t,tup)
    w=(m-1)*(n-1)
    actual=good*q**(w*t)
    want=predicted(m,n,q,t)
    assert actual==want,(m,n,q,t,actual,want)
    print('PASS m=%s n=%s q=%s t=%s H=%s tuples=%s' %(m,n,q,t,len(unique_h),actual))


if __name__=='__main__':
    for m,n,q,t,literal in [
        (2,2,2,2,True),(2,2,3,2,True),(2,3,2,2,True),
        (3,2,2,2,False),(3,3,2,2,False),
        (2,2,2,3,False),(2,3,2,3,False),
        (2,2,3,3,False),(3,3,2,3,False),
        (2,3,2,4,False),
    ]:
        finite_check(m,n,q,t,literal)
    print('VERIFY_OK_RECTANGULAR_BAND_COMMUTING_VARIETIES')


def check_maximal_commutative_subalgebras(m,n,q):
    """Exhaustively enumerate maximal cliques using literal products, not profiles."""
    assert q==2
    elems=list(product(range(q),repeat=m*n))
    N=len(elems)
    adj={i:{j for j in range(N) if i!=j and commute_direct(elems[i],elems[j],m,n,q)}
         for i in range(N)}
    maximal=[]
    def bronk(R,P,X):
        if not P and not X:
            maximal.append(frozenset(R))
            return
        if not P: return
        pivot=max(P|X,key=lambda v:len(adj[v]&P)) if P|X else None
        for v in list(P-(adj[pivot] if pivot is not None else set())):
            bronk(R|{v},P&adj[v],X&adj[v])
            P.remove(v); X.add(v)
    bronk(set(),set(range(N)),set())
    from collections import defaultdict
    fibers=defaultdict(set)
    for i,a in enumerate(elems):fibers[rows_cols(a,m,n,q)].add(i)
    zero_r=(0,)*m; zero_c=(0,)*n
    pure_left={i for h,I in fibers.items() if h[0]==zero_r for i in I}
    pure_right={i for h,I in fibers.items() if h[1]==zero_c for i in I}
    candidates={frozenset(pure_left),frozenset(pure_right)}
    for h in fibers:
        if h[0]!=zero_r and h[1]!=zero_c:
            candidates.add(frozenset(fibers[(zero_r,zero_c)]|fibers[h]))
    assert set(maximal)==candidates,(m,n,q,len(maximal),len(candidates))
    for cl in maximal:
        # Pairwise addition and multiplication stay within each listed maximal clique.
        cv={elems[i]:i for i in cl}
        for i in cl:
            for j in cl:
                assert tuple((x+y)%q for x,y in zip(elems[i],elems[j])) in cv
                assert multiply(elems[i],elems[j],m,n,q) in cv
    print('MAXIMAL_SUBALGEBRAS_OK m=%d n=%d q=%d count=%d' %(m,n,q,len(maximal)))

if __name__=='__main__':
    check_maximal_commutative_subalgebras(2,2,2)
    check_maximal_commutative_subalgebras(2,3,2)
