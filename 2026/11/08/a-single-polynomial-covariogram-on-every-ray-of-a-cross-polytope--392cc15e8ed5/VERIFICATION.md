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

The standalone `verification/verify.py` was executed with `--hull` from the extracted new research package and returned `CROSSPOLYTOPE_RADIAL_POLYNOMIAL_OK 216`. It compares two different exact implementations, a pre-cancellation geometric partition integral and the single-polynomial expression, over all listed rational parameters and verifies origin and support endpoints. Optional Qhull computations use floating-point volumes to check the same formula independently in dimensions two through four.

The finite tests support but cannot certify arbitrary real directions or all dimensions; the proof in `RESULT.md` establishes the universal identity. The endpoint derivative was separately cross-checked against the inclusion–exclusion box-density formula on sample positive rational directions. Historical priority and an independent mathematical audit remain unperformed.
