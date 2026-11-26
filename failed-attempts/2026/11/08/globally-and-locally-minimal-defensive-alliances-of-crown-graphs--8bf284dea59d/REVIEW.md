# Independent mathematical audit

## correctness

PASS

For the ordinary closed-neighborhood allowance and degree n−1, a selected vertex requires t=ceil((n−2)/2) selected neighbors. Thus both shores must have size at least t, and any matched selected pair forces both sizes to be at least s=t+1. When the shores are disjoint, sizes at least t suffice. A deletion is possible from any oversized shore in the relevant feasibility regime, reducing the local analysis to disjoint (t,t) pairs and (s,s) pairs. In the latter, a single deletion is possible exactly when the intersection has size at most one. No proper subset can stay in the both-at-least-s regime; global minimality is therefore governed by whether at most one deletion on each shore can remove all shared indices. If k=2 these deletions are forced apart, with exactly two ways to allocate the indices, both producing disjoint (t,t) minima. If k>=3 no proper alliance remains. Choose the intersection and then each exclusive part to obtain the stated labelled binomial factors. Disjoint t-pairs exist since 2t<=n; X=Y of size s witnesses the local maximum in all cases and the global second size precisely when s>=3. The frozen verifier was inspected but not rerun; this decision rests on the unrestricted proof.

## originality

FAIL

The distinct indexed finding 8c1a382222d3 states the same labelled crown census on the same n>=3 domain, including both classification thresholds, both polynomials and the local-only count. Its binomial expression is combinatorially identical; the exact two witnesses for a locally-only set follow immediately from the two known families and their sizes. This is equivalent coverage, not a judgment about who obtained the result first.

## value

FAIL

The exact local/global distinction would be useful in a natural symmetric graph family in isolation, but the substantive classification and invariant are already present in the matching record. The computed spectra and exactly two witnesses are immediate consequences, not a separate valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
