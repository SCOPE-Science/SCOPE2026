# Optimal two-sensor Brownian-bridge path recovery has a unique noise-dependent spacing

## Finding
Let \(B\) be a standard mean-zero Brownian bridge on \([0,1]\). For every noise variance \(\eta>0\), observe \(Y_i=B(x_i)+\varepsilon_i\) at two freely chosen locations \(0\leq x_1\leq x_2\leq1\), where the observation errors are independent centered Gaussians of variance \(\eta\), independent of \(B\). The loss is the integrated posterior variance
\[
\mathcal J_\eta(x_1,x_2)=\int_0^1\operatorname{Var}\bigl(B(t)\mid Y_1,Y_2\bigr)\,dt.
\]
Among **all** ordered pairs, including coincident observations and endpoints, there is exactly one minimizer:
\[
(x_1^*,x_2^*)=\left(\frac{1-b_\eta}{2},\frac{1+b_\eta}{2}\right),
\]
where \(b_\eta\in(0,1/3)\) is the unique zero of the explicit polynomial \(H(b,\eta)\) below. The separation \(b_\eta\) is strictly decreasing and continuous in \(\eta\), with
\[
 b_\eta=\frac13-\frac23\eta+O(\eta^2)\quad(\eta\downarrow0),\qquad
 b_\eta\sim\frac1{8\eta}\quad(\eta\to\infty).
\]
Thus the two sensors are distinct for every finite positive noise variance, and approach duplicate measurements at the midpoint only in the infinite-noise limit.

The root-defining polynomial is
\[
\begin{aligned}
H(b,\eta)={}&b^2(b-1)^3(3b-1)
-2\eta b(b-1)^2(5b^2+5b-2)\\
&+2\eta^2(b-1)(2b^3+19b^2-1)-16\eta^3b(b+1).
\end{aligned}
\]
The formula specifies an optimal site pair for any real \(\eta>0\) using a single root within a rigorously isolated interval, not a numerical-local-optimum assumption.

## Assumptions and scope
The bridge covariance is \(k(s,t)=\min(s,t)-st\). The sites can be independently chosen anywhere in the closed unit interval and may coincide; observation noise is independent with the same known positive variance at both readings. The posterior mean is the mean-square optimal path predictor. There is no unknown regression mean, sensor-placement cost or optimization over the observation variance. The scalar loss integrates Lebesgue-time posterior pointwise variance, **not** posterior uncertainty about the path integral, worst-case pointwise variance or mutual information.

## Proof
**1. Exact loss.** For \(0<x<y<1\), set \(a=x\), \(b=y-x\), \(c=1-y\). Conditional on the two latent bridge values, the three intervening Brownian bridges contribute exactly \((a^2+b^2+c^2)/6\) to the integrated variance. The two latent values have posterior precision and interpolation Gram matrices
\[
Q=\begin{pmatrix}a^{-1}+b^{-1}+\eta^{-1}&-b^{-1}\\-b^{-1}&b^{-1}+c^{-1}+\eta^{-1}\end{pmatrix},\qquad
T=\frac13\begin{pmatrix}a+b&b/2\\b/2&b+c\end{pmatrix}.
\]
Hence \(\mathcal J_\eta=(a^2+b^2+c^2)/6+\operatorname{tr}(TQ^{-1})\), with continuous extension to boundary and coincident sensors. An independent check uses \(\mathcal J_\eta=1/6-\operatorname{tr}[(K+\eta I)^{-1}M]\), where \(K_{ij}=k(x_i,x_j)\), \(M_{ij}=\int k(t,x_i)k(t,x_j)dt\); for \(x\leq y\), \(M_{11}=x^2(1-x)^2/3\), \(M_{22}=y^2(1-y)^2/3\), and \(M_{12}=x(1-y)(2y-x^2-y^2)/6\).

**2. Short-gap centering.** Put \(d=x+y-1=a-c\), \(u=d^2\), so \(0\leq u\leq(1-b)^2\). Define
\[
G=b\bigl((1-b)^2-u\bigr)+2\eta(1-b^2-u)+4\eta^2>0.
\]
Algebraic expansion gives
\[
12(b-2\eta-1)(b^2-b-2\eta)G\,[\mathcal J_\eta(b,d)-\mathcal J_\eta(b,0)]
=u[A(b,\eta)+uC(b,\eta)],
\]
where the coefficients of \(C\), in increasing powers of \(\eta\), are
\(-b^2(1-b)^2,\ 4b(b-1),\ 4(b^2-b-1),\ -8\), all strictly negative for \(0<b<1\); the coefficients of \(A\) are
\[
 b^2(b-1)^4,\quad -4b(b-1)^3(b+1),\quad
 4(b-1)(b+1)(5b^2-2b-1),\quad -16(3b^2-1).
\]
At the largest admissible \(u=(1-b)^2\), the bracket equals
\[
4b^2(1-b)^3\eta+4b(1-b)(3-b-6b^2)\eta^2+8(1+2b-7b^2)\eta^3>0
\]
for \(0\leq b\leq1/2\), \(\eta>0\). As the bracket decreases in \(u\), centering strictly improves every noncentered pair with separation at most \(1/2\).

**3. Large-gap exclusion.** For \(1/2\leq b\leq1\), compare with the centered pair of gap \(1/2\). Set
\[
N(u)=48(4\eta+1)(8\eta+1)G\,[\mathcal J_\eta(b,d)-\mathcal J_\eta(1/2,0)].
\]
Its quadratic coefficient in \(u\) is \(-4(b+2\eta)(4\eta+1)(8\eta+1)<0\), so it is concave on \([0,(1-b)^2]\). At \(u=0\), the four coefficients of \(N\) in increasing powers of \(\eta\) are
\[
\begin{aligned}
&b(1-b)^2(2b-1)(6b-1),\\
&2(b-1)(2b-1)(36b^3-44b^2-3b+1),\\
&4(2b-1)(48b^4-116b^3+38b^2+34b+1),\\
&16(2b-1)(2b+1)(7-4b^2).
\end{aligned}
\]
They are nonnegative on \([1/2,1]\). In particular, the quartic in the third line has positive Bernstein coefficients \((16,137/8,187/12,43/4,5)\) after mapping \(b=(1+t)/2\); and \(36b^3-44b^2-3b+1<0\) since \(36b^3\leq36b^2\). At \(u=(1-b)^2\), writing \(z=b(1-b)\in[0,1/4]\), one obtains
\[
N((1-b)^2)=4b(1-b)(16b^2-16b+5)\eta
+4(5+36z-192z^2)\eta^2+16(9-128z^2)\eta^3>0.
\]
Concavity implies \(N(u)\geq0\) throughout the interval, with equality only at the centered gap-\(1/2\) pair. Thus no gap larger than \(1/2\) beats that pair.

**4. The unique optimal symmetric gap.** Substituting \(d=0\) gives
\[
J_\eta(b)=\frac16-\frac{(1-b)^2(2b+1)}{24[\eta+(1-b)/2]}
-\frac{b^2(1-b)^2}{24[\eta+b(1-b)/2]}.
\]
Its exact derivative is
\[
J_\eta'(b)=\frac{(b-1)H(b,\eta)}{6(b-2\eta-1)^2(b^2-b-2\eta)^2}.
\]
For \(b\in[1/3,1]\), substitute \(b=(1+3t)/(3(1+t))\). Every coefficient of \((1+t)^6H\) in nonnegative integer powers of \(t,\eta\) is nonpositive, and at least one is strictly negative for \(\eta>0\); thus \(J_\eta'(b)>0\) for \(1/3\leq b<1\). For \(0<b<1/3\), substitute \(b=t/(3(1+t))\). Its degree-six polynomial \((1+t)^6H\), written in increasing powers of \(t\), has a positive constant \(2\eta^2\) and negative leading coefficient \(-16\eta(6\eta+1)(18\eta+1)/243\). Each intermediate coefficient (indices \(1,\ldots,5\)) has exactly one positive \(\eta\)-zero, respectively in the disjoint rational intervals
\[
(223/100,224/100),\ (96/100,97/100),\ (50/100,51/100),\
(25/100,26/100),\ (9/100,10/100).
\]
All five coefficients start positive and eventually turn negative. Since their thresholds occur in strictly decreasing index order, the coefficient list has exactly one sign variation for **every** \(\eta>0\). Descartes' rule and opposite endpoint signs therefore give exactly one root \(t>0\), equivalently one \(b_\eta\in(0,1/3)\). The derivative changes from negative to positive there, giving the unique global symmetric optimum. Steps 2–3 promote it to the unique unrestricted optimum.

**5. Monotonicity and limiting rates.** For fixed \(b\in(0,1/3)\), the coefficients of \(H(b,\eta)\) in ascending powers of \(\eta\) also have exactly one sign variation: the constant is positive, the cubic coefficient negative, and the middle sign changes occur in order (the quadratic coefficient changes at a \(b<1/4\); the linear at a \(b>1/4\)). Every separation therefore corresponds to exactly one positive noise variance. This and the preceding unique-separation result imply that the continuous root curve is a strictly decreasing bijection from \((0,\infty)\) onto \((0,1/3)\). Expanding \(H(1/3+k\eta,\eta)\) to first order yields \(-8(3k+2)\eta/243\), so \(k=-2/3\). Rescaling \(b=z/\eta\) gives \(\eta^{-2}H(z/\eta,\eta)\to-2(8z-1)\), hence \(z=1/8\). The expansion roots are simple, justifying the error orders.

## Verification
The independent posterior-covariance and bridge-precision formulas, all sign-certificate polynomial identities, the Bernstein coefficients, the transformed derivative coefficients, rational root brackets, and both asymptotic expansions were checked using the bundled executable `verify.py` with SymPy. It reports 60 exact checks. Additional numerical minimization over unrestricted sites agreed, e.g. \(\eta=0.1\) gives gap \(0.2742030828\) and sites approximately \(0.3628984586,0.6371015414\); \(\eta=1\) gives gap \(0.0975436820\). Computation is supplementary; the proof covers all real \(\eta>0\).

## Relationship to prior work
The classical error-free Brownian-bridge path-design problem has equally spaced sites; this is explicitly attributed to Mukherjee (2003) in the later open-access discussion by Tsirpitzi, Miller and Burman. Guestrin, Krause and Singh (2005) and Krause, Singh and Guestrin (2008) investigate Gaussian-process sensor placement principally through mutual information and approximation algorithms. Tzoumas, Jadbabaie and Pappas (2015 preprint) address noisy dynamic-state estimation through sensor-set selection. Santin (2022, Theorem 5) proves an optimal fill-distance rule for **noise-free** interpolation with a modified bridge Green kernel; its kernel parameter is not independent measurement-noise variance. A 2023 open-access article on Brownian-bridge model misspecification treats regression-plus-bridge prediction and a noise-free limiting design, not the above exact two-noisy-point no-regression optimization. None of the inspected material gives or implies the present unrestricted finite-positive-noise root and inverse-noise collision law. A historical dissertation was available only by abstract, so equivalence with unexamined older material cannot be fully excluded.

## Limitations
The claim is specific to exactly two independent, equal-variance point observations and a standard bridge with known endpoints. It does not optimize adaptive sampling, correlated or heteroscedastic observation errors, larger sensor sets, posterior integral variance, mutual information, or prediction under an unknown trend. An external independent mathematical audit has not been performed. Bibliographic search cannot certify absence of unpublished or unindexed equivalent work.

## References
- C. Guestrin, A. Krause, A. P. Singh, *Near-Optimal Sensor Placements in Gaussian Processes*, ICML (2005), DOI: https://doi.org/10.1145/1102351.1102385 (publisher public date 2005-08-07).
- A. Krause, A. Singh, C. Guestrin, *Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies*, JMLR 9 (2008), pp. 235–284, https://jmlr.org/papers/v9/krause08a.html .
- B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue Ph.D. dissertation (catalog record and abstract), https://docs.lib.purdue.edu/dissertations/AAI3043760/ .
- V. Tzoumas, A. Jadbabaie, G. J. Pappas, *Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms*, arXiv:1509.08146, initially public 2015-09-27, https://arxiv.org/abs/1509.08146 .
- G. Santin, *Equally spaced points are optimal for Brownian Bridge kernel interpolation*, arXiv:2210.15959 (2022), https://arxiv.org/abs/2210.15959 .
- *Robust optimal designs using a model misspecification term*, Metrika (2023), DOI: https://doi.org/10.1007/s00184-023-00893-6 .
