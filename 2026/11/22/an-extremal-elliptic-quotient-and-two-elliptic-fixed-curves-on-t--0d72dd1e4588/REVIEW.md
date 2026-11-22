# Self-review

## Correctness: PASS

The exact function-field substitutions from the quartic sign-change quotient produce the isotrivial Weierstrass K3. The transposition transforms \((t,X,Y)\) into \((t^{-1},t^{-4}X,t^{-6}Y)\); the invariant generators yield the specified rational elliptic equation. Four and two \(I_0^*\) fibers follow from exact discriminant valuations at all boundary points. The quadratic map is branched only at two smooth fibers, making the quotient and the fixed locus global rather than merely birational claims. A constant-curve descent argument proves all sections, and the two elliptic fixed fibers determine the invariant lattice by Nikulin. `CHECK.py` passed the symbolic identities; it is not a substitute for surface-theoretic arguments.

## Originality: PASS with residual risk

The initiating source [1, Section 3.7] treats the same involution and gives invariant rank ten, but describes only one fixed elliptic curve, hence \(a=10\). The independently derived quotient equation identifies two fixed elliptic fibers, the explicit rational surface and full Mordell–Weil group, and Nikulin type \((10,8,0)\). published-finding corpus semantic searches and inspected literature did not identify prior equivalent equations for this named involution. The general Nikulin and extremal-rational-surface theories are not claimed as new. The source's conflicting conclusion warrants independent checking, and historical coverage cannot prove priority.

## Value: PASS

A named self-mirror K3 example was used to compare mirror invariant lattices. An explicit elliptic quotient and a different fixed-locus type are structurally important: they refine the integral invariant lattice, give two complete singular-fiber lists and determine the quotient Mordell–Weil group. The conclusion is not just a routine rewriting of a known invariant, because it resolves a precise discrepancy in the geometric involution computation that changes the polarization discriminant length.

## Limitations and closest literature

The result holds over \(\mathbb C\) for this explicit quartic and involution only. Barrett et al. [1] is the closest direct claim; Nikulin [2] supplies the general two-elliptic classification; Miranda–Persson [3] classifies abstract extremal surfaces; Garbagnati–Salgado [4] treats general elliptic-fibration involutions. Independent audit remains open.

Self-review: passed. Independent audit: not yet performed.
