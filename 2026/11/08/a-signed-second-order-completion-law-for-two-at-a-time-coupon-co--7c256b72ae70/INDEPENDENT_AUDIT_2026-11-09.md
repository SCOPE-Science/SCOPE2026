# Independent mathematical audit

## correctness

PASS

Exact inclusion-exclusion for events of k missed types uses q_nk=(n−k)(n−k−1)/[n(n−1)]. For bounded c_n, expanding m log q_nk yields −k(log n+c_n)−k(k+1)(log n+c_n)/(2n)+O(k³log n/n²); multiply C(n,k) expansion to get the two factorial polynomials k(k−1), k(k+1). Truncating at 6log n and bounding tails by λ^k/k! uniformly controls the O(log²n/n²) remainder. Alternating Poisson factorial moments give λ² and λ²−2λ, with unique λ=2 log-term cancellation; at m=floor(n(log n−log2)/2), λ_n=2+O(1/n) gives the stated negative n^-1 term.

## originality

PASS

Best-of-knowledge originality of the exact final claim (not of elementary starting tools). Search matched Poisson approximation for group coupon drawings and general exact inclusion-exclusion. The exact IE expression is classical, but the explicit uniform second-order coefficient and exceptional cancellation are not equivalent to knowing the Poisson limit or error order. From general O(log n/n) approximation one cannot deduce the explicit signed expression or O(log²n/n²) remainder after subtraction. The present expansion requires additional controlled k-dependent Taylor and dominated factorial tails.

## value

PASS

The natural completion window for uniform pair drawings has a correction whose sign reverses and cancels at one explicit parameter. That sharp signed term adds information not supplied by generic Poisson error bounds; it can guide finite-n coverage calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
