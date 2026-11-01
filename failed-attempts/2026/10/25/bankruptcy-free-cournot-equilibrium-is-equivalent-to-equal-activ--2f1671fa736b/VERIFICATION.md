---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

At an interior Cournot equilibrium each positive-output firm must have price strictly above marginal cost, since at equality decreasing its own output a little yields strictly positive profit, whereas at below-cost output zero dominates. For c_i<c_j, intermediate value and strictly decreasing continuous P permit i to raise output until c_i<P(Q′)<c_j; i remains solvent and j earns strictly negative operating profit. For equal c, a deviation that makes any other active firm insolvent makes the deviating positive-output firm insolvent too; zero output cannot lower the price. These arguments require no demand derivative, exactly match the stated assumptions, and extend to any n. Independently checked a three-firm linear-demand numerical illustration and own-profit/rival-profit signs. A caveat: P(Q)=12-Q as written in the illustration is not globally nonnegative on [0,infinity), although the local calculations and the theorem itself are valid; one may extend the local demand curve smoothly to a strictly positive decaying tail without changing the illustration near equilibrium.

## originality

FAIL

Decisive logical prior coverage: Beviá, Corchón, and Yasuda, 2011/2015 preprint of Oligopolistic Equilibrium and Financial Constraints, Section 2 Example 1 and the immediately following paragraph, proves for any number of firms and any continuous inverse demand that in the heterogeneous constant-average-cost case only the lowest-cost firm can be active in a bankruptcy-free allocation, while with identical constant costs every nonnegative-profit allocation is BF. The submitted all-interior Cournot iff theorem follows immediately, with constant marginal costs equal to constant average costs and positive equilibrium profits. Thus the original claim is a corollary of an earlier stronger BF-allocation classification, not a novel criterion.

## value

FAIL

Although economically interpretable, the entire equal-active-cost BF criterion is an immediate special case of the earlier general BF output-allocation analysis. The constant-cost no-bankruptcy direction is tautological once the common-price and equal-cost premises are written. Neither a new structural lemma nor a meaningful unknown boundary remains in the unchanged claim; a separate reformulation for n firms and example does not create substantive new mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
