# Strict negative skewness and a two-term cubic law for random spherical triangle perimeters

## Finding

Let \(d\ge3\) and let \(U_1,U_2,U_3\) be independent, surface-uniform points of \(S^{d-1}\subset\mathbb R^d\). Their shorter great-circle distances are \(\Theta_{ij}=\arccos(U_i\cdot U_j)\); the intrinsic spherical triangle perimeter is \(P_d=\Theta_{12}+\Theta_{23}+\Theta_{31}\). Define
\[
\ell_d=\frac{\Gamma(d/2)^2}{(d-1)\Gamma((d-1)/2)\Gamma((d+1)/2)}.
\]
For **every** integer \(d\ge3\), the three individual distances are pairwise independent, yet their perimeter has a strictly negative third centered moment satisfying the finite-dimensional strict inequality
\[
\mathbb E[(P_d-3\pi/2)^3]<-6d\ell_d^3<0.
\]
An absolutely convergent, nonnegative-coefficient spherical-harmonic trace series gives this third moment exactly. As the ambient dimension increases,
\[
\begin{aligned}
\mathbb EP_d&=\frac{3\pi}{2},\\
\operatorname{Var}(P_d)&=\frac3d+\frac3{d^2}+O(d^{-3}),\\
\mathbb E[(P_d-3\pi/2)^3]&=-\frac6{d^2}-\frac9{d^3}+O(d^{-7/2}),\\
\operatorname{Skew}(P_d)&=-\frac2{\sqrt{3d}}+O(d^{-2}),\\
\sqrt{\frac d3}(P_d-3\pi/2)&\Longrightarrow N(0,1).
\end{aligned}
\]
In particular, the relative first correction cancels between the third moment and the variance normalization: there is no \(d^{-3/2}\) term in standardized skewness.

## Assumptions and scope

The sphere has radius one and is equipped with normalized rotationally invariant surface measure \(\sigma_d\). All three vertices are independent. Each geodesic side is the unique shorter great-circle arc almost surely; coincident or antipodal cases have probability zero. The perimeter is the sum of these three intrinsic side lengths, not a Euclidean chord perimeter. All finite-dimensional statements hold for integer \(d\ge3\), and the asymptotic statements concern \(d\to\infty\) with exactly three vertices.

Put \(T_{ij}=U_i\cdot U_j\) and \(g(t)=\arcsin t\). Then \(\Theta_{ij}-\pi/2=-g(T_{ij})\). The density of any \(T_{ij}\) is
\[
 w_d(t)=c_d(1-t^2)^{(d-3)/2},\qquad
 c_d=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)},\quad -1<t<1.
\]
For \(l\ge0\), let \(Q_{l,d}\) be the Gegenbauer polynomial normalized by \(Q_{l,d}(1)=1\) with parameter \((d-2)/2\), and set
\[
 \lambda_{l,d}=\int_{-1}^{1}g(t)Q_{l,d}(t)w_d(t)\,dt,\qquad
 h_{l,d}=\frac{(2l+d-2)(l+d-3)!}{l!(d-2)!}.
\]
The spectral exact formula is
\[
 \boxed{\mathbb E[(P_d-3\pi/2)^3]
 =-6\sum_{k=0}^{\infty}h_{2k+1,d}\lambda_{2k+1,d}^{\,3}.}
\]
Every term of this series is nonnegative before multiplication by \(-6\). The sum is finite. The exact variance is
\[
 \operatorname{Var}(P_d)=3\int_{-1}^{1}g(t)^2w_d(t)\,dt.
\]

## Proof

**Pairwise independence and reduction.** Fixing a common vertex, the two remaining vertices are independent and uniform; the two incident arc lengths therefore have independent conditional distributions that do not depend on the fixed vertex. All three pairs of side lengths are independent. Symmetry of \(w_d\) shows that each centered side has mean and third moment zero. All mixed cubic terms involving only two sides vanish by pairwise independence. Expanding the cube therefore gives
\[
 \mathbb E[(P_d-3\pi/2)^3]
 =-6\,\mathbb E[g(T_{12})g(T_{23})g(T_{31})]. \tag{1}
\]
The pairwise independence also yields the stated exact variance integral.

**Positive spectral trace and strict sign.** Define on \(L^2(S^{d-1},\sigma_d)\) the self-adjoint integral operator
\[
 (\mathcal T f)(x)=\int_{S^{d-1}}g(x\cdot y)f(y)\,d\sigma_d(y).
\]
The power series \(g(t)=\sum_{j\ge0}a_jt^{2j+1}\), with strictly positive coefficients \(a_j\), converges uniformly on \([-1,1]\). Each kernel \((x\cdot y)^{2j+1}\) is positive semidefinite: it is the inner product of odd tensor powers of \(x\) and \(y\). Its integral operator has finite rank and nonnegative trace. Because \(\sum_j a_j=g(1)=\pi/2\), \(\mathcal T\) is a positive trace-class operator, with trace \(\pi/2\). Fubini and the trace-class identity give
\[
 \mathbb E[g(T_{12})g(T_{23})g(T_{31})]
 =\operatorname{tr}(\mathcal T^3)>0.
\]
By rotation invariance \(\mathcal T\) acts by the scalar \(\lambda_{l,d}\) on the degree-\(l\) spherical harmonics, whose dimension is \(h_{l,d}\). Even-degree eigenvalues vanish by oddness; all remaining eigenvalues are nonnegative. Taking the trace of the cube proves the exact series.

The degree-one eigenvalue is
\[
 \lambda_{1,d}=\int_{-1}^1t\arcsin(t)w_d(t)\,dt.
\]
Integration by parts, with the boundary factor \((1-t^2)^{(d-1)/2}\) vanishing at both endpoints, yields \(\lambda_{1,d}=\ell_d\). Since \(h_{1,d}=d\), the trace is at least \(d\ell_d^3\). It is **strictly greater**: the positive coefficient of \(t^3\) in \(g\) gives a strictly positive eigenvalue on degree-three harmonics (the degree-three component of the symmetric tensor cube is nonzero for \(d\ge3\)). Combining with (1) proves the strict finite-dimensional bound.

**Sharp moment coefficients.** For two independent uniform sphere points, even inner-product moments satisfy
\[
 \mathbb E[T^{2k}]=\frac{(2k-1)!!}{d(d+2)\cdots(d+2k-2)}.
\]
The uniformly valid expansions \(g(t)^2=t^2+t^4/3+O(t^6)\) and \(g(t)=t+t^3/6+O(t^5)\), together with these moments, give
\[
 \operatorname{Var}(P_d)=3\left[\frac1d+\frac1{d(d+2)}+O(d^{-3})\right].
\]
Independence of the third vertex and isotropy give the exact contractions
\[
 \mathbb E[T_{12}T_{23}T_{31}]=\frac1{d^2},\qquad
 \mathbb E[T_{12}^3T_{23}T_{31}]=\frac{3}{d^2(d+2)}.
\]
Expanding the product of three copies of \(g\) through total degree five consequently gives
\[
 \mathbb E[g(T_{12})g(T_{23})g(T_{31})]
 =\frac1{d^2}+\frac3{2d^2(d+2)}+O(d^{-7/2}).
\]
To justify the remainder uniformly, use \(|g(t)|\le(\pi/2)|t|\), \(|g(t)-t-t^3/6|\le C|t|^5\), and Hölder's inequality. Every error monomial has total inner-product degree at least seven, and its expectation in absolute value is \(O(d^{-7/2})\), since each fixed absolute moment of an individual inner product of order \(r\) is \(O(d^{-r/2})\). Formula (1) now yields the displayed two-term third-moment expansion.

Taking the three-halves power of the variance expansion gives
\[
 \operatorname{Var}(P_d)^{3/2}=(3/d)^{3/2}\left(1+\frac3{2d}+O(d^{-2})\right).
\]
The same relative term \(3/(2d)\) occurs in the negative third-moment expansion; it cancels on division. This proves the sharper standardized-skewness remainder \(O(d^{-2})\).

**Normal limit.** Write \(U_i=G_i/\|G_i\|\) using independent standard Gaussian vectors \(G_i\in\mathbb R^d\). A multivariate central limit theorem for the three coordinatewise products \((G_{1r}G_{2r},G_{2r}G_{3r},G_{3r}G_{1r})\) shows that \(\sqrt d(T_{12},T_{23},T_{31})\) converges jointly to three independent standard Gaussians. Since \(g(t)=t+O(t^3)\) near zero, the stated normal limit for the centered perimeter follows.

## Verification

The companion `check_perimeter.py` evaluates the degree-one gamma-function eigenvalue against independently integrated Gegenbauer coefficients, checks the exact Legendre-coefficient sequence in ambient dimension three, and numerically evaluates the positive spectral trace for dimensions \(3,4,8,16\). It also samples independent unit-vector triples in dimensions \(3,8,24,64\), checks the exact inner-product triple contraction, and compares observed centered moments against the analytic expansions. Computation only corroborates the proof; finite simulation does not establish the all-dimensional statements.

For \(d=3\), an additional independently checkable specialization is
\[
 \lambda_{2k+1,3}=\frac{\pi}{8(k+1)^2}\left(\frac{\binom{2k}{k}}{4^k}\right)^2.
\]
Truncating this rigorously convergent positive series numerically gives third centered moment approximately \(-1.09070211\); this low-dimensional number is **not** claimed independently novel, since an older complete perimeter-density formula already exists in ambient dimension three.

## Relationship to prior work

Finch and Jones, *Random Spherical Triangles* (first public arXiv version September 27, 2010, arXiv:1009.5329), discuss the classical exact perimeter-density representation for three uniform vertices on the ordinary two-sphere, including their Section 2.3. That density already determines all moments at \(d=3\), so no formula obtained solely in dimension three is claimed as new here. The present claim concerns the **all-dimensional** strict sign, explicit harmonic lower bound, and sharp two-term higher-dimensional cubic law.

Cai, Fan and Jiang, *Distributions of Angles in Random Packing on Spheres* (first public version June 2, 2013, arXiv:1306.0256), establish marginal and empirical/extreme angle laws primarily when the number of sampled points grows. Their limiting angle results do not give the fixed-three-vertex cyclic mixed third moment or the perimeter skewness correction derived here. Classical positive-definite spherical-kernel theory supplies the framework for the spectral argument; the positivity of this particular kernel is also proved directly above.

Johan Philip, *The Area and Perimeter of a Random Spherical Triangle* (manuscript dated May 7, 2015), gives exact distributions for two polar random-triangle constructions on the ordinary two-sphere; in the vertex-sampling construction (Case 2, Section 9), the perimeter density and its mean and variance are already established. Its pairwise-independence explanation in the polar construction also makes clear that pairwise independence alone is not new. No special case for \(d=3\) or pairwise-independence statement is asserted as historically original.

The known identity \(\mathbb E[T_{12}T_{23}T_{31}]=1/d^2\) is not claimed as new; it is an elementary contraction also consistent with existing results on triangular cumulants of random correlation matrices. The nonlinear arcsine trace, the global strict sign and the cancellation at the first relative skewness correction are the candidate contribution.

## Limitations

The theorem treats exactly three independent vertices and integer dimension \(d\ge3\). It concerns intrinsic great-circle distances, not chord lengths. It does not provide a closed-form density of the perimeter in arbitrary dimension, a Berry–Esseen rate for the normal approximation, or a complete proof of historical priority. In dimension three a full density formula predates this result, and unpublished or differently formulated harmonic-moment work might imply the presented higher-dimensional identities. The numerical checks are not independent mathematical validation.

## References

1. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329 (first posted September 27, 2010), https://arxiv.org/abs/1009.5329.
2. T. Cai, J. Fan and T. Jiang, *Distributions of Angles in Random Packing on Spheres*, arXiv:1306.0256 (first posted June 2, 2013), https://arxiv.org/abs/1306.0256; Journal of Machine Learning Research 14 (2013), 1837–1864.
3. J. Philip, *The Area and Perimeter of a Random Spherical Triangle*, manuscript dated May 7, 2015, https://people.kth.se/~johanph/spherical.pdf, especially Section 9.
4. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108, DOI 10.1215/S0012-7094-42-00908-6 (background; direct positivity proof provided above).
