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

# Verification notes

The theorem is established analytically by the exact \(U(2)\times U(2)\) spectral decomposition, the uniform cubic cutoff bound, a convergent beta-series identity, and a harmonic-sum asymptotic. The reproducible standalone script `verify_count.py` uses rational arithmetic to count all eigenvalues strictly above a rational threshold, including their exact squared K-type multiplicities; at small thresholds it also compares against an independent naive enumeration.

Executed command: `python3 verify_count.py`. Output: `PASS 24 exact counting diagnostics`. Tested \(\gamma\in\{1/2,1,2\}\), with small-threshold direct comparisons and five finer scales per weight. For the illustrative case \(\gamma=1\), the analytically predicted leading and logarithmic coefficients were \(12\) and \(144^{2/3}/6\), respectively. The scaled remainders remained consistent with the proved \(O(\tau^{-2/3})\) allowance; no uniform numerical bound was inferred from these examples.

The program does not test the validity of the Faraut–Korányi spectral decomposition independently of the underlying published functional-analytic result. That decomposition is cited and its normalization and matrix-ball multiplicities are explicitly reconstructed in the proof. Neither finite tests nor the mathematical derivation constitute an independent external audit. The second-term conclusion is not claimed uniformly as \(\gamma\downarrow0\).
