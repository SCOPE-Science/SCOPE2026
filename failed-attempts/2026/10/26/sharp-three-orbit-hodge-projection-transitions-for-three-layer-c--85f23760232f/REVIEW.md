# Independent mathematical audit

## correctness

PASS

For the standard incidence orientation convention, Q=DᵀL⁺D and C=I−Q are symmetric; orientation changes conjugate by a diagonal sign matrix. The clique-constant mode gives the path Laplacian and its orthogonal complement gives S=(nI+L_P3)⁻¹. I checked the displayed 3×3 inverse by multiplication and the three source types by the clique and path symmetries (the endpoint degree pairs separate the types for all n≥2). The clique-edge absolute sum is 2(n−1)/n plus twice the total variation of a column of S. For a path edge, the injection splits into its constant and zero-mean clique components; the first interface carries total absolute current 1 since the shifted-mode voltage difference is in (0,1), and the other interface contributes 2(n−1)|w₂−w₁|/n. The complementary column is 1 plus the cut column minus twice its diagonal. Substitution gives all six stated rational functions. The middle clique column beats the outer one for both projections. The signs of the vertical-minus-middle differences have factors n−3 for cut and n−5 for cycle, with strictly positive remaining factors, proving the stated and distinct ties. The norm comparison is correct, including 9/5>8/5 at n=2 and the reverse for every n≥3. Symmetry identifies row and column maxima. Independently written /workspace/review-evidence/hodge.py used (L+J)⁻¹ between incidence factors, reproducing all 322 columns and both maxima for n=2,…,8; this finite check is not the proof for all n. The theorem concerns canonical projections only.

## originality

FAIL

The earlier Resultary record d11ca8ac5f42 already gives exact absolute cut-column sums of both product-edge types for arbitrary H□K_m, exact diagonals, and the identity giving complementary sums. Its result applies to H=P₃, m=n for every n≥2 (the m≥4 restriction is on dominance, not on the exact formulas). Direct specialization gives all six formulas and their maximizing thresholds; the exact prior implication, not a publication-date inference or a search hit, is decisive.

## value

FAIL

The distinction between cut and cycle maximizers on this smallest nontrivial path factor is illustrative and correct; nevertheless, the whole precise fact is mechanically implied by the extant exact arbitrary-base formula. Computing the three entries and factoring their differences is a useful worked example, not a surviving independent exact invariant under the scientific standard. No narrower independent claim remains after removing this covered specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
