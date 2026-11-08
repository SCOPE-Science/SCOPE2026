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

# Verification notes

The standalone Python 3 script `verify_roots.py` computes the complete set of matrices commuting with the nonzero rank-one square-zero matrix having a single \(1\) in position \((1,2)\). Each root of \(X^m=C\) necessarily commutes with \(C\), so this restricted enumeration is exhaustive. The program computes actual powers and ranks and compares every counted rank stratum with the partition/centralizer formula. Run `python verify_roots.py`; the expected exact standard output is included in `verification_output.txt`.

Enumerated field orders are \(q=2,3,4,5\), including genuine nonprime \(\mathbb F_4\). Enumerated dimensions and exponents are recorded line by line in the output. All eleven cases passed; the marker is `ALL_MINIMAL_NILPOTENT_POWER_FIBERS_PASS`. The algebraic argument separately establishes the result for all finite fields and every \(n,m\) in its scope. This evidence is finite corroboration, not an infinite computational certificate. Only a self-review was performed; no independent audit was requested or conducted.
