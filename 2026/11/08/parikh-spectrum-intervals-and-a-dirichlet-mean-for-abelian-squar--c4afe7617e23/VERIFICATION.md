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

# Verification record

Execute \(\texttt{python3 reproduce.py}\) with Python 3 standard library, from the artifact directory. The file performs exact direct enumeration of the half-Parikh classes of Abelian squares in every binary word containing three ones through length \(32\), a total of \(40920\) words. The observed output on the included file was:

```text
DIRECT_HALF_PARIKH_OK 40920
EHRHART_VERTEX_VOLUME_OK 7 10 15552 7488
DIRICHLET_EXPECTATION_OK 157/288
ALL_CHECKS_PASSED
```

The two polytope vertex sets are recovered by exact rational Gaussian elimination through all four-hyperplane intersections, verifying cardinalities seven and ten and that every coordinate denominator divides twelve. Exact integer lattice counts at dilations \(0,12,24,36,48\) are compared against the values in RESULT.md; fourth differences give four-volumes \(1/32\) and \(13/864\). The theorem that these finite differences compute the volume is Ehrhart's theorem and is an analytic premise, not an empirical inference. The proof of the all-length wordwise formula is the interval lemma in RESULT.md. Neither direct enumeration nor lattice checks are independent mathematical audits.

Limitations: the complete limiting cumulative-distribution formula and convergence rate are not supplied, and publication priority remains subject to unindexed literature. No external validation has been performed.
