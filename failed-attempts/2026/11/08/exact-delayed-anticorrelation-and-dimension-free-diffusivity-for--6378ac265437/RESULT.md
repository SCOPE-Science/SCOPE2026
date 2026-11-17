# Exact delayed anticorrelation and dimension-free diffusivity for twisted baker maps

## Finding
Let \(M\ge2\) be any integer. For the twisted baker map of Saiki, Takahasi and Yorke on \(X=[-1,1]\times[0,1]^{M-1}\), start from normalized Lebesgue volume \(m\), and put \(Y_n=x_1(F^n x)\). Its stationary covariance sequence \(C_M(n)=\mathbb E_m[Y_0Y_n]\) has the **exact rational generating function**
\[
\boxed{\quad\sum_{n\ge0}C_M(n)z^n
=\frac{(1-z/2)^{M-1}}{3\big[(1-z/4)(1-z/2)^{M-1}+z^M/2^{M+1}\big]}\quad}
\]
initially as a power series around zero. All nonzero poles lie strictly outside the closed unit disk. The reciprocal pole locations are exactly the nonzero roots of
\[
(\lambda-1/4)(\lambda-1/2)^{M-1}+2^{-(M+1)}=0.
\]
In particular the sharp exponential correlation rate is \(\limsup_{n\to\infty}|C_M(n)|^{1/n}=\rho_M<1\), where \(\rho_M\) is the largest modulus of those roots.

The first negative covariance appears **exactly at lag \(M\)**:
\[
\boxed{C_M(n)=\frac1{3\cdot4^n}>0\quad(0\le n<M),\qquad
C_M(M)=\frac13\big(4^{-M}-2^{-(M+1)}\big)<0.}
\]
Despite these nonzero correlations, their total positive-lag sum cancels exactly:
\[
\boxed{\sum_{n=1}^{\infty}C_M(n)=0.}
\]
For each fixed \(M\ge2\), the physical first-coordinate sum obeys a central limit theorem with **the same variance in every dimension**:
\[
\boxed{\quad n^{-1/2}\sum_{k=0}^{n-1}Y_k\ \Longrightarrow\ N(0,1/3),\qquad
\lim_{n\to\infty}\frac1n\mathbb E_m\left[\left(\sum_{k=0}^{n-1}Y_k\right)^2\right]=\frac13.\quad}
\]
An explicit bounded martingale--coboundary identity, proved below, supplies the central limit theorem without a generic quantitative-mixing assumption.

## Assumptions and scope
Fix an integer \(M\ge2\) and \(X=[-1,1]\times[0,1]^{M-1}\). Coordinates are denoted \((x_1,\ldots,x_M)\). Define the piecewise-affine, generally noninvertible map
\[
F(x_1,\ldots,x_M)=\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\ge0.
\end{cases}
\]
Let \(m\) be normalized \(M\)-dimensional Euclidean volume on \(X\) (density \(1/2\)); sets on branch boundaries have measure zero. The observable is \(f(x)=x_1\), already centered under \(m\). All covariances refer to \(m\), not to uniform counting on periodic points. The limit \(n\to\infty\) is taken with \(M\) fixed. The model itself, its invariance of \(m\), and its Bernoulli/ergodic property are known from Saiki--Takahasi--Yorke; the exact affine statistics stated here are the claim.

## Proof
**1. Exact two-branch transfer.** Both full inverse branches exist for almost every \(y\in X\):
\[
G_L(y)=((y_1-1)/2,y_2,\ldots,y_M),\qquad
G_R(y)=(y_2,\ldots,y_M,(1-y_1)/2).
\]
They each have inverse Jacobian modulus \(1/2\), so the normalized-volume transfer operator \(P\), adjoint to composition by \(F\), is
\[
(Ph)(y)=\tfrac12\big[h(G_L(y))+h(G_R(y))\big].
\]
Consequently \(P1=1\), \(m\) is invariant and \(\langle h\circ F^n,k\rangle_m=\langle h,P^n k\rangle_m\) after choosing the proper adjoint orientation; more specifically \(\langle f,f\circ F^n\rangle_m=\langle P^n f,f\rangle_m\).

**2. Affine transfer matrix.** Use the centered coordinate functions \(g_1=x_1\) and \(g_j=x_j-1/2\) for \(2\le j\le M\). Direct substitution in the two inverse branches gives
\[
Pg_1=\tfrac14g_1+\tfrac12g_2,\qquad
Pg_j=\tfrac12g_j+\tfrac12g_{j+1}\ (2\le j<M),\qquad
Pg_M=-\tfrac14g_1+\tfrac12g_M.
\]
Write \(Pg_i=\sum_j(A_M)_{ij}g_j\). Thus the only nonzero entries of \(A_M\) are \((A_M)_{11}=1/4\), \((A_M)_{12}=1/2\), \((A_M)_{jj}=(A_M)_{j,j+1}=1/2\) for \(2\le j<M\), and \((A_M)_{M1}=-1/4\), \((A_M)_{MM}=1/2\). Orthogonality of the centered coordinates under product Lebesgue measure yields \(\mathbb E[g_1^2]=1/3\) and \(\mathbb E[g_1g_j]=0\) for \(j>1\). Hence
\[
C_M(n)=\tfrac13(A_M^n)_{11}.
\]
Expansion along the cyclic edge gives
\[
\det(I-zA_M)=(1-z/4)(1-z/2)^{M-1}+\frac{z^M}{2^{M+1}},
\]
while the first diagonal cofactor of \(I-zA_M\) is \((1-z/2)^{M-1}\). Taking the \((1,1)\) resolvent entry proves the stated generating function and characteristic equation.

**3. No unit-modulus affine spectrum.** Conditional Jensen shows that \(P\) contracts \(L^2(m)\). Therefore every eigenvalue of the finite-dimensional centered affine restriction \(A_M\) has modulus at most one. If a nonzero centered affine \(h=\sum_j a_jg_j\) were an eigenfunction of modulus-one eigenvalue, equality in Jensen would force \(h(G_L(y))=h(G_R(y))\) for almost every \(y\). Comparing the coefficients of \(y_2,\ldots,y_M\) gives \(a_1=a_2=\cdots=a_M\), and the coefficient of \(y_1\) gives \(a_1+a_M=0\). Thus every coefficient would vanish, a contradiction. Hence \(\rho_M<1\) and all correlations are absolutely summable. The numerator of the rational generating function vanishes only at \(z=2\), whereas the denominator equals \(1/2\) there; consequently no finite pole cancels, and the Cauchy--Hadamard formula gives the claimed sharp \(\limsup\) rate. This is a spectral statement **only for affine observables**, not the complete transfer spectrum on an infinite-dimensional Banach space.

**4. Exact onset and full cancellation.** In the graph of the matrix \(A_M\), leaving vertex 1 and returning for the first time requires the full directed cycle through vertices \(2,\ldots,M\), with length \(M\) and signed weight \(-2^{-(M+1)}\). All shorter closed walks at 1 use its loop of weight \(1/4\) exclusively. Thus \((A_M^n)_{11}=4^{-n}\) for \(n<M\) and \((A_M^M)_{11}=4^{-M}-2^{-(M+1)}\), with the latter strictly negative for all \(M\ge2\). Evaluating the absolutely convergent rational series at \(z=1\) gives
\[
\sum_{n\ge0}C_M(n)=\frac{(1/2)^{M-1}}{3[(3/4)(1/2)^{M-1}+2^{-(M+1)}]}=\frac13.
\]
Because \(C_M(0)=1/3\), the sum of all positive-lag covariances is zero.

**5. Explicit martingale--coboundary identity.** Define the bounded centered affine function \(H(x)=\sum_{j=2}^M(x_j-1/2)\), and let
\[
d(x)=f(x)+H(x)-H(Fx).
\]
The two branches immediately simplify to
\[
d(x)=\begin{cases}x_1,&x_1<0,\\x_M,&x_1\ge0.\end{cases}
\]
The inverse branches show \(Pd(y)=\tfrac12[(y_1-1)/2+(1-y_1)/2]=0\) and \(Pd^2(y)=(1-y_1)^2/4\). Under \(m\), \(d\) is uniform on \([-1,1]\), hence \(\mathbb E d=0\) and \(\mathbb E d^2=1/3\). Let \(\mathcal F_j=F^{-j}(\mathcal B(X))\), a decreasing filtration. Then \(d\circ F^j\) is a reverse-martingale difference because
\[
\mathbb E[d\circ F^j\mid\mathcal F_{j+1}]=(Pd)\circ F^{j+1}=0.
\]
The conditional second moments are \((Pd^2)\circ F^{j+1}\). By the ergodicity established in the originating paper, their Cesàro average tends almost surely to \(\int Pd^2\,dm=1/3\). Boundedness of \(d\) verifies the conditional Lindeberg condition. The martingale-difference central limit theorem, applied to the finite sum in reverse time order, yields
\[
n^{-1/2}\sum_{j=0}^{n-1}d\circ F^j\Longrightarrow N(0,1/3).
\]
Finally
\[
\sum_{j=0}^{n-1}f\circ F^j
=\sum_{j=0}^{n-1}d\circ F^j-H+H\circ F^n,
\]
and the remainder is bounded by \(2\|H\|_\infty\), independently of \(n\). This proves the central limit theorem for \(f\). Since the reverse martingale differences are pairwise orthogonal, the same bounded remainder and Cauchy--Schwarz show that \(\mathbb E[(\sum_{j<n}f\circ F^j)^2]/n\to1/3\). (Equivalently, use the absolutely summable covariance series proved above.)

## Verification
A standalone standard-library checker `check.py` constructs the rational matrix in every integer dimension from 2 to 10 and checks its determinant at \(M+1\) distinct rational arguments; since both determinant sides are polynomials of degree at most \(M\), this also verifies their identity for each tested dimension. It verifies the exact first-negative-lag coefficients, the \(z=1\) resolvent identity, both inverse-branch identities and the conditional-martingale variance polynomial with rational evaluations. Running `python check.py` prints three `OK` markers. A separate direct simulation of the original map at dimensions 2, 3 and 5 checked the covariance formula against uniform sampled initial points. These computations support the algebra for the inspected finite dimensions only; the all-dimensions theorem is established by the symbolic proof above.

## Relationship to prior work
Saiki, Takahasi and Yorke, *The twisted baker map* (arXiv:2202.04304; originally posted 9 February 2022), define this exact map and prove that normalized Lebesgue measure is invariant, that the system is Bernoulli/mixing, and that real- and complex-spectrum periodic points are both dense and equidistributed. Their paper's Sections 1--3 and Appendix A discuss symbolic cylinders, periodic Jacobians and ergodicity, but do not present the volume-sampled affine autocovariance transform, a first-anticorrelation dimension threshold, or the coordinate's exact asymptotic variance.

A distinct published calculation of the **Jacobian spectra of periodic points** for this same map, titled *Exact real-spectrum residue law for the twisted baker map* (published-finding corpus record `2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b`), classifies periodic return-derivative eigenvalues by symbolic right-visit residue. Its determinant is a derivative cocycle over selected fixed orbits; the present determinant is the volume-transfer restriction on affine observables, a different matrix with a different dynamical purpose. Previously stored same-map results involving individual periodic multiplier minima or gap histograms likewise do not imply volume-sampled coordinate correlations. Classical Gordin/martingale-difference central limit results supply the probabilistic implication once a suitable coboundary is constructed; the claimed contribution is the explicit map-specific identity and exact correlation law, not a new general central limit theorem.

## Limitations
The statement covers the specified piecewise-affine map and normalized Lebesgue initial sampling, with fixed \(M\) in the central limit theorem. The pole formula describes affine observables and does not assert a complete spectral gap for all Hölder, bounded-variation or \(L^2\) functions. The central limit theorem gives a weak limit and exact variance, not an explicit convergence rate or a large-deviation principle. The literature comparison does not exclude an unindexed equivalent application of elementary transfer-matrix or martingale methods. A separate independent mathematical review has not been carried out.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first version 9 February 2022, version 3 dated 13 January 2023, journal DOI: 10.1088/1361-6544/acb4d3. In particular equation (1.1), Theorems C and D, Section 3.3 and Appendix A. https://arxiv.org/abs/2202.04304
2. *Exact real-spectrum residue law for the twisted baker map*, published published-finding corpus research record `2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b`, 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b
3. M. I. Gordin, *The central limit theorem for stationary processes*, Doklady Akademii Nauk SSSR 188 (1969), 739--741; a classical source for martingale approximation of stationary processes.
4. H. Rootzén, *Gordin's theorem and the periodogram*, Journal of Applied Probability 13 (1976), 365--370, DOI 10.2307/3212842, on the Gordin martingale central limit method.
