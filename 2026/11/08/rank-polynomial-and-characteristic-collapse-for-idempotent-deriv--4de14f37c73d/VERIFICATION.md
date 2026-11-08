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
# Reproducibility

Run `python3 verify.py` using Python 3 and only its standard library. The script enumerates every small projection matrix over the prime fields of orders two, three, and five, constructs the induced action on the tensor-product center, and forms an independent linear system for all central shears. It computes the dimension of that solution space by elimination and computes the rank of the resulting block derivation. It then compares complete rank histograms with the proved Gaussian-binomial formula.

Successful execution prints four `RANK_HIST_OK` records and the exact final line `VERIFY_OK`. The tested triples \((a,b,q)\) are \((2,2,2)\), \((2,2,3)\), \((2,2,5)\), and \((2,3,2)\). These checks do not exhaust arbitrary fields or dimensions, cannot independently certify the general proof, and do not check priority in uninspected literature. The algebraic proof and asymptotic estimates are in `RESULT.md`.
