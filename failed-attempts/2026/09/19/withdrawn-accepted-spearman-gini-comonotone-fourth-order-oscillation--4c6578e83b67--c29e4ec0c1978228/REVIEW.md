# Scientific review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The derivation starts only from the explicit boundary formulas in arXiv:2609.19890v1. Expanding with \(N=\lfloor\theta\rfloor\), \(h=N^{-1}\), and \(r=\theta-N\), then eliminating \(h\), gives the same quadratic and cubic coefficients on both algebraic branches. The fourth coefficient reduces to a single symmetric phase function of \(\operatorname{dist}(\theta,\mathbb Z)\). The source branch switch occurs at \(r=N/(2N+1)=1/2+O(h)\); the two limiting fourth-order branch polynomials coincide at \(1/2\), so this displacement does not alter the limit. Direct high-precision evaluations of the exact source formulas converge to the claimed phase coefficient for phases across both branches, including \(r=1/2\).

Adversarial checks included both sides of the moving branch junction, integer and half-integer parameter sequences, and the signs of the cubic correction. The normalized fourth-order remainder converges to distinct limits on integer and half-integer sequences, so the nonexistence of a unique fourth-order coefficient is not a numerical artifact.

## Originality

**PASS, to the best of our knowledge.** The exact attainable region and its countably algebraic parametrization are prior work and are not claimed here. The auxiliary rho–footrule optimizer is also prior work. Searches using the exact coefficient forms, endpoint/comonotonic asymptotics, smoothness/differentiability terminology, and the rho–gamma pair did not locate the quadratic-cubic endpoint law or the fourth-order phase oscillation. The source paper states continuity, concavity, strict monotonicity and the countably piecewise algebraic structure, but does not state endpoint asymptotics or differentiability order.

The main residual risk is that equivalent endpoint regularity of the auxiliary rho–footrule problem may appear in older or differently phrased literature. The present originality claim is therefore limited to the explicit rho–gamma endpoint expansion, phase function, exact interval of fourth-order limit points, and the Peano-order consequence.

## Value

**PASS.** The result resolves the local geometry hidden by the countably many algebraic pieces accumulating at comonotonicity. It shows that the pieces cancel through cubic order, producing a universal sharp law, and identifies the first order at which their arithmetic structure survives. The exact width \(1/2\) of the fourth-order oscillation gives a concise regularity invariant of the newly determined attainable boundary.

## Limitations

- This is a local endpoint result, not a new global attainable-region theorem.
- The fourth-order phase is stated in the source parameter \(\theta\), not solely as an elementary function of \(g\).
- The proof depends on the correctness of the exact parametrization in arXiv:2609.19890v1.
- Independent audit has not been performed.
