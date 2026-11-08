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

The analytic verification is in `RESULT.md`: an exact label-conditioned reduction, a path recurrence, finite-cycle boundary cases, a power-series decomposition and positive beta-integral alternating sums. Each critical step has its normalization and range indicated there. The strict inequalities hold for every integer \(n\ge3\); asymptotics are as \(n	o\infty\) separately through odd and even integers.

`check_one_shot_cycle.py` runs using only Python's standard library. Its independent colour-enumerated vertex-subset dynamic program computes expected occupancy of every finite random conflict graph and compares it to the closed formula for \(3\le n\le10\). It then checks 29 additional finite cases using exact rational two-sided alternating Taylor enclosures for \(e^{-1}\), and checks 24 rational beta-kernel bounds; 61 grouped exact-rational assertions passed. The finite checks neither prove the all-size theorem nor constitute independent mathematical audit.

The checker was executed from its included standalone source file and returned a passing exit status. The analytic inequalities do not rely on any external numerical data or on an unverified simulation. Unproved extensions include biased A/B proposals, multiple attempts per site, finite-size fluctuations, and noncycle substrates.
