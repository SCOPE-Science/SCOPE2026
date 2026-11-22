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
# Reproducibility of the finite checks

Run `python3 verify.py` with Python 3's standard library. The program independently implements admissible one-point order states and then compares them to a second implementation using the exhaustive three-family division. The actual recorded output is in `verification_output.txt`.

The script checks 682 parameter bipartite comparison graphs with side sizes at most three; 46 balanced and rectangular deleted-matching instances with sides at most four; 14 rational-weight exact expected values from complete finite probability-space summation; and complete and fully matching-deleted endpoint formulas with side sizes one through five. All tests reached `VERIFY_OK`.

The finite checks do not prove the limit distribution or independent-omission universality. Those results use the deterministic matching formula, a Poisson limit for rare independent Bernoulli variables, an overlapping-edge union bound, a uniform normalized type-count bound, and exponential estimates on the three type families. Full details, hypotheses, and limits are in `RESULT.md`.
