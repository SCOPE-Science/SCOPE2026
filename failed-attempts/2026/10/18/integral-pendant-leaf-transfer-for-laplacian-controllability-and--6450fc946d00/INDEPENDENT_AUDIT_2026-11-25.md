# Independent mathematical audit

## correctness

PASS

The signed weighted transfer follows integrally from the old block y[j+1]=L y[j]-e z[j+1] and the leaf block z[j+1]=t(z[j]-e^T y[j]), with z[1]=t. Thus after clearing the last entries with the first column, the old block of the remaining columns is -t K times an integer upper-unitriangular matrix. Expanding down the first column gives (-1)^n, which cancels the sign from (-t)^n; this also proves the determinant identity over the reals. For the finite threshold I independently generated rooted isomorphism classes through order nine as multisets of smaller branches, grouped by rerooting, and used exact rational elimination rather than the supplied leaf-addition/Bareiss program. The free-tree counts were 1,1,1,2,3,6,11,23,47, with 749 vertex positions tested by orbit weighting. Through order eight no nonzero determinant exceeded magnitude one. At nine there was one nonunit root orbit of size two: precisely the stated tree and roots, both with determinant -2. For root 2, the indicator w of {0,5,6,7} satisfies Lw=w modulo 2 and w^T e_2=0, so its parity kernel contains the integer image; both have index two. Unit-leaf iteration gives witnesses at every larger order.

## originality

FAIL

A distinct published Resultary/SCOPE record gives the same sharp threshold, the same unique unlabelled tree and two symmetry-related roots, and the same parity description of the reachable-state lattice. These are prominent parts of the frozen finding, not just overlapping background. The published record does not establish the general weighted integer block transfer, and the evidence does not adjudicate priority: the two index paths have different dates, but that alone does not establish first disclosure or dependency. This is failure of the full frozen finding to clear the distinctness check, not evidence that the weighted transfer is known or that any claim is false.

## value

PASS

The transfer controls the entire integral cokernel, including obstructions invisible to real or rational rank, and makes extension constructions transparent. The sharp tree threshold and explicit parity sublattice give a meaningful boundary and distinguish two natural controllability questions. These are worthwhile mathematical objects even though the finite claim is already covered and cannot be credited as distinct here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
