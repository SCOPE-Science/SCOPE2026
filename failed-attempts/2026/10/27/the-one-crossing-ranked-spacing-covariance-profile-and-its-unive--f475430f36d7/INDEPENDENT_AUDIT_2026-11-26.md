# Independent mathematical audit

## correctness

PASS

Sorting uniform simplex coordinates preserves constant density on the ordered chamber. The weighted successive differences form a linear bijection onto the simplex, preserving total mass, with constant Jacobian; hence they are again uniform Dirichlet. Expanding Q in these coordinates gives the matrix 1/max(i,j), with row sum 1+H_m−H_j and trace H_m. The exact third moments minus the product of first and second moments give Cov(Y_j,Q)=2(H_m−H_{j−1}−1)/[m(m+1)(m+2)], and summing with the inverse linear map gives the claimed formula. The tail sums decrease while their removed weights are positive; after that all remaining weights are nonpositive with a negative last term. The first tail sum starts at 1/4 for m=2 and increases with m, so there are strict signs at the two ends and at most one boundary zero. The covariances sum to zero because the ranked lengths sum to one. For k/m→α in (0,1) the Riemann sum gives the cubic-scaled profile; testing α on either side of e⁻² and using the finite sign ordering proves the threshold limit. Direct integration at m=2 gives ±1/48. The supplied finite checker was inspected, not run; the proof supplies the unrestricted statements.

## originality

FAIL

The main claim is fully covered by a distinct published catalogue statement, 8821b74b45c3. Its displayed exact formula, proof of the same single switch and its proportional-rank limit cover the substantive results; the remaining cancellation is the identity that the spacings sum to one. The matching record is catalogue-dated Nov. 2, after the assigned Oct. 27 label. This is a decision about demonstrable equivalent coverage and lack of a distinct surviving claim, not a finding that the Nov. 2 entry preceded the frozen work or originated the theorem. Earlier catalogue records independently cover the maximum-rank specialization only.

## value

FAIL

The covariance and universal threshold answer a natural exact question and would be useful as a distinct result. Here the distinct indexed record has the same theorem and the same ordered-simplex and Dirichlet moment proof; the general proportional sequence and cancellation add no independently useful new finding beyond it. No valuable repair remainder was identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
