# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Cuntz-semigroup blindness of the Elliott–Niu toolkit at [0,1]∨[0,1]² vs +[0,1], with the exact surviving fiber invariant

## 1. Setting
Fix rapid growth sequences (nᵢ),(kᵢ) with 0 < rc < ∞ and let
X₁ = [0,1]∨[0,1]², X₂ = X₁∨[0,1], A₁ = A(X₁,(nᵢ),(kᵢ)), A₂ = A(X₂,(nᵢ),(kᵢ))
be the simple unital UHF–Villadsen algebras. Both seeds are contractible finite
simplicial complexes, solid, dim 2, K-contractible. Write
γ = (1/2)∏ᵢ nᵢ/(nᵢ+kᵢ) ≠ 0.

## 2. Statement (emergent finding)
(a) The generalized comparison-radius function takes the same values on both
algebras: r∞(τₓ) = γ for Dirac traces τₓ at interval-branch points and
r∞(τ_y) = 2γ for Dirac traces at square-branch points, for both A₁ and A₂.
Hence the Elliott–Niu II constant-vs-nonconstant Cuntz separation
(Corollary 5.7/5.8) provably does not distinguish this pair.
(b) Regular-stratum fiber-multiplicity lemma: on X^N minus the wedge-point
singular set, the stratum with exactly j square-coordinates (loc.dim N+j) has
C(N,j) connected components for X₁ versus C(N,j)·2^{N−j} for X₂.

## 3. Proof of (a)
Stage functions r_s(x) = (1/2)·loc.dim(x)/((n₁+k₁)⋯(n_{s−1}+k_{s−1})) converge
uniformly to r∞ (Lemma 5.2 of Elliott–Niu II). Take x on an interval branch
off the wedge point: loc.dim((x,…,x)) = n₁⋯n_s in X^{n₁⋯n_s}; take y on the
square branch: loc.dim((y,…,y)) = 2n₁⋯n_s. The Corollary 5.7 sandwich argument
with continuous majorants/minorants f,g at stage s₀ and the growth condition
(5.2)/(5.25) gives r∞(τₓ) = γ, r∞(τ_y) = 2γ. The computation uses only the
loc.dim values 1 and 2, present in both seeds; X₂'s extra interval branch only
duplicates the value γ. Thus both algebras have nonconstant r∞ with identical
range {γ,2γ}: no constancy dichotomy, so Corollaries 5.7–5.8 cannot separate them.

## 4. Proof of (b)
Write X₁ = I ∪ S, X₂ = I ∪ S ∪ I′ glued at ∗. Delete ∗: X₁∖{∗} has 2 components
(I∖{∗}, S∖{∗}); X₂∖{∗} has 3 (two punctured intervals + punctured square).
In X^N, fix which j coordinates lie on the square branch: C(N,j) choices.
Each of the remaining N−j interval coordinates contributes 1 punctured branch
in X₁ vs 2 in X₂ (I vs I∪I′). The square coordinates minus ∗ are connected.
Hence C(N,j) vs C(N,j)·2^{N−j} components. Verified for N = 2,3,4 in
artifacts/fiber_counts.txt.

## 5. Why the target remains open / value of this finding
All established invariants (Elliott invariant, numerical rc, Poulsen trace
simplex, r∞ range) agree; (a) shows the newest published Cu tool is blind here,
answering the "why not just apply Cor 5.7" question negatively. (b) quantifies
the sole surviving finite-stage seed difference (per-level entropy gap
(1−j/N)·log 2), giving any future isomorphism/non-isomorphism proof its
necessary foothold. This directly narrows the open problem flagged in
Elliott–Niu II Remark 5.10.

## 6. Limitations
Does not decide Cu(A₁) ≅ Cu(A₂); no theorem is claimed lifting (b) to Cu.
Conjecture (not claimed): the multiplicity may vanish in the limit under the
radius-of-comparison quotient; or it may survive as a Cu invariant — both open.
