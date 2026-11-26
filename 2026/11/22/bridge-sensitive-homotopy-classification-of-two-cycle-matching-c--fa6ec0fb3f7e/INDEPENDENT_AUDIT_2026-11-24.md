# Independent mathematical audit

## correctness

PASS

Deleting the bridge in the matching complex leaves the join A of the two cycle complexes, while the bridge link L is the join of the matching complexes of the vertex-deleted cycles. Its inclusion is the join of the two individual inclusions. For length m=0 mod 3 the individual source is contractible; for m=1 mod 3 each of the two adjacent line-graph vertex deletions has contractible link Ind(P_{m-3}), so the individual inclusion is an equivalence; for m=2 mod 3 the sphere source has smaller dimension than the target and the map is null, including S^0 into a connected circle. These facts make A→X an equivalence when a residue is zero, make X contractible for (1,1), and give a splitting relative to A in the two remaining cases, by a nullhomotopy of the join attachment. Joins distribute up to homotopy as suspended smashes for these based finite complexes, with the S^0 cases included. The sphere dimensions, multiplicities and integral bridge-deletion assertions all follow. I inspected VERIFICATION.md, verify_barbell.py and verification_output.txt without executing the uploaded script. Independently, signed simplicial boundary elimination over F3 (replay: python3 barbell_review.py from the scratch script directory) checked both Betti ranks and inclusion image ranks for all six unordered pairs from {3,4,5}; for (4,5) the degree-2 image has rank 1 in rank 2, and for (5,5) the image has rank 1 in degree 3 and zero in degree 2. The image calculation adds a basis of the deletion's cycles to the columns of the enlarged complex's boundary and subtracts the rank of the boundary alone. This is finite corroboration, not a substitute for the integral cofiber argument.

## originality

PASS

Pass for the exact six-case integral homotopy types and the bridge-deletion map classification. The classical path and cycle formulas and qualitative sphere-wedge alternative are directly credited. The most similar indexed record uses the same barbell graph but computes a different complex and map; the date alone establishes no priority.

## value

PASS

A barbell is a natural minimal test of how matching topology reacts to a bridge. An integral classification with the inclusion identifies exactly when a single edge kills the existing homology, distinguishes mixed-dimensional wedges from the qualitative outerplanar alternative, and gives reusable attachment information not present in Betti counts alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
