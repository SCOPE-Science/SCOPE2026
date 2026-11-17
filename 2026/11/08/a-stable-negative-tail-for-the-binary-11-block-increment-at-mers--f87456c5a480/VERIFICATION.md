---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The eight-state (carry, previous input, previous output) transfer matrix T_b(z) weights each new pair increment qy−px. The zero-shift tail vector g accounts exactly for the infinitely continuing carry with geometric probability 2^{−h}; hence natural densities follow from dyadic cylinder frequencies plus vanishing tail. The inspected rational Laurent-polynomial verify.py constructs T_1, g and w=(T_1−I)g independently; its finite algebraic identities show (T_1^4−(z/2)T_1^3)w=0, G_4 numerator, and e0^T T_1^4 w=(z−1)^2(z+1)(2z²+z+2)/128. These imply the claimed exact G_{k+1}−G_k polynomial for every k≥4, stable negative coefficients, and sharp initial values by coefficient extraction. Independent counts of 2^19 consecutive inputs at k=4,5,6 give nondecrease 83/128, negative−1=45/256 and negative−2=45/512, matching the analytic coefficients; finite counts are not proof.

## originality

PASS

PASS best-of-knowledge with prominent overlap: published October 25 Resultary result already proves the exact nondecrease density 83/128 and sharp threshold k=4; that is NOT newly claimed independently. Its full primary text explicitly disclaims determination of the complete distribution. The additional stable coefficient formula for every negative j and exact polynomial generating-function recurrence are not entailed by the one scalar survival probability. General Sobolewski–Spiegelhofer recurrences could computationally yield the distribution, so the overlap remains a priority/implication risk but no explicit prior full-tail result was identified.

## value

PASS

The genuinely new portion is the *entire* geometrically decaying negative tail, which resolves an infinite collection of exact conditional probabilities with one sharp k cutoff, and structural Laurent transfer recurrence explaining its stability; these are motivated finer statistics of a natural binary block-counting difference beyond the already known scalar bias. The theorem also acknowledges that nondecrease=83/128 itself is previously established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
