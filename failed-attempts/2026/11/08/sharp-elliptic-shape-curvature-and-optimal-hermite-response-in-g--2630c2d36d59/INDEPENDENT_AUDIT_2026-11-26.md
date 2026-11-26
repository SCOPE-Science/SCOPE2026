# Independent mathematical audit

## correctness

PASS

For fixed s>0 the ellipse has constant area and its squared radial boundary in the rescaled Fock plane is b=s/(cosh(2t)-sinh(2t)cos(2θ)). Differentiating this moving radial limit gives P''00=-2s²exp(-s) and P'20=s²exp(-s)/√2, with the rest of the first-variation column zero. The fixed compact-disk pullback is trace-norm analytic and the top disk mode is isolated by s exp(-s); the h2 gap is s(s+2)exp(-s)/2. The reduced resolvent gives both stated coefficients and the plus sign of the phase-normalized h2 term. The quarter-turn yields evenness of the eigenvalue and hence the fourth-order remainder. Differentiating the loss coefficient gives the unique maximizing area. Independent polar incomplete-gamma quadrature in 18-mode sections corroborates the coefficients at four areas and three deformations; this is not the proof and gives no uniformity in area. Replay: python3 /workspace/evidence/bounded_checks.py 5; derivation in /workspace/evidence/mathematical_checks.md. The frozen checker was read, not executed.

## originality

FAIL

Two earlier indexed general Gaussian shape Hessians already cover the principal ellipse coefficient. The maximizing signal derivative follows from their first-variation entries by the standard reduced resolvent. Analyticity and the ellipse symmetry give the remainder, and one-variable differentiation gives the area calibration. The core finding is covered by stronger results, even though the specialization is explicitly presented here.

## value

FAIL

The fixed-window ellipse question is well motivated, and the calculation is useful pedagogically, but it is an exact single-mode instance of the stronger shape Hessian. The signal derivative, parity remainder and area maximum do not leave an independent substantive result once that prior coverage is recognized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
