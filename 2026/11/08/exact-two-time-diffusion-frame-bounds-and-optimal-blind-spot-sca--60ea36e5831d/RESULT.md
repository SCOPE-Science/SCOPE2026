# Exact two-time diffusion frame bounds and optimal blind-spot scaling on the integer line

## Finding
Let \(L\) be the normalized graph Laplacian on \(\ell^2(\mathbb Z)\),
\[
(Lf)(n)=f(n)-\frac{f(n-1)+f(n+1)}2.
\]
For \(0<c<1\), let \(H_c\) consist of the sequences whose Fourier transform vanishes outside
\[
E_c=\{\theta\in[-\pi,\pi):|\cos\theta|\ge c\}.
\]
For \(t>0\), measure the initial state and its heat evolution only at even vertices:
\[
\mathcal S_t f=\bigl((f(2k))_{k\in\mathbb Z},((e^{-tL}f)(2k))_{k\in\mathbb Z}\bigr).
\]
Define, for \(0\le u\le1\),
\[
d_t(u)=e^{-2t}\sinh^2(tu),\quad T_t(u)=1+e^{-2t}+2d_t(u),\quad
\Lambda_\pm(u,t)=\frac{T_t(u)\pm\sqrt{T_t(u)^2-4d_t(u)}}2.
\]
Then, for every \(0<c<1\) and \(t>0\), the **optimal** squared sampling-frame bounds are
\[
\boxed{A_c(t)=\Lambda_-(c,t),\qquad B_c(t)=\Lambda_+(1,t)}.
\]
That is, \(A_c(t)\|f\|_2^2\le\|\mathcal S_t f\|_2^2\le B_c(t)\|f\|_2^2\) for all \(f\in H_c\), and neither constant can be improved. No single time snapshot at even vertices has a positive lower bound on \(H_c\). When \(c=0\), no **finite** collection of heat observation times at even vertices has a positive lower frame bound on \(\ell^2(\mathbb Z)\), despite almost-everywhere injectivity for two distinct times.

The best choice of heat observation time for small spectral gaps has a universal limit. Let \(t_0\) be the unique positive solution
\[
t_0=1+e^{-2t_0},\quad\text{equivalently }t_0=1+\tfrac12W(2e^{-2})\approx1.1088575528785494.
\]
Then
\[
\boxed{\lim_{c\downarrow0}c^{-2}\max_{t>0}A_c(t)
=\frac{t_0^2}{1+e^{2t_0}}\approx0.12070751969725028.}
\]
For every choice of maximizer \(t_c\in\operatorname{argmax}_{t>0}A_c(t)\), one has \(t_c\to t_0\) as \(c\downarrow0\). Thus the optimal lower frame bound decays *quadratically* in the spectral distance from the unavoidable heat-flow alias collision.

## Assumptions and scope
The Fourier convention is \(\widehat f(\theta)=\sum_{n\in\mathbb Z}f(n)e^{-in\theta}\), with Plancherel measure \(d\theta/(2\pi)\). The space \(H_c\) is an infinite-dimensional closed spectral subspace; for \(c=0\), it is all of \(\ell^2(\mathbb Z)\). The bounds concern unweighted, noise-free observations at times zero and \(t\), with \(\ell^2\)-norms over both even-vertex observation sequences. The restriction \(c<1\) ensures \(E_c\) has positive measure. Distinct times are essential for two snapshots. The only time-optimization objective is the lower frame bound \(A_c(t)\), not its ratio to the upper bound.

## Proof
**Fourier fibers and exact normalization.** The multiplier of \(L\) is \(1-\cos\theta\). Write the torus as two aliases \(\theta\) and \(\theta+\pi\), with representative \(\theta\in[-\pi/2,\pi/2)\). The Fourier transform of downsampling by two is the average of the two aliased transforms. Plancherel therefore identifies the total observation norm with the direct integral of the squared norm of
\[
M_t(u)=\frac1{\sqrt2}\begin{pmatrix}
1&1\\ e^{-t(1-u)}&e^{-t(1+u)}
\end{pmatrix},\qquad u=\cos\theta.
\]
The input norm is the corresponding direct integral of the Euclidean norm of the two Fourier coefficients. On \(H_c\), precisely the fibers \(u\in[c,1]\) are present; each contains both alias components. Note that the \(1/\sqrt2\) is forced by the even-site downsampling normalization.

**Exact eigenvalues and sharp extrema.** Direct multiplication gives
\[
\operatorname{tr}(M_t(u)^*M_t(u))=1+e^{-2t}\cosh(2tu)=T_t(u),\quad
\det(M_t(u)^*M_t(u))=e^{-2t}\sinh^2(tu)=d_t(u).
\]
Consequently the two eigenvalues of this positive matrix are exactly \(\Lambda_\pm(u,t)\). Put \(q=e^{-2t}\) and \(d=d_t(u)\). Both eigenvalues solve
\[
\lambda^2-(1+q+2d)\lambda+d=0.
\]
At \(\lambda=0\) the polynomial is \(d>0\), whereas at \(\lambda=1/2\) it equals \(-1/4-q/2<0\). Hence \(0<\Lambda_-<1/2<\Lambda_+\). Implicit differentiation with respect to \(d\) yields
\[
\frac{d\Lambda_-}{dd}=\frac{1-2\Lambda_-}{\Lambda_+-\Lambda_-}>0,\qquad
\frac{d\Lambda_+}{dd}=\frac{2\Lambda_+-1}{\Lambda_+-\Lambda_-}>0.
\]
Since \(u\mapsto d_t(u)\) increases strictly for \(u>0\), the smallest and largest fiber eigenvalues increase with \(u\). Their essential extrema over \([c,1]\) are therefore \(\Lambda_-(c,t)\) and \(\Lambda_+(1,t)\). Continuity and positive-measure neighborhoods of either endpoint show the constants are optimal, not merely bounds.

**Minimality and the collision.** A single observation time gives one scalar for each two-component alias fiber, hence an infinite-dimensional kernel on \(H_c\). For \(c=0\), every finite selection of times \(0\le t_1,\ldots,t_m<\infty\) produces an \(m\times2\) fiber matrix whose columns coincide at \(\theta=\pi/2\), because the two aliased Laplacian eigenvalues both equal one. Its smallest singular value tends to zero as \(\theta\) approaches this point from either side. Therefore there is no positive essential lower bound. This assertion does not claim a nonzero \(\ell^2\) null vector: the collision is a measure-zero event and only blocks stable inversion.

**Sharp optimal-gap asymptotics.** For any fixed \(t>0\), as \(c\downarrow0\),
\[
d_t(c)=e^{-2t}t^2c^2+O_t(c^4),\quad
\Lambda_-(c,t)=\frac{t^2}{1+e^{2t}}c^2+O_t(c^4).
\]
The convergence of \(c^{-2}A_c(t)\) to \(F(t)=t^2/(1+e^{2t})\) is uniform on compact time intervals. It is also tight at zero and infinity, uniformly in \(0<c\le1/2\): from \(\Lambda_+\ge1+e^{-2t}\) and \(\sinh(tc)\le tc e^{tc}\),
\[
0\le c^{-2}A_c(t)=\frac{d_t(c)}{c^2\Lambda_+(c,t)}\le t^2e^{-2(1-c)t}\le t^2e^{-t}.
\]
Since this bound vanishes at both time endpoints, convergence is uniform over \(t>0\). Moreover \(A_c(t)\to0\) as \(t\downarrow0\) and \(t\to\infty\) for fixed \(c<1\), so a maximizer exists. Differentiation shows that the only positive stationary point of \(F\) satisfies \(t=1+e^{-2t}\). The left side is strictly increasing and the right side strictly decreasing, so it is the unique maximizer \(t_0\). Uniform convergence plus uniqueness yields the limit of the maxima and convergence of all maximizing times.

## Verification
Run `python CHECK.py` with Python 3, NumPy and SciPy. The program independently constructs the two-time alias matrices and their singular-value spectra on 49 gap/time combinations; checks the location of both spectral extrema; verifies the continuum formulas against direct Fourier observations on periodic cycles of lengths 128 and 256; and numerically checks the predicted optimal-time limit. The checker supplies finite corroboration only. The exact infinite-dimensional claims and the optimization limit follow from the analytic proof above.

## Relationship to prior work
Aldroubi, Davis and Krishtal (2013/2015) established general polyphase-matrix criteria for dynamical sampling in \(\ell^2(\mathbb Z)\) and the failure of uniform full-space diffusion sampling at alias collisions. Those qualitative implications are **not new** here. Aldroubi and collaborators (2021) studied continuous heat-flow sampling away from spectral blind spots and obtained general quantitative estimates. Cabrelli, Cordero, Bulai, Saliani and Molter (2026) studied the graph normalized Laplacian, including lattice graph Paley–Wiener spaces. The contribution at issue is the explicit **sharp** two-snapshot spectral-gap frame bounds for the normalized discrete heat flow on \(\mathbb Z\), together with the globally best small-gap constant and convergence of optimal observation times. The recent graph paper's accessible abstract did not disclose these formulas, but its full text was unavailable; it remains a publication-priority risk. The 2013 general polyphase theorem provides the conceptual reduction rather than the explicit time-optimized constants.

## Limitations
No result is claimed for nonuniform spatial grids, noisy or approximate evolution models, arbitrarily weighted observation channels, continuous-time integrated measurements, general graphs, or more than two times for \(c>0\). The existence of an optimizer is proved but uniqueness at each fixed positive gap is not claimed. The work does not claim novelty of the standard polyphase representation, the basic alias-collision obstruction, or spectral-gap restriction itself. Exact prior-art coverage cannot be certified solely by literature searches; notably a plausible 2026 paper was not available in full text. The finite numerical checker does not certify the continuum proof or publication priority independently.

## References
- I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, first posted 2026-09-21, https://arxiv.org/abs/2609.25472.
- A. Aldroubi, J. Davis and I. Krishtal, *Exact Reconstruction of Spatially Undersampled Signals in Evolutionary Systems*, arXiv:1312.3203, https://arxiv.org/abs/1312.3203; DOI:10.1007/s00041-014-9359-9.
- A. Aldroubi, K. Gröchenig, L. Huang, P. Jaming, I. Krishtal and J. L. Romero, *Sampling the Flow of a Bandlimited Function*, Journal of Geometric Analysis 31 (2021), 9241–9275, DOI:10.1007/s12220-021-00617-0, https://link.springer.com/article/10.1007/s12220-021-00617-0.
- A. Aldroubi, C. Cabrelli, I. Krishtal and U. Molter, *Dynamical Sampling: A Survey*, La Matematica (2026), DOI:10.1007/s44007-026-00215-y, https://link.springer.com/article/10.1007/s44007-026-00215-y.
