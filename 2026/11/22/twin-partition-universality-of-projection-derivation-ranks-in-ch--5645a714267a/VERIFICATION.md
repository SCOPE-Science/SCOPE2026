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

# Reproducibility checks

Execute `python3 check_projection_derivations.py` using ordinary Python 3, without third-party modules. The checker verifies the complete finite-field rank polynomials by enumeration of all symmetric zero-sum matrices for the stated small dimensions; it separately constructs the original Leibniz constraint matrix for several graphs, including non-bipartite examples, enumerates all its solutions over \(\mathbb F_2\), and checks \(D^2=D\), ranks and predicted polynomial. It also checks the product identity directly on a natural basis for selected complete multipartite graphs. Its final line should be `UNIVERSAL_TWIN_CLASS_RANK_CENSUS_VERIFIED`.

`CHECKS.txt` records the output of executing this exact standalone code before packaging. Exhaustive small cases do not substitute for the full proof, which uses arbitrary-dimensional symplectic linear algebra. No independent audit has been performed.
