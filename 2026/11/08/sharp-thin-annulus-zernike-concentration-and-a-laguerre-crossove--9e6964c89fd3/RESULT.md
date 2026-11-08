# Sharp thin-annulus Zernike concentration and a Laguerre crossover

## Finding
Fix integers \(m\geq0\) and \(n\geq1\). In the azimuthal Zernike sector
\[
\mathcal Z_{m,n}=\left\{f(re^{i\theta})=r^m e^{im\theta}p(r^2):p\in\mathbb C[u],\ \deg p\le n\right\}\subset L^2(\mathbb D),
\]
let \(C_{m,n,\varepsilon}\) be the positive concentration operator defined by
\[
\langle C_{m,n,\varepsilon}f,f\rangle_{L^2(\mathbb D)}
=\int_{\sqrt{1-\varepsilon}<|z|<1}|f(z)|^2\,dA(z),
\qquad 0<\varepsilon<1.
\]
Use the ordinary, unnormalized area measure on both sides. Write \(\lambda_{\min}\) and \(\lambda_{\max}\) for its smallest and largest eigenvalues. At each *fixed* pair \((m,n)\), as \(\varepsilon\downarrow0\),
\[
\boxed{\lambda_{\max}\sim(n+1)(n+m+1)\varepsilon,}
\qquad
\boxed{\lambda_{\min}\sim
\frac{\varepsilon^{2n+1}}{(2n+1)\binom{2n}{n}^{2}\mathrm B(m+1,2n+1)}.}
\]
Consequently, the exact leading spectral condition number is
\[
\boxed{\kappa(C_{m,n,\varepsilon})\sim
(n+1)(n+m+1)(2n+1)\binom{2n}{n}^{2}
\mathrm B(m+1,2n+1)\,\varepsilon^{-2n}.}
\]
For the continuous restriction map from the disk norm to the annulus norm, the singular-value condition number is the square root of this expression.

A *different*, simultaneous high-azimuthal-order limit exists for the first nonconstant radial band \(n=1\). Let \(\tau>0\) be fixed and take \(m\to\infty\) with \(\varepsilon=\tau/(m+1)\). Both eigenvalues converge, respectively, to
\[
\boxed{\Lambda_\pm(\tau)=1-e^{-\tau}(1+\tau^2/2)
\ \pm\ \tau e^{-\tau}\sqrt{1+\tau^2/4}.}
\]
They are strictly between zero and one with \(\Lambda_-<\Lambda_+\). The limiting condition number equals \(\Lambda_+(\tau)/\Lambda_-(\tau)\), and
\[
\Lambda_-(\tau)\sim \tau^3/24,\quad
\Lambda_+(\tau)\sim2\tau,\quad
\frac{\Lambda_+(\tau)}{\Lambda_-(\tau)}\sim48\tau^{-2}
\quad(\tau\downarrow0),
\]
whereas both \(\Lambda_\pm(\tau)\to1\) when \(\tau\to\infty\). The fixed-order and high-order asymptotic regimes are not interchangeable without accounting for the product of azimuthal order and annular thickness.

## Assumptions and scope
The complex Hilbert-space inner product is the disk \(L^2\) inner product, and the observation is continuous, noiseless area restriction to a concentric outer annulus. The Fourier azimuthal order \(m\), radial degree cutoff \(n\), and squared-radius thickness \(\varepsilon\) are exactly as defined above; \(\mathcal Z_{m,n}\) has dimension \(n+1\). The first displayed asymptotics hold with \(m,n\) fixed; the explicit crossover is only asserted for \(n=1\) and \(\tau>0\) fixed. No uniformity in growing radial degree is claimed.

## Proof
**1. Radial Gram reduction.** Set \(u=r^2\), \(v=1-u\). The angular integral and radial Jacobian yield the common factor \(\pi\), which cancels in every Rayleigh quotient. In the basis \(1,v,\dots,v^n\), define the full-disk and observed Gram matrices
\[
G_{ij}=\int_0^1 u^m(1-u)^{i+j}\,du=\mathrm B(m+1,i+j+1),
\]
\[
B_{ij}(\varepsilon)=\int_0^\varepsilon v^{i+j}(1-v)^m\,dv,
\qquad0\le i,j\le n.
\]
Both are strictly positive definite for \(0<\varepsilon<1\). The eigenvalues of \(C_{m,n,\varepsilon}\) are exactly the generalized eigenvalues of the pair \((B(\varepsilon),G)\), or equivalently of \(G^{-1}B(\varepsilon)\). They lie in \((0,1)\): a nonzero polynomial has strictly positive energy on both the observed interval and its complement.

**2. Largest eigenvalue.** As \(\varepsilon\downarrow0\), the matrix \(\varepsilon^{-1}B(\varepsilon)\) converges entrywise to the rank-one matrix \(e_0e_0^T\). Thus \(\varepsilon^{-1}G^{-1}B(\varepsilon)\) has one nonzero limiting eigenvalue, \((G^{-1})_{00}\). The degree-\(k\) shifted Jacobi polynomial \(P_k^{(0,m)}(2u-1)\) has endpoint value one and squared \(L^2(u^mdu)\) norm \(1/(2k+m+1)\). Therefore the endpoint Christoffel kernel equals
\[
(G^{-1})_{00}=\sum_{k=0}^n(2k+m+1)=(n+1)(n+m+1),
\]
which proves the first formula. Here the endpoint functional is evaluation at \(u=1\), i.e. coefficient \(e_0^T\) in the \(v\)-basis.

**3. Smallest eigenvalue.** Let \(D_\varepsilon=\mathrm{diag}(\varepsilon^{j+1/2})_{j=0}^n\). Direct integration gives
\[
B(\varepsilon)=D_\varepsilon(H+O_{m,n}(\varepsilon))D_\varepsilon,
\qquad H_{ij}=\frac1{i+j+1}.
\]
The error is entrywise, hence also in matrix norm at fixed dimension. Consequently,
\[
\varepsilon^{2n+1}B(\varepsilon)^{-1}G
\longrightarrow (H^{-1})_{nn}\,e_ne_n^TG.
\]
Indeed, in the \((i,k)\)-entry the only term surviving the powers \(\varepsilon^{2n-i-j}\) is \(i=j=n\). The limiting rank-one matrix has its unique nonzero eigenvalue \((H^{-1})_{nn}G_{nn}\); all others vanish. Since \(B^{-1}G\) has positive real eigenvalues and these are exactly the reciprocals of the eigenvalues of \(G^{-1}B\), it follows that
\[
\lambda_{\min}\sim\varepsilon^{2n+1}/[(H^{-1})_{nn}G_{nn}].
\]
For the moment Gram matrix of \(1,t,\dots,t^n\) on \([0,1]\), the Schur complement formula identifies \(1/(H^{-1})_{nn}\) with the squared norm of the unique monic orthogonal polynomial of degree \(n\). That polynomial is \(P_n(2t-1)/\binom{2n}{n}\), whose squared norm is \(1/[(2n+1)\binom{2n}{n}^2]\). Hence
\[
(H^{-1})_{nn}=(2n+1)\binom{2n}{n}^2,
\qquad G_{nn}=\mathrm B(m+1,2n+1).
\]
This proves the second formula. Dividing the two leading asymptotics proves the condition-number formula.

**4. High-order Laguerre crossover.** For \(n=1\), set \(x=(m+1)(1-u)\), so observation \(u\in[1-\tau/(m+1),1]\) becomes \(x\in[0,\tau]\). Up to an identical positive scalar in both Gram matrices, the full and observed measures become
\[
\left(1-\frac{x}{m+1}\right)^m\mathbf1_{[0,m+1]}(x)\,dx,
\quad\text{and}\quad
\left(1-\frac{x}{m+1}\right)^m\mathbf1_{[0,\tau]}(x)\,dx.
\]
For monomials of degrees at most two, dominated convergence gives the full moments \(\int_0^\infty x^j e^{-x}dx=j!\) and the restricted moments \(\int_0^\tau x^j e^{-x}dx\); the domination follows from \((1-x/(m+1))^m\le e^{-mx/(m+1)}\le e^{-x/2}\) for \(m\ge1\). The generalized eigenvalues therefore converge to those of the limiting Laguerre moment pair. The orthonormal basis \(1,1-x\) for \(e^{-x}dx\) has restricted Gram matrix
\[
\begin{pmatrix}
1-e^{-\tau}&\tau e^{-\tau}\\
\tau e^{-\tau}&1-(1+\tau^2)e^{-\tau}
\end{pmatrix}.
\]
Its two eigenvalues, calculated by the quadratic formula, are exactly \(\Lambda_\pm(\tau)\). Strict positivity and the upper bound one follow from the nonzero mass of every nonzero linear polynomial on both \([0,\tau]\) and \((\tau,\infty)\). Taylor expansion yields the displayed small-\(\tau\) constants, and exponential decay yields the large-\(\tau\) limit. This completes the proof.

## Verification
Run `python verify.py` in a Python environment with `mpmath`. The self-contained checker evaluates the two positive-definite moment matrices using beta and incomplete-beta integrals, computes generalized concentration eigenvalues in high precision, verifies the Hilbert inverse identity for several degrees, tests the two sharp fixed-order coefficients, and compares the explicit crossover with independently evaluated finite-order spectra. Its expected final line is `ANNULAR_ZERNIKE_CHECKS_PASS 176`. The proof above covers every allowed integer order and cutoff, not just those tested.

## Relationship to prior work
Papadopoulos, Gutleb, Slevinsky and Olver (first publicly posted 11 October 2023, arXiv:2310.07541) construct annular Zernike/Jacobi orthogonal bases and analyze sparse differential operators on annuli. Their reported conditioning results concern discretized Laplacian matrices with an annular-adapted basis. Here the operator is instead continuous *restriction from the disk norm to a shrinking outer annulus*, in a fixed disk-Zernike sector, and the precise smallest and largest concentration eigenvalue asymptotics and high-azimuthal Laguerre crossover are the objects of study. The 2014 Fourier-Laguerre Slepian analysis of Khalid, Kennedy and McEwen, arXiv:1403.5553, concerns three-dimensional ball localization with a different spectral band. The earlier optical annular-basis literature (e.g. Díaz and Mahajan, 2013) establishes orthogonal aberration bases for annular sectors, not an identified sharp shrinking-annulus spectral conditioning law in the stated disk norm. These comparisons do not constitute exhaustive historical priority certification.

## Limitations
The results concern pure continuous radial Zernike subspaces with one fixed azimuthal mode and noiseless full-annulus measurements. No theorem is asserted for arbitrary finite sensor placement, mixtures of azimuthal sectors, noisy or nonlinear inverse problems, angularly incomplete annuli, or simultaneous growth of radial cutoff. Existing results on Jacobi moments, Christoffel kernels and Hilbert-matrix inversion are essential ingredients and are not claimed as new. An equivalent result could be encoded in classical truncated moment-matrix or optical aberration literature; independent historical-priority assessment has not occurred.

## References
1. I. P. A. Papadopoulos, T. S. Gutleb, R. M. Slevinsky and S. Olver, *Building hierarchies of semiclassical Jacobi polynomials for spectral methods in annuli*, arXiv:2310.07541 (first posted 11 October 2023); SIAM J. Sci. Comput. 46 (2024), A3448–A3476. https://arxiv.org/abs/2310.07541.
2. Z. Khalid, R. A. Kennedy and J. D. McEwen, *Slepian spatial-spectral concentration on the ball*, arXiv:1403.5553 (2014); Appl. Comput. Harmon. Anal. 40 (2016), 470–504. https://arxiv.org/abs/1403.5553.
3. J. A. Díaz and V. N. Mahajan, *Orthonormal aberration polynomials for optical systems with circular and annular sector pupils*, Appl. Opt. 52 (2013), 1136–1147. https://doi.org/10.1364/AO.52.001136.
