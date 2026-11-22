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

The supplied `verify.py` performs exact rational Gauss-Jordan inversion and matrix multiplication, comparing direct numerical transitions with independently obtained spectral expressions for seven star sizes, seven rational step sizes and nine powers. Its output is `VERIFY_OK 33958`; all asserts succeed. It also verifies an exact negative off-diagonal of the squared Crank–Nicolson update on a four-vertex path at step 30. This finite checker does not establish the general theorem; projector algebra, the scalar monotonicity argument and the unique crossing prove the unrestricted integer and real-parameter claims. No external independent validation has been performed.
