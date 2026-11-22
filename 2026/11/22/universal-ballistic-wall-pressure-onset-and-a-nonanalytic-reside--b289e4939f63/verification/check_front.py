"""Self-contained checks for the two-wall ballistic onset and fractional cusp."""
import math
import random


def quadrature(fn, a, b, n=10000):
    h = (b - a) / n
    return h * (fn(a) + fn(b) + 4 * sum(fn(a + (2*j-1)*h) for j in range(1, n//2+1)) + 2 * sum(fn(a+2*j*h) for j in range(1, n//2))) / 3


def beta_hold(beta, rng):
    return rng.random() ** (1.0 / beta)


def conditional_sim(beta0, beta1, v, L, gamma, eps, n, seed):
    rng = random.Random(seed)
    tmax = L / v + eps
    count = 0
    # Observe the left wall at stationarity. The length-biased sojourn has
    # Beta(beta0+1,1) law; a uniform point in that sojourn gives the residual.
    for _ in range(n):
        hold_length = rng.random() ** (1.0 / (beta0 + 1.0))
        residual = rng.random() * hold_length
        t = residual
        if t >= tmax:
            continue
        x, direction = 0.0, 1
        for events in range(80):
            time_to_wall = (L-x)/v if direction == 1 else x/v
            time_to_flip = rng.expovariate(gamma)
            if t + min(time_to_wall, time_to_flip) >= tmax:
                break
            if time_to_flip < time_to_wall:
                x += direction * v * time_to_flip
                t += time_to_flip
                direction = -direction
                continue
            x = L if direction == 1 else 0.0
            t += time_to_wall
            hold = beta_hold(beta1 if direction == 1 else beta0, rng)
            if t + hold >= tmax:
                if direction == 1:
                    count += 1
                break
            t += hold
            direction = -direction
        else:
            raise RuntimeError('Unexpected event-loop length')
    return count/n


def run():
    # Exact non-Markov wall laws: F_i(s)=s**beta_i on 0<=s<=1.
    b0, b1 = .5, .75
    mean0, mean1 = b0/(b0+1), b1/(b1+1)
    L, v, gamma = 1.0, 1.0, .5
    tau = L/v
    c = 1/(2*L+v*(mean0+mean1))
    q0, q1 = v*c*mean0, v*c*mean1
    assert abs(2*L*c+q0+q1-1)<1.e-14
    assert abs(q0/mean0-v*c)<1.e-14 and abs(q1/mean1-v*c)<1.e-14
    beta_coeff = math.gamma(1+b0)*math.gamma(1+b1)/math.gamma(2+b0+b1)
    for eps in (.025, .05, .1, .2, .4):
        direct = quadrature(lambda s: (1-s**b0)*(1-(eps-s)**b1), 0, eps)
        exact = (eps - eps**(1+b0)/(1+b0) - eps**(1+b1)/(1+b1)
                 + beta_coeff * eps**(1+b0+b1))
        assert abs(direct-exact) < 2.e-8
    # The coefficient of the 1+min(beta) noninteger cusp is exact, even
    # with different wall distributions (the other power is higher).
    for eps in (1.e-4, 1.e-5, 1.e-6, 1.e-7):
        exact = (eps - eps**1.5/1.5 - eps**1.75/1.75
                 + beta_coeff*eps**2.25)
        ratio = (exact-eps)/(eps**1.5)
        assert abs(ratio+2/3) < 1.0 * eps**.25
    # Independent Markovian subcase: closed elementary convolution.
    for mu0, mu1 in ((1., 1.), (.4, 2.), (1.1, .6)):
        for eps in (.03, .2, .6):
            quad = quadrature(lambda s: math.exp(-mu0*s-mu1*(eps-s)), 0, eps)
            closed = eps*math.exp(-mu0*eps) if mu0==mu1 else (math.exp(-mu1*eps)-math.exp(-mu0*eps))/(mu0-mu1)
            assert abs(quad-closed)<1.e-10
    # Independently simulate the physical finite-speed process, no use of
    # the direct-path integral in the sampler. The direct path is a subset.
    for eps, n, seed in ((.10, 220000, 172), (.20, 220000, 173)):
        direct = (eps - eps**1.5/1.5 - eps**1.75/1.75 + beta_coeff*eps**2.25)
        lower = (v*c*math.exp(-gamma*tau)*direct)/q0
        estimate = conditional_sim(b0, b1, v, L, gamma, eps, n, seed)
        se = math.sqrt(max(.001, estimate*(1-estimate))/n)
        # Front correction from atypically fast reversals is O(eps**2).
        assert estimate >= lower - 5*se, (eps, estimate, lower)
        assert estimate <= lower + 6*eps*eps + 5*se, (eps,estimate,lower)
        print('eps=',eps,'conditional_sim=',round(estimate,7),'direct_lower=',round(lower,7),'SE=',round(se,7))
    print('PASS: stationary renewal normalization, fractional front, Markov reduction, direct stochastic trajectories')


if __name__ == '__main__':
    run()
