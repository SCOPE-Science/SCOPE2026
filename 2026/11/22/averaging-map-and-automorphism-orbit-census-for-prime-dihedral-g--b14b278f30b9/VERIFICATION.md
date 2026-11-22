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

# Verification of the prime-dihedral averaging-map census

Run `python3 artifacts/verify.py` using the standard Python 3 library. The script constructs all image-subgroup strata, checks that each candidate meets the group averaging identity for every pair of elements, detects duplicate candidates, enumerates the full affine automorphism group, and counts its map orbits. For \(p=3\) it independently finds 129 total, 51 pointed, 60 total orbit classes, and 25 pointed orbit classes; for \(p=5\) it finds 15965, 3305, 3969, and 824, respectively. Successful completion prints `PRIME_DIHEDRAL_AVERAGING_VERIFIED`.

The computation has finite scope. General validity for all odd primes follows from the subgroup classification and Burnside calculations in RESULT.md. All other dimensions and composite rotation orders are outside this proof. Independent audit is not performed.
