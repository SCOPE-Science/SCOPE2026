# Boundary-site transition and cubic optimal-loss shift in a half-line quantum walk

## Finding
For the continuous-time half-line tight-binding walk with a Lindblad sink at site one, the eventual absorption probability from a localized initial site \(n\ge1\) decreases **strictly** with \(n\), for every positive sink-to-hopping ratio \(\eta\). Its rate-optimization problem has a boundary transition: from \(n=1\) the optimal absorption probability has supremum one as \(\eta\to\infty\); for every \(n\ge2\), an optimal finite ratio exists, and **every** such ratio is strictly greater than one. For all sufficiently large \(n\) the optimizer is unique and
\[
\eta_n^*=1+\frac{3}{4n^3}+O(n^{-4}).
\]
In particular, the bulk-matching prescription \(\eta=1\) is never exactly optimal at any finite site \(n\ge2\), though the shift is only cubic in the initial distance.

## Assumptions and scope
Fix \(\Omega>0\) and \(\kappa>0\). On \(\ell^2(\mathbb N)\), with \(\mathbb N=\{1,2,\ldots\}\), let \(H_+=\Omega I-(\Omega/2)B\), where \(B\) is nearest-neighbor adjacency with a hard wall at zero. The no-jump generator is \(A=-iH_+-\kappa|1\rangle\langle1|/2\). Initially \(\psi(0)=|n\rangle\), and \(P_n(\eta)=\kappa\int_0^\infty |\langle1|e^{At}|n\rangle|^2dt\), with \(\eta=\kappa/\Omega\). This is an eventual probability, not a finite-time hitting probability or a mean absorption time. The theorem applies to the exact infinite half-line, with no further disorder, dephasing, traps or resets.

## Proof
The exact Parseval/resolvent computation in Riberi, arXiv:2605.08056v4, Eq. (15), supplies the following **prior** identity for every \(n\ge1\):
\[
P_n(\eta)=B(\eta)+C_n(\eta),\quad
B(\eta)=\frac{2\eta}{\pi}\int_0^\pi\frac{\sin k}{1+\eta^2+2\eta\sin k}\,dk,\quad
C_n(\eta)=\frac{2\eta}{\pi}\int_0^1\frac{q^{2n-2}(1-q^2)}{1+\eta^2q^2}\,dq.
\]
No novelty is claimed for this integral representation, its weak/strong bulk duality, or the known \(O(n^{-2})\) correction. The following deductions are the finding.

**Strict distance ordering.** The integrand of \(C_n-C_{n+1}\) equals \((2\eta/\pi)q^{2n-2}(1-q^2)^2/(1+\eta^2q^2)\), strictly positive for \(0<q<1\). Thus \(P_n>P_{n+1}>B\) for all \(n\ge1\) and \(\eta>0\).

**Optimization transition.** Writing \(t=\log\eta\), the bulk term is
\[
B(e^t)=\frac1\pi\int_0^\pi\frac{\sin k}{\cosh t+\sin k}\,dk.
\]
It is even in \(t\), strictly decreasing for \(t>0\), and uniquely maximized at \(t=0\). Direct differentiation under the integral sign yields
\[
\frac{dC_n}{d\eta}(\eta)=\frac2\pi\int_0^1q^{2n-2}(1-q^2)\frac{1-\eta^2q^2}{(1+\eta^2q^2)^2}\,dq>0\quad(0<\eta\le1).
\]
The same range has \(B'(\eta)\ge0\). Hence \(P_n'(\eta)>0\) throughout \(0<\eta\le1\), so every finite maximizer has \(\eta>1\). For \(n\ge2\), the bound \(C_n(\eta)\le(2/(\pi\eta))\int_0^1q^{2n-4}(1-q^2)dq\) implies \(C_n\to0\) as \(\eta\to\infty\); also \(B\to0\), and both terms tend to zero as \(\eta\downarrow0\). By continuity and strict positivity, each \(n\ge2\) has a finite global maximizer, necessarily greater than one. For \(n=1\), the substitution \(u=\eta q\) gives
\[
C_1(\eta)=\frac2\pi\int_0^\eta\frac{1-u^2/\eta^2}{1+u^2}\,du\longrightarrow1
\]
as \(\eta\to\infty\), while \(B\to0\); since \(P_1\le1\) as an absorption probability, its supremum equals one. This does not assert finite-\(\eta\) monotonicity of \(P_1\).

**Unique distant-site optimizer.** Again put \(t=\log\eta\), and rewrite
\[
C_n(e^t)=\frac1\pi\int_0^1q^{2n-3}(1-q^2)\operatorname{sech}(t+\log q)\,dq \qquad(n\ge2).
\]
Since \(\operatorname{sech}\) and its first two derivatives are uniformly bounded, \(\sup_{t\in\mathbb R}|\partial_t^jC_n(e^t)|=O(n^{-2})\) for \(j=0,1,2\). The strict, isolated global maximum of \(B(e^t)\) at \(t=0\) forces every global maximizer \(t_n\to0\). Moreover
\[
\frac{d^2}{dt^2}B(e^t)\bigg|_{t=0}
=-\frac1\pi\int_0^\pi\frac{\sin k}{(1+\sin k)^2}dk=-\frac{2}{3\pi}<0.
\]
Thus there is a fixed neighborhood of zero where the full objective is strictly concave for all sufficiently large \(n\); all maximizers lie there, so the global maximizer is eventually unique. Its derivative at the matching point is
\[
D_n:=\frac{d}{dt}C_n(e^t)\bigg|_{t=0}=\frac2\pi\int_0^1q^{2n-2}\frac{(1-q^2)^2}{(1+q^2)^2}dq
=\frac{1}{2\pi n^3}+O(n^{-4}).
\]
The last step follows by replacing \((1+q^2)^{-2}\) with \(1/4+O(1-q)\), using the exact beta integral \(\int_0^1q^{2n-2}(1-q^2)^2dq=[(n-1/2)(n+1/2)(n+3/2)]^{-1}\), and bounding the error by the next beta moment. Taylor expansion of the strictly concave first-order equation gives
\[
t_n=\frac{D_n}{2/(3\pi)}+O(n^{-5})=\frac{3}{4n^3}+O(n^{-4}),\qquad
\eta_n^*=e^{t_n}=1+\frac{3}{4n^3}+O(n^{-4}).
\]
The \(O(n^{-5})\) first-order-equation remainder uses \(t_n=O(n^{-3})\), the bounded third derivative of \(B\) locally and the uniform \(O(n^{-2})\) bound on \(C_n''\). Independently, for every fixed \(\eta>0\), the source correction has the sharp leading form \(C_n(\eta)=\eta/[\pi(1+\eta^2)n^2]+O(n^{-3})\).

## Verification
The standalone file `CHECK.py` evaluates the exact integrals numerically, tests the strict spatial ordering, finite-site optimization and inverse-cubic scale, and compares the integral against independent finite-chain non-Hermitian evolution. It reports 285 passing numerical assertions. These finite tests do not prove strict ordering for all sites or the asymptotic theorems, which follow from the displayed positive integrands, uniform bounds, beta integrals and concavity argument.

## Relationship to prior work
Riberi's latest publicly available version, arXiv:2605.08056v4, already proves the exact absorption integral above, the strong/weak large-distance duality, its \(O(n^{-2})\) spatial correction, and onset of duality-breaking at \(O(n^{-3})\). It states that the optimal rate approaches equal hopping and loss from far away. The present claim instead rigorously classifies optimization by initial-site position, proves strict monotonicity across all sites and obtains the explicit optimal-coupling coefficient \(3/4\). Prior finite-path Lindblad-sink mean-time optimization concerns a different observable and a different state space. Discrete-time coined absorption and general finite-graph transport efficiency results do not directly imply this exact half-line cubic optimizer.

## Limitations
Global uniqueness is shown only for all sufficiently large initial sites; a finite maximizer exists for every \(n\ge2\), but uniqueness for every individual finite \(n\) is not claimed. The result is a theorem for eventual absorption, not a finite-time optimum. Quantitative optimality gain above \(\eta=1\) is small far from the boundary. Complete historical originality cannot be guaranteed without further independent literature review. There is no independent audit.

## References
- Francisco Riberi, *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056v4 (first posted 2026-05-08), https://arxiv.org/html/2605.08056v4, especially Eq. (15) and Appendix D.2.
- E. P. M. Amorim, L. R. Cerutti, O. P. de Sá Neto, and M. C. de Oliveira, *Absorption-based qubit estimation in discrete-time quantum walks*, APS Open Science 1, 000015 (2026), https://doi.org/10.1103/zns5-vzyy (different discrete-time coined model).
- *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, Entropy 23, 85 (2021), https://www.mdpi.com/1099-4300/23/1/85 (finite-graph trapping context; abstract and search-visible excerpt only).
