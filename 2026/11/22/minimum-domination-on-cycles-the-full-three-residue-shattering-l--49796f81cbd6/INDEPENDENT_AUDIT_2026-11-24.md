# Independent mathematical audit

## correctness

PASS

The class is every minimum-cardinality dominating set, not the independent or inclusion-minimal families. A set of m=ceil(n/3) selected vertices dominates iff all consecutive cyclic gaps are at most 3, with budget 3m-n=0, 2, or 1 according to the residue. An arc between positive endpoints requires minimum deficit (-g mod 3), and zero deficit fixes every third vertex. On C_(3k+2), an all-positive triple leaves two consecutive zero-deficit arcs, and requesting their midpoint query negative exhausts the budget on the complementary arc and forces that midpoint positive. The same argument rules out the (2,0,0) minimum-deficit triple in C_(3k+1). For four queries, two consecutive zeros give the same contradiction; in the remaining alternating (1,0,1,0) pattern, requiring the first two anchors and omitting the next two leaves just one length-two jump on the complementary arc. Skipping the subsequent displacement-zero query then forces the next displacement-two query. Sufficiency follows from the C4 and C5 pair seeds and all eight C7 trace witnesses, checked by their gaps: subdividing an edge by three vertices permits a new selection at displacement three after the preceding old selection, changing its gap d into 3,d and preserving all old labels. Rooted gap compositions give nk pairs for residue 2 and n*binomial(k,2) triples for residue 1, including zero at n=4. Residue zero has only three periodic concepts; all singletons in all orders are shattered by rotation. The literal slip at RESULT.md line 51 is that the minimum deficits sum to 1 modulo 3, not the gap residues (which sum to 2); the definition and subsequent argument use the correct deficits. The all-order proof establishes the claim independently of the logged finite tests.

## originality

PASS

Credit the complete optimizer description and counts to prior work. The residue-only classification of which supports carry every trace, the all-order face polynomial, and the missing-label obstructions and subdivision argument are distinct from the optimizer description. The closest indexed learning-theory results change either the concept class or the graph; none of the inspected sources supplies a stronger lemma directly covering the stated trace tests. The bounded search does not certify historical priority.

## value

PASS

This gives a uniform, residue-only answer for every possible shattered support in a standard infinite optimum-solution family and pinpoints the changes in VC dimension, including the exceptional four-cycle. It answers simultaneous signed query extension without enumerating optimizers. Both the two-defect obstruction and the lifting of every old trace are substantive tools; this is not a recalculation of the previously known domination number or count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
