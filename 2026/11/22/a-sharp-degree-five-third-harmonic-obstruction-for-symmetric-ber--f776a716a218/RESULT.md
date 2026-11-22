# A sharp degree-five third-harmonic obstruction for symmetric Bernstein sampling on the circle

## Finding

Let \(n\ge1\) and \(0=\theta_0<\theta_1<\cdots<\theta_n=\pi\), with reflection symmetry \(\theta_{n-j}=\pi-\theta_j\). Define the node-perturbed Bernstein operator
\[
(T_{n,\boldsymbol\theta}f)(\pi u)=\sum_{j=0}^n\binom nj u^j(1-u)^{n-j}f(\theta_j),\qquad 0\le u\le1.
\]
For the canonical positive-semidefinite circle kernel \(f(\theta)=\cos\theta\), the following **sharp universal degree threshold** holds:

**(i)** For every such symmetric grid, \(T_{n,\boldsymbol\theta}f\) remains a positive-semidefinite isotropic circle kernel whenever \(1\le n\le4\).

**(ii)** For every integer \(n\ge5\), there exists a *strictly increasing*, reflection-symmetric grid for which its **third cosine coefficient is negative**, so the output is not positive semidefinite. In every degree, the constant and all positive even Fourier coefficients are zero, and the first cosine coefficient is strictly positive. Hence the third harmonic is the *first possible* offending Fourier mode.

**(iii)** For a concrete one-parameter family, take \(\theta_j=j\varepsilon\) for \(0\le j<n/2\), \(\theta_{n-j}=\pi-j\varepsilon\), and \(\theta_{n/2}=\pi/2\) if \(n\) is even. Here \(0<\varepsilon<\pi/n\). As \(\varepsilon\downarrow0\), the third **raw** Fourier integral tends to
\[
I_n=\int_0^1 S_n(u)\cos(3\pi u)\,du<0\qquad(n\ge5),
\]
where \(S_n=\sum_{j<n/2}B_{n,j}-\sum_{j>n/2}B_{n,j}\) (the central coefficient is zero when \(n\) is even). At degree five,
\[
I_5=\frac{80(4-3\pi^2)}{81\pi^6}<0.
\]
For \(r=\lceil n/2\rceil\) one has \(S_{2r}=S_{2r-1}\) and the sharp wide-degree expansion
\[
I_n=-\frac{2}{3\pi}+\frac{3\pi}{4(2r+1)}+O(r^{-2})\quad(r\longrightarrow\infty).
\]
The ordinary cosine-series coefficient is \(2I_n\), whereas this statement uses the raw integral \(I_n\).

## Assumptions and scope

The circle is parametrized by geodesic distance \(\theta\in[0,\pi]\). Positive semidefiniteness means that \(f(d(z_i,z_j))\) yields positive-semidefinite matrices for every finite collection of sites on the unit circle, equivalently all Fourier cosine coefficients of the even periodic extension are nonnegative. All grids are finite, strictly ordered, endpoint-fixed and exactly reflection symmetric. The statement concerns the single distinguished input \(f(\theta)=\cos\theta\), not preservation of *every* positive-type input at high degrees.

Let \(B_{n,j}(u)=\binom nj u^j(1-u)^{n-j}\) and define raw cosine integrals \(\mathcal C_k(P)=\int_0^1P(u)\cos(k\pi u)\,du\). This normalization differs by a factor of two from positive-frequency cosine-series coefficients. Every polynomial involved has an absolutely summable cosine series.

## Proof

**Symmetry and the earliest possible negative harmonic.** Reflection of both nodes and Bernstein weights gives \(P_n(1-u)=-P_n(u)\) for \(P_n=T_{n,\boldsymbol\theta}(\cos)(\pi u)\). Hence \(\mathcal C_{2k}(P_n)=0\) for every integer \(k\ge0\). Since the sampled values \(\cos\theta_j\) decrease strictly with \(j\), the Bernstein derivative identity yields
\[
P_n'(u)=n\sum_{j=0}^{n-1}B_{n-1,j}(u)\bigl(\cos\theta_{j+1}-\cos\theta_j\bigr)<0\quad(0<u<1).
\]
Integrating by parts, \(\mathcal C_1(P_n)=-(1/\pi)\int_0^1P_n'(u)\sin(\pi u)du>0\). Therefore only odd harmonics of index three or more can obstruct positivity.

**The complete low-degree guarantee.** In degree four, the samples are \((1,c,0,-c,-1)\), where \(c=\cos\theta_1\in[-1,1]\). For each odd positive integer \(k\), direct twice-repeated integration by parts gives
\[
\mathcal C_k(P_4)=\frac{8}{(k\pi)^4}\bigl((k\pi)^2-6+c(12-(k\pi)^2)\bigr).
\]
For \(k=1\), both the minimum at \(c=-1\) and its numerator \(2\pi^2-18\) are positive because \(\pi^2>9\). For odd \(k\ge3\), the minimum occurs at \(c=1\) and the parenthesis is exactly \(6\). Thus every nonzero cosine coefficient is nonnegative, and the zero coefficient vanishes by antisymmetry. For degrees one to three, elevate the Bernstein representation to degree four: the elevated samples remain antisymmetric, preserve the endpoint values \(1,-1\), and have the form \((1,c,0,-c,-1)\) with \(|c|\le1\), because degree elevation takes convex combinations of the original sampled values. This proves (i) for all grids and every output frequency.

**The binomial-majority limiting polynomial.** For each \(n\ge5\), the displayed cluster family is strictly ordered when \(\varepsilon<\pi/n\). Its values \(\cos\theta_j\) tend to \(+1\) for \(j<n/2\), to \(-1\) for \(j>n/2\), and to zero at the middle node when \(n\) is even. Thus \(P_n\to S_n\) uniformly by finiteness of the Bernstein sum. Binomial degree elevation shows \(S_{2r}=S_{2r-1}\). Furthermore
\[
S_{2r-1}'(u)=-2(2r-1)\binom{2r-2}{r-1}u^{r-1}(1-u)^{r-1}.
\]
The degree-five polynomial is \(S_5(u)=1-20u^3+30u^4-12u^5\), giving the exact negative raw third coefficient in (iii) by elementary integration.

**An all-degree sign argument.** By integration by parts, \(I_{2r-1}\) has exactly the sign of
\[
J_r=\int_0^1u^{r-1}(1-u)^{r-1}\sin(3\pi u)du
=2\int_0^{1/2}u^{r-1}(1-u)^{r-1}\sin(3\pi u)du.
\]
For \(r=3\), \(J_3<0\) by the computed degree-five result. On \((0,1/2)\), \(\sin(3\pi u)\) changes sign **exactly once**, positive before \(u=1/3\) and negative afterwards. For every integer \(r>3\), the added factor \([u(1-u)]^{r-3}\) is increasing on that half interval. Comparing this factor with its value at \(1/3\) therefore shows \(J_r<0\) whenever \(J_3<0\): the negative part receives no smaller relative weight than the positive part. Hence \(I_n<0\) for every \(n\ge5\). By continuity, sufficiently small strictly positive \(\varepsilon\) retains the negative third integral, proving (ii).

**Asymptotic strength.** Let \(U_r\) have the \(\operatorname{Beta}(r,r)\) distribution. The derivative identity gives
\[
I_{2r-1}=\frac{2}{3\pi}\mathbb E\sin(3\pi U_r)
=-\frac{2}{3\pi}\mathbb E\cos\bigl(3\pi(U_r-\tfrac12)\bigr).
\]
Since \(\mathbb E(U_r-1/2)^2=[4(2r+1)]^{-1}\) and \(\mathbb E(U_r-1/2)^4=3/[16(2r+1)(2r+3)]\), Taylor's theorem for cosine with remainder bounded by the fourth moment yields the expansion in (iii). The limit is strictly negative, so the spectral violation does not shrink with increasing degree.

## Verification

The independent symbolic sign steps are: \(S_5=1-20u^3+30u^4-12u^5\); \(\int_0^1S_5\cos(3\pi u)=80(4-3\pi^2)/(81\pi^6)\); the strict half-interval sign change at \(u=1/3\); and the beta second and fourth central moments. The included `verify.py` evaluates direct Bernstein polynomials, the majority polynomial, the low-degree cosine signs, and the asymptotic formula at selected degrees. Finite checks support but do not replace the analytic all-degree proof.

## Relationship to prior work

Otten, Nguyen and Watts (2026) establish positivity preservation for **equispaced** Bernstein nodes at every degree; the present result concerns arbitrary symmetric perturbations and identifies the first-harmonic-to-third-harmonic spectral obstruction. Earlier complete degree-three and degree-four node classifications identify admissible grids at those two degrees, while a degree-five one-parameter classification treats a different constrained family. Neither finite-degree classification implies the all-degree, fixed-input, fixed-output-frequency failure or its limiting nonzero negative coefficient. The present proof does not claim originality for Bernstein positivity preservation on uniform nodes or these prior finite classifications.

## Limitations

The bad grids form a clustered family near the endpoints; no statement says that *all* nonuniform symmetric grids fail at high degrees, and uniform grids remain positivity-preserving. The theorem concerns \(f(\theta)=\cos\theta\), not every positive-definite kernel, and it gives an existence range for small \(\varepsilon\) rather than a sharp finite cutoff for \(\varepsilon\) at each degree. The asymptotic concerns the singular cluster limit and is not a uniform asymptotic across all admissible grids. No external independent mathematical audit has been conducted.

## References

1. Matthew Otten, Nam Nguyen and Thomas W. Watts, “Preservation of Positive-Definiteness by Bernstein Operators on the Circle,” arXiv:2608.04836, first posted August 5, 2026. https://arxiv.org/abs/2608.04836
2. “Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle,” publicly indexed mathematical result, 2026.
3. “Complete positive-definite classification of quartic Bernstein circle sampling nodes,” mathematical result, 2026.
4. “Degree-five positive-definite Bernstein sampling along a symmetric one-parameter grid,” mathematical result, 2026.
5. I. J. Schoenberg, “Positive definite functions on spheres,” Duke Mathematical Journal, 1942.
