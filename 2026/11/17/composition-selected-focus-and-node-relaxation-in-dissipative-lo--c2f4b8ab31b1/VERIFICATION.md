---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS. Exact invariants log(v_i)/c_i-log(v_j)/c_j give v_j(t)=v_j(0)e^{c_jY(t)}. The scalar equation Σ b_jv_j(0)e^{c_ja}=Σb_jp_j has a unique root a, selecting one positive equilibrium on each conserved leaf. The convex relative-entropy L=Phi(u;U)+Σ(b_j/c_j)Phi(v_j;p_j) has derivative -d(u-U)²; compact strictly positive sublevels and LaSalle imply every strictly positive trajectory converges to that selected point. On the leaf the exact planar linearization is [[0,1],[-UB,-Ud]], B=Σb_jc_jv_j*: node/focus discriminant and strict coexistence precisely c_min<Ud²/(4S)<c_max follow from positive weighted means. For a focus, angular frequency ω=sqrt(UB-(Ud)^2/4) with polar angular drift ω+O(r), yielding central-level crossings ω/pi; stable real distinct nodes have eventual fixed-sign transverse velocity, hence finite crossings. Checked explicit m=2 example: S=2, B=2+8w, boundary w=7/8, invariant R*=7*8^8/9^9, crossing rate sqrt(8w-7)/pi. Read pinned check_star.py symbolic identities and its finite IVP tests, but the infinite claims rely on Lyapunov and local dynamical arguments, not numerics.

## originality

PASS

Best-of-knowledge PASS for the complete composition-selected strict focus/node basin criterion and exact central-level crossing clock in a fixed-coefficient LV star. The conservation and LaSalle methods themselves are classical and not credited as original. The source graph classification and older convergence theory do not state the specific quantitative two-dimensional leaf spectral partition, but older potentially relevant full text is inaccessible.

## value

PASS

PASS. The natural dissipative star has a continuum of equilibria whose individual dynamics are selected by conserved compositions. A sharp iff criterion for coexistence of two distinct spectral relaxation types for the same fixed model coefficients, together with a computable basin divider and asymptotic oscillation clock, is a useful structural result even though its constituent linearization and LaSalle methods are standard. It is more than a generic stability exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
