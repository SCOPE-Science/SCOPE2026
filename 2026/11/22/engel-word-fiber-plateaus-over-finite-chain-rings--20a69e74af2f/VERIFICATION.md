---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The scalar formula for the repeated adjoint was checked by induction, and ideal valuations were checked against the complete finite chain. The multiplicities \(M_s\) sum to \(q^{2\ell}\); the target fibers sum to \(q^{4\ell}\). Every shift in fiber size is exactly \(M_sq^{\ell+s}\), which verifies the sharp plateau and stabilization assertions.

The embedded code directly enumerates \((X,Y)\) and repeated brackets, rather than using the counting formula to generate observed fiber values. It verifies the formula for all targets over the indicated truncated polynomial rings and modular integer rings, including the mixed-characteristic and equicharacteristic pair of length-three rings with residue order two. See `checks.txt`.

Full verification of every finite ring is impossible by finite tests; the universal proof rests on valuation properties of chain rings. Equivalence to an unlocated stronger published result has not been ruled out. No independent audit or external mathematical certification was performed.
