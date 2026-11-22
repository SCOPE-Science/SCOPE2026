# Gaussian marginals, a two-Gaussian invariant law, and optimal ordering in noisy coordinate reshuffling

## Finding

For the quadratic \(f(x)=\tfrac12(x_1^2+x_2^2+2cx_1x_2)\), with \(0<c<1\), consider full coordinate updates corrupted by fresh independent Gaussian oracle noise of variances \(u,v>0\). Every epoch updates both coordinates exactly once, in order \((1,2)\) with probability \(p\in[0,1]\) and \((2,1)\) otherwise; orders and noises are independent between epochs. At epoch boundaries the unique stationary distribution is **exactly the two-component Gaussian mixture**

\[
\pi_p=p\,N(0,\Sigma_{12})+(1-p)\,N(0,\Sigma_{21}),\qquad
\Sigma_{12}=\begin{pmatrix}a&-ca\\-ca&d\end{pmatrix},\quad
\Sigma_{21}=\begin{pmatrix}a&-cd\\-cd&d\end{pmatrix},
\]

where

\[
a=\frac{u+c^2v}{1-c^4},\qquad d=\frac{v+c^2u}{1-c^4}.
\]

Both one-coordinate stationary marginals are Gaussian with variances \(a,d\), **independent of the ordering probability**, although the stationary joint distribution is non-Gaussian whenever \(0<p<1\) and \(u\ne v\). Specifically its mixed fourth cumulant is

\[
\operatorname{cum}(X_1,X_1,X_2,X_2)
=\frac{2p(1-p)c^2(u-v)^2}{(1+c^2)^2}>0.
\]

The exact stationary expected optimization error equals

\[
L(p)=\mathbb E_{\pi_p}f(X)
=\frac{u+v+2c^2[(1-p)u+pv]}{2(1+c^2)}.
\]

Thus for unequal noise variances the unique globally optimal fixed order is to **update the noisier coordinate first**: \(p=1\) if \(u>v\), and \(p=0\) if \(v>u\). Equal noise variances make every order probability optimal. For \(u>v\), uniform independent reshuffling incurs the exact excess stationary objective \(c^2(u-v)/[2(1+c^2)]\) relative to the optimal order.

## Assumptions and scope

Let \(c\in(0,1)\), \(u,v\in(0,\infty)\), and \(p\in[0,1]\). The Hessian is \(H=\begin{pmatrix}1&c\\c&1\end{pmatrix}\succ0\), with minimizer \(0\). At a coordinate \(i\), observe \(\partial_i f(x)+\xi_i\), where every call draws fresh centered Gaussian noise with variance \(u\) for coordinate \(1\), variance \(v\) for coordinate \(2\), and all noises are mutually independent. Take a unit step in that one coordinate: equivalently \(x_i\leftarrow-cx_{3-i}-\xi_i\). An epoch means exactly two updates with no additional noise, applied in the stated order. The order is redrawn independently in every epoch and independently of all oracle noise. The invariant law concerns observations at epoch boundaries; no claim is made about intermediate within-epoch states. Initial data may be any independent distribution with finite second moment.

## Proof

**1. Contraction and uniqueness.** For fixed choices of noise, two states driven synchronously differ according to a linear deterministic epoch map. Order \((1,2)\) acts on differences by

\[
M_{12}=\begin{pmatrix}0&-c\\0&c^2\end{pmatrix},\qquad
M_{21}=\begin{pmatrix}c^2&0\\-c&0\end{pmatrix}
\]

for order \((2,1)\). Direct multiplication gives

\[
M_{12}^{\mathsf T}HM_{12}
=\operatorname{diag}(0,c^2(1-c^2)),\qquad
M_{21}^{\mathsf T}HM_{21}
=\operatorname{diag}(c^2(1-c^2),0).
\]

The Schur complement bounds \(x^{\mathsf T}Hx\ge(1-c^2)x_i^2\) imply \(\|M_{12}x\|_H,\|M_{21}x\|_H\le c\|x\|_H\). Therefore the epoch Markov transition is a strict \(c\)-contraction in quadratic Wasserstein distance induced by \(H\); the Gaussian innovations have finite second moments. The usual complete-metric contraction argument (or the convergent past-innovation series) yields a unique invariant measure with finite second moment, approached geometrically from any independent finite-second-moment initial law.

**2. Common marginal variances.** Solve the simultaneous equations

\[
a=c^2d+u,\qquad d=c^2a+v.
\]

They have the unique positive solution reported above. Start with *any* joint law whose two marginals are centered \(N(0,a)\) and \(N(0,d)\), independent of upcoming noise and order. If order \((1,2)\) is used, the output coordinates are

\[
X_1'=-cX_2-\xi_1,\qquad X_2'=-cX_1'-\xi_2.
\]

Thus the pair is jointly centered Gaussian (a linear function of the Gaussian input marginal \(X_2\) and fresh independent Gaussian innovations), with variances \(a,d\) and covariance \(-ca\). If order \((2,1)\) is used, the analogous output is jointly Gaussian with the same diagonal and covariance \(-cd\). Consequently the mixture \(pN(0,\Sigma_{12})+(1-p)N(0,\Sigma_{21})\) is invariant under one fresh epoch. The two covariances are positive definite because their determinants equal \(av\) and \(du\), respectively. Uniqueness from Step 1 proves this is the entire invariant distribution, not only a covariance approximation.

**3. Non-Gaussian joint dependence.** Both components have the same Gaussian marginal variances \(a,d\); their covariances are \(-ca\) and \(-cd\). By Isserlis' identity, conditional on either mixture component, \(\mathbb E[X_1^2X_2^2]=ad+2\operatorname{Cov}(X_1,X_2)^2\). Subtracting the Gaussian fourth-moment expression formed from the mixture's average covariance yields

\[
\begin{aligned}
\kappa_{1122}&=2\left[p(ca)^2+(1-p)(cd)^2-(pc a+(1-p)c d)^2\right]\\
&=2p(1-p)c^2(a-d)^2
=\frac{2p(1-p)c^2(u-v)^2}{(1+c^2)^2}.
\end{aligned}
\]

A genuine joint Gaussian has vanishing fourth cumulants. Hence the mixture is non-Gaussian for all strictly mixed orders and unequal noise variances, despite both Gaussian marginals. For the given domain, it is Gaussian precisely when \(p\in\{0,1\}\) or \(u=v\).

**4. Exact steady-state objective and strict order choice.** The invariant covariance is \(\Sigma_p=p\Sigma_{12}+(1-p)\Sigma_{21}\). Therefore

\[
\mathbb E f(X)=\tfrac12\operatorname{tr}(H\Sigma_p)
=\tfrac12[a+d-2c^2(pa+(1-p)d)]
=\frac{u+v+2c^2((1-p)u+pv)}{2(1+c^2)}.
\]

Its derivative in \(p\) is \(-c^2(u-v)/(1+c^2)\), strictly negative for \(u>v\) and strictly positive for \(v>u\). This proves uniqueness of the minimizing endpoint, all equality cases, and the reshuffling penalty.

## Verification

Run `python verify.py` after installing packages in `requirements.txt`. The script symbolically checks the marginal fixed-point equations, order contraction matrices, component covariance positive-determinant identities, stationary objective, derivative and fourth cumulant formula. A separate independent epoch-chain simulation with fixed reproducible seed and \(210000\) retained epochs after \(5000\) burn-in empirically checks means of five predicted moments for one illustrative nondegenerate parameter set. The exact algebraic identities and the written proof, not the finite simulation, establish the all-parameter theorem.

## Relationship to prior work

Gürbüzbalaban–Ozdaglar–Vanli–Wright (arXiv:1803.08200, first public 2018-03-22) study permutation, cyclic and with-replacement coordinate descent on convex quadratics, but their exact-line-search update has **no fresh additive Gaussian oracle noise**, and their convergence results do not give this invariant law or precision-order optimum. Safran–Shamir (arXiv:2106.06880) study finite-epoch shuffled finite-sum SGD rates, again a distinct transition and noise model.

Chen–Ip (2014) give general scan-order dependence and a mixture representation for *random-scan incompatible Gibbs chains* in two variables. That establishes relevant mixture principles and must not be mistaken for a novelty claim about Gaussian mixtures in general. Here each macro-transition updates both coordinates **exactly once** under an independently randomized full permutation, with a particular heteroscedastic Gaussian oracle. The explicit full invariant, exact mixed cumulant, Gaussian marginal invariance and strict noisier-first objective optimizer are not stated by their general random single-site scan result. Their results are a substantive conceptual precursor.

The published Gaussianity/nonorthogonality-graph theorem for noisy randomized Kaczmarz classifies with-replacement single-row updates and gives fourth-cumulant obstructions; it is not an exact invariant distribution or order-choice result for independent two-coordinate full epochs. Published finite-epoch results on noisy-free two-coordinate reshuffling likewise optimize a different finite-horizon loss. Related stationary order-risk results for scalar noninterpolating finite-sum quadratics have a different scalar-component iteration with biased epochs and do not cover this two-dimensional fresh Gaussian oracle model.

## Limitations

The result is limited to a two-dimensional SPD quadratic with equal unit diagonal Hessian, fixed nonzero coupling, fresh Gaussian noise by coordinate, and exactly two updates per epoch. It characterizes stationary **epoch-boundary** distributions and expected objective, not transient convergence-rate optimality, non-Gaussian noise, adaptively chosen orders, multiple coordinates, or time-averaged risk. The independent random order and fresh noise assumptions are essential. The Gaussian-mixture principle has important earlier analogues; no independent publication-priority assessment has been made, and an older specialized equivalent may exist.

## References

1. M. Gürbüzbalaban, A. Ozdaglar, N. D. Vanli, and S. J. Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200 (first submitted 2018-03-22), https://arxiv.org/abs/1803.08200.
2. I. Safran and O. Shamir, *Random Shuffling Beats SGD Only After Many Epochs on Ill-Conditioned Problems*, arXiv:2106.06880 (first submitted 2021-06-12), https://arxiv.org/abs/2106.06880.
3. S.-H. Chen and E. H. Ip, *Behaviour of the Gibbs sampler when conditional distributions are potentially incompatible*, Journal of Statistical Computation and Simulation 85 (2015), 3266–3275 (online 2014-10-13), https://doi.org/10.1080/00949655.2014.968159.
4. *Gaussianity is exactly a nonorthogonality-graph compatibility condition for noisy randomized Kaczmarz*, public research note, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-gaussianity-is-exactly-a-nonorthogonality-graph-compatibility-co--525a6be445a9.
5. *Sharp randomized-to-deterministic ordering transition for two-component quadratic reshuffling*, public research note, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-randomized-to-deterministic-ordering-transition-for-two-co--0dcf8057d8e5.
