# Independent mathematical audit

## correctness

PASS

For every integer N≥2, u=βe1+εe2 and v=εe3+γ∑e_j are orthonormal for ε=1/N, β²=1−ε², γ=β/√N. A=2I+uvᵀ+vuᵀ has eigenvalues 1,3 on span(u,v), 2 elsewhere, so is SPD of condition 3 and a single Arnoldi step from u gives v exactly. With disjoint column supports every full-rank two-row sketch must pick one of first two rows and one of next N+1; four row-amplitude types exhaust selection. Since β>γ>ε, all min-singular-value maximizers {1,j≥4} have sketch condition √N, whereas unique condition-minimizer {2,3} has condition one. DEIM and pivoted-QR Q-DEIM both pick the former. With orthonormal V, κ(VR^{-1})=κ(SV) for SV=QR. Independent exact rational tests covered selected N=2,3,9,100; symbolic four-type proof supplies uniform quantifier.

## originality

PASS

PASS best of knowledge: Bergermann 2026 motivates E-optimal row selection and whitening-condition distortion but does not give an unbounded optimality mismatch on an exact fixed-condition SPD Krylov basis; Q-DEIM inverse norm analyses and NP-hardness studies concern different guarantees. Nearby prior SPD two-row sketch/Ritz failures have different output criteria.

## value

PASS

PASS: The exact counterexample falsifies a natural surrogate-objective implication for a current deterministic Krylov selection strategy even when the parent SPD matrix is well conditioned, and the algorithm pivots exhibit the theoretically inferior selection. It is a motivated structural limitation of the chosen metric, not a recommendation to sample vanishing-amplitude rows in floating point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
