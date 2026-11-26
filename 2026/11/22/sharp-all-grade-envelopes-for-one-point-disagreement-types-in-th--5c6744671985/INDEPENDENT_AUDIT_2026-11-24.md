# Independent mathematical audit

## correctness

PASS

In the generic two-order Fraïssé limit, any pair of gaps is realized by the one-point extension property, and ultrahomogeneity makes any two realizations of the same gap pair have the same type over the parameters. For a grade-k pair, h=|A_i∩B_j| obeys max(0,i+j-n)<=h<=min(i,j) and 2h=i+j-k. Thus (u,v)=((i+j-k)/2,(i-j+k)/2) is an integer pair exactly in the claimed candidate rectangle; the inverse always gives legal gaps. For the folded list, the first and third clauses enumerate the parity of k in the disjoint intervals [1,k] and [k+1,n], and the other two enumerate the opposite parity in [1,n-k] and [n-k+1,n]. At a candidate cell, an odd position fails the intersection test exactly when t<=k-i, with k-i<=j, and every odd t>k is counted since j-k<=i. The even positions counted are exactly the positive evens up to i-k (if positive), since i-k<=min(j,n-k) and the far even fold gives a value at least 2n-k+1-j>i. Hence h=ceil(j/2)+floor((i-k)/2)=u by the parity constraint. For the lower bound with 2k<=n, the row walk starts at i and ends at n-i, changing by ±1. Each of the first and last k+1 rows contributes, with two different endpoints in the shared row when n=2k>=2. Reversing the second order complements grade, giving the opposite lower bound. The reverse permutation has d=min(i+j,2n-i-j) and the identity has d=|i-j|, attaining the correct lower sides including k=0,n and n=1. No exhaustion of all maximizing permutations is required or claimed.

## originality

PASS

The supported distinct contribution is the sharp pointwise lower and upper envelopes at all grades with a grade-specific constructor, not the two-gap encoding, the previously catalogued upper bounds at grades one and two, or the exact average. Distinct 2026-11-22 records were compared without presuming their order or priority.

## value

PASS

Grading the one-point type count by its actual order disagreements refines the otherwise constant (n+1)^2 count. Exact envelopes and witnesses show that the central-grade count varies from order n to order n^2 as the parameter pattern changes, a genuinely quantitative feature not determined by the known mean or small-grade bounds. The explicit witness saturates every admissible cell at the chosen grade, rather than joining isolated finite examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
