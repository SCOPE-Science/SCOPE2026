# Scientific review

## Correctness — PASS

The Heawood graph has a directly specified twenty-one-edge Fano-incidence construction. Each simple hexagon corresponds bijectively to a noncollinear Fano triple, independently verified by graph-depth-first enumeration; hence there are exactly twenty-eight. The binary cycle space has dimension eight, with fundamental-cycle chord coordinates. A complete, exact 256-character signed enumeration gives six multiplier levels (multiplicities 28, 56, 108, 42, 21, 1 in increasing eigenvalue order), independently recovered by a butterfly transform. Restriction to the cycle space repeats each value exactly 8192 times. The inverse projection kernel has absolute integer mass 1936 in 256 entries, giving sharp norm 121/16; averaging arbitrary competing projections over translations proves unrestricted optimality. The stand-alone `verify.py` passed after construction and covers every finite case required by the proof. No infinite extrapolation is claimed.

## Originality — PASS under bounded comparison

Dejter (arXiv:1002.1960, originally dated 2010-02-09) connects the twenty-eight hexagons to Coxeter-graph disjointness, but his paper's principal results concern seven-cycles of the Coxeter graph and the Klein graph, not signed Fourier transforms of Heawood edge masks. Lawrence–Wilson (arXiv:1907.11978) proves geometric cycle-enumeration and transitivity results, not the 256-character cycle-code transform or a projection norm. Brouwer's graph reference gives the ordinary adjacency spectrum of the fourteen-vertex Heawood graph, which cannot directly substitute for the Fourier spectrum of the 21-edge incidence group. Related published work for six-cycles of complete bipartite graphs with a three-vertex shore concerns a different incidence orbit and does not contain this seven-by-seven projective-plane restriction. The twenty-eight noncollinear Fano triples in seven point coordinates have affine dimension six, versus eight for the twenty-eight Heawood hexagon edge masks; a coordinate-affine equivalence therefore cannot subsume this result. A hidden earlier equivalent identity or code-table computation remains possible, so originality is best-knowledge, not certified priority.

## Value — PASS

The Heawood graph is the canonical cubic girth-six cage and Fano-incidence graph. Its shortest cycles form a natural set of twenty-eight measurements whose edge-parity profiles are governed by the full eight-dimensional cycle code. Determining which 21-coordinate Boolean Fourier signals survive those measurements, and the smallest possible endpoint amplification needed to recover their range, is an intrinsic, nontrivial stability classification. The exact rank and optimal norm are not implied by merely knowing the twenty-eight hexagons or their Coxeter disjointness graph. The result is finite but complete and supplies a reusable eight-dimensional certificate. No general claim about other cages is made.

## Literature and scientific limits

Primary comparisons include Dejter (2010), Lawrence–Wilson (2019), and Brouwer's Heawood reference. The most relevant indexed analogue is the six-cycle Walsh study of \(K_{3,n}\), which uses different objects. Searches for an exact Heawood cycle-code transform and the fraction \(121/16\) revealed no covering theorem; failed search alone is not proof of priority. The finite computation has been checked in the attached verifier, but no independent researcher has audited it.

Self-review: passed. Independent audit: not yet performed.
