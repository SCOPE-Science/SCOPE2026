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

For the classical Poisson kernel on (0,1) and constant trace extension, a jump at s=(m+a)/n gives a Gamma(m,n)/Gamma(m+1,n) CDF mixture of mean s (shape zero is an atom). Integrating its signed step residual gives the mean absolute deviation minus right overshoot. The Gamma first moment and Gamma–Poisson identity yield 2s p_m(ns) and the stated affine interpolation of r_m. The cell derivative is strictly decreasing through any eligible root; the negative derivative at a cell's right boundary excludes grid knots and s=1, and s=0 gives zero. This includes n=1. Equality first requires the variation measure to be supported on the finite set of globally maximizing roots; distinct signed residuals cannot align both to the left of the two jumps and between them, so only one jump is possible. The leading constant follows by Stirling and a competitor with 1−s=c√(log n/n), c>1. More explicitly, 1−√s≥(1−s)/2 gives the upper exclusion of all c≥1+ε using the uniform Stirling error after s→1. For c≤1−ε the Gamma density on the stated overshoot window is bounded below by a constant times √n exp(−d²/2−O(1+d³/√n)); multiplying by the square of the window size gives an overshoot larger than √(log n)/n. This excludes every such maximizer even in a tie. The frozen files were read, not executed. Separate direct quadrature at n=1,2,3,10 reproduced 0.439539995635, 0.334482432795, 0.288945671583, 0.187336430786 to numerical precision; replay /workspace/branches/8e238f6a-8504-45ab-b674-a751237b42ea/check_record2_independent.py. Neither a finite sweep nor the supplied checks establish the limit.

## originality

PASS

The exact finite-interval Poisson-kernel norm, complete equality and universal retreat constant are not covered by the inspected weighted-rate or different-kernel theorems. The kernel and continuation convention are part of the claim; neither the classical operator nor Poisson/Gamma identities are new.

## value

PASS

The exact norm and equality criterion identify the most adverse discontinuities for a standard approximation operator. The √(log n) factor in their distance relative to the diffusive scale is a genuine boundary effect missed by a rate bound; the constant applies to every maximizer, not a fitted numerical sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
