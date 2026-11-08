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

`python3 check.py` is a complete, dependency-free verifier of the **finite** combinatorial identities cited in RESULT.md. It enumerates all \((n-1)!\) parent arrays for every order \(3\le n\le8\), independently computes the indicator of no childless children at each vertex, checks exact single and joint probabilities for all vertex pairs against falling-factorial inclusion–exclusion, compares first/second moments, and checks the sole undirected-root boundary correction. Rational comparisons use `fractions.Fraction` and are exact. The script also checks the algebraic constant and numerically integrates the two-point limiting covariance kernel; this integral check is approximate, with an explicit tolerance.

Observed output on replay:

```
n=3: 2 trees; mean=2; variance=0
n=4: 6 trees; mean=5/2; variance=1/4
n=5: 24 trees; mean=19/6; variance=5/36
n=6: 120 trees; mean=91/24; variance=143/576
n=7: 720 trees; mean=177/40; variance=1253/4800
n=8: 5040 trees; mean=3641/720; variance=158879/518400
constant= 0.03812640853839578 pair numerical= -0.08066388550615114
PASS: all exhaustive rational and numerical consistency checks
```

**Proof boundaries.** Finite enumeration does not imply uniform asymptotic covariance estimates. The analytical proof derives the exact fixed-size probabilities, controls the inclusion–exclusion tails by factorial moments, and proves a uniform first-order covariance expansion without singular division by the age coordinates. Convergence of the resulting Riemann sums establishes the variance; the central limit theorem invokes the already-published joint fringe-tree Gaussian limit. This package has not received independent mathematical validation.
