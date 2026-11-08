"""Exact verifier for SIR final-size laws on a bouquet of triangles.

Run with: python3 verify.py. Standard library only.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from math import comb


def petal_pgf(m, lam):
    """Integrate a petal multinomial law against the shared beta variable."""
    lam = F(lam)
    c = 2 / (1 + lam)
    # coefficient of u^power_u z^power_z for one triangle
    single = {(2, 0): F(1), (1, 1): c, (2, 1): -c,
              (0, 2): F(1), (1, 2): -c, (2, 2): c - 1}
    poly = {(0, 0): F(1)}
    for _ in range(m):
        nxt = defaultdict(F)
        for (a, b), v in poly.items():
            for (i, j), w in single.items():
                nxt[(a+i, b+j)] += v*w
        poly = nxt
    ans = [F(0)] * (2*m + 1)
    for (i, j), coeff in poly.items():
        ans[j] += coeff / (1 + lam*i)  # E[U^i] = 1/(1 + lam*i)
    return tuple(ans)


def labeled_sir_pgf(m, lam):
    """An independent full 3^(2m+1)-state CTMC first-step recursion."""
    lam = F(lam)
    n = 2*m+1
    nbr = [[] for _ in range(n)]
    for j in range(m):
        a,b = 2*j+1, 2*j+2
        for x,y in ((0,a),(0,b),(a,b)):
            nbr[x].append(y)
            nbr[y].append(x)

    @lru_cache(None)
    def f(state):
        infective = [i for i,s in enumerate(state) if s==1]
        if not infective:
            count = sum(s==2 for s in state)-1  # omit initial hub
            return tuple(F(k==count) for k in range(2*m+1))
        events=[]
        for i in infective:
            nxt=list(state);nxt[i]=2
            events.append((F(1),tuple(nxt)))
        for i,s in enumerate(state):
            if s!=0:continue
            rate=lam*sum(state[j]==1 for j in nbr[i])
            if rate:
                nxt=list(state);nxt[i]=1
                events.append((rate,tuple(nxt)))
        total=sum(rate for rate,_ in events)
        out=[F(0)]*(2*m+1)
        for rate,nextstate in events:
            p=f(nextstate)
            for k in range(2*m+1):out[k]+=rate*p[k]/total
        return tuple(out)
    return f((1,)+(0,)*(n-1)),f.cache_info().currsize


def mean_and_variance(p):
    mean=sum(F(k)*v for k,v in enumerate(p))
    variance=sum(F(k*k)*v for k,v in enumerate(p))-mean*mean
    return mean,variance


def mu_tri(lam):
    lam=F(lam)
    return lam*(2*lam**2+4*lam+1)/((lam+1)**2*(2*lam+1))


def var_tri_limit(lam):
    x=F(lam)
    return (x*x*(12*x**5+60*x**4+100*x**3+58*x*x+13*x+1)
            / ((x+1)**4*(2*x+1)**2*(3*x+1)*(4*x+1)))


def e_sigma2(lam):
    x=F(lam)
    return 2*x*(6*x+1)*(2*x*x+5*x+1)/((x+1)**2*(2*x+1)*(3*x+1)*(4*x+1))


def tri_variance(m,lam):
    return var_tri_limit(lam)+e_sigma2(lam)/(4*m)


def star_variance(m,lam):
    x=F(lam)
    return x*x/((1+x)**2*(1+2*x))+x/(2*m*(1+x)*(1+2*x))


def P(x):
    return 12*x**4+14*x**3-15*x*x-13*x-2


def Q(m,x):
    return 2*m*x*P(x)-(13*x+3)*(1+x)**2*(1+2*x)


def delta_closed(m,x):
    x=F(x)
    return -x*x*Q(m,x)/(2*m*(1+x)**4*(1+2*x)**2*(1+3*x)*(1+4*x))


def check():
    tally=0
    for m in range(1,5):
        for lam in (F(1,2),F(1),F(2)):
            an=petal_pgf(m,lam)
            direct,numstates=labeled_sir_pgf(m,lam)
            assert an==direct,(m,lam)
            assert sum(an)==1 and min(an)>=0
            mean,var=mean_and_variance(an)
            assert mean==2*m*mu_tri(lam)
            assert var==4*m*m*tri_variance(m,lam)
            tally+=4
    for m in (1,2,3,4,5,10,30):
        for lam in (F(1,4),F(1,2),F(1),F(5,4),F(2),F(3)):
            assert tri_variance(m,lam)-star_variance(m,lam)==delta_closed(m,lam)
            tally+=1
    for lam in (F(1,4),F(1,2),F(1),F(2),F(3)):
        x=lam
        assert mu_tri(x)-x/(1+x)==x*x/((x+1)**2*(2*x+1))
        tally+=1
    assert delta_closed(1,F(1)) > 0
    assert delta_closed(2,F(2)) < 0
    assert delta_closed(1,F(2)) > 0
    assert delta_closed(1,F(3)) < 0
    print(f'PASS: {tally} exact distribution, moment, normalization and identity checks; 12 labeled CTMC computations.')

if __name__=='__main__':check()
