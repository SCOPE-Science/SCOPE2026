---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For f=1 on first dyadic half and zero on second, u=f(k_i)f(k_j) belongs to sparse space for N>=2. Decomposing transverse factor f=(1+s)/2 gives P_N D_i u = (D_N f)/2 + (P_{V_{N-1}}D_N f)s/2; at k_i=k_j=m/2+1 the input is zero, D_Nf=0 but adjacent-pair average of negative jump equals -1/2, so projected derivative is +1/4. Thus u-r_i P_ND_iu-r_jP_ND_ju is -(r_i+r_j)/4<0 for every positive step with any nonzero transport speed, independently of dimension or level. A small constant offset gives strictly positive initial state. At N=1 the sparse cone a>=sum|b_j| is invariant exactly for every 0<=r_j<=1; d=1 reduces to full upwind. Independently recomputed dyadic tensor projection at d=2,N=2 with derivative values 1/4 each, and inspected exact verify.py. Edge cases N=0 and zero speeds correctly yield identity.

## originality

PASS

Huang 2026 proves sharp L2 contractivity of the same sparse method, not in its accessible abstract an order-positivity theorem. Guo–Cheng scheme background and alternative positivity-limited DG are not logical implications of this all-level negative barrier. Actual semantic searches revealed no identical published theorem. Full-text access to most relevant Huang paper blocked, retained priority risk.

## value

PASS

Distinguishing L2 stability from positivity is mathematically important for transport discretizations. The explicit universal failure for every d>=2,N>=2, paired with a sharp N=1 and one-dimensional boundary, is a motivated complete structural classification affecting the need for positivity limiting. The all-level theorem is not a sample counterexample or a mere routine use of CFL conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
