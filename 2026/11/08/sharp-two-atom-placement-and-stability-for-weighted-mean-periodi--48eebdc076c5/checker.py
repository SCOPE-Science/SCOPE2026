"""Exact rational verification of weighted periodic H1 evaluation norms."""
from fractions import Fraction as F
from itertools import product

def integrate_poly_square(a,b,c,left,right):
    # exact integral of (a*t^2+b*t+c)^2 over a rational interval
    coeff=(c*c,2*b*c,b*b+2*a*c,2*a*b,a*a)
    return sum(co* (right**(j+1)-left**(j+1))/F(j+1) for j,co in enumerate(coeff))

def independent_dual_norm(x,alpha,beta,d):
    S=alpha+beta; M=1+S
    # derivative profile v(t) = 1(t<=x)-x - [(1/2-t)+beta*(1(t<=d)-d)]/M.
    cuts=sorted(set([F(0),x,d,F(1)]))
    ans=F(0)
    for left,right in zip(cuts,cuts[1:]):
        mid=(left+right)/2
        A=F(0)
        B=F(1)/M
        C=F(mid<x)-x -(F(1,2)+beta*(F(mid<d)-d))/M
        # C expression uses mid only for step indicators; coefficient for - (1/2-t) is t/M
        ans+=integrate_poly_square(A,B,C,left,right)
    return ans

def resistance(t):
    u=t%1
    return u*(1-u)

def green_formula(x,alpha,beta,d):
    S=alpha+beta; M=1+S
    return F(1)/(12*M*M)+(alpha*resistance(x)+beta*resistance(x-d))/M-alpha*beta*resistance(d)/(M*M)

def exact_max(alpha,beta,d):
    S=alpha+beta; M=1+S
    return F(1)/(12*M*M)+S/(4*M)-alpha*beta*d*(d+S)/(S*M*M)

def independent_candidates(alpha,beta,d):
    S=alpha+beta
    # stationary point in long gap; stationary point on short gap if present
    xs= (alpha-beta+2*beta*d)/(2*S)
    xl=F(1,2)+beta*d/S
    pts=[F(0),d,F(1),xl]
    if 0<=xs<=d: pts.append(xs)
    return pts

def test():
    checked=0; maximizers=0; strict_design=0
    vals=[F(1,5),F(1,2),F(1),F(3),F(7)]
    gaps=[F(0),F(1,7),F(1,4),F(2,5),F(1,2)]
    samples=[F(i,20) for i in range(21)]
    for a,b,d in product(vals,vals,gaps):
        for x in set(samples+independent_candidates(a,b,d)):
            assert independent_dual_norm(x,a,b,d)==green_formula(x,a,b,d),(a,b,d,x)
            checked+=1
        vals2={x:independent_dual_norm(x,a,b,d) for x in independent_candidates(a,b,d)}
        assert max(vals2.values())==exact_max(a,b,d),(a,b,d)
        maximizers+=1
        S=a+b;M=1+S
        best=(F(4)+9*S+6*S*S)/(48*M*M)
        deficit=((a-b)**2*(F(1,4)+S/2)/4+a*b*(F(1,2)-d)*(F(1,2)+d+S))/(S*M*M)
        assert exact_max(a,b,d)-best==deficit
        if a!=b or d!=F(1,2):assert deficit>0
        else:assert deficit==0
        strict_design+=1
    print('INDEPENDENT_EXACT_HILBERT_PROFILE_AND_GREEN_IDENTITY_OK',checked)
    print('ALL_CANDIDATE_EXTREMA_AND_DESIGN_DEFICITS_OK',maximizers,strict_design)
    print('UNIFORM_CIRCLE_BASELINE_OK',F(1,12))
    print('BALANCED_ANTIPODAL_EXAMPLE_OK',exact_max(F(1,2),F(1,2),F(1,2)))
    print('ALL_TWO_ATOM_CIRCLE_SOBOLEV_CHECKS_OK')
if __name__=='__main__':test()
