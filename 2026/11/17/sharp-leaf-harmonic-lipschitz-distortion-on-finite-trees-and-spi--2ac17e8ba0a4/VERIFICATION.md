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
# Reproducible mathematical checks

Run `python3 check_harmonic_extension.py` using Python 3 and its standard library only. The checker builds independent exact rational Dirichlet systems and enumerates every extreme tree-edge sign assignment on ten spiders, comparing the resulting sharp edge slope with the formula. Four additional non-spider trees are checked by comparing direct finite harmonic-measure cut sums with sign enumeration. All compositions of a prescribed edge count into a prescribed number of positive arm lengths are enumerated for \(4\le n\le12\), verifying the balanced optimum for 45 order/arm-count pairs. Four larger explicit families corroborate the asymptotic rate.

Actual successful diagnostic output:

```text
EXACT_HARMONIC_DIRICHLET_VS_INDEPENDENT_SIGN_ENUMERATION_PASSED 10
GENERAL_TREE_HARMONIC_MEASURE_CUT_IDENTITY_CHECKS_PASSED 4
EXHAUSTIVE_FIXED_ORDER_AND_LEAF_COUNT_SPIDER_EXTREMA_PASSED 45
SQRT_ORDER_ASYMPTOTIC_WITNESSES_PASSED 4
ALL_HARMONIC_EXTENSION_DIAGNOSTICS_PASSED
```

The all-tree norm identity, branching-rigidity theorem, complete optimizer classification and infinite \(\sqrt n/2\) limit are mathematical proofs in `RESULT.md`. Finite checks do not establish these universal assertions and no external or independent certification is claimed. The source comparison is limited by incomplete access to the full older tree-Dirichlet paper.
