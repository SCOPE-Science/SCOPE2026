"""Independent exact-arithmetic checks for a scalar randomized-stage Langevin recurrence.
Standard Python 3 library only; see RESULT.md for all-parameter proofs.
"""
from fractions import Fraction as F
from math import sqrt


def q(t, a):
    return 1 - 2*a + t*t*a*a

def amp(t,a):
    return 1-t+t*t*a

def innov_var(t,a):
    return 2*t*(1-2*t*a+t*t*a)  # normalized curvature lambda=1

def fourth_cumulant(t, vals):
    # vals contains (alpha, probability), with calibrated stationary variance 1.
    a2 = sum(p*amp(t,a)**2 for a,p in vals)
    a4 = sum(p*amp(t,a)**4 for a,p in vals)
    g = sum(p*innov_var(t,a) for a,p in vals)
    g2 = sum(p*innov_var(t,a)**2 for a,p in vals)
    a2g = sum(p*amp(t,a)**2*innov_var(t,a) for a,p in vals)
    assert a2 < 1 and a4 < 1
    v = g/(1-a2)
    k = (6*a2g*v+3*g2)/(1-a4) - 3*v*v
    return v, k

def run():
    count = 0
    # Exact Pythagorean parameters make sqrt(1-t^2) rational.
    for u,v in [(3,4),(5,12),(8,15),(7,24),(20,21),(9,40)]:
        t=F(2*u*v,u*u+v*v)
        root=F(v*v-u*u,u*u+v*v) if v>u else F(u*u-v*v,u*u+v*v)
        # swap if needed to get real sqrt exactly.
        assert root*root == 1-t*t
        alpha=1/(1+root)
        assert 0<t<1 and F(1,2)<alpha<1
        assert q(t,alpha)==0
        assert amp(t,alpha)**2+innov_var(t,alpha)==1
        vv,kk=fourth_cumulant(t,[(alpha,F(1))]);assert vv==1 and kk==0
        count+=5
    for den in range(2,40):
        for num in range(1,den):
            t=F(num,den)
            p=1/(2-t*t)
            law=[(F(0),1-p),(F(1),p)]
            assert sum(prob*q(t,a) for a,prob in law)==0
            vv,k=fourth_cumulant(t,law)
            assert vv==1 and k>0
            e4=sum(prob*amp(t,a)**4 for a,prob in law)
            vq=sum(prob*q(t,a)**2 for a,prob in law)
            assert k == 3*t**4*vq/(1-e4)
            count+=5
    t=F(3,5);p=F(25,41)
    assert fourth_cumulant(t,[(F(0),1-p),(F(1),p)])==(F(1),F(3321,10498))
    count+=1
    # In anisotropic case, any exact mode calibration would force m_2=0,
    # but then m_1=0 and no calibration possible. Verify exact differences.
    for d in range(2,20):
        h=F(1,d)
        for k in range(2,11):
            # residual on lambda=2 vs lambda=1: 3 h^2 m2 (when lambda=1 eq 0)
            m2=F(k,2*k+1)
            e1=1-2*F(1,2)*(1+h*h*m2)+h*h*m2
            # use exact first-mode solution m1=(1+h^2m2)/2
            m1=(1+h*h*m2)/2
            assert 1-2*m1+(2*h)**2*m2 == 3*h*h*m2>0
            count+=1
    # Grid-supplement to analytic mixing optimum at t=1/sqrt(2).
    tstar=1/sqrt(2)
    def contraction(t): return 2-t-sqrt(1-t*t)
    for k in range(1,10000):
        t=k/10000
        assert contraction(t)>contraction(tstar)-1e-12
        count+=1
    print('PASS',count,'exact or supplementary numerical checks')
    print('rational nonconstant-stage kurtosis example: 3321/10498')
    print('calibrated contraction optimum: 2-sqrt(2) at t=1/sqrt(2)')

if __name__=='__main__':run()
