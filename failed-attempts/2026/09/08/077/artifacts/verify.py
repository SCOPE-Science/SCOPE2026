"""Final replay verifier for the witness pair + corpus spot-checks. Run: python3 verify.py -> prints VERIFY_OK/FAIL."""
import sys, json
sys.path.insert(0, 'artifacts')
from garside import (positive_normal_form, perm_of_word, compose, identity,
                     delta_perm, left_weighted, simple_word)
from invariants import cycling, summit_class_invariant
from dehornoy2 import artin_action, is_identity, free_reduce_word, is_sigma_positive

N = 4
X = (0, 0, 1)        # sigma1^2 sigma2 (0-based gens)
Y = (0, 0, 1, 0, 0)  # sigma1^2 sigma2 sigma1^2

def expand(p, facs):
    d = simple_word(delta_perm(N), N)
    out = []
    for _ in range(p): out += [g + 1 for g in d]
    for s in facs: out += [g + 1 for g in simple_word(s, N)]
    return out

def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    return cond

ok = True
# 1. normal forms left-weighted, Delta-power 0, perm match, clen<=10
for w, nm in ((X, 'X'), (Y, 'Y')):
    p, facs = positive_normal_form(w, N)
    ok &= check(p == 0, f'{nm} inf(power)=0 is {p}')
    ok &= check(all(left_weighted(facs[j], facs[j+1]) for j in range(len(facs)-1)), f'{nm} left-weighted {facs}')
    q = identity(N)
    for f in facs: q = compose(q, f)
    ok &= check(q == perm_of_word(w, N), f'{nm} factor-perm product matches word perm')
    ok &= check(len(facs) <= 10, f'{nm} clen={len(facs)}<=10')
# 2. same Artin permutation
ok &= check(perm_of_word(X, N) == perm_of_word(Y, N) == (0, 2, 1, 3), 'same Artin perm (0,2,1,3)')
# 3. summit invariants via logged cycling orbits
px, fx = positive_normal_form(X, N)
py, fy = positive_normal_form(Y, N)
sx = summit_class_invariant(px, fx, N)
sy = summit_class_invariant(py, fy, N)
ok &= check(sx[0] == 0 and sx[1] == 1, f'X summit (inf,len)=(0,1): {sx[:2]}')
ok &= check(sy[0] == 0 and sy[1] == 2, f'Y summit (inf,len)=(0,2): {sy[:2]}')
# cycling conjugacy certificates: e_next == A1^{-1} e A1 via Artin action
for w, nm in ((X, 'X'), (Y, 'Y')):
    p, facs = positive_normal_form(w, N)
    p2, f2 = cycling(p, list(facs), N)
    e1, e2 = expand(p, facs), expand(p2, f2)
    A1 = [g + 1 for g in simple_word(facs[0], N)]
    A1inv = [-g for g in reversed(A1)]
    ok &= check(artin_action(A1inv + e1 + A1, N) == artin_action(e2, N), f'{nm} cycling=conjugation replay')
    ok &= check(len(e1) == len(w), f'{nm} expsum preserved {len(e1)}=={len(w)}')
# 4. distinct summit len => non-conjugate (one-sided lemma: canonical length of summit element is conjugacy invariant)
ok &= check((sx[0], sx[1]) != (sy[0], sy[1]), 'distinct summit invariants => non-conjugate')
# 5. Dehornoy: X^{-1}Y freely equals s0^2 (positive, nontrivial) => X<Y
X1 = [g + 1 for g in X]; Y1 = [g + 1 for g in Y]
Xinv = [-g for g in reversed(X1)]
fr = free_reduce_word(Xinv + Y1)
ok &= check(fr == [1, 1], f'X^-1 Y free-reduces to [1,1]: {fr}')
ok &= check(is_sigma_positive(fr) and not is_identity(fr, N), 'quotient sigma-positive nontrivial => X<Y, X!=Y')
ok &= check(artin_action(X1 + fr, N) == artin_action(Y1, N), 'X * (X^-1Y) == Y word problem')
# 6. closure: s=n Seifert circles (lemma for closed braids), chi=s-c, components from perm cycles
def comps(w):
    pr = perm_of_word(w, N); vis = [0]*N; mu = 0
    for i in range(N):
        if not vis[i]:
            mu += 1; j = i
            while not vis[j]: vis[j] = 1; j = pr[j]
    return mu
for w, nm in ((X, 'X'), (Y, 'Y')):
    mu = comps(w); chi = N - len(w)
    print(f'INFO {nm}: components={mu} seifert_circles={N} chi={chi} crossings={len(w)}')
ok &= check(comps(X) == 3 and comps(Y) == 3, 'both closures 3-component (perm (0,2,1,3): cycles (0)(1 2)(3))')
print('VERIFY_OK' if ok else 'VERIFY_FAIL')
