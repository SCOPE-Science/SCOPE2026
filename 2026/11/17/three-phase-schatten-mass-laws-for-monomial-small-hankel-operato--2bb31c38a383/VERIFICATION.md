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

This is an analytical statement about a concrete, degree-dependent family of finite-rank operators. For \(\gamma>1\) and \(a>-1\), one checks the squared norm of \(z^j\) in the source and target by evaluating the beta integral
\[
2(j+1)^2\int_0^1r^{2j+1}(1-r)^\gamma\,dr=2(j+1)^2 B(2j+2,\gamma+1).
\]
The kernel coefficient of \(w^j\overline{z}^{\,j}\) is \(\Gamma(j+a+2)/(\Gamma(a+2)\Gamma(j+1))\); the normalized moment of \(|w|^{2m}\) under \(\nu_a\) is its reciprocal at degree \(m\). These identities produce the anti-diagonal singular weights without any numerical fitting. The gamma-ratio bounds and the three summation arguments appear in RESULT.md.

`check.py` requires Python 3 and SciPy; run `python check.py` in a directory containing the unpacked artifacts. The checker evaluates 124 finite diagnostics: beta-moment identities, finite anti-diagonal weights, and illustrative convergence to bulk, critical, and edge asymptotics. It prints `SMALL_HANKEL_FINITE_DIAGNOSTICS_OK 124` on success. The integer factorial tests and sample comparisons are auxiliary: only the proof establishes all exponents, degrees, and boundary regimes.

The theorem does not require Lean or external certificates. An independent mathematical or historical-priority assessment has not been performed. The inaccessible full Janson paper remains a specific unresolved priority risk.
