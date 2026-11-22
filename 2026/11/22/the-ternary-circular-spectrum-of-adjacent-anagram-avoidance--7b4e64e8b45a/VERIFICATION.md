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

Run `python3 verify_spectrum.py` and `python3 verify_bruteforce.py` from an extracted copy of this package. Both use the Python standard library only.

The first program constructs the integer triple-overlap matrix from the original forbidden-block predicate. It independently calculates traces of its first \(27\) powers, uses exact Newton identities to recover all characteristic coefficients, and verifies the proposed factorization of \(\det(I-zT)\) coefficient by coefficient. The second enumerates all ternary indexed words for lengths one through eleven and compares the cyclic block predicate directly, without using matrix traces; it also checks primitive rotation classes through length nine.

Recorded checks: exact determinant certificate passed; all first fifteen transfer trace values passed; all eleven exhaustive finite length comparisons passed; primitive-orbit identity checks through length nine passed. The finite enumeration is a cross-check only, while the all-length proof relies on the closed-walk bijection and exact determinant identity. These are same-package calculations, not independent expert certification. The package does not attempt to resolve historical equivalence across all possible literature.
