# Reentrant positivity and the sharp half-weight boundary for four symmetric Gaussian quadrature nodes

## Finding
For the Gaussian covariance kernel \(k_\lambda(x,y)=e^{-\lambda(x-y)^2}\) on \([-1,1]\), with the uniform probability integration measure and fixed sites \(\{-4/5,-9/16,9/16,4/5\}\), unconstrained Bayesian quadrature has **four positive weights at small shape** and again **four positive weights at large shape**, yet **exactly two positive and two negative weights** at shape \(\lambda=2\). This sign reentrance persists under sufficiently small independent perturbations of the two positive site radii. The example realizes, with symmetric sites, the sharp half-positive lower bound for four-point quadrature based on a totally positive kernel. At least two distinct outer-weight zeros follow; we do not assert there are exactly two.

## Assumptions and scope
The integration functional is \(I(f)=\frac12\int_{-1}^1f(x)\,dx\). For \(\lambda>0\) and distinct nodes \(X=(-b,-a,a,b)\) with \(0<a<b<1\), the Gaussian kernel is strictly positive definite; Bayesian quadrature's unique weights solve \(K_\lambda w=m_\lambda\), where \((K_\lambda)_{ij}=k_\lambda(X_i,X_j)\) and \((m_\lambda)_i=I(k_\lambda(X_i,\cdot))\). No nonnegativity constraints or postprocessing of the weights are imposed. By reflection symmetry the weights, in the stated increasing node order, are **\((v,u,u,v)\)**. The focal radii are \(a=9/16\), \(b=4/5\); the variable \(\lambda\) is the Gaussian inverse squared lengthscale.

## Proof
### 1. Reduction to two scalar numerators
Put
\[
 A=1+e^{-4\lambda a^2},\quad B=1+e^{-4\lambda b^2},\quad
 C=e^{-\lambda(b-a)^2}+e^{-\lambda(b+a)^2},\quad
 F(v)=\frac12\int_{-1}^1e^{-\lambda(x-v)^2}\,dx.
\]
The equations for the two distinct weights reduce to
\[
 \begin{pmatrix} A&C\\C&B\end{pmatrix}
 \begin{pmatrix}u\\v\end{pmatrix}=
 \begin{pmatrix}F(a)\\F(b)\end{pmatrix}.
\]
The two-by-two matrix is the restriction of the positive definite four-by-four kernel Gram matrix to reflection-even vectors. Hence \(\Delta=AB-C^2>0\) for every \(\lambda>0\), and
\[
 u=\frac{BF(a)-CF(b)}{\Delta},\qquad
 v=\frac{AF(b)-CF(a)}{\Delta}.
\]
### 2. Positivity at small shape
Taylor expansion of the Gaussian and integration of each monomial give, as \(\lambda\downarrow0\),
\[
 \begin{aligned}
 \Delta&=8(b^2-a^2)^2\lambda^2+O(\lambda^3),\\
 BF(a)-CF(b)&=\tfrac43(b^2-a^2)(3b^2-1)\lambda^2+O(\lambda^3),\\
 AF(b)-CF(a)&=\tfrac43(b^2-a^2)(1-3a^2)\lambda^2+O(\lambda^3).
 \end{aligned}
\]
Consequently
\[
 \lim_{\lambda\downarrow0}u=\frac{3b^2-1}{6(b^2-a^2)},\qquad
 \lim_{\lambda\downarrow0}v=\frac{1-3a^2}{6(b^2-a^2)}.
\]
For \(a=9/16\), \(b=4/5\), these limits are, respectively, \(2944/6213>0\) and \(325/12426>0\). Positivity follows for all sufficiently small positive shapes. The limits are the usual symmetric polynomial-cubature weights; positivity of the limits alone is not claimed as new.

### 3. Exactly two negative weights at shape two
For \(\lambda=2\), exact-rational Taylor interval arithmetic with truncation order 80 proves
\[
 AF(b)-CF(a)<-1/100,\qquad
 BF(a)-CF(b)>1/100,\qquad
 \Delta>1/100.
\]
Each assertion is tested on rational enclosures of the exact functions. Therefore \(v(2)<0<u(2)\): precisely the two outer weights are negative. To reproduce the inequalities, execute `python3 verify.py` from this package. That standalone standard-library program computes \(P_{80}(z)=\sum_{j=0}^{80}(-z)^j/j!\) with error at most \(z^{81}/81!\) for \(e^{-z}\), \(z\ge0\), and integrates the polynomial termwise for \(F\), with the corresponding bound \((\lambda(1+v)^2)^{81}/81!\). It propagates bounds for all products by exact `fractions.Fraction` interval arithmetic. Hence the computer check is a finite rational *certificate* of the three strict inequalities, not a floating-point sign guess. The printed floating-point centers are for inspection only.

### 4. Positivity at large shape and robust reentrance
For every fixed \(v\in(-1,1)\), dominated Gaussian scaling gives \(F(v)=\sqrt\pi/(2\sqrt\lambda)(1+o(1))\) as \(\lambda\to\infty\). As \(A,B\to1\), \(C\to0\), and \(\Delta\to1\), both \(u\) and \(v\) are eventually strictly positive. Continuity in \(\lambda>0\) therefore forces at least one outer-weight zero below 2 and at least one above 2, with a negative open interval around shape 2. The inequalities \(0<a<b<1\), \(a^2<1/3<b^2\), and the three strict certified inequalities at \(\lambda=2\) persist in a nonempty open neighborhood of the chosen radii. Every point of that neighborhood has the same positive–negative–positive outer-weight sign pattern.

## Verification
The file `verify.py` is self-contained and requires no data, network, or third-party dependencies. It provides exact rational enclosures at \(\lambda=2\) and asserts strict positivity of the inner numerator and the determinant, together with strict negativity of the outer numerator. The first and last positivity regimes are established analytically, not from numerical scans. An independent audit has not been performed.

## Relationship to prior work
Huszár and Duvenaud (2012) introduced the weighted Bayesian quadrature interpretation and exhibited that weights need not all be nonnegative. Karvonen, Kanagawa, and Särkkä (2019) proved that at least \(\lfloor(n+1)/2\rfloor\) weights are positive for univariate totally positive kernels and that local optimality of the nodes suffices for complete positivity. The present four-node example attains the former bound with two positive weights at finite shape, but does not contradict the latter criterion because the prescribed nodes are not locally optimal at that shape. Karvonen and Särkkä (2020) established convergence to polynomial-interpolation weights in the increasingly flat limit; that known asymptotic is consistent with our strictly positive flat-limit formulas and does not imply the intervening negative regime. Oettershagen (2017) studies optimal kernel cubature design, with a different focus from fixed-site shape-induced reentrance. Our new assertion is the explicitly certified, perturbation-robust **sign return** in a fixed symmetric four-site Gaussian design—not the Gaussian kernel formula, the possibility of negative weights, or the flat limit.

## Limitations
The result is existential in the shape coordinate: it certifies at least two, not exactly two, outer-weight zeros. It does not claim the prescribed locations are locally optimal, nor an optimal noise-amplification bound, and it does not claim analogous reentrance for all four-node configurations or other kernels. Literature coverage can miss older or unindexed equivalent examples; publication priority is provisional pending independent verification.

## References
1. F. Huszár and D. Duvenaud, *Optimally-Weighted Herding is Bayesian Quadrature*, 2012, arXiv:1204.1664, https://arxiv.org/abs/1204.1664 . First publicly released 2012-04-07.
2. T. Karvonen, M. Kanagawa, and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, *Statistics and Computing* 29 (2019), 1317–1333, https://doi.org/10.1007/s11222-019-09901-0 ; arXiv:1812.08509.
3. T. Karvonen and S. Särkkä, *Worst-case optimal approximation with increasingly flat Gaussian kernels*, arXiv:1906.02096, https://arxiv.org/abs/1906.02096 .
4. J. Oettershagen, *Construction of Optimal Cubature Algorithms with Applications to Econometrics and Uncertainty Quantification*, doctoral dissertation, University of Bonn (2017), https://www.ins.uni-bonn.de/media/public/publication-media/diss_oettershagen.pdf?pk=460 .
