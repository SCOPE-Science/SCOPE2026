---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Mark an unordered pair of leaves with fixed common neighbor and delete both: a bijection to a uniform labelled tree on n-2 vertices. Reinserted leaves contribute two while the fixed center can no longer be a leaf. The Prüfer code on the reduced tree is an iid word of length n-4 and the remaining leaf count is the number of absent noncenter labels among n-3 eligible symbols, proving every binomial moment. Multiplying by the ordinary marked-pair expectation gives E C and mixed covariance; monotonicity of (1-1/x)^(x-2) proves strict positivity. Overlapping marked pairs give the stated C factorial second moment and the n=4 boundary; asymptotic expansions deliver 0.6178583783. Checked checker source through n=8 and matched exact previous primary formula by symbolic term comparison; these finite checks are corroborative.

## originality

FAIL

FAIL, multiple independent stronger published sources: 2026-10-26 Leaf-sibling Palm dominance in uniform labeled trees gives exactly the same count of all degree-unrestricted sibling-leaf pairs, the identical size-biased law 2+Z with the same n-3 designated boxes/n-4 draws, all factorial moments, positive all-size covariance, plus stronger stochastic domination. Another 2026-11-08 complete published theorem Cherry-Palm deletion and persistent leaf–symmetry correlation gives the same unrestricted model, exact full test-function deletion identity, covariance and limiting Pearson 0.6178583783. The 2026-10-25 exact conditional joint (L,C) polynomial determines the entire bivariate law. All three primary scientific texts were read fully. This is exact statement-level mathematical coverage.

## value

FAIL

FAIL as a new scientific contribution because the specific all-order size-biased law, positive covariance, and limiting Pearson constant were explicitly published before this record; additional independent finite checking and changed notation do not make the repeated invariant unknown or independently valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
