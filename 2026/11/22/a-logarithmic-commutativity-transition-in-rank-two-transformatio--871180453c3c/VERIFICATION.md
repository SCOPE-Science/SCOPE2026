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

# Verification details

`verify.py` is a complete, Python 3 standard-library-only checker. Run `python3 verify.py` from the directory containing the file. Its output is recorded exactly in `verification_output.txt`.

It checks direct composition for every ordered pair of self-maps in all \(2\)-, \(3\)- and \(4\)-point rank-two sandwiches, compares against the seven-base closed formula, and separately recomputes the formula via every admissible equality-partition/fiber-color type for all 66 parameter pairs \(2\leq n\leq12\). It also tests a change of fiber placement at \(n=4,k=2\).

Direct enumerations verify six small instances, not the whole infinite family. The infinite-size conclusion rests on the exhaustive 18-case symbolic partition proof, and the asymptotic window is proved by the displayed exact ratios rather than numerical convergence. The comparisons at \(n=100,1000,10000\) are illustrations only. No independent validation or audit was performed.
