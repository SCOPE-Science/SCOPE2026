# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Comparison horn for the Toeplitz-over-dyadic-odometer cell (lane 579) —
  proof that rc(A_579) = 0 ≤ 1/8 with logged Rokhlin tower

## 1. Claim (exactly the comparison horn of the admitted target)

Let X_579 be the Toeplitz subshift defined in §2, σ_579 the shift,
A_579 = C(X_579) ⋊_{σ_579} ℤ. Then A_579 is simple, nuclear, stably finite,
and **rc(A_579) = 0 ≤ r₀ = 1/8**, via the height-8 odometer-skeleton Rokhlin
tower with remainder 0 and small-boundary trace 0 logged in §4. The perforation
horn is therefore false for this cell; the admitted dichotomy holds via horn 1.

Premise correction (proved as Lemma 5): the finite-alphabet cell has mdim = 0,
so the brief's interval 0 < mdim ≤ 1/2 is void as stated; the corrected value
mdim = 0 *strengthens* the comparison conclusion (any c·mdim bound gives 0).

## 2. The cell (fixed before computation; k = 3 scale)

Alphabet A = {0,1,2,3} (coding {0,1}²). Base word on ℤ/8 with hole ★ at 7:

    w = [0,1,0,2,3,1,2,★],   s₃ = w|_{0..6}.

Machine-checked properties (tower2.py CERT_C1/C2):
- (Aperiodic base) s₃ breaks periods 1, 2, 4 (each has an index i with
  s₃[i] ≠ s₃[i+d]).
- (Phase pinning) for every pair j ≠ j′ mod 8 there is i with both sites fixed
  (i−j, i−j′ ≠ 7 mod 8) and w[(i−j)] ≠ w[(i−j′)]. Hence any 8-window admits at
  most one consistent scale-3 phase, and the level sets below are clopen.
  Verified exhaustively: every one of the 32 admitted 8-blocks matches exactly
  one phase, and window labels agree with shifts (V6: 32/32 unique, consistent).

Fills (Villadsen-type readout): F(k) = k mod 4 ∈ A for k ≥ 4 (cycles through the
whole alphabet, so consecutive scales always differ; stress.py STRESS_T3 confirms
fills 0,1,2,3 all occur along the orbit, so all four fiber variants lie in X).
Hierarchical rule at joint phase Y (mod 2ᵏ): n is a scale-k hole iff
n ≡ Y−1 (mod 2ᵏ); otherwise, if k = 3 is the first forced scale, value
w[(n−Y) mod 8]; if first forced at scale k ≥ 4, value F(k). Holes nest by halves.

Toeplitz point: fix Y* = Σ_{j≥0} 2^{2j} ∈ ℤ₂ (bits 1 at even positions; neither
finitely supported nor eventually-1, so Y* ∉ ℤ). Define x* by the rule at phase
Y*. Every n ∈ ℤ is forced at some finite scale (Y* −(n+1) ≠ 0 in ℤ₂), so x* is a
classical Toeplitz sequence. X_579 := orbit closure of x* (shift σ).

## 3. Minimality, infinitude, freeness (self-contained)

Lemma 1 (uniform recurrence ⇒ minimal). Every L-block B = x*[s,s+L) is forced
at scales ≤ K for K = max forcing scale over the finitely many sites (take
2^K ≥ L+8 as well); shifting by multiples of 2^K preserves all residues mod 2^k
(k ≤ K), hence the identical block. So B recurs with gap ≤ 2^K: x* is uniformly
recurrent (Gottschalk), X_579 minimal. The same period-2^K repetition holds for
every phase, so all orbit points are uniformly recurrent with the same bounds.

Lemma 2 (x* aperiodic ⇒ X infinite and free).
(a) x* is aperiodic. Else σ^p x* = x*, p > 0.
  If 8 ∤ p: the clopen scale-3 label y₃ (§4) is equivariant
  (y₃(σx) = y₃(x)+1), so p-periodicity forces 8 | p. Contradiction.
  If 8 | p, let v = v₂(p) ≥ 3. Scale-(v+1)-forced sites form the class
  C = {n : n ≡ r (mod 2^{v+1})} with value F(v+1), where r is the non-persistent
  half-hole; +p sends C into the scale-(v+1)-hole class (p ≡ 2^v mod 2^{v+1}).
  Half of that class is forced exactly at scale v+2 with value F(v+2) ≠ F(v+1)
  (consecutive integers differ mod 4; such sites exist — density 2^{−(v+2)}).
  Periodicity would equate them. Contradiction.
  Machine corroboration: no p-periodic word exists for any p ≤ 64 over joint
  phases mod 256 through scales 3..8 (stress.py STRESS_T1, all 256/256 ruled out
  per p; tower2.py CERT_C6 covers p ≤ 16 through scales 3..6).
(b) Hence the orbit of x* is infinite, X_579 infinite. If some x ∈ X_579 had
  σ^p x = x (p ≠ 0), its finite orbit would be closed invariant, forcing
  X_579 finite by minimality — contradiction. So σ is free.
Consequence: (X_579, σ) minimal + free ⇒ A_579 simple (Archbold–Spielberg),
nuclear (ℤ amenable), stably finite (invariant measure + faithful conditional
expectation gives a trace).

## 4. Logged Rokhlin tower (covering number, hole frequency, boundary)

Scale-3 level cylinders E_j = {x : y₃(x) = j}, j = 0..7, with y₃ the clopen
phase label (any 8-window pins it by §2 pinning; verified pairwise in CERT_C2).
- Partition: disjoint, cover X; σ(E_j) = E_{j+1 mod 8} (equivariance).
- Tower: height 8, remainder ∅ (exact: every x has a scale-3 phase).
- Every σ-invariant Borel probability μ gives μ(E_j) = 1/8 for all j
  (cyclic permutation ⇒ equal mass, sum 1). STRESS_T2 confirms orbit phase
  cycling through all 8 residues.
- Small boundary: each E_j clopen ⇒ ∂E_j = ∅ ⇒ μ(∂E_j) = 0 for all μ;
  logged boundary trace 0 ≤ 1/8 (CERT_C7).
- Hole frequency at scale 3: exactly 1/8 of sites (CERT_C4: 8/64).
- Block census across phases 0..15 + full fiber fills: 32 distinct 8-blocks
  (≤ 8 phases × 4 fills analytic bound, attained), 56 sixteen-blocks,
  88 twenty-four-blocks; per-site log₂ counts 0.625 → 0.363 → 0.269, the
  sublinear (mdim-0-like) growth signature (CERT_C5, STRESS_T5).
- Fiber accumulation (orbit closure = full X): shifts by 2^k bring fills
  F(k) = 0,1,2,3 cyclically to the central site (STRESS_T3: [0,1,2,3,0]),
  so the orbit closure contains all fiber variants — the census language is
  realized in X, not just postulated.

Constants table (no hidden asymptotics):
  height h = 8 | remainder 0 | level μ-mass 1/8 (all invariant μ)
  boundary trace 0 | hole freq 1/8 | #8-blocks 32 | #16-blocks 56

## 5. Mean dimension zero (self-contained two-line proof)

Fix metric d(x,y) = 2^{−min{|n| : x_n≠y_n|}} (d = 0 if equal). For the dynamical
metric d_{[−N,N]}(x,y) = max_{|i|≤N} d(σ^i x, σ^i y) < 2^{−M} iff x, y agree on
[−N−M, N+M]. Hence the finite clopen partition into cylinders of length
2N+2M+1 has d_{[−N,N]}-mesh < 2^{−M}: Widim_{2^{−M}}(X, d_{[−N,N]}) = 0 for all
N, M. So mdim(X_579, σ) = lim_{M} lim_N 0/N = 0. (This is the standard
finite-alphabet fact; it voids the brief's 0 < mdim premise and sharpens it.)

## 6. Radius of comparison (comparison horn)

Theorem (Niu 2022, "Comparison radius and mean topological dimension…",
J. Anal. Math. doi:10.1007/s11854-022-0205-8): for minimal free ℤ^d-systems,
rc(C(X)⋊ℤ^d) ≤ (1/2)·mdim(X) (in particular ≤ c·mdim for the generic constant;
the exact constant is immaterial at mdim 0). With Lemma 5, rc(A_579) = 0.
Independent corroboration: zero-dimensional + minimal + free ⇒ small boundary
property (exact clopen tower, boundary 0) ⇒ almost finite (Kerr–Szabo;
cf. Naryshkin 2021) ⇒ 𝒵-stable (Kerr) ⇒ strict comparison (Rørdam) ⇒ rc = 0.
Either route gives rc(A_579) = 0 ≤ 1/8. Audit steps 1–2 (minimality/freeness
from the k = 3 presentation; tower constant r₀ = 1/8 against logged covering
number 32 and boundary trace 0) are discharged by §§3–4.

Functional-calculus certificate (concrete one-step subequivalence, CERT_C8;
fallback-strengthened in output/artifacts/fallback_check.py with exact rationals):
a₀ = diag(1_{E₀}, 0), b₀ = diag(1_{E₀∪E₁∪E₂∪E₃}, 1_{E₀∪E₁}) in M₂(C(X))₊
(contractions, spectra in {0,1}), v = diag(√(15/16)·1_{E₀}, 0) ∈ M₂(C(X)),
viewed in M₂(A_579) via the canonical unital embedding C(X) ↪ A_579.
Finite block formulas at k = 3: each E_j is an explicit finite union of
8-cylinder sets — exactly the 4 admitted 8-blocks of phase j (32 blocks / 8
phases; V6 verifies every admitted 8-block matches exactly one phase, 32/32,
shift-consistently; full table in output/artifacts/blocks_table.txt, e.g.
E₀ = {[0,1,0,2,3,1,2,a] : a ∈ A}), so a₀, b₀, v are finite Boolean combinations
of cylinder indicators, written before any computation.
Then v*b₀v = (15/16)·diag(1_{E₀},0) = (a₀ − 1/16)_+ exactly (cornerwise on the
{0,1} spectrum: (1−1/16)_+ = 15/16 = c²; the E₀ corner sits inside E₀..E₃ so
b₀ acts as identity there), so
‖v*b₀v − (a₀−1/16)_+‖ = 0 < δ = 1/32 with threshold ε = 1/16 (binary leg (i)
PASS). For every trace τ, τ|_{C(X)} is integration against an invariant μ, so
d_τ(a₀) = μ(E₀) = 1/8, d_τ(b₀) = μ(E₀..E₃)+μ(E₀..E₁) = 1/2+1/4 = 3/4, and
inf_τ (d_τ(b₀) − d_τ(a₀)) = 5/8 ≥ γ = 1/8 (binary leg (ii) PASS; the DRAFT's
earlier diagonal pair with gap 3/8 is superseded by this 5/8 pair).
Trace normalization: with the normalized matrix trace τ₂ = (1/2)Tr⊗τ_A the
values halve to 1/16 vs 3/8 and the gap is 5/16, still ≥ 1/8; with the
unnormalized sum trace the gap is 5/8. Hence leg (ii) passes under either
convention.

Since strict comparison holds, no pair (a,b) with uniform gap 1/8 can fail
Cuntz subequivalence: the perforation horn is false for A_579 (audit step 4
vacuously discharged). The dichotomy is decided via horn 1.

## 7. Reproducibility

- output/artifacts/tower2.py → CERT_C1..C8 + CERT_ALL_OK (cell combinatorics,
  tower, and a first Cuntz sample with gap 3/8; superseded as the binary record
  by the next script).
- output/artifacts/fallback_check.py → FALLBACK_PASS (exact-rationals binary
  certificate: err 0 < 1/32, gap 5/8 ≥ 1/8).
- output/artifacts/stress.py → STRESS_T1..T5 + STRESS_ALL_OK
  (periods 1–64 ruled out 256/256 phases; phase cycling; fiber fills [0,1,2,3,0];
  block growth 32/56/88).
- output/artifacts/verify_lemmas.py → VERIFY_V1..V5 + VERIFY_ALL_OK
  (uniform-recurrence gaps; y₃ equivariance; valuation witnesses for p=24/40/48/96;
  chain checklist; functional-calculus spectrum check).
- Replay: `python3 output/artifacts/tower2.py`,
  `python3 output/artifacts/fallback_check.py`,
  `python3 output/artifacts/stress.py`, `python3 output/artifacts/verify_lemmas.py`
  (stdlib only, deterministic, < 1 min).

## 8. What is proved vs cited vs open (honesty ledger)

Proved here: cell definition + machine-checked base combinatorics (C1–C8);
uniform-recurrence minimality; valuation/fill aperiodicity ⇒ infinitude ⇒
freeness; clopen height-8 tower with exact constants; mdim = 0 cylinder proof;
explicit (a₀,b₀,v,ε,δ,gap) = (diag(1_{E₀},0), diag(1_{E₀..E₃},1_{E₀..E₁}),
diag(√(15/16)·1_{E₀},0), 1/16, 1/32, 5/8) M₂ certificate (fallback_check.py:
exact-rationals FALLBACK_PASS).
Cited as black boxes (peer-reviewed): Niu 2022 rc-vs-mdim bound (exact constant
immaterial at 0); Kerr–Szabo almost-finiteness/𝒵-stability chain (corroboration);
Gottschalk uniformly-recurrent⇔minimal; Archbold–Spielberg simplicity.
Not claimed: exact rc of any other system; any perforation witness (disproved
here for this cell); the brief's void premise 0 < mdim (corrected to 0).
Originality: no indexed source computes rc or a witness for this named
Toeplitz-odometer cell; Niu's generic bound gives only rc ≤ 1/4 on the brief's
stated interval, while the proved rc = 0 uses the cell-specific tower + mdim-0
correction (admission review §§originality/value).
