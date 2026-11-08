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

# Verification

The attached `bipartite_variance_checker.py` uses only Python standard library exact fractions; run from the directory containing it with `python bipartite_variance_checker.py`. Its independent signed-constraint vertex reconstruction compares the exact real variances to the scalar lattice formula for sizes \((2,2)\) and \((3,2)\) at parameters \(1\), \(3/2\), and \(2\). It independently enumerates the vertices of the two-variable Hilbert upper-bound linear program for 560 rational parameter combinations; tests all parity endpoint cases with part sizes from two to thirteen; and evaluates the balanced even formula at forty parameter points. The expected final line is `ALL_BIPARTITE_VARIANCE_DIAGNOSTICS_PASSED`. The proof in RESULT.md, rather than the finite tests, supports the all-parameter statements. Independent mathematical audit remains unperformed.
