# Two-branch Fourier spectra for uniform hard-core configurations on cyclic prisms

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the cyclic prism graph, and choose one of its independent vertex sets uniformly (the hard-core model at fugacity one). Let \(X_{j,r}\) be the indicator that rung \(j\in\mathbb Z/n\mathbb Z\), rail \(r\in\{0,1\}\), is occupied. Form the covariance matrix \(C_n=(\operatorname{Cov}(X_{j,r},X_{\ell,s}))\). Equivalently, \(C_n\) is one quarter of the Gram matrix of the centered coordinate Walsh characters \(\chi_{j,r}=(-1)^{X_{j,r}}\).

Put \(a=1+\sqrt2\), \(b=1-\sqrt2=-a^{-1}\), \(\varepsilon=(-1)^n\), \(Z_n=a^n+b^n+\varepsilon\), and \(c_{n,k}=\cos(2\pi k/n)\). There are precisely two complete sets of eigenvalues, each with one eigenvalue for every \(0\le k<n\):
\[
\lambda^+_{n,k}=\frac{\sqrt2\,(a^n-b^n)}{4Z_n(3+c_{n,k})}
 +\mathbf1_{k=0}\frac{n(\varepsilon Z_n-1)}{8Z_n^2},
\]
\[
\lambda^-_{n,k}=\frac1{4Z_n}\left(
\frac{a^n-\varepsilon}{\sqrt2+c_{n,k}}
+\frac{\varepsilon(1-a^{-n})}{\sqrt2-c_{n,k}}
\right).
\]
The \(+\) and \(-\) branches correspond to rail-symmetric and rail-antisymmetric spatial Fourier modes, respectively. All \(2n\) eigenvalues are strictly positive, including when different formulas happen to coincide. The sharp squared-energy condition ratio \(\kappa_n=\lambda_{\max}(C_n)/\lambda_{\min}(C_n)\) has the exact limiting value
\[
\boxed{\displaystyle\lim_{n\to\infty}\kappa_n=4+2\sqrt2.}
\]
The same ratio holds for the unscaled centered-Walsh Gram matrix; its eigenvalues are four times the displayed values. These formulas supply the entire finite-size spectrum rather than only its limit.

## Assumptions and scope
All independent sets, including the empty set, are given equal probability. Within a rung, simultaneous occupation is forbidden; along either rail, consecutive occupied sites are forbidden, including the wrap-around edge. The graph is the ordinary simple graph \(C_n\square K_2\) with \(n\ge3\). Expectations use the uniform counting measure; the spatial discrete Fourier transform uses \(n^{-1/2}\)-normalized exponentials. Eigenvalues are for the real covariance matrix \(C_n\) (not a normalized-by-\(2n\) matrix); the Fourier eigenvectors may be regarded as complex and paired by conjugation to obtain real eigenspaces.

## Proof
**Transfer matrix.** Each rung has three allowed states: empty \(E\), occupied on the upper rail \(U\), or occupied on the lower rail \(L\). Two successive states are compatible unless they occupy the same nonempty rail. In the ordered basis \((E,U,L)\), the symmetric transfer matrix is
\[
T=\begin{pmatrix}1&1&1\\1&0&1\\1&1&0\end{pmatrix}.
\]
A closed compatible sequence of \(n\) states is exactly an independent set of \(P_n\), hence \(Z_n=\operatorname{tr}(T^n)\). With \(|S\rangle=(|U\rangle+|L\rangle)/\sqrt2\), \(|A\rangle=(|U\rangle-|L\rangle)/\sqrt2\), the \((E,S)\) block of \(T\) is \(\left(\begin{smallmatrix}1&\sqrt2\\\sqrt2&1\end{smallmatrix}\right)\); its eigenvalues are \(a,b\), and the \(A\) eigenvalue is \(-1\). This proves the asserted partition function.

**Occupation operators.** Let \(S=\operatorname{diag}(0,1,1)\) and \(A=\operatorname{diag}(0,1,-1)\) act on rung states. In the transfer-eigenvector basis \((|+\rangle,|-\rangle,|A\rangle)\), where \(|\pm\rangle=(|E\rangle\pm|S\rangle)/\sqrt2\), the nonzero matrix entries of \(S\) are \(S_{++}=S_{--}=1/2\), \(S_{+-}=S_{-+}=-1/2\), and \(S_{AA}=1\). Those of \(A\) are \(A_{+,A}=A_{A,+}=1/\sqrt2\) and \(A_{-,A}=A_{A,-}=-1/\sqrt2\). Thus, writing \(s_j=X_{j,0}+X_{j,1}\), \(d_j=X_{j,0}-X_{j,1}\), one finds \(\mathbb E d_j=0\), \(\mathbb E s_j=(Z_n+\varepsilon)/(2Z_n)\), and, for every \(h\in\{0,\ldots,n-1\}\),
\[
\mathbb E(s_0s_h)=\frac{(a^n+b^n)/4+\varepsilon+(a^h b^{n-h}+b^h a^{n-h})/4}{Z_n},
\]
\[
\mathbb E(d_0d_h)=\frac1{2Z_n}\sum_{r\in\{a,b\}}
\left[r^h(-1)^{n-h}+(-1)^h r^{n-h}\right].
\]
The two rail-parity sectors are orthogonal by the rail-exchange symmetry. In the normalized symmetric/antisymmetric rail bases, the covariance eigenvalue at spatial frequency \(k\) is half the discrete Fourier transform of \(\operatorname{Cov}(s_0,s_h)\) or of \(\mathbb E(d_0d_h)\), respectively.

**Finite geometric-sum identity.** For real \(x,y\) with \(x\ne y\) and \(x^2+y^2-2xy\cos(2\pi k/n)\ne0\), and for \(z^n=1\) with \(z=e^{-2\pi i k/n}\), direct summation of two geometric progressions gives
\[
\sum_{h=0}^{n-1}(x^h y^{n-h}+y^h x^{n-h})z^h
=\frac{(x^n-y^n)(x^2-y^2)}{x^2+y^2-2xy\cos(2\pi k/n)}.
\]
Use this first with \((x,y)=(a,b)\) and then with \((a,-1)\) and \((b,-1)\), recalling \(ab=-1\), \(a^2+b^2=6\), and \(a^2+1=2\sqrt2a\). The nonconstant term in \(\operatorname{Cov}(s_0,s_h)\) is the geometric-sum contribution; the constant term equals
\[
\frac{(a^n+b^n)/4+\varepsilon}{Z_n}
-\left(\frac{Z_n+\varepsilon}{2Z_n}\right)^2
=\frac{\varepsilon Z_n-1}{4Z_n^2}.
\]
Its discrete Fourier transform contributes only at \(k=0\). These calculations give both formulas exactly, including their factors of two and the special zero-frequency correction.

**Strict rank.** The empty independent set and every one-vertex independent set occur with positive probability. If a linear combination of the \(2n\) indicators had zero variance, comparing its value on the empty set and on each singleton forces every coefficient to vanish. Therefore \(C_n\) is positive definite. The transfer/Fourier construction displays \(2n\) eigenvectors, completing the spectral classification.

**Sharp asymptotic ratio.** Since \(|b|=a^{-1}<1\) and \(Z_n=a^n(1+O(a^{-n}))\), uniformly over all admissible spatial frequencies, the two branches converge, up to the \(k=0\) symmetric correction \(O(na^{-n})\), to
\[
f_+(c)=\frac{\sqrt2}{4(3+c)},\qquad
f_-(c)=\frac1{4(\sqrt2+c)},\qquad -1\le c\le1.
\]
Both functions decrease strictly with \(c\). Their global smallest value is \(f_+(1)=\sqrt2/16\), and their global largest value is \(f_-(-1)=1/[4(\sqrt2-1)]\); the other branch extrema are strictly between these. The Fourier grids approach both endpoints as \(n\to\infty\) (with \(k=0\) exactly attaining \(c=1\) and \(k=\lfloor n/2\rfloor\) approaching \(c=-1\)). Uniform convergence now proves the claimed limiting ratio, namely \(4+2\sqrt2\). No assertion about finite-\(n\) extremizing frequencies is required for this limit.

## Verification
The standalone standard-library program `check.py` directly enumerates all compatible rung strings for \(3\le n\le9\). It computes each of the two spatial Fourier covariance branches without using the transfer-matrix formula, and compares them with the displayed expressions. It also checks sample larger lengths numerically. Finite enumeration is not used to justify the all-\(n\) theorem: that is supplied by the transfer identity and positive-definiteness argument above.

## Relationship to prior work
The general hard-core distribution and occupancy viewpoint are developed by Davies, Kang, Pirot and Sereni (first publicly circulated 2020-03-31). Standard independence-polynomial references already give the single-variable prism partition function; its enumeration is not claimed as new. The separate published calculation of first-coordinate Fourier stability on a single cycle (the Lucas cube) concerns \(C_n\), not the two-rail prism \(C_n\square K_2\), and does not supply these rail-parity eigenvalue branches or the limiting prism ratio. The contribution here is the exact full two-branch covariance/Fourier-frame spectrum and its sharp asymptotic conditioning, not the transfer-matrix method itself.

## Limitations
The theorem covers uniform independent sets at fugacity one, not the general positive-activity model or larger ladder widths. It gives the finite spectrum explicitly but does not classify finite-\(n\) extremal indices. Historical equivalent hard-core ladder structure-factor calculations are possible and remain a priority concern. No independent scientific audit has been performed.

## References
1. E. Davies, R. J. Kang, F. Pirot, J.-S. Sereni, *Graph structure via local occupancy*, arXiv:2003.14361, first version 2020-03-31. https://arxiv.org/abs/2003.14361
2. E. W. Weisstein, *Independence Polynomial*, Wolfram MathWorld, entry displaying the closed prism polynomial. https://mathworld.wolfram.com/IndependencePolynomial.html
3. *Exact Lucas-cube Fourier precision and parity-split sharp frame conditioning*, published research record, 2026-11-01; public abstract available via published-finding corpus (related one-cycle setting, not a proof of the prism claim).
