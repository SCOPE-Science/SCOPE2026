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

The source `verify.py` exhaustively checks the finite local computations required by the proof. The recorded output is `verification_output.txt` and was reproduced by running `python3 verify.py` using the standard Python interpreter in a clean standalone directory.

The twenty-seven local anchored Euler weights are checked by explicitly enumerating every clique in all local boxes whose coordinate extents belong to \(\{0,1,2\}^3\). Six finite full complexes are independently enumerated as cross-checks. The oriented cycle is checked to consist of sixteen tetrahedra and to have zero signed boundary. Every signed coordinate permutation of the unit cube is verified to act by the coordinate-permutation sign. The distinguished even-parity tetrahedra are checked to have no further common neighbor in dimensions three through six.

The global wedge concentration comes from Gupta–Sarkar–Shukla, Theorem 4.13, arXiv:2511.04238v1, by a one-Lipschitz retraction. It is not proved by these finite tests alone. The unrestricted maximality statement and the integral homotopy conclusion are supported by the mathematical arguments in `RESULT.md`, rather than by an extrapolation from the enumerated cases.

All embedded artifacts are self-contained. Independent audit: not performed.
