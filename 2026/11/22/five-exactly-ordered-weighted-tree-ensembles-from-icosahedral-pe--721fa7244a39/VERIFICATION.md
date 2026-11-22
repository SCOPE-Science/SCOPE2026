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

# Exact reconstruction and limits

Run the package's standalone Python 3 programs in the same directory:

```bash
python3 verify_laplacian.py
python3 verify_transfer_current.py
```

The first enumerates all 125 matchings of the icosahedron and reconstructs every degree-at-most-six weighted tree polynomial from seven exact integer matrix-tree determinants, with a checked eighth integer value. It certifies five polynomial classes, class counts 5/20/60/30/10, and the positive quotient of adjacent polynomial differences by \(t-1)^2\. The second independently computes 1,000 rational transfer-current determinant values after checking an explicit isomorphism between separately constructed graphs. Both actually passed from the named source files. The 125-matching enumeration is exhaustive because each perfect matching has a unique first paired vertex at every recursive step.

These are exact finite computations establishing a finite graph classification, not statistical experiments, a theorem for arbitrary graphs, or an external scientific audit.
