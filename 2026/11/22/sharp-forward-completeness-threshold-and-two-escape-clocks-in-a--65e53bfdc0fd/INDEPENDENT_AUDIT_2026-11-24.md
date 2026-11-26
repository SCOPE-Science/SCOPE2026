# Independent mathematical audit

## correctness

PASS

With alpha>0 and arbitrary fixed beta, a hypothesized |z|≤R on a finite horizon bounds both lower coordinates by O(1+R), so the cubic damping at ±R dominates even the xy term. A first-contact barrier followed by compact continuation proves all-data forward existence for gamma<0. For gamma>0, w=sigma*z grows at least as gamma*w^3/2 on the proposed bounded x,y strip. The integrals of dt/dw and w*dt/dw are small for large M and preclude exit through the strip faces, giving finite escape time and finite x,y limits for both signs. At gamma=0 the logarithmic strip is propagated by |dy/dw|≤2/(alpha*w), while integrating (1+log(w/M))/w² prevents x exit. For a separate check of the expansions set v=1/w and G=xy−x−y−beta. In backward remaining time tau, dv/dtau=gamma/v−sigma*alpha−v+sigma*G*v². On the cubic tails this gives v²=2*gamma*tau+(4/3)*sigma*alpha*sqrt(2*gamma)*tau^(3/2)+O(tau²); inversion gives alpha/(3*gamma) in z for either sign. At the quadratic boundary G=O(log(1/v)) and sigma=−1, giving v=alpha*tau−alpha*tau²/2+O(tau³*|log tau|) and the stated negative pole and constant in z. Integrating the resulting z expansions gives the stated velocity and position formulas, including the finite renormalized velocity at gamma=0. Independent regularized-time diagnostics at reciprocal initial curvatures 10^−5 and 10^−6 reproduce convergence to the first clock corrections for both cubic signs and the quadratic tail.

## originality

PASS

The distinct contribution is the global iff completeness threshold with two rigorously realized escape clocks, including their first corrections, for this exact three-dimensional flow. Known local results on the same equation and global results on different equations do not cover this assertion. This is a best-of-knowledge comparison, not a priority certification.

## value

PASS

The theorem separates forward existence from numerically observed bounded attractors in an established model. It answers exactly when one can assume global forward continuation and quantifies a real qualitative change at the boundary: velocity is integrable up to blow-up on either cubic tail but diverges logarithmically on the quadratic tail. The open-set estimates and first corrections make this more than scalar dominant-balance heuristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
