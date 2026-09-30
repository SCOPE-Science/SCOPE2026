# Certified two-sided Bilu–Linial datum for the canonical symmetric signing of X^{3,5} (d=4, n=60)

## Context

The two-sided Bilu–Linial conjecture (open since 2006) asks whether every
d-regular graph admits a signing (2-lift) whose new eigenvalues all lie in
[-2√(d-1), 2√(d-1)] in absolute value. Marcus–Spielman–Srivastava and
Hall–Puder–Sawin settled only the one-sided version (upper bound on
λ_max); for non-bipartite base graphs the lower side (-λ_min) remains open.
This record decides one concrete symmetric instance in the smallest
4-regular LPS cell.

## Definitions

- Base graph G₀ = X^{3,5}: 4-regular on 60 vertices (PSL(2,5) Cayley graph
  from the norm-3 LPS quaternion construction over F₅, filed generators
  g₁=(2,3,3,0), g₂=(0,1,4,2); filed in `artifacts/lps_graph.json`).
- Generator-invariant signings: σ(g,gs) depends only on the generator label
  s ∈ {g₁,g₂} with ε(s)=ε(s⁻¹); 4 signings (e₁,e₂) ∈ {+1,-1}².
- Predetermined signing ε* = (-1,+1): lexicographically first nontrivial
  signing in filed generator order. Signed adjacency A (60×60, symmetric,
  {0,±1}, 4-regular support) filed in `artifacts/A_eps_star.csv`.
- ρ(ε*) = max|λ| over Spec(A); Ramanujan line for d=4: 2√3 = 3.464101615….

## Result

For the filed ε* = (-1,+1):

- Exact signed moments: Tr(A⁴) = 1920, Tr(A⁶) = 18000 (Tr(A²) = 240).
- Exact signed non-backtracking closed-walk counts: N₃=0, N₄=240, N₅=0,
  N₆ = Tr(B⁶) = 240.
- Certified enclosure: ρ(ε*) ∈ [3.409309059, 3.44], width 0.0307 ≤ 0.05,
  lying strictly below 2√3 (gap 0.0241).
- Verdict: ε* **is two-sided Ramanujan** (ρ ≤ 2√3): a symmetric two-sided
  Ramanujan example, deciding one concrete instance of the open two-sided
  Bilu–Linial conjecture in the example direction.

## Proof / evidence

- Lower bound (exact): integer vector v (`artifacts/rayleigh_vector.json`)
  gives vᵀAv = 3405552, vᵀv = 998898, so
  ρ ≥ vᵀAv/vᵀv = 3.409309059 exactly (Rayleigh quotient ≤ λ_max ≤ ρ).
- Upper bound (exact): U = 3.44 = 86/25; scaled matrices 86I∓25A are proved
  positive definite by fraction-free (Bareiss) integer LDL — all 60 pivots
  positive (min 86) for both 3.44I−A and 3.44I+A — hence every eigenvalue
  lies in (−3.44, 3.44) and ρ < 3.44 rigorously (Sylvester's criterion).
  Rerun: `python3 artifacts/certify_upper.py` (~1–2 min) → CERTIFY_UPPER_OK
  (independently re-executed by the auditor).
- Moments/counts (exact): pure-integer matrix multiplication and signed
  non-backtracking enumeration from the filed matrix reproduce
  Tr₂/Tr₄/Tr₆ = 240/1920/18000 and N₆ = 240.
- Replay: `python3 artifacts/verify.py` (seconds) → VERIFY_OK.
- Corroboration only (not proof): float spectrum max/min = ±3.409321836,
  consistent with the certified enclosure.

## Limitations

- The verdict is relative to the filed canonical generator pair
  (lexicographically first simple connected normalized LPS pair); LPS
  generator conventions vary and an all-pairs scan shows pair-dependent
  verdicts. The filed matrix plus generator data fix the object exactly.
- One-sided MSS/HPS theorems are provably silent on this two-sided value;
  no covering theorem implies the filed numbers.
- The full-target obstruction (all four ρ above 2√3) is FALSE on this
  canonical cell (census ρ: 4.0, 3.409321836, 3.409321836, 4.0); this
  record honestly certifies the predetermined ε* instance instead.

## Reproducibility

Filed artifacts: `A_eps_star.csv` (matrix), `lps_graph.json` (base +
labels + generators), `rayleigh_vector.json`, `verify.py`,
`certify_upper.py`, `eps_star_data.json`, `spectrum_eps_star.txt`.
Run `verify.py` then `certify_upper.py` as above.

## References

- Bilu–Linial, Constructing expander graphs by 2-lifts (FOCS 2004); Ramanujan
  signing of regular graphs (CPC 2006).
- Marcus–Spielman–Srivastava, Interlacing Families I (Annals 2015):
  one-sided 2-lift bound.
- Hall–Puder–Sawin, Ramanujan coverings of graphs (Adv. Math. 2018,
  arXiv:1506.02335): one-sided r-covering bound; fully non-bipartite
  two-sided case left open.
