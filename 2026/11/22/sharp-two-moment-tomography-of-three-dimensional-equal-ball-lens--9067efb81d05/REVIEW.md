# Scientific review

## Correctness — PASS

Surface area is uniform in spherical axial coordinate on each of two opposite equal-area caps. The exact parametrization, first and fourth radial moments, and diagonal covariance matrix are integrated explicitly in RESULT.md; an independent-pair polarization identity gives both even distance moments. The inverse follows by a strictly monotone quadratic ratio; the global square-root inequality and exact equality case are elementary, with all endpoints handled. `verify.py` rechecks seven symbolic identities and ten independent two-point simulations across five settings. Risks: experiments cannot certify continuum statements; the proof supplies those. The collapsed lens is explicitly excluded, and a coincident-ball full sphere is included without double counting.

## Originality — PASS (provisional)

Relevant published published-finding corpus full texts were compared at the **claim and implication** level: `589d8e6fc2c0` handles one cap, not the two-sphere boundary mixture; `dbb6d001c487` handles uniform **volume** points within the same lens, not its boundary; `bdea9ec9027d` handles spherical lunes. Drach–Tatarko's 2023 original study proves isoperimetric lens extremality and gives background geometry but not two-point boundary moments. Searches for surface-pair chords, random distances, tomography, moment inverses, and equivalent parameterizations found no stated stronger covering theorem. The single-cap moment wedge is credited, and its coincidence with the lens wedge is recognized as an ambiguity, not evidence of globally unique reconstruction. Residual priority risk: unindexed/classical boundary-lens moment formula, or an unpublished deduction, could be equivalent; independent literature audit remains outstanding.

## Mathematical value — PASS

The equal-ball lens is a natural curvature-bounded extremizer with two freely varying geometric parameters. Exact quantitative reconstruction of both radius and overlap from a minimal pair of rotation-invariant boundary distance statistics fills a motivated geometric measurement gap. The sharp inverse exponent identifies the precise near-ball loss of identifiability; the cross-family cap/lens ambiguity gives a concrete limit to this method. Unlike isolated number tables or arbitrary slices, this is a complete all-parameter inverse classification with boundary and stability behavior. It does not claim a general convex-body inverse theorem.

Self-review: passed. Independent audit: not yet performed.
