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

The proof in `RESULT.md` establishes every length \(n\ge3\) by inclusion–exclusion, character orthogonality, a three-point roots-of-unity filter and direct Fourier inversion. The checker `verify_ternary_surjections.py` uses exact integer-coordinate arithmetic on \(\mathbb Z[\omega]\), where \(\omega^2=-1-\omega\).

**Executed check:** `python3 verify_ternary_surjections.py`

**Observed output:** `PASS: 3267 exact character coefficients; ranks, spectral minima, multiplicities and all-length identities tested.`

The exhaustive character comparisons cover \(3\le n\le7\) only. Binomial-identity checks through \(n=49\) are finite checks. Neither provides a substitute for the all-parameter proof. No formal proof assistant or independent external review is claimed.
