# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Finite Hjorth-shadow data for odometer conjugacy on minimal Cantor homeomorphisms

## Scope and honesty statement
This note proves three finite-level facts about the conjugacy action of
H = Homeo(2^N) on the Polish space M of minimal homeomorphisms of the
Cantor cube. It does **not** prove Hjorth turbulence, density of any
H-orbit in M, generic E0-ergodicity, or non-Borel-reducibility to
countable-structure isomorphism. Those infinite-level transfers remain
open; the finite data below are exactly the base-point certificates the
target programme requires, with gaps marked.

## 1. Setup
X = 2^N with product topology; P_m = partition into 2^m cylinders;
H with uniform metric; M = {minimal T in H} with subspace topology.
M is Polish: M = ∩_{A,B} ∪_n {T : T^n(A) ∩ B ≠ ∅} over clopen basis pairs,
a Gδ in the Polish group H. Basic neighbourhoods of φ are fixed by the
level-m pattern σ_m ∈ Sym(P_m). A pattern cycle is *minimality-compatible*
if it is a single cycle (necessary for minimality of any φ realising it).
V_m = {g ∈ Sym(P_{m+1}) : g preserves mod-2^m blocks} is the finite shadow
of the 2^{−m}-ball Stab(P_m) about id in H.

## 2. Theorem L1 — Local transitivity (finite Hjorth shadow)
**Statement.** Let s_m(a) = a+1 mod 2^m. Then the V_m-conjugacy orbit of
s_{m+1} equals the set of all single-cycle lifts of s_m; both have
cardinality 2^{2^m − 1}.

**Proof.** Atoms (c,ε), c ∈ Z_{2^m}, ε ∈ {0,1};
s_{m+1}(c,ε) = (c+1 mod 2^m, ε + 1_{c=2^m−1}).
*Orbit size.* g ∈ V_m is g(c,ε) = (c, ε+f(c)) for bits f(c). The equation
g·s = s·g forces f constant (compare at the carry c = 2^m−1 with
non-carry c, using that s advances the block in both cases but flips the
fiber only at the carry); constants {id, s_{m+1}^{2^m}} centralise s.
Hence Stab = {id, s^{2^m}}, |orbit| = 2^{2^m}/2 = 2^{2^m−1}.
*Lifts.* A lift ψ(c,ε) = (s_m(c), ε+f(c)) has
ψ^{2^m}(c,ε) = (c, ε+Σ_b f(b)) (each of the 2^m steps advances the block
once through s_m and adds f of the visited block; all blocks visited
exactly once). If Σf is even, ψ^{2^m} = id on 2^{m+1} points, so ψ splits
into two 2^m-cycles; if Σf is odd, ψ^{2^m} swaps the two fibers over each
block while ψ permutes blocks cyclically, giving one 2^{m+1}-cycle. Exactly
half of the 2^{2^m} lifts are single: 2^{2^m−1}.
Conjugates of the single cycle s_{m+1} by block-preserving g are single
cycles lifting s_m (conjugation preserves cycle type; block-preservation
preserves the quotient). Finite sets, same size, inclusion ⇒ equality. ∎

**Exact instances** (stdlib replay, `lane403_attack{6,8,10}.py`):
m=2: 8 lifts, orbit 8, equality (`finite_level_log6.json` B3);
m=3: 128 lifts, orbit 128 distinct, equality (`finite_level_log8.json`);
m=4: 32768 = 2^15 lifts, orbit 32768, equality (`finite_level_log10.json`).

*Reading for Hjorth.* For U = level-m neighbourhood of the binary odometer
and V = Stab(P_m)-ball, every minimality-compatible refinement at level
m+1 is realised by a V-conjugate — the exact finite pattern of
O(U,V) ≠ ∅ local density at these scales.

## 3. Lemma L2 — Twisted-product lift (constructive density shadow)
**Statement.** Let M | N, K = N/M, τ a single M-cycle. With atoms (b,j),
ψ(b,j) = (τ(b), j + 1_{b=b₀}) is a single N-cycle with M-quotient τ.
**Proof.** ψ^M(b,j) = (b, j+1): M steps visit each block once (τ single),
firing the fiber +1 exactly at b₀. So ψ^M is fiber-rotation × block-id of
order K, and ψ permutes blocks as τ: |orbit of any atom| = M·K = N. ∎
**Verification** (`lane403_attack12.py`, `finite_level_log12.json`):
exhaustive over all τ for M ≤ 6 (1, 2, 24, 120, 6 cycles), 12/12 sampled τ
for M ∈ {10,15,8}, 12/12 divisor pairs incl. 8|32 — ALL OK.
**Corollary.** Any single N-cycle (in particular the pure-odometer pattern)
is S_N-conjugate to ψ, so a conjugator g sends the odometer level-N pattern
to one with prescribed cyclic M-quotient: the odometer H-orbit meets every
cyclic-factor basic open at divisor levels.

## 4. Proposition P3 — Eigenvalue obstruction (route constraint)
(a) A p-cyclic clopen partition yields Koopman eigenvalue ζ_p = e^{2πi/p}
via f = Σ_j ζ_p^{−j} 1_{B_j}; eigenvalues are conjugacy-invariant.
(b) Binary-odometer eigenvalue group = 2-power roots only. Finite shadow:
cyclic quotient of a single 2^n-cycle has order dividing 2^n (divisor table
`finite_level_log6.json`); 2^n mod 3 ≠ 0 ∀n (`finite_level_log4.json`).
(c) So no binary-odometer-type point can carry the target's dense orbit in
full M across all cyclic factors; the witness must be eigenvalue-universal
yet non-odometer (Toeplitz almost-1-1 extension of the universal odometer
is the natural candidate). Constraint: all 60 same-fiber single-swaps at
level 30 break the 30-cycle (`finite_level_log9.json`) — coherent Toeplitz
twists need hole/growing-block design (Kaya-type), not attempted here.

## 5. Relation to the target and fallback
- Target (turbulent φ*, generic E₀-ergodicity, non-reducibility): NOT proved;
  credible route remains (Toeplitz-over-universal-odometer) but needs
  construction + density proof + turbulence transfer beyond this session.
- Preset fallback (explicit Toeplitz φ* with PROVED dense + meagre orbit):
  NOT met — density proof is unavailable; only finite-level shadows.
- This note's value (per fallback record's own retrieval clause): exact
  base-point Hjorth-shadow data (L1 counts, L2 construction) plus proved
  search constraints (P3, twist-failure census) that future work queries
  without re-coding. Originality: live-admission scan found no turbulence/
  non-classifiability theorem on M and no such finite local-transitivity
  count; the L1 orbit-stabiliser count and L2 twisted lift are new as
  stated (elementary, but previously unrecorded in this action).

## 6. Reproducibility
All in `output/artifacts/`, stdlib only:
`lane403_attack6.py` → `finite_level_log6.json` (B1/B2/B3/U1),
`lane403_attack8.py` → `finite_level_log8.json` (m=3 equality),
`lane403_attack10.py` → `finite_level_log10.json` (m=4 equality),
`lane403_attack12.py` → `finite_level_log12.json` (L2, ALL OK),
plus exploratory `lane403_attack{,2,3,4,5,7,9,11}.py` and logs
`finite_level_log{,3,4,5,7,9,11}.json` (incl. withdrawn v4/v5 claims,
superseded by corrected enumerations; see WORKLOG).
`RESULTS.md` summarises the proved statements.
