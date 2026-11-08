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

# Reproducibility of the finite result

The package contains two standalone exhaustive verifiers and an exact witness table. No downloaded data, external libraries or other result files are needed.

To run the subset-based proof computation:

```sh
python verify_subset.py
```

This checks all 17 sectors after visiting every one of the \(3^{16}=43,046,721\) labeled three-colorings as a unique ordered triple of disjoint color-class sets. It independently counts induced edges, checks the complete integer-minima table and equality counts, verifies all rational coexistence knots and the independence polynomial, and checks the JSON exact witnesses.

To run the second, independently encoded base-three exhaustive enumeration:

```sh
cc -O3 -std=c99 verify_ternary.c -o verify_ternary
./verify_ternary
```

This decodes the same \(3^{16}\) configurations directly from ternary integers and sums the graph's 40 edge penalties without using the subset recurrence. Both verification paths completed successfully and agreed on the complete minimum/count arrays. Their loops are finite and exhaustive; the computation does not make any infinite-system assertion. The rational envelope deduction appears in RESULT.md and is checked for every sector by `verify_subset.py`.

The mathematical review reported in REVIEW.md is same-model only; no independent scientific audit, external certification or additional verification channel is asserted.
