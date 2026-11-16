# Unique maximin harmonic sampling by calibrated pendant vacancies on sunlet cycles

## Finding

For every integer \(n\ge3\), form the sunlet graph by attaching one pendant vertex \(y_i\) to each vertex \(x_i\) of the cycle \(C_n\). Give an independent set \(I\) Gibbs weight \(\alpha^{\#\{x_i\in I\}}\beta^{\#\{y_i\in I\}}\), with the **calibrated one-parameter activities**
\[
\alpha(r)=\frac{1}{2(1-r)},\qquad \beta(r)=\frac r{1-r},\qquad 0<r<1.
\]
Let \(X_i,Y_i\in\{0,1\}\) be the corresponding occupation indicators. The marginal law of \(X\) is the hard-core law of fugacity \(1/2\) on \(C_n\), independent of \(r\); given \(X\), the pendant indicators are independent, with \(Y_i=0\) if \(X_i=1\) and \(Y_i\sim\operatorname{Bernoulli}(r)\) if \(X_i=0\).

Let \(G_n(r)=\operatorname{Cov}(X_0,\ldots,X_{n-1},Y_0,\ldots,Y_{n-1})\) be the Gram matrix of the **centered first-coordinate Walsh observation system**, with squared observation energy measured using the Gibbs probability law and unscaled \(0/1\) coordinates. Define
\[
\rho=\sqrt3-2,\quad u_n=\rho^n,\quad p_n=\frac{(1-1/\sqrt3)/2+((1+1/\sqrt3)/2)u_n}{1+u_n},\quad c_n=1-p_n,
\]
\[
 s_n=\frac{1-u_n}{6\sqrt3(1+u_n)}+\frac{nu_n}{3(1+u_n)^2}.
\]
For every \(n\ge3\), \(0<s_n<c_n\). **There is exactly one** \(r_n\in(0,1)\) maximizing \(\lambda_{\min}(G_n(r))\); it is the unique root in \((0,1/2)\) of
\[
\boxed{2(s_n-c_n)r_n^2+(c_n+4s_n)r_n-2s_n=0.}
\]
The uniform measure over all sunlet independent sets corresponds to \(r=1/2\), hence is **strictly suboptimal** under this fixed-rim-marginal comparison. At the optimum, the bottleneck Fourier frequency is the constant rim mode, coupled to the constant pendant mode, and the smallest eigenvalue is simple.

Indeed, for \(j=1,\ldots,n-1\), put
\[
\sigma_j(n)=\frac{(1-\rho^2)(1-u_n)}{6(1+u_n)(1-2\rho\cos(2\pi j/n)+\rho^2)},\qquad \sigma_0(n)=s_n.
\]
The **entire** \(2n\)-dimensional covariance spectrum comprises the two numbers
\[
\boxed{\Lambda_\pm(a,r)=\frac{(1+r^2)a+c_nr(1-r)\pm\sqrt{\bigl[(1+r^2)a+c_nr(1-r)\bigr]^2-4ac_nr(1-r)}}2}
\]
for each \(a\) in the rim Fourier list \(\sigma_0(n),\ldots,\sigma_{n-1}(n)\), with multiplicities inherited from the Fourier modes.

As \(n\to\infty\), \(r_n\to0.222304143110410\ldots\), the optimal smallest eigenvalue tends to \(0.087662874994294\ldots\), versus \(0.079851317839934\ldots\) at \(r=1/2\). The asymptotically optimal activities tend to \(\alpha=0.642924860111458\ldots\) and \(\beta=0.285849720222916\ldots\).

## Assumptions and scope

The graph has \(2n\) **labelled** vertices, and all independent sets, including the empty set, carry strictly positive Gibbs probability. The observation matrix is the covariance of the \(2n\) unscaled centered indicator functions; no whitening or individual coordinate variance normalization is applied. The admissible design family changes the two graph fugacities **together** to keep the rim marginal distribution fixed. E-optimality means maximizing the smallest squared singular value of this observation Gram, not minimizing its condition number, and not maximizing the logarithmic determinant. All numerical constants above describe limits, not rounded exact identities.

## Proof

**1. Exact calibrated law.** For a fixed rim-independent configuration \(x\), a vacant rim vertex permits a leaf contribution \(1+\beta\), while an occupied rim vertex permits only the empty leaf. Summing over leaves gives the rim weight \((\alpha/(1+\beta))^{\sum_i x_i}\) times a common normalizer. The prescribed activities satisfy \(\alpha/(1+\beta)=1/2\) and \(\beta/(1+\beta)=r\), proving the stated conditional distribution.

**2. Exact rim Fourier covariance.** Write \(z=1/2\), \(T(z)=\bigl(\begin{smallmatrix}1&z\\1&0\end{smallmatrix}\bigr)\), with eigenvalues \(A(z)=(1+\sqrt{1+4z})/2\), \(B(z)=(1-\sqrt{1+4z})/2\). The rim partition function is \(Z_n(z)=\operatorname{tr}(T(z)^n)=A(z)^n+B(z)^n\). Let the generalized Fibonacci numbers be \(F_0(z)=0,F_1(z)=1,F_m(z)=F_{m-1}(z)+zF_{m-2}(z)\). For distinct positions separated by \(1\le k<n\), the two-site occupation probability is \(z^2F_{k-1}(z)F_{n-k-1}(z)/Z_n(z)\); the one-site probability is \(zF_{n-1}(z)/Z_n(z)\). These statements follow by fixing the occupied sites and counting the two resulting open paths, and also from two marked derivatives of the transfer-matrix trace. Using \(F_m(z)=(A(z)^m-B(z)^m)/(A(z)-B(z))\) and summing finite geometric series against the nonconstant Fourier characters gives the stated \(\sigma_j(n)\) for \(j\ne0\). The constant eigenvalue equals \(\operatorname{Var}(\sum_iX_i)/n=[(z\partial_z)^2\log Z_n(z)]/n\) at \(z=1/2\), which differentiates to the displayed \(s_n\). The mean is \(p_n=[z\partial_z\log Z_n(z)]/n\).

**3. The constant mode is strictly least.** For any \(j\ne0\), put \(v=2-\sqrt3=-\rho\in(1/4,3/10)\) and \(B_n=(1-\rho^n)/(6\sqrt3(1+\rho^n))\). Since \(1+2v\cos(2\pi j/n)+v^2<(1+v)^2\), the displayed nonconstant-mode formula gives \(\sigma_j(n)>B_n\). For odd \(n\), \(s_n<B_n\) because \(\rho^n<0\). For even \(n\ge4\), the least nonconstant mode is \(j=1\) or \(n-1\). The bounds \(B_n>1/11\), \(2v>1/2\), \((1+v)^2<169/100\), and \(1-\cos(2\pi/n)\ge8/n^2\) give
\[
\sigma_1(n)-B_n>\frac{400}{1859n^2}.
\]
On the other hand, \(s_n-B_n=nv^n/[3(1+v^n)^2]<n(3/10)^n/3\), and \(n^3(3/10)^n\le64(3/10)^4=0.5184<1200/1859\) for every \(n\ge4\). Therefore \(s_n<\sigma_1(n)\), completing strictness. Positivity of the rim covariance follows because its support includes the empty rim set and each singleton, so no nonzero linear score is constant on the support. The inequality \(s_n<c_n\) follows directly from the displayed closed expressions: since \(|\rho|<3/10\) and \(n(3/10)^n\le3(3/10)^3\) for \(n\ge3\), the two terms in \(s_n\) have combined absolute value at most \((1+0.027)/(6\sqrt3(1-0.027))+0.027/(1-0.027)^2<1/4\). Also \(p_n<1/2\) since the support contains the empty set and every configuration obeys \(X_i+X_{i+1}\le1\); hence \(c_n>1/2\). Thus \(0<s_n<c_n\) without any general negative-dependence assumption.

**4. Exact two-channel spectral decomposition.** Conditional means satisfy \(\mathbb E[Y_i\mid X]=r(1-X_i)\), and conditional variances are \(r(1-r)(1-X_i)\). The law of total covariance yields
\[
G_n(r)=\begin{pmatrix}K_n&-rK_n\\-rK_n&r^2K_n+c_nr(1-r)I_n\end{pmatrix},\qquad K_n=\operatorname{Cov}(X).
\]
A unitary discrete Fourier transformation on rim and leaf indices simultaneously splits this matrix into the specified \(2\times2\) blocks. For \(a'>a\), the difference of those blocks is the rank-one positive semidefinite matrix \((a'-a)(1,-r)^\mathsf T(1,-r)\). Thus the globally least eigenvalue comes uniquely from \(a=s_n\), and its exact branch is \(\Lambda_-(s_n,r)\).

**5. Unique global E-optimum: a threshold-certificate argument.** The following argument also applies with arbitrary \(0<s<c\), independent of the cycle. Write \(B_s(r)=\bigl(\begin{smallmatrix}s&-sr\\-sr&s r^2+cr(1-r)\end{smallmatrix}\bigr)\). For any \(0<t<s\), since its top-left entry after subtraction is positive, \(B_s(r)\succeq tI\) is equivalent to
\[
Q_t(r):=-(c(s-t)+st)r^2+c(s-t)r-t(s-t)\ge0.
\]
For each \(t\), \(Q_t\) is strictly concave in \(r\), with **unique** maximizer
\[
r_t=\frac{c(s-t)}{2\{c(s-t)+st\}}\in(0,1/2).
\]
Its maximum is nonnegative precisely when
\[
H(t):=c^2(s-t)-4ct(s-t)-4st^2\ge0.
\]
The quadratic \(H\) has exactly one zero \(t_*\) in \((0,s)\): \(H(0)=c^2s>0\), \(H(s)=-4s^3<0\), and a quadratic with these strict endpoint signs crosses just once inside the interval. At \(t_*\), the feasible set of \(r\) is the singleton \(\{r_{t_*}\}\), since the concave quadratic just touches zero. Above \(t_*\), no \(r\) is feasible. Hence \(t_*\) is the **unique maximized least eigenvalue**, attained at the **unique** \(r_*=r_{t_*}\). Eliminating \(t_*\) from the tangency equations gives \(2(s-c)r_*^2+(c+4s)r_*-2s=0\), with the required root strictly between \(0\) and \(1/2\). The other root is outside \((0,1/2)\), and both endpoints \(r=0,1\) have zero least eigenvalue. Therefore \(r=1/2\), representing uniform sunlet independent-set sampling, is not optimal.

**6. Infinite-cycle limit.** Because \(|\rho|<1\), the expressions in Step 2 give \(p_n\to(1-1/\sqrt3)/2\) and \(s_n\to1/(6\sqrt3)\). Continuity and uniqueness of the root on \((0,1/2)\) prove convergence of the optimum and of the least eigenvalue. The quoted decimals result by substituting these exact algebraic limits into the quadratic and the displayed \(\Lambda_-\) branch.

## Verification

`verify.py` (Python 3 and NumPy) independently enumerates all rim independent sets for \(3\le n\le13\), compares the entire exact Fourier spectrum, directly enumerates all weighted sunlet independent sets for \(3\le n\le6\) at four distinct activities, checks the full covariance against the block expression, tests the analytic root against a numerical design grid, and verifies the universal block identity on auxiliary random stationary binary laws. It reports **2,869 passing finite assertions**. This replay supports normalization and algebra; the infinite-size classification is proved in Steps 1–6, not inferred from enumeration.

## Relationship to prior work

Bezáková, Galanis, Goldberg and Štefankovič (2021 preprint) study weighted hard-core independent-set sampling and spectral independence for rapid mixing, but not calibrated pendant-channel covariance optimization. Ortiz and Villanueva (2022) count independent sets in corona graphs, but do not derive the centered two-channel Fourier spectrum or the unique E-optimal Gibbs tuning. A published result on the vertex-uniform covariance spectrum for independent sets of an undecorated cycle gives a related single-channel benchmark with rim fugacity one, not the calibrated fugacity-one-half pendant sampling or the maximin two-channel theorem. Published weighted-sunlet leader-selection results optimize a grounded Laplacian inverse trace, not the covariance of Gibbs occupation indicators. Thus these statements are not interchangeable under parameter renaming or spectral duality. The universal two-channel threshold argument and its sunlet Fourier application are the claimed contribution, rather than independent-set enumeration or the general hard-core transfer matrix.

## Limitations

Only the fixed-rim-marginal **one-parameter** activity family is optimized, not independent unconstrained optimization over both positive fugacities; the result is not about whitening or higher-order Walsh observables. The general two-channel lemma is valid for positive-definite binary covariance with a common marginal, but the closed Fourier inputs and unique constant bottleneck use the specific cycle law. Historical priority remains provisional: a general E-optimal covariance design theorem outside the inspected published literature might imply the two-channel threshold formula. Independently assessed mathematical validation has not been performed.

## References

- I. Bezáková, A. Galanis, L. A. Goldberg and D. Štefankovič, *Fast Sampling via Spectral Independence Beyond Bounded-Degree Graphs*, arXiv:2111.04066v1, first posted November 7, 2021. https://arxiv.org/abs/2111.04066
- C. Ortiz and M. Villanueva, *Independent Sets in Corona Graphs*, *Matemática Contemporânea* 48 (2022), 53–63, DOI:10.21711/231766362021/rmc486. https://doi.org/10.21711/231766362021/rmc486
- *The complete vertex-covariance spectrum of cycle stable-set polytopes*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-vertex-covariance-spectrum-of-cycle-stable-set-poly--f7c01b21256b
- *Exact two-leader phase transition on weighted sunlet graphs*, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-leader-phase-transition-on-weighted-sunlet-graphs--486f277a9ec1
