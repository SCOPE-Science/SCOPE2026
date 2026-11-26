# Independent mathematical audit

## correctness

PASS

Independent calculation: for four ordered velocity times with successive gaps x,y,z, condition on the clock and use Gaussian pairings within unbroken intervals. The adjacent pairing factors and cancels from the connected moment. The two remaining pairings each require no refresh across the full span; subtracting the unconditional covariance products gives the connected moment 2 sigma^4 exp[-a1(x+z)](exp[-a2 y]-exp[-2 a1 y]), with a1=gamma+r and a2=2 gamma+r. It is strictly positive for positive gaps. Integration over the ordered time simplex, with the factor 24, proves strict displacement fourth cumulant at every positive time. After dividing by t the gap integrand acquires the factor (1-(x+y+z)/t)_+; dominated convergence gives 48 sigma^4/a1^2 times (1/a2-1/(2 a1)), exactly the claimed absolute rate. The covariance gives Var(X_t)/t -> 2 sigma^2/a1 and hence the claimed standardized rate. Differentiation gives the respective derivative signs 2 gamma^2-4 gamma r-3 r^2 and 2 gamma^2-r^2, establishing unique interior maxima. Repeating the endpoints of the connected moment and adding the two cross-pair products yields Cov(V_0^2,V_t^2)=2 sigma^4 exp[-a2 t]; the two lag slopes invert as stated. This route does not require interchanging derivatives and renewal limits.

## originality

FAIL

A distinct indexed result covers the same unreset-position process and gives a stronger connected velocity formula, the same strict all-time displacement result, and both exact asymptotic coefficients. The two optima and the proposed velocity-lag inversion follow directly, even though they are not stated as such there. This is demonstrated scientific coverage, not a finding about chronological priority: the covering record has a later date in its index path, and the checked primary fixed-reset paper does not establish this Gaussian-marked result. No separate non-mechanical remainder in the frozen Finding was identified.

## value

PASS

As a scientific statement, this separates the effects of thermal relaxation and velocity refresh in a model whose entire second-order velocity signal cannot do so. Comparing absolute and variance-normalized fourth-order transport also changes the predicted operating point substantially. This physical and inferential motivation is distinct from whether the formulas constitute a new contribution, which fails above.

The dated certificate retains the supplied scientific assessment, sources and limitations.
