# A logarithmic first-negative-frequency frontier for the circular geodesic Gaussian

## Finding
For every \(t>0\), let the intrinsic-distance Gaussian on the unit circle be \(G_t(\theta)=\exp(-t\theta^2)\) for \(-\pi\le\theta\le\pi\), extended with period \(2\pi\). Define its real Fourier coefficients by
\[
a_t(n)=\frac1\pi\int_0^\pi e^{-t x^2}\cos(nx)\,dx,\qquad n=0,1,2,\ldots.
\]
Every odd coefficient is **strictly positive for every bandwidth**. For even coefficients at large bandwidth, define
\[
B(t)=2\pi t+\frac{\log t}{2\pi}+\frac{\log(2\pi^{3/2})}\pi.
\]
There are constants \(T,C>0\), independent of indices, such that whenever \(t\ge T\), every even \(n\ge0\) satisfies
\[
\begin{aligned}
n\le B(t)-C\frac{(\log t)^2}t&\implies a_t(n)>0,\\
n\ge B(t)+C\frac{(\log t)^2}t&\implies a_t(n)<0.
\end{aligned}
\]
In particular the first negative index \(n_-(t)=\min\{n\ge0:a_t(n)<0\}\) exists and is even; for \(t\ge T\),
\[
-C\frac{(\log t)^2}t\le n_-(t)-B(t)\le 2+C\frac{(\log t)^2}t.
\]
The width two reflects the even-frequency lattice; no exact rounding assertion is made when \(B(t)\) lies in the shrinking transition strip.

## Assumptions and scope
The metric is intrinsic arc distance on a circle of circumference \(2\pi\), **not** Euclidean chord distance and **not** graph distance on a finite cyclic sample. The parameter \(t\) is strictly positive and the frequency index is a nonnegative integer. Fourier coefficients are normalized using \(d\theta/(2\pi)\) over the full circle. The sign-frontier estimates apply as \(t\to\infty\); the odd-frequency positivity holds without a large-\(t\) assumption. Constants are absolute but not optimized.

## Proof
**1. Exact Gaussian-versus-antipodal identity.** The half-line Gaussian cosine integral gives
\[
\frac1\pi\int_0^\infty e^{-t x^2}\cos(nx)\,dx
=\frac{e^{-n^2/(4t)}}{2\sqrt{\pi t}}.
\]
In the omitted integral substitute \(x=\pi+v/t\). Since \(n\) is an integer, \(\cos(n\pi+nv/t)=(-1)^n\cos(nv/t)\). Define
\[
J_t(q)=\int_0^\infty e^{-2\pi v-v^2/t}\cos(qv)\,dv.
\]
Then the **exact identity**, with all normalizations included, is
\[
a_t(n)=\frac{e^{-n^2/(4t)}}{2\sqrt{\pi t}}
-\frac{(-1)^n e^{-\pi^2t}}{\pi t}J_t(n/t).\tag{1}
\]

**2. Strict positivity of the antipodal factor.** Extend the integrand evenly to the whole line. The Fourier transforms of \(v\mapsto e^{-2\pi|v|}\) and \(v\mapsto e^{-v^2/t}\) are, respectively, \(4\pi/(4\pi^2+q^2)\) and \(\sqrt{\pi t}e^{-tq^2/4}\). Both are strictly positive. The Fourier transform of their product is a convolution of those strictly positive integrable functions and is strictly positive at every real frequency. It is twice \(J_t(q)\), hence \(J_t(q)>0\) for every \(t>0\), \(q\in\mathbb R\). Equation (1) immediately proves \(a_t(n)>0\) for every odd \(n\). Also \(a_t(0)>0\) directly from its defining integral.

**3. Uniform rational approximation of the antipodal factor.** Set \(a=2\pi\) and \(h_t(v)=e^{-av}(e^{-v^2/t}-1)\) for \(v\ge0\). For every \(t\ge1\), direct differentiation, \(|1-e^{-v^2/t}|\le v^2/t\), and \(|(e^{-v^2/t})'|\le2v/t\) give
\[
\|h_t\|_{L^1(0,\infty)}+\|h_t''\|_{L^1(0,\infty)}\le C_0/t
\]
for an absolute constant \(C_0\). Note that \(h_t(0)=h_t'(0)=0\) and that the function and derivatives decay at infinity. For \(|q|\le1\), use the first norm, and for \(|q|\ge1\) integrate by parts twice and use the second. Thus uniformly in real \(q\),
\[
J_t(q)=\frac{a}{a^2+q^2}+O\!\left(\frac1{t(1+q^2)}\right)
=\frac{a}{a^2+q^2}\left(1+O(t^{-1})\right).\tag{2}
\]
The relative error in (2) is uniform across the **entire** real frequency axis, not merely frequencies of bounded size.

**4. The global even-frequency sign frontier.** Because \(J_t(q)>0\), (1) shows that for even \(n\) the sign of \(a_t(n)\) is that of \(R_t(n)-1\), where
\[
R_t(n)=\frac{\sqrt{\pi t}}{2J_t(n/t)}\exp\!\left(\pi^2t-\frac{n^2}{4t}\right).
\]
By (2), uniformly for all real \(n\ge0\),
\[
\log R_t(n)=F_t(n)+O(t^{-1}),\quad
F_t(n)=\pi^2t-\frac{n^2}{4t}+
\log\!\left(\frac{\sqrt{\pi t}(4\pi^2+n^2/t^2)}{4\pi}\right).\tag{3}
\]
Its derivative is
\[
F_t'(n)=\frac nt\left[-\frac12+\frac{2}{t(4\pi^2+n^2/t^2)}\right]<0
\]
for all \(n>0\) and sufficiently large \(t\), while \(F_t(0)>0\) and \(F_t(n)\to-\infty\) as \(n\to\infty\). Hence \(F_t\) has exactly one positive root \(\nu_t\).

Writing \(n=2\pi t+\Delta\) with \(\Delta=O(\log t)\) gives, uniformly in that range,
\[
F_t(2\pi t+\Delta)
=-\pi\Delta+\tfrac12\log t+\log(2\pi^{3/2})
+O\!\left(\frac{(\log t)^2}t\right).
\]
The intermediate value theorem and the strict slope \(F_t'(\nu_t)=-\pi+o(1)\) imply
\[
\nu_t=B(t)+O\!\left(\frac{(\log t)^2}t\right).\tag{4}
\]
Because (3) is uniform in **all** indices, and \(F_t\) is decreasing with slope bounded away from zero near its unique root, it has the sign of \(\nu_t-n\) whenever \(|n-\nu_t|\ge C_1/t\), with a fixed sufficiently large \(C_1\). Away from a fixed neighborhood of the root, monotonicity only strengthens the sign margin. Combining this conclusion with (4) proves both global even-index implications. Finally, all even integers below the lower threshold are positive, all beyond the upper threshold are negative, and consecutive even integers are separated by two units. This proves the bounds for the least negative index. \(\square\)

## Verification
The standalone Python program `verify.py` uses high-precision quadrature on the exact integral identity, checks the Gaussian-versus-tail representation at selected parameters, tests odd-frequency positivity at multiple bandwidths, checks the predicted consecutive even sign pairs, and compares the uniform rational approximation of \(J_t\) at several frequencies. It passed 81 finite diagnostics. These finite diagnostics are **not** a proof of the quantified infinite-index assertions; the latter follow from steps 1--4.

## Relationship to prior work
Da Costa, Mostajeran and Ortega (first public preprint 2023-02-21) prove that an intrinsic geodesic Gaussian is not positive definite on the circle at any fixed bandwidth. Their Section 4 uses alternating eigenvalues of **finite sampled circulants** and partial theta estimates; it does not locate the first negative coefficient of the continuous Fourier series or classify all odd modes. Two later mathematical notes treat the **finite-cycle** last-indefiniteness scale and, for sample sizes divisible by four, a Nyquist logarithmic window. The finite cyclic Fourier eigenvalues sum **aliased** continuum coefficients; in particular their logarithmic window does not imply the present continuum sign constant, the all-odd positivity assertion, or the two-unit localization of the first negative continuum index. Both problems have a logarithmic balance mechanism, which is not independently claimed novel here. Wood (1995) studies general criteria for truncated line covariances to be circle covariances, not a known exact two-parameter first-frequency law. Historical priority is conditional on accessible comparisons; no uniqueness of discovery or independent validation is claimed.

## Limitations
The theorem does not identify the exact integer first-negative frequency inside the vanishing-width ambiguous transition strip, and it does not supply a closed-form finite-bandwidth sign table for even modes. The uniform proof is asymptotic in bandwidth; it supplies no explicit smallest admissible \(T\). A plausible older source on truncated covariance functions was available only by abstract, not by its complete text, leaving a concrete bibliographic priority risk. Numerical checks do not certify infinite frequency families.

## References
1. N. Da Costa, C. Mostajeran and J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623v1 (first public 2023-02-21), https://arxiv.org/abs/2302.10623.
2. *The sharp \(\pi/N\) Gaussian covariance transition on discrete circles*, publicly available mathematical note (2026-10-25), public record: 2026-10-25, exact title above.
3. *A sharp \(\pi/n\) last-failure scale for geodesic Gaussian matrices on finite cycles*, publicly available mathematical note (2026-11-01), public record: 2026-11-01, exact title above.
4. A. T. A. Wood, *When is a truncated covariance function on the line a covariance function on the circle?*, Statistics & Probability Letters 24 (1995), 157--164, https://doi.org/10.1016/0167-7152(94)00162-2.
