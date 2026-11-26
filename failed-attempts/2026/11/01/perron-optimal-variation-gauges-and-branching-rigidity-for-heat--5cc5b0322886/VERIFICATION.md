---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Integrating along the tree gives all edge gradients, and differentiating yields Q=-BBᵀC with diagonal -2c_e and absolute off-diagonal column entries A_fe c_e. The right derivative of the weighted ℓ¹ induced norm at the identity is the maximum weighted column candidate, each attained on a cut indicator. Subdividing time proves the bound and the right derivative forces its exponent. For M=C(A-2I) the positive Perron vector after a scalar shift attains the minimum, and a positive left eigenvector forces equality for an optimizer. Similarity proves the symmetric formula and congruence the sign. Paths and the claw have line-graph radii below and equal to 2. Every other tree supplies a K4 or a triangle with an attached vertex in the line graph, forcing radius above 2. With consistent path orientation, Q=(A-2I)C, and its eigenvalues are minus the positive eigenvalues of BᵀCB; this includes the scalar one-edge case. Contractive means nonexpansive; the claw admits no strictly positive prefactor-one decay rate. The frozen checker was inspected, not run, and the proof does not require its finite samples.

## originality

FAIL

A distinct earlier Resultary record states the fixed-gauge exponent, all-time envelope, cut witnesses and the identical path-or-claw criterion in a more general vertex-mass setting. The remaining optimized eigenvalue and path-gap formulas, though not stated in the inspected earlier Finding, are mechanically implied by its exact formula and edge equation via the same standard Perron/Collatz–Wielandt principle and the incidence spectrum. The claimed sharp combination is therefore covered, not merely similar in topic.

## value

FAIL

The rigidity classification and cut witnesses would be meaningful if not already stated for a broader setting. After crediting that result, the remaining formulas are a standard Perron optimization of a known quotient and its immediate path spectral identification; no distinct substantive or independently needed nonmechanical result survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
