"""Truncated rank-2 quantum scattering solver (exact, sympy rational in t)."""
import sympy as sp
t = sp.Symbol('t')

def E_log_coeffs(j, vdeg, M):
    """Return dict kexp -> coeff (sympy) for X=log E(-t^j z^v), kexp = multiple m of v with m<=M.
    vdeg unused (multiples). M = max multiple."""
    X = {}
    if j % 2 == 0:
        for k in range(1, M+1):
            c = (-1)**(k-1) * t**(j*k) / (k*(t**k - t**(-k)))
            X[k] = sp.simplify(X.get(k, 0) + c)
    else:
        r = 0
        while (2**r) <= M:
            s = 2**r
            for k in range(1, M//s + 1):
                c = (-1)**(k-1) * t**(s*j*k) / (k*(t**(s*k) - t**(-s*k)))
                m = k*s
                X[m] = sp.simplify(X.get(m, 0) + c)
            r += 1
    return X

def E_series(p, v, N):
    """p: dict shift->int coeff. v=(a,b). Return dict (A,B)->sympy rational: E(-p z^v) truncated |.|<=N."""
    tot = v[0]+v[1]
    M = N//tot
    X = {}  # m -> coeff
    for j, c in p.items():
        if c == 0: continue
        Xj = E_log_coeffs(j, tot, M)
        for m, cc in Xj.items():
            X[m] = sp.simplify(X.get(m, 0) + c*cc)
    # F = exp(X), commuting powers: F_0=1, F_m from Bell polynomials
    F = {(0,0): sp.Integer(1)}
    # Xpow[m] = coeff of z^{m v}
    Xc = {m: sp.simplify(X.get(m,0)) for m in range(1, M+1)}
    # exp via recurrence: F_0=1; F_m = sum_{k=1..m} (k/m) ... use standard: m F_m = sum_{k=1..m} k X_k F_{m-k}? For ordinary exp of power series: F = exp(X), X_0=0: F_0=1, F_m = (1/m) sum_{k=1..m} k X_k F_{m-k} *? Actually for ordinary generating (exponential in ring, not exp series): if F=exp(X) then F' = X' F gives m F_m = sum_{k=1..m} k X_k F_{m-k}. Yes.
    Fm = {0: sp.Integer(1)}
    for m in range(1, M+1):
        s = 0
        for k in range(1, m+1):
            s += k * Xc.get(k,0) * Fm.get(m-k,0)
        Fm[m] = sp.simplify(s/m)
    for m in range(1, M+1):
        F[(m*v[0], m*v[1])] = sp.simplify(Fm[m])
    return F

def mul(F, G, N, n):
    H = {}
    for (a1,b1),c1 in F.items():
        for (a2,b2),c2 in G.items():
            a=a1+a2; b=b1+b2
            if a+b<=N:
                w = n*(a1*b2-b1*a2)
                H[(a,b)] = sp.simplify(H.get((a,b),0) + c1*c2*t**w)
    return H

def sinv(F, N, n):
    H = {(0,0): sp.Integer(1)}
    for d in range(1, N+1):
        for a in range(d+1):
            b=d-a; m=(a,b)
            s=0
            for u1 in range(a+1):
                for v1 in range(b+1):
                    for u2 in range(a+1):
                        for v2 in range(b+1):
                            if u1+u2==a and v1+v2==b and not (u2==a and v2==b):
                                cu=F.get((u1,v1),0); cv=H.get((u2,v2),0)
                                if cu!=0 and cv!=0:
                                    s += cu*cv*t**(n*(u1*v2-v1*u2))
            H[m]=sp.simplify(-s)
    # remove zeros
    return {k:sp.simplify(v) for k,v in H.items() if sp.simplify(v)!=0}

def solve(n, p1, p2, N):
    v1=(1,0); v2=(0,1)
    F1=E_series(p1,v1,N); F2=E_series(p2,v2,N)
    F1i=sinv(F1,N,n); F2i=sinv(F2,N,n)
    Ess={}; Q={}
    for d in range(1,N+1):
        cur=[(a,d-a) for a in range(d+1) if a>=1 and (d-a)>=1]
        # product of knowns: P = F2 * O_known_desc * F1 * F2i * F1i ; O sorted ascending slope, leftmost largest slope
        Oknown=sorted([v for v in Ess], key=lambda v: (v[1]/v[0], v[0]))
        P=dict(F1i)
        P=mul(dict(F2i),P,N,n)
        P=mul(dict(F1),P,N,n)
        for v in Oknown:
            P=mul(dict(Ess[v]),P,N,n)
        P=mul(dict(F2),P,N,n)
        for v in cur:
            D=sp.simplify(P.get(v,0))
            qv=sp.simplify(-(t-t**(-1))*D)
            qv=sp.together(qv)
            Q[v]=qv
            # to dict shift->int for E_series
            if sp.simplify(qv)==0:
                Ess[v]={(0,0):sp.Integer(1)}; continue
            K0=40
            qvs=sp.together(qv)
            nn0,dd0=sp.fraction(qvs)
            # cancel factors of (t^k-1)/(t-1)? clear denominators by multiplying with (t^K-1) factors if needed
            polyK=sp.together(qvs*t**K0)
            nn1,dd1=sp.fraction(polyK)
            if sp.simplify(dd1-1)!=0:
                nn1=sp.expand(sp.cancel(qvs*t**K0))
                nn1,dd1=sp.fraction(sp.together(nn1))
                if sp.simplify(dd1-1)!=0:
                    raise ArithmeticError(f"non-Laurent q at {v}: qv={qv}")
            PpolyK=sp.Poly(sp.expand(nn1),t)
            assert PpolyK is not None, f"non-Laurent q at {v}: {qv}"
            qd={}
            for (e,),c in PpolyK.as_dict().items():
                if c==0: continue
                qd[e-K0]=int(c)
            Ess[v]=E_series(qd,v,N)
    # verify
    Oknown=sorted([v for v in Ess], key=lambda v: (v[1]/v[0], v[0]))
    P=dict(F1i); P=mul(dict(F2i),P,N,n); P=mul(dict(F1),P,N,n)
    for v in Oknown: P=mul(dict(Ess[v]),P,N,n)
    P=mul(dict(F2),P,N,n)
    bad={k:sp.simplify(v) for k,v in P.items() if k!=(0,0) and sp.simplify(v)!=0}
    return Q,Ess,bad

def is_barinv(q):
    return sp.simplify(q - q.subs(t,1/t))==0

def _laurent_dict(q):
    q=sp.expand(sp.cancel(sp.together(q)))
    if q==0: return {}
    K0=60
    q2=sp.together(q*t**K0)
    nn,dd=sp.fraction(q2)
    if sp.simplify(dd-1)!=0:
        nn=sp.expand(sp.cancel(q*t**K0)); nn,dd=sp.fraction(sp.together(nn))
        if sp.simplify(dd-1)!=0: return None
        P=sp.Poly(sp.expand(nn),t)
    else:
        P=sp.Poly(sp.expand(nn),t)
    if P is None: return None
    dd={}
    for k,v in P.as_dict().items():
        try: dd[k[0]-K0]=int(v)
        except Exception: return None
        if sp.simplify(v-dd[k[0]-K0])!=0: return None
    return {k:v for k,v in dd.items() if v!=0}

def lefschetz_decomp(q):
    dd=_laurent_dict(q)
    if dd is None: return None
    if not dd: return {}
    res={}
    for _ in range(300):
        if not dd: return res
        md=max(dd); c=int(dd[md])
        if c<=0: return None
        m=md+1
        if m<1: return None
        for j in range(m):
            e=m-1-2*j
            dd[e]=dd.get(e,0)-c
            if dd[e]==0: del dd[e]
        res[m]=res.get(m,0)+c
    return None
