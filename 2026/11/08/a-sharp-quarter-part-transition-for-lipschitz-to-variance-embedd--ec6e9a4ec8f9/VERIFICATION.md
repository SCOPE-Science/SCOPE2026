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

# Verification of the sharp multipartite Lipschitz-to-variance norm

The supplied `checks/verify_multipartite_spread.py` is a standalone Python standard-library script. Run it with `python3 checks/verify_multipartite_spread.py` after extracting the package; no external data files or dependencies are required.

The enumeration anchors one vertex to value zero and exhausts every integer assignment with edge differences at most one for every unordered positive part profile of order two through eight. The proof separately establishes that every true extremizer belongs to the enumerated integer class. Every maximizing assignment is compared against the exact formula and the binary/polarized equality characterization, using exact `Fraction` arithmetic. Recorded successful output:

```
EXHAUSTIVE_INTEGER_LIPSCHITZ_PROFILES_AND_EQUALITY_SHAPES_OK 58 13800 968
SHARP_QUARTER_PHASE_AND_TIE_CERTIFICATES_OK 499497
ALL_MULTIPARTITE_SPREAD_CHECKS_OK
```

The residue-class boundary computation is independently cross-checked for \(4\le N\le1000\), but this finite range is not used as a universal proof. The proof's independent arguments are the tight-edge graph rank criterion, integer-valued extrema, variance calculations and four-residue threshold inequalities. The literature comparison identifies prior extreme-potential classification as antecedent; novelty is restricted to sharp norm/equality optimization and its phase behavior. No independent audit has been performed.
