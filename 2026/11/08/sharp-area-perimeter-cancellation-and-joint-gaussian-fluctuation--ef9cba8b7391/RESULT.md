# Sharp area–perimeter cancellation and joint Gaussian fluctuations for uniformly thinned regular polygons

## Finding

Let \(Q_n\) denote the regular \(n\)-gon inscribed in the unit circle, where \(n\ge4\). Choose uniformly an \(m\)-element subset of its vertices, \(3\le m\le n\), and call its convex hull \(H_{n,m}\). Define the nonnegative geometric deficits
\[
 D_P=\operatorname{per}(Q_n)-\operatorname{per}(H_{n,m}),\qquad
 D_A=\operatorname{area}(Q_n)-\operatorname{area}(H_{n,m}).
\]

**Sharp deterministic inequality.** For every proper subset, \(3\le m<n\),
\[
 0<D_A<2D_P.
\]
The factor \(2\) is best possible uniformly in \(n,m\): deleting a single vertex and allowing \(n\to\infty\) makes \(D_A/D_P\to2\).

**Two-scale joint fluctuation law.** Fix \(0<\alpha<1\), take \(m=m_n=\lfloor\alpha n\rfloor\), and put \(p_n=m_n/n\). Define
\[
 c_3(p)=\frac{2\pi^3(1-p)}{p^2},\qquad
 c_5(p)=\frac{3\pi^5(1-p)(2-p)^2}{p^4}.
\]
Then, as \(n\to\infty\),
\[
 \left(
 n^{5/2}\left[D_P-\frac{c_3(p_n)}{n^2}\right],\ 
 n^{9/2}\left[2D_P-D_A-\frac{c_5(p_n)}{n^4}\right]
 \right)\ \Longrightarrow\ N_2(0,\Sigma(\alpha)),
\]
with strictly positive-definite \(\Sigma(\alpha)\). In particular,
\[
 n^2D_P\xrightarrow{\mathbb P}c_3(\alpha),\qquad
 n^4(2D_P-D_A)\xrightarrow{\mathbb P}c_5(\alpha).
\]
The entries of \(\Sigma\) are explicit: if \(G\) is a geometric random variable on \(\{1,2,\ldots\}\) with \(\Pr(G=k)=p(1-p)^{k-1}\), and \(i,j\in\{3,5\}\), set
\[
 C_{ij}(p)=\operatorname{Cov}(G^i,G^j)
 -\frac{\operatorname{Cov}(G^i,G)\operatorname{Cov}(G^j,G)}{\operatorname{Var}(G)}.
\]
Then
\[
 \Sigma(\alpha)=\alpha\,\operatorname{diag}(\pi^3/3,\pi^5/10)
 \begin{pmatrix}C_{33}(\alpha)&C_{35}(\alpha)\\C_{35}(\alpha)&C_{55}(\alpha)\end{pmatrix}
 \operatorname{diag}(\pi^3/3,\pi^5/10).
\]
In particular,
\[
 C_{33}(p)=\frac{36(5-p)(2-p)(1-p)^2}{p^6},
 \qquad \Sigma_{11}(p)=\frac{4\pi^6(5-p)(2-p)(1-p)^2}{p^5}.
\]
The remaining two covariance entries are fully determined by the stated finite geometric-moment formula; for convenient direct evaluation,
\[
 \begin{aligned}
 C_{35}(p)&=\frac{180(p-4)(p-2)(p-1)^2(p^2-17p+20)}{p^8},\\
 C_{55}(p)&=\frac{900(p-2)(p-1)^2(p^5-53p^4+624p^3-2480p^2+3680p-1808)}{p^{10}}.
 \end{aligned}
\]

## Assumptions and scope

All vertices have unit circumradius; the sampling is **without replacement**, with exactly \(m\) distinct selected vertices, not independent sampling of continuous circle angles. The chordal perimeter and ordinary planar area are unnormalized (not semiperimeter). No interiority of the circumcenter is assumed. The deterministic bound holds at each finite \(n\) with \(3\le m<n\). All fluctuation assertions hold for fixed \(\alpha\in(0,1)\), and integer \(n\to\infty\), rather than uniformly when \(\alpha\) approaches zero or one.

## Proof

**1. Exact gap geometry and deterministic inequality.** In counterclockwise order let \(g_1,\ldots,g_m\ge1\) be the cyclic step gaps in the ambient \(n\)-vertex grid; \(\sum_i g_i=n\). The chord formula and oriented shoelace identity give
\[
 \operatorname{per}(H_{n,m})=2\sum_{i=1}^m\sin\frac{\pi g_i}{n},\qquad
 \operatorname{area}(H_{n,m})=\frac12\sum_{i=1}^m\sin\frac{2\pi g_i}{n}.
\]
The signed shoelace sum is positive for a counterclockwise inscribed convex polygon, even if one gap exceeds half the circumference. Put \(\theta=\pi/n\) and \(f(t)=4\sin t-\tfrac12\sin(2t)\). Since
\[
 f(0)=0,\qquad f''(t)=-4\sin t(1-\cos t)<0\quad(0<t<\pi),
\]
strict concavity gives \(f(k\theta)<k f(\theta)\) for each integer \(k\ge2\) with \(k\le n-2\); the weaker nonstrict inequality holds for \(k=1\). A proper selection has some gap at least two. Therefore
\[
 2D_P-D_A=n f(\theta)-\sum_i f(g_i\theta)>0.
\]
The other strict inequalities follow because dropping a vertex of a strictly convex polygon strictly reduces both its perimeter and its area (or directly from strict concavity of the chord sum and strict geometric containment). For a single deleted vertex, just one gap equals two. Expanding \(2\sin t-\sin2t= t^3+O(t^5)\) and \(\sin2t-\tfrac12\sin4t=4t^3+O(t^5)\) proves the optimal ratio \(2\).

**2. Uniform compositions are conditioned geometric spacings.** Sampling a subset, then choosing one selected vertex as a uniform cyclic root, makes its ordered gap vector uniform on the \(\binom{n-1}{m-1}\) positive integer compositions of \(n\) into \(m\) parts. Equivalently, if \(G_1,\ldots,G_m\) are independent geometric variables of parameter \(p_n=m/n\), this gap law is the conditional law of \((G_1,\ldots,G_m)\) given \(\sum_iG_i=n\): every permitted composition has the identical unconditioned probability \(p_n^m(1-p_n)^{n-m}\). Rotation invariance means that the symmetric statistics used below have the original uniform-subset law as well.

**3. Cancellations and leading means.** Write \(S_k=\sum_i g_i^k\). Taylor's theorem, with an absolute remainder bounded by a constant times the next odd power for all angles \(\pi g_i/n\in[0,\pi]\), gives
\[
 \begin{aligned}
 D_P&=\frac{\pi^3}{3n^3}(S_3-n)-\frac{\pi^5}{60n^5}(S_5-n)+O(n^{-7}S_7),\\
 2D_P-D_A&=\frac{\pi^5}{10n^5}(S_5-n)+O(n^{-7}S_7).
 \end{aligned}
\]
A marginal of the uniform composition has distribution
\[
 \Pr(g_1=k)=\frac{\binom{n-k-1}{m-2}}{\binom{n-1}{m-1}},\qquad
 1\le k\le n-m+1.
\]
For any fixed positive integer \(r\) and \(p_n\to\alpha\in(0,1)\), geometric tails and a fixed-\(k\) factorial-ratio expansion imply \(\mathbb E S_r=m\mathbb E(G^r)+O(1)\), uniformly as \(n\to\infty\) for \(G\sim\operatorname{Geom}(p_n)\). In particular, \(S_7=O_{\mathbb P}(n)\). The elementary geometric-moment identities
\[
 p\mathbb EG^3-1=\frac{6(1-p)}{p^2},\qquad
 p\mathbb EG^5-1=\frac{30(1-p)(2-p)^2}{p^4}
\]
produce the two stated centering constants and show that discarded remainders vanish under their respective central-limit normalizations.

**4. Joint conditioned central limit theorem.** For \(k\in\{3,5\}\), define
\[
 W_k=G^k-\mathbb EG^k-b_k(G-1/p),\qquad
 b_k=\frac{\operatorname{Cov}(G^k,G)}{\operatorname{Var}(G)}.
\]
Then \(\operatorname{Cov}(W_k,G)=0\) and \(\operatorname{Cov}(W_i,W_j)=C_{ij}(p)\). On \(\sum_iG_i=n=m/p_n\), the sum of the linear conditioning terms is zero. Fourier inversion on the integer-valued sum therefore gives, for each fixed real vector \(u\),
\[
 \frac{\int_{-\pi}^{\pi}\!\left[\mathbb E\exp\{it(G-1/p_n)+i\langle u,W\rangle/\sqrt m\}\right]^m\,dt}
 {\int_{-\pi}^{\pi}\!\left[\mathbb E\exp\{it(G-1/p_n)\}\right]^m\,dt}
 \longrightarrow \exp\{-\tfrac12 u^\mathsf TC(\alpha)u\}.
\]
To justify the limit, split the integrals at \(|t|\le m^{-2/5}\). Uniformly for \(p_n\) in a compact subinterval of \((0,1)\), the logarithm of the characteristic function has its quadratic Taylor expansion with bounded third-order remainder; the cross quadratic term disappears because \(\operatorname{Cov}(W,G)=0\). In the intermediate region \(m^{-2/5}<|t|<\delta\), the positive variance of \(G\), the orthogonality \(\operatorname{Cov}(W,G)=0\), and uniformly bounded moments imply a modulus bound \(\exp(-ct^2)\) for the perturbed one-step characteristic function, giving an exponentially small integral after raising to the \(m\)-th power. In the outer region \(|t|\ge\delta\), lattice span one gives a fixed modulus gap below one, stable under the \(O(m^{-1/2})\) perturbation. The denominator is of order \(m^{-1/2}\) by the one-dimensional local central limit theorem (or the same Fourier estimate). Thus conditional \(m^{-1/2}\)-scaled sums of the third and fifth powers converge jointly with covariance \(C(\alpha)\). Since \(m/n\to\alpha\), the Taylor coefficients above give the displayed matrix \(\Sigma(\alpha)\).

**5. Nondegeneracy.** A linear combination of the residuals \(W_3,W_5\) cannot be almost surely constant or zero unless both coefficients vanish: otherwise a polynomial with nonzero third- or fifth-degree term would agree with an affine polynomial at every positive integer, contrary to polynomial identity. Thus \(C(\alpha)\), and hence \(\Sigma(\alpha)\), is strictly positive definite for every fixed \(\alpha\in(0,1)\).

## Verification

The standalone script `check.py` reconstructs planar polygon area and perimeter independently from Cartesian geometry for all \(7813\) vertex selections with \(4\le n\le12\) and \(m\ge3\), including \(7804\) proper subsets. It symbolically reconstructs geometric moments through degree ten, verifies all three explicit residual covariance expressions, the two mean coefficients, the cubic cancellation, and the fifth-order residual coefficient, and checks the exact composition-marginal moment formula in five finite configurations. The script passed with maximum Cartesian-versus-gap discrepancy \(1.78\cdot10^{-15}\). This finite verification is supporting evidence; the Fourier and concavity arguments above are the infinite proofs.

Reproduction: run `python check.py` with Python 3 and SymPy installed. No data files are needed.

## Relationship to prior work

Wang, Xu and Liu (2021) study area and semiperimeter extrapolation for polygons formed by **independent continuously uniform circle points**. Wang, Li and Xu (2023) develop higher-order cancellation and Dirichlet-spacing normal approximations in that continuous model. Their methods motivate examining the cancellation, but their random spacings are continuous Dirichlet variables rather than the positive-integer **uniform-composition law under fixed-size grid sampling** here. Neither inspected text supplied the present retention-fraction-dependent two-scale covariance matrix or the sharp deterministic comparison to the complete regular grid; the 2021 full text was not accessible, so this absence is not asserted for its uninspected portions. Gusakova, Reitzner and Thäle (2022) establish central limit results for convex hulls of random **interior** samples of a fixed polygon, a different sampling regime. Standard conditional-sum central limit methods supply a known technique, not claimed as a new theorem on their own.

## Limitations

The joint limit is not uniform as \(\alpha\downarrow0\) or \(\alpha\uparrow1\); it does not cover fixed sample size, Bernoulli thinning without conditioning on retained count, or smooth noncircular boundaries. Historical priority is provisional: an earlier discrete-circle sampling theorem using other terminology could conceivably imply the Gaussian result. The 2011 paper by Bélisle on continuously sampled circle points was not fully available for comparison; no assertion about its entire contents is made. The direct verification uses finite samples and exact finite symbolic identities but is not an independent mathematical audit.

## References

1. S. Wang, W.-Q. Xu, J. Liu, *Random Polygons and Optimal Extrapolation Estimates of pi*, Statistics, Optimization & Information Computing 9 (2021), 241–249, doi:10.19139/soic-2310-5070-1193; publication date 2021-03-28.
2. S. Wang, Z. Li, W.-Q. Xu, *Nonlinear random extrapolation estimates of pi under Dirichlet distributions*, Journal of Numerical Analysis and Approximation Theory 52 (2023), 273–294, doi:10.33993/jnaat522-1360; online 2023-12-22.
3. A. Gusakova, M. Reitzner, C. Thäle, *Variance expansion and Berry–Esseen bound for the number of vertices of a random polygon in a polygon*, arXiv:2204.11316 (2022-04-24).
4. C. Bélisle, *On the polygon generated by n random points on a circle*, Statistics & Probability Letters 81 (2011), 236–242 (abstract/context only; full text not inspected).
