# The sharp universal budget for unequal two-site Poisson confirmation

## Finding

Let two sites independently contain a target with common probability \(p\in(0,1)\). Conditional on its presence, encounters at either site follow independent rate-\(\lambda>0\) Poisson processes. A site counts as *confirmed* only following at least two encounters. Given a fixed total survey time \(T>0\), select nonnegative allocations \(t_1+t_2=T\) to maximize the probability that **at least one site** is confirmed. Set the dimensionless budget \(B=\lambda T\), and let \(x=\lambda t_1\). The objective is

\[
S_{p,B}(x)=1-q_p(x)q_p(B-x),\qquad
q_p(z)=1-p+p(1+z)e^{-z},\qquad 0\le x\le B.
\]

There is a universal sharp constant \(B_*\), independent of \(p\), with the following properties.

1. For every \(0<B\le B_*\) and every \(p\in(0,1)\), **every** globally optimal allocation belongs to \(\{0,B/2,B\}\): only concentration or equal division can maximize confirmation. In particular, for \(0<B\le2\) only the two concentrated allocations are optimal.
2. For every \(B>B_*\) some \(p\in(0,1)\) admits a strictly positive, strictly unequal global optimum. Thus the cutoff in the preceding statement is best possible; the asymmetry is not an artifact of a single choice of parameters.
3. Put \(y_*>3\) for the unique root on \((3,\infty)\) of

\[
\cosh y+y e^{-y}-1-y=\frac{y^2(y-1)}2.
\]

Then \(B_*=2y_*=8.402063023929754724\ldots\). A certified rational bracket is \(8.40206<B_*<8.40208\).
4. With the rational parameters \(p=999/1000\), \(B=41/4\), the strictly asymmetric split \((x,B-x)=(3,29/4)\) beats *both* concentration and equal division, with respective failure probabilities

\[
q_p(3)q_p(29/4)=0.0013702673047721578\ldots,
\quad q_p(41/4)=0.0013973741126825452\ldots,
\quad q_p(41/8)^2=0.0013975754732683889\ldots.
\]

For every fixed \(p\in(0,1)\), however, sufficiently large budgets uniquely favor equal division. The phenomenon of unequal global optima therefore occupies a finite intermediate-budget regime for any fixed occupancy probability.

## Assumptions and scope

The two presences are independent with identical probability \(p\). Conditioned on presence, encounter streams are independent, stationary Poisson streams of the same known rate \(\lambda\). Encounters require no recovery time, and two encounters at the *same site* constitute a confirmation; detections across sites are not pooled. There is no travel or setup cost. The objective is the probability of confirming **at least one site** before survey time expires, not expected detections, parameter-estimation precision, or persistence after a discovery. Zero time at a site contributes no confirmed result. All theorems quantify over real \(B>0\) and \(p\in(0,1)\), not finite grids.

## Proof

**1. Exact symmetric reduction.** Since a rate-one Poisson count up to dimensionless exposure \(z\) is at most one with probability \((1+z)e^{-z}\), the site-specific no-confirmation probability is \(q_p(z)\) as stated. Independent presence and encounters make the joint no-confirmation probability the product. Thus maximizing \(S\) is equivalent to minimizing \(q_p(x)q_p(B-x)\), or to maximizing the additive utility \(g_p(x)+g_p(B-x)\) with \(g_p(z)=-\log q_p(z)\). The latter is an increasing convex-then-concave (S-shaped) function, so this is also exactly an instance of classical S-shaped resource allocation, not a fundamentally different objective disguised by a product.

Put \(y=B/2\), \(t=|x-y|\in[0,y]\), \(\theta=(1-p)/p>0\), and \(a=\theta e^y>0\). Factoring out the positive constant \(p^2e^{-B}\), the product to be minimized becomes

\[
P_y(t)=(1+y)^2-t^2+2a[(1+y)\cosh t-t\sinh t]+a^2.
\]

For \(t>0\), define

\[
F_y(t)=\frac{(1+y)(\cosh t-1)-t\sinh t}{t^2},
\qquad F_y(0)=\frac{y-1}{2}.
\]

The exact identity

\[
P_y(t)-P_y(0)=t^2(2aF_y(t)-1)
\tag{1}
\]

will identify the only possible locations of global minima. Every \(a>0\) corresponds to a legitimate \(p=1/(1+a e^{-y})\in(0,1)\).

**2. No interior minimum of the comparison function.** The convergent entire power series is

\[
F_y(t)=\sum_{k=1}^{\infty}\frac{y-(2k-1)}{(2k)!}\,t^{2k-2}.
\tag{2}
\]

For \(y\le3\), all nonconstant coefficients are nonpositive, with at least one strictly negative: \(F_y\) is strictly decreasing for \(t>0\). For \(y>3\), the coefficients of \(F_y'(t)\) have strictly positive entries followed by strictly negative entries, with at most one intervening zero coefficient. Consequently \(F_y'\) can change sign at most once, and then only from positive to negative. Indeed, let \(m\) index the last positive coefficient of \(F_y'\); dividing its power series by the corresponding positive monomial makes every nonzero term weakly decreasing in \(t>0\), with at least one strictly decreasing term. The quotient is strictly decreasing, and so has at most one zero. Moreover

\[
F_y'(y)=\frac{-y^2e^{-y}-2[(1+y)(\cosh y-1)-y\sinh y]}{y^3}<0
\quad (y>3),
\]

because \((1+y)(\cosh y-1)-y\sinh y=\cosh y+y e^{-y}-1-y>0\) when \(y>3\), for example by \(\cosh y\ge1+y^2/2+y^4/24>1+y\). Therefore \(F_y\) has no strict interior minimum on \([0,y]\) for any \(y>0\), and, more precisely,

\[
F_y(t)>\min\{F_y(0),F_y(y)\},\qquad 0<t<y.
\tag{3}
\]

**3. Unique universal transition.** Define

\[
G(y)=F_y(y)-F_y(0)=
\frac{\cosh y+y e^{-y}-1-y}{y^2}-\frac{y-1}{2}.
\]

For \(y\le3\), step 2 gives \(G(y)<0\). Direct differentiation yields

\[
y^4G''(y)=(y^2+6)\cosh y-4y\sinh y
+(y^3+2y^2+2y)e^{-y}-2y-6.
\]

For every \(y\ge3\), since \(\sinh y<\cosh y\) and \(\cosh y\ge1+y^2/2\), this is strictly greater than

\[
((y-2)^2+2)\cosh y-2y-6
\ge 3(1+y^2/2)-2y-6>0.
\]

Thus \(G\) is strictly convex on \([3,\infty)\). The elementary bounds \(20<e^3<21\) show \(G(3)<0\), whereas \(G(y)\to\infty\) as \(y\to\infty\). Strict convexity proves that \(G\) has exactly one zero \(y_*\) on \((3,\infty)\), with \(G(y)<0\) for \(y<y_*\) and \(G(y)>0\) for \(y>y_*\). Certified exponential-series bounds at the rational points \(420103/100000\) and \(420104/100000\) yield the displayed bracket.

**4. Subcritical rigidity and sharpness.** If \(y\le y_*\), then \(F_y(t)\ge F_y(y)\) for \(0\le t\le y\). From (1), if \(2aF_y(y)\ge1\), every \(P_y(t)\ge P_y(0)\), with strict inequality for nonendpoint \(0<t<y\) except the degenerate endpoint comparison. If \(2aF_y(y)<1\), then for \(0<t<y\),

\[
P_y(t)-P_y(0)\ge\frac{t^2}{y^2}[P_y(y)-P_y(0)]
>P_y(y)-P_y(0),
\]

because the bracket is negative and \(t^2<y^2\). Hence all global optima have \(t=0\) or \(t=y\), corresponding exactly to equal division or concentration. When \(B\le2\), so \(y\le1\), differentiate to get

\[
P_y'(t)=2t\left[a\left(y\frac{\sinh t}{t}-\cosh t\right)-1\right].
\]

The parenthetic hyperbolic expression is nonpositive for \(y\le1\) because its power series has coefficients \((y-(2k+1))/(2k+1)!\). Therefore \(P_y\) is strictly decreasing on \((0,y]\), so the concentrated splits are exactly the two optima.

If \(y>y_*\), then \(F_y(y)>F_y(0)=(y-1)/2>0\). Choose sufficiently small \(0<t<y\) with \(0<F_y(t)<F_y(y)\) and choose

\[
\frac1{2F_y(y)}<a<\frac1{2F_y(t)}.
\]

Then (1) gives \(P_y(t)<P_y(0)\) but \(P_y(y)>P_y(0)\). Thus neither the equal allocation nor either concentrated allocation is optimal. By compactness a global optimum exists, and every such optimum is genuinely positive and unequal. This proves the claimed sharpness for every \(B>B_*\). A rational example is certified by exact exponential enclosures in the standalone checker.

**5. The large-budget return to equal allocation.** Fix \(p\in(0,1)\) and write \(g(z)=-\log q_p(z)\). Direct differentiation gives

\[
g''(z)=\frac{p e^{-z}[(1-p)(1-z)+p e^{-z}]}{q_p(z)^2}.
\]

For all sufficiently large \(z\), \(g''(z)<0\). The function \(g\) increases strictly and approaches the finite limit \(L=-\log(1-p)\). Fix any \(M>1\) with \(g''(z)<0\) for \(z\ge M\). As \(g(M)<L\), for all sufficiently large \(B\),

\[
2g(B/2)>g(M)+L.
\]

Consequently no maximizing allocation of \(g(x)+g(B-x)\) can have \(\min\{x,B-x\}\le M\), because such a sum is at most \(g(M)+L\). On the remaining central interval, the sum is strictly concave and symmetric, and hence uniquely maximized by \(x=B/2\). This finishes the proof.

## Verification

The standalone standard-library script `proof_checks.py` verifies a certified rational bracket \(420103/100000<y_*<420104/100000\) using Taylor expansions with a geometric positive-remainder upper bound, compares the rational asymmetric witness against both endpoints by certified intervals, and tests the key identities and subcritical bound on reproducible independent parameter grids. Its successful run reported 7,205 assertions. The exact interval checks rigorously certify the stated rational witness and root bracket; the floating-point grid tests do not prove any universal statement. Those conclusions are proved in the preceding analytic argument. The checker can be run with `python3 proof_checks.py` in a standalone directory containing this file and the checker.

## Relationship to prior work

Guillera-Arroita, Ridout and Morgan [1] analyze design of replicated imperfect-detection occupancy surveys, including tradeoffs between the number of sites and visits. Their primary objective is estimator precision, and their formulation does not give this union-of-two-confirmations universal allocation boundary. Moore and McCarthy [2] optimize spatial-temporal ecological searches with one-encounter detection and an *expected number of sites detected* objective; their negative-exponential failure response differs from the two-encounter confirmation tail and the nonlinear union probability here. Srivastava and Bullo [3] analyze generic nonconvex allocations with sigmoidal utilities and approximation algorithms, not this exact sharp numerical threshold and all-budget theorem.

The generic S-shaped resource-allocation tradition [4] and classical multiplant firm [5] are **directly relevant**: maximizing the present union success is exactly equivalent, by a strictly monotone logarithmic transformation, to maximizing the sum of two identical S-shaped utilities \(g_p\). They must not be treated as inapplicable or excluded. Their complete texts were inaccessible, and an equivalent general theorem in that literature could still cover the result. A previously established fixed-parameter two-habitat Poisson-quorum example already shows asymmetric optima at one particular budget and suitability probability. The present contribution is **not** the discovery that asymmetry can occur; it is the universal impossibility below a sharp budget and the exact onset for arbitrary positive budgets above it. That earlier example alone gives neither universal implication.

## Limitations

The result does not optimize cost of travel, mixed site qualities, different confirmation thresholds, imperfect encounter identification, or risk-sensitive objectives, and it does not establish empirical relevance without calibration. A guaranteed asymmetry **for every** occupancy probability above the threshold is not claimed; the quantifier is existence of at least one probability for each supercritical budget. The sharp constant applies to the dimensionless two-site, two-encounter model only. Historical priority remains qualified by inaccessible general S-shaped allocation literature, despite the specific comparisons recorded above. No independent validation has been performed.

## References

[1] G. Guillera-Arroita, M. S. Ridout and B. J. T. Morgan, “Design of occupancy studies with imperfect detection,” *Methods in Ecology and Evolution* 1 (2010), 131–139. First online May 4, 2010. https://doi.org/10.1111/j.2041-210X.2010.00017.x

[2] A. L. Moore and M. A. McCarthy, “Optimizing ecological survey effort over space and time,” *Methods in Ecology and Evolution* 7 (2016), 891–899. First online March 25, 2016. https://doi.org/10.1111/2041-210X.12564

[3] V. Srivastava and F. Bullo, “Knapsack problems with sigmoid utilities: Approximation algorithms via hybrid optimization,” *European Journal of Operational Research* 236 (2014), 490–498. Author preprint: https://motion.me.ucsb.edu/pdf/2012n-sb.pdf ; DOI: https://doi.org/10.1016/j.ejor.2013.12.035

[4] F. M. Vicentini, “On the Resource Allocation Problem with S-Shaped Utility Functions,” Case Western Reserve University technical memorandum 201 (1970), catalog record: https://commons.case.edu/wsom-ops-reports/370/

[5] W. Ginsberg, “The multiplant firm with increasing returns to scale,” *Journal of Economic Theory* (1974), https://doi.org/10.1016/0022-0531(74)90053-2
