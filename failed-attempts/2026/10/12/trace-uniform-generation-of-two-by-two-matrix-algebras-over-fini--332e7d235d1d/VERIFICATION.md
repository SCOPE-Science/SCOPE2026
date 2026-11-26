---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The only maximal proper unital F_q-subalgebras are the q+1 rational line stabilizers and the q(q−1)/2 conjugate quadratic fields. Indeed an irreducibly acting subalgebra acts faithfully on a simple module, so is simple, and the dimension-two module permits only the quadratic field or the full algebra. Quadratic fields are conjugate by identification of the natural space as the one-dimensional module over the field and their normalizer has size 2(q²−1). Distinct line stabilizers meet in a split diagonal algebra, at least three meet in scalars, and every field intersection with a different maximal subalgebra is also scalars. On full matrices, a line stabilizer, a split diagonal algebra, and a quadratic field the trace is surjective (on the field it is the separable field trace). Their prescribed-fiber sizes are q^(3m), q^(2m), q^m, q^m. Put b=q+1, e=q(q−1)/2 and let s count scalar tuples in the fiber: all scalar terms cancel with coefficient 1−b+binom(b,2)−e=0, regardless of s in characteristic two. This gives q^m(q^m−1)(q^m−q), zero exactly at m=1 in the stated domain. For the product, each surjective evaluation of the free unital algebra has a maximal two-sided kernel. Two evaluations have equal kernel precisely when an automorphism relates their tuples; distinct kernels are pairwise comaximal, so the Chinese remainder theorem gives surjectivity, while equal kernels force a graph relation. Distinct kernels, not abstract nonisomorphism of their quotient algebras, are the criterion in the proof. The PGL action is free, giving the stated falling-factor product and at m=2 the orbit count q^4(q−1). Independent exact checks at branches/a2e0ba22-fe4c-466a-9e5f-0c0f48d6d42e/ord1_independent_reproduction.py with repro_q2.txt and repro_q3.txt reproduced q=2,3 pair fibers (24 and 432 per trace) and 8640 generating pairs for q=2,k=2; these are bounded checks, not the universal proof.

## originality

FAIL

The trace-fiber law is not read off the unconditioned cardinality alone in characteristic two. The stronger decisive evidence is the explicit signed maximal-subalgebra set count in Kravchenko–Mazur–Petrenko (2012), §7A, which already supplies every contributing subset, its coefficient and the cancellation of the scalar contribution. Restrict that calculation to a trace fiber and use the elementary surjectivity of trace on each remaining subspace; this mechanically yields the entire result, even in characteristic two. Their Theorem 6.3 and equation (9) also already give the complete direct-power census and cutoff. This is verified implication, not a claim that the precise trace-conditioned formula is explicitly printed. No independently non-implied remainder survives.

## value

FAIL

Equidistribution under a prescribed trace is a natural statistic, but here it reduces exactly to slicing the complete previously known signed count by a surjective linear map on every surviving piece. The even-characteristic nuance is a useful clarification of that argument, not an additional difficult-to-obtain invariant under the implication standard. The other displayed results are already exact prior formulas, leaving no distinct worthwhile claim to retain by narrowing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
