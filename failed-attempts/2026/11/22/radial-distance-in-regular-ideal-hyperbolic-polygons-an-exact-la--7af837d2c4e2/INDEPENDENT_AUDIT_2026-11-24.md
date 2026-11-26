# Independent mathematical audit

## correctness

PASS

Independent Klein-model check: in each half-sector 0 <= theta < phi=pi/n the side is reached at tanh r = cos(phi)/cos(theta). Thus the area inside radius t per half-sector is the integral of cosh(min(t,r))-1. For t above the inradius split at B_n; integrating the side-limited part by v=sin(theta)/sin(phi) yields arcsin(sin(B_n)/sin(phi))=G_n. This gives both CDF branches, the normalized continuous density (including the junction) and the exact incircle mass. Expanding the forbidden half-angle gives B_n(rho+h) ~ sin(phi)*sqrt(2h/cos(phi)); integrating the missing polar area gives exactly the stated h^(3/2) coefficient. At fixed n the allowed angle is 4n*cot(phi)*exp(-2t)+O_n(exp(-4t)); integrating the density gives the stated exponential tail. For the limit, set theta=v*pi/n. After area normalization the two cutoffs in the sector integral tend to exp(s) and b/sqrt(1-v^2), with b=2/pi; the minimum is bounded by the disk cutoff. Dominated convergence gives the integral of this minimum on [0,1], which evaluates to the claimed H through and at its join, and has left mass b at the limiting incircle. Its derivative deficit there is b*sqrt(2h)+O(h^(3/2)) and its right survival asymptotic is b^2*exp(-s)/2. No interchange of fixed-n tail and large-n limits is needed. Independent replay /workspace/replay/04.py passed 20 clipped-sector quadratures and six scaled-sector checks; these are finite checks, not the proof. The frozen checks/regular_ideal_polygon.py is present and was inspected, not executed.

## originality

FAIL

A distinct same-date Resultary record exactly covers the complete finite-n law and the scalar many-side limit and explicitly states the fixed-n tail and density defect. The remaining CDF defect and limiting tail/transition are elementary integrations or expansions of those same formulas. This is demonstrated equivalent coverage and a stronger marked result, not a mere search hit; no priority or publication order within that date is inferred. No uncovered substantive part of the frozen finding survives.

## value

FAIL

The radial law is a meaningful geometric diagnostic, but the frozen package adds no distinct scientific result once the exact scalar formulas and stronger marked limits in 54abf06270a5 are credited. An alternative centering and expansions of the same law do not supply a separate worthwhile claim; no repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
