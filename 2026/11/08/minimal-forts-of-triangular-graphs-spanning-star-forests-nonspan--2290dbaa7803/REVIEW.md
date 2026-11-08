# Scientific assessment

## Correctness — PASS

The claim has a complete proof for every integer \(n\geq3\). The crucial identity for an unselected root edge \(uv\) is that its selected-neighbor count in the line graph is \(d_H(u)+d_H(v)\), which reduces forts exactly to no simultaneous zero and one degrees. Inclusion-minimality is then proved against **all proper nonempty subsets**: spanning edge-cover-minimal subgraphs are star forests; any nonspanning fort contains a cycle; and proper subsets of the claimed forests and cycles cannot be forts. The block-weighted exponential formula and cycle multiplicities are derived without double-counting the size-two star. Exact direct enumeration for orders three through seven confirms the classification and coefficients; it does not substitute for the proof.

## Originality — PASS, with publication-priority caveat

The 2024 preprint of Becker et al. concerns general minimal-fort bounds and specific families including paths, cycles, spiders, wheels, sunlets, and windmills. Its searchable full text does not present triangular graphs or line graphs as a treated family. The 2023 preprint of Cameron et al. introduces fort hypergraph methods and considers Cartesian products, not this exact root-edge classification. Searches for triangular graph / Johnson graph / line graph minimal forts, equivalent stalled zero forcing formulations, and direct coefficient sequences did not identify a statement implying the two-family theorem. General algorithms for enumerating minimal forts do not by themselves give this explicit uniform classification. The possibility of an unindexed or differently named stronger result remains a genuine priority risk.

## Mathematical value — PASS

Minimal-fort hyperedges are the irredundant obstructions in the fort transversal formulation of zero forcing. For a standard strongly regular graph family, the result identifies the entire obstruction hypergraph as the union of two familiar combinatorial objects, giving a closed cardinality enumerator, a sharp full spectrum, and a unique uniform small-order case. It is substantially more informative than a numerical minimum or a routine isolated coefficient, without claiming a new general zero-forcing theorem.

## Reproducibility and limitations

Execute `python3 verify_forts.py` with Python 3.8 or later. The standalone enumerator enumerates all proper subsets when testing minimality, so the nonmonotonic fort property is not silently reduced to single deletions. Full evidence supports only the specified triangular-graph family. The work has not undergone independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
