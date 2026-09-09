# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Interval-certified minima of L(1,χ) and central nonvanishing for primitive characters of conductor q ≤ 32

## Theorem (certified census)

Let q ≤ 32 and χ run over primitive Dirichlet characters mod q (204 in total;
conductor distribution in Table 1 of the artifact `chars_integer_data.json`).
Then:

1. **L(1,χ) enclosures.** For every such χ there is a computed complex interval
   box B_χ = R_χ × iI_χ with Re-width and Im-width both ≤ 10⁻⁶ (in fact ≤ 2×10⁻⁷⁹
   at the working precision) such that L(1,χ) ∈ B_χ, and 0 ∉ B_χ in the sense
   that the rigorous lower bound |L(1,χ)|² ≥ min_{(x,y)∈B_χ}(x²+y²) > 0.
2. **Extremal minimum pair.** The minimum of |L(1,χ)| over the window is attained
   exactly on one conjugate pair at conductor 19:
   - q* = 19, (Z/19Z)× = ⟨2⟩, χ*(2) = exp(2πi·5/18), χ̄*(2) = exp(2πi·13/18)
     (indices i=4 and i=12 in the artifact enumeration; both odd, χ*(−1) = −1).
   - Rigorous boxes: Re ∈ [0.40032619437131310, 0.40032619437131311] (width 0 at
     display precision; true width < 10⁻⁷⁸), Im ∈ ±[0.10231204279254681, …],
     |L(1,χ*)|² ≤ 0.170728816001 (upper corner bound), while every χ outside the
     pair satisfies |L(1,χ)|² ≥ 0.185251856461 (lower bound), witnessed by
     χ = quadratic-type even character mod 5 with L(1,χ) = 0.4304089409640040….
     Hence both minimum boxes lie strictly below every other box: the gap is
     ≈ 0.0145 ≫ box diameters (≈ 10⁻⁷⁹).
3. **Central nonvanishing (even χ).** For every even primitive χ in the window
   (99 characters), L(1/2,χ) ≠ 0 with an explicit rigorous witness:
   |L(1/2,χ)| ≥ |S_{B,q}(χ)| − U(B,q) > 0, where S is the interval partial sum
   over n ≤ Bq and U(B,q) = E_max/√(Bq+1), E_max = ⌊φ(q)/2⌋, is the closed-form
   tail majorant from the block-mean-zero lemma below. At B = 1500 all 99 pass
   (smallest: q = 5, |L| ∈ [0.208658, 0.254844]);
   the replay script re-verifies all 99 already at B = 300.

## Closed forms used (proved below)

- **Odd χ:** L(1,χ) = (π/2q) Σ_{(a,q)=1} χ(a) cot(πa/q).
- **Even χ:** with ζ_q = e^{2πi/q}, τ(χ̄) = Σ_a χ̄(a)e^{2πia/q},
  S(χ) = Σ_a χ̄(a) Log(1 − ζ_q^{−a}), L(1,χ) = −S(χ)/τ(χ̄),
  where Log is the principal branch (all arguments 1 − ζ_q^{−a} avoid (−∞,0]).
- **Central tail (even χ only):** with block mean M = Σ_{a=1}^{q}χ(a) = 0,
  |Σ_{n>N}χ(n)/√n| ≤ E_max/√(N+1), E_max = ⌊φ(q)/2⌋; applied with N = Bq.

## Proofs of the formulas

*Digamma form.* For nonprincipal χ,
L(1,χ) = Σ_n χ(n)/n = q^{−1}Σ_a χ(a)ψ… precisely,
Σ_{m≥0}(m+a/q)^{−1} Abel-sums to −ψ(a/q) via ψ(z) = log z − Σ…, and
Σ_a χ(a) = 0 kills the pole: L(1,χ) = −q^{−1}Σ_a χ(a)ψ(a/q). Verified numerically
against truncated Dirichlet series to O(q/N).

*Odd case.* Pair a ↔ q−a; χ(q−a) = −χ(a); reflection
ψ(a/q) − ψ(1−a/q) = −π cot(πa/q) gives the cotangent form (each pair counted
once, equivalently π/2q over the full unit sum). Matched the digamma form to
~10⁻¹⁵ on all odd probes.

*Even case.* Fourier expansion −Log(1−e^{−2πia/q}) = Σ_{m≥1}e^{−2πiam/q}/m and
τ-orthogonality χ̄-projection give S(χ) = −τ(χ̄)L(1,χ). The identity
|τ(χ̄)|² = q (primitivity) was rechecked numerically (|τ|² = q to 10⁻¹⁵ on all
even probes); the certificate divides by the interval τ directly, so no
separate use of |τ|² = q is needed for soundness.

*Central tail (even χ only; corrected).* Let χ be nonprincipal (hence every
primitive χ of conductor ≥ 3, in particular every even χ here) and set
M = Σ_{a=1}^{q}χ(a) = 0 — verified per character from the integer enumeration
(max|M| = 9.8×10⁻¹⁴ over all 99 even χ; the verifier re-asserts |M| < 10⁻⁹).
Let f(n) = n^{−1/2} > 0 decreasing, N′ = Bq a period multiple, and split the tail
into blocks r ≥ 0. On block r put C_b = Σ_{a=1}^{b}χ(N′+rq+a) (C_0 = 0,
C_q = M = 0). Summation by parts on the block gives
T_r = C_q f(N′+(r+1)q) + Σ_{b=1}^{q−1}C_b(f_b − f_{b+1}) with f_b = f(N′+rq+b),
so with M = 0, |T_r| ≤ E_max(f(N′+rq+1) − f(N′+rq+q)) where
E_max = max_b|C_b| ≤ ⌊φ(q)/2⌋ (crudest valid: at most φ(q)/2 nonzero summands of
modulus 1). Summing over blocks telescopes: every difference is bounded by the
integral of −f′ over the block span, the spans are disjoint, so the total is at
most f(N′+1). Hence the valid majorant |R| ≤ E_max/√(N′+1), evaluated in interval
arithmetic (upper endpoint taken). The previous majorant
q(1/√(N+1) − 1/√(N+q)) with the "|C| ≤ q telescoping" justification was wrong and
is withdrawn: it already fails for the odd character mod 3 at B = 300, where the
true tail ≈ 1.09×10⁻² exceeds the old T ≈ 1.11×10⁻⁴. Odd central values are not
claimed (the target requires only even ones).

## Rigorous computation (what the auditor replays)

- **Character enumeration (exact integers only):** generators of (Z/qZ)×, discrete-log
  table, all exponent tuples k, exact multiplicativity filter, conductor filter
  (χ(a) = 1 whenever a ≡ 1 mod d), conjugate-pair dedup. Completeness identity
  Σ_{d|q}N_prim(d) + 1 = φ(q) passes for every q ≤ 32; character orthogonality
  passes on all 3336 (i,j) pairs.
- **Interval evaluation:** χ-values are *not* stored floats; each χ(g_j) is
  evaluated as iv.cos/iv.sin of the exact rational 2πk_j/o_j inside mpmath's
  outward-rounded interval context (50–80 dps). All downstream ops (cot via
  iv.cos/iv.sin, Log via iv.log, sqrt, division) stay in interval arithmetic.
  Hence every box rigorously contains the true value *conditional on mpmath iv
  outward rounding* (standard assumption, stated as a limitation).
- **Determinism:** the verifier recomputes everything from
  `chars_integer_data.json`; run `python3 verify.py [--half-nblocks=K]` prints
  `VERIFY_OK`. Full tables: `certL1_table.json` (204 rows), `certLhalf_table.json`
  (99 rows).

## Computed evidence (selected values)

- Minimum pair: q=19, χ*(2)=ζ₁₈⁵: L(1,χ*) ∈ 0.40032619437131310 ± 10⁻¹⁶ +
  i(0.10231204279254681 ± 10⁻¹⁶); |L|² ∈ [0.17072881600020…, …] (width ~10⁻⁷⁹).
- Runner-up: q=5 even χ (k=2): L = 0.43040894096400403… (real; the iv imaginary
  box is symmetric noise at 10⁻³⁰ scale, see Limitations); |L|² ≥ 0.185251856461.
- Central minimum: q=5 even: |L(1/2,χ)| ∈ [0.208658, 0.254844] (B=1500, corrected U).
- Zero-exclusion: all 204 |L(1)|²-box lower bounds > 0 (smallest 0.1707…);
  all 99 even central witnesses |S| − U > 0.

## Limitations and uncertainties (honest)

- Soundness of the *width/containment* claims inherits mpmath `iv` outward-rounding
  correctness at the stated dps; no independent IEEE-rounding audit was performed.
  Mitigation: all margins are enormous (gaps 10⁻² vs widths 10⁻⁷⁹ for L(1);
  central witnesses have margin ≥ 10⁻⁶ vs interval noise ~10⁻³⁰), so a rounding
  bug would have to be catastrophic to flip any qualitative conclusion; the
  box endpoints are published for independent re-checking with Arb/MPFI.
- Real even characters have exact Im(L(1,χ)) = 0 by conjugation symmetry, but the
  interval evaluation passes through complex Log/τ and returns a symmetric
  micro-box straddling 0 (e.g. q=5: Im ∈ [−1.8×10⁻³⁰, 1.6×10⁻³⁰]). This does not
  affect any |·|² lower bound or disjointness claim; it is documented, not hidden.
- The two minimum boxes are conjugates with bit-identical |·|² intervals; the
  "pair" is that conjugate pair, and disjointness is claimed versus all boxes
  outside the pair (proved: both upper endpoints < third lower endpoint).
- Odd central values L(1/2,χ) are *not* claimed nonzero (they can vanish by sign;
  the target claim only requires even ones). No strip-fragment fallback was needed.
- No originality is claimed for the formulas (classical); the new contribution is
  the closed, replayable interval census with the named extremal pair over q ≤ 32.

## Reproduction

```
python3 output/artifacts/verify.py --half-nblocks=300   # ~2 min, prints VERIFY_OK
python3 output/artifacts/verify.py                      # full B=1500 central check
```

Artifacts: `output/artifacts/chars_integer_data.json` (exact enumeration data),
`output/artifacts/certL1_table.json`, `output/artifacts/certLhalf_table.json`,
`output/artifacts/verify.py`.
