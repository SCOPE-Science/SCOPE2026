---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The restriction of the seventh-power sum to the linear hyperplane is not identically zero (use coordinates 1,1,−2,0,…). The projective Jacobian condition gives common nonzero sixth powers, hence precisely the zero-sum sixth-root tuples modulo free simultaneous scaling. In the chart x_N=1, the Hessian is 42 times the diagonal with entries x_i^5 plus the rank-one term with coefficient x_{N−1}^5. Its rank-one determinant multiplier is 1+x_{N−1}^5∑_{i≤N−2}x_i=−1/x_{N−1}. This proves nondegeneracy and, by the local Jacobian ideal, reducedness. Every intersection of distinct components would have dimension at least N−4≥1, contradicting isolated singularities; repeated factors also contradict isolated singularities. S_2 and R_1 give normality. The triangular-lattice constant term follows by using the primitive sixth root basis and inverting one Laurent variable; (S+2)^k has the order-three Franel constant term. Normalization makes the field of every point a subfield of Q(√−3); rational points are exactly balanced signs and the remaining Galois orbits have length two. Independent walk DP and the finite binomial sum agreed through N=12, with explicit walk enumeration through N=7 and independent sign checks through N=8. Counts for N=5,…,10 and the two small residue-field decompositions agree.

## originality

FAIL

Two affirmative comparisons exhaust the frozen finding. A distinct co-dated Resultary theorem specializes at p=3 to the identical septic variety and covers the geometry, exact count, and even the full scheme-theoretic splitting. OEIS A002898 already states precisely the Franel transform of the triangular lattice closed-walk count as well as the exponential generating function underlying the general theorem's count at p=3. There is no distinct residual counting theorem. This is statement-level coverage, not a determination of priority between same-day records.

## value

FAIL

The geometry and residue fields of these symmetric sections are meaningful invariants in themselves. As a standalone contribution, however, this record only recombines a covered specialization of the entire nodal scheme with an already explicit expression for the same walk sequence. Neither a new sharp invariant nor a new mathematical consequence beyond that coverage is exhibited. The elementary constant-term proof can still be useful exposition; it does not supply an audit-worthy new scientific remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
