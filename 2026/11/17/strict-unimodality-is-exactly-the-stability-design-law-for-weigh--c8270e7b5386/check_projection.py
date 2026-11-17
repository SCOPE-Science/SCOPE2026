"""Exact rational tests for weighted affine least-squares path-variation design."""
from fractions import Fraction as F
from itertools import product
from random import Random


def projection(t, mu, w, x):
    total = sum(mu)
    m = sum(a*b for a, b in zip(mu,t)) / total
    s = sum(mu_i*(t_i-m)**2 for mu_i,t_i in zip(mu,t))
    b = sum(mu_i*(t_i-m)*x_i for mu_i,t_i,x_i in zip(mu,t,x))/s
    a = sum(mu_i*x_i for mu_i,x_i in zip(mu,x))/total-b*m
    return [a+b*z for z in t]


def coefficients(t, mu, w):
    total = sum(mu)
    m = sum(a*b for a,b in zip(mu,t)) / total
    s = sum(mu_i*(t_i-m)**2 for mu_i,t_i in zip(mu,t))
    c = [sum(mu[j]*(t[j]-m) for j in range(i,len(t)))/s for i in range(1,len(t))]
    W = sum(w[i]*(t[i+1]-t[i]) for i in range(len(w)))
    return c, W*max(c_i/w_i for c_i,w_i in zip(c,w))


def tv(w, x):
    return sum(w_i*abs(x[i+1]-x[i]) for i,w_i in enumerate(w))


def admissible(t,w):
    signs=[(w[i-1]>w[i])-(w[i-1]<w[i]) for i in range(1,len(t)-1)]
    if signs.count(0)>1: return False
    for m in [*t[1:-1], *((t[i]+t[i+1])/2 for i in range(len(t)-1))]:
        if t[0]<m<t[-1] and all((s>0 and t[i]>m) or (s<0 and t[i]<m) or (s==0 and t[i]==m) for i,s in enumerate(signs,1)):
            return True
    return False


def design(t,w):
    if not admissible(t,w):return None
    delta=[-w[0]] + [w[i-1]-w[i] for i in range(1,len(t)-1)] + [w[-1]]
    candidates = [*t[1:-1], *((t[i]+t[i+1])/2 for i in range(len(t)-1))]
    for m in candidates:
        if not(t[0]<m<t[-1]): continue
        if all((v==0 and ti==m) or (v!=0 and ti!=m and (v/(ti-m))>0) for ti,v in zip(t,delta)):
            return [v/(ti-m) if v else F(1) for ti,v in zip(t,delta)]
    raise AssertionError('admissibility mismatch')


def main():
    checked=0; designed=0; nonadmissible=0
    for n in range(2,8):
        t=[F(2*i+(i*i)//4) for i in range(n)]
        for w_raw in product(range(1,4), repeat=n-1):
            w=list(map(F,w_raw)); mu=design(t,w)
            if mu is None:
                nonadmissible+=1
            else:
                designed+=1
                c,K=coefficients(t,mu,w)
                assert K==1, (n,w,mu,c,K)
                W=sum(w[i]*(t[i+1]-t[i]) for i in range(n-1))
                assert c==[wi/W for wi in w], (n,w,mu,c)
            checked+=1
    rng=Random(730991)
    for trial in range(3000):
        n=rng.randint(2,10)
        t=[F(0)]
        for i in range(n-1):t.append(t[-1]+F(rng.randint(1,8),rng.randint(1,4)))
        mu=[F(rng.randint(1,9),rng.randint(1,5)) for _ in t]
        w=[F(rng.randint(1,9),rng.randint(1,5)) for _ in range(n-1)]
        c,K=coefficients(t,mu,w)
        assert all(x>0 for x in c) and K>=1
        x=[F(rng.randint(-9,9), rng.randint(1,8)) for _ in range(n)]
        Px=projection(t,mu,w,x)
        assert tv(w,Px)<=K*tv(w,x)
        k=max(range(n-1),key=lambda j:c[j]/w[j])
        step=[F(int(i>k)) for i in range(n)]
        assert tv(w,projection(t,mu,w,step))==K*tv(w,step)
    print(f'EXACT_RATIONAL_ALL_WEIGHT_PATTERNS_PASS {checked} admissible={designed} nonadmissible={nonadmissible}')
    print('RANDOM_IRREGULAR_GRID_PROJECTION_AND_SHARP_STEP_PASS 3000')
    print('ALL_WEIGHTED_AFFINE_PATH_TESTS_PASS')

if __name__=='__main__':main()
