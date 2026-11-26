# Independent mathematical audit

## correctness

PASS

In the exact scaled map, q(y)=1-lambda/(1+y²) belongs to (0,1) and increases on y>=0. Thus y increases, u decreases, the two limits exist in their extended domains, and coordinatewise ordering is preserved. The strict test V/[1-q(Y+1)]<1 at a state (Y,V) traps height below Y+1 by a first-crossing geometric bound; every finite-height orbit eventually meets the test. For f(y)=1/(1+y²), the excess of the left sum on a step is at most u_k[f(y_k)-f(y_{k+1})]. Summing with u_k<=V gives total velocity loss at most lambda times (integral_Y^infinity f + V f(Y)), valid also for bounded orbits. This is O(1/u_0) from the first post-step state when u_0 is large. For a ballistic orbit it becomes smaller than V at a sufficiently late iterate; this strict finite test establishes openness. Ordering and the two nonempty open phases leave a nonempty closed bounded critical interval of speeds. On a critical tail Y=y_n, the left-sum excess E is between 0 and u_n f(Y), giving u_n=lambda/Y+O(Y^-3). In its Taylor refinement the quadratic term is sum_k Δy_k·(u_k(-f'(y_k))/2), with the second factor lambda*y_k^-4+O(y_k^-6); the cubic remainder sums to O(Y^-5) by integral comparison. Quadrature of y^-4 also costs at most u_n Y^-4=O(Y^-5). Therefore E=lambda/(3Y³)+O(Y^-5), and the arctangent integral adds the -1/(3Y³) term, giving A=lambda(lambda-1)/3 for the cubic velocity coefficient. The squared-height increment is 2lambda+(2A+lambda²)/y_n²+O(y_n^-4). It first yields y_n²=2lambda*n+O(log n), then the harmonic coefficient (5lambda-2)/6 and an absolutely summable O(log n/n²) residual, proving the finite C and all three log signs. Reflection preserves the recurrence. As an independent formal replay, the Laurent ansatz h=lambda/y+A/y³+B/y⁵ in h(y+h(y))=q(y)h(y) gives lambda³-4lambda*A=lambda²-lambda*A at order y^-5 after B cancels; this checks the coefficient but proves no existence. The frozen script was inspected, not run: it shoots to y=100 at lambda=0.4,0.6, checks finitely many residuals, and does not certify a critical initial speed. The coefficient and critical-orbit assertion rest on the analytical bounds, not on finite shooting.

## originality

PASS

The bounded comparison found exact same-map results in other parameter regimes, including an adjacent endpoint with the same leading exponent. They do not cover the critical expansion for the open interval 0<lambda<1 or the cancellation at 2/5. The originating paper is recognized as prior art for the model, not credited here as independently checked full text. The comparison supports the bounded mathematical novelty judgment, not a historical priority claim.

## value

PASS

On a natural fixed-line slice, the result classifies the two open phases and proves a critical escape for every nonnegative starting height. Linear stability of the fixed line cannot determine that global boundary. The controlled next-order term separates opposite signs of secular drift and identifies the exact coupling where the uncorrected squared-height clock converges. It is not a conjecture about arbitrary quadrants or about numerical shooting, and the proof does not rely on asserting a singleton critical set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
