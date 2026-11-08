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

The accompanying file `check_near_middle.py` requires Python 3 and NumPy. Execute `python3 check_near_middle.py` from a directory containing that file. In the preparation check, it constructed signed-intersection matrices for each \(1\le k\le4\) and \(a=0,1,2\), independently diagonalized the resulting twelve real symmetric matrices, and checked all predicted eigenvalues and multiplicities (largest matrix order 210). It also compared the exact integer coefficient extraction with the binomial/Catalan closed forms for \(1\le k\le149\), totaling 447 arithmetic parameter sets. It printed `NEAR_MIDDLE_WALSH_SPECTRUM_PASS`. Floating-point tolerance for direct eigenspectrum comparison is \(10^{-7}\); the theorem for all integer \(k\ge1\) is established by the printed proof, not by finite numerics.

The analytical dependencies are the classical Johnson harmonic decomposition and elementary coefficient extraction, monotonicity of central binomial/Catalan ratios, and Stirling asymptotics. No external formal certification or independent verification has been carried out.
