# Scientific review

## Correctness — PASS

The object and edge-coordinate normalization are explicit for every integer \(p,q\ge2\). The proof reconstructs covariance using the weighted matrix-tree polynomial, then verifies exact block covariance entries using the split-graph Laplacian pseudoinverse. The clique and independent-set symmetry decomposition supplies all eigenvalues and dimensions; the exceptional \(p=2\) case is handled independently. The determinant identity \(\det(B-TI)=q(p-2)(q-3)/(p^2(p+q)^3)\) proves the threshold for the full infinite domain. Exact rational tree enumeration checks 1,565 covariance entries in nine small parameter profiles and 64 spectral trace profiles. Risks: an unnoticed algebraic error beyond the tested range is possible, though the proof exposes all necessary identities; external independent proof checking has not occurred.

## Originality — PASS (historical priority provisional)

Actual literature and published-result searches compared variants under spanning-tree covariance, transfer currents, complete multipartite fixed-forest counting, spanning-tree polytope spectra, and principal-component transitions. The closest primary sources give general tree-polytope constructions, generic moment computation, and strong forest-containment formulas. Those statements imply access to pair moments but do not state or directly imply the complete special-family spectrum and the \(q=3\) extremal-eigenspace reversal without substantial diagonalization. The full text of a 2023 particularly relevant fixed-forest counting paper was inaccessible, so unexamined implicit coverage remains a risk. No historical-priority certification or independent novelty review is asserted.

## Mathematical value — PASS

The theorem classifies a metric second-moment invariant of a standard infinite two-parameter graphic-matroid base-polytope family, identifies all principal-component multiplicities, and gives a sharp, clique-size-independent spectral transition with exact condition numbers. The full spectrum is not a mere renaming of the general transfer-current covariance identity; distinguishing the two competing largest representations requires a nontrivial all-parameter diagonalization and exact sign comparison. This is useful as a geometric benchmark for anisotropy of vertex distributions in graph polytopes. It does not claim algorithms or results for arbitrary graphs.

## Closest literature and limits

Aprile–Fiorini–Huynh–Joret–Wood (2021), arXiv:2106.11945, establishes spanning-tree-polytope context; Zmigrod–Vieira–Cotterell (2021) treats expectation computation for spanning-tree distributions; Li–Chen–Yan (2023), DOI:10.1002/jgt.22954, covers complete multipartite fixed-forest containment but its full text was unavailable; Wang–Ge (2026), arXiv:2602.03602, gives a general fixed-forest formula, inspected through its principal theorem. Neither inspected full-text claim exhibits this covariance spectrum or its sharp principal-mode switch. The affine Euclidean edge metric and uniform distinct-tree measure are essential.

Self-review: passed. Independent audit: not yet performed.
