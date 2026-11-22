# Unique two-time observation design for Brownian quadratic path energy

## Finding

Let \(B\) be standard Brownian motion on \([0,1]\), and let \(Q=\int_0^1 B(t)^2\,dt\). For two deterministic, exact, possibly repeated observations at \(0\leq a\leq b\leq1\), estimate \(Q\) by its conditional mean \(\widehat Q_{a,b}=\mathbb E[Q\mid B(a),B(b)]\). The integrated Bayes squared risk
\[
\mathcal R(a,b)=\mathbb E[(Q-\widehat Q_{a,b})^2]
\]
has **exactly one ordered global minimizer**, and that minimizer is interior:
\[
(a_*,b_*)=(0.518444606516422\ldots,\ 0.852334484860895\ldots),
\qquad \mathcal R_* = 0.019658529715848\ldots.
\]

The first coordinate \(a_*\) is the unique zero of
\[
R(a)=303872a^6+748224a^5-2700756a^4+1719468a^3+21627a^2-139968a-11664
\]
in \((0.518,0.519)\). Define
\[
A(a)=4272a^5-4346a^4+389a^3+432a^2+36a,
\]
\[
D(a)=6288a^4-5774a^3-54a^2+432a+36.
\]
Then \(b_*=a_*-A(a_*)/D(a_*)\). Thus the two optimal times are specified exactly by rational polynomials and an isolating interval, not by numerical optimization alone.

For contrast, the two noiseless locations minimizing the posterior variance of the **linear** Brownian area \(\int_0^1 B(t)\,dt\) are \((2/5,4/5)\). Using those sites for the quadratic energy yields risk exactly \(131/5625=0.023288888\ldots\), so the goal-specific design reduces mean-square risk by approximately \(15.588\%\). The nonlinear goal also differs from the best one-observation location \(3/4\).

## Assumptions and scope

The Brownian motion is real, has \(B(0)=0\), independent centered Gaussian increments, and covariance \(\mathbb E[B(s)B(t)]=\min\{s,t\}\). Observations are deterministic and noiseless. Both sample times may be anywhere in the compact ordered simplex \(0\le a\le b\le1\), including coincident samples and the endpoints. All estimators are square-integrable functions of the observations; conditional expectation uniquely minimizes risk in that class, up to almost-sure equivalence. All risk values are unconditional over Brownian paths. The theorem is for exactly two observation channels, with possible duplication, and does not assert an optimal design for noisy or adaptive observations.

## Proof

**1. Reduction to a two-dimensional Gaussian quadratic.** First suppose \(0<a<b\le1\). Write \(x=a\), \(y=b-a\), and \(c=1-a-y\). The independent standard-normal coordinates
\[
\xi_1=B(a)/\sqrt{x},\qquad \xi_2=(B(b)-B(a))/\sqrt y
\]
parametrize the conditional mean path \(m(t)=\mathbb E[B(t)\mid B(a),B(b)]=\phi_1(t)\xi_1+\phi_2(t)\xi_2\). The deterministic piecewise-linear functions are
\[
\phi_1(t)=\begin{cases}t/\sqrt x,&0\le t\le x,\\\sqrt x,&x\le t\le1,\end{cases}\qquad
\phi_2(t)=\begin{cases}0,&0\le t\le x,\\(t-x)/\sqrt y,&x\le t\le x+y,\\\sqrt y,&x+y\le t\le1.\end{cases}
\]
The residual Gaussian bridge process \(B-m\) is independent of \((\xi_1,\xi_2)\), and its covariance is observation-independent. Hence the conditional expectation of \(Q\) differs from \(\int_0^1m(t)^2dt\) by a deterministic constant. Let \(M_{ij}=\int_0^1\phi_i(t)\phi_j(t)\,dt\). Direct integration gives
\[
M_{11}=x-\frac{2x^2}{3},\quad M_{22}=y\left(c+\frac y3\right),\quad
M_{12}=\sqrt{xy}\left(c+\frac y2\right).
\]
Since \(\xi\) is standard normal, \(\operatorname{Var}(\xi^TM\xi)=2\operatorname{tr}(M^2)\). Isserlis' formula also yields \(\operatorname{Var}(Q)=2\int_0^1\int_0^1\min(s,t)^2dsdt=1/3\). The law of total variance proves
\[
\mathcal R(x,x+y)=\frac13-2F(x,y),
\]
where
\[
F(x,y)=\left(x-\frac{2x^2}{3}\right)^2+y^2\left(1-x-\frac{2y}{3}\right)^2
+2xy\left(1-x-\frac y2\right)^2.
\]
This polynomial extends continuously to all boundaries and equals the correct explained variance there, including repeated observations. Therefore it suffices to maximize \(F\) on \(x\ge0\), \(y\ge0\), \(x+y\le1\).

**2. Elimination of every boundary maximizer.** A feasible interior witness \((x,y)=(1/2,1/3)\) has \(F=457/2916\). On either coordinate boundary \(x=0\) or \(y=0\), \(F(z)=z^2(1-2z/3)^2\), \(0\le z\le1\), whose maximum is \(9/64<457/2916\), attained at \(z=3/4\). On the remaining boundary \(y=1-x\),
\[
F\bigl(x,1-x\bigr)=G(x)=\frac{x^4-5x^3+3x^2+x+2}{18}.
\]
The polynomial \(457/2916-G(x)\) has **all 13 Bernstein coefficients of degree 12 strictly positive** on \([0,1]\). This is an exact rational certificate that it is strictly positive throughout the interval, including the endpoints. Coefficients are recomputed without rounding by the embedded verifier. Thus every global maximizer is interior and stationary.

**3. Exact classification of stationary points.** Elimination of \(y\) from the two equations \(F_x=F_y=0\) gives
\[
\operatorname{Res}_y(F_x,F_y)=\frac{x^3}{2125764}R(x).
\]
The degree-one subresultant is \((A(x)+D(x)y)/2916\), so every interior stationary point has \(R(x)=0\) and \(A(x)+D(x)y=0\). Descartes' sign rule bounds the number of positive real roots of \(R\), counted with multiplicity, by three. Direct exact-rational sign comparisons at the three disjoint pairs
\[
(518/1000,519/1000),\quad(735/1000,736/1000),\quad(1208/1000,1209/1000)
\]
prove at least three distinct positive roots, hence exactly three. Only the first two lie below one.

On each of the first two rational intervals, exact Bernstein interval certificates give \(A(x)>0\) and \(D(x)<0\). For the first interval, they also give \(-A(x)-(1-x)D(x)>0\); consequently \(y=-A(x)/D(x)\) satisfies \(0<y<1-x\). For the second interval, the same difference is strictly negative, yielding \(y>1-x\) and ruling out feasibility. No other stationary point is feasible. The compactness of the simplex and the strict boundary comparison therefore force the unique feasible stationary point to be the unique global maximum.

**4. Exact numerical characterization.** Isolate the first positive root of \(R\) in the first rational interval, set \(y=-A/D\), and evaluate \(1/3-2F\). This yields the locations and risk above. Since observations are unordered physically, reversing \(a_*\) and \(b_*\) is the same design; uniqueness is stated for the ordered pair.

**5. Linear-target comparator.** For \(L=\int_0^1 B(t)\,dt\), conditioned on \(B(a),B(b)\), its posterior variance is the sum of bridge-area variances on \([0,a]\), \([a,b]\) and a terminal Brownian segment; direct covariance integration yields \(a^3/12+(b-a)^3/12+(1-b)^3/3\). Minimizing over the three nonnegative lengths gives ratios \(a:(b-a):(1-b)=2:2:1\), hence \((a,b)=(2/5,4/5)\). Substitution into the quadratic energy criterion gives the stated exact risk \(131/5625\).

## Verification

The included `verify.py` (SymPy only) recomputes both stationary polynomials, their resultant and subresultant, the three exact root signs, Descartes' variation count, the degree-12 strict Bernstein boundary certificate, and the **whole-interval** Bernstein sign certificates required to exclude the second stationary root. It verifies the exact algebraic comparisons \(457/2916\), \(9/64\), \(131/5625\), \(29/1458\), and \(5/96\). It then prints approximations to the root, optimal second node and minimum risk. Every inequality proving globality is exact rational arithmetic; floating-point root approximations serve only to display the result.

Run with `python verify.py` after installing `sympy`; no external data or hidden code are required. The preceding written proof, not finite sampling or numerical root searching, establishes the all-design theorem.

## Relationship to prior work

Neuberger, Alexanderian and van Bloemen Waanders (2024) derive a general data-averaged posterior-variance criterion for nonlinear Gaussian goal functions via quadratic approximation; their criterion motivates choosing sample sites for a **quadratic**, rather than only linear, functional. Their general formula is prior work and is not claimed here. The contribution above is the explicit global optimization and uniqueness theorem for two **point observations of Brownian motion**, with its algebraic isolating certificate and strict quantitative separation from optimal linear-area sampling. Their reported PDE examples and greedy sensor designs do not establish this exact Brownian two-site result.

Foster, Lyons and Oberhauser (2019) study Gaussian polynomial approximations of Brownian paths and their integrated approximation errors, a distinct projection objective rather than the posterior risk of the integrated square conditional on exactly two path values. Chakraborty, Huan and Catanach (2024) target goal-oriented information gain by likelihood-free inference, a distinct design criterion. Similar-looking Gaussian integral quadrature results typically estimate a **linear** path functional; those statements do not imply the present two-site quadratic conditional-variance optimizer.

## Limitations

The claim concerns a specific natural nonlinear path functional and noiseless deterministic two-site designs; it does not solve generic quadratic-goal sensor placement, more than two observations, sensor noise, stochastic/adaptive location selection, or absolute-error loss. The optimization reduction to a quartic and the sextic algebraic certificate do not establish a general algorithmic performance guarantee. The general Gaussian quadratic-goal variance formula is established literature. Related historical optimal-design literature might contain an equivalent special case under different terminology; exhaustive priority checking and independent mathematical audit have not been performed.

## References

1. J. Nicholas Neuberger, Alen Alexanderian, Bart van Bloemen Waanders, *Goal oriented optimal design of infinite-dimensional Bayesian inverse problems using quadratic approximations*, arXiv:2411.07532 (first public version, 2024-11-12), https://arxiv.org/html/2411.07532v1.
2. James Foster, Terry Lyons, Harald Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998 (first public version, 2019-04-15), https://arxiv.org/abs/1904.06998.
3. Atlanta Chakraborty, Xun Huan, Tommie Catanach, *A Likelihood-Free Approach to Goal-Oriented Bayesian Optimal Experimental Design*, arXiv:2408.09582 (first public version, 2024-08-18), https://arxiv.org/abs/2408.09582.
