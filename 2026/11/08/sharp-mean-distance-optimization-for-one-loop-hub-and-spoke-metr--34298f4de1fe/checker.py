"""Standalone numerical checks of the one-loop hub-and-spokes distance formulas.
Scientific calculations use uniformly arclength-distributed points; no external packages.
"""
import math
import random


def exact_mean(cycle, arms):
    ls = [float(x) for x in arms]
    C = float(cycle)
    L = C + sum(ls)
    S2 = sum(x*x for x in ls)
    S3 = sum(x*x*x for x in ls)
    I = C**3/4 + (C*C/2)*sum(ls) + L*S2 - (2/3)*S3
    return I/(L*L)


def formula_equilateral(k, L, t):
    return L*((1-t)**3/4 + t*(1-t)**2/2 + t*t/k-2*t**3/(3*k*k))


def optimum(k):
    return k*(k-4+2*math.sqrt(k*k-2*k+2))/(3*k*k-8)


def sample_graph_point(rng, cycle, arms):
    L=cycle+sum(arms)
    t = rng.random()*L
    if t < cycle: return (-1,t)
    t -= cycle
    for i,a in enumerate(arms):
        if t < a: return (i,t)
        t-=a
    return (len(arms)-1, arms[-1])


def distance(a,b,cycle):
    i,x=a; j,y=b
    if i == -1 and j == -1:
        d=abs(x-y); return min(d,cycle-d)
    if i == -1: return y+min(x,cycle-x)
    if j == -1: return x+min(y,cycle-y)
    return abs(x-y) if i==j else x+y


def main():
    rng=random.Random(708351)
    cases=[(.5,[.5]),(.3,[.4,.3]),(.45,[.07,.12,.16,.20]),(.2,[.16]*5)]
    for C,arms in cases:
        target=exact_mean(C,arms)
        N=140000
        sim=sum(distance(sample_graph_point(rng,C,arms),sample_graph_point(rng,C,arms),C) for _ in range(N))/N
        assert abs(sim-target)<.006,(C,arms,sim,target)
    for k in range(1,51):
        t=optimum(k)
        assert 0<t<1, (k,t)
        theoretical=exact_mean(1-t,[t/k]*k)
        assert abs(theoretical-formula_equilateral(k,1,t))<1e-12
        for u in [1e-5,.0001,.1,.2,.5,.8,.9,.999,1-1e-5]:
            assert formula_equilateral(k,1,u)+1e-11>=theoretical
        if k>=2:
            assert optimum(k)>optimum(k-1)
    for k in range(2,9):
        for _ in range(500):
            arms=[rng.random()+.02 for _ in range(k)]
            c=.8
            m=sum(arms)/k
            assert exact_mean(c,arms)+1e-12>=exact_mean(c,[m]*k)
    assert abs(formula_equilateral(1,1,optimum(1))-17/75)<1e-13
    print('ONE_LOOP_BOUQUET_OPTIMAL_MEAN_DISTANCE_OK')

if __name__=='__main__':main()
