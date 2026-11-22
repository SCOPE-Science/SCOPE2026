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

# Reproducible checks and scope

The included `verify_two_token.py` directly enumerates unordered occupied-vertex pairs and allowed single-token moves. It builds adjacency without using the proof's incidence reduction, then checks exact integer characteristic polynomials for six parameter pairs. For each it evaluates the full unitary matrix exponential at four positive times and compares the same-shore probability with the analytic formula. For all three balanced test pairs it independently constructs and exponentiates the classical continuous-time exclusion generator at three times. All assertions passed for the actual included script, with a numerical comparison tolerance of \(2\times10^{-11}\) on time evolution. Sample sizes are finite and are not asserted to verify the theorem for all \(m,n\).

The proof supplies the all-size identity by an exact four-sector singular-value decomposition. The sharpness and nonattainment are mathematical, using irrationality of \(2\sqrt{(r-1)/(r-2)}\) for every integer \(r\ge3\) and density of the irrational torus flow. The classical limit follows from an explicit two-state rate generator and a limiting exponential. Exact eigenvalue identities are tested symbolically; numerical propagator checks use floating point. No independent validation, formal proof certification or experimental quantum implementation is claimed.

To reproduce with Python 3, NumPy, SciPy and SymPy installed, execute `python verify_two_token.py` from the directory containing the extracted code.
