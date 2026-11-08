# Radius-order comparison and smooth sharpness for exact ball-proximal optimization

## Finding

The exact Euclidean ball-proximal method admits a coordinatewise comparison principle on orthogonally separable strictly convex objectives. Larger radii, even when chosen independently at every iteration, produce no larger absolute coordinates or objective gaps than smaller radii from the same initial point. For a constant radius, this gives a dimension-explicit termination bound, and smooth strongly convex diagonal quadratics attain that bound exactly.

Precisely, under the conditions below, if two strictly positive radius sequences obey \(r_k\le R_k\) for all \(k\), and \(x^r_k,x^R_k\) denote their respective exact ball-proximal iterates from the same initial point, then for every \(k\) and coordinate \(i\),
\[
\left|\left(Q^\top(x^R_k-x_*)\right)_i\right|
\le
\left|\left(Q^\top(x^r_k-x_*)\right)_i\right|.
\]
Consequently \(f(x^R_k)\le f(x^r_k)\) and \(\|x^R_k-x_*\|_2\le\|x^r_k-x_*\|_2\). A constant radius \(t>0\) reaches the minimizer in at most
\[
N_t\le\left\lceil\frac{\|Q^\top(x_0-x_*)\|_1}{t}\right\rceil
\le\left\lceil\frac{\sqrt d\,\|x_0-x_*\|_2}{t}\right\rceil
\]
steps if \(x_0\ne x_*\), and in zero steps otherwise. For every integer \(d\ge2\), there exists a smooth strongly convex quadratic in dimension \(d\), starting a Euclidean distance \(\sqrt d\) from its minimizer, whose exact constant-radius-one trajectory takes **exactly \(d\) steps**. Hence the displayed dimension factor cannot be reduced uniformly even within smooth strongly convex quadratics.

## Assumptions and scope

Let \(d\ge1\), let \(Q\) be a real orthogonal \(d\times d\) matrix and \(x_*\in\mathbb R^d\). Suppose
\[
f(x)=f(x_*)+\sum_{i=1}^d\phi_i\!\left(\left|(Q^\top(x-x_*))_i\right|\right),
\]
where every \(\phi_i:[0,\infty)\to[0,\infty)\) is continuously differentiable and strictly convex, \(\phi_i(0)=\phi_i'(0)=0\), and \(\phi_i'(s)>0\) for \(s>0\). In particular \(x_*\) is the unique minimizer. The iteration at a strictly positive radius \(t\) solves the **entire ball subproblem exactly**:
\[
B_t(x)=\underset{\|u-x\|_2\le t}{\operatorname{argmin}}\ f(u).
\]
Strict convexity makes the output unique. At and after reaching \(x_*\), iterates remain there. This is an exact-oracle theorem, not an implementation-cost statement and not a theorem for approximate subproblems or arbitrary coupled convex functions.

## Proof

**1. Scalarization and implicit equations.** By orthogonal invariance of the ball and evenness in each transformed coordinate, it suffices to work with a nonnegative vector \(w\in[0,\infty)^d\); the signs of nonzero transformed coordinates are preserved. If \(\|w\|_2\le t\), the global minimum \(0\) lies in the ball and is selected. Otherwise the ball constraint is active. The KKT conditions, with a positive multiplier and strictly convex objective, are necessary and sufficient, yielding a unique \(\lambda>0\) and nonnegative output \(p\) satisfying
\[
p_i+\lambda\phi_i'(p_i)=w_i,\qquad
\sum_{i=1}^d(w_i-p_i)^2=t^2.
\]
For a fixed \(\lambda>0\), write \(p_i=P_i(w_i,\lambda)\). The map \(u\mapsto u+\lambda\phi_i'(u)\) is strictly increasing from zero to infinity. Thus \(P_i\) is nondecreasing in \(w_i\) and nonincreasing in \(\lambda\). In addition its displacement \(\delta_i(w_i,\lambda)=w_i-P_i(w_i,\lambda)\) is nondecreasing in both arguments: for the first, if \(w'_i\ge w_i\), then \(0\le P_i(w'_i,\lambda)-P_i(w_i,\lambda)\le w'_i-w_i\), directly from the monotonicity of \(\phi_i'\); for the second, \(P_i\) decreases with \(\lambda\). At least one coordinate is positive outside the terminal ball, and the aggregate displacement \(D(w,\lambda)=(\sum_i\delta_i(w_i,\lambda)^2)^{1/2}\) increases continuously from zero to \(\|w\|_2\) as \(\lambda\) increases from zero to infinity. The required multiplier is therefore unique.

**2. Radius and input comparison.** For nonnegative \(w\le v\) componentwise, the displacement maps satisfy \(D(w,\lambda)\le D(v,\lambda)\) for every fixed multiplier. If neither is terminal at radius \(t\), the multipliers giving displacement \(t\) satisfy \(\lambda(w,t)\ge\lambda(v,t)\). Therefore, coordinate by coordinate,
\[
P_i(w_i,\lambda(w,t))\le
P_i(v_i,\lambda(v,t)).
\]
If the smaller input is terminal, its output is zero; if the larger input is terminal, both inputs are terminal. This proves monotonicity of \(B_t\) in the nonnegative orthant. For the same input, the multiplier increases with the radius, so \(B_T(w)\le B_t(w)\) coordinatewise whenever \(T\ge t\). Iterating these two comparisons gives the stated dominance for arbitrary coordinatewise ordered positive radius sequences. Strictly increasing \(\phi_i\) also implies objective dominance. Any earlier termination of the small-radius trajectory forces both trajectories to be at the minimizer; hence a larger-radius trajectory cannot require more steps whenever the trajectories terminate.

**3. Finite-length budget.** Every nonterminal step stays in the same nonnegative orthant in transformed coordinates, changes coordinates only toward zero, and has displacement exactly \(t\). Thus
\[
\|w^k\|_1-\|w^{k+1}\|_1
=\|w^k-w^{k+1}\|_1
\ge\|w^k-w^{k+1}\|_2=t.
\]
If the first minimizer occurs at step \(N_t\ge1\), the first \(N_t-1\) steps are nonterminal and the preceding iterate is nonzero. Consequently \((N_t-1)t<\|w^0\|_1\), proving \(N_t\le\lceil\|w^0\|_1/t\rceil\), including the exact-integer boundary. The Cauchy–Schwarz inequality yields the Euclidean expression. For unequal radii the same argument gives \(\sum_{k=0}^{N-2}t_k<\|w^0\|_1\) whenever the first arrival occurs at step \(N\).

**4. Smooth sharpness, with no limiting numerical argument.** Fix \(d\ge2\). For \(0<\varepsilon<1\), let
\[
f_\varepsilon(x)=\frac12\sum_{i=1}^d\varepsilon^{i-d}x_i^2,
\qquad x^0=(1,\ldots,1),\qquad t=1.
\]
This objective has a positive-definite diagonal Hessian and is infinitely differentiable. Let \(x^k(\varepsilon)\) denote its exact ball-proximal iterate. We prove inductively that, for each fixed \(0\le k\le d-1\),
\[
\lim_{\varepsilon\downarrow0}x^k(\varepsilon)
=(\underbrace{0,\ldots,0}_{k},\underbrace{1,\ldots,1}_{d-k})=:v_k.
\]
The base case is immediate. Suppose it holds for \(k\le d-2\), and put \(S=\sum_{i\le k}(x_i^k)^2\), which tends to zero. Eventually \(S<1\), and the current norm tends to \(\sqrt{d-k}>1\); the next step is thus nonterminal and has length exactly one. Construct a feasible comparison point \(y\): set its first \(k\) coordinates to zero, its \((k+1)\)-st coordinate to \(\max\{0,x^k_{k+1}-\sqrt{1-S}\}\), and its remaining coordinates equal to \(x_i^k\). Its distance to \(x^k\) does not exceed one. Dividing its objective by \(\varepsilon^{k+1-d}\), we obtain
\[
\frac{2f_\varepsilon(y)}{\varepsilon^{k+1-d}}
=y_{k+1}^2+
\sum_{i=k+2}^{d}\varepsilon^{i-k-1}(x_i^k)^2
\longrightarrow0.
\]
Optimality of the actual next iterate gives the same vanishing upper bound for its nonnegative rescaled objective. Since the quadratic coefficients of coordinates \(1,\ldots,k+1\) are at least \(\varepsilon^{k+1-d}\), all these output coordinates tend to zero. Their squared displacement tends to one, contributed entirely by the previous \((k+1)\)-st coordinate. Because the full displacement has squared norm one, the displacement in the remaining coordinates tends to zero, leaving their values tending to one. This proves the induction. In particular \(\|x^k(\varepsilon)\|_2\to\sqrt{d-k}>1\) for every \(k\le d-2\). A single sufficiently small \(\varepsilon>0\) therefore makes each of the first \(d-1\) iterates nonterminal. Thus \(N_1\ge d\), while the proven \(\ell_1\) bound gives \(N_1\le\lceil d\rceil=d\). Hence \(N_1=d\) exactly for this smooth strongly convex quadratic. The proof is existential with an explicit parameter family; it does not claim a universal numerical cutoff on \(\varepsilon\) as a function of \(d\).

## Verification

The proof supplies the infinite-family and all-radius conclusions. The standalone Python file `verify.py` independently solves quadratic ball subproblems using high-precision bisection of their scalar KKT multiplier. It checks 960 ordered-radius trajectory comparisons on independently generated diagonal positive-definite objectives and exhibits exact step counts equal to the dimension in dimensions \(2\) through \(7\) at concrete parameter choices. Execute `python verify.py` in the package directory; expected output begins `VERIFY_OK`. These finite tests are supplementary and do not certify the infinite claims or historical originality.

## Relationship to prior work

Richtárik and Li, *A Sharper Theory of Ball-Proximal Optimization: Convergence and Radius Selection* (arXiv:2609.35147v1, first public September 28, 2026), develop general convex ball-proximal bounds, study radius selection, show that increased radii need not reduce iterations in general, and present a polyhedral sharpness construction. Their general results do not state the present coordinatewise radius-comparison principle for orthogonally separable objectives or the smooth positive-definite quadratic dimension-attainment construction. The geometric convex-optimization starting point is credited to Gruntkowska, Li, Rane and Richtárik, *The Ball-Proximal ("Broximal") Point Method* (arXiv:2502.02002), which already proves finite termination and general distance bounds. The present comparison is an additional structural statement, not a claimed improvement to the general-case theory or a refutation of its nonmonotone-radius example. Carmon and coauthors' *Acceleration with a Ball Optimization Oracle* (arXiv:2003.08078) concerns accelerated ball-oracle complexity, not this exact basic-iteration comparison.

## Limitations

The comparison requires the objective to be separable after an orthogonal change of coordinates and each component to have its minimum at zero. It does not extend here to general coupled convex objectives, nonsmooth piecewise-affine objectives, nonorthogonal separations, nonconvex objectives, inexact ball solves, or the cost of computing the oracle. The smooth sharpness construction can have arbitrarily poor Hessian conditioning as \(\varepsilon\) tends to zero. The literature comparison is bounded; mathematical priority is not independently established by an absence of search hits.

## References

1. Peter Richtárik and Hanmin Li, *A Sharper Theory of Ball-Proximal Optimization: Convergence and Radius Selection*, arXiv:2609.35147v1 (2026). https://arxiv.org/abs/2609.35147
2. Kaja Gruntkowska, Hanmin Li, Aadi Rane and Peter Richtárik, *The Ball-Proximal (=“Broximal”) Point Method: a New Algorithm, Convergence Theory, and Applications*, arXiv:2502.02002 (2025). https://arxiv.org/abs/2502.02002
3. Yair Carmon and collaborators, *Acceleration with a Ball Optimization Oracle*, arXiv:2003.08078 (2020). https://arxiv.org/abs/2003.08078
