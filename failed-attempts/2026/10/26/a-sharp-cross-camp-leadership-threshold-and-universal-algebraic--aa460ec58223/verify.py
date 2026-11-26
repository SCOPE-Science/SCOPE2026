"""Independent arithmetic and ODE spot checks of a two-camp leadership theorem.
No package dependency beyond the Python standard library. Finite tests are not the proof.
"""
from fractions import Fraction as F
from math import exp, sqrt


def model_rhs(W, signs, anchor, s, z, rho):
    xx = [s * sign for sign in signs]
    aa = [anchor * sign for sign in signs]
    opin, leaders = [], []
    for i, row in enumerate(W):
        avg = sum(row[j] * xx[j] for j in range(len(signs)))
        mismatch = xx[i] - avg
        opin.append(-(1-z) * mismatch - z * (xx[i]-aa[i]))
        leaders.append(z*(1-z)*(rho*xx[i]*xx[i]-mismatch*mismatch))
    return opin, leaders


def reduced_rhs(s,z,a,kappa,rho):
    return (-((1-z)*kappa+z)*s+a*z, (rho-kappa*kappa)*s*s*z*(1-z))


def exact_tests():
    signs=[1,1,-1,-1]
    W=[[F(v,20) for v in row] for row in [
        [6,4,8,2], [2,8,4,6], [7,3,8,2], [2,8,6,4]]]
    assert all(sum(row)==1 for row in W)
    cross=[sum(row[j] for j,sg in enumerate(signs) if sg!=signs[i]) for i,row in enumerate(W)]
    assert cross == [F(1,2)]*4
    count=0
    for a in [F(1,3),F(3,4),F(1)]:
        for s in [F(1,10),F(2,5),F(3,5)]:
            for z in [F(1,10),F(1,3),F(3,4)]:
                for rho in [F(1,4),F(1),F(7,4),F(3)]:
                    f,g=model_rhs(W,signs,a,s,z,rho)
                    fs,gz=reduced_rhs(s,z,a,F(1),rho)
                    assert f==[sign*fs for sign in signs]
                    assert g==[gz]*4
                    count+=1
    # A three-vertex graph with nonuniform cross-camp exposure cannot
    # retain a common scalar signed opinion amplitude at positive finite time.
    sx=[1,1,-1]
    nonuniform=[[F(3,4),F(0),F(1,4)],
                [F(0),F(1,2),F(1,2)],
                [F(1,2),F(1,2),F(0)]]
    f,_=model_rhs(nonuniform,sx,F(2,3),F(2,3),F(1,2),F(1))
    assert f[0] != f[1]
    return count


def flow(t_end,h,kappa,rho,a=1.0,u=.5):
    s,z=a,u
    n=round(t_end/h)
    h=t_end/n
    def ff(S,Z):
        return reduced_rhs(S,Z,a,kappa,rho)
    for _ in range(n):
        k1,l1=ff(s,z)
        k2,l2=ff(s+h*k1/2,z+h*l1/2)
        k3,l3=ff(s+h*k2/2,z+h*l2/2)
        k4,l4=ff(s+h*k3,z+h*l3)
        s+=h*(k1+2*k2+2*k3+k4)/6
        z+=h*(l1+2*l2+2*l3+l4)/6
        assert 0<=s<=a+1.e-10 and 0<=z<=1+1.e-10
    return s,z


def numeric_tests():
    # Constant-leadership critical exact trajectory.
    kappa=F(3,2); a=F(4,5); u=F(2,5)
    c=float(kappa*(1-u)+u)
    s_inf=float(a*u/(kappa*(1-u)+u))
    s,z=flow(4,.005,float(kappa),float(kappa*kappa),float(a),float(u))
    assert abs(z-float(u))<1.e-12
    assert abs(s-(s_inf+(float(a)-s_inf)*exp(-c*4)))<1.e-11
    # An arbitrary positive conviction above the sharp threshold.
    s,z=flow(70,.1,1.,2.)
    assert s> .999999 and z>.999999
    # The subcritical neutralization is algebraic, with unit amplitude
    # at kappa=1, rho=1/2, a=1.
    s,z=flow(20000,.25,1.,.5)
    assert abs(s*sqrt(20000)-1)<.025,(s,z,s*sqrt(20000))
    assert abs(z*sqrt(20000)-1)<.025,(s,z,z*sqrt(20000))
    # The same asymptotic for a different kappa, anchor and initial leadership.
    kappa=F(3,2);rho=F(3,4);a=.7
    s,z=flow(20000,.2,float(kappa),float(rho),a,.3)
    B=sqrt(2*(float(kappa*kappa-rho)))
    assert abs(s*sqrt(20000)-1/B)<.03
    assert abs(z*sqrt(20000)-float(kappa)/(a*B))<.03


if __name__=='__main__':
    count=exact_tests()
    numeric_tests()
    print(f'PASS: {count} exact four-node vector-field comparisons; nonconstant cross-exposure countercheck; exact critical solution; four numerical asymptotic checks')
