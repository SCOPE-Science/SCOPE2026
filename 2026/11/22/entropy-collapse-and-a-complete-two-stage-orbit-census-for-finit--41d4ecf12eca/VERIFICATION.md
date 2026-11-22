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

# Verification and reproducibility

Run `python3 checker.py` in a directory containing the accompanying program, with Python 3.10+ and SymPy installed. It rebuilds the forbidden-six-word five-block adjacency matrix; checks 14 states and 18 edges; exactly checks the two polynomial identities; confirms primitivity through positive fifteenth matrix power and the seven-state symbol-interchange quotient; and compares traces with direct enumeration of every binary cyclic word at periods 1 to 12. The executable checks passed when run from the candidate package.

The exact uniform entropy inequality follows from the run-boundary tower conjugacy, finite-fiber entropy preservation, ergodic-measure variational principle, and complementary-symbol symmetrization as proved in `RESULT.md`; the program does not claim to certify those infinite-dimensional arguments. The numerical Perron root is an approximation to a uniquely specified algebraic number. The checker requires SymPy; no missing data files or external downloads are required. No independent mathematical audit has been performed.
