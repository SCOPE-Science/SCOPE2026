# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified low-level NPA collapse for a named 4-input graph game (H4-GRAPH)

## 1. Instance (fixed in this report; shape as admitted)

Classical inputs to this lane provided no explicit question/predicate file — only the
shape: a 4-input (2×2) binary linear graph BCS game at NPA level 1+AB with classical
value strictly below the relaxation. We therefore FIX one precise instance here, and
prove the collapse for exactly that instance:

**H4-GRAPH.** Two questions per party (x, y ∈ {0,1}), binary answers a, b ∈ {±1},
graph incidence `G = [[2,1],[1,1]]` with edge signs `s = [[+,+],[+,-]]`.
The Bell functional (bias form) is

    B := 2<A0 B0> + <A0 B1> + <A1 B0> − <A1 B1>,        (total weight M = 5)

and the game value is `ω = 1/2 + B/(2M) = 1/2 + B/10`.
Equivalently: one 2-vs-2 nonlocal comparison on horizontal inputs plus a minus-sign
triangle on the remaining three edges — a fixed small nonplanar incidence fragment
with parity constraints. The multiplicities (2,1,1,1) record a doubled edge; all
weights and signs are committed constants of the instance, not a parameter sweep.
This instance is distinct from uniform-weight magic-rectangle tables and from the
tilted-CHSH families of the surveyed prior work.

## 2. Result

**Theorem.** For H4-GRAPH:

- classical bias βc = 3 exactly, i.e. ωc = 0.8;
- NPA 1+AB optimum = commuting-operator value = λ := (3/2)√6 ≈ 3.67423,
  i.e. ω*(H4-GRAPH) = 1/2 + 3√6/20 ≈ 0.86742, attained;
- the optimum carries a flat-extension rank loop: the 9×9 level-1+AB optimal moment
  matrix Γ has rank exactly 4 and its level-2 extension keeps rank 4, so a
  finite-dimensional tracial representation attains the bound.

Hence the NPA hierarchy collapses onto the commuting-operator value already at
level 1+AB for this natural small graph game, and the equality is certified by an
exact sum-of-squares identity plus an explicit optimal strategy — not by solver
tolerance.

## 3. Proof

Work with ±1 observables: Ax² = By² = I, and [Ax, By] = 0 on the bipartite
(commuting-operator) algebra. Let T₀ := 2A₀+A₁, T₁ := A₀−A₁, so B = T₀B₀+T₁B₁.

### 3a. Classical value (exact enumeration)

For deterministic assignments (a₀,a₁,b₀,b₁) ∈ {±1}⁴ the bias is
2a₀b₀+a₀b₁+a₁b₀−a₁b₁ ∈ {±5,±3,±1}, and (1,1,1,1) gives 2+1+1−1 = 3.
Grouping on (b₀,b₁): if b₀=b₁=β then B=β(3a₀+a₁) ≤ 4 over ±1 but ≡ odd, so ≤ 3;
if b₀≠b₁ the same parity argument gives |B| ≤ 3. Hence βc = 3, ωc = 0.8. ∎

### 3b. Dual (upper) bound: exact SoS identity inside span(S_{1+AB})

Choose ℓ₀ := √6, ℓ₁ := √6/2. Set E₀ := ℓ₀B₀−T₀, E₁ := ℓ₁B₁−T₁.
Both E₀, E₁ lie in span(S_{1+AB}) = span{I, A₀, A₁, B₀, B₁}.
Claim, as an exact operator identity on any commuting-operator representation
(using only Aₓ² = By² = I and [Aₓ,By] = 0):

    λI − B = E₀²/(2ℓ₀) + E₁²/(2ℓ₁),     λ := (3/2)√6.          (★)

Proof. Since Alice-side Tₓ commutes with Bob-side By, (ℓB−T)² = ℓ²I + T² − 2ℓTB,
so Eₓ²/(2ℓₓ) = ℓₓI/2 + Tₓ²/(2ℓₓ) − TₓBₓ. Moreover T₀B₀+T₁B₁ = B term by term
(T₀B₀ = 2A₀B₀+A₁B₀, T₁B₁ = A₀B₁−A₁B₁). Hence

    λI − B − ΣₓEₓ²/(2ℓₓ) = (λ − (ℓ₀+ℓ₁)/2)I − T₀²/(2ℓ₀) − T₁²/(2ℓ₁).

Write S := A₀A₁+A₁A₀. From Aₓ² = I: T₀² = (2A₀+A₁)² = 5I+2S and
T₁² = (A₀−A₁)² = 2I−S. The S-coefficients are 2/(2ℓ₀) = 1/√6 from T₀² and
−1/(2ℓ₁) = −1/√6 from T₁² — they cancel exactly. The scalar remainder is

    (3√6/2) − (√6/2+√6/4) − 5/(2√6) − 2/√6 = 3√6/4 − 9/(2√6) = 0.

Thus (★) holds identically. Since each Eₓ² ≥ 0 in every commuting-operator
representation, ⟨B⟩ ≤ λ for every commuting-operator state — and in particular
Tr(BΓ) ≤ λ for every NPA 1+AB feasible moment matrix, whose certificate space
contains exactly the squares of span(S_{1+AB}). The accompanying script confirms
the residual vanishes (max-abs < 1e−15) and complementary slackness Eₖ|ψ⟩ = 0
holds at the optimal strategy. ∎

### 3c. Primal: explicit 2-qubit strategy attaining λ

Take |ψ⟩ = |Φ⁺⟩ = (|00⟩+|11⟩)/√2 and X–Z-plane observables along

    u₀ = (1,0,0),          u₁ = (1/4, 0, √15/4),
    v₀ = T̂₀,              v₁ = T̂₁,     T₀ = 2u₀+u₁,  T₁ = u₀−u₁,

i.e. Aₓ = uₓ·σ ⊗ I, By = I ⊗ v_y·σ. For |Φ⁺⟩, ⟨AₓBy⟩ = uₓ·v_y exactly, giving

    ⟨A₀B₀⟩ = 3√6/8 + … = 9/(4√6)+…; precisely
    (c₀₀, c₀₁, c₁₀, c₁₁) = (3√(3/2)/4, √(3/2)/2, √(3/2)/2, −√(3/2)/2),

so 2c₀₀+c₀₁+c₁₀−c₁₁ = (3/2)√6 = λ exactly (sympy-exact in the verifier).
The state's 1+AB moment matrix Γ (9×9, Γᵤᵥ = ⟨ψ|u†v|ψ⟩) is real positive
semidefinite with unit diagonal, satisfies all level-1+AB NPA constraints
(projectivity, [Aₓ,By] = 0 entries, normalization), and has value λ. ∎

### 3d. Commuting-operator value and collapse

§3b bounds every commuting-operator model by λ; §3c attains λ with a
finite-dimensional (2-qubit) model. Hence ωqc(H4-GRAPH) = λ, attained.
Since NPA 1+AB is a relaxation of the commuting set bounded above by λ (§3b)
and feasible at λ (§3c), its optimum equals λ as well. The 1+AB relaxation is
therefore exact. ∎

### 3e. Flat extension (rank loop) and tracial representation

The nine moment vectors {w|ψ⟩ : w ∈ S_{1+AB}} all live in ℂ⁴. The exact Gram
minor on columns {I, A₀, B₀, A₀B₀} has determinant 25/1024 ≠ 0 (exact sympy
computation), so rank(Γ_{1+AB}) ≥ 4, hence rank = 4 exactly. All sixteen
level-2 word-vectors (degree ≤ 2 per party and their products) also live in ℂ⁴
and contain the same nonzero 4×4 minor, so any level-2 extension moment matrix
has rank exactly 4 = rank(Γ_{1+AB}): the rank loop closes and Γ_{1+AB} admits a
flat extension. The GNS representation on the 4-dimensional range gives the
finite-dimensional attaining representation; |Φ⁺⟩ has maximally mixed
single-party marginals, i.e. the tracial property on each local algebra. ∎

## 4. Numbers

| quantity | value |
|---|---|
| classical bias βc / game value | 3 / 0.8 |
| NPA 1+AB optimum | (3/2)√6 ≈ 3.6742346142 |
| commuting-operator value | (3/2)√6 attained (2-qubit) |
| game value ω* | 1/2+3√6/20 ≈ 0.8674234614 |
| rank(Γ_{1+AB}) / rank(Γ^{(2)}) | 4 / 4 (loop closed) |
| exact Gram minor det | 25/1024 |

## 5. Reproduction

Run `python3 output/artifacts/verify_h4.py` (requires only numpy + sympy).
It replays: (1) exhaustive classical enumeration → 3; (2) exact correlators and
bias (3/2)√6 with strict gap 0.674…; (3) SoS residual < 1e−15 and Eₖ|ψ⟩ = 0;
(4) exact 4×4 Gram minor det 25/1024, rank-4 loop over all 16 level-2
word-vectors. Expected output ends with `VERIFY_OK`.

## 6. Scope and limits

- The collapse is proved for the H4-GRAPH instance fixed in §1 (weights
  (2,1,1,−1)); it does not claim any universal finite-level exactness, which
  the surveyed counterexamples refute elsewhere.
- The dual bound is a single exact operator identity using only relations visible
  at level 1+AB (Aₓ² = By² = I, [Aₓ,By] = 0); no dimension assumption, no
  Cauchy–Schwarz step, and no scalar-profile maximization are needed.

## 7. Prior-art separation

Asymptotic NPA convergence reviews prove only limit behavior; the large-BCS
non-attainment construction and the tilted-CHSH Motzkin non-exactness result
target different games/functionals. None decides 1+AB exactness for the
(2,1,1,−1)-weighted 2×2 graph game here, whose SoS certificate and rank loop
are new.
