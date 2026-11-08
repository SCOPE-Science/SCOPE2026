#!/usr/bin/env python3
"""Exact checks for birth-death fixation on a two-quality four-cycle.

Requires Python 3 and SymPy. No simulation or finite-grid check is used
as a substitute for the symbolic transition-equation identities.
"""
from fractions import Fraction
from itertools import product
import sympy as S

R, T = S.symbols('r s', positive=True)
U, V = R + T, R * T
NEIGHBORS = tuple(((i - 1) % 4, (i + 1) % 4) for i in range(4))
COUNT = 0


def check(truth, label):
    global COUNT
    assert truth, label
    COUNT += 1


def group_orbits(group):
    """Equivalence classes of nonabsorbing mutant masks under permutations."""
    def push(mask, permutation):
        return sum(((mask >> i) & 1) << permutation[i] for i in range(4))
    owners, classes = {}, []
    for mask in range(1, 15):
        if mask in owners:
            continue
        orbit = sorted({push(mask, permutation) for permutation in group})
        idx = len(classes)
        for member in orbit:
            check(member not in owners, 'orbits overlap')
            owners[member] = idx
        classes.append(orbit)
    check(set(owners) == set(range(1, 15)), 'orbit partition not exhaustive')
    return owners, classes


def transition_equations(high, group, r=R, s=T):
    owners, classes = group_orbits(group)
    system = S.zeros(len(classes))
    rhs = S.zeros(len(classes), 1)
    for idx, orbit in enumerate(classes):
        representative = orbit[0]
        for parent in range(4):
            mutant = bool(representative & (1 << parent))
            fecundity = (r if parent in high else s) if mutant else S.Integer(1)
            for target in NEIGHBORS[parent]:
                updated = (representative | (1 << target)) if mutant else (representative & ~(1 << target))
                if updated == representative:
                    continue
                system[idx, idx] += fecundity
                if updated == 15:
                    rhs[idx] += fecundity
                elif updated != 0:
                    system[idx, owners[updated]] -= fecundity
    return system, rhs, owners


ADJACENT_GROUP = [tuple(range(4)), (1, 0, 3, 2)]
ALTERNATE_GROUP = []
for swap02, swap13 in product([False, True], repeat=2):
    p = list(range(4))
    if swap02:
        p[0], p[2] = p[2], p[0]
    if swap13:
        p[1], p[3] = p[3], p[1]
    ALTERNATE_GROUP.append(tuple(p))


def fixation_sym(high, group):
    L, b, owner = transition_equations(high, group)
    p = L.inv(method='DM') * b
    return S.factor(sum(p[owner[1 << i]] for i in range(4)) / 4)


U_SYM, V_SYM = S.symbols('u v')
B = (2*U_SYM**4 + 3*U_SYM**3*V_SYM + 6*U_SYM**3
     + 2*U_SYM**2*V_SYM**2 + 2*U_SYM**2*V_SYM
     + 9*U_SYM**2 + 12*U_SYM + 4*V_SYM + 8)
P = (U_SYM*V_SYM**2 - 5*U_SYM*V_SYM - 2*U_SYM**2
     - 3*U_SYM - 2*V_SYM**2 - 4*V_SYM)

def factored_gap(r=R, s=T):
    return (-((r-s)**2) * (r+s+1) * P.subs({U_SYM:r+s,V_SYM:r*s}) /
            (2*(r+1)*(s+1)*(r*s+1)*B.subs({U_SYM:r+s,V_SYM:r*s})))


def alternate_probability(r=R, s=T):
    return r*s*(2*r*s+r+s)/(2*(r+1)*(s+1)*(r*s+1))


def independent_full(r, s, high):
    """An independent 14-state rational Markov-chain calculation."""
    masks = list(range(1, 15))
    eq = S.zeros(14)
    b = S.zeros(14, 1)
    for index, mask in enumerate(masks):
        for i in range(4):
            is_mutant = bool(mask & (1 << i))
            f = (r if i in high else s) if is_mutant else S.Integer(1)
            for j in NEIGHBORS[i]:
                if bool(mask & (1 << j)) == is_mutant:
                    continue
                updated = (mask | (1 << j)) if is_mutant else (mask & ~(1 << j))
                eq[index, index] += f
                if updated == 15:
                    b[index] += f
                elif updated != 0:
                    eq[index, masks.index(updated)] -= f
    solution = eq.inv(method='DM') * b
    return sum(solution[masks.index(1 << i)] for i in range(4))/4


def run():
    a = fixation_sym({0, 1}, ADJACENT_GROUP)
    b = fixation_sym({0, 2}, ALTERNATE_GROUP)
    check(S.cancel(b - alternate_probability()) == 0, 'alternating closed expression')
    check(S.cancel(a - b - factored_gap()) == 0, 'exact fixation difference identity')
    check(S.expand(P.subs({U_SYM:R+T,V_SYM:R*T})
                   -(R**3*T**2+R**2*T**3-2*R**2*T**2-5*R**2*T-2*R**2
                     -5*R*T**2-8*R*T-3*R-2*T**2-3*T)) == 0,
          'symmetric polynomial expansion')
    l, h = S.symbols('l h', positive=True)
    p_hl = S.expand(P.subs({U_SYM:h+l,V_SYM:h*l}))
    check(S.expand(p_hl - (h**3*l*l + h*h*(l**3-2*l*l-5*l-2)
                                -h*(5*l*l+8*l+3)-2*l*l-3*l)) == 0,
          'one-positive-root cubic identity')
    check(S.factor(p_hl.subs(h, l)) == 2*l*(l+1)*(l**3-2*l*l-3*l-3),
          'diagonal bifurcation polynomial')
    # Each test below uses the original 14 nonabsorbing states, independently
    # of orbit compression or the derived analytic expressions.
    pairs = [(1,1),(2,2),(2,1),(10,1),(1,10),(3,2),(2,3),(5,4),
             (1,2),(7,1),(1,7),(1,3),(3,1),(4,1),(4,5),
             (S.Rational(1,2),S.Rational(3,2)),
             (S.Rational(3,5),S.Rational(9,4))]
    for rr, ss in pairs:
        rr, ss = S.Rational(rr), S.Rational(ss)
        for high, formula in [({0,1},a), ({0,2},b)]:
            full = independent_full(rr, ss, high)
            expected = formula.subs({R:rr,T:ss})
            check(full == expected, f'14-state independent check {rr},{ss},{high}')
    check(a.subs({R:2,T:1}) == S.Rational(579,1454), 'adjacent example')
    check(b.subs({R:2,T:1}) == S.Rational(7,18), 'alternate example')
    check(a.subs({R:10,T:1}) == S.Rational(44825,70058), 'adjacent high example')
    check(b.subs({R:10,T:1}) == S.Rational(155,242), 'alternate high example')
    check(a.subs({R:2,T:1}) > b.subs({R:2,T:1}), 'moderate strength ordering')
    check(a.subs({R:10,T:1}) < b.subs({R:10,T:1}), 'strong strength reversal')
    check(a.subs({R:2,T:2}) == S.Rational(8,15), 'isothermal check')
    check(b.subs({R:2,T:2}) == S.Rational(8,15), 'alternate isothermal check')
    print('PASS:', COUNT, 'exact assertions; symbolic 8/7-orbit identities and independent 14-state solutions')

if __name__ == '__main__':
    run()
