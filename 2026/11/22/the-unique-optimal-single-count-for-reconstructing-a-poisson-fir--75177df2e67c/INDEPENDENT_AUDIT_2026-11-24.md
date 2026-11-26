# Independent mathematical audit

## correctness

PASS

For zero observed events memorylessness gives conditional mean x+1/lambda and variance 1/lambda^2; for k>=1 the first arrival is the minimum of k uniform times and gives mean x/(k+1). Projection in L2 is optimal even without restricting the estimator family. With z=lambda*x, the squared mean average reindexes to exp(-z)(1+2z+zF(z)), where F is the given entire series. Subtracting it from 2 gives normalized risk; differentiating yields R'=-exp(-z)g, g(0+)=1, g'(0+)=0 and g''=(1+z-exp(z))/z^2<0. A negative slope at z=1 supplies a linear negative upper bound for g thereafter. Its sole crossing proves global optimality including x=0; separately the large-z risk tends to 1. For the retained bit the law of total variance subtracts z^2/expm1(z) from 1; the gain derivative has sign of (2-z)exp(z)-2 for z>0, with exactly one positive sign change. Independent differentiation and numerical optimization of a direct posterior-variance mixture and of the bit risk reproduced both times, risks and the stated improvements.

## originality

PASS

The supported distinct claim is the globally optimal time and risk for a single deterministic full cumulative count when estimating the latent first arrival. Neither the standard posterior mean construction nor the binary root considered alone is claimed as new. The strongest neighboring result gives the same binary constant as a limiting design for a different target.

## value

PASS

First-arrival reconstruction is a natural latent-event inference target. The unique scale-free optimal query time and risk solve the full information-budget design problem, not just the textbook fixed-time regression. The separately optimized binary comparison quantifies the benefit of retaining count magnitude instead of only detecting arrival.

The dated certificate retains the supplied scientific assessment, sources and limitations.
