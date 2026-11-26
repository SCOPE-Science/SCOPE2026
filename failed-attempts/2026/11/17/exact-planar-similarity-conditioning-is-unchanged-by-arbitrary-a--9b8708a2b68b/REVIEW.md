# Independent mathematical audit

## correctness

PASS

Reconstructed all three similarity classes. A nonscalar repeated-eigenvalue matrix has rank-one square-zero part with range equal to kernel; an orthonormal basis puts this part in the form with single positive entry equal to its norm. In the distinct-eigenvalue case the normalized involution Q satisfies QQ*=(Q*Q)^(-1); for norm a>1 it takes the right singular line of singular value a to the orthogonal right singular line of singular value 1/a. Fixing the phase gives the canonical entries a and 1/a. For a=1, Q is a selfadjoint unitary involution with eigenvalues ±1, and the sum/difference basis gives the same form. Thus the diagonal map diag(b/a,1) in the A-to-B orientation intertwines both canonical families with condition number max(a/b,b/a). Apply the affine polynomial defining the nilpotent or involution to any amplified intertwiner and use norm preservation under tensoring with a nonzero Hilbert identity to obtain the reverse bound in both directions. Tensoring the optimal small intertwiner gives equality and attainment for arbitrary nonzero K, including nonseparable K. The scalar case is identity; choosing involutions of norms 1 and t with spectrum {±1} gives the envelope theta_(2,q)(t)=t, including t=1. Replay: these identities and RESULT.md Steps 1–5; verify.py and VERIFICATION.md inspected, not executed. The finite assertions are not evidence for arbitrary amplification on their own.

## originality

FAIL

Demonstrably covered, not mathematically false. Distinct indexed Resultary record e8fd5affa661 explicitly reconstructs both exact norm-ratio formulas and finite-multiplicity cancellation as a special case of a broader simultaneous theorem. The single-pair proof's lower and upper bounds apply unchanged with an arbitrary nonzero Hilbert identity. The finite-q envelope is an immediate consequence of those same formulas and the displayed canonical family. The equal record dates do not resolve historical priority, but do not remove demonstrable equivalent and stronger indexed coverage.

## value

FAIL

The planar threshold is a mathematically natural benchmark for the broader cancellation problem, and the exact formulas are useful as background. The proposed standalone advance does not add a distinct exact fact to the strongest identified result: its arbitrary Hilbert multiplicity follows directly from the same polynomial norm bound and tensor product upper bound, and the envelope uses the already available canonical matrices. No substantive surviving remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
