# Independent mathematical audit

## correctness

PASS

In angular time every admissible path is c-Lipschitz for circle geodesic distance (integrate along the shorter arc), and a circle c-Lipschitz selection corresponds to a periodic path with the given a.e. speed bound. Pairwise L(theta)-U(eta)<=c d(theta,eta) is necessary and the upper envelope of L(theta)-c d(theta,eta) is itself a selection when those inequalities hold, including at the optimum. At fixed separation d the amplitudes in the two orientations are 2A sin(alpha+d/2) and 2A|sin(alpha-d/2)|; comparing their squares gives an ordering from sin(phi) sin(d)>=0. The resulting quotient derivative has sign h-G(x), where x=alpha+d/2 and G'(x)=2A(x-alpha)sin x. This gives the global maximum, including the one-sided case h=h_0 and the antipode at phi=0, h approaching 2A. Pointwise nonempty iff h>=h_0; constant feasible iff h>=2A; at phi=pi the intermediate branch is empty. Expanding G from alpha gives A sin(alpha)(x-alpha)^2 for fixed nonzero lag below pi, or (2A/3)x^3 at zero lag; expanding the speed then gives the stated coefficients and exponents. At pi/2 the derivative A(pi-phi) yields the claimed linear vanishing for fixed phi<pi. Independent check: python3 /workspace/review_checks.py 2 maximizes over all ordered pairs on a 1,024-phase grid in five examples; agreement is within 1.5e-5 in scaled speed in these examples. This does not verify the continuous optimum on its own. The frozen checker was inspected, not executed.

## originality

PASS

The supported distinction is the evaluated sharp sinusoidal speed-width frontier and its change in endpoint scaling, not the general Lipschitz-selection principle or an empirical result about fish. No materially equivalent prior calculation was found in the checked sources; the ecological follow-up and general selection literature were only partially accessible.

## value

PASS

The model separates instantaneous refuge availability from continuous occupancy at a prescribed speed, and gives the sharp threshold and a constructive trajectory. The distinct phase-dependent speed savings near the feasibility boundary add quantitative content beyond set-selection existence. This is an idealized benchmark, not a physiological threshold or a field prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
