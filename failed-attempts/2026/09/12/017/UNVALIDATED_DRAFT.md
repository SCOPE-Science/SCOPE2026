# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — The rank-3 trace-smoothness claim is false: uniform-trace, non-conjugate pair

## Target disproved
> In the Polish space of simple ordered rank-≤3 Bratteli diagrams with Vershik
> minimal homeomorphisms, the uniquely-ergodic good full-support locus is a dense
> Gδ comeager set on which conjugacy is smooth via the Borel trace on a fixed
> clopen partition.

We refute the smoothness half by exhibiting two systems **in the locus itself**
with identical fixed-partition trace that are not topologically conjugate.
Since completeness of the invariant fails on the locus, the conjunction is false
— independently of whether the unique-ergodicity locus is comeager.

## Fixed data (the residual vagueness, removed)
The target's "fixed clopen partition" is coding-fixed before the examples are
built: the canonical partition at a fixed finite level, i.e. the vertex-tower
cylinders. We fix level 1: U_w = tower through vertex w at level 1, w ∈ {1,2,3},
and τ(X) = (μ_X(U_1), μ_X(U_2), μ_X(U_3)) with μ_X the (unique) invariant measure.
Both systems below are built on the same vertex set, so this partition is
identified across them (standard telescoping/vertex-identification convention).
Remarkably, the collision below holds at **every** level, so no vertex-tower
choice of fixed partition can separate the pair.

## The two systems
Vertex sets V_n = {1,2,3} for all n ≥ 1; V_0 a singleton with first-edge
vector m = (1,1,1).

System X (stationary): every level n ≥ 1 has incidence matrix

    M1 = [[2,1,1],[1,2,1],[1,1,2]],   det M1 = 4, rank 3.

System Y (one non-stationary head, stationary tail): level 2 has incidence

    A = [[2,2,0],[0,0,4],[2,2,0]],    det A = 0, rank 2,

and every level n ≥ 2 has incidence M1. Both have 3 vertices at every level
(rank ≤ 3). Edges are explicitly listed by the integer entries (parallel edges
indexed 1..M(v,w)); column sums of both M1 and A are (4,4,4) and row sums are
(4,4,4), so A has no zero row or column.

Orderings (proper). X: uniform lexicographic order at every level; max-source
function s ≡ 1, min-source function t ≡ 3. Then the max path is 1^∞ (unique:
s is constant) and the min path is 3^∞ (unique). Y: at level 2 use, in
1-indexed notation, s_A = {1↦1, 2↦3, 3↦1} and t_A = {1↦2, 2↦3, 3↦2}, all with
positive entry counts (e.g. A[0][0]=2, A[1][2]=4, A[2][0]=2 for max;
A[0][1]=2, A[1][2]=4, A[2][1]=2 for min), and uniform lexicographic order with
s ≡ 1, t ≡ 3 at every level n ≥ 3. Backward induction: the max path's tail
v_2,v_3,… is forced to 1^∞ hence v_1 = s_A(1) = 1, so the max path is the
unique 1^∞; the min path is the unique 2·3^∞ (v_1 = t_A(3) = 2, tail 3^∞).
Verified by depth-6 truncation enumeration in the script. Hence both diagrams
are properly ordered with Cantor path spaces, and the Vershik maps are minimal
homeomorphisms (Herman–Putnam–Skau: simple + proper ⇒ minimal).

Simplicity. X is stationary with M1 strictly positive, hence primitive, hence
simple. For Y, A·M1 is strictly positive (min entry 4, verified) with no zero
row/column in A; thus any two vertices at levels differing by ≥ 2 connect, so
Y is simple (every pair of vertices v at level n, u at level ≥ n+2 has a path
through the A·M1 block; levels n, n+1 connect since A has no zero row/column).

Unique ergodicity + good full support. Heights satisfy h^{(n+1)} = M h^{(n)}
with h^{(1)} = (1,1,1); column sums 4 give h^{(n)} = 4^{n-1}(1,1,1) for BOTH
systems (for Y because A·m = (4,4,4) too — verified heights agree at every
level). Define single-path cylinder masses p_v^{(n)} = (1/3)/4^{n-1} ending at
vertex v of level n. Flow consistency: children of a level-n path ending at w
contribute Σ_v M1[v][w]·(1/3)/4^n = 4·(1/3)/4^n = (1/3)/4^{n-1} (column sum 4),
and at Y's level 1, Σ_v A[v][w]·(1/3)/4 = 4·(1/3)/4 = 1/3 (verified). This
defines a Borel probability invariant under the tail/Vershik action with every
vertex tower of mass exactly 1/3 > 0, hence full support; by minimality every
invariant measure has full support, and the Bratteli–Vershik unique-ergodicity
criterion (constant column sums with Perron left eigenvector (1/3,1/3,1/3);
equivalently the uniform tower-mass flow is the unique consistent one — the
strictly positive stochastic tail M1ᵀ/4 is a uniform projective contraction, so
the inverse limit of tower-mass simplices is a singleton) gives that this is
the ONLY invariant measure. So both X and Y are uniquely ergodic with
full-support measures. Goodness is proved directly, with no black box: every
level-n single-path cylinder in either system has identical mass (1/3)/4^{n−1}
(uniform heights), the systems are non-atomic (cylinder masses → 0), and every
clopen is a finite union of level-N cylinders for large N; hence any two clopen
sets of equal measure are unions of equally many equal-mass cylinders, and any
clopen U with μ(U) < μ(V) embeds measure-preservingly as a sub-union of a
cylinder refinement of V — i.e. the measures are good in Akin's sense. Thus
X, Y lie in the target's locus.

Trace collision. Tower U_w at every level has mass 1/3 in both systems, so

    τ(X) = (1/3, 1/3, 1/3) = τ(Y),

indeed at every level, not just level 1. Any coding-fixed clopen partition by
vertex towers therefore assigns X and Y the identical value.

Non-conjugacy. By Giordano–Putnam–Skau, topological conjugacy of minimal Cantor
systems induces an order-isomorphism of unital dimension groups, hence a
ℚ-linear isomorphism of K_0 ⊗ ℚ. For stationary X all bonding maps are
det-4 isomorphisms on ℚ³, so K_0(X) ⊗ ℚ ≅ ℚ³ (dimension 3; char poly
(λ−4)(λ−1)²). For Y the bonding map at level 1→2 is the rank-2 map A, and all
later maps are isomorphisms, so the direct limit factors through im(A) ⊗ ℚ ≅
ℚ² (rank A·M1 = 2 verified stable); K_0(Y) ⊗ ℚ ≅ ℚ² (dimension 2; char poly of
A is λ(λ−4)(λ+2)). Dimensions 3 ≠ 2, so X and Y are not topologically
conjugate. (Equivalently, rationalized K_0 rank is a conjugacy invariant and
differs.)

## Conclusion
X and Y are both simple rank-3 properly-ordered Vershik minimal systems,
uniquely ergodic with good full-support measures — members of the target's
locus — with identical Borel trace on the fixed clopen partition but not
topologically conjugate. The trace invariant is therefore incomplete on the
locus, and the claimed smoothness (classification by that trace) is FALSE.
The conjunction constituting the target claim is disproved. ∎

## Provenance of each ingredient (proof vs computation vs citation)
- Proof (new, in this draft): the two-system construction, height/measure
  computation, tower-mass collision, and the K_0⊗ℚ dimension argument from the
  explicit matrices. Flow-consistency identities are proved by the column-sum-4
  computation, displayed above.
- Computation (exact, replayable): `output/artifacts/verify_target.py`
  (stdlib only) checks primitivity/positivity, Perron pairs, dets, ranks,
  char polys, height agreement, flow consistency, max/min-path uniqueness
  truncations, and the trace collision — 30/30 PASS, report in
  `output/artifacts/verification_report.json`.
- Citations (classical, used as black boxes): Herman–Putnam–Skau (simple +
  proper ⇒ minimal Vershik homeomorphism); Giordano–Putnam–Skau (conjugacy ⇒
  K_0 order-isomorphism, hence K_0⊗ℚ invariant). Unique ergodicity and goodness
  are proved directly from the explicit uniform tower-mass data (see above),
  not cited. No unpublished or AI-generated mathematics is cited.

## Limitations / what is NOT claimed
- We do not decide whether the uniquely-ergodic locus is comeager; the target
  conjunction is already false via the smoothness half.
- Smoothness in the full descriptive-set-theoretic sense also requires the
  invariant to be Borel and the relation Borel; our refutation targets
  completeness (two same-trace non-conjugate systems), which already defeats
  classification-by-trace on the locus.
- Simplicity, properness, and good-measure claims rest on the classical
  theorems cited; the novel content is the explicit colliding pair.
