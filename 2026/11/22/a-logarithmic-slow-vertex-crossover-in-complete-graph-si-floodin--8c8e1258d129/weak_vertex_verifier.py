"""Exact finite-state checks for an SI process with one low-susceptibility vertex.

Run with Python 3 (standard library only). The argument N is total vertices.
Ordinary-to-ordinary edge infection attempts occur at rate 1/N;
each edge incident to the distinguished vertex acts at rate rho/N.
"""
from fractions import Fraction


def last_probability_product(N, rho):
    rho = Fraction(rho)
    m = N - 1
    ans = Fraction(1)
    for j in range(1, m):
        ans *= Fraction(j, 1) / (Fraction(j, 1) + rho)
    return ans


def last_probability_dynamic(N, rho):
    """Forward transient CTMC state weights; no closed-product assumption."""
    rho = Fraction(rho)
    m = N - 1
    still_susceptible = Fraction(1)
    for k in range(1, m):
        ordinary_rate = Fraction(k * (m-k), N)
        weak_rate = rho * k / N
        still_susceptible *= ordinary_rate / (ordinary_rate + weak_rate)
    return still_susceptible


def mean_completion_time(N, rho):
    """Backward equations on the two-coordinate Markov chain."""
    rho = Fraction(rho)
    m = N - 1
    infected_weak = [Fraction(0) for _ in range(m+1)]
    susceptible_weak = [Fraction(0) for _ in range(m+1)]
    for k in range(m-1, 0, -1):
        rate = (Fraction(k) + rho) * (m-k) / N
        infected_weak[k] = 1 / rate + infected_weak[k+1]
    susceptible_weak[m] = N / (rho*m)
    for k in range(m-1, 0, -1):
        a = Fraction(k*(m-k),N)
        b = rho*k/N
        susceptible_weak[k] = (1+a*susceptible_weak[k+1]
                                    + b*infected_weak[k])/(a+b)
    return susceptible_weak[1]


def direct_generator_equations(N, rho):
    """Independent holding-time recursion for the mean, using an explicit matrix."""
    rho = Fraction(rho)
    m = N-1
    states = [(k,w) for k in range(1,m+1) for w in (0,1) if (k,w)!=(m,1)]
    # Each state has only successors with k increasing or w increasing.
    # This representation differs from the two-loop recursion above.
    value = {(m,1):Fraction(0)}
    for k,w in reversed(states):
        transitions = []
        if k<m:
            transitions.append(((k+1,w), (Fraction(k)+(rho if w else 0))*(m-k)/N))
        if not w:
            transitions.append(((k,1),rho*k/N))
        total = sum((rate for _,rate in transitions), Fraction(0))
        value[(k,w)] = (1+sum((rate*value[next_state] for next_state,rate in transitions),Fraction(0)))/total
    return value[(1,0)]


def run():
    checks = 0
    for N in range(3,14):
        for rho in (Fraction(1,7),Fraction(1,1),Fraction(3,2),Fraction(7,3)):
            assert last_probability_product(N,rho) == last_probability_dynamic(N,rho)
            assert mean_completion_time(N,rho) == direct_generator_equations(N,rho)
            if rho == 1:
                assert last_probability_product(N,rho) == Fraction(1,N-1)
            checks += 1
    print(f"PASS: {checks} exact rational cases; marked-last and full-chain mean checks")
    for N in (100,1000,10000,100000):
        from math import log,exp
        rho = 1/log(N)
        approx = exp(sum(-__import__('math').log1p(rho/j) for j in range(1,N-1)))
        print(f"N={N}: marked-last probability={approx:.6f}; limiting value={exp(-1):.6f}")

if __name__ == '__main__':
    run()
