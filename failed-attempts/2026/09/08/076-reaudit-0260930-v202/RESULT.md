# Certified Rouché-disk zero table for exponential sections s_n, n ≤ 16, with Szegő-curve gap logs and extremal witnesses

## Context

Zeros of the exponential partial sums s_n(z) = Σ_{k=0}^n z^k/k! converge (scaled by n) to the Szegő curve |ze^{1−z}| = 1 (Szegő 1924), with refined asymptotics by Newman–Rivlin (1972), Saff–Varga, Bleher–Mallison (2006), and stability-region analysis by Iserles–Nørsett. Published small-n tables give bare floating-point approximations without enclosing disks or replayable count logs. This record supplies a small-n certified fragment: per-zero isolating disks with Rouché proofs, whole-disk Szegő-gap intervals, and two closed finite-scope extremals.

## Definitions

- s_n(z) = Σ_{k=0}^n z^k/k!, 1 ≤ n ≤ 16, with exact rational coefficients 1/k!. deg s_n = n.
- Disks D(c, r): Gaussian-rational center c (denominator dividing 10^9), radius r = 3/10 (census) and nested refinement r = 1/100 (gap/extremal statements). 136 disks total (n per degree).
- Rouché majorant: write a_0 = s_n(c), a_1 = s_{n−1}(c) = s_n′(c), a_k = s_{n−k}(c)/k! for k ≥ 2. On |w−c| = r, g(w) = a_0 + a_1(w−c), h = s_n − g. With m := |a_1|r − |a_0| and M := Σ_{k=2}^n |a_k|r^k, |g| ≥ m > M ≥ |h| implies s_n and g have equal zero counts inside; |a_0| < |a_1|r gives g exactly one zero, strictly inside.
- Scaled Szegő quantity: w_n(z) = (z/n)e^{1−z/n}; gap = |w_n(z)| − 1 = (|z|/n)e^{1−Re z/n} − 1.

## Result (headline claim)

1. **Complete disjoint Rouché census.** For every 1 ≤ n ≤ 16 and every zero of s_n there is a disk D(c, 3/10) in `artifacts/disks.json` (136 rows) satisfying m > M and |a_0| < |a_1|r, hence containing exactly one zero of s_n. The n disks at each degree are pairwise disjoint (|c_i − c_j|² > (3/5)², exact) and number exactly n, so all n zeros are accounted for once each. Smallest Rouché margin m − M over all 136 disks: 0.00365 (at n = 16).
2. **Nested refinement.** The same centers with radius 1/100 satisfy the same Rouché inequality (min margin 0.000207); each D(c, 1/100) also contains exactly one zero. All gap and extremal statements use these refined disks.
3. **Maximal-real-part witness.** The largest real part among all 136 zeros is attained at n = 16 by the conjugate pair c = 7726102197/10^9 ± 12679347/1600000 i (7.726102197 ± 7.924591875 i, indices j = 14, 15). Refined Re-intervals: witness disks Re ≥ 7.7161; every other disk Re ≤ 6.9848.
4. **Minimal Szegő-gap extremal.** Whole-disk gap intervals satisfy: both n = 16 witness disks gap ∈ [0.158380647, 0.161927324]; every other of the 134 disks gap-lo ≥ 0.170167940 (runner-up n = 15, j = 13, 14). Hence the minimal scaled Szegő-curve gap across n ≤ 16 is attained at (n*, j*) = (16, 14)/(16, 15), certified by disjoint intervals (0.161927324 < 0.170167940).

## Proof / evidence

- Exact rational recurrence p_k = c^k/k!, s_m(c) = Σ p_k in `Fraction` arithmetic; absolute values bounded by floor/ceil square roots ⌊10^12√q⌋/10^12 via `math.isqrt` (sound: (t/D)² ≤ q < ((t+1)/D)²; hi-bound (t+1)/D soundness integer-verified). Residuals |s_n(c)| tiny (~1e−6 or less), |s_{n−1}(c)| order 1, tail M small at r ≤ 0.3.
- Disjointness is exact rational arithmetic; counting is Rouché count 1 per disk × n disjoint disks = n = degree.
- Gap monotonicity |w| = (|z|/n)e^{1−Re z/n}: whole-disk lo = ((|c|−r)/n)e^{1−(Re c+r)/n}, hi = ((|c|+r)/n)e^{1−(Re c−r)/n}, with rigorous sqrt via `isqrt` and rigorous exp via order-60 Taylor with Lagrange remainder x^N/N!·e^x under crude E = 3^ceil(x) (asserted < 10^−9; passed).
- Independent stdlib-only verifier `artifacts/verify.py` recomputes every inequality from committed centers/radii and prints: `VERIFY_OK disks=136 rouche_r=0.3+0.01 disjoint=1..16 maxRe_lo=7.7161>others_hi=6.9848 gap_ext_hi=0.161927<others_lo=0.170168`. Auditor re-ran it and independently re-proved all 136×2 Rouché inequalities, disjointness, and both extremal separations in exact arithmetic.
- Numpy root-finding supplies seed approximations only; soundness does not depend on them.

## Limitations

- Finite scope n ≤ 16 only; no new Szegő limit theorem or asymptotics.
- No winding-number quadrature log is shipped; the route uses the equivalent Rouché linear-majorant count, fully replayed.
- Extremal claims are over the finite scope n ≤ 16 only.
- Gap `glo`/`ghi` floats in `gaps.json` are decimal renderings of rigorous Fraction bounds (agreement rechecked to 1e−9).

## Reproducibility

- `python3 verify.py` (stdlib only) in `artifacts/` re-derives every inequality from committed `disks.json`/`gaps.json` and prints `VERIFY_OK ...`.
- Centers/radii: Gaussian rationals, denominator dividing 10^9, r = 3/10 (refinement 1/100 uses same centers).

## References

- G. Szegő (1924), Über eine Eigenschaft der Exponentialreihe.
- D. J. Newman & T. J. Rivlin (1972), The zeros of the partial sums of the exponential function, J. Approx. Theory 5:405–412. https://doi.org/10.1016/0021-9045(72)90007-X
- P. Walker (2003), The Zeros of the Partial Sums of the Exponential Series, Amer. Math. Monthly 110(4):337–339. https://doi.org/10.1080/00029890.2003.11919971
- P. Bleher & R. Mallison (2006), Zeros of sections of exponential sums. https://doi.org/10.1155/imrn/2006/38937
