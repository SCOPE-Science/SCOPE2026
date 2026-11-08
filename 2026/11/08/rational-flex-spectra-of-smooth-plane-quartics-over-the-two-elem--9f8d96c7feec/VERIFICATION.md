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

# Exact verification

Both dependency-free programs, `verify_orbits.py` and `verify_direct.py`, executed successfully with the expected termination markers `VERIFY_ORBITS_OK` and `VERIFY_DIRECT_OK`. The first enumerated all nonzero degree-four equations and their projective equivalence classes, decided geometric smoothness via three-chart Gröbner-unit tests, then calculated tangent contact multiplicities. The second iterated all \(10920\) smooth equations rather than only representatives and independently calculated their characteristic-two Hasse jets.

The exact smooth population is \(10920\), the exact smooth projective class count is \(78\), and the unique four-flex stratum has exactly one projective orbit containing \(168\) equations. The displayed representative's four rational flexes were explicitly checked via tangent polynomials. The smoothness decisions on all \(279\) orbit representatives were also cross-compared with a separate computer-algebra Gröbner test. No random sampling or unbounded inference occurs.

The programs are executable Python source, not external formal proof certificates; a future independent audit may inspect their implementation. No independent mathematical review has occurred.
