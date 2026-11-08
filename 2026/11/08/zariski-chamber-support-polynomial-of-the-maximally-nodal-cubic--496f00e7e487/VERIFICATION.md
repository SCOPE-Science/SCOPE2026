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

# Reproduction and boundaries

The two standalone verification programs use only the Python standard library. From the same directory run `python verify_exhaustive.py` followed by `python verify_graph.py`. The first constructs divisor classes as integral vectors in the plane-blow-up intersection lattice, tests all \(2^{13}=8192\) subsets with exact rational elimination, and outputs the negative-support histogram. The second classifies the sixty-four labeled graphs on four vertices into eleven isomorphism classes and expands the independent Schur-complement graph enumerator. Expected coefficients in both cases: `1, 13, 69, 186, 260, 168, 29`, total `726`. The actual transcript of these two program executions is `verification_output.txt`. The first ends in `ALL_CHECKS_PASSED`, and the second prints the identical polynomial and total.

These computations are exhaustive conditional on the full negative-curve classification. The geometric proof of that classification appears in RESULT.md and does not depend on computer enumeration. No finite-field extrapolation, numerical eigensolver, external proof system, or independent expert audit is claimed.
