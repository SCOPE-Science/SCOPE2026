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

# Computational verification and boundaries

Execute `python3 verify.py` in a directory containing that standalone script. No external packages, network, or proprietary software are required. The exact generated output is included as `verification_data.json`.

For the polygon orders 4, 6, 8, 10, 12, the program respectively checks 8, 54, 374, 2690, 19883 nonempty orbit faces; verifies complete dimensions and face-count tables; constructs 3, 24, 175, 1290, 9679 disjoint pairs; orients all Hasse incidences; and checks that a topological sort visits every nonempty face. The residual critical cells are one zero-cell and 1, 5, 23, 109, 524 top-dimensional cells. The first four cases also have a distinct exhaustive all-subset face count, while the fifth uses complete hereditary generation.

The mathematically essential lemma is that the half-turn fixed-point space is PL-homeomorphic to the orbit-barycenter subcomplex. The proof uses equality of barycentric coefficients on each chord orbit. The enumeration and acyclicity checks are finite and exact and do not extrapolate beyond the stated domain. Verification does not imply any independent validation or certification.
