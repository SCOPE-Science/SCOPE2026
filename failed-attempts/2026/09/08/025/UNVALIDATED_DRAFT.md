# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified regulator and class-number table for real quadratic fields Q(sqrt(d)), squarefree d <= 200

## Status

**Partial theorem (proven core) + explicitly quarantined remainder.** All 121 squarefree
d in [2,200] have certified period, minimal unit with exact norm equation, regulator
interval, Minkowski-bound prime-splitting census, exact class number h, and (for the
68 fields with h=1) principal-ideal generator certificates — all re-derived by an
independent stdlib-only verifier in under a second. Invariant-factor (Smith-form)
decomposition is proven only for h <= 3 (116/121 fields); the five h=4 fields have
certified class-number order 4 with group structure explicitly **unresolved**.
The target's "complete ideal-multiplication relation log for the largest-h field"
was **not** completed and is quarantined with a documented obstruction (below).

## 1. Objects and conventions

- O' = Z[sqrt(d)] (order of conductor 1 or 2); O = maximal order
  (O = O' unless d = 1 mod 4, when O = Z[(1+sqrt(d))/2]). D = discriminant
  (d if d = 1 mod 4 else 4d). M = sqrt(D)/2 (Minkowski bound; never an integer here).
- x0, y0, norm: minimal solution of x^2 - d*y^2 = +-1 (convergents, exact big ints).
  eps = x0 + y0*sqrt(d), fundamental unit of O'.
- `regulator` column (topic convention): log of the minimal totally-positive unit of O',
  i.e. log(eps) if norm = +1, else 2*log(eps) (the square). Norm is recorded alongside,
  so both values are recoverable.
- EPS = fundamental unit of O; R_field = log(EPS) (standard regulator, used inside the
  class-number formula). H = class number of O; H+ = narrow (strict) class number.

## 2. Proven results (121/121 fields; verifier re-derives each)

**(A) Periods and minimal units.** Two independent integer CF routines per d
(stop-at-2a0; convergent-norm rule) agree on all 121; a doubled-block repeat check
certifies minimality; exact big-int check N(x0,y0) = (-1)^l. Extremes:
longest period l = 22 unique at d = 166; largest topic-regulator
R = 43.0437534417 at d = 181 (l = 21, norm -1, doubled); largest field regulator
R_field = 24.2055021388 at d = 199 (runner-up d = 151, 21.9634633555).

**(B) Minkowski prime-splitting census.** Complete rational-prime list below M per field
(independently re-sieved by the verifier) with Kronecker(D/p)-verified types
(split/inert/ramified). No norm below M is missing.

**(C) Class numbers (exact).** H+ = number of rho-cycles of reduced indefinite binary
quadratic forms of discriminant D (exact integer arithmetic; every form's cycle closure
replayed; primitivity asserted per form). Parity rule: H = H+ if l odd, H = H+/2 if l
even (proved via the H+/H exact sequence and the norm -1 criterion). Independently, the
class-number formula H*R_field = sqrt(D)/2 * L(1,chi) with the rigorous tail bound
|tail_N| <= D/N + 1/(floor(N/D)+1) + 1e-9 (float allowance) gives an interval of
half-width < 1/2 around H for every field (N = 100000 sufficed everywhere), pinning H
exactly. Distribution: H = 1: 68 fields; H = 2: 46; H = 3: 2 (d = 87, 167);
H = 4: 5 (d = 82, 130, 145, 170, 195).

**(D) h = 1 certificates (68/68).** For each h = 1 field, every split/ramified prime
p < M has an exhibited generator alpha in O with |N(alpha)| = p (exact equation; search
bounds 2000, escalated to 200000 where needed), which generates the prime ideal(s)
above p; inert primes give principal (p). By Minkowski + unique factorization this
proves H = 1. The verifier rechecks every norm equation.

**(E) Maximal-order subtlety (handled exactly).** [O:O'] is 1 or 2; the unit index
m = [O^x : O'^x] divides 3 when d = 1 mod 4 (and equals 1 when 2 splits, i.e. d = 1
mod 8). Exactly 17 fields (all 5 mod 8: 5, 13, 21, 29, 53, 61, 69, 77, 85, 93, 109,
133, 149, 157, 165, 173, 181) have m = 3, each with an exactly verified cube root
sigma = (U+V*sqrt(d))/2, sigma^3 = eps (integer identity (U+V√d)^3 = 8x0+8y0√d with
U = V mod 2). R_field = R_conv/3 there; the class-number-formula pinning uses R_field
throughout. The d = 1 mod 8 no-cube-root assertion is enforced as a runtime check.

## 3. Proofs of the facts the computation relies on (sketches)

1. *CF period.* The (m, den, a) iteration is purely integral; a_l = 2a0 first occurs at
   the period (standard theorem); N(p_{l-1},q_{l-1}) = (-1)^l; the convergent is the
   least solution (each solution arises from a convergent, and period minimality makes
   l - 1 the first index with the right norm sign).
2. *Narrow vs ordinary.* H+/H injects into {+-1}-signs of units (principal-ideal sign
   map), so H+ in {H, 2H}; norm -1 unit exists iff l is odd (odd l exhibits one; even l
   makes every convergent norm +1, and every unit is +-eps^k). Hence l odd -> H = H+,
   l even -> H+ = 2H (H+ is even in all 52 even-period fields — verified).
3. *Forms count H+.* Reduced indefinite forms of discriminant D fall into disjoint
   rho-cycles in bijection with narrow classes (reduction operator theory; the code
   uses only the checkable consequence: the rho graph on the finite reduced set is a
   disjoint union of cycles, replayed per field). Primitivity: imprimitive content
   g > 1 needs g^2 | D; g = 2 with D = 4d forces d = (b/2)^2 - 4a'c', impossible for
   d = 2, 3 mod 4 — asserted per form at runtime.
4. *Tail bound.* Group chi(n)/n into blocks of D consecutive terms using mean-zero of
   chi: |block_m| <= D/N_m with N_m the block start... (full elementary estimate in
   `compute.py` docstring chain; the implemented bound E = D/N + 1/(M0+1) + 1e-9 is
   re-derived term-by-term in the report appendix of the verifier log). Positivity
   L_lo > 0 held for all 121 fields at N = 100000.
5. *h = 1 from witnesses.* Standard Minkowski + unique factorization argument above.

## 4. Reproduction

- `artifacts/compute.py` (stdlib only) regenerates all six data files (~1 min).
- `artifacts/verifier.py` (stdlib only, independent code paths: third CF route,
  root-counting Legendre, re-sieved primes, replayed intervals, exact norm checks,
  10 random-field analytic spot checks) passes 2952/2952 checks in < 1 s:
  `python3 artifacts/verifier.py artifacts` exits 0.
- Columns: `table.csv` = (d,D,period,regulator,x0,y0,norm,M,h,invariants) exactly as
  specified; `table_full.json` adds R_conv/R_field/m_index/sigma/cycle data;
  `ideals.json`, `principals.json`, `Lbounds.json`, `extremal.json` as specified.

## 5. Limitations and quarantined remainder (no overclaim)

- **Group structure:** proven only for H <= 3 (invariants C1/C2/C3, 116 fields). The five
  H = 4 fields (82, 130, 145, 170, 195) have certified order 4 with structure
  (C4 vs C2xC2) explicitly unresolved — recorded as `"unresolved"`, not defaulted.
- **Maximal-h relation log:** the target's "complete ideal-multiplication relation log
  for the largest-h field" is QUARANTINED: obstruction = composing/reducing O-ideals
  with Smith-form relation replay was not completed in this pass; only the certified
  order (4, five-way tie) is claimed. No relation matrix is published.
- Values of H(d) overlap scattered LMFDB/PARI/textbook tables; the contribution is the
  single dependency-free certificate chain (period -> unit -> regulator -> Minkowski
  census -> group order -> principal certificates -> minute-scale verifier), not new
  values alone. Confrontation with Cohen-Lenstra or the cited infinite-family results
  is left to future work.
