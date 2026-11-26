# Independent mathematical audit

## correctness

PASS

The original theorem is true. For positive B with B-cI compact, infinitely many subthreshold eigenvectors force a sequence of distinct eigenvalues increasing to c; their closed span reduces B and its restriction has norm c without an eigenvector of that eigenvalue. Thus beta(H) forces finite subthreshold multiplicity r. Conversely, for such a positive scalar-plus-compact operator with finite subthreshold multiplicity, every reducing restriction is positive scalar plus compact and still has finite negative index relative to c. If it has a positive compact eigenvalue relative to c, its largest one realizes the norm; otherwise an infinite-dimensional restriction has a c-eigenvector because its negative part is finite rank, and a finite-dimensional restriction always attains. For the estimate let A=cI-B and C=B-D, so A+C=cI-D. For the positive eigenvalues with zeros appended, compact self-adjoint Weyl min–max gives lambda^+_(r+n)(A+C)<=lambda^+_(r+1)(A)+lambda^+_n(C)<=s_n(C), because the first term on the right is zero. Directly, when kappa_(r+n)>0, the span of the first r+n eigenvectors of Q intersects E_B([c,infty)) in dimension at least n, and the quadratic form of C is at least kappa_(r+n) on that intersection. Neither argument assumes commutation. The clipping formula keeps at most m subthreshold eigenvalues and is positive, including when some retained eigenvalues are zero or fewer than m deficits exist. Its compact error has exactly the asserted zero-padded tail. Taking p-th powers termwise is valid also for p<1 and with infinite extended cost. With no fixed budget, dropping finitely many terms cannot change Schatten summability. An infinite Schatten-summable deficit has tail cost tending to zero and cannot have a repair of zero cost since D itself fails beta(H); a finite deficit gives D itself as a zero-cost repair. Read RESULT.md lines 4–39 and the supporting verification material. The recorded 27 finite-matrix tests in verify.py were not rerun and are supplementary; no finite check proves the operator theorem.

## originality

FAIL

The decisive issue is mechanical implication, not lack of access or a priority claim about a later catalogue result. The known positive beta(H)/AN structure identifies the feasible class here by a finite negative index relative to c. The exact proposed noncommuting inequality is the ordinary two-index compact self-adjoint Weyl min–max inequality with one summand's (r+1)-st positive eigenvalue zero. Deleting the spectral tail gives its equality case directly, and the Schatten and zero-distance conclusions are then summation and the same class criterion. This leaves no nonmechanical remainder in the frozen theorem. The checked earlier sources do not need to state the optimization verbatim for this deduction to be decisive.

## value

FAIL

The one-sided repair problem is natural and the exact formula is a useful way to package the spectral data. But the value standard for a narrow invariant excludes a routine consequence: the full noncommuting lower envelope follows by the standard eigenvalue-index substitution, and the equality and Schatten statements follow by ordinary clipping and summation. The frozen record supplies no further invariant, obstruction, or estimate not mechanically supplied by those ingredients. No distinct surviving claim was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
