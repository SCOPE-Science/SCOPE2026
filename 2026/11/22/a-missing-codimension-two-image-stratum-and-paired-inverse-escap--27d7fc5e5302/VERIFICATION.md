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

# Reproducibility and verification

The theorem follows by an exhaustive elementary inverse case analysis. The companion `check.py` runs exact symbolic checks of the Jacobian and inverse identities, along with representative exact input/output case tests. The missing-image locus follows from the simultaneous equations \(m_+=m_-=0\), not from finite testing. Both singular inverse branches have the verified exact residue \(\lim_{W\to0}Wz_\sigma=-Y/(2b)\) for targets with \(X=2a\) and fixed nonzero \(Y\).

Reproduce in the directory containing the two files using `python check.py` (requires SymPy). The checks do not constitute independent mathematical certification. No numerical finite test is used as a substitute for the all-parameter proof. The analysis does not cover typical forward-time dynamics or arbitrary approach paths to the omitted stratum.
