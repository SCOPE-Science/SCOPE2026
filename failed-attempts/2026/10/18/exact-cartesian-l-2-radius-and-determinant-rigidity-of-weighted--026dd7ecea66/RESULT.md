# Exact Cartesian \(L^2\) radius and determinant rigidity of weighted three-cycles

## Finding
For a three-dimensional cyclic weighted shift \(W\) over \(\mathbb C\), write \(We_0=ae_1\), \(We_1=be_2\), \(We_2=ce_0\), where \((a,b,c)\ne(0,0,0)\). Define
\[
S=|a|^2+|b|^2+|c|^2=\|W\|_{\mathrm F}^2,\qquad
\eta=\frac{3\sqrt3|abc|}{S^{3/2}}\in[0,1].
\]
The Cartesian \(L^2\) numerical radius introduced in [1] admits the exact formula
\[
\boxed{\displaystyle\omega_2(W)^2=\frac{2S}{3\pi}\int_0^{\pi/2}
\cos^2\!\left(\tfrac13\arccos(\eta\cos t)\right)\,dt.}
\]
At fixed \(S>0\), this expression is strictly increasing in \(\eta\). In particular, the pair \((\|W\|_{\mathrm F},\omega_2(W))\) determines \(|\det W|=|abc|\) uniquely; weights with the same Frobenius norm and determinant modulus have the same radius. The complete sharp range is
\[
\boxed{\displaystyle
\frac12\|W\|_{\mathrm F}\le\omega_2(W)\le
\sqrt{\frac16+\frac{\sqrt3}{4\pi}}\,\|W\|_{\mathrm F}.}
\]
Equality on the left holds exactly when \(abc=0\); equality on the right holds exactly when \(|a|=|b|=|c|>0\). Every value between these two endpoints is realized at fixed positive Frobenius norm. The theorem includes complex phases and zero weights.

## Assumptions and scope
Use the standard Hermitian inner product on \(\mathbb C^3\), its spectral norm, and the Frobenius norm. For every complex matrix \(T\), define the original source's invariant by
\[
\omega_2(T)^2=\frac1{2\pi}\int_0^{2\pi}
\left\|\tfrac12(e^{i\theta}T+e^{-i\theta}T^*)\right\|_{\mathrm{op}}^2\,d\theta.
\]
This integral coincides with the Cartesian definition in [1] by changing \(\theta\) to \(-\theta\). The displayed formula is only claimed for the specified weighted three-cycle, without invertibility or normality assumptions. At \(W=0\), both sides of the sharp bounds vanish, but \(\eta\) is left undefined.

## Proof
**1. Exact characteristic polynomial.** Set \(H_\theta=(e^{i\theta}W+e^{-i\theta}W^*)/2\), a trace-zero Hermitian matrix. Directly from the three nonzero directed edges,
\[
\operatorname{tr}(H_\theta^2)=\frac S2,\qquad
\det H_\theta=\frac14\operatorname{Re}(e^{3i\theta}abc).
\]
For a trace-zero Hermitian \(3\times3\) matrix, the characteristic polynomial is consequently
\[
\det(\lambda I-H_\theta)
=\lambda^3-\frac S4\lambda-
\frac14\operatorname{Re}(e^{3i\theta}abc).
\]
This equality can also be checked by expanding its six permutations. In particular its three roots are real.

**2. Spectral norm.** Put \(q_\theta=\operatorname{Re}(e^{3i\theta}abc)\). Replacing the sign of \(q_\theta\) by its opposite negates all roots of the polynomial, so their greatest absolute value depends only on \(|q_\theta|\). When \(q_\theta\ge0\), its largest positive root is also the largest root in modulus (the sum of all roots is zero, and the remaining two are nonpositive). Substituting \(\lambda=\sqrt{S/3}\cos u\) into the characteristic equation and using \(4\cos^3u-3\cos u=\cos3u\) yields
\[
\|H_\theta\|_{\mathrm{op}}
=\sqrt{\frac S3}\cos\!\left(\tfrac13\arccos\bigl(\eta|\cos(3\theta+\phi)|\bigr)\right),
\]
where \(\phi\) is an argument of \(abc\) if nonzero, and any real number otherwise. AM–GM gives \(0\le\eta\le1\), so all inverse cosines are defined. At \(|q_\theta|=0\), the expression gives \(\sqrt S/2\) and remains valid.

**3. Averaging and monotonicity.** The distribution of \(|\cos(3\theta+\phi)|\) under uniform \(\theta\in[0,2\pi]\) is that of \(\cos t\) with density \(2/\pi\) on \([0,\pi/2]\). Squaring and averaging the last display proves the asserted one-dimensional formula. The map \(u\mapsto\cos^2(\arccos(u)/3)\) is continuous and strictly increasing on \([0,1]\); since \(\cos t>0\) for \(0\le t<\pi/2\), the integral is strictly increasing in \(\eta\). Thus its value at fixed \(S\) reconstructs \(|abc|\) uniquely.

**4. Both exact endpoints and rigidity.** At \(\eta=0\), the integrand is \(\cos^2(\pi/6)=3/4\), giving \(\omega_2(W)^2=S/4\). At \(\eta=1\), \(\arccos(\cos t)=t\) for \(0\le t\le\pi/2\), and
\[
\frac{2S}{3\pi}\int_0^{\pi/2}\cos^2(t/3)\,dt
= S\left(\frac16+\frac{\sqrt3}{4\pi}\right).
\]
Strict monotonicity shows the lower endpoint requires \(|abc|=0\), and the upper endpoint requires \(\eta=1\). Equality in the AM–GM inequality for \(|a|^2,|b|^2,|c|^2\) occurs exactly at equal moduli; since \(S>0\), all are nonzero. This supplies both equality classifications. As \((|a|,|b|,|c|)\) travels continuously along the positive-octant sphere between a coordinate-axis point and its equal-coordinate point, \(\eta\) moves continuously from \(0\) to \(1\), so every radius in the stated range is realized.

## Verification
The reproducibility script `CHECK.py` constructs the matrices from several complex and zero-weight triples, evaluates the original operator-norm angular average directly by Hermitian eigenvalues, and compares it to the independent one-dimensional integral. It separately checks both endpoint constants and the characteristic polynomial. These finite numerical tests are only diagnostics: the four analytical steps above establish the statements for every complex triple, including boundary cases. Run `python3 CHECK.py` with NumPy and SciPy installed.

## Relationship to prior work
Audeh–Moradi–Sahoo [1] introduced \(\omega_2\) on general complex Hilbert spaces and proved generic estimates involving the usual numerical radius and Cartesian parts. Their relevant results and proofs were inspected; they do not determine the entire fixed-Frobenius range or its equality cases for arbitrary weighted three-cycles. Earlier cyclic-shift numerical-radius work concerns the **classical supremum numerical radius**, rather than the source's new angular-square-averaged invariant.

The determinant sensitivity is specific to the first genuinely nontrivial cyclic size for this average. Indeed, for a two-cycle \(V=\begin{psmallmatrix}0&b\\a&0\end{psmallmatrix}\), direct angular integration gives \(\omega_2(V)^2=(|a|^2+|b|^2)/4\), independent of the weight product. For a three-cycle the invariant instead distinguishes every admissible normalized value of \(|abc|\). This comparison motivates studying the first dimension in which such spectral geometry survives Cartesian averaging.

## Limitations
The theorem classifies the three-cycle family only. It does not give corresponding classifications for general \(3\times3\) matrices or cycles of length at least four, nor does it infer uniqueness of the weights from \(\omega_2\). Other triples with the same \(S\) and \(|abc|\) are genuinely indistinguishable by this invariant. The novelty comparison is based on accessible prior work and may miss an equivalent older integral-geometry treatment; independent validation and publication-priority certification were not performed.

## References
[1] Wasim Audeh, Hamid Reza Moradi, and Satyajit Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1, posted October 4, 2026, https://arxiv.org/abs/2610.04844.
[2] Shankhadeep Mondal, Ram Narayan Mohapatra, and Kasun Tharuka Dewage, *Refined upper bounds for the numerical radius via weighted operator means*, arXiv:2602.04134 (2026), https://arxiv.org/abs/2602.04134. This concerns bounds for the ordinary numerical radius, not the averaged invariant classified here.
