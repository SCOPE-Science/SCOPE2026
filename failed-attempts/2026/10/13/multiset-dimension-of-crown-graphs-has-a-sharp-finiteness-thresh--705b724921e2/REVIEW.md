# Independent mathematical audit

## correctness

PASS

For n≥3 the four distance multiplicities at a_i are (x_i,q−y_i,p−x_i,y_i), with the symmetric formula at b_i. Within each shore two equal membership pairs collide, giving n≤4. At n=4 all four pairs are used, yielding p=q=2 and a cross-shore collision at the (0,0) index. At n=3 the two balanced three-pattern choices collide at (0,0) or (1,1), respectively, and all six histograms for each unbalanced choice are distinct. There are 2·3! sets. The frozen verifier and recorded output were inspected, not executed. A fresh Floyd–Warshall and subset-enumeration implementation tested every subset of each Cr_3 through Cr_8 (87,360 total): exactly twelve size-three sets at n=3, none thereafter, and each individual subset agreed with the stated predicate. This corroborates rather than proves the unbounded conclusion.

## originality

FAIL

The entire result is a direct consequence of the October 12 crown outer-multiset classification after a complement reduction, not merely a similar result for a differently defined invariant. Crown vertices have the same full distance histogram (1,n−1,n−1,1). Thus W resolves all vertices iff both W and V\W are outer multiset resolving: zero distinguishes membership across the two parts of this partition; within W, taking the common total histogram minus the histogram to V\W gives precisely the needed equality test. The earlier result gives both sizes ≥2n−3, hence n≤3; for n=3 both sizes equal three. The earlier outer criterion for W then says the omitted shore sizes are (2,1) or (1,2) with one common index. This gives exactly one doubly absent index, one singleton index, and one doubly selected index. Its complement automatically meets the same criterion. This recovers both exact membership collections and the count twelve. The scalar boundary also follows independently from the 2017 cycle theorem.

## value

FAIL

Ordinary multiset resolution on a canonical diameter-three family is a natural question, but in this case the entire proposed contribution is mechanically recoverable from the earlier all-set theorem by a single histogram subtraction and the exact size bound. The bounded reproduction and independent elementary argument do not supply a separate new invariant, general theorem, or unresolved boundary to retain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
