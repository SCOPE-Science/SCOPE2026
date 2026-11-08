"""Independent exact-rational checks of a weighted-biclique two-leader theorem.
Python >=3.9, standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations


def poly(p,q,t):
    d=q-p
    A0=q*q*((p-2)*d*d+(2*p*p-3*p+2)*d+2*p*p)
    A1=q*((2*p-7)*d*d+(4*p*p-10*p+7)*d+p*(6*p+1))
    A2=(p-6)*d*d+(2*p-3)*(p-2)*d+4*p*p
    return A0 + A1*t + A2*t*t


def alpha2(p,q):
    d=q-p
    return (p-6)*d*d+(2*p-3)*(p-2)*d+4*p*p


def J0(p,q,a,b):
    l=p-a;r=q-b;D=p*q-l*r
    assert D>0
    return F(l,q)+F(r,p)+F(l*r*(p+q),p*q*D)


def diag_reduction(p,q,a,b,t):
    l=p-a;r=q-b;D=p*q-l*r
    alpha=F(r,q*D)
    g=F(1,q)+alpha
    norm=F(1,q*q)+2*alpha/q+l*alpha*alpha+F(r,D*D)
    return t*norm/(1+t*g)


def same_reduction(q,t):
    return 2*t/(q*(q+2*t))


def formula(p,q,t,kind):
    assert p>=3 and q>=p and t>0
    if kind=='SS':return J0(p,q,2,0)
    if kind=='AS':return J0(p,q,2,0)-diag_reduction(p,q,2,0,t)
    if kind=='AA':return J0(p,q,2,0)-same_reduction(q,t)
    if kind=='AB':return J0(p,q,1,1)-same_reduction(q,t)
    if kind=='BS':return J0(p,q,1,1)-diag_reduction(p,q,1,1,t)
    if kind=='BB':return J0(p,q,0,2)-same_reduction(q,t)
    raise ValueError(kind)


def gauss_trace(A):
    n=len(A)
    M=[[F(v) for v in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        piv=next(i for i in range(k,n) if M[i][k])
        M[k],M[piv]=M[piv],M[k]
        f=M[k][k];M[k]=[v/f for v in M[k]]
        for i in range(n):
            if i!=k:
                f=M[i][k]
                if f:M[i]=[x-f*y for x,y in zip(M[i],M[k])]
    return sum(M[i][n+i] for i in range(n))


def brute(p,q,t,s):
    n=p+q
    L=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(p):
        for j in range(p,n):
            L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    L[0][0]+=t;L[1][1]+=t;L[0][1]-=t;L[1][0]-=t
    rest=[i for i in range(n) if i not in s]
    return gauss_trace([[L[i][j] for j in rest] for i in rest])


def cls(p,s):
    to=lambda i:'S' if i<2 else ('A' if i<p else 'B')
    return ''.join(sorted(to(i) for i in s))


def expected(p,q,t):
    f=poly(p,q,t)
    return {'AS'} if f>0 else ({'BS'} if f<0 else {'AS','BS'})


def main():
    tested=0
    # All two-leader pairs for small instances, not just symmetry representatives.
    for p in range(3,6):
        for q in range(p,9):
            for t in [F(1,3),F(1),F(24),F(100)]:
                values={}
                for s in combinations(range(p+q),2):
                    kind=cls(p,s)
                    got=brute(p,q,t,s)
                    assert got==formula(p,q,t,kind),(p,q,t,s,got,formula(p,q,t,kind))
                    values[s]=got;tested+=1
                vmin=min(values.values())
                types={cls(p,s) for s,val in values.items() if val==vmin}
                assert types==expected(p,q,t),(p,q,t,types,expected(p,q,t))
    # Exact polynomial comparison identity and class domination on larger parameter grids.
    algebra=0
    for p in range(3,12):
        for q in range(p,65):
            for t in [F(1,7),F(1),F(24),F(100),F(10000)]:
                den=p*q*(2*q+3*t)*(p*q+q*q-q+(p+2*q-2)*t)
                assert formula(p,q,t,'BS')-formula(p,q,t,'AS')==poly(p,q,t)/den
                kinds=['SS','AS','AB','BS','BB']+(['AA'] if p>=4 else [])
                vals={k:formula(p,q,t,k) for k in kinds}
                opt=min(vals.values())
                assert {k for k in kinds if vals[k]==opt}==expected(p,q,t)
                algebra+=1
    assert alpha2(3,7)==0 and alpha2(3,8)<0
    assert alpha2(4,12)>0 and alpha2(4,13)<0
    assert alpha2(5,30)==0 and alpha2(5,31)<0
    assert all(alpha2(p,q)>0 for p in range(6,15) for q in range(p,200))
    assert poly(3,9,F(24))==0
    assert formula(3,9,F(24),'AS')==F(46,15)
    print('PASS:',tested,'exact full grounded-inverse pair comparisons;',algebra,'exact symbolic-formula/optimizer grid checks; all boundary checks')

if __name__=='__main__':main()
