# Independent mathematical audit

## correctness

PASS

For the unrestricted uniform ordered pair, alternating paths have exponential weights 1 for odd size and 1/2 per endpoint class for even size; even graph cycles have weight 1/k including k=2. Removing an ordered tuple of specified components leaves the coefficient ratio b_{n−s}/b_n. Lugo's positive coefficient asymptotic yields the uniform e^{-s/√n}(1+o(1)) ratio for s=O(√n log n), by the square-root expansion and the uniform prefactor. For s≤n/2 the ratio is bounded by C e^{-s/√n}; for s>n/2 even multiplying the exponentially small bound by a fixed polynomial in n does not affect factorial moment sums. Disjoint marked-window mixed factorial moments factorize, and odd/even lattice sums each have half the total weight, giving the three Poisson intensities. The first-moment upper-tail bound gives tightness at the top, the cycle weight 1/k makes large alternating cycles negligible, and the equal-size ordered-path pair bound is O(n^{-1/2}) above each fixed low height cutoff. Since a path yields one permutation cycle of its own size, while an even graph cycle gives two of half its size, this establishes the maximum and top mark conclusions. An independently implemented bounded check covered 60,397 ordered pairs through n=7 and verified 106 exact marked component/coefficient identities; the 60,528 in the frozen narrative counts assertions in its supplied script, not pairs.

## originality

FAIL

The finding is correct but already follows from the published largest-cluster and discrete joint extreme-occupancy estimates of Panagiotou–Ramzews (2022), applied to the Lugo assembly, followed by exact conditional coloring. This is not merely prior coverage of a scalar Gumbel law: their estimates apply to arbitrary distinct sizes in the moving extreme window, which retains the parity information. They give the Poisson joint law for counts on disjoint windows intersected with odd and even sites; the remaining subdivision is independent thinning with known weights. No substantive distinct claim survives in the bound finding.

## value

FAIL

The maximum period is a meaningful observable, and the specialization is correct. But the bound claim adds only a standard application of published local extreme-assembly estimates, a parity Riemann sum and known independent type allocation. It gives no new extremal mechanism, quantitative control beyond what supports that specialization, or independent geometric/dynamical conclusion not accessible from those inputs. The tie and graph-cycle bounds are routine consequences of the same coefficient estimates. No genuinely separate valuable remainder within the assigned claim was established, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
