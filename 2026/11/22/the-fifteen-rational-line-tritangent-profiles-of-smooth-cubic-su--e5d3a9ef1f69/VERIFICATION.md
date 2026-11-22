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

# Exact computational verification

Running `python verify.py` with Python 3.9+ and SymPy performs the full characteristic-two finite enumeration. The `orbits.csv` companion is a certificate, not an unvalidated assumed orbit partition: the script visits all 1,048,575 nonzero cubic forms, verifies the 141 orbit sizes, and establishes generation of the order-20,160 substitution group. Four-chart derivative ideal Gröbner tests check geometric smoothness over an algebraic closure; then explicit arithmetic in fields with 2, 4 and 8 elements builds all Frobenius-stable three-line sections. All 15 rational planes and 35 rational lines are tested per smooth representative.

Expected result: `BINARY_CUBIC_TRITANGENT_CENSUS_VERIFIED all_forms=1048575 all_orbits=141 smooth_orbits=36 smooth_forms=322560 joint_profiles=15 tritangent_section_forms=106 sum_hist=322560`. Full weighted and projective-orbit distributions follow.

The checker is exhaustive within the finite object and verifies its own certificates. It does not establish originality independently, deduce statements about other finite fields, or perform independent mathematical audit.
