# Independent mathematical audit

## correctness

PASS

Reconstructed the exact mu(C5) graph on originals 0..4, clones 5..9 and apex 10; all 20 edges and full ten-element D5 action follow from degree classes and pentagon automorphisms. An independent implementation (distinct from verify.py) enumerated all matchings with simplex counts (20,135,365,360,87), rebuilt oriented simplex boundaries and calculated ranks (19,116,249,87) over F2 and F101. Because d1<=20-1=19, d2<=135-rank(d1)=116, d3<=365-rank(d2)=249, d4<=87, modular lower bounds force identical rational ranks. Thus reduced H3 has rank 360-249-87=24 and all other reduced rational groups vanish, not just a mod-prime assertion. Independently computed all 10 signed fixed-face trace vectors: identity (20,135,365,360,87), each nonidentity rotation (0,0,0,0,2), each reflection (2,-3,-5,0,1). Signed reduced Lefschetz then gives H3 character (24,-1,0). The rational character is exactly 2 regular D5 plus Q(zeta5) (reflection acts by conjugation). Finite rational semisimplicity gives module isomorphism; averaging yields D5-invariant dimension 2 and C5-invariant dimension 4; rational orbit-space cohomology equals group invariants. The independent computations exhaust all simplices and 10 automorphisms of this ONE finite graph, and a fresh SHA-1 Git tree rebuild matches the assigned source tree. No integral representation or homotopy quotient claim is inferred.

## originality

PASS

The original contribution assessed is the entire rational D5-homology module and quotient invariants for the canonical Grötzsch matching complex; not the previously published wedge of 24 three-spheres or known face vector. Full comparison with the earlier same-graph source https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-gr-tzsch-graph-matching-complex-is-a-wedge-of-twenty-four-th--514850eb507b/RESULT.md finds its integral homotopy theorem does not determine a D5 action. The 2025 full accessible Balasubramanian article lists exact matching polynomial coefficients, without signed fixed-face or homology module data. Engström connectivity and Jonsson complete-graph matching complex theorems do not imply the 24,-1,0 trace. Closely related five-crown and Tietze equivariant results concern different complexes and acting groups. Real Resultary and web searches under graph/line-graph/Mycielski/equivariant aliases identified no independent earlier exact character. This is bounded best-of-knowledge originality, not a certified priority search.

## value

PASS

The Grötzsch graph is a canonical smallest triangle-free 4-chromatic graph with intrinsic full dihedral symmetry; the natural action on the ordinary matching complex yields an exact rational representation invariant. The earlier 24-dimensional nonequivariant H3 is insufficient to determine rotation/reflection signs, its rational irreducible decomposition, or the Betti number of the symmetry quotient. Computing the complete module 2Q[D5]+Q(zeta5) and a two-dimensional invariant sector fills a motivated, previously undetermined exact structural gap. The exact single-graph classification is mathematically useful in equivariant combinatorial topology without claiming a family theorem or paper-sized downstream result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
