# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Partial theorem: Alexander-span growth and Fox–Milnor nonslice witnesses in a frozen 8_20 braid twist family (finite-family result; infinite ribbon-gap headline NOT claimed)

## Objects (frozen, reproducible)

- Seed: KnotAtlas `8_20`, braid representative `BR(3, {1,1,1,-2,-1,-1,-1,-2})` (Gittings data via KnotTheory`), word
  `w_0 = [1,1,1,-2,-1,-1,-1,-2]`, 3 strands, closure a knot (permutation a 3-cycle).
- Family (this report only): for `m >= 0`,
  `w_m = [1,1,1,-2] + [-1]^{2m} + [-1,-1,-1,-2]` (insert `2m` copies of `σ_2^{-1}`
  after the 4th generator). Crossing numbers `c(m) = 8 + 2m`. Closure checked a knot
  (3-cycle) for `m = 0..4` by `verify_family.py`.
- Method: unreduced Burau representation (exact, sympy only); Alexander polynomial =
  top-left `(n-1)x(n-1)` minor of `(I - B(w))`, a standard closed-braid formula, hence exact.
  Calibration: reproduces KnotAtlas `8_20` Alexander `t^2-2t+3-2t^{-1}+t^{-2}` and
  `|Δ(-1)| = 9` exactly; trefoil sanity `t(t^2-t+1)` up to the documented factor.

## Theorem (finite-family, proved by computation in stated range)

For `m = 0,1,2,3,4`, let `K_m` be the closure of `w_m`. Then:

1. (Exact Alexander polynomials.) Up to the fixed normalization (clear denominators to
   min-degree 0, sign fixed by `Δ(1) = 1`):
   - `Δ_0 = t^4-2t^3+3t^2-2t+1` (span 4),
   - `Δ_1 = t^6-2t^5+4t^4-5t^3+4t^2-2t+1` (span 6),
   - `Δ_2 = t^8-2t^7+4t^6-5t^5+5t^4-5t^3+4t^2-2t+1` (span 8),
   - `Δ_3 = t^{10}-2t^9+4t^8-5t^7+5t^6-5t^5+5t^4-5t^3+4t^2-2t+1` (span 10),
   - `Δ_4 = t^{12}-2t^{11}+4t^{10}-5t^9+5t^8-5t^7+5t^6-5t^5+5t^4-5t^3+4t^2-2t+1` (span 12).
   Hence `span Δ_m = 4 + 2m` for `m = 0..4`.
2. (Genus lower bounds.) Since `2g(K) ≥ span Δ_K`, `g(K_m) ≥ 2+m` for `m = 0..4`
   (i.e., lower bounds 2,3,4,5,6). No equality is claimed.
3. (Determinants.) `det(K_m) = |Δ_m(-1)| = 9,19,29,39,49 = 10m+9` for `m = 0..4`.
4. (Nonslice witnesses.) `K_1, K_2, K_3` are NOT smoothly (hence not topologically)
   slice: a slice knot has square determinant (Fox–Milnor `Δ(t) ≐ f(t)f(t^{-1)}`
   gives `det = |f(-1)|^2`), but 19, 29, 39 are not squares. No sliceness claim is
   made for `K_4` (det 49 is square; test inconclusive).

## What is explicitly NOT claimed

- The admitted infinite headline (`g = 2+m` with `g_4 = 0` and ribbon witnesses for
  all `m`) is NOT proved and NOT claimed. The tested braid word family in fact
  refutes its slice half for `m = 1,2,3`. Genus equality is not proved either
  (only the lower bound `g ≥ 2+m`; the canonical Seifert genus of the closed-braid
  diagram is an upper bound, not used for the lower-bound claim).
- No `DT` codes, no Seifert matrices/SNF, no ribbon bands, no signature computations
  are offered: the completed certificate uses only the braid–Burau–Alexander route.

## Proof / replay

- Run `python3 output/artifacts/verify_family.py` (imports `output/artifacts/burau.py`).
  It prints the table (m, crossings, knot-closure, span, genus lower bound, det,
  square?, `Δ(1)`, canonical `Δ`) for `m = 0..4`. `output/artifacts/family_m04.py`
  and `output/artifacts/twistscan.py` log the underlying Laurent forms and the
  36-case site scan that selected this insertion site.
- Mathematical facts used: (i) closed-braid Alexander minor formula; (ii) `2g ≥ span Δ`;
  (iii) Fox–Milnor determinant-square obstruction. All three are classical; the new
  content is the exact computed values for these five explicitly frozen above-range
  words (10–16 crossings for `m = 1..4`, outside the Rolfsen table scope).

## Novelty / limits

- `K_0 = 8_20` values are tabulated (KnotAtlas); `K_1..K_4` (10,12,14,16 crossings)
  are above the Rolfsen range and their Alexander polynomials/determinants/nonslice
  statuses are not in the checked KnotAtlas pages. Conjectured pattern
  (`span = 4+2m`, `det = 10m+9`) is computed evidence for `m ≤ 4` only, stated as
  conjecture, not theorem, beyond `m = 4`.
- Failed route logged honestly: a Wirtinger/Fox-calculus script (`alexander.py`)
  produced a wrong polynomial for the seed and was abandoned in favor of the
  calibrated Burau route; a PD Seifert-circle script gives canonical genus 3 for the
  seed diagram (upper bound only), consistent with tabulated minimal genus 2.
