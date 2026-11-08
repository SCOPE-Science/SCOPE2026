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

# Reproducibility and limits

Run `python3 verify.py` in the same directory as this file. Only the Python 3 standard library is required. The executed checker reported:

```
PASS: 14,456 exact comparisons, complete G(n,m) enumerations for n=4,5,6
```

The program directly enumerates all labeled simple graphs for three orders and computes \(T\), \(O\), and \(TO\) from edge masks, without using the overlapping-triple derivation. It compares exact fixed-edge covariances with the overlap expression and factored identity, checks exact independent-edge covariances at six rational parameters per order, and checks the analytic identities and sign pattern across additional finite orders. All calculations use arbitrary-precision integers and rational arithmetic.

The finite checks do not certify the infinite-family statements by themselves. The general proof in `RESULT.md` rests on the exhaustive classification of ordered pairs of vertex triples, exact hypergeometric edge-inclusion probabilities, elementary algebraic factorization, and sign analysis. Historical novelty has not been independently validated.
