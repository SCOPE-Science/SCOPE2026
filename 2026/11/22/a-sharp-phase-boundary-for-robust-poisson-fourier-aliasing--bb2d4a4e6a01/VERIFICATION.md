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

The Cauchy quantile is the boundary parametrization for the Cayley map based at m+is; its target harmonic measure has Fourier magnitudes r^|k| with r²=((c−m)²+(a−s)²)/((c−m)²+(a+s)²). Grid averaging leaves modes k=Nℓ; orthogonality in the single shared shift gives 2r^(2N)/(1−r^(2N)). Compact support bounds r away from 1 for each reference, justifying summation/integration. Convexity of the L² norm bounds the mixture by the worst singleton, and the compactness maximum is attained by an admissible Dirac mixture. The variance is not equal to that maximum for every mixture. Maximizing over c gives distance C+|m|, strictly worse for m≠0 than m=0 at the same s because r² is increasing in that squared distance. At m=0, T_a=1−r²=4as/[C²+(a+s)²] has no interior minimum in a and is uniquely maximized in s at √(a²+C²). T_A−T_B has the sign of AB−C²−s². A positive crossing, when present, is below the maximum of T_B; the lower envelope peaks uniquely at the crossing if the crossing is at or above the maximum of T_A, and otherwise at the maximum of T_A, also when there is no positive crossing. This gives the claimed phase boundary, two radius formulas and active sets; the branch formulas coincide at equality and their slopes in C have opposite nonzero signs there. A<B rules out zero worst radius, and compactness gives R_*<1; strict monotonicity of the variance in the radius makes the optimizer independent of N. Scaling by the total mass gives the relative-variance assertion. VERIFICATION.md and verify.py were inspected without execution; the finite diagnostics are not the universal proof.

## originality

PASS

Credit the known aliasing formula, Möbius change of variables and standard hyperbolic distance. The supported distinction is the exact globally optimal reference and positive-mixture minimax risk over the full rectangular location-scale uncertainty, with an explicit sharp active-set transition, not merely the component formula or a centered deterministic exactness scale.

## value

PASS

For a natural reference-selection problem this gives the exact worst-case variance and a unique resolution-independent optimal reference, even for arbitrary positive mixing and an unknown mixture normalizer. The boundary marks a genuine change in the obstructing target scale and reverses how the optimal width responds to location uncertainty; this is more than computing a standard aliasing tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
