# Scientific review

## Correctness — PASS

The complete proof is based on the incidence-excess identity \(k^2-(k^2-2)=2\); a radius-zero anchored clockwise gap encoding with exactly two units; and legal source slides equated to adjacent transfers of two units on a cyclic set of \(k\) sites with two capacity-one sites. The two-unit transfer graph is connected, and a closed transfer loop advances the anchor. Degree-two, three and four counts follow from a complete enumeration of token occupancy types. Every assertion quantifies over all integers \(k\ge3\); source ignitions must be unburned and round labels are fixed. Direct enumerations of independently generated schedules and transitions corroborate the infinite proof at \(k=3,4,5\), and the constructive schedule generator checks through \(k=7\). The finite enumerations are not offered as proof for all \(k\).

## Originality — PASS, subject to historical-priority risk

Bonato, Janssen and Roshanbin, *How to burn a graph* (arXiv:1507.06524v1, Section 2, formula (1), Theorem 10, Corollary 11), describe graph burning, the distance/ball formulation and the minimum number of rounds for paths and cycles, **not** the complete reconfiguration graph, components or degree spectrum of the optimum strict schedules for \(C_{k^2-2}\). The 2021 survey of graph burning discusses the framework, and Pereira et al. (ESA 2024, Sections 1–3) study optimization algorithms, not the stated two-defect reconfiguration classification. The previously studied perfect-square and one-below-square source-slide cases do not imply the present two-defect result: the permitted gap defects increase from zero or one to a genuinely interacting two-unit local-mobility system. Search comparisons of the complete statement, its aliases and stronger coverage revealed no covering theorem in sources checked. Unindexed or inaccessible work remains a real priority risk, not a claim of absolute novelty.

## Value — PASS

The exact component count and degree distribution determine which optimum contagion-scheduling choices can be reached by changing a single ignition position while holding all other source times and locations fixed. At a deficit of two vertices from the perfect square, interacting overlap defects produce local degrees two, three and four and a connected state system within each of \((k-1)!\) cyclic-order classes. This is structural information not supplied by the known minimum burning number or by simpler zero-/one-defect classifications. The result applies to a natural infinite family rather than an arbitrarily chosen finite instance.

## Limits of the review

The component diameters, other cycle orders and alternative move rules are not determined. Search-based historical comparison cannot establish absolute priority. Computations only corroborate a separately supplied infinite-family proof. An independent external audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
