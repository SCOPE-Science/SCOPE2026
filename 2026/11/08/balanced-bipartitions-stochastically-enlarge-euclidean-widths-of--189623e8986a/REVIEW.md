# Scientific review: balanced bipartitions and directional widths

## Correctness
**PASS.** The support function is exactly twice the maximum cross-part absolute coordinate gap. A threshold graph on real coordinates cannot have two distinct edge-bearing components: for any two long edges, their extreme ordered endpoints create a third long bridging edge. This gives the exact conditional probability of avoiding every long edge, and the binomial difference has a definite sign under each balancing transfer. Distinct coordinates yield a nonempty interval with precisely one long edge, proving strictness of all positive width moments by the tail-integral identity. The general argument covers all stated integers and thresholds. Finite enumeration checks the conditional formula and sign separately.

## Originality
**PASS, subject to historical-priority risk.** Higashitani--Jochemko--Michałek (arXiv:1807.07678, Sections 3--4) classifies facets and Ehrhart invariants of exactly these complete-bipartite symmetric edge polytopes; its facet characterization and \(h^*\)-formula imply no distributional comparison of Euclidean widths. Chen--Davis--Korchevskaia (arXiv:2107.12315, Sections 3--4) studies face/facet subgraphs, and Ohsugi--Tsuchiya (arXiv:2008.08621, Sections 1--2) studies lattice-volume and matching-polynomial information. Related geometric results concerning graph skeletons, inballs, Löwner ellipsoids, and graphical zonotopes have different objects or invariants. The possibility of an earlier equivalent theorem in random-partition/extremal-distance language remains unresolved.

## Mathematical value
**PASS.** The classification compares a natural family of nonnested graph-derived lattice polytopes by their entire distribution of Euclidean directional widths, not merely a single extremal radius or average. The conditional binomial law gives a structural reason for the strict balance extremum and transfers to every positive moment. This reveals geometric behavior not determined directly by known Ehrhart or face-counting formulas.

## Limitations
The CDF is represented by a spherical average of an exact finite conditional count, not a closed elementary density. Strict CDF inequality is not claimed at every threshold. The finite checker tests examples, while the universal assertion depends on the independent analytic argument. Published-source searches reduce but cannot eliminate the risk of equivalent older formulations.

Self-review: passed. Independent audit: not yet performed.
