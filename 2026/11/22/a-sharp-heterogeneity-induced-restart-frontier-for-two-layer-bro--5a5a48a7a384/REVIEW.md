# Scientific review

## Correctness — PASS
The generator and Fickian flux-matching interface condition are explicit. The first and second moments follow from unique polynomial transmission boundary-value problems. The third moment and critical curvature follow from the same recurrence. The resetting renewal transform, strict sign reduction to a reciprocal quadratic, and local onset from the implicit-function theorem cover all stated parameters and boundary cases. Fifty-one independent symbolic/high-precision assertions support the algebra; finite tests do not prove the universal statements. Scope excludes claims about global optimality and asymmetric critical curvature.

## Originality — PASS, with residual priority risk
The small-rate restart criterion and renewal identity are prior theorems, not original contributions. Existing heterogeneous-resetting work (Lenzi et al., 2022; Ray, 2020) uses spatially varying/power-law diffusivity and different target geometries. Layered diffusion literature (Carr, 2018; Bressloff, 2023) develops transmission/absorption methods without this exact Poisson-restart contrast classification. The distinct claim is the explicit sharp diffusivity-and-length domain, universal midpoint contrast \(3\pm2\sqrt2\), positive critical quadratic curvature, and local optimal onset. A broadly stated prior moment or renewal formula could still imply the parameterization implicitly; independent priority review remains necessary.

## Mathematical value — PASS
The location of the reset is held fixed at a symmetric geometric midpoint, so the change from slowdown to speedup is caused solely by material contrast. This separates geometric and material contributions, identifies a sharp and dimensionless experimental-design threshold for ideal layered transport, and distinguishes a zero first derivative from a genuinely neutral intervention through the exact second-order term. The result is model-specific rather than a universal restart principle.

## Scope and reproducibility
Parameters and interface conventions are specified in RESULT.md. The independent hyperbolic Laplace transform checks polynomial exit-time moments and exact renewal mean. Run `python checker.py`; dependencies are SymPy and mpmath. Numerical tests and symbolic simplifications support the proof but cannot certify priority against all literature.

Self-review: passed. Independent audit: not yet performed.
