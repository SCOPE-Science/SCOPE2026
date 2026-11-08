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

The analytic proof in RESULT.md establishes the complete small-radius law and the global angular stability inequality. The independent endpoint-pair simulations in the accompanying standard-library `verify.py` compare the predicted exact formula with 1,080,000 seeded random pairs over four strictly convex polygons. Analytic special-case identities are checked for the equilateral triangle and the square. An alternating-turn centrally symmetric family checks numerically that the stability quotient approaches \(1/6\).

Execute `python3 verify.py` using Python 3.8 or later. Expected terminal marker: `VERIFY_OK convex_polygons=4 random_pairs=1080000 analytic_special_cases=2 sharpness_sizes=4`.

Simulation tolerances are statistical; neither finite sampling nor finite numerical angle lists certify theorems for arbitrary convex polygons. The proof uses the exact Jacobian of the adjacent-edge parameter map and Euler's sine product. No external theorem prover or independent audit was performed. Historic priority is not independently certified.
