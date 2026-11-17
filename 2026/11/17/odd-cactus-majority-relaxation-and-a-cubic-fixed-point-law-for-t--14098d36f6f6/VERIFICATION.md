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

With Python 3, from the directory containing the two scripts:

```
python verify_majority.py
python verify_transfer.py
```

`verify_majority.py` directly constructs each labelled triangular cactus chain and applies all \(2^{2n+1}\) synchronous binary majority updates for \(1\leq n\leq8\). It checks both one-step and two-step fixed populations against the claimed sequence, reporting \(2,6,12,26,56,120,258,554\), and \(174{,}760\) distinct initial states total.

`verify_transfer.py` independently enumerates run lengths, verifies the matrix recurrence for each \(1\leq n\leq80\), and enumerates all binary states on six odd-cycle bouquets: one three-cycle, one five-cycle, two triangles, a triangle with a pentagon, three triangles, and two pentagons. Each case verifies equality of the one-step and two-step fixed counts.

These are finite reproducibility checks only. The full-parameter conclusions rely on the stated proofs of the bipartite-cycle obstruction, precise boundary word grammar, and transfer generating function. No independent external mathematical review or certification is asserted.
