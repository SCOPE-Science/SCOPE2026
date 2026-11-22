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

# Verification and scope

The standalone standard-library Python file `verify_peak_law.py` checks the exact formula against two independently formulated finite enumerators. The first explicitly loops over every descending vertex permutation for all \(n=2,3,4\) and every matching-deletion count \(0\le m\le n\). The second dynamic program over subsets of already exposed vertices counts peak occurrences independently of the proposed initial-run decomposition, testing every \(m\) for \(n=2,3,4,5,6\) and also \((n,m)=(7,3)\). All tests use exact integer counts and rational probabilities.

The checker also validates probability normalization, the degree-based exact mean, the full affine-mixture identity at each coefficient, and numerical consistency of the leading total-variation coefficient over several large orders and deletion fractions. Sample direct enumerated distribution: for \((n,m)=(3,3)\), \(\Pr(S=1,2,3)=(2/15,11/15,2/15)\).

Run:

```bash
python verify_peak_law.py
```

Successful run ends in:

```text
INDEPENDENT_FULL_PERMUTATIONS_PASS 4 5
INDEPENDENT_SUBSET_DP_AND_AFFINE_MIXTURE_PASS 6 7
INDEPENDENT_SUBSET_DP_PASS 7 3
FIRST_ORDER_TV_NUMERICAL_CROSSCHECK_PASS 500
VERIFY_OK
```

The verified finite checks cannot prove the uniform infinite-order asymptotic. That claim depends on the explicit initial-run and extra-peak proof and its summably uniform product expansion, provided in `RESULT.md`. The scientific correctness and originality judgments are same-model assessments, not independent certification. In particular, the full text of one older general local-maxima report was unavailable for historical-priority comparison.
