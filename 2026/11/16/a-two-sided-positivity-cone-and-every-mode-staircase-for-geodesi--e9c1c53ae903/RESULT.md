# A two-sided positivity cone and every-mode staircase for geodesic exponentials on \(\mathbb S^3\)

## Finding
Let \(\mathbb S^3\) be the round unit three-sphere, \(\theta(x,y)=\arccos\langle x,y\rangle\in[0,\pi]\), and let \(a>0\), \(b\in\mathbb R\). Consider the continuous, isotropic kernel
\[
K_{a,b}(x,y)=e^{-a\theta(x,y)}\bigl(1+b\cos(2\theta(x,y))\bigr).
\]
Set \(t=a^2\) and, for integers \(m\ge3\),
\[
R_m(t)=\frac{[t+(m-3)^2][t+(m+3)^2]}{t^2+(2m^2-6)t+m^4+6m^2-39},\qquad L(t)=\min_{m\ge3}R_m(t).
\]
The denominator is positive; \(0<L(t)<1\), and the minimum is attained. Define
\[
U(t)=\begin{cases}(t+16)/(8-t),&0<t<8,\\ +\infty,&t\ge8.\end{cases}
\]
Then **the exact positive-definiteness criterion on every finite subset** is
\[
\boxed{K_{a,b}\succeq0\text{ on }\mathbb S^3\quad\Longleftrightarrow\quad -L(a^2)\le b\le U(a^2).}
\]
The infinite minimization reduces to two adjacent explicit integers: letting
\[
\mu(t)=\sqrt{t+5+2\sqrt{(t+1)(t+4)}},
\]
one has
\[
\boxed{L(t)=\min\{R_{\lfloor\mu(t)\rfloor}(t),R_{\lceil\mu(t)\rceil}(t)\}.}
\]
As \(t\) grows from zero to infinity, the unique minimizing index visits every integer \(m=3,4,5,\ldots\) in order, with a nonempty parameter interval at each index. The sole transition from \(m\) to \(m+1\) occurs at the unique positive root \(\tau_m\) of
\[
\boxed{3t^2+(2m^2+2m+11)t-(m^4+2m^3-9m^2-10m+4)=0.}
\]
The transition parameters are strictly increasing. Only the two adjacent degrees tie at a transition; triple ties never occur. Furthermore,
\[
\frac{\mu(a^2)}a\longrightarrow\sqrt3,\qquad
\boxed{\lim_{a\to\infty}a^2(1-L(a^2))=3.}
\]
Every admissible kernel, including the two boundary branches, is **strictly positive definite** on finite sets of pairwise distinct points. It is \(C(\mathbb S^3)\)-universal if and only if all its inequalities are strict: \(b>-L(t)\) and, when \(t<8\), \(b<U(t)\). At the lower boundary exactly one or two finite spherical harmonic degrees are absent; at the finite upper boundary only degree zero is absent.

## Assumptions and scope
Positive definiteness means nonnegative quadratic forms for every finite configuration of points of the round unit sphere in \(\mathbb R^4\); strict positive definiteness excludes repeated points. The angle is **intrinsic geodesic distance**, not chordal distance. The parameters range over all \(a>0\) and real \(b\). The kernel is not normalized to unit diagonal; in the admissible region \(K_{a,b}(x,x)=1+b>0\), because \(L(t)<1\). Universality refers to uniform density of the reproducing-kernel Hilbert space in \(C(\mathbb S^3)\). No assertion is made for \(a=0\) or other sphere dimensions.

## Proof
**1. Exact Schoenberg coefficients.** On \(\mathbb S^3\), \(C_\ell^1(\cos\theta)=\sin((\ell+1)\theta)/\sin\theta\). The sign of the degree-\(\ell\) Gegenbauer coefficient is the sign of
\[
A_\ell=\int_0^\pi e^{-a\theta}(1+b\cos2\theta)\sin\theta\sin((\ell+1)\theta)\,d\theta.
\]
Write \(q=e^{-\pi a}\), \(I_k=a(1-(-1)^kq)/(t+k^2)\), and
\[
J_\ell=\frac{I_\ell-I_{\ell+2}}2
=\frac{2a(\ell+1)(1-(-1)^\ell q)}{(t+\ell^2)(t+(\ell+2)^2)}>0.
\]
The product-to-sum formula yields the exact identities
\[
A_0=J_0+\frac b2(J_2-J_0),\qquad
A_1=J_1+\frac b2J_3,\qquad
A_\ell=J_\ell+\frac b2(J_{\ell-2}+J_{\ell+2})\quad(\ell\ge2).
\]
Thus \(A_0/J_0=1+b(t-8)/(t+16)\) and \(A_1/J_1=1+b(t+1)/(t+25)\). For \(t<8\), degree zero imposes \(b\le U(t)\); at \(t=8\) it is positive for every \(b\); for \(t>8\) it only requires \(b\ge-(t+16)/(t-8)<-1\). Degree one requires \(b\ge-(t+25)/(t+1)<-1\).

**2. The sharp lower frontier.** For \(\ell\ge2\), write \(m=\ell+1\). The common parity factor \(1-(-1)^\ell q\) cancels, and elementary rational simplification gives
\[
\frac{2J_\ell}{J_{\ell-2}+J_{\ell+2}}=R_m(t)
=1+\frac{24(t+5-m^2)}{D_t(m^2)},\quad
D_t(y)=y^2+(2t+6)y+t^2-6t-39.
\]
For \(m\ge3\), \(D_t(m^2)>0\) since \(D_t(9)=t^2+12t+96>0\) and \(D_t\) increases for \(y\ge9\). Also \(R_m(t)>0\) from its factored numerator. Choose any integer with \(m^2>t+5\): then \(R_m(t)<1\), whereas \(R_m(t)\to1\) as \(m\to\infty\). Thus \(0<L(t)<1\), attained at a finite \(m\). All constraints of degrees zero and one that give *lower* bounds lie below \(-1\) and are automatically weaker than \(b\ge-L(t)>-1\). Hence Schoenberg's coefficient criterion proves the displayed necessary and sufficient two-sided region, including both boundaries. Outside the region an explicit degree has a negative coefficient.

**3. Unique continuous minimum and exactly two discrete candidates.** Treat \(y=m^2\ge9\) as a continuous variable. Differentiate the part of \(R\) that varies with \(y\):
\[
\frac{d}{dy}\frac{y-t-5}{D_t(y)}
=\frac{4(t+1)(t+4)-(y-t-5)^2}{D_t(y)^2}.
\]
Its two real zeros are \(y_\pm=t+5\pm2\sqrt{(t+1)(t+4)}\). The lower one satisfies \(y_-<1\) for every \(t>0\), while \(y_+>9\). The ratio on the left increases strictly until \(y_+\) and decreases strictly afterwards, so \(R\) decreases then increases, with its unique minimum at \(m=\mu(t)=\sqrt{y_+}\). Hence only \(\lfloor\mu(t)\rfloor\) and \(\lceil\mu(t)\rceil\) need comparison.

**4. Complete staircase and no skipping.** Exact subtraction gives
\[
R_{m+1}(t)-R_m(t)=\frac{24(2m+1)[C_m-(2m^2+2m+11)t-3t^2]}{D_t(m^2)D_t((m+1)^2)},
\]
where \(C_m=m^4+2m^3-9m^2-10m+4\). Writing \(m=3+u\) shows
\[
C_{3+u}=u^4+14u^3+63u^2+98u+28>0\quad(u\ge0).
\]
Consequently each adjacent comparison has a unique positive root \(\tau_m\), with \(R_m<R_{m+1}\) before that root and \(R_{m+1}<R_m\) after it. The continuously increasing \(\mu(t)\) ranges from \(3\) as \(t\downarrow0\) to infinity, and the switch satisfies \(m<\mu(\tau_m)<m+1\): at \(\mu=m\), \(R_m<R_{m+1}\), and at \(\mu=m+1\), the reverse holds, so the unique crossing lies strictly between. Because \(\mu\) increases, \(\tau_3<\tau_4<\cdots\); every index controls a nonempty interval, and no triple tie is possible. The positive root of the displayed quadratic is an exact radical formula when desired.

**5. Strong definiteness, universality, and asymptotics.** As \(m\to\infty\), \(R_m(t)\to1>L(t)\); hence for every admissible \(b\ge-L(t)\) all sufficiently large even and odd Schoenberg degrees have strictly positive coefficients. The classical two-parity strictness criterion on spheres of dimension at least two proves strict positive definiteness. By the compact-sphere spectral universality criterion, uniform density holds exactly when **every** degree is present; the equality cases above have precisely the finite missing degrees stated, while the interior has all coefficients positive. Finally \(\mu(t)^2=3t+10+O(t^{-1})\). At either nearest integer \(m=\sqrt{3t}+O(1)\),
\[
1-R_m(t)=\frac{24(m^2-t-5)}{D_t(m^2)}=\frac3t+O(t^{-3/2}),
\]
which proves the two limits.

## Verification
The standalone `checker.py` verifies five rational-polynomial identities with symbolic algebra, compares the explicit coefficients to independent numerical integration at multiple degrees and damping strengths, verifies the finite spectral constraints and active-index predictions for a broad deterministic parameter grid, and tests both sides of 33 consecutive mode transitions. It reports 8,831 passed checks. These experiments are supplementary; the global infinite-degree and all-parameter assertions follow from the proof above, including the strict endpoint inequalities.

## Relationship to prior work
Schoenberg's theorem and the strictness criterion provide general harmonic sign conditions, not this evaluated sharp parameter cone. Said, Da Costa, Steinert and Mostajeran give a broad harmonic characterization of universality of invariant kernels; the present special-function calculation supplies the complete parameter boundary and explicit spectral zeros for the stated two-parameter family. The earlier three-sphere damped-wave classification treats a *single* product \(e^{-a\theta}\cos(\omega\theta)\); it yields the sharp condition for a pure integer-frequency wave but does not imply the signed **sum** of unmodulated and doubled-frequency terms, its negative frontier, or the consecutive mode transitions. An earlier sharp cosine-modulated exponential result is for \(\mathbb S^2\) and first-frequency modulation, which does not entail these \(\mathbb S^3\) Gegenbauer coefficients. Related circle results use one-dimensional Fourier coefficients and likewise do not imply the three-sphere phase diagram.

## Limitations
The theorem concerns only the intrinsic unit three-sphere and the specified harmonic order. It neither classifies higher-harmonic multipliers nor treats general dimension. Priority is assessed against accessible sources, not established by absence of search matches; an older equivalent rational Gegenbauer-ratio optimization remains possible. Equality is spectral, and floating-point calculations are not proofs of exact equality. No independent external validation has been performed.

## References
1. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal **9** (1942), 96–108.
2. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, *Bernoulli* **19** (2013), 1327–1349, arXiv:1111.7077. https://arxiv.org/abs/1111.7077
3. D. Chen, V. A. Menegatto, X. Sun, *A necessary and sufficient condition for strictly positive definite functions on spheres*, *Proc. Amer. Math. Soc.* **131** (2003), 2733–2740.
4. S. Said, N. Da Costa, F. Steinert, C. Mostajeran, *Universality of kernels on Riemannian symmetric spaces*, arXiv:2608.00010 (public metadata dated 2026-06-19). https://arxiv.org/abs/2608.00010
5. *Sharp damping thresholds and a finite Schoenberg test for geodesic waves on the three-sphere*, published 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-damping-thresholds-and-a-finite-schoenberg-test-for-geodes--543d6b941b9f
6. *A two-frequency Schoenberg test for cosine-modulated geodesic exponentials on the two-sphere*, published 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-two-frequency-schoenberg-test-for-cosine-modulated-geodesic-ex--509c2a9eeeb8
