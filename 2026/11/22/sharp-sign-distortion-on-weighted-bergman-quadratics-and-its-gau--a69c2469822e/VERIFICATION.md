---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The radial beta integral gives m_j=j!/(beta)_j. Expanding the square of the quadratic leaves only one phase-sensitive term, 4m_2 Re(b^2 conjugate(ac)); independent signs average it out and a flip of exactly one of the outer modes reverses it. For fixed magnitudes, the maximal ratio uses maximal destructive interference in the input. With v=|b|^2, x=|ac|/v and t=|a|/|c|, minimizing H/(4m_2 v^2 x) in x is the strict equality case for m_2/x+x(t^2+4m_2+m_4/t^2). The balancing substitution for t then gives the displayed F_beta. The norm term in F_beta is convex by the vector-norm second derivative: its Cauchy–Schwarz residual is nonnegative and its vector dotted with its second derivative is positive. The cosh term gives strict convexity and uniform coercivity. A_beta-B_beta has sign beta-1, so the derivative at zero is positive and the unique minimizer is negative. Each of the three parameters increases strictly, which increases the minimum by comparison at the new minimizer. Uniform coercivity and local uniform convergence justify both limits of the minima; the scale change gives limiting moments j!. Sharp equality requires all three coefficients, the unique x,t, and the specified phase; constructive and destructive phases give opposite sides of the Rademacher comparison. An independent 65-digit decimal bisection in y=exp(s), /tmp/opencode/frozen-quadratic-endpoints.py, reproduced the illustrative endpoint and area-weight decimals. The proof, not the numerical check, gives the all-weight result.

## originality

PASS

Credit the earlier three-mode fourth-moment expansion and qualitative randomization framework. The distinct claim supported here is the sharp sign and Rademacher comparisons with a quartic phase-averaged or sign-transformed denominator, their equality conditions and strict dependence on the disk weight. The strongest inspected weighted-quadratic results optimize a different ratio and do not supply these conclusions.

## value

PASS

Degree two is the first cutoff with colliding exponents in the square and therefore the first nontrivial fourth-norm sign distortion. The exact unconditional and randomized comparisons, all equality cases, and strict evolution from Hardy to Gaussian weights quantify that minimal resonance in a way the usual fourth-to-second moment constant does not. This gives a natural exact benchmark for higher-mode analyses without claiming the higher-degree problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
