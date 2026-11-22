---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For strictly positive rank-one B=uw^T with identical strain dynamics, common recovery d, and the physical Euler step restriction, w^Tx^(r) is multiplied at each generation by the common positive factor 1-hd+h sum_i w_i u_i(1-z_i), preserving each weighted share. Subtraction of q_r times total equation cancels infection exactly and yields x_i^(r)-q_r z_i=(1-hd)^k initial discrepancy. For rho=w^Tu<d, scalar S decays geometrically; at rho=d, transverse profile errors are O(S^2), z_i/S->u_i/d and reciprocal S increments ->h sum_i w_i u_i^2/d, yielding k x_i^r ->q_r u_i/(h sum_i w_i u_i^2). For rho>d, monotone sub/supersolution iteration traps every nonzero total state at unique endemic z*. The all-interior initial-condition quantifier in the converse forces w^TM(z) proportional to w^T for every z, and varying z_i proves each row B_i proportional to w. Independently verified exact rational 2-node, 3-strain share identity for 16 generations, not a universal-time proof.

## originality

PASS

Best-of-knowledge originality after actual mathematical implication comparisons with primary literature and published Resultary corpus; no located stronger theorem implies the entire exact final claim. Distinct known antecedents and historical risks are documented.

## value

PASS

The initial weighted shares explicitly select a point of a known neutral coexistence continuum, the exact all-time nodewise exchange mode decays at (1-hd)^k, and the converse characterizes precisely which positive contact matrices conserve such a share for all initial states. These are motivated invariants and a structural rigidity theorem, not another existence-only neutral equilibrium result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
