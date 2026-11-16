# Scientific review: optimal asymmetric polar-cap allocation

## Correctness — PASS
The three restriction eigenvalues follow by direct integration of normalized spin-one Wigner densities. For fixed \(h\in(0,1)\), writing \(d=|p-q|\), the least eigenvalue is the smaller of a strictly increasing central-order branch and a strictly decreasing extreme-order branch. Their factored difference has exactly one zero \(d_*\) in \((0,h)\), proving that the two reflected, unequal allocations are the only global optimizers. Both the multiplicity statement and the small-cap improvement follow by substitution and Taylor expansion. An independent quadrature implementation and symbolic tests passed; numerical grids were not used as proof.

## Originality — PASS, with residual historical-priority risk
Michel, Plattner and Seibert (2021) set up general spin-weighted Slepian concentration and its single polar-cap kernel, while Seibert (2018) developed closely related spin-weighted cap methods. The inspected portions discuss concentration eigenproblems for prescribed regions, not globally optimal area allocation between an antipodal pair. Earlier vector Slepian literature likewise gives operator methods but not the same maximin area theorem in the material accessible here. A search for unequal-cap allocations, the explicit algebraic split, and spin-one degree-one minimax concentration found no published statement implying this theorem. Nearby published results concerning *center separation* for scalar quadratic harmonics or *shape Hessians* for coherent-state cap concentration concern different optimizations. Search and access limitations prevent a guarantee of historical priority, especially against non-indexed measurement-design literature.

## Mathematical value — PASS
Fixed total observed area is a natural sampling-design constraint, and the smallest concentration eigenvalue exactly governs worst-case reconstructibility of the harmonic coefficients. Even at the first nontrivial spin-one harmonic degree, the optimum **always breaks north–south symmetry**, and the best unequal design doubles the guaranteed observed energy in the small-area limit. The unique optimizer, exact spectral tie and quadratic law for the smaller cap give a useful structural boundary and precise calibration for directional harmonic measurements.

## Boundaries and risk
The theorem is not extended to all vector harmonics, both spin chiralities, higher degrees, displaced caps or arbitrary observation sets. General earlier kernel formulas can be specialized to reproduce its initial eigenvalue polynomials, but deriving the global two-cap maximin and uniqueness remains a separate, explicit optimization. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
