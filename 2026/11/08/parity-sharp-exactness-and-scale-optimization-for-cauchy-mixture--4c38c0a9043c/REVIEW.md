# Independent mathematical audit

## correctness

PASS

The cotangent substitution with the absolute Jacobian gives the stated continuous value at the zero-phase node. The Poisson kernel with r=(a-L)/(a+L) has an absolutely convergent Fourier series, and roots-of-unity averaging leaves exactly the n-fold aliases. The odd mixture is strictly decreasing with the stated endpoint limits and opposite signs about 1 at the extreme component scales, including n=1. For even n, each excess is nonnegative and not all can vanish. Differentiating in log L gives the factorization in RESULT.md lines 101–113: the bracket is bounded below by 1 and the only possible zero of a component's second derivative is its own scale, for n>2. Strict increase of the derivative and its endpoint signs give a unique interior minimizer. The n=2 formula follows by minimizing (A/L+BL)/2. For large counts, away from the geometric midpoint the largest endpoint ratio dominates (odd) or loses to the midpoint comparison (even). In a fixed small midpoint neighborhood the intermediate ratios are bounded by eta*rho for eta<1, whereas the larger endpoint ratio is at least rho. Dividing the root or derivative equation by the larger endpoint power first bounds the ratio of endpoint powers above and below; this gives x=log(L/L0)=O(1/n). The derivative of log(u/v) at x=0 is (1-rho^2)/rho=4L0/(a_+-a_-); the remaining smooth factors in the even derivative produce at most O(1/n) in the log balance. This yields the claimed O(n^-2) remainder and the two equal leading endpoint contributions to the even bias. In the balanced odd case, u>v at the root and adding two nodes decreases the positive term relative to the negative term strictly. The exact root equation n log(u/v)=log(1+u^n)-log(1-v^n), with x=O(n^-2), gives the stated exponentially small displacement. Balanced even symmetry gives the exact minimizer and bias. The support script and verification report were inspected but not executed; the all-count proof, not the reported finite tests, is decisive.

## originality

PASS

On the inspected evidence, the distinct result is the global parity-dependent scale-selection law for a nontrivial positive finite centered mixture: all-count optimization, its sharp extremal-mass asymptotics, and balanced two-scale monotonicity. The change of variables, aliasing identity, and matched single-component exactness are not credited as new.

## value

PASS

The scale is a natural free parameter of the transformed quadrature. Knowing a globally unique normalization-exact choice for odd counts, a globally unique positive-bias minimum for even counts, and how its true error depends on extremal component scales and masses gives actionable information not supplied by exponential convergence at a prescribed scale. The monotone balanced odd limit quantifies a different, much smaller displacement; these are complete structural statements about the stated objective, not about quadrature for general test functions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
