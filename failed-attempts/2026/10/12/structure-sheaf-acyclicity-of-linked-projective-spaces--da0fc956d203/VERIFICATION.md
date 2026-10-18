---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The cited 2026 primary paper establishes the exact SNC Mayer–Vietoris resolution for O_X (Proposition 2.4), X simple normal crossings (Theorem 3.3), and each nonempty stratum X_Δ as image of a rational map from a projective space (Proposition 4.1); smooth projective irreducible strata are therefore unirational, so H^q(X_Δ,O)=0 for q>0 in characteristic zero via resolution, pullback of differential forms and Hodge symmetry. The resulting hypercohomology is the simplicial cohomology of the dual complex. Theorem 4.4 proof explicitly proves every K_a with |a|<=r contractible by convex cover nerve, and K_0 equals the dual complex because 0 belongs to every independence polytope. This yields H^0=C and H^i=0 for i>0 under the claimed hypotheses, but it is already implied by the source.

## originality

FAIL

Decisive claim-versus-prior implication overlooked by the source self-review: in De León–Esteves–Vital arXiv:2609.37634v2 Theorem 4.4 proof (pp15–16), the contractibility of the entire family K_a for |a|<=r is proved explicitly. Its a=0 instance IS the submitted dual-complex contractibility. The same paper Proposition 2.4 provides the full exact structure-sheaf Mayer–Vietoris resolution; Theorem 3.3 smooth SNC strata and Proposition 4.1 projective-space rational image plus standard characteristic-zero Hodge vanishing imply all H^i(O). The precise cohomology formula need not appear verbatim to be covered by a direct standard corollary. No genuinely new independent theorem remains in the assessed two-part result.

## value

FAIL

The cohomological interpretation is natural and may be useful expository context, but the asserted dual-complex topology is exactly proved in the motivating primary article and the higher O-cohomology computation is a routine SNC Čech/Hodge deduction from its stated lemmas. As a proposed independent research finding, it does not fill a remaining mathematical gap or supply a novel structural invariant, boundary or computation; correctness and a useful restatement are insufficient for independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
