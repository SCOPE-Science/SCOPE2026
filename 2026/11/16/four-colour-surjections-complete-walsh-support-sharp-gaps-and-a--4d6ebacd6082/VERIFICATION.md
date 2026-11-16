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

# Verification of the mathematical result

`verify.py` is standard-library-only and reconstructs the actual onto-word indicator for every \(n=4,5,6,7,8,9\), independent of the closed algebraic Fourier formula. It performs the integer Walsh–Hadamard transform, compares all \(349{,}440\) coefficients with the formula, and verifies exact support counts and the least nonzero multiplier magnitudes. It reconstructs the range-projection kernel for \(n=4,5,6,7\), testing even-length contractivity and odd-length negative-kernel witnesses. The run returned marker `QUATERNARY_SURJECTION_WALSH_EXACT_PASS`.

Observed ranks for \(n=4,5,6,7,8,9\): \(64,196,1024,3550,16384,60616\). Observed sharp multiplier gaps: \(8,16,8,16,8,16\). Exact endpoint projection norms for \(n=4,5,6,7\): \(1,91/16,1,14107/1024\). These are finite checks only; the proof of all-length statements is in `RESULT.md`.

The proof of absence of extra even-length zeros uses the exact four-case character formula and arithmetic modulo eight; the odd-length extra zeros use the nonzero-vector character sum; the gap uses explicit frequencies. Neither a computer check nor a package hash constitutes independent mathematical validation.
