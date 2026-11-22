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

The analytic proof reduces every candidate partition to within-class cyclic energies. The strict convexity of the squared screened-cycle Green kernel makes cyclic equispacing a necessary and sufficient classwise equality condition; strict convexity of the explicit class energy as a continuous function of class size forces all class sizes equal. The unique combination of both equality conditions identifies residue classes modulo the probe count. All steps are valid for integers \(k\ge3\), \(m\ge2\), and every finite \(\mu>0\).

Run `python3 check_cycle_probing.py` to independently calculate exact rational resolvents and check the quadratic-form variance identity on six sites. The same program exhausts eight finite instance partitions and reports 1,358,283 exact comparisons; its finite experiments are corroboration rather than proof of the all-parameter theorem.

Coverage limitations: no nondivisible orders, nonuniform edge weights, correlated probes, or formal zero/infinite screening endpoints. A human independent mathematical audit has not been performed.
