"""Diagnostic checks for a half-normal line-transect information design.

Run: python checker.py. Only Python's standard library is needed.
The mathematical uniqueness proof is in RESULT.md, not in this script.
"""
from math import erf, exp, sqrt, pi, isclose

def moments(a):
    assert a > 0
    e = exp(-a*a/2)
    j0 = sqrt(pi/2) * erf(a/sqrt(2))
    j2 = j0 - a*e
    j4 = 3*j2 - a**3*e
    return j0, j2, j4

def gram(a):
    j0,j2,j4=moments(a)
    return j0*j4-j2*j2

def gram_prime(a):
    j0,j2,j4=moments(a)
    return exp(-a*a/2)*(j4-2*a*a*j2+a**4*j0)

def elasticity(a):
    return a*gram_prime(a)/gram(a)

def optimum(kappa):
    lo,hi=.25,15.
    for _ in range(80):
        mid=(lo+hi)/2
        if elasticity(mid)>2*mid/(kappa+mid):lo=mid
        else:hi=mid
    return (lo+hi)/2

def run():
    count=0
    # Full-rank, positive derivative, and decreasing elasticity on a diagnostic grid.
    vals=[]
    for i in range(2,301):
        a=i/50
        f,fp=gram(a),gram_prime(a)
        assert f>0 and fp>0;count+=2
        vals.append(elasticity(a))
        # Differentiation identity checked against centered differences.
        eps=1e-5
        fd=(gram(a+eps)-gram(a-eps))/(2*eps)
        assert abs(fd-fp)<2e-5*max(1,abs(fp));count+=1
    for left,right in zip(vals,vals[1:]):
        assert left>right;count+=1
    ref=[(0,2.4834032294617278),(.2,2.551327335944169),
         (1,2.7441753329137435),(5,3.1663319905717625),
         (100,4.152682610731369)]
    for k,desired in ref:
        root=optimum(k)
        assert abs(root-desired)<1e-8;count+=1
        assert abs(elasticity(root)-2*root/(k+root))<1e-10;count+=1
        for factor in [.1,.3,.5,.8,.95,1.05,1.2,1.5,2,3]:
            a=root*factor
            assert gram(root)/(k+root)**2>gram(a)/(k+a)**2;count+=1
    assert all(optimum(ref[i][0])<optimum(ref[i+1][0]) for i in range(len(ref)-1));count+=1
    # Exact small-a leading coefficient and large-a limit (numerical diagnostics).
    assert abs(gram(.1)/(.1**6)-4/45)<1e-3;count+=1
    assert abs(gram(12)-pi)<1e-7;count+=1
    print(f"PASS: {count} diagnostic assertions")
if __name__=='__main__':run()
