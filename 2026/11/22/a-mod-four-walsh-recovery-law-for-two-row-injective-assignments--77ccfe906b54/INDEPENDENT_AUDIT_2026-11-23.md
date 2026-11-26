# Independent mathematical audit

## correctness

PASS

With counting convolution the characters of F_2^(2n) are an orthogonal eigenbasis. Each support vector uses row-one coordinate i and row-two coordinate j with i!=j, so deleting the diagonal from the product of the two row sums gives W=ab-c. The (u,v,t) type count chooses the first negative set and the inside/outside portions of the second; no type multiplicity is lost when different types give the same W. Modulo 4, W=n(n-1)-2(n-1)(u+v)+4(uv-t); for odd n this gives residues 0 or 2 and the claimed nonzero lower bounds. At n=4k+3 the stated (2k+1,2k+1,k) yields 2, including k=0. At n=4k+1, k>=1, the feasible overlaps k and k-1 give 0 and 4. At every even n a balanced first row and constant second row give 0; flipping a position where the first row is positive gives 2, including n=2. The all-positive signs attain the triangle-inequality bound n(n-1); rank and condition number then follow in the stated normalization. n=1 has empty support and no nonzero gap, and is not claimed.

## originality

PASS

The contribution is the combined all-width signed classification, exact singularity criterion and sharp surviving gaps for the row-saturating 2-by-n injections, not diagonalization by Walsh characters or a general permanent identity. No implication-equivalent statement was located in the checked material.

## value

PASS

The two-row model is the first row-saturating assignment convolution in which a genuinely nontrivial collision exclusion couples the rows. The result identifies when recovery on the full labelled Boolean space is possible and, otherwise, gives exactly how many directions are lost and how strongly the remaining directions can be inverted in l2. The all-width mod-four transition and attained norm ratio add substance beyond applying the standard diagonalization or giving a routine small-board spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
