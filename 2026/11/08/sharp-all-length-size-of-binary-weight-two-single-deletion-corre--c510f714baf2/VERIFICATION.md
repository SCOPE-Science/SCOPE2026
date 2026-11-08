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

## Reproducibility

Execute `python3 verify.py` using Python 3.10 or later (standard library only). The script constructs the two explicit codeword families for each \(2\le n\le120\), computes *every* distinct single-deletion output of every word, and verifies pairwise shadow disjointness and attainment of the formula. For \(2\le n\le12\), it also independently builds the complete weight-two single-deletion confusability graph and uses an exact maximum-clique branch-and-bound in the graph of compatible codewords to establish the optimum on those finite lengths.

Expected output:

```
VERIFY_OK construction_lengths=2..120 exact_maximum_lengths=2..12
exact_maxima_n2_to_n12=1,1,2,3,4,4,5,6,7,7,8
```

## Proof limits

The finite computation does not prove the infinite-length theorem. The universal argument is the counting upper bound \(a+2b\le n-1\), the adjacent-index path upper bound \(a\le\lceil(n-1)/2\rceil\), and the explicit deletion-shadow-disjoint construction given in `RESULT.md`. No external independent validation is asserted.
