# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Unitary conjugacy is not Borel reducible to =⁺

## Theorem
Let H be separable infinite-dimensional, U(H) with the strong operator topology,
C_unit unitary conjugacy, and =⁺ equality of countable sets of reals on ℝ^ℕ.
Then C_unit is **not** Borel reducible to =⁺.

## Proof
Write E₂ for the l²-translation equivalence on ℝ^ℕ:
x E₂ y ⟺ Σₙ(xₙ−yₙ)² < ∞. We show E₂ ≤_B C_unit and E₂ ≰_B =⁺;
transitivity of Borel reducibility then gives C_unit ≰_B =⁺.

### 1. E₂ Borel reduces to equivalence of product measures
Fix the logistic homeomorphism h: ℝ → Y=(0,1), h(t)=1/(1+e^{−t}).
For x ∈ ℝ^ℕ put μˣ = ⊗ₙ h_∗N(xₙ,1) ∈ P(Y^ℕ).
The map x ↦ μˣ is continuous (hence Borel): if x^{(k)}→x coordinatewise,
each finite marginal ⊗_{j≤n} h_∗N(x^{(k)}_j,1) converges weakly (Gaussian
densities vary continuously in the mean), and convergence of all finite
marginals implies weak convergence on the countable product Y^ℕ.

Hellinger affinity of N(a,1), N(b,1): with d=a−b,
ρ = ∫ √(p_a p_b) = ∫ (2π)^{−1/2} exp(−((s−a)²+(s−b)²)/4) ds.
Since (s−a)²+(s−b)² = 2(s−(a+b)/2)² + d²/2, the integrand is
e^{−d²/8} times the N((a+b)/2,1) density, so ρ(a,b) = e^{−d²/8}.
Pushforward by the fixed injective h preserves affinities, so the factor
affinities of μˣ, μʸ are ρₙ = exp(−(xₙ−yₙ)²/8).

Kakutani's criterion (Kakutani 1948): for product measures with pairwise
equivalent factors, ⊗μₙ ∼ ⊗νₙ ⟺ Πₙρₙ > 0 ⟺ Σₙ(−log ρₙ) < ∞,
else they are orthogonal. Here −log ρₙ = (xₙ−yₙ)²/8, so
μˣ ∼ μʸ ⟺ Σₙ(xₙ−yₙ)² < ∞ ⟺ x E₂ y.

Fix a Borel isomorphism Ψ: Y^ℕ → [0,1] (Kuratowski; any two uncountable
Polish spaces are Borel isomorphic) and put ν_x = Ψ_∗μˣ ∈ P([0,1]).
Pushforward along a fixed Borel isomorphism is Borel and preserves
(non-)equivalence, so x ↦ ν_x is Borel and ν_x ∼ ν_y ⟺ x E₂ y.
Each μˣ is non-atomic (product of non-atomic factors), Ψ is bijective,
hence every ν_x is non-atomic.

### 2. Measure equivalence Borel reduces to unitary conjugacy
Identify [0,1] with 𝕋 via t ↦ e^{2πit}. For a probability measure ν on 𝕋
let M_ν be multiplication by z on L²(ν). Fix the enumeration
u₀=1, u₁=z, u_{−1}=z^{−1}, … of trigonometric monomials; their span
(trigonometric polynomials) is uniformly dense in C(𝕋), hence dense in
every L²(ν). If ν is non-atomic the uⱼ are linearly independent in L²(ν):
indeed a non-zero trigonometric polynomial has only finitely many zeros,
and a non-atomic measure gives zero mass to finite sets, so no non-trivial
finite linear combination vanishes ν-a.e. (else a cofinite set would be
ν-null, contradicting ν(𝕋)=1).

Hence Gram–Schmidt on (uⱼ) yields, for every non-atomic ν, an orthonormal
basis eⱼ(ν) of L²(ν) and a unitary G_ν: L²(ν) → ℓ². Set
U_ν = G_ν M_ν G_ν^{−1} ∈ U(ℓ²). Each Gram–Schmidt step uses only integrals
∫ ḡ₁g₂ dν of fixed bounded continuous functions (continuous, hence Borel in
ν for the weak topology), field operations, √·, and division by strictly
positive norms; the matrix entries ⟨U_ν ξ,η⟩ are therefore Borel functions
of ν, so ν ↦ U_ν is Borel for the SOT Borel structure on U(ℓ²).

Claim: for non-atomic ν,λ, U_ν is unitarily conjugate to U_λ ⟺ ν ∼ λ.
(⇒) The vector 1 is cyclic for M_ν with spectral measure ν. If
W: L²(ν)→L²(λ) intertwines M_ν,M_λ, then g=W1 is cyclic for M_λ with the
same spectral measure, i.e. ν(E)=∫_E|g|²dλ. Cyclicity forces g≠0 a.e.
(any positive-measure zero set would support L² functions orthogonal to all
p·g), so ν ∼ λ. (⇐) If ν ∼ λ, f ↦ f·(dν/dλ)^{1/2} intertwines the
multiplication operators.

Composing, x ↦ U_{ν_x} ∈ U(ℓ²) is Borel and
x E₂ y ⟺ ν_x ∼ ν_y ⟺ U_{ν_x} C_unit U_{ν_y}. Thus E₂ ≤_B C_unit.

### 3. E₂ is turbulent, hence not reducible to =⁺
The additive group ℓ² (Polish in ‖·‖₂) acts continuously by translation on
ℝ^ℕ (product topology); its orbit equivalence is E₂. This action is
turbulent (Hjorth's canonical example):
- Every orbit x+ℓ² is dense: y is approximated by points agreeing with y on
  the first N coordinates and with x afterwards (finite, hence ℓ²,
  modifications).
- Every orbit is meager: x+ℓ² = ∪_k{y: Σ(yₙ−xₙ)²≤k}, each piece closed
  (partial sums continuous, sup lower semicontinuous) and nowhere dense
  (a basic open set constraining finitely many coordinates is escaped by a
  large spike far out).
- Local orbits are somewhere dense: let U fix the first N coordinates within
  ε and V contain the ℓ²-ball of radius r. Any z agreeing with x beyond some
  M and in U is reached from x by successive single-coordinate increments of
  size <r, all intermediate points staying in U; such points are dense in U.

By Hjorth's turbulence theorem (Hjorth 2000; cf. Gao, *Invariant Descriptive
Set Theory*, Ch. 7), every turbulent orbit equivalence is generically =⁺-
ergodic: any Borel homomorphism to =⁺ maps a comeager set into a single =⁺
class. Since each E₂ class is meager, a comeager set contains two E₂-
inequivalent points, so no Borel map can simultaneously be E₂→=⁺ class-
injective on classes and constant on a comeager set. Hence E₂ ≰_B =⁺.
(Equivalently: E₂ ≰ any S∞-action orbit equivalence, while =⁺ ≤ isomorphism
of countable structures, Friedman–Stanley 1989.)

### 4. Conclusion
If C_unit ≤_B =⁺, composing with E₂ ≤_B C_unit would give E₂ ≤_B =⁺,
contradiction. Therefore no Borel f: U(H) → ℝ^ℕ satisfies
U C_unit V ⟺ f(U) =⁺ f(V). That is, unitary conjugacy is not Borel
reducible to =⁺. ∎

## Black boxes used (all classical)
Kakutani's product-measure dichotomy (1948); Kuratowski Borel isomorphism;
Hjorth's theorem that turbulent actions are generically =⁺-ergodic.
All novel steps — the explicit Gaussian/Kakutani computation, the Borel
Gram–Schmidt coding of measures by cyclic multiplication unitaries with the
cyclicity/spectral-type argument, and the direct turbulence verification —
are proved above. The Hellinger identity ρ=e^{−d²/8} is verified numerically
in output/artifacts/gaussian_affinity.py.
