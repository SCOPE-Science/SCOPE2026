# Two spectral bands and an exact conditioning law for alternating Laplace-kernel sampling

## Finding
For every \(\alpha>0\) and \(0\leq\delta<1/2\), let \(g_\alpha(t)=e^{-\alpha|t|}\), and consider the critical-density, period-two sampling grid
\[
x_{2k}=2k+\delta,\qquad x_{2k+1}=2k+1-\delta\qquad(k\in\mathbb Z).
\]
Let \(T_{\alpha,\delta}:\ell^2(\mathbb Z)\to\ell^2(\mathbb Z)\) be the bounded coefficient-to-sample operator
\[
(T_{\alpha,\delta}c)_j=\sum_{n\in\mathbb Z}c_n g_\alpha(x_j-n).
\]
Write
\[
\eta=\alpha/2,\qquad \tau=\alpha(1/2-\delta),\qquad
m=\frac{\sinh\tau}{\sinh\eta},\qquad p=\frac{\cosh\tau}{\cosh\eta}.
\]
Then the **complete squared-singular-value spectrum** is the union of exactly two closed bands:
\[
\boxed{\sigma(T_{\alpha,\delta}^{*}T_{\alpha,\delta})=
[m^2\tanh^2\eta,\ m^2\tanh^2\alpha]
\ \cup\ [p^2\tanh^2\alpha,\ p^2\coth^2\eta].}
\]
Consequently the exact best constants in the coefficient sampling inequality \(A\|c\|_2^2\le\|Tc\|_2^2\le B\|c\|_2^2\) are
\[
\boxed{A=\frac{\sinh^2\tau}{\cosh^2\eta},\qquad
B=\frac{\cosh^2\tau}{\sinh^2\eta}.}
\]
For \(0<\delta<1/2\), the spectral gap \((m^2\tanh^2\alpha,p^2\tanh^2\alpha)\) is genuinely open. At \(\delta=0\), \(m=p=1\) and the two bands meet. As the paired sampling sites coalesce, the sharp lower bound has the quadratic law
\[
\boxed{A=\frac{\alpha^2}{\cosh^2(\alpha/2)}(1/2-\delta)^2+O((1/2-\delta)^4).}
\]
The spectral endpoints are sharp approximate spectral values, not generally \(\ell^2\)-eigenvalues.

## Assumptions and scope
All statements quantify over every \(\alpha>0\), every \(0\le\delta<1/2\), and every \(c\in\ell^2(\mathbb Z)\). The generator is the unit-height symmetric two-sided exponential, and the domain norm is the **coefficient** \(\ell^2\) norm, not the \(L^2(\mathbb R)\) norm of the synthesized function. Boundedness follows from exponentially decaying matrix rows and columns. The sampling grid contains exactly two sites per two unit cells; at \(\delta=1/2\), those sites coincide and stable recovery of coefficient sequences fails. The Fourier representation below uses the cell frequency \(\theta\in[-\pi,\pi]\).

## Proof
**Hyperbolic interpolation.** Every absolutely convergent combination \(f(t)=\sum_{n\in\mathbb Z}c_n g_\alpha(t-n)\) obeys \(f''=\alpha^2f\) on each open interval \((k,k+1)\), hence for \(0\le s\le1\)
\[
f(k+s)=\frac{\sinh(\alpha(1-s))}{\sinh\alpha}f(k)+\frac{\sinh(\alpha s)}{\sinh\alpha}f(k+1).
\]
By density, the identity applies to all coefficient sequences in \(\ell^2\). Define
\[
a=\frac{\sinh(\alpha(1-\delta))}{\sinh\alpha},\qquad
b=\frac{\sinh(\alpha\delta)}{\sinh\alpha}.
\]
Collecting adjacent lattice samples gives the factorization \(T_{\alpha,\delta}=M_\delta T_{\alpha,0}\), where \(M_\delta\) is the direct sum on consecutive sample pairs of the symmetric block \(M=\left(\begin{smallmatrix}a&b\\ b&a\end{smallmatrix}\right)\). Its positive eigenvalues are \(a-b=m\) and \(a+b=p\); the hyperbolic addition formulas yield the announced expressions for \(m,p\). In particular, \(0<m\le p\) for \(0\le\delta<1/2\), with strict inequality if \(\delta>0\).

**Global sharp extrema.** The integer-sample convolution \(T_{\alpha,0}\) has scalar Fourier symbol
\[
h_\alpha(\omega)=\sum_{n\in\mathbb Z}e^{-\alpha|n|}e^{in\omega}
=\frac{1-e^{-2\alpha}}{1-2e^{-\alpha}\cos\omega+e^{-2\alpha}}.
\]
Its minimum and maximum are \(\tanh(\alpha/2)\) and \(\coth(\alpha/2)\). Since the extremal singular values of \(M\) are \(m,p\), the operator norms provide \(\|Tc\|_2\ge m\tanh(\alpha/2)\|c\|_2\) and \(\|Tc\|_2\le p\coth(\alpha/2)\|c\|_2\). The corresponding even/odd Bloch modes at zero cell frequency simultaneously extremize the convolution and \(M\), so these bounds are exact. Their squares simplify to the stated \(A,B\). Spectral continuity or Bloch packets shows both endpoint values are in the operator spectrum.

**Two-band decomposition.** Set \(r=e^{-\alpha}\), \(u=1+r^2\), \(X=\cos^2(\theta/2)\), and \(D=u^2-4r^2X\). The pair-cell Fourier multiplier for integer sampling is the Hermitian matrix
\[
C(\theta)=\frac{1-r^2}{D}
\begin{pmatrix}
 u&r(1+e^{-i\theta})\\
 r(1+e^{i\theta})&u
\end{pmatrix}.
\]
Thus the squared singular values at each frequency are the two eigenvalues \(\lambda_-(\theta)\le\lambda_+(\theta)\) of the Hermitian positive matrix \(S(\theta)=M C(\theta)^2M\). Direct multiplication gives
\[
\operatorname{tr}S=\frac{(1-r^2)^2}{D^2}
\big[(p^2+m^2)(u^2+4r^2X)+4(p^2-m^2)urX\big],
\qquad \det S=\frac{m^2p^2(1-r^2)^4}{D^2}.
\]
Put \(k=\tanh\alpha=(1-r^2)/u\) and \(q=p^2-m^2\ge0\). For \(\chi_\theta(z)=z^2-(\operatorname{tr}S)z+\det S\), exact polynomial expansion yields
\[
\begin{aligned}
\frac{D^2u^4}{(1-r^2)^4}\chi_\theta(m^2k^2)
&=-4m^2rX\big[q u^2(1+r+r^2)+4m^2r(u^2-r^2X)\big],\\
\frac{D^2u^4}{(1-r^2)^4}\chi_\theta(p^2k^2)
&=-4p^2rX\big[q H(r,X)+4m^2r(u^2-r^2X)\big],
\end{aligned}
\]
where
\[
H(r,X)=1+3r+3r^2+(6-4X)r^3+3r^4+3r^5+r^6>0.
\]
Here \(0<r<1\), \(0\le X\le1\), and \(u^2-r^2X>0\). For \(X>0\) each characteristic polynomial is negative at its displayed argument. Thus
\[
\lambda_-(\theta)<m^2\tanh^2\alpha,
\quad \lambda_+(\theta)>p^2\tanh^2\alpha\qquad(X>0).
\]
At \(X=0\), equivalently \(\theta=\pi\), \(C(\pi)=\tanh\alpha I\) and both inequalities become equalities. At \(X=1\), equivalently \(\theta=0\), the matrices \(M\) and \(C(0)\) have common symmetric/antisymmetric eigenvectors and yield the global minimum \(m^2\tanh^2\eta\) and maximum \(p^2\coth^2\eta\). The two continuous eigenvalue functions take all intervening values, but the characteristic-polynomial inequalities exclude all values in the indicated gap. Bloch diagonalization therefore gives exactly the two claimed intervals. If \(\delta=0\), their common endpoint is \(\tanh^2\alpha\); otherwise \(p>m\) and the gap is open.

**Collision limit.** The identity \(m=\sinh[\alpha(1/2-\delta)]/\sinh(\alpha/2)\), inserted into the sharp lower bound, and the Taylor series of \(\sinh\) give the stated positive quadratic coefficient and remainder. At \(\delta=1/2\) the paired sampling rows coincide, so the lower bound is zero.

## Verification
The accompanying standalone `verify_spectrum.py` performs exact symbolic checks of the two characteristic-polynomial factorizations, followed by independent numerical Bloch-matrix scans for 20 parameter pairs across a range of decays and offsets. It checks all four band endpoints. The checker is a reproducible consistency test; the proof of the infinite and continuous-frequency assertions is the algebra and spectral argument above.

## Relationship to prior work
De Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor (2026, Section 5) prove broad qualitative stability for sufficiently small perturbations of sampling lattices in totally positive shift-invariant spaces. That result covers invertibility for suitable perturbations but does not provide the exact period-two singular spectrum, gap, or sharp conditioning law. A previous exact study of **constant translated** sampling lattices for asymmetric two-sided exponentials determines bounds in the synthesized-function \(L^2\) norm; a 2-periodic alternation with coefficient-norm spectral bands is not a corollary of it. Kloos and Stöckler study Zak-transform zeros and Gabor frames, which use a different measurement operator. Antezana, Carbajal, and Romero study random periodic sampling patterns, rather than this deterministic critically dense two-site family. Elementary Fourier diagonalization, Floquet block reduction, and hyperbolic interpolation are methods used, not asserted as new results.

## Limitations
The result is restricted to the symmetric two-sided exponential generator and the paired alternating grid at one sample per unit interval. It does not yield best \(L^2(\mathbb R)\)-normalized sampling constants, nor extend without modification to arbitrary totally positive generators or irregular jitter. The analytic proof establishes the full infinite-volume spectrum; the finite numerical scan is not offered as infinite proof. Equivalent older spectral formulas in periodic exponential-spline literature may exist and require further bibliographic review. Independent external mathematical validation has not been carried out.

## References
1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, and M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1 (first submitted 2026-08-05), https://arxiv.org/html/2608.04992v1.
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/html/1311.7359v1.
3. K. Gröchenig and I. Shafkulovska, *Sampling theorems with derivatives in shift-invariant spaces generated by periodic exponential B-splines*, arXiv:2311.08352 (2023), https://arxiv.org/html/2311.08352v1.
4. J. Antezana, J. Carbajal, and J. L. Romero, *Random periodic sampling patterns for shift-invariant spaces*, arXiv:2305.15261 (2023), https://arxiv.org/abs/2305.15261.
5. *Sharp shifted sampling bounds and two tight phases for asymmetric two-sided exponentials* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-shifted-sampling-bounds-and-two-tight-phases-for-asymmetri--acaeec402fe4.
