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

# Verification and reproducibility

The file `verify.py` is a standalone Python 3 standard-library diagnostic. Run it with:

```
python verify.py
```

The actual execution on the embedded file returned `COSINE_MAP_INVERSE_TAIL_VERIFY_OK`. It constructed thousands of remote inverse branches at four observation cutoffs and checked the two forward-output residuals, nonzero Jacobians and successive weighted-tail increments against the exact predicted factor \(2/(\pi|bc|)\). For \((a,bc,d,e)=(0.01,1.2,1,1)\), the observed weighted increment from \(R=2000\) to \(R=10000\) was approximately \(0.8535000\), compared with the predicted \(0.8538333\). These finite tests are diagnostics, not proofs of the asymptotic or non-sigma-finiteness claims.

Independent derivations in `RESULT.md` establish (i) the entire distant inverse lattice via monotonicity and a root-exhaustion argument, (ii) the Jacobian identity and summable reciprocal-error estimate, (iii) uniform remote-branch weights for bounded target sets and the area formula, and (iv) absolute continuity in the extended sense and lack of sigma-finiteness. These are the evidence for the infinite statements. The full real-plane domain and the nonzero parameters are essential. No independent mathematical audit or external certificate has been performed.
