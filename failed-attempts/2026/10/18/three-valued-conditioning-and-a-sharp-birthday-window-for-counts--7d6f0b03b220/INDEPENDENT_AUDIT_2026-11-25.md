# Independent mathematical audit

## correctness

PASS

The padded rows do not enter SA. In full rank, the isometries A and Q imply kappa(AR^(-1))=kappa(R)=kappa(SA). With no collision the active Gram is the identity; with at most m-2 occupied buckets the dimension bound forces rank failure. Exactly m-1 occupied buckets means exactly one pair. Equal signs annihilate e_i-e_j in the zero-sum hyperplane. With opposite signs the compressed Gram on the hyperplane is I+(xx^T-yy^T)/2, with x=e_i-e_j and y the projection of e_i+e_j. These vectors are orthogonal, with squared lengths 2 and 2-4/m. Thus the two exceptional eigenvalues are 2 and 2/m and the rest are one. Counting injections of the active coordinates or paired blocks and multiplying the single-pair case by one half gives the stated masses. When s=m-1 the collision-free event is impossible; the other two events remain positive. Expansion of log p1 gives -m(m-1)/(2s)+O(m^3/s^2) in the quadratic window, and p_{sqrt(m)}/p1=C(m,2)/(2(s-m+1)). Below that scale the falling-factorial upper bounds make both finite masses vanish, and above it the union bound sends p1 to one.

## originality

FAIL

The conventional birthday bound alone does not cover this claim. The closest distinct indexed unicyclic results do: on a consistently oriented unit-scale pure cycle they give exactly the target hyperplane, its full-rank probability and the complete collision-case classification with condition number sqrt(m). Their statements and proof also supply the injection counts, so the total three-mass law and elementary birthday scaling are implied. This is demonstrable equivalent coverage in the available corpus, not a determination of publication precedence or attribution from the date labels.

## value

FAIL

The distinction between rank survival and good conditioning is useful for this natural benchmark. But the narrow exact invariant contributed by this record is already mechanically determined by the indexed pure-cycle case. The simple window limit and rewriting the same singular-value ratio as the isometric right-QR condition number add no separate structural content beyond that equivalent coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
