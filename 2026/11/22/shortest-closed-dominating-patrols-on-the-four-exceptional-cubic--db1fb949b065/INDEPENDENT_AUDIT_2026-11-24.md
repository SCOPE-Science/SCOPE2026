# Independent mathematical audit

## correctness

PASS

I re-enumerated the four specified labeled graphs independently. For length 2k and a fixed root, a closed word corresponds bijectively to an ordered pair of length-k half-walks from the root to the same midpoint, with the second half reversed. Taking the union of their closed neighborhoods, I recovered all the coverage maxima in RESULT.md lines 67–72, and the optimum (length, rooted words, dihedral classes) tuples (10,10920,546), (8,96,6), (12,5400,225), (10,240,12). Connectivity, cubic degree and bipartiteness were checked directly; length zero sees four vertices. I independently generated automorphisms by extending an injective map along neighbor permutations in breadth-first order. Every automorphism gives exactly one such extension, and the terminal maps preserve all edges. This gave group orders 336, 96, 216, 240 and exactly the ten reported orbit sizes and representative words. Leaf stripping and support degrees recover the listed tree and cycle geometries. In the excursion descriptions 'two-edge' refers to distinct off-cycle edges in the traversed support, not a two-step budget for the whole detour.

## originality

PASS

The supported distinct claim is the joint optimum-walk and full-automorphism classification for exactly these four graphs, not the definition of a watchman's walk, the classification of the graphs, or unconditional priority for every individual count. The strongest indexed exact match is the frozen record itself. No available distinct comparison establishes the ten-orbit classification; there is an explicit unresolved multiplicity-literature risk.

## value

PASS

These are the four naturally named exceptions in a cubic-symmetry classification; the walk problem distinguishes their structure in a way neither girth nor graph symmetry alone provides. In particular the complete orbit list distinguishes an optimal tree-supported Heawood walk from its cyclic alternatives, and detects non-cycle optima in Pappus but none in Möbius–Kantor or Desargues. The precise orbit representatives and support data are useful test cases for structural claims about shortest dominating walks allowing repeated edges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
