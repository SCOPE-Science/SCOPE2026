# Independent mathematical audit

## correctness

PASS

PASS: In the unique decomposition w=1^a0 0 1^a1 ... 0 1^at, a one after j zeros accounts for C(j,2) 001-subsequences. A fixed positive-weight profile fixes J zero positions and ell marked ones; precisely three independent nonnegative free slots a0,a1,h remain. Therefore GF exactly P_k/(1-z)^3. The all-ones-at-gap-2 profile has unique largest core k+2; any J>=3 has length at most k+1 because ell<=k-C(J,2)+1. Thus n>=k has exact quadratic binomial extrapolation (missing terms at d=n+1,n+2 vanish), whereas at k-1 the degree k+2 term adds exactly 1. This reconstructs quantifiers and boundary cases; k=0 is explicitly excluded. Finite independently implemented direct counting checks n<=11, k<=7 agree, but the bijection supplies the all-k proof.

## originality

FAIL

FAIL: The published 2026-11-02 general two-run theorem establishes the EXACT all-length rational GF for 0^a1^b, all attainable k. At a=2,b=1, its canonical profile of ones after the second zero is bijective to the current triangular-partition profile, with q=ell, t_q=J and h=q+t_q; its numerator is exactly P_k, not merely same eventual degree. The remaining n=k onset and discrepancy at k-1 follow mechanically by bounding the maximum monomial degree of this already-known numerator. Absence of an explicitly printed threshold in that earlier statement is not new mathematical content independent of the stronger exact enumeration. The earlier general theorem is more encompassing, so this full final claim is covered by implication.

## value

FAIL

FAIL as a purported new contribution: the all-length distribution and partition profile were already provided for the full two-run class. Extracting the special parameter a=2,b=1 and the routine maximal-core threshold is not a distinct motivated gap after the exact all-k numerator is known. Correct and reproducible computations do not rescue a previously implied specialization; preserve entire source package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
