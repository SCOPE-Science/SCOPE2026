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

# Reproduction

Run `python artifacts/verify.py` with an ordinary Python 3 interpreter from this package root. The script has no nonstandard Python dependencies. Its token-graph generator applies the symmetric-difference edge definition without using the proof classification. Bron–Kerbosch on the complement independently enumerates every maximal independent set for all \(2\le m,n\le5\). It compares labelled sets and cardinality multiplicities, not merely total counts. For all \(2\le m,n\le7\), each structurally generated candidate is separately tested for independence and domination under the token-move graph adjacency. It also checks the closed total count and the minimum cardinality and minimum-set counts for \(2\le m\le7\), \(m\le n<10\).

Observed output ended with:

```
DIRECT_MAXIMAL_INDEPENDENT_OK 5 5 677
FORMULA_AND_DOMINATION_OK m,n=2..7
INDEPENDENT_DOMINATION_AND_MINIMUM_COUNTS_OK 2<=m<=7, m<=n<10
VERIFY_OK
```

The unrestricted theorem is established by its independent mathematical argument. Finite checks are confirmatory and cannot certify all parameter values. Independent mathematical audit was not performed.
