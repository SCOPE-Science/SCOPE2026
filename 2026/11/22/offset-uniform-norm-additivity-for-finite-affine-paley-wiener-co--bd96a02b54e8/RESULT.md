# Offset-uniform norm additivity for finite affine Paley–Wiener composition sums

## Finding
Let \(N\geq3\), \(\sigma,\tau>0\), and take pairwise distinct real numbers \(a_1,\ldots,a_N>0\) with \(\sigma\max_j a_j\leq\tau\). Fix nonzero complex coefficients \(c_1,\ldots,c_N\). For every vector of real offsets \(b=(b_1,\ldots,b_N)\), let
\[
T_b:B_\sigma^2\longrightarrow B_\tau^2,\qquad
(T_bf)(z)=\sum_{j=1}^N c_jf(a_jz+b_j).
\]
Write \(d_j=c_j/\sqrt{a_j}\), \(\ell_j=\log a_j\), and \(L=\sum_{j=1}^N|d_j|\). Define the compact subgroup
\[
H=\overline{\{(e^{-it(\ell_j-\ell_1)})_{j=2}^N:t\in\mathbb R\}}\ \subseteq\ \mathbb T^{N-1}
\]
and the phase target \(r=(r_2,\ldots,r_N)\), where
\[
r_j=\frac{d_1}{|d_1|}\frac{\overline{d_j}}{|d_j|}.
\]
Then the following are equivalent:

1. \(r\in H\).
2. **For every** real offset vector \(b\), the operator norm and the essential norm both equal the sum of the individual operator norms: \(\|T_b\|=\|T_b\|_{\mathrm e}=L\).
3. For zero offsets, \(\|T_0\|=L\).

Whenever these conditions hold, **every approximation number is flat**:
\[
a_k(T_b)=L\qquad(k\geq1,\ b\in\mathbb R^N).
\]
The phase condition has a fully arithmetic form: it holds if and only if
\[
\prod_{j=2}^N r_j^{m_j}=1
\quad\text{for every }(m_2,\ldots,m_N)\in\mathbb Z^{N-1}
\text{ such that }\sum_{j=2}^N m_j(\ell_j-\ell_1)=0.
\]
In particular, if the \(N-1\) logarithmic ratios \(\log(a_j/a_1)\), \(2\leq j\leq N\), are linearly independent over \(\mathbb Q\), then **arbitrary complex coefficient phases and arbitrary real offsets give exact norm additivity and flat approximation numbers**. This independence holds outside a countable union of proper hypersurfaces of the positive slope parameter space.

The condition cannot simply be dropped. At zero offsets, slopes \((1,2,4)\), and coefficients \((1,1,-1)\), the exact norm for every \(\tau\geq4\sigma\) is
\[
\|C_z+C_{2z}-C_{4z}\|=\frac{3\sqrt5}{4}
<1+\frac1{\sqrt2}+\frac12=L.
\]
For slopes \((1,2,s)\) with \(\log s/\log2\notin\mathbb Q\), by contrast, the corresponding norm equals \(1+1/\sqrt2+1/\sqrt s\), for every choice of real offsets. Thus logarithmic resonance can cause a strict, explicit cancellation deficit, whereas the nonresonant additivity is robust to all affine offsets.

## Assumptions and scope
The Hilbert Paley–Wiener space \(B_\sigma^2\) consists of entire functions of exponential type at most \(\sigma\) whose restrictions to \(\mathbb R\) are square-integrable, equipped with the real-line \(L^2\) norm. Equivalently, the unitary Fourier transform identifies it with \(L^2([-\sigma,\sigma])\). Here \(\|T\|_{\mathrm e}=\inf\{\|T-K\|:K\text{ compact}\}\) and \(a_k(T)=\inf\{\|T-R\|:\operatorname{rank}R<k\}\). All \(b_j\) are real: complex offsets have different individual norm factors and are not covered. Coefficients must be nonzero and slopes positive and pairwise distinct; duplicate slopes can first be combined only when their affine offsets also coincide.

## Proof
**Fourier normalization and upper bound.** With the convention \(f(x)=(2\pi)^{-1/2}\int e^{ix\xi}\widehat f(\xi)\,d\xi\), the Fourier transform of \(f(a_jx+b_j)\) is
\[
a_j^{-1}e^{ib_j\eta/a_j}\widehat f(\eta/a_j).
\]
It is supported in \([-a_j\sigma,a_j\sigma]\). A change of variables on the real line gives \(\|C_{a_jz+b_j}\|=a_j^{-1/2}\) (real offsets are isometric translations), so \(\|T_b\|\leq L\) for every \(b\).

**A Mellin boundary witness, including essential norm.** Restrict the Fourier input to positive frequencies and put \(x=\log\eta\). The unitary logarithmic-coordinate map sends \(\widehat f\) to \(g(x)=e^{x/2}\widehat f(e^x)\), supported on \(( -\infty,\log\sigma]\). On this channel,
\[
(\mathcal M T_b\mathcal M^{-1}g)(x)
=\sum_{j=1}^N d_j e^{ib_je^x/a_j}g(x-\ell_j).
\]
For \(R>0\), \(t\in\mathbb R\), and \(B\leq\log\sigma\), take the normalized logarithmic packet
\[
g_{R,B,t}(x)=R^{-1/2}e^{itx}\mathbf1_{[B-R,B]}(x).
\]
All its images lie in the allowed output bandwidth, since \(B+\max_j\ell_j\leq\log\tau\). At fixed \(R,t\), letting \(B\to-\infty\) removes the offset factors uniformly on the supports: \(e^{ib_je^x/a_j}\to1\). For zero offsets, overlap lengths give the **exact** identity
\[
\|T_0g_{R,B,t}\|^2
=\sum_{j,k=1}^N d_j\overline{d_k}e^{-it(\ell_j-\ell_k)}
\left(1-\frac{|\ell_j-\ell_k|}{R}\right)_+.
\]
Consequently, as \(R\to\infty\), these squared norms tend to \(|m(t)|^2\), where
\[
m(t)=\sum_{j=1}^N d_je^{-it\ell_j}.
\]
For each fixed \(R,t\), the packets with \(B\to-\infty\) are weakly null, while every compact operator sends them to norm-null vectors. It follows that
\[
\boxed{\quad\|T_b\|_{\mathrm e}\geq\sup_{t\in\mathbb R}|m(t)|\quad}
\]
for *every* real offset vector. In particular this lower bound is independent of the offsets.

**Exact unshifted norm.** At \(b=0\), logarithmic Fourier coordinates on the positive and negative frequency channels extend to full-line translation operators. Plancherel in the logarithmic coordinate diagonalizes their finite sum as multiplication by \(m(t)\). Restricting the input to \(x\leq\log\sigma\) cannot increase the full-line norm. The boundary packets give the reverse inequality, hence
\[
\|T_0\|=\|T_0\|_{\mathrm e}=\sup_{t\in\mathbb R}|m(t)|.
\]
The same symbol occurs on both frequency signs because all slopes are positive and offsets vanish.

**Triangle equality and integer relations.** Put \(z_j(t)=d_je^{-it\ell_j}\). For fixed nonzero magnitudes \(|z_j(t)|=|d_j|\), the identity
\[
L^2-|\textstyle\sum_jz_j(t)|^2
=2\sum_{i<j}|d_i||d_j|\bigl(1-\cos(\arg z_i(t)-\arg z_j(t))\bigr)
\]
shows that \(\sup_t|m(t)|=L\) precisely when the ratios of all phases approach one. Relative to the first phase, this is exactly the assertion \(r\in H\). The character-annihilator form of the one-parameter Kronecker density theorem gives the displayed integer-relation criterion. If the condition holds, the essential-norm lower bound and triangle upper bound squeeze both norms to \(L\) for every \(b\). Conversely, equality for zero offsets forces \(r\in H\). Finally, every finite-rank operator is compact, so \(L=\|T_b\|_{\mathrm e}\leq a_k(T_b)\leq\|T_b\|=L\).

**Exact resonance boundary.** For \((a_j)=(1,2,4)\), \((c_j)=(1,1,-1)\), write \(z=e^{-it\log2}\). Then
\[
m(t)=1+2^{-1/2}z-2^{-1}z^2,
\quad |m(t)|^2=\frac{11}4+\frac{\cos\theta}{\sqrt2}-2\cos^2\theta,
\quad z=e^{i\theta}.
\]
The concave quadratic is maximized at \(\cos\theta=1/(4\sqrt2)\), with value \(45/16\). The exact norm is therefore \(3\sqrt5/4\). For \((1,2,s)\), the logarithmic ratios are rationally independent when \(\log s/\log2\) is irrational; the density theorem then forces full triangle equality regardless of the offsets.

## Verification
The included `witness_check.py` uses only the Python standard library. Running `python witness_check.py` prints `PALEY_MELLIN_OFFSET_WITNESS_OK` and checks the exact three-slope resonant maximum, the explicit finite-packet overlap identity at increasing window lengths, and a generic nonresonant case with three nonzero, unequal real offsets. These finite tests are **not** used as proofs of the full theorem: the infinite-dimensional statement is established by the Fourier–Mellin packet limit and the Kronecker phase criterion above.

## Relationship to prior work
Lin, Lu, Yang and Zu (arXiv:2611.19948v1, posted 15 November 2026) establish no-cancellation and two-sided Schatten/essential-norm comparisons for finite sums of weighted compositions on Gaussian Fock space, not exact norm additivity for affine sums on Paley–Wiener space. Classical Paley–Wiener affine-symbol and range results identify individual composition operators (Mukherjee–Jafari–McInroy 2010); Álvarez–Severiano (arXiv:2508.19975) analyze spectra and dynamics of individual operators. Hai, Huy and Tien (arXiv:2611.21261v1, posted 16 November 2026) treat individual operator norms, differences and component topology, but not the offset-uniform finite-sum classification. The Mellin transform, Fourier-multiplier norm identity and Kronecker density theorem are classical ingredients and not claimed as new. The contribution assessed here is their exact combination into an offset-uniform **if and only if** norm/essential-norm/approximation-number theorem with an explicit resonance boundary for Paley–Wiener affine composition sums.

## Limitations
The result is for finite sums with positive, pairwise distinct slopes, nonzero coefficients and **real** affine offsets; it does not classify sums with nonreal offsets, arbitrary entire weights, or endpoint \(p\ne2\) spaces. When the phase-compatibility condition fails, the zero-offset norm is known exactly through \(m\), but arbitrary-offset norms are not classified. Published general Toeplitz/Wiener–Hopf and covariant-representation methods could contain an implicit formulation of parts of the result; the offset-uniform equivalence should receive independent literature review. There is no independent mathematical audit.

## References
1. Z. Lin, Y. Lu, R. Yang and C. Zu, *Finite Sums of Weighted Composition Operators on the Fock Space*, arXiv:2611.19948v1 (15 November 2026), https://arxiv.org/html/2611.19948v1.
2. P. V. Hai, V. N. Huy and P. T. Tien, *Analytic Tools and Weighted Composition Operators on Paley–Wiener Spaces*, arXiv:2611.21261v1 (16 November 2026), https://arxiv.org/html/2611.21261v1.
3. C. F. Álvarez and O. R. Severiano, *Spectra of Composition Operators on Paley–Wiener Spaces and Some Consequences*, arXiv:2508.19975 (27 August 2025), https://arxiv.org/abs/2508.19975.
4. S. Mukherjee, F. Jafari and J. E. McInroy, *On the Range of Composition Operators on Spaces of Entire Functions*, arXiv:1006.2793 (7 June 2010), https://arxiv.org/abs/1006.2793.
5. Classical Plancherel/Mellin Fourier multiplier theory and the one-parameter Kronecker density theorem (used in their standard forms).
