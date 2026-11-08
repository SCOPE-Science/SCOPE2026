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

# Reproducibility and limits

Run `python3 artifacts/verify.py` from the directory containing this file. The script uses only Python's standard library and reports 3061 passing numerical/symbolic-identity diagnostic assertions with the values \(x_c\approx1.16556118520723\), \(\sin^2(x_c)/x_c\approx0.724611353776709\), and \(x_c/\sin^2(x_c)\approx1.38005013968930\).

The script checks several exact structural identities (unitary transition amplitude, failure probability and one-step renewal formula) against independent direct calculations, and tests the explicit envelope and maximizing laws at sampled points. The assertion count includes finite sampled inequalities; it is not a machine proof of the global optimization. The global statement instead follows from the analytic proof of a concave majorant on the whole half-line, Jensen's inequality and its equality conditions, as detailed in RESULT.md. Infinite-support waiting distributions are covered by that argument and not by finite sampling.

The first small-mean phase is an unattained infimum when \(\tau>0\) almost surely. Its two-atom boundary law uses a zero-length interval only as a mathematical closure. No randomized laboratory protocol, finite-sample parameter-estimation claim, performance certification or independent scientific audit is supplied.
