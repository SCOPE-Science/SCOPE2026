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

# Computational verification and scope

Run `python3 verify_prime_triplets.py`, with Python 3's standard library only, in the directory containing the included program. The recorded output is provided in `verification_output.txt`.

For each of 66 positive indices in each family, the program computes the exact denumerant capped at two by a three-stage unbounded-coin dynamic program. It evaluates every integer through \(4a^2\) and checks that the largest with fewer than two representations equals the claimed polynomial. It also checks that every integer between the claimed threshold plus one and that test limit has at least two representations. The family minima at \(k=0\) are checked separately. Both tests passed on the provided program and output.

The proof of the all-parameter statement is symbolic and appears in `RESULT.md`. Finite computation is not substituted for that proof. The literature comparison is limited to accessible material and can miss an equivalent unindexed statement. No independent external audit is represented by this document.
