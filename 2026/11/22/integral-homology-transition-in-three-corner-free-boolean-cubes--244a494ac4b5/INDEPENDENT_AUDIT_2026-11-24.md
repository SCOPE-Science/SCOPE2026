# Independent mathematical audit

## correctness

PASS

Any three vertices of a Boolean coordinate square form a three-vertex path. Conversely, the two edges of such a path in Q_n flip distinct coordinates, and the path lies in that coordinate square. Avoidance is exactly induced maximum degree at most one, i.e. components of size at most two, proving the identification with Ind_2(Q_n). For the Morse matching, a directed cycle would have to alternate up and down, since up edges never occur consecutively and the dimension must return. At the least stage present on the cycle, the toggled vertex is added and hence is also deleted on some down edge; both ends of that down edge were unmatched at the beginning of this stage, so that edge would have been matched and oriented up. This contradiction establishes acyclicity in the augmented face graph. The signed critical boundaries follow by successive unit elimination with incidence signs. An independent bounded implementation (not the source checker) rebuilt the forbidden triples and faces and reproduced the critical ranks and integral matrices; see /workspace/branches/91850047-73a7-45df-a0cb-45917c15986f/independent_check.py and independent_check_results.txt. It enumerated 3,302,633 faces for n=5, including the empty face. The critical ranks in degrees 5 through 11 were (1,16,757,73,12,1,1); nonzero differential ranks were 1,15,61,12,1 in degrees 6,7,8,9,11, respectively. Consecutive compositions vanished; unit Smith elimination left only zero residual matrices. The torsion of the cokernel of d_(j+1) equals the torsion of H_j, because the quotient by H_j is a free boundary image. Thus H_7 is free of rank 757-15-61=681 and all other reduced groups vanish. The original lower cases were also independently reproduced but are not a new finding. The source Python and C++ were inspected, not executed; this is an integral homology check, not a homotopy classification.

## originality

PASS

The corrected claim is limited to the five-cube. Stronger exact results for dimensions two through four cover those parts of the original table, and are credited in the repair as prior results. No distinct inspected statement gives the five-cube integral homology of this two-independence complex; ordinary cube independence and full-square hyperedge constructions involve different simplicial complexes. The verdict credits the specific five-cube computation only, not a new construction or a discovery of the mixed four-cube case.

## value

PASS

The dimension-five member is the immediate successor to the known first mixed case at dimension four. An exact calculation is useful because mixed-degree behavior might have persisted; instead the next complex concentrates in degree seven with exact integral rank 681 and no torsion. That qualitative return and its complete integral numerical witness motivate this particular cutoff, without claiming a general pattern or treating the repeated lower cases as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
