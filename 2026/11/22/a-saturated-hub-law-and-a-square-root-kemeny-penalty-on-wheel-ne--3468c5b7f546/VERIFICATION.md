---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

On the orthogonal complement of the constants the symmetric Markov Laplacian is positive definite for every irreducible feasible kernel, even without an aperiodicity hypothesis. The second derivative of the inverse trace in a nonzero stochastic direction E is twice the squared Frobenius norm of A^(-1/2) E A^(-1), with A=I-P+J/(m+1) evaluated at that point. Connected support is preserved by convex mixing, and approaching a disconnected kernel forces a positive gap to zero and the objective to infinity. Consequently cyclic averaging and strict convexity justify unrestricted existence and uniqueness. Fourier decomposition gives one gap (m+1)b and m-1 gaps b+2a(1-cos(2πk/m)). Any rim hold is strictly suboptimal at fixed positive spoke weight b. Along a=(1-b)/2 the total positive contribution to the derivative from negative cosines is at most m-1, whereas the radial derivative is at most -m²/(m+1); the derivative is strictly negative up to b=1/m. Summing the convergent Poisson kernel selects multiples of m and the k=0 term to remove is m for both kernels. The optimal q=1-1/m gives delta=sqrt(2m-1)/m and rho^m tending to zero; the comparator q=2/3 gives leading m²/sqrt(5), hence the stated sqrt(2/5) ratio coefficient. At m=3 the wheel is K4 and the two walks agree. For finite replay, form the claimed kernel for m=3 through 8 and invert I-P+J/(m+1) over the rationals; the checked values are 9/4, 118/35, 875/186, 8172/1309, 21511/2696, 35206/3555. Lowering one spoke or one rim edge by 1/(24m), symmetrically increasing the two endpoint holds, strictly increased the rational trace in each test. These are finite corroboration, not the global argument. The frozen verify_wheel.py was inspected, not executed.

## originality

PASS

The credited general convex formulations and wheel Fourier methods do not by themselves select the active constraints. The closest prior wheel result does have the same weighted Laplacian trace up to a constant, but optimizes over a different feasible set. The all-size active-set proof and the exact divergent loss of the standard symmetric maximum-degree comparator are not supplied by the inspected prior statements. This is a best-of-knowledge assessment, not a priority guarantee.

## value

PASS

A wheel is a canonical test of hub versus rim allocations. Determining that every row is tight at the unrestricted optimum rules out apparently plausible asymmetric and holding alternatives, rather than just evaluating a chosen walk. The sharp, unbounded loss for the usual symmetric maximum-degree rule is a useful analytical benchmark for how differently inverse-gap and mixing design criteria can behave. No performance claim outside this objective and feasible set is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
