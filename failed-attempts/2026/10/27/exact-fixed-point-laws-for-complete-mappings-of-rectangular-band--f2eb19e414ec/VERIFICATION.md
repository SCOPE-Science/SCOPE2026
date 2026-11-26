---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The band product forces each orthomorphism row to be a bijection of columns. For each reached column, the first coordinates of the images under α then run through a permutation of the rows, independently across those columns. This yields a bijection to the independent row and column permutation choices, and its product count. For a specified subset of cells T, α fixes every cell exactly when each incident row permutation fixes its specified columns and each incident column permutation fixes its specified rows. A uniform m-permutation fixes r specified points with probability (m−r)!/m!, and expansion of the product of 1+(t−1) times the fixed-point indicator gives the entire stated PGF. The singleton probability is 1/(ab). Ordered distinct pairs in a common row, a common column, and neither contribute 1/a, 1/b, and (a−1)(b−1)/(ab) respectively to the second factorial moment, equal to the variance since the mean is one. For one side of length one this is the ordinary uniform permutation, including deterministic variance zero at 1×1. For fixed k there are at most k nonempty row factors and k nonempty column factors; each specified k-cell event has probability (ab)^(−k)(1+O_k(1/a+1/b)) uniformly as both sides grow. The factorial moments therefore tend to 1, which gives ordinary moment convergence and the Poisson(1) law by moment determinacy.

## originality

FAIL

The distinct indexed finite-band result 522c8013084e gives both the count and precisely the labeled row-column product parametrization, including its explicit formula for α on a cell. Its displayed cycle polynomial is for θ, not α, and is not itself the answer. But its parametrization already gives the entire uniform law of α as a product of independent unrestricted permutations. Requiring the two component permutations to fix the row and column indices on T gives the frozen full PGF directly by the standard specified-fixed-point probability, not by a new structural lemma. The finite correction and restricted two-growing-side limit then follow by ordinary second-moment counting and fixed-order factorial moments. This is direct implication of the audited claim, not a finding of earlier priority based on the distinct record's later path date.

## value

FAIL

The fixed-point statistic is naturally motivated by the semigroup cycle question and its precise finite correction could be useful in isolation. As a distinct contribution relative to the current indexed result, however, it is a mechanically obtained narrow invariant of an already specified independent-permutation parametrization. The two-growing-side Poisson limit uses only its uniform fixed-order factorial estimate; the frozen record offers no other asymptotic regime or α cycle analysis that survives independently of that calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
