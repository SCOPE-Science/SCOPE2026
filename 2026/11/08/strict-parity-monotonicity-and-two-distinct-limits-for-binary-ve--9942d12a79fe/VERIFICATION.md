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

# Reproduction and verification

Run `python3 verify.py` with Python 3 and no external dependencies. The script enumerates all dual characters of \(\operatorname{Sym}_m(\mathbb F_q)\) at seven parameter pairs: \((q,m)=(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(8,2)\). For every character it directly computes the quadratic character sum by enumerating all \(v\in\mathbb F_q^m\). It verifies the predicted values (zero or \(q^{m-j}\)), the exact number \(q^{2j}\) of nonzero diagonal character choices for every alternating matrix rank, and the full sharp endpoint norm.

The exact-rational second phase generates parity-conditioned nullity birth–death distributions for \(q=2,4,8\) through matrix dimension \(29\), comparing every expectation with the separately evaluated alternating-rank formula and checking strict decrease after every two-dimensional augmentation. It prints `BINARY_VERONESE_FOURIER_CHECKS_PASS` and `BINARY_VERONESE_MARKOV_CHECKS_PASS` only on success.

Observed exact values include \(L_2(2)=3/2\), \(L_3(2)=15/8\), \(L_4(2)=183/64\), \(L_5(2)=3783/1024\), \(L_2(4)=13/4\), \(L_3(4)=253/64\), and \(L_2(8)=57/8\). Approximate parity limits are \(0.7043688567618808\) and \(0.9190785712529057\) for \(q=2\); \(0.8030852218326849\) and \(0.9875120626833671\) for \(q=4\).

The enumerations and finite Markov iteration are corroborative; the all-parameter argument is provided in the proof. No independent mathematical audit has been performed.
