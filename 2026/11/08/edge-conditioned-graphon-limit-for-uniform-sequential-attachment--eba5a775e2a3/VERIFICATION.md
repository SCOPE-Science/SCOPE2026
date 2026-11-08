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

Run `python verify.py` with a standard Python 3 installation. The verifier independently enumerates small outdegree sequences, checks integer convolution coefficients of the edge-count generating polynomial, tests complement symmetry and exact moments, verifies constancy of the exponential likelihood ratio on exact-count fibres, evaluates the symmetry and derivative identities of the continuous cumulant function, and checks the binomial priority-coupling bounds using exact rational arithmetic. Its final PASS count is printed by the executable.

The analytical proof is contained in `RESULT.md`, including the smoothing argument behind the tilted lattice local limit, the conditioning transfer from exponential concentration, and the independent-edge coupling. Computational checks do not prove asymptotic graphon convergence or historical originality. No independent scientific audit has been performed.
