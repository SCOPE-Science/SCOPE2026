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

# Reproducible checks

Run `python3 VERIFY.py` from the directory containing this document and the script. It has no third-party dependencies.

The script generates all six exceptional curves, fifteen line transforms and six conic transforms, checks that their class sum is the anticanonical multiple, that every intersection number off the diagonal is zero or one, that every row has ten neighbors and that all common-neighbor counts match parameters \((27,10,1,5)\). It recomputes three reduced determinants by exact Bareiss elimination and separately performs \(3\)-adic and \(5\)-adic Smith pivot elimination at three deletion indices. Its success marker is `SCHLAEFLI_27_LINE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK`.

**Observed exact outputs:** for deletion indices 0, 18 and 26 the spanning-tree count is 5129015115539641837921875; the \(3\)-valuations have frequencies \(0:7,2:14,3:5\), and the \(5\)-valuations have frequencies \(0:20,1:6\). The resulting invariant factors, including units, are \(1^7,9^{13},45,135^5\).

The calculation settles a specified finite integer matrix. Geometry of the cubic surface and the regular-smoothing interpretation use the standard descriptions and arguments in `RESULT.md`; the executable check does not independently verify global algebraic geometry or historical priority. Independent mathematical audit has not been performed.
