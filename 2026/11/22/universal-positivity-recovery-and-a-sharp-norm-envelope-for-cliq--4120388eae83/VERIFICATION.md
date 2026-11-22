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
# Reproduction and checks

Run `python3 verify.py` with Python 3, NumPy and SciPy. Exact rational projector resolutions are checked separately from the numerical diagonalization. The complete graph Laplacians are built from edges and degree counts rather than by using the theorem's projector formulas. The checker covers all ordered base-clique compositions through ten vertices, seven increasing spectral generators, and five positive times per graph-generator combination. It tests full matrix entries, induced row norms, sharp sign transitions and the topology envelope. It also verifies orthogonal projector algebra using exact rational arithmetic on all ordered partitions of eight leaves.

Observed output:

`VERIFY_OK exact_projector_checks= 956 matrix_and_norm_tests= 17570 sign_phase_tests= 3514 peak_bound_tests= 1506`

The diagnostic checks are finite and include floating-point tolerances. They do not certify the universal quantifiers, arbitrary generator functions, uniqueness of scalar roots, or global literature originality. Those mathematical statements are supported by the analytic proof in `RESULT.md`; historical priority remains subject to further specialist comparison.
