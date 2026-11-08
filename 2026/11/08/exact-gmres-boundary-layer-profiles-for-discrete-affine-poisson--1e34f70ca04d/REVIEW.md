# Self-review

## Correctness — PASS
The argument is exact for all integer dimensions \(n\ge2\) and all nonzero real boundary pairs. The identity \(A_nb=L e_1+R e_n\), finite propagation and the orthogonal endpoint-pair decomposition prove every term of the residual formula without extrapolating from experiments. Dirichlet sine eigenmodes give the precise Krylov grade; localized supports give the full ramp curve and symmetry gives the full constant curve. Exact rational checks replay the finite-dimensional formulas from `verify.py`. The asymptotic tolerance law follows by monotone inversion of the explicitly proved normalized limit, rather than from finite tests.

## Originality — PASS, with historical-priority risk
Published mathematical-record searches, the complete 2026 motivating source, and primary older Toeplitz GMRES analyses were compared for implication rather than title match. General pseudoinverse formulas and spectral residual bounds give ingredients, but no inspected theorem states the exact residual profile for *all* affine Dirichlet-harmonic right-hand sides together with the three-way grade and distinct full-length constant/ramp tolerance laws. The 2004 Liesen–Strakoš paper focuses principally on Jordan and nonnormal tridiagonal extensions; the 2007 Zhang thesis gives general bounds and endpoint-focused explicit cases. Priority remains uncertain for material outside inspected sources, and finite propagation is standard.

## Value — PASS
This is the complete natural two-parameter class of discrete harmonic right-hand sides for the one-dimensional Dirichlet Poisson stencil, rather than an arbitrary numerical slice. Exact curves reveal a mesh-linear solver cost and distinct tolerance exponents for two canonical boundary configurations on the *same* SPD coefficient matrix. The result directly addresses recent interest in attainable GMRES behavior under structural and right-hand-side constraints. It does not claim a new general GMRES convergence theorem or finite-precision performance improvement.

## Scientific limitations
Generality stops at this fixed one-dimensional operator and discrete-affine family. Beyond the half-grid, explicit formulas are established only for the two special profiles. The historical literature comparison is substantial but not exhaustive.

Self-review: passed. Independent audit: not yet performed.
