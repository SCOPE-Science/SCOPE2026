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

# Reproducibility and scope

Run `python3 verify_extension_geometry.py` with Python 3 standard library. Exact rational Gaussian elimination checks the matrix ranks for \(2\le m\le10\), deriving extension dimensions \(2m(m-2)\) and \(2(m-2)\) from the independent polynomial-gradient comparison map. An exact finite-field count validates the smooth rank-one-matrix quadric has \((q+1)^2\) points for \(q\in\{2,3,5,7\}\). The observed output ends in `VERIFY_OK` and `QUADRIC_VERIFY_OK`.

The all-\(m\) theorem is proved by coherent-system Ext exactness and line-bundle cohomology, not by the finite range of computed ranks. The moduli classification depends on unique simple subobjects and vanishing of cross Homs; the first splitting wall follows from the boundary map \(H^0(E(-6))\to H^1(\mathcal O(-3))\). Those arguments and their hypotheses are in `RESULT.md`. No independent mathematical audit or higher-\(m\) splitting census is asserted.
