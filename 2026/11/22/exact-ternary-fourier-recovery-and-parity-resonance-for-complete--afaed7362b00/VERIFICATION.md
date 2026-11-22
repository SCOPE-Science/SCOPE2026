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

# Reproducibility and mathematical checks

Run `python3 verify.py` in the directory containing this file. The standalone program uses Python standard-library integer arithmetic. It represents a Fourier value in the Eisenstein integers as the pair of coefficients of \(1\) and \(\omega\), where \(\omega^2+\omega+1=0\), and applies direct radix-three transforms to the independently generated proper-colouring indicator.

The actual run printed `VERIFY_OK cases=30 exact full DFT m+n<=9`. All ordered shore pairs with \(1\le m,n\le6\) and \(m+n\le9\) were tested. Each Fourier value, the spectral rank and nullity, largest singular value and smallest strictly positive singular value were checked without floating point.

The infinite proof is the two-shore inclusion–exclusion, signed-power zero classification, and exact character residue counts in RESULT.md. Finite verification supports these calculations but cannot establish their universal validity. Other graph families and other palette orders were not tested and are not claimed. No independent audit has been performed.
