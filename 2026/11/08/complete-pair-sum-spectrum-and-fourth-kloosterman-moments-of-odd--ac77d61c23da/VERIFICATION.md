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

`CHECKER.py` uses only the Python 3 standard library and runs without external data. It computes the exact ordered-pair convolution over \(\mathbb Z/p^k\mathbb Z\), compares the full positive-multiplicity histogram and additive energy against the formulas, and directly evaluates all Kloosterman Fourier frequencies for six small odd moduli including \(15\) to check CRT.

Exact checks cover \((p,k)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,1),(7,2),(11,1),(11,2)\); numerical Fourier moment checks cover \(n=3,5,9,15,25,27\) with relative tolerance \(10^{-6}\). The nonstandard proof steps are the complete root-lifting classification and its careful multiplicity count. All unbounded quantifiers rely on the symbolic proof in `RESULT.md`, not these instances.

The finite-field \(k=1\) case is historical background. Even modulus, weighted sharp extension, and independent audit are outside the established claim.
