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

The proof follows admissible height histories for every horizontal column. The key signed weight is \(K_i(h,h')=\mathbf1_{h'\geq h-1}+(-1)^{\xi_i}\mathbf1_{h'\geq h}\); the initial factor is \(1+(-1)^{\xi_0}\). When this factor is positive, all later weights are nonnegative and a forced descending history has weight \(2\). If any later sign is positive, a distinct history with one flat step adds at least \(4\), giving the sharp and unique minimum. Full support of the counting measure gives the unique maximum.

Run `python3 verify_schroder.py` from the extracted package root. The code uses direct enumeration and an integer Walsh transform through \(n=8\), and a separate signed recurrence for every frequency through \(n=14\). It checks the large Schröder totals using a Catalan-binomial sum and prints assertion counts. Finite checks corroborate but do not certify the all-order argument. The kernel is a counting measure: replacing it with a zero-one support indicator is outside the claim.
