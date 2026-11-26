# Independent mathematical audit

## correctness

PASS

The frozen statement that the last edge changes the shape/geometry of the optimal placements is misleading as a claim about the sets themselves: the two displayed classifications give exactly the same family on the common labeled vertices. The corrected RESULT, REVIEW, AUDIT and SLOGAN are in repairs/1/ with the supporting package; the frozen files remain intact. Reassessment: if D is the diagonal matching indicator, the clique-symmetric and clique-antisymmetric restrictions are mI-J and mI-J+2D, respectively. For k<m, summing within each clique in the eigenvector equations at an unmatched coordinate forces the two clique sums to zero at eigenvalue m; matched coordinates must then agree. This yields the two independent class constraints and dimension 2m-k-2. Antisymmetric matched sum-zero vectors give dimension k-1 at m+2; the remaining two antisymmetric block-constant modes have trace m+2 and determinant 2k. Their roots are distinct (discriminant at least (m-2)^2+8), avoid 0,m,m+2 and have both class coordinates nonzero. The symmetric m-space and antisymmetric m-space, together, have the required two independent constraints. PBH at the lower bound demands two missing classes of different types, exactly the condition for independent constraint columns (1,1),(1,0),(0,1); this also sees all but at most one of the matched antisymmetric coordinates. For k=m the restrictions are mI-J and mI-J+2I, with 2 distinct from m (m>=3), and both large spaces are detected by observing m-1 distinct pairs. The counts are 2^k(m-k)^2+2k(m-k)2^(k-1) and m*2^(m-1). At k=m-1 the only allowable omissions are both unmatched singletons, or an old matched pair and one singleton. Upon joining the singletons into the new match these are precisely the cases omitting the new pair or an old pair, respectively; both implications preserve the chosen vertices. An independent exact Kalman rank replay (integer Krylov vectors, full rank modulo a prime or exact rational fallback) at repairs' declared m=3..5 checked all 1094 candidate sets, 420 controlling sets, equality of the actual final-edge optimizer families for each m, and the 4/12 zero-forcing split at (3,2). Replay: python replay/1_cliques.py. This checks small graphs only; the block/PBH argument covers all stated m,k. The frozen verifier was inspected, not executed.

## originality

PASS

Best of knowledge: the exact fixed-unit-Laplacian min-size placement classification and resulting final-edge invariance are not supplied by the inspected strong-structural criterion or by the relevant surfaced records. The repaired corollary is a consequence of the classification, not claimed as an independent invention of a new controllability test. The existence of unlocated equivalent work remains possible.

## value

PASS

Two dense communities with a varying number of independent bridges give a natural coordinate-leader problem. The result determines the budget and every allowable optimum on the actual labeled graph, with exact preservation under the final bridge despite changed eigenspaces, and a documented separation from zero forcing. This is not simply tabulation or restating PBH. The false suggestion of changed optimum geometry does not survive into the repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
