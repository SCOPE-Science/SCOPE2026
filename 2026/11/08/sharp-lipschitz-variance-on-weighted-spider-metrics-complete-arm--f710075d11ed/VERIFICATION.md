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

# Exact arithmetic verification

Run `python3 check_spider.py` using a standard Python 3 interpreter. The program enumerates every saturated edge-sign potential for each tested metric, computes exact unnormalized numerator \(W^2\operatorname{Var}_\mu f\), verifies the signed first-moment formula, and checks the predicted arm-sign rigidity for all maximizers. Edge lengths and positive vertex mass inputs in the finite experiments are integers; normalization gives rational probabilities.

Observed output from execution of the bundled checker:

```
ARBITRARY_POSITIVE_INTEGER_EDGE_LENGTHS_AND_VERTEX_MASSES_OK 180 368
EQUAL_ARM_PARITY_FORMULA_AND_ALL_MAXIMIZERS_OK 16
STAR_PARTITION_THRESHOLD_EXACT_OK 4
ALL_WEIGHTED_SPIDER_VARIANCE_CHECKS_OK
```

There were 180 seeded heterogeneous instances (arm counts 2–5 and up to 11 edges), 16 equal-arm enumerations, and four explicit integer PARTITION inputs. These checks are exact on the sampled domains but do not establish a universal formula, numerical independence, or exhaustive coverage of real weights. The proof's universal steps are the strictly convex edge-coordinate argument and the positive-pair-coupling arm argument in RESULT.md. No third-party validation was performed.
