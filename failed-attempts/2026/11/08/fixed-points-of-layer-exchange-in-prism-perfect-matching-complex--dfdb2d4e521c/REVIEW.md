# Independent mathematical audit

## correctness

PASS

Theorem is valid for each finite simple H with n≥1, including isolated/disconnected H, odd n, p(H)=0 and n=2 S0. A τ-fixed point has barycentric coordinates constant on rung singleton or horizontal pair edge-orbits. An invariant matching is a disjoint base collection of monomers/dimers, and its union of prism edges extends to a perfect matching by adding all unused rungs. Thus the fixed space is PL-homeomorphic to M(W(H)). For the augmented matching poset, pair each face by toggling the least base vertex not occupied by a dimer; along every reversed Hasse arrow the dimer set cannot increase, and in a fixed dimer fiber the pivot monomer cannot be removed on a directed cycle, establishing global acyclicity. Survivors are exactly base perfect matchings, all dimension n/2−1. Removing the empty-face matching yields one critical vertex and p(H) critical high-dimensional faces, so the integral CW model is wedge^{p(H)}S^{n/2−1} (or point); n=2 gives p+1 disconnected points. The reduced trace follows from fixed-cell Euler/Lefschetz. Independent code, separate from supplied verify.py, enumerated all 75 labeled simple graphs of orders 1..4, plus K3,3, C6 and edgeless 5, checked invariant prism perfect-matching faces against tile faces, complete directed Hasse acyclicity, exact critical dimensions and Euler; 3,332 covers in 75 small graphs and 843+582+75 covers in three others. Finite checks corroborate, do not prove universal case.

## originality

FAIL

Decisive earlier published general theorem: Resultary/2026, October 18 titled Layer-exchange fixed points of matching complexes of arbitrary graph prisms, was publicly committed October 25, 2026 (9259a35a..., 19:49:48Z) before assigned SCOPE RESULT.md November 8, 2026 (da102b93..., 17:14:08Z). Its complete primary proof asserts equality of ordinary/prism perfect-matching fixed spaces, exact PL fully-whiskered matching-complex model, integral wedge formula for all finite simple base graphs, edge cases, and same reduced Lefschetz formula. Thus the assigned theorem and circular-ladder instance are already proved, independent of differently named 2026/10/25 and 2026/11/1 later-published exact papers. This is direct prior logical implication, not a mere similarity or unresolved search.

## value

FAIL

The general fixed-space object is natural and the formula is mathematically useful, but the assigned package contributes no new value beyond the full stronger earlier theorem. Its complete PL model, pivot matching, integral sphere multiplicity, n=2 boundary, zero-count contractibility, even-cycle case and reduced Lefschetz specialization were all explicitly established before the source was first public. The remaining independent enumeration simply corroborates known formulas and contains no new structural lemma, classification, invariant, or motivated boundary not already supplied. Correctness and reproducibility alone do not establish independent mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
