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

The finite conditional distribution and all parameters are defined and proved in `RESULT.md`. A direct mapping enumeration in `check_mapping.py` verifies 464 exact assertions through seven vertices, including independent evaluation of both statistics and their conditional binomial moments. The proof of the infinite assertions is analytic: deletion identity, conditional occupancy representation, strict monotonicity and a uniform conditional coupling with classical occupancy statistics. The Gaussian marginal invokes a published classical occupancy central limit theorem, and no finite enumeration is used as a substitute for the limiting proof. This is not an independent audit.
