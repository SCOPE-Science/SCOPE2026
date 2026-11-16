# Sharp spectral conditioning of atomic Bergman-kernel dilations on Hardy space

## Finding
For real \(p>1\) and \(0<q<1\), the single-atom Bergman-kernel Cesàro operator on the classical Hardy space,
\[
(T_{p,q}f)(z)=\frac{f(qz)}{(1-qz)^p},\qquad z\in\mathbb D,
\]
has a canonical orthonormal-in-each-vector (but nonorthogonal as a family) eigenbasis with exactly computable, globally sharp Riesz bounds. Put
\[
h(z)=\prod_{k=1}^{\infty}(1-q^kz)^{-p},\qquad N=\|h\|_{H^2}^2,\qquad\psi_n(z)=\frac{h(z)z^n}{\sqrt N}.
\]
Then \(T_{p,q}\psi_n=q^n\psi_n\), and for every finitely supported complex sequence \((c_n)\),
\[
\frac{\prod_{k=1}^{\infty}(1+q^k)^{-2p}}{N}\sum_{n\ge0}|c_n|^2
\le \left\|\sum_{n\ge0}c_n\psi_n\right\|_{H^2}^2
\le \frac{\prod_{k=1}^{\infty}(1-q^k)^{-2p}}{N}\sum_{n\ge0}|c_n|^2.
\]
Both constants are optimal. All nonzero eigenvalues are simple, so the same sharp bounds hold for any unit-normalized eigenbasis, up to unimodular coefficient changes. Its squared condition number is
\[
\kappa_{p,q}=\left[\prod_{k=1}^{\infty}\frac{1+q^k}{1-q^k}\right]^{2p},
\qquad
\lim_{\epsilon\downarrow0}\epsilon\log\kappa_{p,e^{-\epsilon}}=\frac{p\pi^2}{2}.
\]

The rank-one Riesz spectral projection at \(q^n\), denoting \(1/h=\sum_{j\ge0}b_jz^j\), satisfies the exact identity
\[
(P_nf)(z)=h(z)z^n[z^n](f/h),\quad
\|P_n\|=\|h\|_{H^2}\biggl(\sum_{j=0}^{n}|b_j|^2\biggr)^{1/2}.
\]
Hence the projection norms converge to \(\|h\|_{H^2}\|1/h\|_{H^2}\), with
\[
\lim_{\epsilon\downarrow0}\epsilon\log\left(\lim_{n\to\infty}\|P_n\|\right)=\frac{p\pi^2}{4}.
\]
The comparison of exponentially diverging eigenbasis and projector conditioning quantifies nonnormal spectral instability even though the eigenvalues remain the simple sequence \(1,q,q^2,\ldots\).

## Assumptions and scope
The norm is the standard Hardy norm \(\|\sum a_nz^n\|_{H^2}^2=\sum|a_n|^2\). The real kernel exponent satisfies \(p>1\), corresponding to the normalized standard weighted Bergman kernel exponent \(\alpha=p-2>-1\). The atom is located at the positive real point \(q\in(0,1)\) with unit mass. Every infinite product converges uniformly on the closed disk, with its analytic branch fixed by positive value at zero. All limits use \(\epsilon=-\log q\). Spectral projections are those of the compact operator on \(H^2\); no matrix truncation is used in their definition.

## Proof
**Conjugacy and spectrum.** The logarithms of \(h\) and \(1/h\) converge uniformly on the closed disk since \(\sum q^k<\infty\). Both are bounded analytic multipliers with bounded inverses. Product cancellation gives \((1-qz)^{-p}h(qz)=h(z)\). Thus
\[
T_{p,q}=M_h C_q M_h^{-1},\qquad C_qf(z)=f(qz).
\]
The diagonal map \(C_q\) is trace class, with precisely simple eigenvalues \(q^n\) and an additional spectral point zero. Similarity proves these statements for \(T_{p,q}\), as well as completeness and uniqueness of each eigendirection. Because \(z^n\) is inner, all \(hz^n\) have the same norm \(\sqrt N\). The unit-normalized eigenvectors therefore differ only by phases.

**Exact sharp bounds.** Multiplication by \(h/\sqrt N\) sends the monomial orthonormal basis onto \((\psi_n)\). Its norm is \(\sup_{|z|=1}|h(z)|/\sqrt N\), and its inverse minimum modulus is \(1/(\sqrt N\|1/h\|_\infty)\). For every \(|z|=1\) and integer \(k\ge1\),
\[
1-q^k\le|1-q^kz|\le1+q^k.
\]
All minima align at \(z=1\), and all maxima at \(z=-1\). Consequently \(\|h\|_\infty=\prod(1-q^k)^{-p}\) and \(\|1/h\|_\infty=\prod(1+q^k)^p\). These give the displayed bounds. They are *globally sharp*: the normalized analytic polynomials \(N_0^{-1/2}\sum_{j=0}^{N_0-1}(\pm z)^j\) have squared boundary modulus equal to a Fejér kernel concentrating at \(z=\pm1\), respectively. Hence their multiplier quotients converge to the maximum and minimum values on the circle.

**Exact spectral projectors.** Similarity gives \(P_n=M_h\Pi_nM_{1/h}\), where \(\Pi_n\) is coefficient projection onto \(z^n\). Writing \(1/h=\sum b_jz^j\), the functional \(f\mapsto[z^n](f/h)\) is represented by the coefficient vector supported on \(0\le j\le n\), with squared norm \(\sum_{j=0}^n|b_j|^2\). Its output vector \(hz^n\) has norm \(\|h\|_{H^2}\). A rank-one operator's norm is the product of these norms. Parseval gives the increasing limit as \(n\to\infty\).

**Exponential rates.** Write \(q=e^{-\epsilon}\). The Riemann-sum limits (both improper integrals are absolutely convergent) give
\[
\epsilon\sum_{k\ge1}-\log(1-e^{-k\epsilon})\to\int_0^\infty-\log(1-e^{-x})\,dx=\frac{\pi^2}{6},
\]
\[
\epsilon\sum_{k\ge1}\log(1+e^{-k\epsilon})\to\int_0^\infty\log(1+e^{-x})\,dx=\frac{\pi^2}{12}.
\]
The integrals follow by integrating their absolutely integrable power series and using \(\sum_{j\ge1}j^{-2}=\pi^2/6\). Their sum immediately yields \(\epsilon\log\kappa\to p\pi^2/2\).

For the projection rate we also need Hardy norms, not just boundary suprema. Let \(g=h\) and \(g=1/h\) separately. In either case the logarithm of its boundary modulus has angular derivative bounded in absolute value by
\[
p\sum_{k\ge1}\frac{e^{-k\epsilon}}{1-e^{-k\epsilon}}=O\left(\frac{\log(1/\epsilon)}{\epsilon}\right).
\]
For \(h\), the maximum occurs at angle zero; for \(1/h\), at angle \(\pi\). An arc of angular width \(\epsilon^2\) around the respective maximizing point has logarithmic modulus within \(o(1)\) of the maximum. Integrating the Hardy boundary modulus squared on this arc implies
\[
\log\|g\|_{H^2}=\log\|g\|_\infty+O(|\log\epsilon|)
\]
for \(\epsilon\downarrow0\) (the upper inequality is immediate). Consequently
\[
\epsilon\log\|h\|_{H^2}\to\frac{p\pi^2}{6},\qquad
\epsilon\log\|1/h\|_{H^2}\to\frac{p\pi^2}{12}.
\]
Adding completes the projector-rate formula.

## Verification
Execute the standalone \(\texttt{CHECK.py}\) with Python 3 (standard library only). It checks the coefficient recursion of both reciprocal infinite products, their convolution identity, eigenvector identities through finite Taylor order, and the exact Riesz-product ratio for a grid of positive exponents and atoms. It also checks explicit finite spectral-projection coefficient norms against rank-one formulas. These finite calculations corroborate algebra only; the proof above, especially the infinite-product convergence and asymptotic boundary estimates, establishes the infinite-dimensional claims.

## Relationship to prior work
Blasco and Pennanen introduced and studied this positive-measure Bergman-kernel Cesàro family (arXiv:2609.21657, first public September 18, 2026). Their principal theorems characterize boundedness between analytic-function spaces, not the canonical eigenvector Riesz condition number or individual spectral projection norms for a single atom. Lechner, Li, Queffélec and Rodríguez-Piazza (arXiv:1612.01177; 2018 journal article) study approximation numbers for broad weighted composition maps, with major focus on lens symbols and operator ideals; their inspected arguments do not supply the present exact eigenvector conditioning. Doctor and collaborators (arXiv:2111.07853) focus on spectra for parabolic quadratic composition symbols. The elementary similarity step uses standard multiplier theory; the claim is the complete quantitative spectral-basis and spectral-projection statement for the concrete kernel-induced atomic family, not a general new similarity principle.

## Limitations
No result is claimed for non-atomic measures, sums of distinct atoms, complex atom locations, or any weighted Bergman space as the *acting* space. The sharp Riesz bounds apply to unit-normalized eigenvectors; they are not asserted to minimize similarity condition over arbitrary rescalings. The results do not give optimal eigenvalue perturbation bounds under arbitrary operator noise. The publication-priority comparison remains provisional for older weighted-composition literature not indexed or fully accessible; no independent audit is claimed.

## References
1. O. Blasco and A. Pennanen, *Cesàro operator induced by a Bergman kernel*, arXiv:2609.21657, first publicly posted September 18, 2026. https://arxiv.org/abs/2609.21657
2. G. Lechner, D. Li, H. Queffélec and L. Rodríguez-Piazza, *Approximation numbers of weighted composition operators*, arXiv:1612.01177; J. Funct. Anal. 274 (2018), 1928–1958. https://arxiv.org/abs/1612.01177
3. J. Doctor, T. Hodges, S. Kaschner, A. McFarland and D. Thompson, *Spectra of Weighted Composition Operators with Quadratic Symbols*, arXiv:2111.07853 (2021). https://arxiv.org/abs/2111.07853
4. I. Chalendar and J. R. Partington, *Weighted composition operators: isometries and asymptotic behaviour*, J. Operator Theory 86 (2021), 189–201. https://jot.theta.ro/jot/archive/2021-086-001/2021-086-001-010.html
