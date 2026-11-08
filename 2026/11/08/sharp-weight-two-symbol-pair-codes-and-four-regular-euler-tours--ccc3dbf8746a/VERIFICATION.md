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

Run `python3 verify.py` using Python 3 standard libraries only. Its actual execution returned:

```
VERIFY_OK exhaustive_sizes=2..9 graph_witness_sizes=10..150
n=10 witness: [(0, 7), (5, 9), (3, 8), (2, 6), (1, 4)]
```

The checker represents a codeword by the pair of its one-coordinates and independently implements the cyclic ordered-pair read distance. For each \(n=2,\ldots,9\), it verifies the claimed witness and iterates all choices of one additional codeword beyond the claimed optimum, rejecting every hypothetical larger valid code. For \(n=10,\ldots,150\), it constructs the circulant graph, computes its Euler circuit, checks twice-occurring vertex labels, and verifies all codeword pairs by direct pair read. The even-length cases additionally check all adjacent label edges are distinct and nonloops. The witness family is not an exhaustive enumeration of all optima; the converse follows from the proof. Finite checks do not substitute for proof at unbounded lengths.

Independent mathematical audit: not performed.
