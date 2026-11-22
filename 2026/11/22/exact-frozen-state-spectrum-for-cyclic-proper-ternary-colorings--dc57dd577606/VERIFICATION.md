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

# Verification methods and limits

Reproduce using `python3 verify.py` (Python 3.10 or later; standard library). Its direct neighborhood evaluation on each proper ternary cyclic coloring for lengths \(3\) through \(13\) agrees with the equal-increment-triple local characterization, and its frozen counts agree with the closed formula. Independently enumerating all \(2^n\) cyclic increment strings through length \(20\), filtering both the modulo-three closure and two excluded triples, gives the same counts. The code also checks the explicit even/odd existence witnesses through length \(301\) and the unweighted transfer trace recurrence.

The proof's noncomputational steps are the cyclic increment bijection, the local swap iff homogeneous triple lemma, the two degree-four determinant evaluations and the roots-of-unity filter. The asymptotic statement additionally uses the roots of the stated cubic and Lucas polynomial. Finite checks do not establish the theorem for arbitrarily large lengths. No independent audit or formal certification is asserted.
