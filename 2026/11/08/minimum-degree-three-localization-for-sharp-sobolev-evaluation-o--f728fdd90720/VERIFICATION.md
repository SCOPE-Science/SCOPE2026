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

# Reproducibility and scope of verification

Run `python3 check_multipartite.py` using only the Python standard library. On a successful execution it prints `ALL_MULTIPARTITE_H1_CHECKS_PASSED`.

The verifier performs 2,910 exact rational vertex-resistance and class-orbit checks across 63 part-size profiles, confirms localization for those 63 finite cases, checks 33 independently subdivided-edge resistance integrals, reconstructs 22 double arclength resistance integrals by exact Simpson integration of the independently calculated quadratic profiles, and confirms seven exact rational sharp constants.

The computations depend only on the supplied program. They do not exhaust all sizes or all continuum positions and make no claim of infinite computer certification. The analytical proof in `RESULT.md` establishes the general identity, the comparison of all edge classes, the strict degree threshold, and the equality classification. No independent mathematical audit has been performed.
