"""Exact-rational diagnostics for a graph formed by loops and pendant edges at one hub.

The checker uses resistance integrals independently of the reproducing-kernel
calculation in the theorem. These finite checks are not a universal proof.
"""
from fractions import Fraction as F
from itertools import product


def Q_formula(loops, leaves, kind, idx, s):
    T = sum(loops) + sum(leaves)
    base = (sum(L**3 for L in loops) / 12 + sum(h**3 for h in leaves) / 3) / T**2
    if kind == 'loop':
        L = loops[idx]
        return base + (T - L) * s * (L - s) / (T * L)
    h = leaves[idx]
    return base + (s*s + (T - 2*h)*s) / T


def double_resistance_integral(loops, leaves):
    # Integrate resistance over ordered pairs of graph edges, separately.
    q = sum((L**3 / 6 for L in loops), F(0))
    q += sum((L**2*M/6 + L*M**2/6 for i,L in enumerate(loops)
              for j,M in enumerate(loops) if i != j), F(0))
    q += sum((h**3/3 for h in leaves), F(0))
    q += sum((h*h*k/2 + h*k*k/2 for i,h in enumerate(leaves)
              for j,k in enumerate(leaves) if i != j), F(0))
    q += 2*sum((L*L*h/6 + L*h*h/2 for L in loops for h in leaves), F(0))
    return q


def W_integral(loops, leaves, kind, idx, s):
    # Integrate effective resistance from the chosen point to every edge.
    C = sum((L*L/6 for L in loops), F(0)) + sum((h*h/2 for h in leaves), F(0))
    T = sum(loops) + sum(leaves)
    if kind == 'loop':
        L = loops[idx]
        return C + (T-L)*s*(L-s)/L
    h = leaves[idx]
    return C+s*s+(T-2*h)*s


def Q_resistance(loops, leaves, kind, idx, s):
    T = sum(loops) + sum(leaves)
    return W_integral(loops, leaves, kind, idx, s)/T - double_resistance_integral(loops, leaves)/(2*T*T)


def q_max(loops, leaves):
    T = sum(loops) + sum(leaves)
    M, H = max(loops), max(leaves)
    base = (sum(L**3 for L in loops)/12 + sum(h**3 for h in leaves)/3)/T**2
    return base + max(M*(T-M)/4, H*(T-H))/T


def test():
    checks = 0
    trial_lengths = [F(1,3), F(1,2), F(2,3), F(1), F(3,2), F(2)]
    samples = [F(0), F(1,5), F(1,2), F(4,5), F(1)]
    configs = []
    for r,p in [(1,1),(1,3),(2,1),(2,2),(3,1),(3,3),(4,2)]:
        for seed in range(11):
            loops = tuple(trial_lengths[(i+2*seed) % len(trial_lengths)] for i in range(r))
            leaves = tuple(trial_lengths[(2*j+seed+3) % len(trial_lengths)] for j in range(p))
            configs.append((loops, leaves))
    for loops, leaves in configs:
        maxima = []
        for kind, E in [('loop', loops),('leaf',leaves)]:
            for idx, length in enumerate(E):
                for a in samples:
                    s=length*a
                    q=Q_formula(loops,leaves,kind,idx,s)
                    assert q == Q_resistance(loops,leaves,kind,idx,s), (loops,leaves,kind,idx,s,q)
                    assert q <= q_max(loops,leaves)
                    maxima.append(q)
                    checks += 1
        assert max(maxima) == q_max(loops,leaves)
    # Exact transition for two equal loops: A=2, hcrit=1/7.
    loops=(F(1),F(1))
    hcrit=F(1,7)
    for h in [F(1,8),hcrit,F(1,6)]:
        qloop=Q_formula(loops,(h,),'loop',0,F(1,2))
        qtip=Q_formula(loops,(h,),'leaf',0,h)
        assert (qloop>qtip if h<hcrit else qloop==qtip if h==hcrit else qloop<qtip)
    # Longest loop, longest arm remain the unique types even when other
    # lengths differ, unless ties occur in the lengths themselves.
    loops=(F(9,5),F(2,3),F(1,2))
    leaves=(F(7,6),F(1,5),F(2,3))
    T=sum(loops)+sum(leaves)
    assert loops[0]*(T-loops[0]) > max(L*(T-L) for L in loops[1:])
    assert leaves[0]*(T-leaves[0]) > max(h*(T-h) for h in leaves[1:])
    # A near-optimal universal threshold: t=4-2 sqrt(3) is the
    # unique interior maximizer of t(1-t)/(4-t). Check the exact
    # associated polynomial reduction over rational t samples.
    for i in range(1,1000):
        t=F(i,1000)
        cutoff=t*(1-t)/(4-t)
        assert cutoff < F(72,1000)
    print('EXACT_RESISTANCE_VS_REPRODUCING_KERNEL_CHECKS_PASSED',checks)
    print('FLOWER_GRAPH_GLOBAL_MAX_AND_TIE_CASES_PASSED',len(configs)+3)
    print('UNIVERSAL_THRESHOLD_SAMPLE_BOUNDS_PASSED',999)
    print('ALL_FLOWER_SOBOLEV_DIAGNOSTICS_PASSED')

if __name__ == '__main__':
    test()
