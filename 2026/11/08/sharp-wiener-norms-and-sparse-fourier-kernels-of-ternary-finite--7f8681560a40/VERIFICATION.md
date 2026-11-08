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

# Verification of the quadratic-shell Fourier norm

The main proof in `RESULT.md` applies to every odd prime power; the following computation tests finite instances only. Run `python checker.py` after installing dependencies in `requirements.txt`.

The checker builds exact finite-field arithmetic as polynomial residue arithmetic over the prime field. For each field order \(q\) it selects a nonsquare parameter and tests two nonzero quadratic radii, giving \(\varepsilon=-1\) and \(\varepsilon=+1\). It enumerates the indicator of the three-dimensional quadratic shell, computes its full additive Fourier transform with multidimensional prime-field FFTs, and compares **every** Fourier coefficient with the stated Salié/Gauss formula after an explicit trace-dual coordinate change. It also checks the exact cardinality, four frequency-sector counts (origin, isotropic, square, nonsquare), Parseval's identity, and the sharp absolute Fourier sum.

Fields checked: \(q=3,5,7,11,9,25,27\). Both discriminant classes pass in every field; the maximum pointwise coefficient discrepancy is below \(6\times10^{-14}\) in double precision.

For \(q=3\), the two exact norms are \(16/9\) and \(8/3\). The corresponding numerical norms are \(1.777777777778\) and \(2.666666666667\). For \(q=9\), they are \(5.530864197531\) and \(6.666666666667\), and for \(q=25\) they are \(15.609926291999\) and \(16.827553482999\). The implemented checks also cover prime-field orders \(5,7,11\) and a cubic extension of characteristic three.

Checker terminus: `TERNARY_QUADRATIC_SHELL_ENDPOINT_PASS`.

**Limits:** FFT comparison is numerical, although field arithmetic, shell membership and multiplicities are exact. These tests do not prove the result at untested field orders and do not establish historical priority. The full mathematical proof is the independent algebraic argument in `RESULT.md`; an external independent audit has not been performed.
