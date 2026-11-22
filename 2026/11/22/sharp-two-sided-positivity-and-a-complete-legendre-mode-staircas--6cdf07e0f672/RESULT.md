# Sharp two-sided positivity and a complete Legendre-mode staircase for a geodesic covariance on the two-sphere

## Finding
Let \(\mathbb S^2\) be the unit sphere, let \(\theta(x,x')=\arccos(x\cdot x')\in[0,\pi]\), and let \(a>0\) and \(b\in\mathbb R\). Consider the geodesically isotropic kernel
\[
K_{a,b}(x,x')=e^{-a\theta(x,x')}\bigl(1+b\cos(2\theta(x,x'))\bigr).
\]
Set \(y=a^2\) and, for every integer \(n\ge0\),
\[
R_n(y)=1+\frac{6\{3n(n+1)-2y-8\}}{\{y+(n-2)^2\}\{y+(n+3)^2\}}.
\]
Define
\[
z_*(y)=\frac{2y+8+5\sqrt{(y+1)(y+4)}}3,\qquad
k(y)=\left\lfloor\frac{\sqrt{1+4z_*(y)}-1}{2}\right\rfloor,\qquad
H(y)=\max\{R_{k(y)}(y),R_{k(y)+1}(y)\}.
\]
Then \(k(y)\ge2\) and \(H(y)>1\). The **complete sharp positive-definiteness region** is
\[
\boxed{K_{a,b}\text{ is positive semidefinite on every finite subset of }\mathbb S^2
\quad\Longleftrightarrow\quad -H(a^2)^{-1}\le b\le U(a^2),}
\]
where
\[
U(y)=\begin{cases}(y+9)/(3-y),&0<y<3,\\ +\infty,&y\ge3.\end{cases}
\]
In particular the pure oscillatory factor \(e^{-a\theta}\cos(2\theta)\), without the unmodulated exponential baseline, is positive definite on the two-sphere **exactly when** \(a\ge\sqrt3\).

The negative boundary undergoes a complete no-skips spectral staircase. For each integer \(n\ge2\), let \(\beta_n\) be the unique positive zero of
\[
\boxed{7y^2+(4n^2+8n+35)y-3n^4-12n^3+n^2+26n+28=0,}
\]
and put \(\beta_1=0\). Then \(0=\beta_1<\beta_2<\beta_3<\cdots\), and every interval \(\beta_{n-1}<y<\beta_n\) has the unique active maximizing Legendre degree \(n\). Precisely two adjacent degrees \(n,n+1\) tie at \(y=\beta_n\); no degree is skipped and there are no triple ties. Every admissible kernel is strictly positive definite on finite sets of pairwise distinct sphere points. It is \(C(\mathbb S^2)\)-universal exactly when the lower inequality is strict and, for \(y<3\), the upper inequality is also strict. At the negative boundary one or two Legendre degrees vanish; at the finite positive boundary only degree zero vanishes.

The high-damping lower boundary has the asymptotic behavior
\[
H(a^2)=1+\frac{27}{10a^2}+O(a^{-4}),\qquad
-H(a^2)^{-1}=-1+\frac{27}{10a^2}+O(a^{-4}),
\]
with the active degree \(n=\sqrt{7/3}\,a+O(1)\). As \(a\downarrow0\), the lower boundary is \(-5a^2/12+O(a^4)\) and the upper boundary approaches \(3\).

## Assumptions and scope
The metric is intrinsic spherical distance, not chordal distance; the sphere is \(\mathbb S^2\) in \(\mathbb R^3\), not the three-sphere. Positive semidefiniteness is for every finite configuration, repetitions allowed. Strict positive definiteness refers to pairwise distinct points. Universality means that the reproducing-kernel Hilbert space is uniformly dense in the continuous functions on the sphere. The kernel is not normalized to unit diagonal; admissibility implies \(K_{a,b}(x,x)=1+b>0\). All \(a>0\) and real \(b\) are included, including both sharp equality branches. The case \(a=0\) is not asserted.

## Proof
**1. Baseline Legendre moments.** For \(n\ge0\), put
\[
I_n(a)=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\sin\theta\,d\theta,
\]
where \(P_n(1)=1\). Direct integration yields
\[
I_0=\frac{1+e^{-\pi a}}{a^2+1},\qquad I_1=\frac{1-e^{-\pi a}}{a^2+4}.
\]
The Legendre equation and derivative identity, integrated by parts, imply
\[
\frac{I_{n+2}}{I_n}=\frac{a^2+n^2}{a^2+(n+3)^2},\qquad n\ge0.
\]
For completeness, writing \(E_n=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\,d\theta\), the two integration-by-parts identities are
\[
a(E_{n-1}-E_{n+1})=(2n+1)I_n,
\qquad a\{nE_{n-1}+(n+1)E_{n+1}\}=(2n+1)\{a^2+n(n+1)\}I_n.
\]
For \(n\ge1\), elimination gives \(aE_{n+1}=(a^2+n^2)I_n\) and \(aE_{n-1}=(a^2+(n+1)^2)I_n\). Comparing consecutive indices establishes the stated recurrence for \(n\ge1\); the degree-zero instance follows from the direct \(I_2\) evaluation or the identity \(E_1=aI_0\). Hence \(I_n>0\) for every integer \(n\ge0\).

**2. Exact doubly modulated moments.** The three-term Legendre recurrence and \(\cos2\theta=2\cos^2\theta-1\) yield
\[
\cos2\theta\,P_n(\cos\theta)=A_nP_{n+2}(\cos\theta)+B_nP_n(\cos\theta)+C_nP_{n-2}(\cos\theta),
\]
where \(A_n=2(n+1)(n+2)/[(2n+1)(2n+3)]\), \(C_n=2n(n-1)/[(2n+1)(2n-1)]\), and
\[
B_n=2\left[\frac{(n+1)^2}{(2n+1)(2n+3)}+\frac{n^2}{(2n+1)(2n-1)}\right]-1.
\]
The terms having zero coefficients are omitted when \(n=0,1\). Substitution of the moment recurrence and exact simplification gives
\[
\frac{\int_0^\pi e^{-a\theta}\cos2\theta\,P_n(\cos\theta)\sin\theta\,d\theta}{I_n(a)}=R_n(a^2).
\]
The right side is valid for \(n=0\) and \(n=1\) as well, where it simplifies to
\[
R_0(y)=\frac{y-3}{y+9},\qquad R_1(y)=\frac{y+4}{y+16}>0.
\]
Consequently the \(n\)th Schoenberg/Legendre coefficient of \(K_{a,b}\) has the sign of \(I_n(a)[1+bR_n(y)]\). Since \(I_n>0\), Schoenberg's criterion reduces positive definiteness exactly to all inequalities \(1+bR_n(y)\ge0\).

**3. Minimum at degree zero and maximum at at most two adjacent degrees.** Write \(z=n(n+1)\) and extend the ratio to the continuous function
\[
\mathcal R_y(z)=1+\frac{6(3z-2y-8)}{(z+y-6)^2+25y},\qquad z\ge0.
\]
Its denominator is strictly positive. The numerator of \(\mathcal R_y'(z)\), after removal of a positive denominator and factor, is
\[
-3z^2+(4y+16)z+7y^2+31y+12.
\]
The roots are \([2y+8\pm5\sqrt{(y+1)(y+4)}]/3\); the negative-sign root is strictly negative and the positive-sign root is \(z_*(y)>6\). Thus \(\mathcal R_y\) increases strictly on \([0,z_*]\) and decreases strictly from \(z_*\) to its limit \(1\) at infinity. As \(\mathcal R_y(0)=R_0(y)<1\), degree zero is the unique global minimum. Since \(R_2(y)>1\) for small \(y\), but more generally \(R_n(y)>1\) for every integer satisfying \(3n(n+1)>2y+8\), the discrete maximum \(H(y)>1\) is attained. The two adjacent integers \(k(y),k(y)+1\) whose triangular numbers bracket \(z_*(y)\) are the only possible maximizers. They are both at least two, because \(z_*(y)>6\).

For negative \(b\), the constraining inequality is the maximum \(H\): \(b\ge-1/H\). For positive \(b\), only negative \(R_n\) constrain the sign, and since the unique minimum is \(R_0=(y-3)/(y+9)\), a finite upper bound exists exactly when \(y<3\) and is \(-1/R_0=(y+9)/(3-y)\). This proves the complete parameter region and explains the qualitative transition for the pure doubly modulated exponential. Outside either boundary, a degree with negative Schoenberg coefficient supplies a direct obstruction.

**4. Full active-degree staircase.** Let
\[
P_n(y)=7y^2+(4n^2+8n+35)y-3n^4-12n^3+n^2+26n+28.
\]
The exact rational identity
\[
R_n(y)-R_{n+1}(y)=
-\frac{12(n+1)P_n(y)}{
\{y+(n-2)^2\}\{y+(n+3)^2\}\{y+(n-1)^2\}\{y+(n+4)^2\}}
\]
holds for every integer \(n\ge2\). Its denominator is positive for \(y>0\), while \(P_n\) is strictly increasing on positive \(y\), and
\[
-P_{u+2}(0)=3u^4+36u^3+143u^2+210u+60>0\qquad(u\ge0).
\]
Thus every adjacent pair has a unique positive tie \(\beta_n\); below it \(R_n>R_{n+1}\) and above it \(R_{n+1}>R_n\). At a tie, unimodality of \(\mathcal R_y\) forces \(n(n+1)<z_*(\beta_n)<(n+1)(n+2)\), so the tied pair are the global maximum candidates, with no third tie. Since \(z_*(y)\) increases strictly and unboundedly in \(y\), the tie locations increase strictly with \(n\), cover every adjacent transition, and diverge to infinity. At \(y\downarrow0\), the unique maximum is degree two; the adjacent-tie ordering implies that each degree \(n\ge2\) controls exactly \((\beta_{n-1},\beta_n)\). This proves the no-skips staircase.

**5. Strictness and universality.** At the lower boundary, precisely the maximizing one or two finite degrees have zero Schoenberg coefficients, while for sufficiently large degrees all coefficients are positive because \(R_n(y)\to1<H(y)\). At the finite upper boundary, the only zero coefficient occurs at degree zero because \(R_0\) is the unique minimum. On the strict interior all coefficients are positive. Hence every admissible kernel has positive coefficients in infinitely many even and infinitely many odd degrees, and the Chen–Menegatto–Sun criterion proves strict positive definiteness on every distinct finite configuration. The compact-sphere spectral universality criterion implies uniform density exactly when every degree has strictly positive coefficient, proving the claim at every endpoint. At the lower boundary, \(b=-1/H>-1\), so the diagonal is positive.

**6. Asymptotic endpoints.** As \(y\to\infty\), \(z_*(y)=7y/3+O(1)\), and the maximizing integer obeys \(n=\sqrt{7y/3}+O(1)\). At the continuous maximum, \(y\,[\mathcal R_y(z_*)-1]\to27/10\); an adjacent-integer displacement changes the profile by \(O(y^{-2})\), giving \(H(y)=1+27/(10y)+O(y^{-2})\). As \(y\downarrow0\), degree two controls and \(R_2(y)=12/(5y)+O(1)\), giving the claimed lower-bound expansion and \(U(y)\to3\).

## Verification
The standalone `checker.py` uses exact symbolic identities for the moment-ratio formulas, continuous derivative, adjacent-crossing polynomial, and leading asymptotic. High-precision numerical quadrature independently tests a range of Legendre coefficients, boundary signs, and candidate maximizers; it also checks the first sixty adjacent switches. The executed checker passed 767 supplementary assertions. These finite tests are not an infinite-degree proof: the analytic sign, monotonicity, and interpolation arguments above establish the complete all-parameter result. Run `python checker.py` in an environment satisfying `requirements.txt`.

## Relationship to prior work
Schoenberg's harmonic criterion and the Chen–Menegatto–Sun strictness theorem supply the general test. Gneiting's study of positive-definite geodesic powered exponentials gives the unmodulated baseline but not the signed second-cosine sharp parameter cone. Said, Da Costa, Steinert and Mostajeran establish the general link between spherical spectral support and kernel universality, including spherical examples; the specific parameter classification and no-skips Legendre staircase are not stated in the material inspected.

Published neighboring explicit classifications were compared at the level of implications. The two-sphere first-cosine classification treats \(e^{-a\theta}(1+b\cos\theta)\), which shifts different Legendre degrees and has a different one-sided parameter cone. The second-cosine classification on the circle is one-dimensional and yields only a lower parameter boundary, not the upper two-sphere boundary. The corresponding three-sphere second-cosine classification has upper boundary \((a^2+16)/(8-a^2)\) for \(a^2<8\), whereas here it is \((a^2+9)/(3-a^2)\) for \(a^2<3\). For instance, \(a=1,b=3\) satisfies the two-sphere criterion but violates the three-sphere upper bound \(17/7\); restricting a positive-definite three-sphere kernel to a two-sphere therefore does not supply the converse needed for this result. This distinction is geometric, not a new notation for an already derived three-sphere formula.

## Limitations
This is an exact result only for the stated two-sphere geodesic second-harmonic family, not arbitrary angular modulations, higher spherical dimensions, or kernels with an unnormalized distance scale. Although the analytic derivation is complete, bibliographic priority is assessed against accessible material, and an equivalent result in unindexed older literature remains possible. No independent audit or independent validation has been performed. The finite checker provides supplementary verification, not a substitute for the proof.

## References
1. S. Said, N. Da Costa, F. Steinert and C. Mostajeran, *Universality of kernels on Riemannian symmetric spaces*, arXiv:2608.00010, first public version 2026-06-19, https://arxiv.org/abs/2608.00010.
2. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, first public version 2011-11-30; *Bernoulli* 19 (2013), 1327–1349, https://arxiv.org/abs/1111.7077.
3. I. J. Schoenberg, *Positive definite functions on spheres*, *Duke Math. J.* 9 (1942), 96–108.
4. D. Chen, V. A. Menegatto and X. Sun, *A necessary and sufficient condition for strictly positive definite functions on spheres*, *Proc. Amer. Math. Soc.* 131 (2003), 2733–2740.
5. *A two-frequency Schoenberg test for cosine-modulated geodesic exponentials on the two-sphere* (public mathematical result, 2026-10-26), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-two-frequency-schoenberg-test-for-cosine-modulated-geodesic-ex--509c2a9eeeb8/RESULT.md.
6. *A two-sided positivity cone and every-mode staircase for geodesic exponentials on the three-sphere* (public mathematical result, 2026-11-16), https://github.com/published-finding corpus/2026/blob/main/2026/11/16/SCOPE-a-two-sided-positivity-cone-and-every-mode-staircase-for-geodesi--e9c1c53ae903/RESULT.md.
7. *Exact every-mode staircase for even-harmonic geodesic-exponential circle covariances* (public mathematical result, 2026-11-16), https://github.com/published-finding corpus/2026/blob/main/2026/11/16/SCOPE-exact-every-mode-staircase-for-even-harmonic-geodesic-exponentia--027cc81ac50f/RESULT.md.
