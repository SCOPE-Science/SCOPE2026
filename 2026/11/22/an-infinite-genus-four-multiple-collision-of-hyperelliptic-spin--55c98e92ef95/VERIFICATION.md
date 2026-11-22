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

The bundled `verify_spin_collision.py` was executed using Python's standard library, without relying on prior-run computation logs. It constructs all spin classes from subsets modulo complement for genus four and genus eight, compares their complete orbit multisets, verifies fixed-point counts at each power and checks the general binomial formula for the first ten values of \(r\). The expected final marker is `INFINITE_HYPERELLIPTIC_SPIN_COLLISION_CHECKS_OK`.

The mathematical proof applies to all positive integers \(r\): at each odd extension, \(d=\gcd(8r,n)\) is odd and \(8\mid 8r/d\), forcing the two parity counts to agree; at even extensions, the branch permutations have conjugate powers. The finite test cannot establish the universal quantifiers by itself. The novelty assessment remains qualified by the possibility of unidentified earlier equivalent statements. No independent audit has been performed.
