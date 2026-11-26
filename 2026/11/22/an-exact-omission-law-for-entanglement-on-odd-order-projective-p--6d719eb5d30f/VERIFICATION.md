---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the computation in RESULT.md lines 31–53. In graph-state basis amplitudes, tracing the line register gives cancellation unless B_fault transposed annihilates the difference of the two point labels; the reduced density then has identical rank-one blocks indexed by the corresponding cosets, giving rank 2^rank(B_fault) and flat nonzero eigenvalues. Odd q gives BB^T=I+J and B1=B^T1=0 in F₂, with n odd, so B has corank one. For the matching update, z=V^Tx forces even parity by the left kernel. Every preimage of Uz is B^TUz+c1; asking it to have V^Tx=z gives exactly the bordered equations. The maps in both directions are inverse, including k=0. When D=0 and k≥1 the border imposes c=0 and one parity constraint, so the loss relative to pristine is k−2. With two flags one cross-incidence instead gives determinant 1 for K_F, while two cross-incidences violate uniqueness of the common line. For Desarguesian odd q the stated finite point/tangent dot product is (s−t)^2 and neither type of finite/infinite cross-incidence occurs; this works over all the specified fields. Read VERIFY.py, VERIFICATION.md and the supplied finite check output without executing the script. Those prime-order tests are not the basis for the general result.

## originality

PASS

On available evidence, the distinct result is the exact odd-plane cross-incidence criterion for every matching, with the sign reversal under repeated induced omissions and its conic realization. The GF(2) entropy law, low-rank compression technique, ordinary projective-plane incidence identities, and conic tangents are not novel ingredients.

## value

PASS

Ideal missing gates are a natural graph-state perturbation. The same parity law handles arbitrary matching sizes rather than a sampled small case, and separates first-omission gains from cumulative losses based on the geometry of the missing flags. The q+1 tangent realization makes the reversal an unbounded family rather than a tiny rank check. This is mathematical value for the specified pure-state cut only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
