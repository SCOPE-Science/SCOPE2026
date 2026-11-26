# The parity-dependent cubic term in the sharp Fejér BV error

## Finding

On the circle of circumference \(2\pi\) with unnormalized arc length, let \(T_nf=K_n*f\), where
\[
K_n(t)=\frac{1}{2\pi n}\left(\frac{\sin(nt/2)}{\sin(t/2)}\right)^2,\qquad n\ge1.
\]
Define \(C_n=\sup_{0<|Df|(\mathbb T)<\infty}\|T_nf-f\|_1/|Df|(\mathbb T)\). For ordinary Fejér means the first correction to the sharp logarithmic law is cubic, has opposite signs in the two parities, and has no intervening inverse-square or inverse-fourth-order term:
\[
C_n=\frac{2}{\pi n}\bigl(\log(2n)+\gamma+1\bigr)
+\frac{1}{\pi n^3}
\begin{cases}-1/3,&n\ \mathrm{even},\\2/3,&n\ \mathrm{odd},\end{cases}
+O(n^{-5}).
\]
Here \(\gamma\) is Euler's constant. The stated contribution is the parity-resolved asymptotic with this remainder, not a new convolution norm principle, equality classification, or general parity-order law for arc deficits.

## Assumptions and scope

Functions are real periodic BV classes up to a.e. equality, with distributional variation including the seam. The density is extended by continuity and integrates to one; convolution and the output norm both use ordinary, unnormalized arc length. The remainder holds for integer \(n\to\infty\). This is the ordinary Fejér kernel (power two of the sine ratio), not its higher powers.

## Proof

**Sharp coefficient as a first moment.** The general circle-convolution first-moment identity is recorded in [1]. In this normalization, integrating the distributional derivative over a shorter arc and then using Tonelli gives \(\|f(\cdot-t)-f\|_1\le |t||Df|(\mathbb T)\) for \(|t|\le\pi\), so positivity and averaging give \(C_n\le2\int_0^\pi tK_n(t)\,dt\). For a semicircle indicator the translation error is exactly \(2|t|\) and the variation is 2. At each \(x\) the translation differences have the same sign as \(t\) varies (determined by whether \(x\) belongs to the semicircle), so averaging preserves the error integral. This proves equality for the purpose of evaluating the norm.

**Harmonic evaluation.** By the ordinary Fejér Fourier formula [3],
\[
2\int_0^\pi tK_n(t)\,dt
=\frac\pi2-\frac4\pi\sum_{\substack{1\le k<n\\ k\ \mathrm{odd}}}\frac{1-k/n}{k^2},
\]
since \(\int_0^\pi t\cos(kt)\,dt=((-1)^k-1)/k^2\). For \(m=\lfloor n/2\rfloor\) let \(S_m=\sum_{j=0}^{m-1}(2j+1)^{-1}\) and \(R_m=\sum_{j=m}^\infty(2j+1)^{-2}\). The exact integral is \(4(R_m+S_m/n)/\pi\). These finite-sum and moment identities are inputs to the expansion.

**Parity-resolved expansion.** From \(S_m=H_{2m}-H_m/2\) and \(R_m=\sum_{k>2m}k^{-2}-\tfrac14\sum_{k>m}k^{-2}\), Euler–Maclaurin gives
\[
S_m=\tfrac12\log(4m)+\tfrac12\gamma+\tfrac1{48m^2}+O(m^{-4}),\qquad
R_m=\tfrac1{4m}-\tfrac1{48m^3}+O(m^{-5}).
\]
In particular, writing \(b=2m\),
\[
\frac{\pi n}{2}C_n=\log(2b)+\gamma+\frac{n}{b}+
\frac1{6b^2}-\frac{n}{3b^3}+O(n^{-4}).
\]
For even \(n\), \(b=n\), giving \(\log(2n)+\gamma+1-1/(6n^2)+O(n^{-4})\). For odd \(n\), \(b=n-1\); writing \(x=1/n\), the difference from \(\log(2n)+\gamma+1\) is
\[
\log(1-x)+(1-x)^{-1}-1+\frac{x^2}{6(1-x)^2}-\frac{x^2}{3(1-x)^3}+O(x^4)
=\tfrac13 x^2+O(x^4).
\]
Here the linear and cubic coefficients in \(x\) both cancel. Multiplication by \(2/(\pi n)\) proves the expansion with the stated error.

## Relationship to other results and limitations

The exact first-moment reduction is contained in the universal probability-convolution lemma of [1], which also gives the triangular distance Fourier series. Its equality argument only uses positivity almost everywhere and hence applies to Fejér despite the isolated zeros. The powered Fejér–Jackson calculation of [2] gives closely analogous finite odd Fourier sums and a parity law for the flatness of the arc maximum, formally extending to power two by the same argument. These parts are not asserted as new here. The squared-Fejér case in [2] has an \(n^{-1}\) law, not the logarithmic ordinary Fejér law or its parity-separated cubic coefficients. Neither inspected result computes these coefficients for ordinary Fejér means; older equivalent Fourier or first-moment expansions may nevertheless exist. No priority ordering is inferred from shared dates.

The parity term gives the first signed finite-degree bias when the logarithmic approximation is used as a sharp uniform BV error budget. It does not assert that a corresponding expansion holds for higher powers, other norms or other normalizations.

## References

1. *Sharp circular BV drift–diffusion error and infinitely recurrent extrema*, Resultary record `67dcd0fce75c`, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-circular-bv-drift-diffusion-error-and-infinitely-recurrent--67dcd0fce75c/RESULT.md), proof Steps 1–3.
2. *Sharp BV approximation and parity-order rigidity for powered Fejér–Jackson kernels*, Resultary record `5321b930c41b`, [RESULT.md](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-bv-approximation-and-parity-order-rigidity-for-powered-fej--5321b930c41b/RESULT.md), Finding and Proof.
3. J. López-Bonilla, S. Vidal Beltrán and J. Yalja Montiel, *A note on Dirichlet and Fejér kernels*, Revista de Matemática: Teoría y Aplicaciones 14 (2007), 101–104, DOI [10.15517/rmta.v14i1.283](https://doi.org/10.15517/rmta.v14i1.283), pp. 102–103.
