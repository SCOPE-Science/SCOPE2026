# Sharp two-time heat-sampling bounds and a unique optimal delay on the infinite ladder

## Finding
Let \(G=\mathbb Z\square K_2\) be the unweighted infinite ladder. Every vertex has degree three. Let \(L=I-A_G/3\) be its normalized graph Laplacian and \(E_t=e^{-tL}\). For every \(t>0\), the two snapshots of an arbitrary \(f=(f_0,f_1)\in\ell^2(\mathbb Z)^2\), both observed **only on rail zero**, are
\[
\mathcal S_t f=\bigl((f_0(n))_{n\in\mathbb Z},\ ((E_t f)_0(n))_{n\in\mathbb Z}\bigr).
\]
This is a bounded isomorphism \(\ell^2(\mathbb Z)^2\to\ell^2(\mathbb Z)^2\) for every \(t>0\). Set \(r=e^{-2t/3}\) and
\[
T_-(r)=1+\frac{r^4(1+r^2)}2,\quad T_+(r)=\frac{3+r^2}2.
\]
The **optimal squared sampling bounds** are
\[
\boxed{A(t)=\frac{T_-(r)-\sqrt{T_-(r)^2-r^4(1-r)^2}}2},
\]
\[
\boxed{B(t)=\frac{T_+(r)+\sqrt{T_+(r)^2-(1-r)^2}}2}.
\]
That is, for every \(f\in\ell^2(\mathbb Z)^2\),
\[
A(t)\|f\|_2^2\le\|\mathcal S_t f\|_2^2\le B(t)\|f\|_2^2,
\]
and neither bound can be improved. The lower bound is controlled by longitudinal frequency \(\theta=\pi\); the upper bound is controlled by \(\theta=0\).

The lower bound \(A(t)\) has exactly one maximizer on \((0,\infty)\). Let \(r_*\in(0,1)\) be the unique root of
\[
\boxed{P(r)=3r^6-3r^5+5r^4-5r^3+5r^2+4r-4=0}.
\]
Then
\[
\boxed{t_*=-\tfrac32\log r_*\ =0.674754444831455\ldots},
\qquad A(t_*)=0.004882704478092798\ldots.
\]
In particular the best observation delay is an intrinsic explicitly characterized constant of the unweighted normalized ladder. At the time endpoints,
\[
A(t)\sim t^2/18\quad(t\downarrow0),\qquad
A(t)\sim \tfrac14 e^{-8t/3}\quad(t\to\infty).
\]

An explicit stable reconstruction is available: with \(y_0=f_0\) and \(y_1=(E_t f)_0\), define the bounded convolution operator \(D=I-(S+S^{-1})/3\) on \(\ell^2(\mathbb Z)\), where \(S\) is the bilateral shift. Then
\[
\boxed{f_1=\frac{e^{tD}}{\sinh(t/3)}y_1-\coth(t/3)y_0.}
\]

## Assumptions and scope
The graph has vertices \((n,j)\), \(n\in\mathbb Z\), \(j\in\{0,1\}\), edges \((n,j)\sim(n\pm1,j)\) and \((n,0)\sim(n,1)\). The norm on each rail is the ordinary counting-measure \(\ell^2\)-norm, with the two observed snapshot norms summed without reweighting. Time zero is included. All statements apply to arbitrary complex square-summable data, without a bandwidth or spectral-notch assumption. The optimization concerns \(A(t)\), **not** the ratio \(B(t)/A(t)\), a determinant, or a finite-cycle discretization. Sharp extrema are spectral essential extrema: the endpoint plane waves themselves are not nonzero \(\ell^2\) signals.

## Proof
**1. Exact Fourier fibers.** Use the unitary discrete Fourier transform on each rail with \(\widehat f(\theta)=\sum_{n\in\mathbb Z}f(n)e^{-in\theta}\) and measure \(d\theta/(2\pi)\). The graph Laplacian becomes
\[
\widehat L(\theta)=\left(1-\frac{2\cos\theta}{3}\right)I-\frac13\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The two observed rows therefore form the fiber matrix
\[
M_t(\theta)=\begin{pmatrix}
1&0\\q_t(\theta)\cosh(t/3)&q_t(\theta)\sinh(t/3)
\end{pmatrix},\quad
q_t(\theta)=e^{-t(1-2\cos\theta/3)}.
\]
Its determinant \(q_t(\theta)\sinh(t/3)\) is nonzero for every \(t>0\). Because \(q_t\) has a positive minimum on the compact frequency circle, and its entries are uniformly bounded, the fiber matrices and their inverses are uniformly bounded. Fourier Plancherel gives the stated isomorphism and stable inverse formula.

**2. Sharp global spectrum.** For fixed \(t>0\), write \(C=\cosh(t/3)\), \(H=\sinh(t/3)\) and \(q=q_t(\theta)\). The Gram matrix is
\[
M_t(\theta)^*M_t(\theta)
=\operatorname{diag}(1,0)+q^2(C,H)^{\mathsf T}(C,H).
\]
It is nondecreasing in \(q^2\) in the Loewner order. The two extreme eigenvalues are therefore minimized or maximized at the extrema of \(q\): \(q_{\min}=e^{-5t/3}\) at \(\theta=\pi\), and \(q_{\max}=e^{-t/3}\) at \(\theta=0\). When \(r=e^{-2t/3}\), the corresponding matrices become
\[
M_-(r)=\begin{pmatrix}1&0\\r^2(1+r)/2&r^2(1-r)/2\end{pmatrix},\qquad
M_+(r)=\begin{pmatrix}1&0\\(1+r)/2&(1-r)/2\end{pmatrix}.
\]
Their Gram traces are \(T_-(r)\), \(T_+(r)\), and their Gram determinants are \(r^4(1-r)^2/4\), \((1-r)^2/4\). The quadratic eigenvalue formula gives precisely \(A(t)\) and \(B(t)\). Continuity in \(\theta\) and positive-measure neighborhoods of the extreme frequencies make these bounds sharp in the infinite-dimensional \(\ell^2\) inequality, even though nonzero \(\ell^2\) plane waves do not attain them.

**3. Unique optimal time.** Let \(\lambda(r)\) denote the lower eigenvalue of \(M_-(r)^*M_-(r)\). Its characteristic equation is
\[
F(\lambda,r)=\lambda^2-\left(1+\frac{r^4(1+r^2)}2\right)\lambda+\frac{r^4(1-r)^2}4=0.
\]
The two roots are distinct because the matrix has nonzero off-diagonal entry for \(0<r<1\). Implicit differentiation gives \(\lambda'(r)=0\) only if
\[
\lambda=\lambda_c(r)=\frac{(1-r)(2-3r)}{4+6r^2}.
\]
A direct polynomial identity (which can also be checked by exact symbolic algebra) is
\[
F(\lambda_c(r),r)=\frac{(1-r)(1+r)^2 P(r)}{4(3r^2+2)^2}.
\]
The derivative of \(P\) admits the decomposition
\[
P'(r)=4+5r(4r^2-3r+2)+3r^4(6r-5).
\]
The middle term is nonnegative for \(r\ge0\), since the quadratic has negative discriminant. On \(0\le r\le5/6\), the last term is at least \(-16/27\) (its negative part is maximized at \(r=2/3\)); for \(r\ge5/6\) it is nonnegative. Hence \(P'(r)>0\) on \([0,1]\). Since \(P(0)=-4\) and \(P(2/3)=64/243>0\), it has exactly one root \(r_*\in(0,2/3)\). There \(0<\lambda_c(r_*)<1/2\), whereas the upper Gram eigenvalue is at least one; thus the critical point belongs to the *lower* eigenvalue. Finally, \(\lambda(r)\to0\) as \(r\downarrow0\) or \(r\uparrow1\). The unique interior stationary point is therefore the unique global maximizer. The change of variables \(r=e^{-2t/3}\) is a bijection from positive times onto \((0,1)\), giving the stated unique \(t_*\).

**4. Endpoint asymptotics and inversion.** At short times the minimum-frequency matrix has first row \((1,0)\) and second row \((1+O(t),\ t/3+O(t^2))\), so its smaller Gram eigenvalue is \(t^2/18+O(t^3)\). At long times it has second row \((r^2/2+O(r^3),\ r^2/2+O(r^3))\), giving \(\lambda=r^4/4+O(r^5)\). Solving the second row of the Fourier measurement equation for \(\widehat f_1\), then applying Fourier inversion, yields the stable reconstruction formula.

## Verification
The standalone `verify.py` uses Python 3, SymPy, and NumPy to recompute the two Gram traces and determinants exactly; verify the derivative identity, sextic resultant factorization, root bracketing and numerical lower-bound constant; and compare the proposed continuum spectral endpoints with exact Fourier-block eigenvalues on cycles of four lengths and three positive observation delays. Its success line is `CHECK_OK exact_gram=4 sextic_resultant=1 rational_brackets=2 finite_cycle_fibers=12`. The finite checks corroborate but do not prove the infinite-dimensional assertion; the preceding Fourier proof and monotonicity argument do.

## Relationship to prior work
Aldroubi, Davis and Krishtal developed general dynamical sampling and polyphase reconstruction on the integer lattice (2013/2015). Bulai, Cabrelli, Cordero, Molter and Saliani (2026) study graph Paley–Wiener dynamical frames, with explicit lattice Fourier theory and finite-path analyses. Both supply conceptual context; their accessible inspected material does not determine the sharp two-rail infinite-ladder sampling constants or the degree-six optimizing equation. Published work on two-time diffusion sampling from even vertices of the single integer lattice instead encounters an alias collision and requires a spectral notch for uniform frame bounds, while published critical-density integer-line sampling uses spatially adjacent sensors and a different evolution geometry. Neither statement implies a uniformly stable one-rail ladder observation or its unique optimal delay. General dynamical sampling criteria are not claimed as new.

## Limitations
This result concerns exactly the unweighted normalized two-rail ladder, time-zero and one later heat snapshot, one fully observed rail, and unweighted observation norms. It does not establish optimal sensor placement among other geometries, an optimal condition number, or stability under missing spatial sites. The proof is analytic, not an extrapolation from finite cycles. Relevant primary-paper full-text retrieval was incomplete despite open-source attempts; an older equivalent specialized observability calculation remains a publication-priority risk. Independent validation has not been performed.

## References
- I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, first posted 2026-09-21, arXiv:2609.25472, https://arxiv.org/abs/2609.25472.
- A. Aldroubi, J. Davis and I. Krishtal, *Exact Reconstruction of Spatially Undersampled Signals in Evolutionary Systems*, first posted 2013-12-04, arXiv:1312.3203, https://arxiv.org/abs/1312.3203.
- A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, first posted 2025-11-13, arXiv:2511.10769, https://arxiv.org/abs/2511.10769.
- *Exact two-time diffusion frame bounds and optimal blind-spot scaling on the integer line*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-time-diffusion-frame-bounds-and-optimal-blind-spot-sca--60ea36e5831d.
- *Critical-density lattice dynamical sampling and the silver-ratio instability*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-critical-density-lattice-dynamical-sampling-and-the-silver-ratio--06e6e4ce4ac1.
