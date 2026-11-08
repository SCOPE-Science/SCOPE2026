# A sharp \(N^{-1}\) positivity-recovery horizon for Fourier-collocation heat flow

## Finding

Let \(N\ge4\) be even. On the equispaced grid of the \(2\pi\)-periodic circle, consider the continuous-in-time Fourier-pseudospectral heat semigroup \(P_N(t)=\exp(tD_N)\), with the discrete Laplacian symbol \(-k^2\), including the single real Nyquist mode \(k=N/2\). Let
\[
T_N=\inf\left\{s\ge0:\ P_N(t)\text{ is entrywise nonnegative for every }t\ge s\right\}.
\]
Then \(T_N\) is finite for every \(N\), and
\[
\boxed{\lim_{\substack{N\to\infty\\N\ \mathrm{even}}}N T_N=\pi.}
\]
More precisely, for each fixed \(c>\pi\), there exists \(N_c\) such that for all even \(N\ge N_c\), every matrix entry of \(P_N(t)\) is **strictly positive** for every real \(t\ge c/N\). Conversely, for each \(0<c<\pi\), all sufficiently large even \(N\) have a **negative** entry of \(P_N(c/N)\). Thus the sharp asymptotic recovery time is proportional to \(N^{-1}\), not the usual \(N^{-2}\) diffusion time across a grid cell.

## Assumptions and scope

All comparisons concern exact, real-arithmetic semidiscretization of the **one-dimensional periodic heat equation** \(u_t=u_{xx}\) with diffusivity one and period \(2\pi\). Index the \(N\) grid nodes by \(j\in\{0,\ldots,N-1\}\), \(x_j=2\pi j/N\). Write \(K=N/2\). The real circulant transition matrix \(P_N(t)\) is the unique matrix whose Fourier eigenvalues are \(\exp(-k^2t)\) for \(-K<k<K\), together with one Nyquist eigenvalue \(\exp(-K^2t)\); it preserves constants and the grid sum. Its entry at a cyclic separation \(j\) is
\[
p_{N,j}(t)=\frac1N\left(1+2\sum_{k=1}^{K-1}e^{-k^2t}\cos\frac{2\pi kj}{N}+e^{-K^2t}(-1)^j\right).
\]
The claim concerns nonnegativity for **every nonnegative initial grid vector**, equivalent to entrywise nonnegativity of \(P_N(t)\). It is not a claim of positivity between grid nodes, nor about a discrete time-stepping map, finite precision, nonlinear equations, or odd grids.

## Proof

**1. Positive full heat kernel and a uniform cutoff bound.** For \(t>0\), set
\[
\Theta(t,x)=\sum_{k\in\mathbb Z}e^{-k^2t}e^{ikx}
=\sqrt{\frac\pi t}\sum_{m\in\mathbb Z}
\exp\!\left(-\frac{(x-2\pi m)^2}{4t}\right)>0,
\]
by Poisson summation. Write \(S_N(t,x_j)=Np_{N,j}(t)\). At the grid, the Nyquist contribution in \(S_N\) is only one copy of its Fourier coefficient, whereas \(\Theta\) includes both signs. Hence exactly
\[
\Theta(t,x_j)-S_N(t,x_j)
=e^{-K^2t}(-1)^j+2\sum_{k=K+1}^\infty e^{-k^2t}\cos(kx_j).
\]
For any grid point, using \((K+\ell)^2-K^2=N\ell+\ell^2\),
\[
\left|\Theta(t,x_j)-S_N(t,x_j)\right|
\le e^{-N^2t/4}\left(1+2\sum_{\ell\ge1}e^{-N\ell t}\right)
=e^{-N^2t/4}\coth(Nt/2). \tag{1}
\]
Choose the representative \(x_j\in[-\pi,\pi]\). The nearest Gaussian image gives
\[
\Theta(t,x_j)\ge\sqrt{\frac\pi t}\exp\left(-\frac{\pi^2}{4t}\right). \tag{2}
\]
For \(t\ge c/N\), the ratio between (1) and (2) obeys
\[
\frac{|\Theta-S_N|}{\Theta}
\le\coth(c/2)\sqrt{\frac{t}{\pi}}
\exp\left(-\frac{N^2t}{4}+\frac{\pi^2}{4t}\right).
\]
The function on the right after the factor \(\coth(c/2)\) decreases strictly with \(t>0\): its logarithmic derivative is
\[
\frac{2t-N^2t^2-\pi^2}{4t^2}<0
\]
for all \(N\ge2\). Therefore the ratio is at most
\[
\coth(c/2)\sqrt{\frac{c}{\pi N}}
\exp\left[-\frac N4\left(c-\frac{\pi^2}{c}\right)\right]. \tag{3}
\]
If \(c>\pi\), expression (3) tends to zero. Thus for every sufficiently large even \(N\), \(S_N(t,x_j)>0\) for **all** \(j\) and all real \(t\ge c/N\). In particular \(\limsup NT_N\le\pi\). For any fixed \(N\), independent of (3), the nonconstant modes vanish as \(t\to\infty\), so \(T_N<\infty\).

**2. The parity-selected antipodal negative entry.** Fix \(0<c<\pi\), and choose the *even* grid offset \(j_N=2\lfloor N/4\rfloor\), for which \(x_N=2\pi j_N/N\in[\pi-2\pi/N,\pi]\) and \(\cos(Kx_N)=(-1)^{j_N}=1\). At \(t=c/N\), the exact tail can be factored as
\[
S_N(c/N,x_N)=\Theta(c/N,x_N)-e^{-cN/4} B_N(c),
\]
where
\[
B_N(c)=1+2\sum_{\ell\ge1}
 e^{-c\ell-c\ell^2/N}\cos(\ell x_N).
\]
The series is dominated by a geometric series for fixed \(c>0\). Since \(x_N\to\pi\), dominated convergence yields
\[
B_N(c)\longrightarrow1+2\sum_{\ell\ge1}(-e^{-c})^\ell
=\frac{1-e^{-c}}{1+e^{-c}}=\tanh(c/2)>0. \tag{4}
\]
The periodized-Gaussian expression and \(\pi-2\pi/N\le x_N\le\pi\) give a constant \(C_c\) such that
\[
0<\Theta(c/N,x_N)\le C_c\sqrt N
\exp\left(-\frac{\pi^2N}{4c}\right). \tag{5}
\]
In (5), \(C_c\) absorbs the bounded factor caused by \(x_N=\pi+O(N^{-1})\) and the exponentially small remote images. Because \(c<\pi\), division of (5) by \(e^{-cN/4}\) tends to zero. Combined with (4), this gives \(S_N(c/N,x_N)<0\) for every sufficiently large even \(N\). Therefore \(T_N\ge c/N\) for all such \(N\), and \(\liminf NT_N\ge\pi\). The two bounds establish the theorem. \(\square\)

## Verification

The accompanying standalone program `verify.py` requires Python 3 and `mpmath`. It compares the Fourier and periodized-Gaussian expressions to high precision, checks the explicit omitted-frequency bound, checks conservation of total grid mass, and tests signed matrix entries at representative times below and above the limiting threshold. The local run passed **419** high-precision assertions. For example, at separation \(j=N/2\) on grids with \(N\) divisible by four, \(p_{64,32}(2.8/64)\approx-4.858466106\cdot10^{-22}\), whereas \(p_{64,32}(3.5/64)\approx6.024191814\cdot10^{-21}\). These tests corroborate, but do not prove, the uniform-in-time or infinite-grid assertions; those rest on the displayed inequalities and dominated convergence.

## Relationship to prior work

Dong Li, *Effective maximum principles for spectral methods* (2021), investigates Fourier collocation and almost-sharp \(L^\infty\) estimates. In particular, Appendix B treats Fourier heat evolution with frequency truncation, derives upper bounds on induced norms, and constructs small-time maximum-principle counterexamples. Those estimates do **not** state the strict entrywise-positive recovery threshold or the sharp coefficient \(\pi\) for the even-grid, periodic pseudospectral heat semigroup. Kim et al. (2023), *A maximum principle of the Fourier spectral method for diffusion equations*, investigate discrete maximum-principle violations in a Neumann diffusion setting via numerical experiments, but do not establish this all-time, asymptotically sharp periodic result. Cai, Lin and Lin (2023) obtain positivity by constrained Fourier projection in kinetic applications, not by waiting for the unmodified periodic heat semigroup to become entrywise positive. The comparison is to the *statements and implications* of these sources, not merely to their titles. The full publicly accessible texts of the three works were inspected in their relevant result sections.

## Limitations

This is an asymptotic theorem for even grids with one specific Nyquist convention. It neither determines an exact \(T_N\) at each finite \(N\) nor proves the analogous asymptotic for odd grids, other Fourier symbols, arbitrary physical domain length or multiple dimensions. Since heat diffusivity is fixed to one and the period to \(2\pi\), \(\pi\) is not claimed as a dimensionless constant for every normalization. The proof assumes exact arithmetic. Specialist publication precedence, particularly under Fourier-cutoff and theta-kernel terminology, remains a residual originality risk; a failed literature search is not itself evidence of novelty.

## References

1. Dong Li, *Effective maximum principles for spectral methods*, arXiv:2107.09438 (first public 2021-07-20), https://arxiv.org/abs/2107.09438 . Relevant: Sections 1, 5 and Appendix B.
2. Junseok Kim, Soobin Kwak, Hyun Geun Lee, Youngjin Hwang and Seokjun Ham, *A maximum principle of the Fourier spectral method for diffusion equations*, Electronic Research Archive 31 (2023), 5396–5405, published 2023-07-31, https://doi.org/10.3934/era.2023273 . Relevant: diffusion setting, discretization and examples.
3. Zhenning Cai, Bo Lin and Meixia Lin, *A positive and moment-preserving Fourier spectral method*, arXiv:2304.11847 (first public 2023-04-24), https://arxiv.org/abs/2304.11847 . Relevant: Sections 1–2, constrained positivity projection.
