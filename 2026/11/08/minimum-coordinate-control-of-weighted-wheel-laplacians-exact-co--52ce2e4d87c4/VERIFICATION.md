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

# Finite computational verification

Run \(`python verify.py`\) with a standard Python interpreter. It uses only the Python standard library and returns an assertion error if its predicted finite cases differ from modular Kalman controllability ranks.

The performed run covered rim sizes \(3\) through \(14\), \(75\) rational spoke-weight instances, \(3548\) independent two-input tests and \(1146\) triple-input tests at a selection of resonances, with zero predicted-versus-observed disagreements. It also checked totient-count formulas for \(68\) rim sizes. Specific counts printed were \(2113\) controllable and \(1435\) uncontrollable tested pairs, and \(526\) controllable and \(620\) uncontrollable tested triples.

The Laplacian is multiplied by the denominator of the spoke weight before reduction modulo \(1000003\). Thus the arithmetic tests operate on integer matrices; floating trigonometry occurs only in selecting and labeling rational test resonances, not in the rank calculations. A modular full rank implies rational full rank; modular rank loss alone does not imply rational rank loss. The general theorem, including irrational weights and all untested graph sizes, is proved by Fourier decomposition, PBH restriction, and exact modular-congruence arguments in \(`RESULT.md`\). No independent external verification is asserted.
