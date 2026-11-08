# Review: Volume moments detect block designs in sparse-paving matroid polytopes

## Correctness — PASS
The proof starts from the established sparse-paving hypersimplex subdivision and verifies disjoint caps directly. Dirichlet and beta moments yield the exact centroid and covariance, while cube-slice inclusion-exclusion supplies the hypersimplex second moment. The degree formula and its iff consequence require only a positive explicit coefficient. Under degree regularity, the positive pair-codegree coefficient proves the sharp two-design criterion (with the degenerate four-point exception handled). The bundled checker compared five actual indicator convex hulls with 2,199 exact-integer-volume simplices and matched their full rational covariance matrices, including the nonregular six-element pair. It also tested matroid duality and the Fano design. This finite corroboration is not an all-dimensional proof.

## Originality — PASS (provisional priority)
Ferroni's 2020 relaxation formula, Hanely et al.'s 2022 Ehrhart/volume decomposition, Joswig–Schröter's earlier compatible cuts, and Ferroni–Schröter's 2022 general valuative framework are cited as prior premises. Their inspected theorems do not evaluate the labelled continuous-volume centroid and full covariance or prove the one-/two-design rigidity. Closest database findings address unrelated geometric centers or vertex-level moments. The accessible prior area result for sparse-paving polytopes is different: even the six-element pair has the same area but can have unequal interior centroids. A previous more general labelled valuation formulation or unlocated special-case inertia calculation could reduce historical priority; that possibility remains a genuine risk.

## Mathematical value — PASS
The exact moment law converts matroid circuit-hyperplane incidence regularity into an intrinsic geometric signal, and the natural design-strength threshold precisely captures when degree-regular base-polytopes become covariance-isotropic in their canonical embedding. It also rigorously separates Ehrhart-equivalent polytopes by a continuous-volume invariant. These are meaningful complete structural classifications rather than an arbitrary numerical slice. The covariance and centroid formulas are directly reusable in geometric and matroid sampling questions.

## Scope and limitations
The theorem is limited to full-dimensional sparse-paving matroid base polytopes. It does not assert that covariance isotropy implies a two-design without the one-design hypothesis, nor does it classify higher-order moments. The proof is mathematical and self-reviewed, not independently audited. The strongest relevant general valuation theorem is explicitly credited; no theorem-strength originality is inferred merely from a failed database search.

Self-review: passed. Independent audit: not yet performed.
