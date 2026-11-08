# Scientific review: spherical-football diameter-tail law

## Correctness — PASS
The domain is the doubled spherical lune of opening \(\pi\alpha\), for fixed \(0<\alpha<1\), with normalized area distribution and intrinsic geodesic distance. The unique diameter pairs are the two ordered opposite-cone-point pairs. The cosine-rule expansion, the positive-quadrant coercivity bound \(Q_\delta(u,v)\ge\min\{1,1+\cos(\pi\alpha)\}(u^2+v^2)\), and dominated convergence reduce the normalized tail to the stated double integral. Its polar-coordinate reduction, elementary tangent substitution, and angular antiderivative yield the exact closed coefficient. Strict monotonicity follows from strict inclusion of elliptical positive-quadrant sublevel regions as the longitude gap increases. Checks of normalization, the smooth endpoint, and three independent integral representations agree. Boundary: no claim for \(\alpha\ge1\); fixed-parameter limit only.

## Originality — PASS, provisional historical priority
The closest geometric predecessor is Mondello–Panov (arXiv:1505.01994v1, 2015-05-08), Section 3.1.1, which constructs arbitrary spherical doubles of bigons and discusses cone angles, not random intrinsic pair-distance tails. Tu–Fischbach (arXiv:math-ph/0201046v1, 2002-01-22) develops Euclidean **chord**-distance distributions inside balls, a different metric and object. The classical round-sphere law gives a quadratic endpoint and does not imply the continuous sub-round coefficient. Related archived local cone-surface and flat-pillowcase distance laws have different curvature and distance endpoints, and no stronger shared theorem was identified. Queries included aliases football/spindle/doubled spherical bigon/cyclic sphere quotient and cone-angle inverse distance tails. Indexed absence cannot prove novelty; older obscure stereological literature remains an explicit risk.

## Mathematical value — PASS
The order-four extreme-distance law is a natural, sharp invariant of a globally curved cone surface. Its explicitly evaluated coefficient is strictly increasing over the full interval of cone angles smaller than \(2\pi\), so a single leading statistical observable recovers the geometry's cone angle. The change from fourth to second order at the round sphere and the discrete cyclic-orbifold specialization expose a geometric singularity signature. This is not merely a computational example or rescaling of the sphere: it is a continuous inverse theorem with a nontrivial boundary layer.

## Verification and limits
The standalone `verify_football.py` evaluates the original radial integral, its angular reduction, the exact coefficient and finite-tail probabilities for four angles. Numeric limiting ratios converge as predicted. Numerical integration is corroboration; the analytic steps above establish the theorem. Independent audit and priority certification have not been performed.

Self-review: passed. Independent audit: not yet performed.
