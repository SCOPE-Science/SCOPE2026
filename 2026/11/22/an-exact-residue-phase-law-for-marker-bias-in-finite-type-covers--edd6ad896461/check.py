"""Reproducible numerical and finite-language checks for renewal-cover asymptotics.

Python >=3.11, standard library only. The analytic proof is in RESULT.md.
"""
from decimal import Decimal, localcontext
from itertools import product


def shift(head, period):
    assert len(period) >= 2 and any(period) and not all(period)
    return (tuple(head), tuple(period))


def bits(d, case):
    head, tail = case
    return head[d-1] if d <= len(head) else tail[(d-len(head)-1) % len(tail)]


def evaluate(z, case, n=None):
    head, tail = case
    N, m = len(head)+1, len(tail)
    denom = Decimal(1)-z**m
    T = sum(Decimal(a)*z**(N+j) for j,a in enumerate(tail))
    Tp = sum(Decimal(a)*(N+j)*z**(N+j-1) for j,a in enumerate(tail))
    F = sum(Decimal(a)*z**(j+1) for j,a in enumerate(head))+T/denom
    Fp = sum(Decimal(a)*(j+1)*z**j for j,a in enumerate(head)) + Tp/denom+T*m*z**(m-1)/(denom**2)
    if n is None: return F, Fp, Decimal(0)
    assert n >= N
    comp = [1-bits(n+j,case) for j in range(m)]
    B = sum(Decimal(v)*z**j for j,v in enumerate(comp))
    Bp = sum(Decimal(v)*j*z**(j-1) for j,v in enumerate(comp) if j)
    H = B/denom
    Hp = Bp/denom+B*m*z**(m-1)/(denom**2)
    return F+z**n*H, Fp + n*z**(n-1)*H + z**n*Hp, H


def root(case, n=None):
    lo, hi = Decimal('0.1'), Decimal('0.999')
    assert evaluate(lo,case,n)[0]<1 and evaluate(hi,case,n)[0]>1
    for _ in range(540):
        mid=(lo+hi)/2
        if evaluate(mid,case,n)[0] > 1: hi=mid
        else: lo=mid
    return (lo+hi)/2


def accepts_graph(word, case, n):
    # State j records zeros after the most recent 1, capped at n-1.
    states=set(range(n))
    for symbol in word:
        nxt=set()
        for j in states:
            if symbol == 0:
                nxt.add(min(j+1,n-1))
            elif j == n-1 or bits(j+1,case):
                nxt.add(0)
        states=nxt
        if not states: return False
    return True


def graph_radius(case, n):
    # Independent primitive adjacency power iteration; both edge labels count.
    v=[1.0]*n
    lam=1.0
    for _ in range(6000):
        w=[]
        for j in range(n):
            w.append(v[min(j+1,n-1)] + (v[0] if j==n-1 or bits(j+1,case) else 0.0))
        lam=max(w)
        v=[x/lam for x in w]
    # normalized max(v)=1; use Collatz-Wielandt spread as residual.
    w=[v[min(j+1,n-1)] + (v[0] if j==n-1 or bits(j+1,case) else 0.0) for j in range(n)]
    ratios=[x/y for x,y in zip(w,v)]
    assert max(ratios)-min(ratios)<1e-9
    return sum(ratios)/len(ratios)


def verify(case):
    head, period = case
    m=len(period)
    q=root(case)
    M=q*evaluate(q,case)[1]
    rho=1/M
    print('head=',head,'period=',period,'q=',str(q)[:23],'rho=',str(rho)[:23])
    assert Decimal('0.5')<q<1
    for n in range(len(head)+1, len(head)+1+2*m):
        # Identity: all length-n words in X have exactly the same pairwise
        # 1-gap restrictions as the n-th canonical cover.
        for w in product((0,1),repeat=n):
            where=[i for i,v in enumerate(w) if v==1]
            in_X=all(bits(b-a,case) for a,b in zip(where,where[1:]))
            in_cover=all(bits(b-a,case) or b-a>=n for a,b in zip(where,where[1:]))
            assert in_X==in_cover
            assert accepts_graph(w, case, n)==in_X
        if n<=9:
            qn=root(case,n)
            assert abs(graph_radius(case,n)-float(1/qn))<1e-8
    for residue in range(m):
        for n in [n for n in (64+residue, 96+residue, 128+residue) if n% m == residue]:
            if n < len(head)+1: continue
            qn=root(case,n)
            Fn, Fpn, H=evaluate(qn,case,n)
            Mn=qn*Fpn
            rhon=1/Mn
            delta_h=(q/qn).ln()
            coef_h=delta_h/(q**n)
            coef_rho=(rho-rhon)/(n*q**n)
            exp_h=evaluate(q,case,n)[2]/M
            exp_rho=evaluate(q,case,n)[2]/(M*M)
            assert abs(coef_h-exp_h)<Decimal('0.00001'),(n,coef_h,exp_h)
            assert abs(coef_rho-exp_rho)<Decimal('0.03'),(n,coef_rho,exp_rho)
            assert 0 < rhon < rho and delta_h>0
            ratio=(rho-rhon)/(n*delta_h)
            assert abs(ratio-rho)<Decimal('0.03'),(n,ratio,rho)
            print('n=',n,'class=',n%m,'h-coeff=',str(coef_h)[:14],
                  'rho-coeff=',str(coef_rho)[:14], 'limit=',str(exp_rho)[:14])


def main():
    with localcontext() as c:
        c.prec=125
        cases=[shift([1],[0,1]),shift([1],[1,0,1]),
               shift([1,0],[1,0,0,1]),shift([1,0,0,1,0],[0,1,0,1,1]),shift([],[0,1,1])]
        for case in cases: verify(case)
        q=root(cases[0]); M=q*evaluate(q,cases[0])[1]
        phi=(Decimal(1)+Decimal(5).sqrt())/2
        assert abs(1/q-phi)<Decimal('1e-95')
        assert abs(M-Decimal(5).sqrt())<Decimal('1e-95')
        for n in (64,65,80,81):
            H=evaluate(q,cases[0],n)[2]
            expected=phi if n%2==0 else Decimal(1)
            assert abs(H-expected)<Decimal('1e-95')
        print('All finite-language, graph-spectral, asymptotic and parity checks passed.')

if __name__ == '__main__': main()
