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

# Verification of the elapsed-time theorem

The proof uses the exact initial-conflict graph, independent Exp(1) first-activation times, and the monotonicity of bichromatic edges under the declared free-color recoloring rule. The event of unfinished stabilization is the event of at least one edge with both endpoints unactivated, so its complement is the independent-set event in vertex Bernoulli retention at \(q=e^{-t}\).

The Stein–Chen theorem is applied to indicators indexed by edges, using overlapping endpoint sets as dependency neighborhoods. Every overlapping pair of *distinct* edges shares three vertices (in a simple graph), which gives the stated \(q^3\) term. There are exactly \(\sum_v d_v(d_v-1)\) ordered pairs of distinct overlapping edges. This theorem's conservative total-variation bound is valid regardless of whether its numerical value exceeds one.

`checker.py` runs with the Python standard library and passed 632,891 assertions. It exhaustively verifies pathwise scheduler equivalence on all labeled graphs of order at most four over 3-color starts and all first-clock orderings, compares independence-set probability sums at rational retention rates on every graph through order five, verifies overlap counts, and tests exact star/clique distributions. Finite enumeration and rational calculations are not infinite-size certification.

The full referenced motivating preprint was inspected at its model, reduction, clock interpretation, general results, special families and appendix context. The Arratia–Goldstein–Gordon 1989 Theorem 1 and its definitions of the three error sums were also checked in a lawful open author-hosted copy. The proof relies on that published Stein–Chen theorem; its proof is not rederived here. Additional literature or independent expert review may affect novelty but not the stated computations. No independent assessment was performed.
