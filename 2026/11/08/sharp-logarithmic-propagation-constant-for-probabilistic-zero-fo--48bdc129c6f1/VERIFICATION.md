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

## Reproduction

Run `python check_friendship.py` with Python 3.10+ and no external packages. The program prints finite exact means and the total number of exact rational assertions. It separately computes the quotient-state and full-coloring-state transition kernels, verifies their distributions for \(m=1,2,3\) through seven rounds, verifies exact drift identities and normalization for all quotient states through \(m=5\), and evaluates finite expectations through \(m=6\).

The checker tests finite consequences of the theorem and the derived kernel. It is not a certificate for the limiting theorem; that rests on the explicit Chernoff, Perron-growth and white-vertex extinction estimates in `RESULT.md`. The star-based uniform moment bound comes from Geneson and Hogben, Lemma 2.3, plus a stated monotone coupling. No independent audit was performed.
