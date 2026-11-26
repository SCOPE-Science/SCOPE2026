# Independent mathematical audit

## correctness

PASS

The all-positive and all-negative traces force a forest S and a connected complement, and each partial positive trace extends to a tree after deleting the other queried edges. Plane duality gives the second forest test, with f_i the face-to-face rim edge F_(i−1)F_i. At a zero in each rim word, the corresponding accumulator resets, giving one state assignment exactly when no rim path has two spokes. If either rim word is all ones, summing its recursion forces the opposite word all zeros and leaves exactly two constant choices for the nonresetting accumulator; this produces the four weighted exceptions. Independently compress the state using (a,d)=(rc,d). The only successor states are 00,01,11 since a'=RC≤R≤D=d'. For those states the weighted matrix (rows and columns in that order) is [[1+z,z,z²],[1,2z,0],[1,0,z]]. Each edge-labelled closed walk lifts uniquely to the original states because the new c and d are determined by its source compressed state and its chosen R,S. Its trace, sum of principal two-minors and determinant are 1+4z, 2z+4z² and z² respectively, proving the cubic and p_0=3 exactly. Newton identities and removal of formal m=1,2 terms give the displayed recurrence and series. The leading coefficient of p_m solves a_m=4a_(m−1)−4a_(m−2) with a_1=4, a_2=8, so subtracting 4 gives 2^(m+1)−4 at degree m. Fixed tree size bounds the all-yes branch of the online tree; repeated queries on a branch cannot occur in a complete mistake tree, and a shattered m-set realizes depth m. The roots at z=1 are the three distinct squared positive eigenvalues of the six-vertex path, giving the stated closed form and growth.

## originality

PASS

The surviving originality is the size-refined wheel enumeration, the identification of its ungraded count with an old numerical sequence minus four, and the labelled nonpure boundary. The general forest/coforest criterion, complementary-tree count, numerical cubic power-sum sequence at z=1, and its numerical trigonometric formula are not original as standalone results. The known univariate sequence warrants explicit credit; it does not determine the joint wheel polynomial or prove the combinatorial identification. Priority is conditional on inspected evidence.

## value

PASS

The exact invariant is motivated by labelled edge queries and simultaneous graph/dual forest constraints, and gives information not recoverable from the ordinary tree count, tree-pair census, or the known ungraded numerical terms. A fixed cubic supplies a compact formula at all rim sizes and reveals an explicit nonpure complex despite the matroid structure on either side. These features are the value, not recomputation of a path-walk table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
