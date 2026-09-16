"""CONSOLIDATED PROOF SCRIPT for the W-star sharpness theorem.

Theorem (Sharpness for single tight 7-cycle):
  Let B_rec(n) be the optimal recursive B-construction (DP optimum = brec(n)).
  Fix x0 in the top block V1^(0), let W = V1^(1) (top block of H[V2^(0)]).
  H(n) := B_rec(n) + ALL triples {x0,w1,w2} (w1<w2 in W).
  Then (i) H(n) is C^3_7-free for every n; (ii) |H(n)| = brec(n)+C(|W|,2) with
  C(|W|,2)/n^2 -> (x*a*)^2/2 ~ 0.0269 (x*=(sqrt3-1)/2, a*=1-x*), so the O(n^2)
  envelope in ex(n,C^3_7) <= brec(n)+C n^2 cannot be improved to o(n^2).

Part A (below): B_rec is C7-free (infinite descent; uses only Lemma 1 word check).
Part B (below): no C7 uses a star triple (SOUND over-approximating exact-depth
  enumeration with capped depth L: over-approx can only ADD surviving words, so
  zero survivors => truly zero at EVERY n). Run: python3 proof_star.py
"""
import itertools
from math import comb

# ---------- Lemma 1: binary cyclic words length 7, window sums in {0,2}: only 0^7
good = [b for b in itertools.product([0, 1], repeat=7)
        if all((b[i] + b[(i+1) % 7] + b[(i+2) % 7]) in (0, 2) for i in range(7))]
print("Lemma1 words:", good)
assert good == [(0,) * 7], "Lemma 1 failed"
print("Lemma 1 (descent words) OK: only all-zero avoids window-sum 1 (and sum-3 excluded: top block empty)")

# ---------- Part B: sound capped-depth enumeration
L = 6  # states: A=0 (V1^(0)\\{x0}), 1..L-1 exact depths, L = deep cap '>=L'
A = 0

def edge_nox0(t):
    s = tuple(sorted(t)); a, b, c = s
    if a == b and c > b:
        return True
    if a == b == c == L:
        return True  # over-approx of deep ambiguity (sound direction only)
    return False

def edge_x0(o1, o2):
    B = (o1 == A and o2 >= 1) or (o2 == A and o1 >= 1)  # pair {x0,A} depth0 + deeper third
    S = (o1 == 1 and o2 == 1)                            # star: both in W=V1^(1)
    return B or S

# sanity of edge rules
assert edge_x0(A, 1) and edge_x0(A, L) and edge_x0(1, 1)
assert not edge_x0(A, A) and not edge_x0(1, 2) and not edge_x0(2, 2)
assert not edge_nox0((1, 2, 2)) and not edge_nox0((0, 0, 0)) and edge_nox0((0, 0, 1))
assert edge_nox0((1, 1, 2)) and not edge_nox0((2, 3, 3))
print("edge-rule sanity OK")

states = [A] + list(range(1, L + 1))
surv = []
total = 0
for rest in itertools.product(states, repeat=6):
    total += 1
    w = (999,) + rest  # 999 = x0 at position 0 (rotation wlog; x0 appears <= once)
    wins = [(w[i], w[(i + 1) % 7], w[(i + 2) % 7]) for i in range(7)]
    has_star = False
    ok = True
    for win in wins:
        nx = win.count(999)
        if nx == 0:
            if not edge_nox0(win):
                ok = False; break
        elif nx == 1:
            o = [s for s in win if s != 999]
            if not edge_x0(o[0], o[1]):
                ok = False; break
            if o[0] == 1 and o[1] == 1:
                has_star = True
        else:
            ok = False; break  # x0 twice impossible (distinct cycle vertices)
    if ok and has_star:
        surv.append(w)
print(f"enumerated {total} words; survivors with >=1 star window, all windows edges: {len(surv)}")
assert len(surv) == 0, f"FAILED: {surv[:5]}"
print("Part B OK: no C7 can use a star triple, at any n (sound over-approx => rigorous).")

# ---------- Part C: surplus constant
import math
x = (math.sqrt(3) - 1) / 2; a = 1 - x; w = x * a
print(f"limit surplus/n^2 = (x*a*)^2/2 = {w**2/2:.6f} (x*={x:.4f}, a*={a:.4f}, |W|/n->{w:.4f})")
N = 1200
b = [0] * (N + 1); ch = [0] * (N + 1)
for n in range(3, N + 1):
    best = -1; ba = 0
    for a_ in range(n + 1):
        v = comb(a_, 2) * (n - a_) + b[n - a_]
        if v > best: best = v; ba = a_
    b[n] = best; ch[n] = ba
for n in [100, 300, 600, 1200]:
    m = n - ch[n]; W = ch[m]
    print(f"n={n}: |V1|={ch[n]} |V2|={m} |W|={W} surplus/ n^2 = C(|W|,2)/n^2 = {comb(W,2)/n**2:.6f}")
print("ALL PROOF-CHECKS PASSED")
