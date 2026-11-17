# Self-review

## Correctness
PASS. The critical bound is \(\langle Q-J_n,Q-X\rangle_F\ge2\) for every even-permutation mixture \(X\), because the relative odd permutation cannot fix all but one label. Hölder's inequality with the rank-\(n-1\) projector \(Q-J_n\) gives the exact lower bound. The positive average of all transpositions lies in the even hull and saturates this inequality for every Schatten index. Strict convexity of Schatten norms for \(1<p<\infty\) proves nearest-point uniqueness and, via the convex-combination/strict-triangle argument, that no nonvertex maximizers exist. The exposed trace face is a simplex because each transposition has a distinguishing off-diagonal entry. The checker verifies the identities and small-order numerics, while the arbitrary-order proof is analytical.

## Originality
PASS within accessible sources; provisional priority. The 2023 Schatten-geometry paper concerns Chebyshev geometry of the unrestricted Birkhoff polytope. The 2007 permutation-polytope paper treats representations and combinatorial faces, not parity-restricted Schatten Hausdorff separation. The 2004 even-permutation work is the most relevant older source but its accessible abstract concerns facet inequalities and membership; full-text inspection was unavailable. This leaves a material historical-priority risk; no evidence of an explicitly stronger already-published norm-by-norm parity comparison was found. Index searches were also compared against known signed-orbit parity gaps, which use a different permutation action, and against a vector-permutahedron parity-loss result, which is not an isometric realization of this matrix-polytope claim.

## Mathematical value
PASS. The formula gives a natural, exact, all-dimensional polytope approximation invariant for a parity restriction that deletes half of the Birkhoff vertices; its Schatten index reveals a sharp nuclear-versus-\(p>1\) limiting dichotomy. The specific nearest-face geometry is a high-dimensional simplex with exact quadratic dimension, despite the highly complicated known facets of the even-permutation polytope. These are structural geometric facts rather than restatements of the parity definition, and they allow quantitative parity-constrained matrix approximation. The result does not claim volume or independent verification.

## Checked literature and limitations
Bouthat–Mashreghi–Morneau-Guérin, arXiv:2310.14043v1, complete accessible HTML, especially Sections 1–5; Baumeister–Haase–Nill–Paffenholz, arXiv:0709.1615v1, accessible PDF with main-results and relevant group-polytope discussion; Cunningham–Wang (2004) bibliographic abstract only; Brualdi–Liu (1991) bibliographic record only. Potential equivalent earlier norm estimates remain unexcluded. Python checker and finite numerical optimizations are corroboration only.

Self-review: passed. Independent audit: not yet performed.
