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

# Verification

Run `python verify.py` with Python 3. The script is standard-library only and performs a direct finite census independently of the theorem's cluster-block construction, then checks the integer congruence certificate.

It enumerates all 638 labelled finite ultrametric bases of sizes one through four over alphabets of sizes two through four, plus every five-point base over three levels. For each base it enumerates admissible one-point distance vectors from the ultrametric three-point criterion, compares every indexed matrix entry with the claimed exact-distance rule, constructs the signed integer basis, computes its exact Bareiss determinant and checks all entries of its transformed Gram matrix. It also checks ranks modulo 2, 3 and 5. The exact expected terminal line starts with `VERIFICATION_OK` and the full output is in `verification_output.txt`.

The proof is independent of the finite search: it classifies every possible type and gives explicit unimodular basis vectors at arbitrary sizes. Finite tests are corroboration, not a proof for infinitely many bases. Independent audit is not performed.
