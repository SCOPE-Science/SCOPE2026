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

# Reproduction and scope

Run `python check_lebedev14.py` with NumPy and SymPy. The script contains its complete fourteen-node coordinate/weight data and uses no downloads or hidden assets. It constructs the nine real orthonormal spherical harmonics explicitly, checks the Parseval identity, enumerates all 2002 retained nine-sets, finds the six exact stated optimizing masks, and records 1456 nonsingular and 546 singular choices. Exact rational/algebraic SymPy computations separately verify normalized monomial moments through degree four, the kernel projector identity, the special five-node Gram characteristic polynomial, and the critical positive-definiteness obstruction determinant. This check was executed successfully from the packaged checker source.

The theorem's all-mask optimum is established by the finite combinatorial forbidden-pair proof in `RESULT.md`; numerical eigenvalues merely corroborate it. The result does not assert that noise-weighting changes preserve the bound or that no earlier literature contains an equivalent optimization. The self-review is recorded in `REVIEW.md`; no independent audit is claimed.
