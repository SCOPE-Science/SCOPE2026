# Independent mathematical audit

## correctness

PASS

The word w_{i,j} produces one weight-one deletion descendant iff j=i+1 and two otherwise. Disjoint shadows give a+2b<=n-1 and adjacent pairs cannot have consecutive starts, so a<=ceil((n-1)/2); hence |C|<=floor((3n-2)/4). The displayed periodic supports (2r,2r+1) and (4r+1,4r+4) have distinct weight-one outputs, and zero-deletion weight-two outputs never collide, including boundaries. Independently rebuilt deletion-shadow sets through n=10 and verified construction size and disjointness. These finite tests corroborate the general combinatorial upper/lower proof.

## originality

FAIL

FAIL: Direct same-channel, same-weight, same-quantifier published results on 2026-10-12 and 2026-10-18 establish the *identical* formula floor((3n-2)/4) for all n>=2 and reproduce the identical explicit supports and essentially identical two-part proof. The alternate expression n-1-floor((n+1)/4) is algebraically equal. The relevant earlier RESULT.md theorem and proof passages were read; this is decisive complete prior mathematical coverage, not a failed search.

## value

FAIL

FAIL: Although exact maximum code sizes are a natural coding-theoretic invariant, the submitted claim and construction are already completely established in earlier published records and add no distinct new invariant, structural classification, or substantive improvement. Reproducing the same proof/verifier does not constitute a new valuable contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
