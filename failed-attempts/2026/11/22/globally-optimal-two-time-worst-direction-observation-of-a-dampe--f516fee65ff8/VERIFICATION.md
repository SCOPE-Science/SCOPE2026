---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

For the equal-information Gramian the argument works after two local corrections: shifting both times multiplies both Fisher eigenvalues by e^(−2at₁), with no extra variance factor if comparing Fisher to Fisher; strict improvement holds exactly for separations with sin(bτ)≠0, which include all possible optima. The smaller root of λ²−(1+q)λ+q sin²z=0 has derivative of the sign of cot(z)[1+q/(1−λ)]−r on (0,π/2). At any zero the derivative of this sign function is strictly negative, and the endpoint signs straddle zero. The Rayleigh quotient perpendicular to the first row bounds later phases by e^(−πr), below the first maximum. This proves clipping and, by comparing cotangent to r, the E/D order. Weak damping first gives δ=O(r) by the D comparison and q−λ=O(δ²/r), then δ=O(r²) from the stationary equation and finally δ=πr²+O(r³). Strong damping follows by localizing c=rz using λ≤z² exp(−2rz), expanding r²λ at c on compacts and using the nondegenerate maximizer of c²/(1+exp(2c)). The stated decimal c* is slightly inaccurate: solving c−1=e^(−2c) gives 1.1088575528785450554…, though the exact Lambert expression is right. The material error is statistical: independent centered equal-variance errors need not have equal location Fisher information, nor need that information be the reciprocal variance. For instance take unit-variance Gaussian first and unit-variance logistic second. The latter has scalar location information w=π²/9 (logistic CDF at a draw is uniform and its location score has squared mean 1/(3s²), with s=√3/π). The Fisher quadratic replaces q by w exp(−2rz). At the claimed phase for a=b=1 and T=2, the stationary residual increases strictly: q increases, λ cannot decrease by the positive-semidefinite update, and λ<1. Thus the reported phase is not even stationary (own bounded numerical check: residual about 0.01726443 at z=0.8730697652). Even common non-Gaussian noise can preserve the timing without the stated variance normalization. No source script was executed; the recorded finite checks only concern the unweighted Gramian.

## originality

FAIL

A distinct indexed record gives the same globally optimal lag with a mathematically equivalent scalar equation and the same strong-damping asymptotic. The matching date does not settle who obtained the result first, but the overlap is demonstrated. The additional portions reduce by shifting and clipping, elementary derivative comparison, and low-order Taylor expansion of the matched theorem's explicit equation. No sufficiently distinct valuable remainder survives that comparison.

## value

FAIL

An exact two-observation timing law for worst-direction information is a motivated baseline for experiment design. However the core global theorem is already covered and the uncovered wording consists of mechanical consequences of that theorem, not an independently useful new timing law or a new analysis of unequal information. Correcting the Fisher assumption would not cure that redundancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
