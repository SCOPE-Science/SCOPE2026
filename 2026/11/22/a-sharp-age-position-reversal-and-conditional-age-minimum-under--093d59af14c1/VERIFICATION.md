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
The source `checks/age_position_check.py` was executed from the packaged path using Python with SymPy and SciPy installed. It verified all five differential-generator identities and the covariance formulas symbolically. Killed-kernel quadrature agreed with mean position and \(\mathbb E[AX]\) at four positive triples \((L,v,D)=(1,1,1),(2,1,0.5),(5,2,0.7),(1.2,2,1.7)\). Five separate killed-kernel time integrals at \(L=v=D=1\) and positions \(x=0.1,0.5,1,2,4\) matched the conditional-age formula. Each numerical comparison used absolute tolerance \(2\cdot10^{-6}\) or tighter. These are reproducibility checks, not a substitute for the all-parameter analytic argument.

Reproduction: install dependencies listed in `checks/requirements.txt` and execute `python checks/age_position_check.py` from the directory holding these files. The source must accompany the result; no other file or external data are required.

The Green representation and renewal occupation identity are standard and credited in `RESULT.md`. The proof explicitly separates newly stated inequalities and covariance classifications from those premises. Independent audit has not been performed.
