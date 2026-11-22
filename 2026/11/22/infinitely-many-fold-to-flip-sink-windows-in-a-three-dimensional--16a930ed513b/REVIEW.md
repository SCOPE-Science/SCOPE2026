# Scientific review: equilibrium staircase and repeated sink windows

## Correctness
PASS. The stationary equations reduce exactly in both directions to \(z=k\sin z\). For positive net gain, positivity of sine restricts positive roots to separated lobes. The derivative numerator of \(z/\sin z\) has strictly positive derivative on each lobe, yielding exactly one minimum and the exhaustive zero/one/two root classification. On the pure-feedback line the characteristic spectrum is exactly \(\{0,0,k\cos z\}\); strict monotonicity of \(z\cot z\) proves the exact attractor windows and the nonattraction of all other nonzero fixed points. The fold/flip transcendental equations yield the inverse-lobe window-width asymptotics, and hyperbolicity yields genuine open three-dimensional parameter persistence. The accompanying diagnostic bisection checker tests specific transcendental calculations but is not used to infer infinitude.

## Originality
PASS within inspected sources and indexed comparisons. Almatroud et al. (2024) give the same map, the scalar fixed-point equation, origin stability and numerical multistability, but not the exact complete positive-gain stationary-state census, infinite fold thresholds, sharp repeated stable-window widths, or persistence of paired sinks in nonzero-delay parameter regions. Closely related indexed results for this or other sine-delay maps concern primitive two-cycles, extra linear feedback, or reciprocal sine nonlinearities, which do not imply the full fixed-point claim. Scalar sine-map roots and the basic implicit-function theorem are classical tools and are not individually claimed as new. The potential for unindexed prior equivalent calculations remains an originality risk.

## Value
PASS. The exact phase diagram addresses a concrete omission in a published three-dimensional map emphasizing symmetry and multistability: the number of stationary states and the gain intervals over which pairs are *genuinely attracting*. It supplies all positive-gain fold counts and identifies infinitely many disjoint and increasingly narrow sink windows with a sharp, useful leading coefficient. Persistence off the singular slice makes the windows relevant for the original full-dimensional family, rather than a degenerate computational curiosity. This is a motivated complete classification and not an arbitrary isolated numeric correction or a claim about chaotic security.

## Inspected literature and limitations
- Almatroud et al., 2024, https://doi.org/10.3390/sym16081093: full open-access HTML introduction, §2 fixed-point derivation and Jacobian, §3 numerical bifurcations, and later discussion.
- Indexed comparisons included other published sine-delay-map two-cycle analyses, which study different invariants and restrictions and do not dominate the fixed-point phase diagram.
- Wilczak, Serrano and Barrio, arXiv:2504.04887 (2025): indexed discussion reports recurring scalar-sine saddle-node pairs; only abstract and an indexed passage were available, not full text. Qualitative sine-map folds are therefore acknowledged as known background.
- Classical scalar sine iteration provides the elementary tangent conditions and is background, not an originality claim.

Residual risks: possible unindexed equivalent fixed-point-fold and stability-window results; extrapolation from the pure-feedback line to an arbitrary nonzero-delay parameter triple is not justified and is explicitly not claimed. The negative-net-gain region, boundary nonlinear stability and global attraction basins remain unclassified.

Self-review: passed. Independent audit: not yet performed.
