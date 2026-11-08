"""Independent numerical checks for the stationary two-site OU reset model."""
import math
from scipy.integrate import quad


def p_age(x, rate, kappa, diffusivity, a):
    """Independent renewal-age integral; s=sqrt(t) removes the source singularity."""
    def integrand(s):
        if s == 0:
            # no evaluation at a source point in the tests
            return 0.
        t=s*s
        mu=a*math.exp(-kappa*t)
        var=-math.expm1(-2*kappa*t)*diffusivity/kappa
        return rate*math.exp(-rate*t)*2*s*sum(math.exp(-(x-sign*mu)**2/(2*var))/math.sqrt(2*math.pi*var) for sign in (-1,1))/2
    val,err=quad(integrand,0,math.sqrt(55/rate),epsabs=4e-10,epsrel=4e-9,limit=500)
    return val


def plateau(x,kappa,diffusivity,a):
    assert x>=0
    k=kappa/(2*diffusivity)
    C=k*math.exp(k*a*a)*math.sqrt(math.pi)/(2*math.sqrt(k))*math.erfc(math.sqrt(k)*a)
    if x<=a: return C
    return k*math.exp(k*a*a)*math.sqrt(math.pi)/(2*math.sqrt(k))*math.erfc(math.sqrt(k)*x)


def check():
    total=0
    for a in (.5,2.,5.):
        for r in (.3,1.,2.8):
            y=[p_age(x,r,1.,1.,a) for x in (0.,.12*a,.37*a,.65*a,.9*a,1.05*a,1.5*a,2*a)]
            if r<1:
                assert all(y[i]>y[i+1] for i in range(len(y)-1)),(a,r,y)
            elif r>1:
                assert all(y[i]<y[i+1] for i in range(4)),(a,r,y)
                assert y[4]>y[5] and y[5]>y[6]>y[7],(a,r,y)
            else:
                assert max(y[:5])-min(y[:5])<3e-7,(a,r,y)
                assert y[5]>y[6]>y[7]
                for x in (0.,.37*a,.9*a,1.5*a,2*a):
                    y1=p_age(x,r,1.,1.,a); y2=plateau(x,1.,1.,a)
                    assert abs(y1-y2)<3e-8,(a,x,y1,y2)
                    total+=1
            total+=1
    for kappa,diffusivity,a in ((1,1,2),(2,3,.4),(.4,1.5,4)):
        r=kappa
        C=plateau(0,kappa,diffusivity,a)
        mass_inside=2*a*C
        out=2*quad(lambda x:plateau(x,kappa,diffusivity,a),a,a+70*math.sqrt(diffusivity/kappa))[0]
        assert abs(mass_inside+out-1)<2e-8,(a,C,mass_inside,out)
        total+=1
        for rate in (.5*kappa,1.8*kappa):
            # independent first-principles age expectation of variance
            v=quad(lambda t:rate*math.exp(-rate*t)*(a*a*math.exp(-2*kappa*t)+(diffusivity/kappa)*(-math.expm1(-2*kappa*t))),0,math.inf)[0]
            formula=(rate*a*a+2*diffusivity)/(rate+2*kappa)
            assert abs(v-formula)<2e-8
            total+=1
    print(f"PASS {total} independent finite parameter checks")

if __name__=='__main__':check()
