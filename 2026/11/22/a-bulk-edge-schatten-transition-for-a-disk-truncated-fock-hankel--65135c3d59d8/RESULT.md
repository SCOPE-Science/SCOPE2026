# A bulk–edge Schatten transition for a disk-truncated Fock Hankel operator

## Finding
Let \(\mathcal F^2\) be the analytic Gaussian Fock space on the complex plane, with Gaussian measure \(d\mu(z)=\pi^{-1}e^{-|z|^2}dA(z)\), and let \(P\) be the orthogonal Fock projection. For each real \(T>0\), consider the big Hankel operator
\[
H_T=(I-P)M_{\overline z\mathbf1_{\{|z|^2\le T\}}}|_{\mathcal F^2}:\mathcal F^2\to L^2(\mu)\ominus\mathcal F^2.
\]
This is a bounded compact operator belonging to every Schatten quasi-ideal \(\mathcal S_p\), \(p>0\). Define
\[
q_n(T)=\Pr\{X_T\ge n+1\},\quad X_T\sim\operatorname{Pois}(T),\quad n\ge0.
\]
Its **complete squared singular-value multiset**, before decreasing rearrangement, is
\[
\boxed{\lambda_n(T)=(n+1)q_{n+1}(T)-nq_n(T)^2,\quad n\ge0.}
\]
Here the term involving \(n\) is zero at \(n=0\). Let \(\Phi\) denote the standard normal distribution function, and for every \(p>0\) set
\[
I_p=\int_{-\infty}^{\infty}[\Phi(u)\Phi(-u)]^{p/2}\,du.
\]
Then the spectral boundary layer is locally uniform: for each fixed real \(u\),
\[
\lim_{T\to\infty}\frac{\sqrt{\lambda_{\lfloor T+u\sqrt T\rfloor}(T)}}{\sqrt T}
=\sqrt{\Phi(u)\Phi(-u)}.
\]
In particular \(\|H_T\|/\sqrt T\to1/2\), and for each fixed \(0<\eta<1/2\),
\[
\lim_{T\to\infty}\frac{\#\{n:\lambda_n(T)>\eta^2T\}}{\sqrt T}
=2\Phi^{-1}\!\left(\frac{1+\sqrt{1-4\eta^2}}2\right).
\]
There are **three sharply different Schatten-power laws**, for every fixed \(p>0\):
\[
\boxed{\begin{aligned}
0<p<1:&\quad \lim_{T\to\infty}T^{-1}\|H_T\|_{\mathcal S_p}^{p}=1,\\
p=1:&\quad \lim_{T\to\infty}T^{-1}\|H_T\|_{\mathcal S_1}=1+I_1,\\
p>1:&\quad \lim_{T\to\infty}T^{-(p+1)/2}\|H_T\|_{\mathcal S_p}^{p}=I_p.
\end{aligned}}
\]
In particular \(I_2=\pi^{-1/2}\). The extra \(1\) in the critical trace limit records order-\(T\) bulk singular values of size approximately one, alongside a \(\sqrt T\)-wide boundary layer with singular values of order \(\sqrt T\).

## Assumptions and scope
All results hold for every real \(T>0\) in the fixed one-complex-dimensional Gaussian space, and for each fixed \(0<p<\infty\) in the stated asymptotics. The space \(\mathcal F^2\) is the closed span of \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\), in \(L^2(\mu)\). Multiplication by the symbol is bounded since its modulus is at most \(\sqrt T\). In the Schatten quasi-ideal notation, \(\|H_T\|_{\mathcal S_p}^p=\sum_n s_n(H_T)^p\); for \(p<1\) this denotes the usual quasi-norm power. The symbol is explicitly discontinuous at the disk boundary; no smooth-symbol extension is asserted.

## Proof
**Exact diagonalization.** In polar coordinates \(t=|z|^2\), radial Gaussian integration is \(e^{-t}dt\). The vectors \(M_{\overline z\mathbf1_{\{t\le T\}}}e_n\) have distinct angular frequencies \(n-1\), so the residuals after projection remain mutually orthogonal. Direct integration gives
\[
\big\|M_{\overline z\mathbf1_{\{t\le T\}}}e_n\big\|^2
=\frac1{n!}\int_0^T t^{n+1}e^{-t}dt=(n+1)q_{n+1}(T),
\]
and, when \(n\ge1\), the only nonzero analytic Fourier coefficient is that of \(e_{n-1}\):
\[
\left|\langle M_{\overline z\mathbf1_{\{t\le T\}}}e_n,e_{n-1}\rangle\right|^2
=\frac{\bigl(\int_0^T t^ne^{-t}dt\bigr)^2}{n!(n-1)!}=nq_n(T)^2.
\]
At \(n=0\) the analytic projection vanishes. Orthogonality proves the exact full squared singular-value formula. Positivity follows from the strict Cauchy–Schwarz inequality for the nonzero multiplier restricted to the disk, and \(\lambda_n\le(n+1)q_{n+1}\). Poisson factorial tails give membership in every \(\mathcal S_p\) for fixed \(T\).

**A two-population identity.** Write \(d_n=q_n(1-q_n)\) and \(r_n=\Pr\{X_T=n+1\}\). Since \(q_{n+1}=q_n-r_n\),
\[
\lambda_n=q_n+n d_n-(n+1)r_n.\tag{1}
\]
The Poisson central limit theorem, uniformly for \(u\) in compact intervals, gives \(q_{\lfloor T+u\sqrt T\rfloor}\to\Phi(-u)\), \(r_{\lfloor T+u\sqrt T\rfloor}=O(T^{-1/2})\). Dividing (1) by \(T\) yields the asserted boundary profile. The product \(\Phi(u)\Phi(-u)\) is symmetric, strictly decreasing for positive \(u\) and reaches its unique maximum \(1/4\) at zero, yielding the operator-norm and threshold-counting constants once tail control is established.

**Uniform tail estimates.** Standard elementary Poisson Chernoff bounds give, with absolute positive constants \(c,C\), for all sufficiently large \(T\):
\[
 d_n\le C\exp[-c(n-T)^2/T]\quad(T/2\le n\le2T),
\]
and factorially summable large-deviation tails for \(n>2T\), while \(d_n\) decays exponentially in \(T\) for \(n<T/2\). The same bounds hold for \(r_n\), with the additional local factor \(O(T^{-1/2})\). They justify all boundary Riemann sums and show that for each fixed \(p>0\),
\[
T^{-(p+1)/2}\sum_{n\ge0}(n d_n)^{p/2}\longrightarrow I_p,
\qquad
T^{-1}\sum_{n\ge0}q_n^{p/2}\longrightarrow1.\tag{2}
\]
These statements also show that no far-tail singular value contributes to the norm or positive-level counting limit. The identity \(I_2=1/\sqrt\pi\) follows from \(\int\Phi(u)\Phi(-u)du=\mathbb E[(Z_1-Z_2)_+]\) for independent standard normals \(Z_1,Z_2\).

**Schatten powers away from the critical point.** Since \(0\le\lambda_n\le q_n+n d_n\), for each \(p>0\) there is \(C_p<\infty\) such that \(\lambda_n^{p/2}\le C_p[q_n^{p/2}+(n d_n)^{p/2}]\). For \(0<p<1\), subadditivity permits \(C_p=1\); (2) gives the upper limit \(1\) after division by \(T\). For any fixed \(0<\delta<1\), uniformly for \(n\le(1-\delta)T\), the identity (1) and Poisson large deviations yield \(\lambda_n\to1\); these indices give the lower limit at least \(1-\delta\). Send \(\delta\downarrow0\). For \(p>1\), (2) shows that the bulk contribution is negligible on the \(T^{(p+1)/2}\) scale. On each fixed central window \(|n-T|\le A\sqrt T\), local uniform boundary convergence gives the lower Riemann-sum limit \(\int_{-A}^A[\Phi(u)\Phi(-u)]^{p/2}du\). The global upper bound from (2), followed by \(A\to\infty\), proves the \(p>1\) law.

**Critical trace.** Set \(a_n=\sqrt{q_n}\), \(b_n=\sqrt{n d_n}\), \(c_n=\sqrt{(n+1)r_n}\). Equation (1) and nonnegativity imply
\[
0\le a_n+b_n-\sqrt{\lambda_n}\le\min(a_n,b_n)+c_n.\tag{3}
\]
For each fixed \(0<\delta<1/2\), the sum of \(\min(a_n,b_n)\) over \(|n-T|\le\delta T\) is at most \(2\delta T+O(1)\); outside, Poisson large deviations make it \(o(T)\). Letting \(\delta\downarrow0\) shows \(\sum\min(a_n,b_n)=o(T)\). Also \(\sum c_n=o(T)\): in the same central interval, Cauchy–Schwarz and \(\sum_{n\ge0}(n+1)r_n=\mathbb E X_T=T\) bound its contribution by \((2\delta)^{1/2}T+o(T)\), and the exterior terms are \(o(T)\) by large-deviation bounds. Thus summing (3), dividing by \(T\) and using (2) at \(p=1\) gives exactly \(1+I_1\). This argument treats the competing bulk and edge populations rather than incorrectly discarding either one.

## Verification
The standalone `CHECK.py` computes the entire diagonal spectrum from Poisson tails, independently checks 64 mode identities against direct Gaussian radial quadratures, checks the exact Gaussian integral at \(p=2\), and compares finite large-disk norm, bulk, edge and Schatten values. It passed 108 numerical assertions. The unlimited-\(T\), all-\(p\) conclusions are supported by the analytic proof above, not by these finite tests. Reproduce with Python 3, NumPy and SciPy by running `python CHECK.py`.

## Relationship to prior work
Qin, *Schatten limits for semi-commutators in Toeplitz quantization on Fock space* (arXiv:2610.30787, first posted 2026-10-22), gives general criteria for vanishing Schatten semiclassical limits, but its available abstract does not provide an expanding-disk Hankel singular spectrum or the sharp coexistence of bulk and edge at trace exponent one. Bauer, Coburn and Hagger (arXiv:1704.05652) supply the general Toeplitz/Hankel semi-commutator identity, not the above spectral asymptotics. Liu, Wang and Zeng (arXiv:2609.26810) characterize boundedness and compactness for broad weighted Fock Hankel classes, rather than this fixed-symbol spectral counting law.

Two especially close published examples have been compared at the level of their complete results. *A Gaussian boundary-interaction law for nested Fock disk semi-commutators* (published-finding corpus record `12a369cea2df`, 2026-11-08) derives the **same Gaussian product** for the spectrum of a diagonal product of disk Toeplitz operators. That product has only a single edge population and Schatten sums of order \(\sqrt T\), whereas the present truncated **anti-analytic big Hankel** operator has an extra order-\(T\) bulk population, squared singular values of order \(T\) at its edge, and the sharp Schatten threshold at \(p=1\). The shared boundary CDF mechanism is credited and does not by itself establish the mixed trace constant \(1+I_1\). *Boundary-Gaussian singular spectrum of disk transfer between the first two Landau levels* (published-finding corpus record `04a288b07a35`, 2026-11-01) proves a Gaussian **density** spectral profile for an interlevel disk projection, not the present square root of a Gaussian **tail product**, and has no bulk population. Neither result is claimed as a new derivation here.

## Limitations
The theorem concerns a single complex dimension, the standard Gaussian weight and a disk-truncated linear anti-holomorphic symbol. It does not prove analogous constants for smooth boundaries, other angular harmonics, higher-dimensional weights or changing Schatten exponent. The limiting boundary CDF profile itself is closely related to previously known disk Toeplitz boundary profiles; the asserted addition is the exact Hankel spectrum and its **combined** sharp bulk/edge Schatten transition. Broader pre-existing semiclassical Hankel results could implicitly contain parts of the finding. Qin's complete 88-page preprint was not retrieved for a whole-document exclusion; the comparison is limited to its available detailed abstract. The separate mathematical audit has not been performed.

## References
- J. Qin, *Schatten limits for semi-commutators in Toeplitz quantization on Fock space*, arXiv:2610.30787v1, first publicly posted 2026-10-22, https://arxiv.org/abs/2610.30787.
- W. Bauer, L. Coburn and R. Hagger, *Toeplitz Quantization on Fock Space*, arXiv:1704.05652, https://arxiv.org/abs/1704.05652.
- G. Liu, X. Wang and Z. Zeng, *Bergman Kernels and Hankel Operators on Weighted Fock Spaces in Several Complex Variables*, arXiv:2609.26810v1, first publicly posted 2026-09-16, https://arxiv.org/abs/2609.26810.
- *A Gaussian boundary-interaction law for nested Fock disk semi-commutators*, published-finding corpus published research (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-gaussian-boundary-interaction-law-for-nested-fock-disk-semi-co--12a369cea2df.
- *Boundary-Gaussian singular spectrum of disk transfer between the first two Landau levels*, published-finding corpus published research (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-boundary-gaussian-singular-spectrum-of-disk-transfer-between-the--04a288b07a35.
