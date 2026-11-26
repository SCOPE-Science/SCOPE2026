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

For every nonempty base j-face σ, orient the cone simplex uσ with the apex first. Its boundary zσ has coefficient +1 on σ and all other terms are apex cones on proper faces, or just the apex for j=0. Their filtration grades are at most that of σ because the apex has minimum weight. Thus replacing σ by zσ is an integral shear preserving each sublevel lattice in both directions, including at tied grades. The grade of zσ is bσ by its leading support term; uσ enters at dσ=bσ+h(j+1)−h(j). The chain complex splits, with inclusion maps respecting the splitting, into the apex and blocks uσ→zσ of unit differential. This proves the claimed half-open intervals integrally, with no torsion or extensions. For the apex-only cone there are no blocks; h(0)=0 sets the sole birth to w(a). The edge example with nonminimal apex checks the need for the hypothesis. Replay: frozen RESULT.md lines 4–43, 48. VERIFICATION.md and verify_cone.py were inspected, not executed; their finite-field checks cannot establish the integral assertion.

## originality

PASS

The explicit all-cone, face-indexed integral answer for dimension delays was not found in the closest inspected statements. The filtration and cone boundary identity are established ingredients, not novelty claims. The direct sum over Z and its exact birth and death grades are the supported distinction.

## value

PASS

A newly used filtration creates transient features even when the underlying complex is contractible. The result resolves the entire persistence module for a natural family, gives known-length reference bars without matrix reduction, and identifies exactly how weights and base faces rather than base homology enter the answer. The integral transition maps and applicability to arbitrary nonuniform delays make it useful as a calibration and interpretation test, not just a computation on one cone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
