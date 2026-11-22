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

# Verification of phase-controlled hub transport

Run the standalone Python programs from a directory containing the `verification` subdirectory:

```
python3 verification/verify_algebra.py
python3 verification/verify_direct.py
```

The first requires SymPy and exactly checks the two-by-two Hermitian Gram matrix and full characteristic polynomials for unit-phase examples with frequency ratios \(2:1\) and \(3:1\), as well as a destructive-interference example. It also checks the polynomial maximum \(16/27\) at the \(3:1\) resonance and the exact inverse formula between frequency ratio and phase-resultant modulus.

The second requires NumPy and SciPy. It directly constructs the full \((m+2)\)-dimensional Hermitian matrix and computes \(e^{-itH}\) using a separate dense-matrix exponential for 264 phase/time configurations with \(m=2,\dots,12\), checking the derived amplitude against the full calculation with error below \(2\cdot10^{-13}\). It also tests a complete-transfer phase choice, an explicit non-transfer phase choice, a dark configuration and an irrational-frequency example whose transfer probability exceeds \(0.998\).

These checks passed. The all-size statements are proved in the accompanying \(\texttt{RESULT.md}\): the symbolic and finite numerical tests are reproducibility aids and do not by themselves establish statements quantified over all graphs or all phases. The historical originality assessment has not undergone independent external examination.
