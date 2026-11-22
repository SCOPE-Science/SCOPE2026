# Mathematical review

## Correctness — PASS

For every root pair \(u\ne v\) the selected closed-neighborhood cardinality is exactly \(d_H(u)+d_H(v)-\mathbf1_{\{uv\in E(H)\}}\). The inequality at all root pairs first forces a three-star if any degree equals three, and otherwise forces all degree-two roots to form a clique of size at most three. This is an exhaustive structural dichotomy, from which the five component types, labelled exponential count and maximality characterization follow by exact elementary reasoning. The matching counts and the two parity formulas are derived by separately counting each graph type. Independently written root-degree branch enumeration, direct-neighborhood enumeration and factorial-component computation agreed over their specified finite domains; the proof does not rely on them for general \(n\).

## Originality — PASS (qualified)

The 2023 first-public preprint (arXiv:2308.16837) motivates limited-packing partitions, focusing on capacity two, whereas arXiv:2405.03237 develops total variants and capacity-two graph products. The inspected passages and searches for the same root-edge degree inequality, its line-graph equivalent, and the exact maximal/cardinality polynomials found no covering theorem. The earlier general closed-neighborhood estimates of Balister–Bollobás–Gunderson do not enumerate these objects. A related three-limited classification for rectangular rook graphs relies on a bipartite root graph and does not imply the triangle alternative or maximal polynomial in \(L(K_n)\). Historical priority remains provisional: obscure tables or unavailable full texts may yet contain equivalent results.

## Value — PASS

The triangle graph \(L(K_n)\) is a canonical, highly symmetric graph family. Closed-neighborhood limited packing models bounded local sensor occupancy. This result is an infinite-parameter **complete classification** and gives every subset cardinality and every inclusion-maximal cardinality, not just a minimum or maximum number. The sharp structural difference between maximum and maximal sets and the unbounded facet-size gap of the nonpure packing complex are natural information for enumeration and local search. The nonbipartite triangle component is essential, not a rename of the known bipartite case.

## Reproducibility and residual limitations

All scripts and exact output tables are embedded with this result, with ordinary C++17/Python3 replay commands in RESULT.md and VERIFICATION.md. Verification is computationally exhaustive only over the listed small orders; the symbolic component classification supplies the all-orders proof. Literature-priority clearance is not exhaustive, and external independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
