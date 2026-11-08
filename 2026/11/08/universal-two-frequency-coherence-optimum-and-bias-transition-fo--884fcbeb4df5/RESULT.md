# Universal two-frequency coherence optimum and bias transition for finite odd-base Cantor measures

## Finding
Let \(b\ge3\) be odd, \(m\ge1\), \(N=b^m\), and \(0<w_j<1\) for every \(1\le j\le m\). Let \(\nu\) be the distribution on \(\mathbb R/\mathbb Z\) of
\[
X=\sum_{j=1}^m\frac{2\varepsilon_j}{b^j},\qquad \mathbb P(\varepsilon_j=1)=w_j,
\]
where the digits are independent. Define
\[
\alpha_j=\left((1-2w_j)^2+4w_j(1-w_j)\sin^2\!\left(\frac{\pi}{2b^j}\right)\right)^{1/2},\qquad \rho=\prod_{j=1}^m\alpha_j.
\]
Then \(0<\rho<1\) and the **exact global minimum** over distinct integer frequencies modulo \(N\) is
\[
\min_{1\le k<N}|\widehat\nu(k)|=\rho,
\quad\text{with equality precisely when}\quad 4k\equiv 1\text{ or }-1\pmod N.
\]
In particular, exactly two nonzero residue classes minimize the absolute Fourier coefficient, independent of *all* digit probabilities \(w_j\).

For two distinct characters \(e_u(x)=e^{2\pi iux}\) and \(e_v(x)=e^{2\pi ivx}\), considered in \(L^2(\nu)\), the squared singular values of their two-column analysis matrix are \(1\pm|\widehat\nu(u-v)|\). Therefore the optimal lower two-character Riesz bound is \(1-\rho\); the optimal squared condition number is \((1+\rho)/(1-\rho)\), with exactly the frequency differences specified above.

There is a sharp asymptotic bias distinction when the same weight \(w_j=w\) is used at all levels. At \(w=1/2\),
\[
\rho=\left(\frac\pi2\right)^m b^{-m(m+1)/2}\,C_b(m),\qquad C_b(m)=\prod_{j=1}^m\frac{\sin(\pi/(2b^j))}{\pi/(2b^j)}\longrightarrow C_b\in(0,1).
\]
For any fixed \(w\in(0,1)\setminus\{1/2\}\),
\[
\rho=|1-2w|^m C_{b,w}(m),\quad C_{b,w}(m)=\prod_{j=1}^m\left(1+\frac{4w(1-w)}{(1-2w)^2}\sin^2\!\left(\frac\pi{2b^j}\right)\right)^{1/2}\longrightarrow C_{b,w}\in(1,\infty).
\]
Thus the least pairwise Fourier coherence decays superexponentially in level for fair digits, but exponentially for each fixed nonfair digit bias.

## Assumptions and scope
All statements concern finite level \(m\), odd integer base \(b\), independent binary digits taking the values zero or one but occupying the *spatial digits* zero or two, and all strictly positive Bernoulli weights. Frequencies are integers identified modulo \(b^m\), since \(\nu\) is supported on the \(b^{-m}\) grid. The two-character conditioning optimum ranges over distinct frequency classes; it is not an optimum for general multi-character frames. The Fourier convention is \(\widehat\nu(k)=\int e^{-2\pi ikx}\,d\nu(x)\), whose absolute value is unchanged by the sign choice.

## Proof
**Product formula.** Independence and finite support give
\[
\widehat\nu(k)=\prod_{j=1}^m\left((1-w_j)+w_j e^{-4\pi i k/b^j}\right).
\]
For an odd integer \(M>1\), the residue classes \(4k\pmod M\) visit every residue. Among all \(M\)-th roots of unity, those closest in angle to \(-1\) are the two roots with exponents \((M\pm1)/2\), and their angular distance to \(-1\) is \(\pi/M\). Consequently
\[
\cos\left(\frac{4\pi k}{M}\right)\ge-\cos\left(\frac\pi M\right),
\]
with equality if and only if \(4k\equiv\pm1\pmod M\). Indeed \(2(2k)\equiv\pm1\pmod M\) is exactly the congruence for the two adjacent roots.

For any \(0<w<1\), expand
\[
\left|(1-w)+w e^{-4\pi i k/M}\right|^2
=1-2w(1-w)\left(1-\cos\left(\frac{4\pi k}{M}\right)\right)
\ge(1-2w)^2+4w(1-w)\sin^2\left(\frac\pi{2M}\right).
\]
Equality holds exactly for \(4k\equiv\pm1\pmod M\) because \(w(1-w)>0\). Apply this at \(M=b^j\) for every \(j\). The product is bounded below by \(\rho\). Since \(4\) is invertible modulo the odd number \(N\), exactly two residues satisfy \(4k\equiv\pm1\pmod N\). Each of them also satisfies one of the two congruences modulo every \(b^j\), and hence attains every factorwise minimum simultaneously. Conversely, any minimizing product must attain the minimum in the last factor \(j=m\), which forces one of those two residues. This proves the exact minimum and equality classification. Every \(\alpha_j\) is positive because the sine is positive and \(w_j(1-w_j)>0\), and is strictly less than one because \(\sin(\pi/(2b^j))<1\).

**Riesz bounds.** Each character has unit \(L^2(\nu)\) norm. Their Gram matrix has diagonal entries one and off-diagonal entries conjugate to \(\widehat\nu(u-v)\), so its eigenvalues are \(1\pm|\widehat\nu(u-v)|\). The ratio is strictly increasing in the Fourier magnitude \(r\in(0,1)\). The global two-character optimum and its equality cases therefore follow from the first part.

**Asymptotics.** When \(w=1/2\), \(\alpha_j=\sin(\pi/(2b^j))\). Pulling out \(\pi/(2b^j)\) gives the displayed formula. Since \(\sin t/t=1+O(t^2)\) as \(t\to0\) and \(\sum_j b^{-2j}<\infty\), the remaining product converges to a strictly positive constant below one. For fixed \(w\ne1/2\), factor \(|1-2w|\) from each \(\alpha_j\). The remaining positive factors equal \(1+O(b^{-2j})\), so their product converges to a finite number strictly greater than one. This completes the proof.

## Verification
The standalone `CHECK.py` recomputes finite discrete Fourier coefficients directly from the probability masses, compares their minimizing residues with the two predicted congruence classes, and checks the product formula and Gram eigenvalues for odd bases, multiple levels, both unbiased and biased (including level-varying) digit weights. The general argument above is independent of these numerical tests.

## Relationship to prior work
Pont, Liehr and Taylor (2026) prove that *infinite* fair odd-base Cantor measures do not have exponential Fourier frames, addressing a substantially different global completeness question. Their work supplies the contemporary odd-base motivation, but does not identify the exact optimal two-frequency coherence, its probability-independent optimizers, or the finite-level bias-rate transition above. Dutkay and Ranasinghe (2016) develop *weighted exponentials* as frames on fractal measures; those weights attach to the frame elements, rather than varying the digit probabilities, and their main results do not imply the present universal minimizer. Ferguson, Mayeli and Sothanaphan (2021/2026 manuscript) quantify tightness of exponential bases on finite abelian sets; their general bounds do not yield the exact family-specific weighted Cantor Gram optimum. The factorization of finite Bernoulli Fourier transforms and basic two-vector Gram eigenvalues are standard; the asserted new item is their **joint sharp, all-depth, all-bias minimization with complete equality cases and bias asymptotics**.

## Limitations
This is a finite-dimensional two-character extremum, not an infinite Fourier-frame theorem, a multi-character optimal design theorem, or a noisy-inversion guarantee. The digit probabilities are assumed strictly between zero and one; at boundary probabilities the distribution may collapse and uniqueness of minimizers fails. The finite-level exact result does not assert anything about integer-frequency differences in an infinite nonperiodic measure. The proof uses elementary root geometry, so earlier equivalent optimization statements could exist under other terminology.

## References
1. J. de Dios Pont, L. Liehr, M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, first public 2026-07-09, arXiv:2607.08656, https://arxiv.org/abs/2607.08656.
2. D. E. Dutkay, R. Ranasinghe, *Weighted Fourier frames on fractal measures*, 2016, arXiv:1602.04749, https://arxiv.org/abs/1602.04749.
3. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, https://arxiv.org/html/1904.04487v6.
