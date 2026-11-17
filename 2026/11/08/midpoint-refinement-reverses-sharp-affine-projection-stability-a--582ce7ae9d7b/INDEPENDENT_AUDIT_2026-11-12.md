# Independent mathematical audit

## correctness

PASS

PASS: Refined nodal hat Gram is M=A/6 with A hub diagonal 2d, each midpoint 4 and leaf 2, coupling 1 along each incidence. Exact inverted evaluation row kernels on unit edges have opposite-signed endpoint coefficients, so the absolute-kernel integral is (p²+q²)/(2(p+q)). The hub, midpoint, leaf norms are respectively 17/9, (76d+29)/(9(4d+3)), and (1552d²+928d+19)/(9(4d+3)(20d+1)); exact positive differences show only outer leaves are norming. Coarse norm (7d+3)/(3(d+1)). Their difference equals -4(32d³−104d²−77d+2)/[9(d+1)(4d+3)(20d+1)]; cubic sign negative at d=2,3 and positive for d>=4, proving sharp reversal. Separate independent SymPy assembly/inversion and signed-edge exact integration checked d=2,…,8, including norming locations and signs. Finite range corroborates the all-d symbolic proof.

## originality

PASS

PASS, best of knowledge: earlier exact star formulas cover one-element-per-arm coarse projection and broader dimension-free spline stability, not the uniformly midpoint-refined d-star. The new leaf-only norming theorem and d=4 reversal are quantitatively different; no stronger same-configuration exact norm or refinement comparison was found in inspected material. General Lp projection-stability literature supplies methodological context, not the rational thresholds.

## value

PASS

PASS: Refinement is a natural operation in approximation theory, and the direction of change of the sharp L∞ least-squares amplification depends unexpectedly on star degree. The exact sharp d=4 boundary, norming-point classification, and high-degree limiting deficit provide a motivated counterexample to naive monotonicity; this is a genuine family calculation, not an arbitrary one-off instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
