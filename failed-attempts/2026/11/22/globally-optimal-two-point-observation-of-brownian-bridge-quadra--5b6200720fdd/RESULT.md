# Globally optimal two-point observation of Brownian-bridge quadratic energy

## Finding
Let \(B\) be the centered standard Brownian bridge on \([0,1]\), with covariance \(K(s,t)=\min(s,t)-st\), and let
\[
Q=\int_0^1 B(t)^2\,dt.
\]
For any predetermined two observation sites \(0\le x\le y\le1\), with no observation noise, estimate \(Q\) by an arbitrary square-integrable function of the observed values \(B(x),B(y)\). The minimum unconditional mean-square risk at fixed sites is attained by the conditional expectation. **Among all pairs of sites, including endpoints and repeated sites, the unique optimal ordered pair** is
\[
\boxed{\quad x_* = \frac{21-\sqrt{41}}{40},\qquad y_* = \frac{19+\sqrt{41}}{40}.\quad}
\]
These sites are reflections about \(1/2\), separated by \((\sqrt{41}-1)/20\), and have minimum unconditional squared risk
\[
\boxed{\quad R_* = \frac{1009}{96000}-\frac{287\sqrt{41}}{288000}
       =0.00412952549950268\ldots .\quad}
\]
The one-observation optimum, even if a second observation is repeated at the same site, is the midpoint and has risk \(1/120\). The common trisection design \(x=1/3,y=2/3\) has quadratic-energy risk \(16/3645\), strictly above \(R_*\).

## Assumptions and scope
The process is one-dimensional, centered, continuous and Gaussian with the stated pinned covariance, and \(Q\in L^2\). Both sites are deterministic and selected before data are seen. Exactly two noiseless point values are available; repeated sites or pinned endpoints provide no extra information. The estimator is allowed to be nonlinear, is optimized in \(L^2\) for its chosen sites, and is the conditional mean. The design criterion is \(\mathbb E[(Q-\widehat Q)^2]\), where expectation is over the bridge. Randomized and adaptive locations, observation noise, alternative energy weights, and other Gaussian covariances are not covered.

## Proof
**1. Conditional-mean estimator.** First assume \(0<x<y<1\), and write \(a=x\), \(b=y-x\), \(c=1-y\), \(U=B(x)\), \(V=B(y)\). Conditional on \((U,V)\), the process is a piecewise-linear interpolation of \((0,U,V,0)\) plus independent zero-endpoint bridges on the three subintervals of lengths \(a,b,c\). Integration of the three squared conditional linear means and of their bridge variances gives
\[
\widehat Q_{x,y}=\mathbb E[Q\mid U,V]
=\frac{(a+b)U^2+bUV+(b+c)V^2}{3}
 +\frac{a^2+b^2+c^2}{6}. \tag{1}
\]
The observations have covariance matrix
\[
\Sigma=\begin{pmatrix}x(1-x)&x(1-y)\\x(1-y)&y(1-y)\end{pmatrix},
\]
and the random quadratic term in (1) is \(Z^{\mathsf T}HZ\), where \(Z=(U,V)^{\mathsf T}\) and
\[
H=\frac13\begin{pmatrix}y&(y-x)/2\\(y-x)/2&1-x\end{pmatrix}.\tag{2}
\]
The Gaussian fourth-moment identity gives \(\operatorname{Var}(\widehat Q_{x,y})=2\operatorname{tr}[(H\Sigma)^2]\). On the other hand, Wick's identity and the Brownian-bridge kernel yield
\[
\operatorname{Var}(Q)=2\int_0^1\!\int_0^1 K(s,t)^2\,ds\,dt
=2\cdot\frac1{90}=\frac1{45}.\tag{3}
\]
The law of total variance therefore gives
\[
R(x,y):=\mathbb E\big[(Q-\widehat Q_{x,y})^2\big]
=\frac1{45}-2F(x,y),\qquad
F(x,y)=\operatorname{tr}[(H\Sigma)^2].\tag{4}
\]
This reduces the global design problem to maximization of an explicit polynomial. Formula (4) extends continuously to sites on the diagonal or boundary (using the effective single observation there), so it covers all admissible pairs.

**2. Center-and-separation coordinates.** Define \(r=(y-x)/2\) and \(t=(x+y-1)/2\). The full ordered design triangle becomes
\[
0\le r\le\frac12,\qquad |t|\le\frac12-r.
\]
Direct multiplication in (2) gives
\[
\begin{split}
G(r,t):=F\!\left(\tfrac12+t-r,\tfrac12+t+r\right)
={}&\frac5{9}r^4-\frac13r^3-\frac1{18}r^2+\frac1{36}r+\frac1{144}\\
&+t^2\left(\frac49r^3+\frac23r^2-\frac1{18}\right)
 +\frac{1-4r}{9}t^4.\tag{5}
\end{split}
\]
When \(t=0\), the expression factorizes as
\[
G(r,0)=\frac{(2r-1)^2(20r^2+8r+1)}{144},\qquad
\frac{d}{dr}G(r,0)=\frac{(2r-1)(40r^2+2r-1)}{36}.\tag{6}
\]
Consequently the unique maximizer of \(G(r,0)\) on \([0,1/2]\) is
\[
r_*=(\sqrt{41}-1)/40\in(0,1/4),\qquad
G(r_*,0)=\frac{3373+287\sqrt{41}}{576000}.\tag{7}
\]

**3. No asymmetric design can match (7).** For \(0\le r\le1/4\), expression (5) is convex in \(u=t^2\in[0,(1/2-r)^2]\), since the coefficient of \(u^2\) is nonnegative. Its maximum occurs either at \(u=0\) or at an endpoint with \(x=0\) or \(y=1\). At the latter boundary the information is only that of one nondegenerate observation, and
\[
F(0,y)=\frac{y^2(1-y)^2}{9}\le\frac1{144}<G(r_*,0).\tag{8}
\]
Therefore no asymmetric pair with \(r\le1/4\) attains the global value, and equality with (7) occurs only at \((r_*,0)\).

For \(1/4\le r<1/2\), differentiate (5):
\[
36\,\partial_rG=80r^3-36r^2-4r+1
 +(48r^2+48r)u-16u^2,\qquad u=t^2.\tag{9}
\]
For each fixed \(r\ge1/4\), the right-hand side is strictly increasing in \(u\) throughout \(0\le u\le(1/2-r)^2\): its derivative in \(u\) is \(48r^2+48r-32u\ge13>0\). At the maximal feasible \(u\) the right-hand side factorizes as
\[
16r(2r-1)(r^2+4r-1)<0.\tag{10}
\]
Thus \(\partial_rG<0\) throughout this half of the design triangle. Holding a feasible \(t\) fixed and moving from \(r\ge1/4\) toward \(1/4\) gives
\[
G(r,t)\le G(1/4,t)=\frac{17}{2304}-\frac{t^2}{144}
\le\frac{17}{2304}<G(r_*,0).\tag{11}
\]
At \(r=1/2\) both sites are pinned endpoints, yielding zero information, so (11) still applies by continuity. Together (6)–(11) prove unique global optimality of \((r_*,0)\), hence of the displayed site pair, up to exchanging labels.

**4. Exact risks and boundaries.** Substituting (7) into (4) yields the radical expression for \(R_*\). One observation at a site \(z\) has \(F=z^2(1-z)^2/9\), uniquely maximized at \(z=1/2\), so repeated and endpoint designs cannot improve upon risk \(1/120\). Substituting \((x,y)=(1/3,2/3)\) in (4) gives \(16/3645\). The square-root term in (7) makes the strict gap against both benchmarks explicit.

## Verification
Run `python verify.py` with Python 3.10+ and SymPy. The verifier independently integrates the three conditional-mean segments, checks the total expectation and Gaussian covariance polynomial, reproduces the center-coordinate factorization and the derivative boundary identity, and derives the exact algebraic optimizer and risk. It performs 325 rational-pair matrix comparisons and 5151 supplementary grid comparisons against the proposed optimum; these finite tests are not used as proof of global optimality. The global conclusion follows from the complete continuous-domain inequalities (5)–(11). `verification_output.txt` records the actual execution output.

## Relationship to prior work
Foster, Lyons and Oberhauser [1] derive conditional estimators for integrated squared Brownian motion given the terminal increment and an **integrated path observation**; their Theorem 2 and discussion do not select two **point-evaluation sites** for the quadratic energy of a pinned Brownian bridge. The basic Gaussian conditional-expectation and Brownian-bridge decomposition used here are established techniques, not claimed as novel.

Tang and Xiao [2] optimize approximations of stochastic iterated integrals using Karhunen–Loève information; the accessible preview describes Fourier-mode budgets, not this exact two-location Brownian-bridge design. Mukherjee [3] considers optimal sites for estimating the **path itself** under integrated linear prediction error, not the quadratic functional \(Q\). A published two-node Brownian-bridge kernel-quadrature result [4] optimizes the expected squared worst-case error for the **linear** target \(\int B\) under independently drawn locations, rather than a deterministic pair for \(\int B^2\). The pinned covariance cannot be replaced by the unpinned Brownian-motion covariance in this optimization; the conditional mean and the resulting polynomial both change.

## Limitations
The theorem concerns a fixed two-point design, exact observations, a standard Brownian bridge and an unconditional mean-square criterion for a nonlinear conditional-mean estimator. No claims are made about adaptive sensing, noisy measurements, larger sampling budgets, other bridge laws, or any general downstream numerical method. Classical Gaussian optimal-design literature may contain an equivalent description; full historical priority requires independent specialist examination. The proof provides global uniqueness for the stated mathematical problem, not uniqueness of the claim in the literature.

## References
1. J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998v1, first public 2019-04-15, Theorems 2–3 and Sections 1, 5, https://arxiv.org/abs/1904.06998.
2. X. Tang and A. Xiao, *Asymptotically optimal approximation of some stochastic integrals and its applications to the strong second-order methods*, Advances in Computational Mathematics 45 (2019), 813–846, first online 2018-10-24, https://doi.org/10.1007/s10444-018-9638-0.
3. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue dissertation, accessible abstract, https://docs.lib.purdue.edu/dissertations/AAI3043760/.
4. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4.
