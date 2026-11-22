# Scientific review: exact planar Kaczmarz row-ordering law

## Correctness (C): PASS

The projection identity \(P_j=v_jv_j^{\mathsf T}\) telescopes every ordered sweep into a rank-one outer product multiplied by consecutive tangent inner products. Its norm therefore has a **literal zero factor exactly at consecutive orthogonal rows**. Even regular frames have a perfect matching of orthogonal row pairs. For odd frames, equality in the product lower bound reduces to Hamiltonian paths of a modular single cycle, yielding exactly \(2n\) optimizers. Compression of specified matched pairs gives exact binomial moments and inversion gives the full random-reshuffling law. A controlled factorial-moment expansion proves the stated Poisson and \(1/n\) asymptotics; conditioning on independent row draws proves its exact comparison. No numerical experiment is promoted to an infinite proof. Finite checker: 87320 assertions for sizes two through eight; it does not exhaust all sizes.

## Originality (O): PASS, with residual publication risk

**Direct identical geometry:** Oswald–Zhou (arXiv:1510.04727, §3, equation (18)) previously use the exact even regular planar row family and prove slow cyclic-order convergence. Neither their stated theorem nor its proof computes the zero-operator distribution over uniform permutations, the sharp reshuffle-versus-IID probability, nor the full global optimum set for all parity classes. This exact frame and cyclic example are therefore credited, not claimed as discoveries. Strohmer–Vershynin (arXiv:math/0702226) establish independent-draw mean-square theory but not random permutation exact termination. Wallace–Sekmen discuss projection-angle dependence; Diaconis–Evans–Graham study a different consecutive-label permutation statistic, not the fixed disjoint orthogonality matching. Published regular-simplex one-epoch and equiangular three-row reshuffling theorems use different frame geometries or objectives; the planar optimal-IID sampling theorem concerns rate, not zero one-sweep probability. Dax discusses orthogonality-based ordering, so that heuristic is known. Inclusion–exclusion for disjoint matching adjacency is elementary prior combinatorics; novelty is bounded to the exact solver-specific classification and comparisons. Equivalent unindexed conclusions may exist, and independent priority verification is needed.

## Value (V): PASS

This is a natural complete classification for a canonical tight overdetermined planar test frame, not an arbitrarily chosen numerical slice. It shows that **exact arithmetic finite termination by a single complete random reshuffle has positive limiting probability for even row counts but is impossible for odd ones**, while giving the full finite distribution, the exact gain over IID draws at matched computational cost, and every globally optimal deterministic ordering (including the odd-size exponentially small optimal norm). These separate exact-termination reliability from mean-square-rate guarantees, of direct interest in Kaczmarz row ordering and randomized iterative methods. Its utility is a precise benchmark, not a universal new solver or a finite-precision guarantee.

## Limitations and publication risks

The event is nonrobust to perturbations of row angles and floating-point roundoff. Other frames, dynamics under multiple independently randomized epochs and finite-precision thresholds are not covered. The matching-adjacency law may be available in classical combinatorial literature; any prior application to identical Kaczmarz conditions would change the originality assessment. Independent peer or mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
