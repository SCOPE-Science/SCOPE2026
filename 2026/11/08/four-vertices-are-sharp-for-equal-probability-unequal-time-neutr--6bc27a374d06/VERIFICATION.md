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

The standalone `verify_moran_multiseed.py` checker requires only Python 3. It lists every connected simple labeled graph on two, three, and four vertices and computes conditional fixation times by exact fraction Gaussian elimination in a finite absorbing chain. Expected group differences are absent for all order-two and order-three cases. Order four has 38 connected labeled graphs in six classes, of which 15 labeled graphs in exactly the path and cycle classes have divergent conditional time at fixed mutant count and fixation probability.

The inverse-degree fixation formula is verified against every transient harmonic equation. For both witness graph classes a separate conditional Doob-transform calculation yields the same rational conditional first moments as the weighted first-moment method. The cycle witness gives conditional times 8 and 7; the path witness gives 20 and 15; both initial configuration pairs have fixation probability 1/2. The checker uses no floating point and no sampling.

General graphs above four vertices, positive selection different from fitness one, alternative update rules, and independent historical priority are not covered.
