# Independent mathematical audit

## correctness

PASS

On each closed segment the coefficient secant slopes lie in [0,1] away from DC; equivalently the map difference is an average of spectral masks applied to the input difference, with DC fixed. Every mask occurs on an open strict chamber, so the upper operator bound is attained by a small step perturbation. Modulo constants the path first-difference coordinates have l¹ norm; their unit vectors are cuts h_k, giving the exact max_mask,max_cut reduction. In Haar band j, Walsh characters of the specified least significant frequency bit change sign between the halves of each dyadic block and span the 2^j block detail space. A cut has at most one nonzero Haar coefficient per band, bounded by √(ℓ_j)/2. For masked details, l² contraction and the within- and between-block jumps give V≤4∑|a_b|≤4√(2^j/ℓ_j)‖u‖₂, producing the claimed geometric sum. In the random-mask calculation the first edge has expected difference 1/2, and at every other edge both endpoints are nonzero so the deterministic part is zero; the n/2 separating characters give independent signs scaled by 1/n. The exact even Rademacher absolute moment gives the stated mean and Stirling gives √(n/π); the unit-variation impulse makes the mean a lower bound on the maximum, not equal to it. At n=2 the only nontrivial mask is the identity. Fresh integer Walsh-character enumeration checked all masks and cuts at n=4,8 (8×3 and 128×7), giving maxima 3/2, 11/4 and exact impulse means 1, 13/8. Replay with entries χ_r(i)=(-1)^(r·i), summing the products χ_r(i)χ_r(j) over retained frequencies for each projection numerator; take adjacent differences and divide by n. The frozen verifier was not executed.

## originality

PASS

The supported contribution is the ordered-path Walsh bound with the exact Bernoulli-mask impulse law. The general mask and cut reduction is a shared piecewise-linear method, and the Rademacher moment is classical. Neither the available Boolean-cube Walsh comparison nor the ordered-path comparisons for other bases cover these two path-specific conclusions.

## value

PASS

Open-path TV is a natural signal roughness measure. The attained two-input gain shows quantitatively that coordinatewise contraction in Walsh coefficients does not control variation uniformly in signal length. The explicit random-mask benchmark identifies typical impulse amplification on the same scale and gives a rigorous lower bound with exact normalization; the result is not just a pair of small-dimensional maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
