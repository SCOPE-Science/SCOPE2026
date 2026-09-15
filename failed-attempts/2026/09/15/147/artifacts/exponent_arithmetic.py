"""Exponent audit v2 (corrected): local sup bound under vol-1 normalization.

Normalization audit (probability measure, fixed Laplace eigenvalue):
- The depth-aspect LOCAL sup bound for an L^2-probability-normalized newform
  on Y_0(p^n) is p^{n/2} (= N^{1/2}, N = p^n = level = index scale). This is the
  standard pre-trace local bound: the p-adic projector onto the depth-n
  newvector line has trace/dimension factor ~ p^n, so |f(x)|^2 << p^n at fixed
  arch parameter. (Squarefree analogue: Saha/Marshall local bound N^{1/2}.)
- The target demands sup << p^{n(1/4-delta')}, i.e. it asks to improve the
  exponent 1/2 -> 1/4-delta': a saving of ~p^{n/4} (a SQUARE ROOT of the local
  bound), not a small-delta refinement.
- Entire amplified pre-trace literature in comparable ranges achieves only
  small savings d ~ 1/24-1/12 over local (best shape: N^{1/2-d}), i.e. bounds
  like p^{0.458n}, versus the target's p^{0.208n}. Gap: a full p^{n/4}.

Waldspurger conversion audit: global toric period P (compact quotient, fixed
Vol) obeys |P| <= sup * Vol_fixed. Explicit Waldspurger:
  L(1/2) ~ Kappa * |P|^2 / beta_p,  Kappa fixed (arch + prime-to-p),
with beta_p = local toric factor of the p-adic NEWVECTOR at the split place.
Parametrize sup = p^{n(1/2-d)} (d = saving over TRUE local p^{n/2}),
beta_p = p^{-n*b} (b=0 means beta~1; b=1 means volume-heuristic p^{-n}).
Then L <= p^{n(1-2d+b)} = C^{(1-2d+b)/2} with C = p^{2n}.
Benchmark C^{5/24} needs (1-2d+b)/2 <= 5/24, i.e. 2d - b >= 7/12 ~= 0.5833.
"""
p = 3
print("Local (prob, fixed lambda): p^{n/2}. Target sup: p^{n(1/4-d')}. Saving demanded: ~p^{n/4}.")
print()
for n in [2, 4, 6, 8, 10]:
    local = p ** (n / 2)
    tgt = p ** (n * (0.25 - 1/24))
    best_known_shape = p ** (n * (0.5 - 1/24))
    print(f"n={n:>2}: local p^{{n/2}}={local:>7.1f} | best-known shape p^n(1/2-1/24)={best_known_shape:>9.1f} | target p^n(1/4-1/24)={tgt:>7.2f}")
print()
print("Feasibility inequality for benchmark C^{5/24}: 2d - b >= 7/12 ~= 0.5833")
print("  d  = sup exponent saving over true local p^{n/2} (technology limit d <=~ 1/12);")
print("  b  = -log(beta_p)/log(p^n), beta_p = newvector toric factor (beta_p <= O(1) => b >= ~0).")
d_max, b_min = 1/12, 0.0
print(f"  most generous known-tech corner: d={d_max:.4f}, b={b_min:.1f} -> 2d-b = {2*d_max-b_min:.4f} < 0.5833. FAILS.")
print("  with volume-heuristic b=1: need d >= 19/24 ~= 0.79 (sup saving p^{0.79n} vs available p^{0.08n}). FAILS.")
print("Conclusion: no (d,b) regime consistent with known technology AND beta_p<=O(1)")
print("reaches the benchmark through the sup-into-Waldspurger triangle inequality.")
