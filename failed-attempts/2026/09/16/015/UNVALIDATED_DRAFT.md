# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Rigidification of the norm-coherent H∞ orientation of height-2 Morava E-theory to an E∞ orientation

## Statement

Let p be a prime, k an algebraic extension of F_p, G a height-2 formal group law
over k, and E = E(k,G) the associated Lubin–Tate E∞-ring spectrum. Let
x : MU⟨0⟩ → E be the H∞ MU⟨0⟩-orientation corresponding, by Zhu's theorem on
norm coherence (Theorem 1.2 / Corollary 8.17), to the unique norm-coherent
coordinate on the universal deformation. Then x lifts to a map of E∞-ring
spectra MU → E, and the lift is unique up to homotopy.

In Hopkins–Lawson terms: the MX_1-orientation obtained from x extends through
MX_p to MX_{p²}, and hence to MU K(2)-locally (the K(2)-local E∞-orientation
tower is constant above p²). This is proved for every height-2 formal group law
G over any algebraic extension k/F_p (in particular for the Honda law over F_p
and for supersingular-elliptic height-2 cases). It therefore decides the target
affirmatively, including existence and uniqueness in the two required test cases.

## Proof

### 1. Uniqueness reduces to existence

E is even-periodic, so π₀ determines the underlying homotopy-commutative
orientation. Suppose f, g : MU → E are two E∞ lifts of x. Then they have the
same underlying complex orientation, and both satisfy the Ando criterion (every
H∞- and hence every E∞-orientation does). By the uniqueness theorem proved in
Section 3 below (instance of the Goerss–Hopkins / orientation-theory argument:
for E an L₂-local complex-orientable E∞-ring with K(1)_*E and K(1)_*L_{K(2)}E
even, [bu, gl₁(E)] → [Σ^∞_+CP^∞, gl₁(E)] is injective), two E∞-lifts with the
same underlying orientation are homotopic. Concretely: Zhu's theorem gives
exactly one norm-coherent coordinate, i.e. exactly one H∞ orientation extending
the K-theory orientation; any E∞ lift restricts to it. So there is at most one
E∞ lift. The remaining content is existence.

### 2. Hopkins–Lawson reduction to two lifting steps

Use the Hopkins–Lawson filtration S → MX_1 → MX_2 → … → MU with:

- Map_{E∞}(MX_1, E) ≃ Or(E) (space of complex orientations);
- for each m there is a pullback square
  Map_{E∞}(MX_m, E) → Map_{E∞}(MX_{m−1}, E) over * → Map_*(F_m, Pic(E));
- MX_{m−1} → MX_m is a rational equivalence for m > 1, a p-local equivalence
  when m is not a prime power, and a K(n)-local equivalence when m > p^n (HL,
  Theorems 1 and 32);
- for E p-local and p-torsionfree, MX_1 → E extends to MX_p iff the
  orientation satisfies the Ando criterion (HL §7).

Fix p. First arithmetically fracture E into its rationalization and its
p-completions; Map_{E∞}(MU, R) ≃ Or(R) for rational R, and π₁ of the mapping
space vanishes for even R, so it suffices to treat E p-complete. Then the
K(2)-local E∞-orientation problem is exactly:

- Step A (MX_1 → MX_p): governed by the Ando criterion. Zhu's theorem says the
  given orientation does satisfy it (norm coherence is the H∞ Ando data), so
  Step A is unobstructed.
- Step B (MX_p → MX_{p²}): the obstruction lives in
  π₀Map_*(F_{p²}, Pic(E)) ≅ E¹(Σ^∞F_{p²}); the tower is K(2)-locally constant
  above p², so no further steps are needed.

Moreover at π₀ Step B is already solved by norm coherence: the degree-p² Ando
equation factors through degree-p data, because norms compose along chains of
degree-p isogenies (N_{ψ∘φ} = N_ψ ∘ N_φ; verified explicitly on the Honda
special fiber in the accompanying artifact, where ker[2] provably has a unique
order-2 subgroup and N_{[2]} = N_F ∘ N_F). Since Zhu's coordinate is compatible
with the norm for every finite-subgroup isogeny — not only degree p — the
π₀-level MX_{p²} Ando datum is forced by, and consistent with, the MX_p datum.
The only possible remaining failure is higher-homotopy coherence, i.e. the
class in E¹(Σ^∞F_{p²}), which is killed by evenness (Step 3).

### 3. Vanishing of the MX_{p²} obstruction for height ≤ 2 even E

Lemma. Let E be p-complete Landweber exact with π_*E even. Then
E_{2n}(F_p) ≅ E_{2n+1}(F_{p²}) ≅ 0 for all n.

Proof. By Arone–Lesh, (Σ^∞F_m)_{p̂} is null unless m = p^k, when it is a
summand of Σ^k(S^{2p^k})_{hΓ_k} for explicit finite groups Γ_k (central
extensions of F_p^{2k} by S¹) with finite-index extraspecial subgroups Γ_k^{(n)}.
Since E_*((S^{2p^k})_{hΓ_k}) ≅ Ẽ_{*−2p^k}(BΓ_k), it suffices that E_*(BΓ_k) be
even for k ≤ 2. The fibration BΓ_k^{(n)} → BΓ_k → BS¹ and its
Atiyah–Hirzebruch spectral sequence propagate evenness from BΓ_k^{(n)} to
BΓ_k. Evenness of Morava K-theory K(n)_*(BΓ_k^{(n)}) for k ≤ 2 is known:
Tezuka–Yagita for k = 1 at all p; Schuster–Yagita for k = 2 at p = 2;
Yagita for Γ_2^{(2)} at odd p. Strickland's lemma (Lemma 8.25) transports
K(n)-evenness to E-evenness for p-local Landweber exact even E. ∎

Applied to E = E(k,G) (p-complete, Landweber exact, even-periodic): the fiber
sequence Map_{E∞}(MX_{p²}, E) → Map_{E∞}(MX_p, E) → Map_*(F_{p²}, Pic(E)),
together with Map_*(F_m, Pic(E)) ≃ Hom(Σ^∞F_m, ΣE) (Σ^∞F_m is (2m−1)-connected),
shows the obstruction to Step B is E¹(Σ^∞F_{p²}) = 0 by the Lemma (p-complete
case included). Hence π₀Map_{E∞}(MX_{p²}, E) → π₀Map_{E∞}(MX_p, E) is
surjective: every Ando orientation extends to MX_{p²}, hence K(2)-locally to MU.

Fracture-square descent (Section 2 proof above) promotes the p-complete lift to
an integral E∞-orientation MU → E lifting x. This gives existence.

### 4. Uniqueness (homotopy)

E(k,G) is L₂-local, complex-orientable, and for height ≤ 2 Landweber exact even
E one has K(1)_*E and K(1)_*L_{K(2)}E even (K(1)_*E ≅ K(1)_*MU ⊗_{π_*MU} π_*E,
and K(1)_*MU is even; L_{K(2)}E is again Landweber exact even by the appendix
lemma). The orientation-theory criterion then gives injectivity of
[bu, gl₁(E)] → [Σ^∞_+CP^∞, gl₁(E)] via the fiber sequence for gl₁(E)∧_p over
L_{K(1)⊕K(2)}gl₁(E), the 3-coconnectivity of the K(2)-local fiber, and the
torsion-freeness lemma ([KUp, L_{K(1)}E] torsionfree, [ΣKUp, L_{K(1)}E] = 0 for
MU-modules E with K(1)_*E even). Hence any two E∞-lifts of the same complex
orientation are homotopic. Combined with Zhu uniqueness of the norm-coherent
coordinate, the E∞ lift of x is unique up to homotopy.

### 5. Test cases

The argument uses only: k algebraic over F_p (so Zhu's Theorem 1.2 applies),
G of height exactly 2 (so the K(2)-local tower stops at p² and the k ≤ 2
evenness input applies), and E(k,G) even-periodic Landweber exact. The Honda
formal group law over F_p ([p](x) = x^{p²} up to coordinate change) and any
supersingular-elliptic height-2 formal group law satisfy these hypotheses, so
existence and uniqueness hold in both required cases — indeed uniformly over
all height-2 G and all algebraic k/F_p.

## Computation (artifact)

`output/artifacts/honda_norms.py` (reproducible; sympy only): constructs the
Honda height-2 formal group law F(x,y) = x + y + x²y² over F₂ mod total degree
9 by solving associativity + [2](x) = x⁴ degree by degree; verifies associator
≡ 0 and [2](x) = x⁴; classifies order-2 subgroup schemes of ker[2]:
J_b = (x² + bx), b ∈ F₂ — J_0 is comultiplication-stable (Δ = 0 in the normal
form) while J_1 is not (normal form uv ≠ 0), so the Frobenius subgroup is the
unique order-2 subgroup (connectedness); checks Frobenius-norm
multiplicativity N_F(gh) = N_F(g)N_F(h) on 200 random polynomial pairs; and
checks the norm-tower identity N_{F²}(g) = N_F(N_F(g)) coefficientwise
(a_i ↦ a_i⁴ = a_i over F₂). This is the π₀ shadow of the MX₂-step Ando
factorization at the special fiber. Output log: `honda_norms.log`.

## References consulted (method blocker only; no Admission re-review)

- M. J. Hopkins, T. Lawson, Strictly commutative complex orientation theory,
  Math. Z. 290 (2018) — MX tower, Theorems 1/32, F_m spaces, MX_1 → MX_p ⟺ Ando.
- A. Senger, Obstruction theory and the level n elliptic genus, arXiv:2203.13743
  (Compos. Math. 2023) — Theorem 1.4 / Corollary 1.5: height ≤ 2 even Landweber
  exact E∞-rings: Ando ⟹ unique E∞ lift; §§2–3 proofs used (Arone–Lesh,
  Tezuka–Yagita, Schuster–Yagita, Yagita, Strickland Lemma 8.25, HL tower).
- Y. Zhu, Norm coherence for descent of level structures (Thm 1.2 / Cor 8.17):
  unique norm-coherent coordinate ⟹ H∞ orientation x: MU⟨0⟩ → E satisfying Ando.
- A. Mazel-Gee / Goerss–Hopkins references for the uniqueness/orientation-theory
  input; Balderrama (periodic refinement, cited in Senger Remark 1.6/3.6).

## Limitations and uncertainty

- The higher-coherence vanishing (Lemma, k ≤ 2 evenness) is quoted from the
  literature chain (Senger §2.2; ultimately TY89/SY04/Yag05 + Strickland +
  Arone–Lesh + HL) rather than re-proved; statements were verified by reading
  the extracted text of Senger but the cited sources' proofs were not
  independently re-derived here.
- The computation covers the Honda special fiber over F₂ (p = 2) to finite
  order (degree < 9) and random sampling for multiplicativity; it evidences,
  but does not replace, the general norm-compatibility theorem of Zhu.
- Rational fracture-square descent details follow Senger's proof; no new
  subtlety is claimed there.
- Claimed scope: height exactly ≤ 2 and k algebraic over F_p. Nothing is
  claimed at height ≥ 3 (Question 2.5 / Problem 1.11 in Senger remain open) or
  for non-algebraic residue fields.
