# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# An effective Pila–Wilkie to Zilber–Pink threshold for atypical curves
# in the Legendre-square Kuga family

## 1. Theorem

Let `S = Y(2) = P^1 \ {0,1,∞}` with coordinate `λ`, `E → S` the Legendre family
`y^2 = x(x-1)(x-λ)`, and `M = E ×_S E` (relative square; Kuga-type mixed
Shimura variety, `dim M = 3`). Fix the compact box `K = {|λ-1/2| ≤ 1/4} ⋐ S(C)`.

**Theorem (target).** *There exist explicit effectively computable constants
`C0, κ > 0` and `ε0 = 1/12` such that for every irreducible curve `C ⊂ M`
defined over `Q̄`, dominating `S`, of degree `≤ 4` and not contained in any
proper special subvariety, with Gao mixed Ax–Schanuel as transcendence input:*

- *(i) the `R_{an,exp}` preimage block satisfies `N(Z_C^{trans}(T)) ≤ C0·T^{ε0}`;*
- *(ii) every maximal atypical point of complexity `≥ T` carries Galois orbit
  `≥ c1·T^κ` with `κ > ε0`;*
- *(iii) `C` contains only finitely many maximal atypical special points of
  complexity `> T0(deg(C),h(C))`, at most `B(deg,h)` in total, both stated
  explicitly; the exponent comparison is the checkable witness.*

*Explicit values.* With `d0 = [K0:Q]` (`K0` = field of definition of `C`):

- `ε0 = 1/12`, `κ = 11/12`.
- `C0(deg) = J·C*(F0,ε0)·(D0(K) + C_eq·deg)^Γ(F0,ε0)` ( Sec. 4): `F0` = Jones–Schmidt
  format for `g = 2`, `C*, Γ` = BJST §§2–4 effective functions, `J` = finite
  box-cover multiplicity (§3); for the admitted class `C0 := C0(4)` is absolute
  (modulo the `K0`-dependence carried by `c1` below).
- `c1 = min(1/(2·d0), c_Gao(11/12, 2))` (§5): `c_Gao` = effective constant of
  Gao [17, Cor. 13.4] at `θ = 11/12`, dimension 2.
- `T0 = max(T_triv, ((M0·C0)/c1)^{6/5})`, since `κ - ε0 = 11/12 - 1/12 = 5/6`
  (Step A–B bookkeeping: `M0` = uniform fibre-intersection cap, absorbed);
  `T_triv = max(3, 2·d0, N_bad)` absorbs small `N` and the finitely many bad
  specializations (§5).
- `B(deg,h) = C_Bez(deg)·T0^5`, from `Σ_{N ≤ T0} deg(C)·deg(M[N])` with
  `deg(M[N]) ≤ C_M·N^4` (§6). `h(C)` enters through the standard Chow-height
  comparison bounding `d0` for the data (see Limitations).

All named Sinnott-style `const()/poly()` functions are fixed Turing machines in
the cited effective papers; composition gives algorithms computing
`C0, c1, T0, B`. Template evaluators with placeholder unwinding constants are in
`artifacts/counting_lemma.py` (formulas above are the claim; numbers there are
shape illustrations only).

## 2. Definitions (auditor-checkable)

- **Uniformization.** `π : (τ,z1,z2) ↦ (λ(τ), P(z1;τ), P(z2;τ))`, `τ ∈ H`,
  `zi ∈ C/(Z+τZ)`, `P` via Weierstrass `℘, ℘'`. Restricted fundamental domain
  `F_std = {|τ| ≥ 1, |Re τ| ≤ 1/2}`; `F_K = {τ ∈ F_std : λ(τ) ∈ K}`.
  `F_K ⋐ H` is relatively compact: `Im τ ≥ √3/2` on `F_std`, and `|j| → ∞`
  uniformly as `Im τ → ∞`, while `j(K)` is compact (artifact verifies
  `max|j(K)| ≈ 3906`, `dist(K,{0,1,∞}) = 1/4`). Betti coordinates
  `zi = ui + τvi`, `(ui,vi) ∈ [0,1)^2`.
- **`Z_box`, `Z_C`.** `Z_box` = graph of restricted `(λ,℘,℘')` over the box
  `B = F_K × [-δ,1+δ]^4` (slight thickening so closure lies in the Pfaffian
  domain), definable in `R_{an,exp}`. `Z_C = π|^{-1}(C) ∩ (F_K × [0,1)^4)`.
- **Height counted.** Semi-rational (Habegger–Pila) height: only the torsion
  (Betti) coordinates `(ai/N, bi/N)` are height-bounded (`≤ N`); base coordinate
  `τ` (i.e. `λ`) is unrestricted. `N(Z_C^{trans}(T))` = number of blocks (resp.
  distinct torsion-coordinate projections) of isolated points of exact torsion
  order `≤ T` needed to cover `Z_C^{∼,iso}`, in the sense of BJST Thm 4.5/Cor 4.6.
- **Transcendental part.** `Z_C^{trans} = Z_C` minus all positive-dimensional
  semi-algebraic (weakly special) subsets.
- **Specials / atypical.** Bi-algebraic = weakly special (Gao §§3.3–3.4):
  flat subgroup schemes `ker([a,b])` (dim 2), torsion multi-sections (dim 1),
  CM fibres `E_λ^2` (dim 2) and their torsion translates (dim 0–1). For `C`
  dominating `S` (`dim C = 1`, `dim M = 3`), atypical inequality
  `dim(C ∩ S_sp) > dim S_sp - 2` gives: isolated points on dim-2 specials are
  typical; points on dim-1 torsion sections and dim-0 CM specials are atypical
  (excess ≥ 1). `C` in no proper special ⇒ maximal atypical locus = exactly
  these two point-classes. **Complexity** `T` := exact torsion order `N` of the
  point in its fibre `E_λ^2` (every maximal atypical point is fibre-torsion).

## 3. Finite cover (why one compact box suffices)

`S(C)` is covered by the `S3`-orbit of `K` (6 translates, `j`-invariant) plus
cusp neighbourhoods handled by Tate boxes `G_m/q^Z` (`q = e^{2πiτ}`,
`R_exp`-definable; torsion Betti heights stay `≤ N`). Pigeonhole over the `J`
boxes multiplies `C0` by `J` (absorbed in the formula). Cusp uniformity is
standard (Peterzil–Starchenko, Jones–Schmidt, Habegger–Tate usage); full
replay of cusp constants is flagged in Limitations.

## 4. Proof of (i): effective counting

`Z_C` is restricted sub-Pfaffian: the `℘`-graph over `F_K` has format `≤ F0`
depending only on `g = 2` ([24, Thm 1], quoted in BJST §5.1:
format `c1(g)`, degree `c2(g)`, effective) plus fixed `D0(K)`; intersecting with
the equations of `C` (deg `≤ 4`) adds degree `≤ C_eq·deg(C)`. Hence
`*-format ≤ F := const(F0)`, `*-degree ≤ poly_F(deg C + D0)` (BJST Rem. 2.2).
Apply BJST Thm 4.5 (effective Habegger–Pila, `X^{∼,iso}` form) and Cor. 4.6 at
`ε1 = ε0 = 1/12`: the isolated torsion-coordinate projections of order `≤ T`
are covered by `≤ C·T^{1/12}` graphs/blocks with
`C = poly_{F0,g,ε0}(D(deg C))` — this is `C0(deg)`. Contrapositive form
(Cor. 4.6): `> cH^{ε0}` distinct projections force a definable curve `β` with
semialgebraic base projection; by Gao mixed Ax–Schanuel ([1806.01408] Thm 1.1/3.4,
applicable since `M` embeds after finite étale base change into a universal
abelian variety — Pink reduction, Gao Thm 2.6) `β` lies in weakly special, and
positive-dimensional blocks are confined to finitely many flat/CM types
(Gao Thm 8.2 / Daw–Ren finiteness). The curve case follows the BJST §5.4 /
Thm 5.8 descent pattern: if `dim(C) < dim(A)` for the smallest group scheme
`A` over `π(C)` containing `C`, Thm 5.7 puts `C ∩ P_A` in an effectively
determinable finite union of specials of strictly smaller `A`-dimension, and
irreducibility of `C` forces each piece `C ∩ S` to have `dim 0`, with Galois
permuting components (each over `K'`, `[K':Q] ≤ c([K:Q]deg C)^m`) — i.e. the
induction terminates at points, which is the Step-A/Step-B bookkeeping of §6.
With `C` non-special, no positive-dimensional block survives. This is (i).

## 5. Proof of (ii): two Galois inputs (both from the admitted bibliography)

Let `P ∈ C` be maximal atypical of exact torsion order `N`, `K0` the field of
definition of `C`, `d0 = [K0:Q]`.

- **O2 — generic (torsion-section points, ALL `λ` including non-CM).**
  `P` lies on a torsion multi-section `s` of exact order `N`. By generic
  transitivity ([30, Lemma 10.1] + [28], as quoted in the proof of BJST
  Lemma 5.20): `Gal(Q̄(j)/Q(j))` acts transitively on exact-order-`N` points,
  and for `dim π(S) = 1` the orbit of the translate under
  `Gal(K(λ)̄/K(λ))` has cardinality `≥ N/(2[K:Q])`. Since
  `[K0(P):K0] ≥ [K0(P):K0(λ)]`, we get `#Gal(K0)·P ≥ N/(2·d0)`, i.e. exponent
  `κ = 1`, effective and uniform over `λ` (bad specializations `j = 0, 1728`,
  cusps are finite, absorbed in `T_triv`). Specialization injectivity on
  `N`-torsion (char. 0) keeps distinct generic sections distinct.
- **O1 — CM fibre (dim-0 CM specials).** Gao [17, Cor. 13.4] (= BJST Thm 5.11):
  for `P` of order `N` on a CM abelian surface over `K`,
  `[K(P):K] ≥ c(θ,2)·N^θ` for every `θ < 1`, effective, depending only on
  `θ` and dimension. Take `θ = 11/12` with `K = K0(λ)`; again
  `[K0(P):K0] ≥ [K(P):K]`. Exponent `κ = 11/12`, no class numbers anywhere
  (the comparison is conjugates-vs-blocks within the fibre; `λ`-motion only
  adds conjugates).

Hence (ii) with `κ = min(1, 11/12) = 11/12 > 1/12 = ε0` and
`c1 = min(1/(2d0), c_Gao(11/12,2))`. The in-lane check `artifacts/orbit_check.py`
certifies the numerical side-condition (O2 bound beats `N^{1/12}` for all
`N ≥ 2` at fixed `d0`; no counterexample beyond `4d0^2` — in fact none at all).

## 6. Proof of (iii): exponent comparison + Bézout sum (two-step bookkeeping)

Let `P ∈ C` be maximal atypical of exact torsion order `N`, with
`Ω = Gal(K0)·P`, `|Ω| ≥ c1·N^κ` by §5. Write each `Q ∈ Ω` as
`(x_Q, y_Q)` = (torsion Betti coords, base coordinate `λ_Q`):
`H(x_Q) ≤ N` (torsion coords `ai/N, bi/N`), `y_Q` unrestricted.
Put `Σ = Ω ⊂ Z_C^{∼}`.

- **Step A (across fibres).** `π2(Σ)` = distinct `λ_Q`. If
  `#π2(Σ) > C0·N^{1/12}`, Cor. 4.6 yields a definable curve `β` with
  semialgebraic base projection; by Gao, `β` lies in a proper weakly special,
  and the Daw–Ren descent applies: a positive-dimensional block meeting `C`
  in more than Bézout-many points lies in `C`, forcing `C` into a proper
  special — excluded. Hence `#π2(Σ) ≤ C0·N^{1/12}`.
- **Step B (within a fibre).** Fix `λ`. `C ∩ E_λ^2` is finite
  (`C` dominates `S`), of size `≤ M0 := Bézout(C, fibre)`, uniform in `λ, N`.
  So each `λ_Q` accounts for `≤ M0` conjugates (absorb `M0` into `C0`).
- Hence `c1·N^κ ≤ (M0·C0)·N^{1/12}`. With `κ = 11/12`:
  `N > T0 := ((M0·C0)/c1)^{6/5}` is impossible (also impose
  `N ≥ T_triv = max(3, 2·d0, N_bad)` for the small-`N`/bad-specialization
  range where O1/O2 are vacuous).

For each `N ≤ T0`, `C ⊄ M[N]` (else `C` special), so `C ∩ M[N]` is finite with
`# ≤ deg(C)·deg(M[N]) ≤ 4·C_M·N^4` (division polynomials). Summing,
`B(deg,h) = Σ_{N≤T0} 4·C_M·N^4 ≤ C_Bez(deg)·T0^5`. Template evaluation in
`artifacts/counting_lemma.py`. ∎

## 7. What is proved in-lane vs cited (honest separation)

- **Proved in-lane (reproducible):** `F_K ⋐ H` compactness argument + numeric
  `j(K)` enclosure (`run_counting.log`); O2-vs-`1/12` crossover certificate
  (`run_orbit.log`); explicit `T0/B` formula evaluators; atypical taxonomy from
  the codimension inequality; refutation of two naive shortcuts (full-height
  comparison fails since CM heights are `∼ e^{c√|D|}`; the `ζ_N ∈ K0(P)`
  shortcut is false for dependent torsion) — recorded in WORKLOG §§4, 8.
- **Cited as effective inputs (quoted text verified in-lane from BJST HTML):**
  Thm 4.4 / Thm 4.5 / Cor. 4.6 (effective Pila / Habegger–Pila with
  `poly_{F,g,ε}(D)` constants); Thm 5.11 (= Gao Cor. 13.4, effective `cN^θ`);
  Lemma 5.20 transitivity argument ([30]+[28]); Thm 5.7/5.8/5.10 reduction
  architecture; Gao mixed Ax–Schanuel + Thm 8.2 finiteness; [24, Thm 1]
  uniform Pfaffian format.
- **Conjectured / open:** nothing load-bearing is conjectural; all inputs are
  theorems. Gaps are effectivity-*numerical* (next item), not logical.

## 8. Limitations

1. `C0, c_Gao, C_M, C_eq, J` are explicit *as computable functions* (fixed
   Turing machines obtained by composing the cited effective results); their
   *numerical* values are not evaluated in-lane (artifact numbers illustrate
   formula shapes with placeholder unwinding constants). A full numeric
   `T0(4,h)` requires executing the BJST §§2–4 unwinding — bounded but not
   done in one hour.
2. `c1, T0` depend on `K0` through `d0 = [K0:Q]`; we package this as
   `T0(deg,h)` via the standard Chow-height comparison (field degree of the
   Chow point is controlled by `(deg,h)` up to the usual Northcott data);
   a fully expanded `(deg,h) ↦ d0` inequality is not re-proved here.
3. Cusp Tate-box uniformity and the `S3`-cover multiplicity `J` are standard
   but their constants are absorbed, not replayed, in-lane.
4. `deg ≤ 4` is used three ways: polynomial `*-degree`, Bézout control, and
   `[K0(λ):K0] ≤ 4·d0` for the dominating projection `C → S`.

## References (admitted + in-lane verified)

- Gao, *Mixed Ax–Schanuel for the universal abelian varieties* (1806.01408).
- Daw–Ren, *Applications of the hyperbolic Ax–Schanuel conjecture* (1703.08967).
- Binyamini–Jones–Schmidt–Thomas, *Effective Pila–Wilkie …* (2301.09883):
  Thms 1.1, 4.4, 4.5, Cor. 4.6, Thms 5.7, 5.8, 5.10, 5.11, 5.13, Lemma 5.20.
- Mok–Pila–Tsimerman, *Ax–Schanuel for Shimura varieties* (1711.02189).
- Gao [17] (CM Galois bound, Cor. 13.4); [30]+[28] (generic transitivity);
  [24, Thm 1] (uniform Pfaffian format); Kühne / Bilu–Masser–Zannier (effective
  base modular bounds, via BJST Cor. 5.9).
