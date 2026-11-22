"""Exact finite-null CDF for the two-sided argmax-standardized KS statistic.

For a uniform sample U_(1)<...<U_(n), let
K=max_i max(i/n-U_(i), U_(i)-(i-1)/n).
Choose the almost surely unique winning index r, and let V=K/sqrt(U_(r)(1-U_(r))).

cdf_exact(n,t) returns an exact algebraic SymPy expression for P(V<=t) when
n is a positive integer and t is a nonnegative rational number.  It uses
an exact piecewise-polynomial count recursion and algebraic integration limits.
No simulation or numerical quadrature is used for the returned value.
"""
from fractions import Fraction
from itertools import combinations
from math import factorial
import sympy as S

u = S.Symbol('u', real=True)

def chamber_breaks(n,j,side):
    a=S.Rational(j,n); b=S.Rational(j-1,n)
    k=(a-u) if side=='+' else (u-b)
    cut=S.Rational(2*j-1,2*n)
    lines=[S.Integer(0), S.Integer(1), u]
    for i in range(1,n+1):
        if i==j: continue
        lines += [S.Rational(i,n)-k, S.Rational(i-1,n)+k]
    lines=list(dict.fromkeys(S.expand(x) for x in lines))
    bounds={S.Integer(0),S.Integer(1),cut}
    for l,r in combinations(lines,2):
        slope=S.diff(l-r,u)
        if slope!=0:
            z=S.simplify(-(l-r).subs(u,0)/slope)
            if 0<z<1: bounds.add(z)
    out=sorted(bounds)
    return [(l,r) for l,r in zip(out,out[1:]) if (r<=cut if side=='+' else l>=cut)]

def volume_poly(n,j,side,chamber,which):
    left,right=chamber; q=(left+right)/2
    a=S.Rational(j,n); b=S.Rational(j-1,n)
    k=(a-u) if side=='+' else (u-b)
    indices=list(range(1,j)) if which=='L' else list(range(j+1,n+1))
    start=S.Integer(0) if which=='L' else u
    end=u if which=='L' else S.Integer(1)
    lo=start.subs(u,q) if hasattr(start,'subs') else start
    hi=end.subs(u,q) if hasattr(end,'subs') else end
    lines=[start,end]
    lowers={i:S.Rational(i,n)-k for i in indices}
    uppers={i:S.Rational(i-1,n)+k for i in indices}
    for i in indices: lines.extend([lowers[i],uppers[i]])
    lines=list(dict.fromkeys(S.expand(z) for z in lines))
    knots=[]
    for ln in lines:
        val=ln.subs(u,q)
        if lo<=val<=hi: knots.append(ln)
    knots=sorted(knots,key=lambda z:z.subs(u,q))
    m=len(indices)
    dp=[S.Integer(1)]+[S.Integer(0)]*m
    for l,r in zip(knots,knots[1:]):
        lv=l.subs(u,q); rv=r.subs(u,q)
        if lv==rv: continue
        allowed={pos for pos,i in enumerate(indices) if lowers[i].subs(u,q)<=lv and uppers[i].subs(u,q)>=rv}
        new=[S.Integer(0)]*(m+1)
        delta=S.expand(r-l)
        for c in range(m+1):
            if dp[c]==0:continue
            new[c]+=dp[c]
            for step in range(1,m-c+1):
                if c+step-1 not in allowed: break
                new[c+step]+=dp[c]*delta**step/S.factorial(step)
        dp=[S.expand(z) for z in new]
    return S.expand(dp[m])

def exact_compare(a,b):
    sign=S.sign(S.simplify(a-b))
    if sign not in (-1,0,1):
        raise ArithmeticError('unable to certify exact algebraic comparison')
    return int(sign)

def cdf_exact(n,t, detail=False):
    assert isinstance(n,int) and n>=1
    t=S.Rational(t)
    if t<=0: return S.Integer(0)
    total=S.Integer(0)
    parts=[]
    for j in range(1,n+1):
        for side in ('+','-'):
            offset=S.Rational(j,n) if side=='+' else S.Rational(j-1,n)
            # both k=offset-u or u-offset; their squares are equal
            roots=[(2*offset+t**2 + sign*t*S.sqrt(t**2+4*offset*(1-offset)))/(2*(1+t**2)) for sign in (-1,1)]
            for lo,hi in chamber_breaks(n,j,side):
                L=lo if exact_compare(lo,roots[0])>=0 else roots[0]
                R=hi if exact_compare(hi,roots[1])<=0 else roots[1]
                if exact_compare(R,L)<=0: continue
                poly=S.Poly(volume_poly(n,j,side,(lo,hi),'L')*volume_poly(n,j,side,(lo,hi),'R'),u)
                primitive=sum(coeff*u**(power[0]+1)/(power[0]+1) for power,coeff in poly.terms())
                term=S.expand(primitive.subs(u,R)-primitive.subs(u,L))
                total+=term
                if detail:parts.append((j,side,lo,hi,str(poly.as_expr()),str(term)))
    out=S.factorial(n)*total
    if detail: return S.simplify(out),parts
    return S.simplify(out)

def direct_stat(x):
    from math import sqrt
    n=len(x); s=sorted(x)
    triples=[(max((i+1)/n-ui,ui-i/n),i) for i,ui in enumerate(s)]
    k,r=max(triples)
    return k/sqrt(s[r]*(1-s[r]))

if __name__=='__main__':
    import argparse,time
    pa=argparse.ArgumentParser();pa.add_argument('n',type=int);pa.add_argument('t',type=str);a=pa.parse_args()
    st=time.time();v=cdf_exact(a.n,S.Rational(a.t))
    print('n=',a.n,'t=',a.t,'cdf exact=',v)
    print('cdf decimal=',S.N(v,20),'seconds=',round(time.time()-st,2))
