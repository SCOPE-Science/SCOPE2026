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
# Reproducibility

Run `python3 verify.py` using the standard Python 3 library from the package directory. The script independently enumerates every primitive affine line using the two canonical coefficient normalizations, intersects them with the modular inverse hyperbola, and compares the entire multiplicity distribution against the formula. It also checks both incidence moment identities and the extremal line counts.

Observed output:

```
VERIFY_OK cases=15 all_primitive_lines=292402 first_moment=PASS sharp_maxima=PASS
```

The tested \(p,k\) values are \((3,1),(3,2),(3,3),(3,4),(3,5),(5,1),(5,2),(5,3),(7,1),(7,2),(7,3),(11,1),(11,2),(13,1),(13,2)\). All tested prime powers are finite: this verifies no unbounded universal quantifier, and cannot exclude a counterexample beyond the tested cases. The paper's classification rests on the stated arithmetic argument; the verifier provides a separate finite consistency check. No independent external audit has been carried out.
