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

# Verification of the local-run law

Execute `python3 verify.py` using the Python 3 standard library; the script is self-contained. Exact arithmetic checks compare the polynomial recurrence with an independent enumeration of all relative arrival-time orders on prescribed path-neighborhoods. Specifically, it verifies \(d=3\), local run lengths \(1,2,3\), and \(d=4\), local run lengths \(1,2\), with rational probabilities \(3/4\), \(31/90\), \(31/252\), \(4/5\), and \(1471/3360\). It checks probability monotonicity over eleven local-run thresholds for each degree from \(2\) to \(7\), compares finite factorial-tail ratios through \(k=30\) at degree three, and performs 100,000 seeded direct local-step simulations for degree three.

Observed result on the included source: `ALL CHECKS PASSED`. At degree three, the exact/asymptotic ratios at lengths \(10,20,30\) were respectively \(1.052870330732\), \(1.024613048221\) and \(1.015578872555\). For the simulated tails at lengths \(1\) through \(5\), all observed frequencies were within \(0.012\) of the exact probabilities.

Finite enumeration and simulation cannot verify the infinite asymptotic or almost-sure claim. Those are justified by the analytical change of variables, the normalized triangle-kernel endpoint concentration with \(O_d(k^{-1})\) error, and the summable upper/lower extremal probability estimates. Independent audit remains unperformed.
