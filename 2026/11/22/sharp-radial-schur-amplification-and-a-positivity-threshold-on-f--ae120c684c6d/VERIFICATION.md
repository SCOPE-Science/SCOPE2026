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

The universal formula is derived in `RESULT.md` using positive semidefinite Schur symbol decompositions and a matching finite trace-norm witness. The finite upper bound reduces to two exact determinant identities; the lower bound uses an exact discriminant and trace-norm calculation. The infinite-star proof explicitly realizes positive kernels as normal diagonal-multiplier Schur maps, and takes lower bounds through finite principal corners.

Run `python checks/weighted_star_check.py` with Python's standard library. This returned `WEIGHTED_STAR_EXACT_IDENTITIES_OK 10559` on 2,560 prescribed rational cases, 7,000 reproducible pseudorandom rational cases, and 999 positive rational infinite-parameter checks. These experiments are supplementary and do not prove the continuous-parameter theorem.

The real-parameter restriction is essential to the stated proof. The known unweighted \(T=1\) special case is not new. Neither publication priority nor the mathematical result has undergone independent validation.
