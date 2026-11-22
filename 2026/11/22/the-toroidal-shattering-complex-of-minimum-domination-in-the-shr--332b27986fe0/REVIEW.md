# Scientific review

## Correctness — PASS

The exact domain is the standard Cayley graph on \(\mathbb Z_4^2\), with closed-neighborhood ordinary domination. A complete 15-difference classification gives 32 and only 32 dominating triples and proves that none of size at most two exists. These are exactly the 32 triangles of an isomorphic but edge-disjoint Cayley graph. Two complete translation-orbit trace tables verify all eight patterns for a triangle; the all-positive trace proves that no other supports can be shattered. The polynomial and VC dimension follow. A positive-only branch bounds online depth by three, and an explicit periodic triangular torus embedding proves the *integral* homology and torsion-free result. The two standalone checkers independently reproduce the optimum and shattering censuses; the Python checker also checks the geometric classification and witness table. The finite-field boundary rank is used as a consistency check only.

## Originality — PASS within inspected evidence

The 2015 geometric source already gives a toroidal Shrikhande model; its graph topology is not claimed new. The 2017 minimum-domination source is a general motivation, not a finite-graph shattering result. The 2019 special-graph domination article addresses cardinalities, not the optimal-set shattering complex, and its stated ordinary domination number four conflicts with an explicit three-vertex cover checked here. Three particularly close public full mathematical records were inspected: *Dominance homotopy and symmetry distinguish the Shrikhande–rook twins* computes a complex of complements of all dominating sets, *Paired-domination distinguishes two graphs with identical total-domination polynomials* studies distinct total/paired constraints, and *A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs* uses only closed neighborhoods as concepts, not minimum ordinary dominating sets. Their conclusions do not imply a toroidal complex from 32 three-element optimizers. Concept-family definitions, not similar terminology, decide noncoverage. An unindexed or inaccessible equivalent result remains possible; searches cannot certify absolute priority.

## Value — PASS

The minimum ordinary dominating sets unexpectedly reconstruct a second, edge-disjoint copy of the original graph as their two-point shattering relation; the entire shattering complex is a torus rather than a simplex skeleton or a flag matroid. This supplies a structural bridge between an extremal graph-optimization family, VC/online learning geometry and integral topology, alongside an explicit resolution of a conflicting published domination-number claim. These are motivated exact invariants, not arbitrary finite table entries.

## Closest literature and limitations

- Sane (2015), *The Shrikhande graph*: known toroidal Cayley construction, not optimizer-shattering.
- Cyman–Henning–Topp (2017), *On accurate domination in graphs*, arXiv:1710.03308: background definitions and comparison of optimization notions, not this concept family.
- VinuPriya–Mageswari–Bibi (2019), *Total Domination and Inverse Total Domination Number of Some Special Classes of Graphs*: directly examines the same graph but claims a conflicting ordinary domination number; the Cayley cover-table proof here is independent of its figure numbering.
- Three 2026 publicly accessible exact graph-complex and shattering records named in `RESULT.md`: all inspect different predicates/concept families.

This is an exact finite graph statement with independent implementations, but no external mathematical audit. Historical priority against unpublished or unindexed work is unresolved. The modular homology rank alone is not used as a proof of integer homology.

Self-review: passed. Independent audit: not yet performed.
