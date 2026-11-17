# Independent mathematical audit

## correctness

PASS

For n>=2, 1<=s=k+1<=n, lambda>=0, minimum l1 distance to sparse l1 unit sphere is t-T_s+|T_s-1|. Support-wise triangle inequality is attained by matching signs and adjusting nonnegative masses. Distance to its lambda-ball thickening is max(0,dist-lambda). Largest-s coordinate averaging T_s>=s t/n is sharp exactly for equal moduli (when t>0); the residual convex piecewise-affine function is maximized at t=0 or 1+lambda. This yields max{0,1-lambda,2[1-s(1+lambda)/n]}, saturation threshold, and origin/boundary/equal-modulus extremizers including critical 2s=n. No finite grid is used as proof.

## originality

FAIL

Earlier published cross-polytope skeleton theorem already proves the identical all-rank Schneider index and the complete pointwise l1 nearest-skeleton distance, including the balanced-boundary and origin obstructions and the majorization sufficiency proof. In notation d=n,s=k+1 its formula ||x||_1+1-2min(1,T_s) is exactly the assigned Step 1. Taking the positive part after subtraction of lambda, maximizing under ||x||_1<=1+lambda using T_s>=s||x||_1/n, and checking two affine endpoints yields the submitted quantitative profile and extremizer switch. This is a direct corollary of the earlier proof, not an independent unknown fact.

## value

FAIL

The quantitative Hausdorff profile and maximizer location are mathematically meaningful for cross-polytope smoothing, but in this package they require only the endpoint maximization of the earlier complete pointwise distance lemma and reproduce its exact threshold/phase diagram. The remaining algebra is an immediate textbook consequence, not an independently useful unknown invariant; correctness and appealing formatting do not make the repeated claim valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
