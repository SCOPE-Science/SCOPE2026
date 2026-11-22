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

# Reproduction and limits

The full theorem is proved in `RESULT.md`; the accompanying `checker.py` is a supplemental numerical falsification probe. Run with `python checker.py` using a Python 3 standard-library interpreter. The checker evaluates the two-group rational-parameter witness, compares the analytical resolvent derivative against four symmetric finite differences, checks the predicted zero and positive cross-group sensitivities in a three-group lower-triangular transmission network, and tests 200 positive parameter systems with two through six groups. A passing run prints the single `PASS` line.

The checker does not prove arbitrary-group convergence, infinitely many parameter choices, or originality. Those aspects depend on the analytic proof and separately recorded literature comparison. A sensitivity derivative is not proof of a feasible real-world intervention; no data calibration or external scientific audit is claimed.
