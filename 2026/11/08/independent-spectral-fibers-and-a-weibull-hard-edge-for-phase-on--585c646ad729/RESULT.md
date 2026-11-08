# Independent spectral fibers and a Weibull hard edge for phase-only cyclic Gabor bases

## Finding

Fix an integer \(p\geq2\), let \(N=2p\), and choose independent random angles \(\Theta_0,\ldots,\Theta_{N-1}\), each Haar-uniform modulo \(2\pi\). Form the unit-norm window \(g\in\mathbb C^{\mathbb Z_N}\) by
\[
 g(j)=N^{-1/2}e^{i\Theta_j}.
\]
With cyclic translation \((T_tg)(j)=g(j-t)\) and modulation \((M_\ell g)(j)=e^{2\pi i\ell j/N}g(j)\), consider the square Gabor synthesis matrix \(G_p\) whose \(2p\) columns are
\[
 \{M_{2k}T_tg:\ t\in\{0,1\},\quad 0\leq k<p\}.
\]
Let \(S_p=G_pG_p^*\), and denote its optimal lower and upper frame bounds by \(A_p=\lambda_{\min}(S_p)\) and \(B_p=\lambda_{\max}(S_p)\). The **exact joint spectral law** is
\[
 \operatorname{spec}(S_p)\ \stackrel{\rm law}{=}\
 \biguplus_{r=0}^{p-1}\left\{1-|\cos(U_r/2)|,\;1+|\cos(U_r/2)|\right\},
 \qquad U_0,\ldots,U_{p-1}\overset{\rm iid}{\sim}\operatorname{Unif}[0,2\pi).
\]
The displayed independence is exact for every \(p\), not an asymptotic approximation, despite adjacent Fourier fibers sharing window coordinates. In particular \(G_p\) is invertible almost surely, \(B_p=2-A_p\) almost surely, and for every \(0\leq x\leq1\),
\[
 \boxed{\mathbb P(A_p>x)=\left(\frac2\pi\arcsin(1-x)\right)^p.}
\]
Consequently, for every \(t\geq0\),
\[
 \boxed{\lim_{p\to\infty}\mathbb P(p^2A_p>t)
       =\exp\left(-\frac{2\sqrt{2t}}\pi\right),}
\]
and, for each \(s>0\), writing \(K_p=B_p/A_p\) for the ratio of the *squared* Gabor frame bounds,
\[
 \boxed{\lim_{p\to\infty}\mathbb P(K_p/p^2\leq s)
       =\exp\left(-\frac4{\pi\sqrt{s}}\right).}
\]
For every real \(r>0\), the positive hard-edge moments converge:
\[
 \boxed{\lim_{p\to\infty}\mathbb E[(p^2A_p)^r]
       =\Gamma(2r+1)\left(\frac{\pi^2}{8}\right)^r.}
\]
For every fixed \(p\geq2\), \(\mathbb E[K_p^r]<\infty\) holds if and only if \(0<r<1/2\). This proves that the expected frame-operator condition ratio is infinite at every dimension even though the square Gabor system is a basis almost surely.

There is also an exact determinant consequence of the same joint law:
\[
 \mathbb E[\log\det S_p]=-2p\log2,\qquad
 \operatorname{Var}(\log\det S_p)=\frac{\pi^2p}{3},
\]
and
\[
 \frac{\log\det S_p+2p\log2}{\pi\sqrt{p/3}}
 \ \xrightarrow{\rm d}\ \mathcal N(0,1).
\]
These are consequences of the single exact independent-fiber theorem rather than separate assumptions.

## Assumptions and scope

All random phases are independent and *continuously* uniform on the unit circle. The complex window has exactly constant modulus \(N^{-1/2}\); no independent Gaussian amplitudes are present. All indices of the underlying cyclic group are taken modulo \(N\). The parameter \(p\) is an arbitrary integer at least two. The frequency subgroup consists of all even residues \(\{0,2,\ldots,2(p-1)\}\subset\mathbb Z_{2p}\), and the translation set is exactly \(\{0,1\}\). With these conventions there are exactly \(2p\) unit-norm synthesis vectors in \(\mathbb C^{2p}\), and the mean frame eigenvalue is one. The condition ratio \(K_p\) is the ratio \(B_p/A_p\), not the spectral condition number of the synthesis matrix, which is \(\sqrt{K_p}\).

## Proof

**1. Exact two-dimensional Fourier fibers.** For arbitrary deterministic \(g\), orthogonality of the \(p\) even modulation characters gives
\[
 \sum_{k=0}^{p-1}e^{2\pi ik(j-j')/p}
  =p\mathbf1_{\{j\equiv j'\pmod p\}}.
\]
Consequently \(S_p\) preserves the \(p\) mutually orthogonal spaces \(H_r=\operatorname{span}\{e_r,e_{r+p}\}\) for \(0\leq r<p\). Its restriction to \(H_r\) is the Gram sum of two columns
\[
 S_p|_{H_r}=w_{r,0}w_{r,0}^*+w_{r,1}w_{r,1}^*,\qquad
 w_{r,t}=\sqrt p\begin{pmatrix}g(r-t)\\g(r+p-t)\end{pmatrix}.
\]
Each column has norm one because each window entry has modulus \((2p)^{-1/2}\). Thus the two eigenvalues are \(1\pm|\langle w_{r,0},w_{r,1}\rangle|\), with no omitted normalization factor.

**2. Explicit phase variables and the cyclic seam.** Write \(\theta_r=\Theta_r\) and \(\phi_r=\Theta_{r+p}\) for \(0\leq r<p\), and put \(\psi_r=\theta_r-\phi_r\) modulo \(2\pi\). The \(\psi_r\) are independent Haar angles. For \(1\leq r<p\), the two columns in the preceding Gram sum are proportional to
\[
 \begin{pmatrix}e^{i\theta_r}\\e^{i\phi_r}\end{pmatrix},\quad
 \begin{pmatrix}e^{i\theta_{r-1}}\\e^{i\phi_{r-1}}\end{pmatrix},
\]
so that
\[
 |\langle w_{r,0},w_{r,1}\rangle|
   =\left|\cos\frac{\psi_r-\psi_{r-1}}2\right|.
\]
At the cyclic seam \(r=0\), the shifted vector instead uses the ordered coordinates \((g(2p-1),g(p-1))\), which are swapped between the two half-blocks. Therefore
\[
 |\langle w_{0,0},w_{0,1}\rangle|
   =\left|\cos\frac{\psi_0+\psi_{p-1}}2\right|.
\]
This plus sign at the seam is essential. Put \(U_0=\psi_0+\psi_{p-1}\) and \(U_r=\psi_r-\psi_{r-1}\) for \(1\leq r<p\), all modulo \(2\pi\).

**3. Independence despite overlapping coordinates.** The integer linear map \(\psi\mapsto U\) has determinant of absolute value two: the equations \(U_1=\cdots=U_{p-1}=0\) force every \(\psi_r\) equal, after which \(U_0\) is twice that value. Equivalently, the matrix is obtained from a first-difference triangular system with a final doubled coordinate. In particular its transpose is injective on \(\mathbb Z^p\). For every nonzero \(k\in\mathbb Z^p\), Haar independence of \(\psi\) gives
\[
 \mathbb E[e^{i k\cdot U}]
   =\mathbb E[e^{i (M^{\!T}k)\cdot\psi}]=0,
\]
where \(M\) is the integer matrix of the map. These are exactly the nontrivial Fourier coefficients of Haar measure on the \(p\)-torus. Hence \(U_0,\ldots,U_{p-1}\) are independent uniform angles, proving the joint eigenvalue law. This argument handles the noninjective torus map correctly: injectivity is not required for Haar pushforward, only surjectivity, here guaranteed by the nonzero determinant.

**4. Exact extremes and the hard edge.** If \(U\) is uniform on \([0,2\pi)\), put \(X=1-|\cos(U/2)|\). For \(0\leq x\leq1\), elementary angular measure gives
\[
 \mathbb P(X\leq x)=\frac2\pi\arccos(1-x),\qquad
 \mathbb P(X>x)=\frac2\pi\arcsin(1-x).
\]
Since \(A_p\) is the minimum of \(p\) independent copies of \(X\), the displayed finite survival formula follows. Every two-eigenvalue block sums to two, hence \(B_p=2-A_p\). Near zero,
\[
 \frac2\pi\arccos(1-x)=\frac{2\sqrt2}\pi\sqrt{x}+O(x^{3/2}).
\]
Substitution of \(x=t/p^2\) proves the Weibull survival limit. The continuous mapping theorem, at strictly positive arguments, gives the stated Fréchet-type condition-ratio limit.

**5. Moments and their sharp domain.** From \(\cos u\geq1-u^2/2\) it follows that \(\arccos(1-x)\geq\sqrt{2x}\) for \(0\leq x\leq1\). Thus \(\mathbb P(p^2A_p>t)\leq\exp(-2\sqrt{2t}/\pi)\) whenever \(0\leq t\leq p^2\), and the probability is zero above \(p^2\). This common integrable tail controls every positive power moment and yields the gamma integral in the theorem. On the other hand the finite survival formula gives, as \(x\downarrow0\),
\[
 \mathbb P(A_p\leq x)=\frac{2\sqrt2\,p}{\pi}\sqrt{x}+O_p(x).
\]
Consequently the negative moment \(\mathbb E[A_p^{-r}]\) is finite precisely for \(r<1/2\). Since \(A_p\leq1\) and \(A_p^{-1}\leq K_p\leq2A_p^{-1}\), the same threshold holds for positive moments of \(K_p\).

**6. Log-volume corollary.** Every block has determinant \(\sin^2(U_r/2)\). The i.i.d. logarithms have mean \(-2\log2\), because \(\pi^{-1}\int_0^\pi\log(2\sin u)\,du=0\), and variance \(\pi^2/3\), because the Fourier series \(\log(2\sin u)=-\sum_{n\geq1}\cos(2nu)/n\) has \(L^2\)-norm squared \(\pi^2/12\) with normalized Lebesgue measure. The classical i.i.d. central limit theorem proves the displayed log-determinant limit.

## Verification

The standalone `CHECK.py` uses only the Python 3 standard library. Its fixed-seed tests reconstruct the full \(2p\times2p\) Gabor synthesis and frame operators directly for \(2\leq p\leq10\), compare every exact two-dimensional block and both calculated eigenvalues, verify the integer phase-map determinants for \(2\leq p\leq22\), and check representative angular distribution and hard-edge constants. Run `python3 CHECK.py` from a directory containing the file. The expected terminal line is `PHASE_GABOR_IID_SPECTRUM_CHECKS_PASSED 27979`. These finite checks do not prove the all-dimensional results; the argument in the preceding section does.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez (first public version May 15, 2026) establish general block equivalence when the modulation set is a subgroup, including the type of fiber decomposition used here. Their results do not give an independent spectral distribution, exact extreme-frame-bound laws or hard-edge asymptotics for Steinhaus windows. Salanevich (2019) and Salanevich and Strachan (2025) investigate finite random Gabor frame singular values and bounds, including Steinhaus windows, using general matrix estimates and random or highly redundant time-frequency sets. Their inspected results do not provide the exact law for this square two-translation/even-modulation geometry. The present probabilistic conclusion depends critically on the special plus-sign cyclic seam and the resulting full-rank integral torus transformation; it is not a consequence of block equivalence alone.

## Limitations

The exact independence mechanism is established only for i.i.d. continuous unit-modulus phases, with the specified even-modulation subgroup and adjacent two-translation geometry. Other phase alphabets, unequal amplitudes, other modulation sets and more than two translations are not covered. The extremes describe the frame operator, so square-root conversion is necessary for condition numbers of synthesis or analysis matrices. Claims of independent publication priority are not made; unindexed or differently normalized treatments could overlap. No numerical experiment is used as evidence of infinite-dimensional or asymptotic correctness.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first version May 15, 2026; full text of version 2 dated October 24, 2026. https://arxiv.org/abs/2605.16139
2. P. Salanevich, *Extreme Singular Values of Random Time-Frequency Structured Matrices*, arXiv:1902.01062, February 4, 2019. https://arxiv.org/abs/1902.01062
3. P. Salanevich, N. Q. D. Strachan, *Robustness to noise and erasures of Gabor frames in finite dimensions*, arXiv:2509.01325, September 1, 2025. https://arxiv.org/abs/2509.01325
