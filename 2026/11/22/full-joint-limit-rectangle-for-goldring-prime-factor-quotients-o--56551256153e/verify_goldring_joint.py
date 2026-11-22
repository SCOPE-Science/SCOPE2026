"""Independent arithmetic checks for the Goldring joint-limit parameterisation.

These finite tests do not prove the infinite prime-pattern theorem; the
latter is supplied by the cited Green--Tao theorem and the six-form lemma.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import isclose


def largest_prime_factor(n):
    if n <= 1:
        return 1
    answer = 1
    d = 2
    while d * d <= n:
        while n % d == 0:
            answer = d
            n //= d
        d += 1
    return max(answer, n)


def prime(n):
    return n > 1 and largest_prime_factor(n) == n


def arithmetic_case(m, x, y, z):
    p, q, r = m*x + m*y - z, m*x - m*y + z, -m*x + m*y + z
    if min(p, q, r, x, y, z) <= 2 or len({p, q, r}) < 3 or len({x, y, z}) < 3:
        return False
    if not all(prime(a) for a in (p, q, r, x, y, z)):
        return False
    if min(x, y, z) < largest_prime_factor(2*m):
        return False
    w = largest_prime_factor(p+q)*largest_prime_factor(p+r)*largest_prime_factor(q+r)
    assert w == x*y*z
    assert F(largest_prime_factor(w), max(p,q,r)) == F(max(x,y,z),max(p,q,r))
    assert F(w,p*q*r) == F(x*y*z,p*q*r)
    return True


def exact_real_centres():
    # All three factors of input/output are positive, with a strictly
    # positive margin at each chosen rational six-form centre.
    cases = [
        (2, F(1), F(1,2), F(1,4), 'A'),
        (3, F(1), F(1,2), F(1,4), 'B'),
        (5, F(1), F(1,7), F(1,13), 'A'),
        (4, F(1), F(7,8), F(1,8), 'B'),
    ]
    for m, p, q, r, orientation in cases:
        if orientation == 'A':
            x,y,z=(p+q)/(2*m),(p+r)/(2*m),(q+r)/2
            assert (p,q,r)==(m*x+m*y-z,m*x-m*y+z,-m*x+m*y+z)
        else:
            x,y,z=(p+q)/2,(p+r)/(2*m),(q+r)/(2*m)
            # The swapped orientation has two multiplier-m edges through r.
            assert p==x+m*y-m*z and q==x-m*y+m*z and r==-x+m*y+m*z
        R=max(x,y,z)/max(p,q,r)
        S=x*y*z/(p*q*r)
        assert 0<R<=1 and S>0
        if (m,p,q,r,orientation)==(3,F(1),F(1,2),F(1,4),'B'):
            assert R==F(3,4) and S==F(5,32)
    return len(cases)


def continuous_params(alpha,beta):
    # Test IVT centres numerically; proof works with arbitrary real values.
    assert 0<alpha<=1 and beta>0
    if alpha<=0.5:
        m=2
        while (1+alpha)**2/(4*m*m*alpha)>=beta or (1+2*alpha)/(2*m)>alpha:
            m+=1
        def val(v):
            u=2*alpha-v
            return alpha*(1+u)*(1+v)/(4*m*m*u*v)
        lo,hi=0.0,alpha
        for _ in range(155):
            v=(lo+hi)/2
            if val(v)>beta:lo=v
            else:hi=v
        v=(lo+hi)/2;u=2*alpha-v
        p,q,r=1.0,u,v
        x,y,z=(1+u)/(2*m),(1+v)/(2*m),(u+v)/2
    else:
        u=2*alpha-1
        m=2
        while alpha**2/(m*m*u)>=beta:
            m+=1
        def val(v): return alpha*(1+v)*(u+v)/(4*m*m*u*v)
        lo,hi=0.0,u
        for _ in range(155):
            v=(lo+hi)/2
            if val(v)>beta:lo=v
            else:hi=v
        v=(lo+hi)/2
        p,q,r=1.0,u,v
        x,y,z=alpha,(1+v)/(2*m),(u+v)/(2*m)
    assert min(p,q,r,x,y,z)>0
    assert isclose(max(x,y,z)/max(p,q,r),alpha,rel_tol=1e-12,abs_tol=1e-12)
    assert isclose(x*y*z/(p*q*r),beta,rel_tol=1e-10,abs_tol=1e-10)
    return m


def complexity_check():
    # The exact six-form coefficient vectors and the three classes of
    # the OTHER five indices for each distinguished form (0-based).
    patterns=[
        ([1],[2,3],[4,5]),
        ([0],[2,3],[4,5]),
        ([0],[1,4],[3,5]),
        ([0],[1,2],[4,5]),
        ([0],[1,2],[3,5]),
        ([0],[1,2],[3,4]),
    ]
    def det(a,b,c):
        return (a[0]*(b[1]*c[2]-b[2]*c[1])
              - a[1]*(b[0]*c[2]-b[2]*c[0])
              + a[2]*(b[0]*c[1]-b[1]*c[0]))
    counter=0
    for m in range(1,26):
        v=[(1,0,0),(0,1,0),(0,0,1),
           (m,m,-1),(m,-m,1),(-m,m,1)]
        for i,(single,pair1,pair2) in enumerate(patterns):
            assert len({i,*single,*pair1,*pair2})==6
            # Each pair cannot span its distinguished vector.
            assert det(v[i],v[pair1[0]],v[pair1[1]])!=0
            assert det(v[i],v[pair2[0]],v[pair2[1]])!=0
            # Singleton vector not proportional.
            a,b=v[i],v[single[0]]
            assert (a[1]*b[2]-a[2]*b[1],
                    a[2]*b[0]-a[0]*b[2],
                    a[0]*b[1]-a[1]*b[0])!=(0,0,0)
            counter+=1
    return counter


def local_check():
    primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
    cases=0
    for m in range(1,26):
        for ell in primes:
            candidates=[a for a in range(ell) if a%ell and (2*m*a-1)%ell]
            assert candidates
            a=candidates[0]
            forms=[a,a,1,2*m*a-1,1,1]
            assert all(v%ell for v in forms)
            cases+=1
    return cases


def main():
    exact=exact_real_centres()
    local=local_check()
    complexity=complexity_check()
    samples=[(a,b) for a in [0.0003,.01,.1,.25,.5,.51,.7,.75,.99,1.0]
                   for b in [0.0001,.01,.1,1.,10000.]]
    for a,b in samples:
        continuous_params(a,b)
    primes=[j for j in range(3,73) if prime(j)]
    found=0
    for m in (1,2,3,5):
        for x in primes:
            for y in primes:
                for z in primes:
                    if arithmetic_case(m,x,y,z):
                        found+=1
                        break
                if found>=m: break
            if found>=m:break
        # At least one pattern for each chosen m.
        assert any(arithmetic_case(m,x,y,z) for x in primes for y in primes for z in primes)
    print(f'GOLDRING_JOINT_PARAM_OK rational_centres={exact} local_checks={local} complexity_rows={complexity} real_targets={len(samples)} sample_prime_patterns>=4')

if __name__=='__main__': main()
