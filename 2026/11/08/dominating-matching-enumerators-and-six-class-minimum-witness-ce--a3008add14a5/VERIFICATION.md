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

# Verification details

Run \(\texttt{python3 verify.py}\) with a standard Python 3 interpreter. No external dependency or network is needed.

The program enumerates the ten local matching symbols, all 34 permitted ordered pairs and 101 legal domination transitions, reconstructs a nonnegative exact integer potential and verifies the 44/24/29/4 cost profile, and decomposes the zero-cost graph into exactly two directed cycles (lengths three and six) and 25 acyclic singleton components. It checks exact defect-coefficient traces through length 103, first against independent rational-denominator recurrences and then against the residue-class closed formulas. The adjugate numerator-degree bound in RESULT.md proves that these finitely many equalities force the claimed rational generating functions at all orders.

A separate implementation enumerates matching edge subsets of the actual two-layer graph and checks ordinary vertex domination for every \(3\le n\le12\) at the provably minimum matching size, and it compares the entire polynomial against independent graph-level enumeration for \(3\le n\le6\). It separately tests domination by an every-third-rung construction for every \(3\le n\le120\). These brute-force cases corroborate, but do not themselves establish, the infinite result.

Expected completion marker: \(\texttt{VERIFY\_OK}\). The formal transfer at lengths one and two is only a device for obtaining series coefficients, not a claim about simple cycle-prism graphs of those orders. The work has not received independent mathematical validation.
