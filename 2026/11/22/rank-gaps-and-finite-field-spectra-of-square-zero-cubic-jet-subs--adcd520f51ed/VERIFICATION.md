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

# Reproduction

Run `python3 verify.py` from a directory containing the supplied standalone file. The standard library alone is required. The recorded terminal output in `verification_output.txt` was obtained by executing that script, not by extrapolating a table.

The first test computes the quadratic substitution equation and independently row-reduces its coefficient matrix at all canonical square-zero linear maps through six generators for three prime fields. The second test evaluates every scalar-fixing endomorphism in two generators for field orders two and three, checks its literal second iterate, and compares all radical-rank fibers. The third test confirms that the formula's omitted integer ranks agree with the claimed interval-gap criterion through sixteen generators.

The proof for all finite fields and generator counts rests on block decompositions, linear algebra over dual numbers, Gaussian counts, and the direct asymptotic bound; computational sampling cannot certify its infinite quantifiers. Similar noncommutative results use the same module method, and global historical priority is not independently verified.
