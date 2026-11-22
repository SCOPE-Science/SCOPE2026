"""Independent numerical checks for the continuum semi-open Glauber correlation bound.
Requires only Python 3 standard library. Tests are consistency checks, not proof.
"""
import math

PI = math.pi

def exact_fourier(length, x, time, terms=360):
    assert 0 < x < length and time > 0
    z = x / length
    factor = PI * PI * time / (2 * length * length)
    return 1 - z - (2 / PI) * sum(math.sin(n * PI * z) * math.exp(-factor * n*n)/n
                                   for n in range(1, terms+1))

def exact_images(length, x, time, shells=15):
    assert 0 < x < length and time > 0
    h = math.sqrt(2*time)
    return sum(math.copysign(math.erfc(abs(x+2*k*length)/h), x+2*k*length)
               for k in range(-shells, shells+1))

def shortcut(length, x, time):
    return (math.erfc(x/math.sqrt(2*time))-math.erfc(length/math.sqrt(2*time))) / math.erf(length/math.sqrt(2*time))

def profile(length, x):
    return 1 - x / length

def coefficient(length, x):
    return x*(length*length-x*x)/(6*length)

def integrated_exact(length, x):
    return x*(length-x)*(2*length-x)/(3*length)

def forcing(length, x, time):
    z = x/math.sqrt(2*time)
    a = length/math.sqrt(2*time)
    return math.erf(z) * a*math.exp(-a*a)/(math.sqrt(PI)*time*math.erf(a)**2)

def simpson(f, left, right, steps):
    assert steps % 2 == 0
    h = (right-left)/steps
    return h/3*(f(left)+f(right)+4*sum(f(left+i*h) for i in range(1,steps,2))
                +2*sum(f(left+i*h) for i in range(2,steps,2)))

def run():
    checks = 0
    for length in (0.7, 1., 2.3):
        for z in (.13, .31, .56, .83):
            x = z*length
            for s in (.035, .08, .16, .31, .65, 1.25):
                time = s*length*length
                u = exact_fourier(length,x,time)
                ui = exact_images(length,x,time)
                v = shortcut(length,x,time)
                assert abs(u-ui)<3e-12, (length,z,s,u,ui)
                assert u-v > 0, (length,z,s,u,v)
                bound = math.erfc(length/math.sqrt(2*time))/math.erf(length/math.sqrt(2*time))
                assert u-v < bound, (length,z,s,u,v,bound)
                assert 0 < u < profile(length,x), (length,z,s,u)
                assert 0 < v < profile(length,x), (length,z,s,v)
                checks += 5
    for z in (.2,.5,.8):
        length = 1.7
        x = z*length
        # The explicit Fourier heat solution must have the predicted finite
        # time-integrated deficit.
        integral = simpson(lambda t: profile(length,x)-exact_fourier(length,x,t)
                           if t else profile(length,x), 0., 10*length*length, 8000)
        assert abs(integral-integrated_exact(length,x)) < 2e-7, (z,integral,integrated_exact(length,x))
        checks += 1
        # The shortcut's long-time bias has the exact positive coefficient.
        for s in (250.,1000.,4000.):
            t=s*length*length
            actual = t*(exact_fourier(length,x,t)-shortcut(length,x,t))
            predicted = coefficient(length,x)
            assert abs(actual/predicted-1)<.009, (z,s,actual,predicted)
            checks += 1
        # The early bias is asymptotically the probability of hitting the far end.
        for s in (.0025,.0035,.005):
            t=s*length*length
            eps_n = math.erfc(length/math.sqrt(2*t))
            eps_x = math.erfc(x/math.sqrt(2*t))
            # exact_images = eps_x - delta; use stable image corrections.
            delta = eps_x-exact_images(length,x,t)
            # At these times delta may underflow by cancellation; its correct
            # leading contribution is the positive image at distance 2N-x.
            delta_image = math.erfc((2*length-x)/math.sqrt(2*t))
            assert delta >= -1e-15
            leading = (eps_n*(1-eps_x)/(1-eps_n)-delta_image)/eps_n
            assert .98 < leading <= 1.0001, (z,s,leading)
            checks += 1
    # Residual of the non-solution: (partial_t - (1/2)partial_xx)v = -forcing.
    for x in (.18,.43,.76):
        for t in (.19,.37,.8):
            h=1e-4
            lhs = ((shortcut(1,x,t+h)-shortcut(1,x,t-h))/(2*h)
                   - (shortcut(1,x+h,t)-2*shortcut(1,x,t)+shortcut(1,x-h,t))/(2*h*h))
            assert forcing(1,x,t)>0
            assert abs(lhs+forcing(1,x,t)) < 2e-7, (x,t,lhs,forcing(1,x,t))
            checks+=2
    # The long-time coefficient has unique interior maximizer N/sqrt(3).
    n = 1.5
    xmax = n/math.sqrt(3)
    assert abs(coefficient(n,xmax)-n*n/(9*math.sqrt(3)))<1e-13
    assert all(coefficient(n,xmax)>coefficient(n,x) for x in (.1*n,.2*n,.5*n,.9*n))
    checks+=2
    print(f"PASS: {checks} independent scalar consistency checks; spectral, image, residual, asymptotic and integral comparisons")
if __name__ == '__main__':
    run()
