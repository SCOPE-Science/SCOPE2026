"""Reproduce the exact one-way dormant-seed corridor calculation.

Requires only the Python standard library.  Assertions complement the
analytic proof; randomized finite-horizon tests are not an infinite proof.
"""
import math
import random


def formula(q, stages, terminal_survival):
    if q == 1.0:
        return 0.0
    result = (1.0 - q) / (1.0 - terminal_survival*q)
    for survival, forward in stages:
        result *= survival * forward * q / (1.0 - survival*(1.0-forward)*q)
    return result


def aware(stages):
    result = 1.0
    for survival, forward in stages:
        result *= survival*forward/(1.0-survival*(1.0-forward))
    return result


def root_function(q, stages, terminal_survival):
    v = (1.0-q)*(1.0-terminal_survival*q)/q
    return v * sum(1.0/(1.0-survival*(1.0-forward)*q)
                   for survival,forward in stages) - (1.0-terminal_survival)


def optimal_q(stages, terminal_survival):
    assert len(stages) >= 1 and 0 <= terminal_survival < 1
    left, right = 0.0, 1.0
    for _ in range(85):
        mid = (left + right)*0.5
        if root_function(mid, stages, terminal_survival) > 0:
            left = mid
        else:
            right = mid
    return (left + right)*0.5


def forward_horizon(q, stages, terminal_survival, years=600):
    """Independent forward Markov recurrence, not the closed product."""
    mass = [0.0]*(len(stages)+1)
    mass[0] = 1.0
    completed = 0.0
    for _ in range(years):
        nxt = [0.0]*len(mass)
        for i,(survival,forward) in enumerate(stages):
            retained = mass[i] * q * survival
            nxt[i] += retained * (1.0-forward)
            nxt[i+1] += retained * forward
        completed += mass[-1]*(1.0-q)
        nxt[-1] += mass[-1]*q*terminal_survival
        mass = nxt
    return completed


def run():
    checks=0
    rng=random.Random(130817)
    for _ in range(400):
        n=rng.randint(1,8)
        stages=[(rng.uniform(.25,.85),rng.uniform(.12,.95)) for i in range(n)]
        s0=rng.uniform(.1,.85)
        q=rng.uniform(.03,.95)
        exact=formula(q,stages,s0)
        forward=forward_horizon(q,stages,s0,600)
        assert math.isclose(exact,forward,rel_tol=2e-11,abs_tol=3e-13)
        checks += 1
        optimum=optimal_q(stages,s0)
        assert 0<optimum<1
        assert abs(root_function(optimum,stages,s0))<5e-10
        assert formula(optimum,stages,s0)>formula(0.0,stages,s0)
        assert formula(optimum,stages,s0)>formula(1.0,stages,s0)
        for k in range(1,100):
            assert formula(optimum,stages,s0)+1e-14 >= formula(k/100,stages,s0)
            checks += 1
        for j in range(n):
            ext=stages[:j]+stages[j+1:]
            if ext:
                assert optimal_q(ext,s0)<optimum
            checks += 1
        assert formula(optimum,stages,s0)<aware(stages)
        checks += 1
    # Closed radical from the homogeneous five-site example.
    stages=[(.75,.5)]*5
    q=4*(36-math.sqrt(66))/123
    assert abs(q-optimal_q(stages,.75))<2e-14
    assert abs(formula(q,stages,.75)-0.010581862916081259)<2e-16
    assert abs(aware(stages)-.6**5)<1e-16
    checks+=3
    # Independent heterogeneous sequence: asymptotic K_n universality.
    stage_seq=[]
    for j in range(1,1201):
        a=math.sin(j*1.217)**2
        b=math.sin(j*.754)**2
        stage_seq.append((.6+.18*a,.32+.4*b))
    for n in [300,600,1200]:
        seq=stage_seq[:n]
        s0=.63
        q=optimal_q(seq,s0)
        K=sum(1/(1-s*(1-p)) for s,p in seq)
        assert abs((1-q)*K-1)<.03
        logratio=math.log(1-q)-math.log(1-s0*q)
        logratio+=sum(math.log(q)+math.log(1-s*(1-p))
                       -math.log(1-s*(1-p)*q) for s,p in seq)
        scaled=math.exp(logratio)*math.e*(1-s0)*K
        assert abs(scaled-1)<.04, (n,scaled)
        checks+=2
    # Singular terminal-survival boundary: no germination hazard while waiting.
    for q in [.1,.3,.5,.7,.9]:
        stages=[(.8,.5)]*4
        v=math.prod(s*p*q/(1-s*(1-p)*q) for s,p in stages)
        assert v<math.prod(s*p*.999/(1-s*(1-p)*.999) for s,p in stages)
        checks+=1
    print(f"PASS: {checks} finite numerical checks; analytical proof supplied separately.")


if __name__=='__main__':
    run()
