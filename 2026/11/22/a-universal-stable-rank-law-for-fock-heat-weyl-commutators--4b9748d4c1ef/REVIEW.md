# Independent mathematical audit

## correctness

PASS

The trace identity and both limits hold in the stated Gaussian normalization, for fixed d and fixed nonzero a. Unitary rotation reduces to a positive real displacement in one coordinate, with a tensor dilation of norm one in the others. Independently, in one coordinate D_r W_a D_r W_a* has multiplier exp(r(1-r)z conjugate(a) - (1-r)|a|²) and affine symbol r²z+(1-r)a. Integrating its kernel on the diagonal gives the cross trace (1-r²)^(-1) exp(-|a|²(1-r)/(1+r)). For t=1-r, the skew generator is conjugate(a) M_z - a ∂_z before rotation (the formula in the proof agrees after its real-displacement reduction). Its commutator with D_r is self-adjoint and has adjacent weights of magnitude |a|t√(n+1)r^n. The maximum weight times two bounds the unitary conjugation difference; finite-rank truncations justify integration since the boundary error is O(√N r^N) at fixed r. The maximizing n is asymptotic to 1/(2t); the absolute difference of the two coherent expectations at a/(|a|√(2t)) matches the upper bound. Squaring and dividing the two expansions gives e/2^(d+1). The analytic checks are decisive; the archived finite sampler was inspected, not executed. The excluded a=0 case has zero commutator and undefined squared-norm ratio.

## originality

PASS

Pass for the sharp operator-norm coefficient and the resulting stable rank of the weighted Weyl heat difference, not for the displaced-thermal overlap alone. No inspected stronger theorem gives both spectral norms for this weighted difference. The closest same-day independent catalogue entry gives a distinct unweighted operator boundary layer and is not dismissed on chronological grounds.

## value

PASS

A canonical translation versus smoothing problem has vanishing operator norm but nonvanishing or diverging Hilbert–Schmidt mass. The sharp norm, combined with the available trace scale, gives the actual effective dimension e/(2^(d+1)t^d), rather than only an order estimate. The coefficient separates this weighted two-sided problem from the nearby affine boundary layer and is useful for quantifying spectral mass; value is not assigned to routine Gaussian overlap recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
