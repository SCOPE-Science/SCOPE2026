# Independent mathematical audit

## correctness

PASS

The formulas and exhaustive conditions are correct. The band product is the outer product of the first input's row sums and the second input's column sums, and balanced sum data have q^h lifts (choose the interior entries, then solve for the bordering row/column). For fixed first sum pair, the kernel in the reduced space W has sizes q^{m+n-1}, q^{n-1}, q^{m-1}, q in the four cases (both zero, only column sums nonzero, only row sums nonzero, both nonzero). Line 43's nonzero-case exponents include h and so describe the lifted matrix-Y kernels, not the stated W kernels; the subsequent fiber arithmetic uses the correct lift exactly once. Summing the reduced kernel sizes over first sum pairs yields K. For rank one, Z=zw^T with at least one factor of zero sum. If both first sum vectors are nonzero, a rank-one output forces either the first column factor parallel to z with sum(w)=0, or the first row factor parallel to w with sum(z)=0. This follows by passing to the quotients by the column and row lines and imposing the common-total condition in the remaining equation. If one sum vector vanishes, the sole nonzero vector has zero total and must span the corresponding target line. Counting the admissible first sum data with these kernels gives the three stated rank-one fibers. In rank two, factorizations of Z=UV^T form one GL2 orbit; the sum rows a,b obey b=aJ after change of bases. If both vanish every basis works, if just one vanishes none works, and if both are nonzero and a b^T=0 then b is a nonzero scalar multiple of aJ. The restriction fixes the determinant and gives one SL2 coset, including in characteristic two. Higher rank or nonzero total is impossible. The kernel and determinant proof also handles empty strata when a dimension is one. An independent reduced-space enumeration matched every target at (m,n,q)=(1,3,3),(3,1,2),(2,2,3),(3,3,3), including zero-fiber sizes 153,28,945,6987465.

## originality

FAIL

Independent originality of the prescribed-target classification is not established: the distinct indexed rank-one sandwich record 8f6dca19a4da gives exactly the same five classes, all fiber sizes, and the same image criterion in every nondegenerate dimension, under an exact algebra identification. The one-dimensional boundary is an immediate specialization of this common reduction, not a distinct advance. The earlier rank census alone is not the reason for failure: it gives aggregates and the zero fiber, but not the five prescribed classes. No relative priority of the two same-date originals is asserted.

## value

FAIL

An exact prescribed fiber classification on this algebra would be useful relative to a rank-only count. Here the exact classification in the nondegenerate regime already appears under the equivalent sandwich presentation. The only wider parameter regime is a one-row or one-column algebra, whose census follows immediately from one linear equation per free entry. As a separate finding this does not add a nonmechanical exact invariant or a substantive boundary to the common result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
