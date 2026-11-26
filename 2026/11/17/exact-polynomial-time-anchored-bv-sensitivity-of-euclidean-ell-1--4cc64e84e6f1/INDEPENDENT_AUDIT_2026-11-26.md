# Independent mathematical audit

## correctness

PASS

The KKT equations give common soft thresholding. On a strict exterior chamber of support size m and signed indicator q, differentiating the active constraint gives J=diag(|q|)-qq^T/m; m=1 gives zero. Every nonzero signed support occurs strictly: assign active input q_i(rho+R/m) and inactive input zero for rho>0. The interior contributes identity. Continuity and finite affine-cell subdivision bound all two-input ratios, including segments along cell boundaries, and any attaining direction can be scaled down inside a maximizing chamber to give a finite pair. The anchored difference isometry identifies its inverse-coordinate columns with tail indicators, so only those columns of J need be maximized. For fixed (m,k,t), with k the first tail index and t the signed tail sum, each row numerator is |q_i|(m 1_{i>=k}-t q_i). The number of used nonzeros, partial signed tail sum and last symbol are sufficient for every future transition and final feasibility. A prefix induction gives the exact score; O(n^3) triples times n positions times O(n^2) states with three transitions gives O(n^6) arithmetic operations and two O(n^2) layers. Rational comparisons use cross-products. Alternating support at odd indices and the constant tail give n for balanced signs; with odd support choose total sign -1 and last sign -1, so the active values sum to m-1/m and the odd-length final value is 1-1/m. This yields the two stated deficits, hence n-4/n. The upper estimate is the product of the l2-to-l1 norm sqrt(4n-3) of anchored differencing (alternating dual signs) and the l1-to-l2 norm sqrt(n) of cumulative summation, with Euclidean projection nonexpansive in between. A separate integer DP reproduced all values through n=15; exhaustive ternary words and tail columns independently matched through n=8.

## originality

PASS

The distinction is the exact anchored-BV optimization over signed cross-polytope projection chambers, including the polynomial DP and linear lower witnesses, not the threshold rule or chamber Jacobian. The strongest same-projector results use coordinate norms; the closest anchored variation hit uses a radial Euclidean-ball projector. Neither evidenced statement covers this coefficient. This assessment is qualified by the unavailable passages noted below.

## value

PASS

For signal perturbations measured by an anchor and local differences, Hilbert nonexpansivity gives no usable sharp bound. The theorem identifies near-dimension amplification for a canonical real convex projector, supplies concrete finite witnesses, and provides exact rational dimension-by-dimension answers without sign-pattern enumeration. The ordered DP resolves a meaningful sharp stability problem, rather than computing a few examples or giving a faster algorithm for projection itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
