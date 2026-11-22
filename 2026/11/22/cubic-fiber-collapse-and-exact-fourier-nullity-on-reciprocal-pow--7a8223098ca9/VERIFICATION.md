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

# Reproducibility and limits

Run `python verification/check.py` from the package root. The program verifies: the divisibility and parity hypotheses, the exact index-three subgroup, the entire three-element preimage of every phase, the order of \(-2\), and the character-mode nullity, for 13 qualifying primes up to 700. For the first two qualifying primes, 31 and 43, an independently constructed complex matrix has numerical ranks 28 and 38, matching predicted nullities 2 and 4. Results obtained by direct execution of the embedded program:

- \(p=31\): \(k=10\), \(d=19\), \(t=10\), nullity \(2\), rank \(28\).
- \(p=43\): \(k=28\), \(d=13\), \(t=7\), nullity \(4\), rank \(38\).
- Additional admissible primes checked: 157, 223, 229, 277, 283, 439, 457, 499, 601, 643 and 691.

These tests do not establish the theorem for infinitely many primes; the proof uses the exact character sum factorization and a nonvanishing cyclotomic argument. Small floating-point singular values are only supplementary diagnostics, not exact rank certificates.

The proof does not establish infinitely many qualifying primes or quantitative invertibility bounds on the nonzero singular values. No independent mathematical audit has been conducted.
