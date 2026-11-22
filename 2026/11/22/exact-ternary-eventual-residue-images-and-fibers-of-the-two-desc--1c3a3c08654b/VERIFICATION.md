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

# Finite reproducibility checks and proof limits

`check.py` uses Python 3 and only the standard library; run `python3 check.py` in a directory containing that file. It compares the integer closed form with the Eulerian recurrence for 90 initial indices, computes the \(3\)-adic logarithm and odd critical point by rational series and unique Hensel lifts, and checks all residue multiplicities and complete period values for moduli \(3^k\) with \(1\le k\le8\). The saved checker passed **29,634 exact assertions**.

The full distinct-residue counts at \(k=1,2,3,4,5,6,7,8\) were respectively \(3,7,20,58,173,517,1550,4648\); zero-fiber counts were \(3,5,5,11,11,29,29,83\). The checker verifies the defining branches, critical constants modulo each tested power, period histograms, and the closed-image counts. All calculations are exact integer modular arithmetic, not floating-point approximations.

The proof's all-depth inference uses analytic isometries, Hensel lifting, a nondegenerate critical-point coordinate and the exact period argument in `RESULT.md`. Running finitely many cases does not establish those theorems, does not certify historical originality, and does not substitute for independent validation. The closest published valuation-focused source's full text remains uninspected.
