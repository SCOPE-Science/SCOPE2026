# Scientific review

## Correctness — PASS
The object is the inclusion graph between the two- and three-subsets of five labels; all 6,212 independent faces are explicitly generated. An exhaustive acyclic matching of the augmented face poset leaves exactly five critical five-cells and one critical four-cell, proving that integral fifth homology is free of rank at most five. Five canonical induced six-edge matchings yield signed octahedral cycles; five closed maximal-facet cochains pair with them as the integral identity matrix. Consequently their classes constitute a primitive full basis. All group actions are checked as equalities of integer chains under each of 120 relabelings and the complementary involution. `check_desargues_integral.py` and `verification_output.txt` permit deterministic replay; finite enumeration is exhaustive for this finite graph, not an inference from tested small instances.

## Originality — PASS relative to inspected evidence
The closest same-graph homotopy records compute the nonequivariant wedge of spheres; the previously accessible same-graph rational symmetry result describes the five-point character twisted by the complement sign. Neither determines the integral group-module lattice or primitive geometric generators, and rational equivalence cannot certify a specific integral lattice. Randić's 1979 automorphism calculation has no topological homology, Freij gives methods rather than this graph-specific lattice, Tsukuda's full paper gives a nonequivariant general incidence reduction, and Kumar–Singh–Verma's full paper concerns Betti invariants of edge ideals, not the present topological equivariant invariant. An unindexed equivalent calculation remains possible. Randić's first published date is recorded only as June 1979 and is not assigned an invented day.

## Mathematical value — PASS
The 20-vertex Desargues–Levi graph is a canonical cubic incidence graph with a natural 240-element symmetry group. A geometric primitive lattice basis supplies arithmetic equivariant information absent from ordinary Betti numbers and rational characters; in particular, an order-five symmetry has one length-five Jordan block upon reduction modulo five. The result is a natural complete integral classification in degree five, not a redundant rational trace calculation or arbitrary subcomplex slice.

## Scope and limitations
This does not classify the integral degree-four action, integral quotient cohomology or equivariant homotopy. A full priority review of all possibly unindexed literature has not been made. The computational certificate independently reconstructs the whole finite object and the pairing but is not independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
