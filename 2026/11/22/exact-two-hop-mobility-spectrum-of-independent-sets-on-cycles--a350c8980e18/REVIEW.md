# Self-review

## Correctness — PASS

The domain is indexed independent sets of \(C_n\) for \(n\ge5\), with exact distance-two relocations only. Every clockwise gap of length at least four permits two distinguishable endpoint moves; smaller gaps permit none. The anchored-gap generating function follows by the exact \(n/k\) rooting multiplicity, including periodic words. Splitting \(n\) into four residue classes gives the complete maximum-degree population, and fixing the five-site `01000` block gives \(nF_{n-3}\) edges. The Perrin frozen-state coefficient is classical, not a novelty assertion. The self-contained `check.py` directly enumerates 39,585 independent sets through ring size 20 and verifies every predicted degree, edge and extremum; further gap-derived checks extend to 75. Finite checking is not substituted for proof.

## Originality — PASS, with historical-priority risk

Actual published-record searches examined strict hop length, exact degree distributions, exclusion gaps, and aliases. Hatano et al. (arXiv:2407.11768, first version July 16 2024), inspected by its available article text, define at-most-two hops rather than exactly two; its central statements concern decision complexity of bounded-hop reconfiguration, not this polynomial. Avis–Hoang (arXiv:2203.16861), inspected by full article text, study adjacent token sliding. The closest published record, *Connected maximal-independent-set exchange sectors and exact degree laws on cycles*, was read through its publicly accessible `RESULT.md`. It restricts states to inclusion-maximal independent sets, which have gaps two or three, and under its arbitrary one-for-one exchange rule every valid move is in fact one step. Our exact-two-hop graph freezes those configurations. Hence its full nonzero-degree polynomial does not imply the new formula. Its frozen subset corresponds to already-known Perrin enumeration, explicitly excluded from novelty. A comprehensive database cannot exclude an unindexed equivalent pure-hop calculation; no such decisive prior statement was located.

## Value — PASS

The strict two-site constraint is a natural distinct physical and combinatorial move rule (it differs both from usual slides and at-most-two hops). The exact degree distribution characterizes mobility at *every* allowed particle number and gap profile, and the four-residue extremizer counts quantify how rare optimally mobile states are. The edge formula provides a global rate-independent count for studying exclusion-process configuration graphs. This is a complete structural classification of a natural invariant, not merely a small numerical table or a rebranding of the classical frozen-state count. No new reachability or stochastic theorem is claimed.

## Closest sources and limitations

- H. Hatano et al., arXiv:2407.11768, initially posted 2024-07-16: at-most-two hop reconfiguration, different move relation.
- D. Avis and D. A. Hoang, arXiv:2203.16861, initially posted 2022-03-31: one-step token sliding, different move relation.
- *Connected maximal-independent-set exchange sectors and exact degree laws on cycles* (published research record, 2026): verified full `RESULT.md`, state space restricted to maximal sets and moves effectively distance one.
- Residual risk: older unindexed exact-two-site hopping models may independently contain the same degree polynomial; this is not disproved. Scope excludes rings smaller than five and connectivity questions.

Self-review: passed. Independent audit: not yet performed.
