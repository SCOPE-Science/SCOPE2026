"""Exact small-market checks for heterogeneous exponential allocation probabilities.
Only Python standard library is needed.  This checker verifies finite instances;
all-parameter statements are established analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations

def p_single(a, others):
    z = F(1)
    for b in others:
        z *= F(a, a + b)
    return z

def p_pair_above_pair(a, b, c, d):
    # Survival of X_a+X_b evaluated at independent X_c+X_d.
    def laplace(x):
        return F(x, x + c) * F(x, x + d)
    if a != b:
        return (a * laplace(a) - b * laplace(b)) / (a - b)
    # Derivative of x^3/[(x+c)(x+d)] at x=a.
    return laplace(a) * (3 - F(a,a+c) - F(a,a+d))

def prob(A,B):
    assert len(A)+len(B) in (2,3,4)
    if len(A)==1: return p_single(A[0],B)
    if len(B)==1: return 1-p_single(B[0],A)
    assert len(A)==len(B)==2
    return p_pair_above_pair(A[0],A[1],B[0],B[1])

def scores(weights):
    n=len(weights)
    ans=[]
    for k in range(1,n):
        for ids in combinations(range(n),k):
            if 0 not in ids: continue # complement has same ex-post probability
            A=tuple(weights[i] for i in ids)
            B=tuple(weights[i] for i in range(n) if i not in ids)
            p=prob(A,B)
            ans.append((ids,p,p*(1-p),sum(A)==sum(B)))
    return ans

def verify():
    trials=0
    for a in range(1,25):
        for b in range(1,25):
            arr=(a,b,a+b)
            rows=scores(arr)
            ex=[x[2] for x in rows if x[3]]
            assert ex and max(x[2] for x in rows)==max(ex), (arr,rows)
            trials+=len(rows)
    for t in range(2,101):
        w=(1,2,t,t+3)
        rows=scores(w)
        A=F(t+3)**3/(F(t+4)*F(t+5)*F(2*t+3))
        B=F(3*t**3+24*t*t+58*t+33,3*(t+1)*(t+5)*(2*t+3))
        e=[x[2] for x in rows if x[3]]
        assert len(e)==1
        assert e[0]==A*(1-A)
        assert max(x[2] for x in rows)==max(A*(1-A),B*(1-B)),(t,rows)
        delta=B*(1-B)-A*(1-A)
        fact=F((3*t**3+2*t*t-46*t-33)*(6*t**3+46*t*t+103*t+51),9*(t+1)**2*(t+4)**2*(t+5)**2*(2*t+3)**2)
        assert delta == fact
        assert (delta>0)==(t>=4)
        trials+=len(rows)
    # Test the general asymptotic prefactor with rational convergence rather than
    # pretending that finite tests establish the limit.
    for a,b in [(1,2),(1,3),(2,3),(2,5),(3,8),(4,7)]:
        t=100000
        d=a+b+t
        pa=p_single(d,(a,b,t))
        pb=p_pair_above_pair(a,d,b,t)
        delta=pb*(1-pb)-pa*(1-pa)
        limit=F(a*(b-a),2)
        rel=abs(delta*t*t-limit)/limit
        assert rel < F(1,100)
        trials+=1
    print(f'PASS {trials} exact allocation comparisons and asymptotic spot checks')
    p=F(7)**3/(F(8)*F(9)*F(11))
    q=F(3*4**3+24*4**2+58*4+33,3*(4+1)*(4+5)*(2*4+3))
    print('four-good exact: ex-ante one-sided probability',p,'alternative',q)
    print('exact EF probability improvement',q*(1-q)-p*(1-p))

if __name__=='__main__':verify()
