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

# Reproducibility and limits

Execute the standalone standard-library checker with `python CHECK.py`. The expected output begins `PASS:` and covers four assertions: a single feasible binary genealogy, its four local count vectors, the exact rational two-parameter alias (including every first-three-row logit), and the strict distinguishing capacity of the fourth sample. It also tests 49 rational members of the open ambiguity interval and a finite rational grid for the fourth identification ratio.

The universal two-to-one classification is proved symbolically in `RESULT.md` by factoring the equality of rational shape ratios; the checker is not an exhaustive validation over infinitely many real parameters. The Fisher-information rank condition follows from the displayed exact Jacobian determinant and strictly positive Bernoulli weights. The tree describes a possible finite genealogy, not a randomized population-level simulation. No external independent audit or validation has been performed.
