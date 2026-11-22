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

# Reproducible verification

Run `python3 verify.py` with the Python standard library. The program generates all endomorphisms of the direct-product abelian groups by allowable images of cyclic generators, tests idempotence on generators, reconstructs entire image groups, derives the p-primary image type using image cardinality and the cardinality of the p-multiple image, then compares the number of maps and their kernel-weighted affine lifts against a separately implemented automorphism-group formula.

Five exhaustive configurations are checked: \((p,a,b)=(3,0,2),(3,2,0),(3,1,1),(5,1,1),(3,1,2)\). In the largest group \(C_9\oplus C_3^2\), the independently enumerated output contains \(380\) idempotent additive maps and \(4780\) affine quandle retractions, matching the theorem's complete type distribution. On \(C_9\oplus C_3\), the checker independently constructs all \(6561\) affine maps, verifies the quandle operation on every ordered pair of inputs, and finds exactly \(136\) composition-idempotents. Successful execution prints `MIXED_TAKASAKI_CHECKS_PASSED`.

The general mathematical claim is justified by the direct proof, not by finite extrapolation. Historical mathematical priority is qualified by the literature review; no external independent audit or certificate is claimed.
