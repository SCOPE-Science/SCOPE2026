# Uniform finite-moment convergence of typical Bohnenblust–Hille ratios
## Finding
For every fixed finite real \(s\ge 1\), consider the full complex coefficient sphere for \(m\)-homogeneous polynomials in \(n\ge2\) variables. Put
\[
N_{m,n}=\binom{m+n-1}{m},\qquad H_{m,n}=\frac{n-1}{2}\log\!\left(m+\frac{m^2}{n}\right),
\]
and let \(R_m\) be the Bohnenblust–Hille ratio. With
\[
Y_{m,n}=\frac{\sqrt{H_{m,n}}}{N_{m,n}^{1/(2m)}}R_m,
\]
one has
\[
\sup_{n\ge2}\int_{\mathbb S_{m,n}}|Y_{m,n}-1|^s\,d\mu_{m,n}\longrightarrow0
\]
as \(m\to\infty\). Hence every fixed finite moment converges uniformly:
\[
\sup_{n\ge2}\left|\int_{\mathbb S_{m,n}}Y_{m,n}^s\,d\mu_{m,n}-1\right|\longrightarrow0.
\]
In particular,
\[
\int_{\mathbb S_{m,n}}R_m\,d\mu_{m,n}
=(1+o(1))\frac{N_{m,n}^{1/(2m)}}{\sqrt{H_{m,n}}},
\]
uniformly in \(n\ge2\).

## Assumptions and scope
The scalar field is complex. The coefficient support is the full set of monomials of total degree \(m\), and \(\mu_{m,n}\) is normalized Euclidean surface measure on the coefficient sphere. The exponent \(s\) is fixed and finite, with \(s\ge1\). No assertion is made for moments whose order grows with \(m\), for exponential moments, or for the real coefficient model.

## Proof
Write \(q_m=2m/(m+1)\). Under standard complex Gaussian coefficients \(g\), arXiv:2609.31779v1 writes
\[
Y_{m,n}=\frac UV,
\qquad
U=\frac{\|g\|_{q_m}}{N_{m,n}^{1/q_m}},
\qquad
V=\frac{\|G\|_\infty}{\sqrt{N_{m,n}H_{m,n}}}.
\]
Its equation (6.19) gives, uniformly in \(n\), exponential concentration of \(U\) about \(\Gamma(1+q_m/2)^{1/q_m}\), and this center tends to \(1\). Proposition 6.5 gives
\[
\sup_{n\ge2}\left|\mathbb E V-1\right|\longrightarrow0
\]
and Gaussian concentration
\[
\mathbb P\{|V-\mathbb EV|>\varepsilon\}\le2e^{-\varepsilon^2H_{m,n}}.
\]
Therefore, for each fixed \(0<\delta<1/4\), all sufficiently large \(m\) satisfy, uniformly in \(n\ge2\),
\[
\mathbb P\{|U-1|>\delta\}\le2e^{-c_\delta N_{m,n}},
\qquad
\mathbb P\{|V-1|>\delta\}\le2e^{-c'_\delta H_{m,n}}.
\]
On their complementary event, \(|U/V-1|\le 2\delta/(1-\delta)\).

For the bad event one needs a uniform integrable envelope. Lemma 3.1 of the same paper gives \(R_m\le N_{m,n}^{1/(2m)}\), hence deterministically
\[
0\le Y_{m,n}\le\sqrt{H_{m,n}}.
\]
The paper also records
\[
N_{m,n}\ge\frac{n(m+1)}2,
\qquad
H_{m,n}\le n\log m,
\qquad
\frac{N_{m,n}}{H_{m,n}}\ge\frac{m+1}{2\log m}\longrightarrow\infty,
\]
while \(H_{m,n}\to\infty\) uniformly in \(n\ge2\). Consequently
\[
\sup_{n\ge2}(1+\sqrt{H_{m,n}})^s
\left(e^{-c_\delta N_{m,n}}+e^{-c'_\delta H_{m,n}}\right)\longrightarrow0.
\]
It follows that
\[
\limsup_{m\to\infty}\sup_{n\ge2}\mathbb E|Y_{m,n}-1|^s
\le\left(\frac{2\delta}{1-\delta}\right)^s.
\]
Letting \(\delta\downarrow0\) proves the uniform \(L^s\) convergence under Gaussian coefficients. Because \(Y_{m,n}\) is homogeneous of degree zero, radial-angular independence gives exactly the same distribution on the coefficient sphere, so the same \(L^s\) conclusion holds for \(\mu_{m,n}\).

Finally, \(L^s\)-convergence to the constant \(1\) implies convergence of the \(s\)-th moments; for \(s=1\) it gives the asserted expectation asymptotic directly.

## Verification
The proof uses only statements verified in arXiv:2609.31779v1: Theorem C(i), Lemma 3.1, Proposition 6.5, equation (6.19), the radial Gaussian/spherical identity, and the displayed comparison \(N_{m,n}/H_{m,n}\to\infty\) uniformly. The argument was checked at the endpoint \(n=2\), where \(H_{m,2}\) has only logarithmic growth, because this is the slowest decay regime for the denominator concentration. The polynomial envelope \((1+\sqrt H)^s\) is still dominated by \(e^{-cH}\) for every fixed finite \(s\).

## Relationship to prior work
Pellegrino and Teixeira prove in Theorem C(i) of arXiv:2609.31779v1 that \(Y_{m,n}\to1\) in spherical measure uniformly in \(n\), and they prove a lower-deviation large-deviation rate. The paper does not state convergence in \(L^s\), uniform integrability of the normalized ratios, convergence of their finite moments, or the corresponding expectation asymptotic. Those conclusions do not follow from convergence in measure alone; the quantitative Gaussian tails and deterministic envelope are both used here.

The classical hypercontractive Bohnenblust–Hille theorem of Defant, Frerick, Ortega-Cerdà, Ounaïes and Seip concerns extremal constants and not the spherical distribution or finite moments of the normalized ratio. Targeted searches for expected Bohnenblust–Hille ratios, moment convergence, uniform integrability, and spherical coefficient models did not reveal a statement implying the result above.

## Limitations
The finding is a finite-moment strengthening of a very recent preprint. It does not identify rates optimized in \(s\), does not treat \(s\) growing with \(m\), and does not establish exponential integrability. An equivalent observation could exist under probabilistic language not indexed by Bohnenblust–Hille terminology; this is the principal residual originality risk.

## References
1. Daniel M. Pellegrino and Eduardo V. Teixeira, *Typical Bohnenblust–Hille Ratios*, arXiv:2609.31779v1, first public 2026-09-24.
2. Andreas Defant, Leonhard Frerick, Joaquim Ortega-Cerdà, Myriam Ounaïes and Kristian Seip, *The Bohnenblust–Hille inequality for homogeneous polynomials is hypercontractive*, Annals of Mathematics 174 (2011), 485–497.
