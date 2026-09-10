# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified obstructions and a measurable lower bound for the degree-5 Z²∗C₂ Schreier cell

## 1. The cell

Let Γ = Z² ∗ C₂ = ⟨a,b,c | [a,b]=1, c²=1⟩, S = {a,a⁻¹,b,b⁻¹,c},
X = Free(2^Γ) the free part of the Bernoulli shift with product measure μ,
and G the Borel Schreier graph on X induced by S (max degree 5).
Write elements in free-product normal form: alternating non-trivial syllables;
equivalently block form B₀ c B₁ c … c Bₖ with every interior Bᵢ ∈ Z² ∖ {0}
(end blocks possibly 0). The representative used in the accompanying code is
exact: right multiplication by a^{±1}, b^{±1} adds to the last block, and
right multiplication by c appends a final 0-block (never triggering a merge,
so the c-count rises by exactly one); the merge rule
[…,B,0,B′,…] → […,B+B′,…] for interior 0-blocks enforces interior-nonzeroness.
Normal-form uniqueness is the standard free-product theorem.

**Theorem 1 (certified census).** Cay(Γ,S) is bipartite of degree 5 at e,
has girth 4 (exactly 4 distinct 4-cycles through e, all from [a,b]=1; no
3- or 5-cycles: closed non-backtracking walks at e number 0,0,8,0 at lengths
3,4,5,6 up to the conventions of the code), and balls B₀…B₆ have sizes
1,6,22,70,214,646,1942 (growth factor ≈ 3).
*Proof of bipartiteness.* ψ(T) = (Σ block coordinates + #c-symbols) mod 2
flips along every generator: an A-move changes the coordinate sum by ±1 with
#c fixed; a right c-move appends a fresh final 0-block (no merge possible,
appended block is last, old interior blocks stay nonzero), so the sum is
fixed and #c rises by one. ∎
The counts, degree, and walk numbers are machine-certified by
`output/artifacts/cayley_cell.py` → `cell_census.json` (replay: run the script).
*Consequence.* Every finite subgraph is bipartite, hence 3-colourable
(χ=2); there is no finite 4-chromatic obstruction. The target's gap framing
(ordinary χ=2 vs measurable/Borel thresholds) is intact.

## 2. Measurable lower bound χ_μ(G) ≥ 3 (rigorous proof)

**Lemma 2 (Neumann-splicing ergodicity).** Every infinite subgroup H ≤ Γ acts
ergodically on (Free(2^Γ),μ); in fact the action is mixing along H.
*Proof.* Free(2^Γ) is conull: Fix(g) is null for every g≠e (g of infinite
order forces infinitely many independent bit-equalities along a coset ladder;
g of order 2, a conjugate of c, partitions Γ into moved pairs, again infinitely
many independent equalities). Let A,B ⊂ Free(2^Γ) have positive measure and
approximate them by cylinders U₁,U₂ on finite supports F₁,F₂ with
μ(A∩U₁) > μ(U₁)−ε, μ(B∩U₂) > μ(U₂)−ε, μ(Uᵢ) close to μ(A),μ(B).
For h ∈ H with hF₂ ∩ F₁ = ∅, independence across disjoint supports gives
μ(U₁ ∩ hU₂) = μ(U₁)μ(U₂). The set {h ∈ H : hF₂ ∩ F₁ ≠ ∅} is finite (a subset
of the finite set in Γ), and H is infinite, so such h exists; for small ε,
μ(A ∩ hB) ≥ μ(U₁)μ(U₂) − 2ε > 0. Hence every pair of positive-measure sets
meets along H, which is equivalent to ergodicity. ∎
*Finite-pattern extension (used below and in §3).* Every finite partial
assignment extends to a point of Free(2^Γ): extend arbitrarily, then for each
h_n ≠ e in an enumeration pick fresh vertices v_n, h_nv_n outside all
previously constrained vertices (possible since Γ is infinite) and set bits
to break h_n-periodicity. Countably many steps keep the constrained set finite
at each stage.

**Theorem 3.** χ_μ(G) ≥ 3: no measurable 2-colouring of G exists.
*Proof.* Suppose c: X → {0,1} is measurable and proper on a conull invariant
Y. Both colour classes are positive: otherwise the conull class contains an
edge with both endpoints in it. Let C = c⁻¹(0), so μ(C) ∈ (0,1).
Properness along a-edges gives a(C∩Y) = Y∖C exactly on Y, and a preserves μ,
so μ(C) = 1/2. Applying twice, a² preserves C mod null; b swaps C mod null.
Hence t := a²b swaps C with its complement mod null (tC = Y∖C up to nulls, by
equal measure 1/2). Then t² preserves C mod null. Now t = a²b is the grid word
(2,1) ≠ 0 in the Z² factor, so t has infinite order (machine-checked:
tⁿ ≠ e for 1 ≤ n ≤ 50, and grid arithmetic gives all n; see
`ergodic_facts.py`), and ⟨t²⟩ is an infinite subgroup, hence ergodic by
Lemma 2. A mod-null-preserved set for an ergodic transformation is null or
conull (pass to C minus the null union ∪_{n∈Z} t^{2n}(C Δ t²C), exactly
invariant), contradicting μ(C)=1/2. ∎
Group facts used (t of infinite order, a^{2n} never an S-neighbour, ⟨a⟩-orbit
distinctness) are machine-checked in `output/artifacts/ergodic_facts.py`.

## 3. Radius-1 factor 3-colouring is impossible (certificate)

**Theorem 4.** No radius-1 clopen (factor) rule F:{0,1}^{B₁} → {1,2,3} can
properly colour G, where B₁ = {e,a,a⁻¹,b,b⁻¹,c}.
*Proof.* Any factor rule must satisfy F(P) ≠ F(P′) for every realizable pair
(P,P′) = (z|_{B₁},(s·z)|_{B₁}), s ∈ S, z free. By the extension lemma every
finite pattern on B₁ ∪ sB₁ extends to a free global configuration, so the
realizable pairs are exactly those from all 2^{|B₁∪sB₁|} assignments.
Exhaustive enumeration (`sft_radius1.py` → `sft_radius1.json`) over all
s ∈ S builds the 64-vertex constraint graph (1539 edges) and finds **46 loops**:
patterns P with (P,P) realizable, forcing F(P)≠F(P) — impossible. Hence no
radius-1 factor 3-colouring exists. The loop patterns are listed in
`sft_radius1.json`. ∎

## 4. No O(log* n) LOCAL 3-colouring rule: audit Step-3 premise is false

**Theorem 5.** ⟨a, v⟩ with v = cac is free of rank 2; each ⟨a,v⟩-orbit spans a
4-regular infinite tree in G. Consequently no O(log* n) deterministic LOCAL
3-colouring rule exists for this cell.
*Proof of freeness (exact).* A reduced word
w = a^{e₀}v^{k₁}a^{e₁}…v^{k_m}a^{e_m} (kᵢ≠0; eᵢ≠0 except possibly e₀,e_m)
expands to a^{e₀}ca^{k₁}ca^{e₁}c…ca^{k_m}ca^{e_m}. Every c is separated by a
nonzero Z²-block (kᵢ≠0; interior eᵢ≠0), so the fused form is a valid normal
form with ≥2 c-symbols if m≥1, or a^{e₀}≠e if m=0; by uniqueness w≠e. ∎
Tree embedding is machine-certified exact to depth 6 (layers 1,4,12,36,108,
324,972 in `local_lowerbound.json`). The LOCAL conclusion uses the classical
Θ(log n) deterministic-LOCAL lower bound for 3-colouring bounded-degree trees
(Chang–Kopelowitz–Pettie line; cf. Brandt et al. 2022 for the forest
LOCAL theory cited in the admission): an O(log* n) rule for the cell would
restrict to one for 4-regular trees, impossible. Hence the audit plan's Step 3
("lift an O(log* n) LOCAL 3-colouring rule through an explicit toast") has a
false premise as stated; a Borel 3-colouring, if it exists, needs a different
ingredient.

## 5. Quantitative LLL failure + local-repair experiment (computed evidence)

For uniform random 3-colouring, edge-bad probability p=1/3 with dependency
degree d=8 gives symmetric-LOVász value e·p·(d+1) ≈ 8.15 ≫ 1; uniform LLL
would need ≥25 colours, and the best non-uniform edge-bad probability is still
1/3 (`lll_log.py`). Operationally, seeded random 3-colourings of Cayley balls
(R=3,4,5) followed by greedy sweeps and 20k-step bounded Moser–Tardos
resampling never reach a proper colouring on any R≥4 trial (residual 57–204
bad edges; `recover_test.py`). This is heuristic finite-ball evidence,
recorded as a recovery test — not a theorem — showing the LLL failure is
operational and no easy local fix exists.

## 6. Status of the target

Proved: ordinary finite 3-colourability (§1) and χ_μ ≥ 3 (§2) — the lower half
of the measurable threshold. Certified obstructions: no radius-1 factor
3-colouring (§3); no O(log* n) LOCAL rule (§4); LLL/MT failure logs (§5).
Open and blocked in-session: the explicit measurable 3-colouring (χ_μ ≤ 3,
equivalently the fallback's invariant-conull Borel 3-colouring with codes)
and the Marks-type game obstruction (χ_B ≥ 4). Together these leave the full
3<4 gap certificate unproved; §2–§4 bank the reusable lower-bound and
no-go halves for any follow-up toast-lift or game attack without re-derivation.
