# Exact every-mode staircase for even-harmonic geodesic-exponential circle covariances

## Finding
On the unit circle, write \(\theta(z,w)\in[0,\pi]\) for the shortest-arc distance. For \(a>0\) and real \(b\), define
\[
K_{a,b}(z,w)=e^{-a\theta(z,w)}\bigl(1+b\cos(2\theta(z,w))\bigr).
\]
For \(t>0\) and integers \(n\ge2\), put
\[
R_n(t)=\frac{[t+(n-2)^2][t+(n+2)^2]}{(t+n^2)(t+n^2+4)},\qquad
r(t)=\min_{n\ge2}R_n(t).
\]
Then \(0<r(t)<1\) and **the exact positive-definiteness classification** is
\[
\boxed{K_{a,b}\text{ is positive semidefinite on every finite circle configuration}\quad\Longleftrightarrow\quad b\ge-r(a^2).}
\]
The minimum is attained at one of the two integers surrounding
\[
q(t)=\sqrt{\frac{t+4+4\sqrt{(t+1)(t+4)}}3},
\]
so infinitely many Fourier inequalities reduce to at most two explicit rational evaluations.

More precisely, for every integer \(n\ge2\) there is a **single exact transition parameter** \(t_n>0\):
\[
\boxed{5t_n^2+(2n^2+2n+25)t_n-3n^4-6n^3+5n^2+8n+20=0.}
\]
The numbers \(t_2<t_3<t_4<\cdots\) strictly increase to infinity. With \(t_1=0\), the unique minimizing nonnegative Fourier frequency is \(n\) throughout \(t_{n-1}<t<t_n\). At \(t=t_n\) exactly the adjacent frequencies \(n,n+1\) tie; **no frequency is ever skipped**. At the covariance boundary \(b=-r(t)\), the Fourier coefficients vanish at precisely \(\pm n\), or precisely \(\pm n,\pm(n+1)\) at a transition, yet the kernel remains strictly positive definite for every finite set of pairwise distinct circle sites.

The first transitions are \(t_2=0.957252408878\ldots\) and \(t_3=4.438629449764\ldots\). The cutoff obeys
\[
r(a^2)=\frac{a^2}{2}+O(a^4)\quad(a\downarrow0),\qquad
r(a^2)=1-\frac9{4a^2}+O(a^{-4})\quad(a\to\infty),
\]
while the active frequency is \(\sqrt{5/3}\,a+O(1)\) at large damping.

## Assumptions and scope
The circle has circumference \(2\pi\) and the angular distance is normalized to \([0,\pi]\). The kernel is real, continuous, stationary, and isotropic in that distance. Positive semidefinite means every finite Hermitian Gram matrix is positive semidefinite, including repeated sites; strict positive definiteness refers to pairwise distinct sites. All parameters \(a>0\), \(b\in\mathbb R\) are included, and boundary equality is permitted. The result is specifically about the second angular harmonic, not all harmonic indices, chordal distance, or higher spheres. The natural correlation normalization divides by \(1+b>0\) in the admissible region.

## Proof
**1. Fourier coefficients and exact admissibility.** Write \(f_a(x)=e^{-a|x|}\) on \([ -\pi,\pi]\), periodically extended. For every integer \(n\), its normalized complex Fourier coefficient is
\[
c_n(a)=\frac1{2\pi}\int_{-\pi}^{\pi}f_a(x)e^{-inx}\,dx
=\frac{a[1-(-1)^ne^{-\pi a}]}{\pi(a^2+n^2)}>0.
\]
Multiplication by \(1+b\cos(2x)\) gives
\[
d_n(a,b)=c_n(a)+\frac b2\{c_{n-2}(a)+c_{n+2}(a)\}.
\]
The three indices have the same parity; consequently, the exponential parity factors cancel in their ratio. Setting \(t=a^2\), direct substitution gives \(2c_n/(c_{n-2}+c_{n+2})=R_{|n|}(t)\), for \(n\ne0\), and the formulas also hold at \(n=0\) when \(R_0(t)=(t+4)/t\). In particular,
\[
R_0(t)=\frac{t+4}{t}>1,\qquad R_1(t)=\frac{t+9}{t+5}>1.
\]
For sufficiently large \(n\), however, \(R_n(t)<1\) by the identity
\[
R_n(t)=1+\frac{4(t+4-3n^2)}{(t+n^2)(t+n^2+4)}.
\]
Thus the global threshold ratio \(r(t)\) lies strictly between zero and one, is achieved among positive integers \(n\ge2\), and neither frequency zero nor one is limiting. The circle Fourier/Herglotz criterion states that the continuous kernel is positive semidefinite exactly when all \(d_n\ge0\). Since \(c_n>0\), this is equivalent to \(1+b/R_{|n|}(t)\ge0\) for every \(n\), and hence exactly to \(b\ge-r(t)\), including the entire positive-\(b\) half-line.

**2. Two-candidate principle.** For real \(y\ge0\), define
\[
Q_t(y)=1+\frac{4(t+4-3y)}{(t+y)(t+y+4)}.
\]
Its derivative has denominator \((t+y)^2(t+y+4)^2>0\) and numerator
\[
4\bigl[3y^2-(2t+8)y-(5t^2+24t+16)\bigr].
\]
The quadratic has exactly one positive root
\[
y_*(t)=\frac{t+4+4\sqrt{(t+1)(t+4)}}3.
\]
Therefore \(Q_t\) decreases strictly up to \(y_*(t)\) and then increases strictly. Its integer-square minimum must occur among \(\lfloor\sqrt{y_*(t)}\rfloor\) and \(\lceil\sqrt{y_*(t)}\rceil\), both at least two because \(y_*(t)>4\). This proves the finite cutoff formula.

**3. Every adjacent crossing and the exhaustive phase diagram.** Exact rational subtraction yields, for \(n\ge2\),
\[
R_n(t)-R_{n+1}(t)=
\frac{4(2n+1)P_n(t)}{(t+n^2)(t+n^2+4)(t+(n+1)^2)(t+(n+1)^2+4)},
\]
where
\[
P_n(t)=5t^2+(2n^2+2n+25)t-3n^4-6n^3+5n^2+8n+20.
\]
For \(n\ge2\), \(P_n(0)<0\), while \(P_n\) strictly increases on \([0,\infty)\) to infinity. Hence it has exactly one positive root \(t_n\), with \(R_n<R_{n+1}\) below it and \(R_n>R_{n+1}\) above it. If \(R_n=R_{n+1}\), unimodality of \(Q_t\) forces its unique minimizer to satisfy \(n^2<y_*(t)<(n+1)^2\), so the tied pair is the unique integer-square minimizing pair, and no other mode ties. The function \(y_*(t)\) increases continuously and strictly from \(4\) to infinity. As the adjacent minimizing intervals move to the right, the transition parameters satisfy \(0<t_2<t_3<\cdots\), with \(t_n\to\infty\). At \(t=0\) (used only as a comparison limit) the ratio at frequency two is zero and all others are positive. Continuity, the strict adjacent crossing orientation, and the two-candidate principle therefore show that \(n\) is the unique minimizer for \(t_{n-1}<t<t_n\), and exactly \(n,n+1\) minimize at \(t_n\), with no skipped frequencies or triple ties.

**4. Strictness and the spectral notch.** At \(b=-r(t)\), the coefficients \(d_n\) are zero exactly when \(|n|\) achieves the threshold minimum; hence there are exactly two zero coefficients, except for the four at crossing values. Every other coefficient, in particular all sufficiently large positive and negative frequencies, is positive. If the Gram quadratic form vanished for pairwise distinct points \(z_1,\dots,z_N\) and complex coefficients \(u_j\), the absolutely convergent Fourier expansion would imply \(\sum_{j=1}^N u_jz_j^k=0\) for all sufficiently large consecutive integers \(k\). The Vandermonde determinant of any \(N\) such consecutive powers is nonzero, implying \(u_j=0\) for all \(j\). Thus the boundary kernel remains strictly positive definite. Off the boundary in the admissible region all Fourier coefficients are strictly positive. In particular the boundary has a finite, exactly classified spectral hole even though it is strictly positive definite on distinct sites.

**5. Asymptotics.** As \(t\downarrow0\), the first branch is \(R_2(t)=t(t+16)/[(t+4)(t+8)]=t/2+O(t^2)\), yielding the small-\(a\) expansion. As \(t\to\infty\), the continuous minimizing square is \(y_*(t)=5t/3+O(1)\), so the minimizing integer is \(n=\sqrt{5/3}\sqrt{t}+O(1)\). At that integer, the explicit rational function gives \(R_n(t)=1-9/(4t)+O(t^{-2})\): the nearest-integer rounding changes \(y\) by only \(O(\sqrt{t})\), and the local second derivative of \(Q_t\) is \(O(t^{-3})\). This yields the stated large-\(a\) expansion. All estimates are taken with \(a\) tending to the stated endpoint; no uniformity in changing circle dimension is claimed.

## Verification
The standalone `CHECK.py` performs 1,004 checks using only the Python standard library, including exact rational simplification and adjacent-difference identities, direct numerical Fourier integration for multiple damping rates and frequencies, global minimizer searches on long finite frequency ranges, and checking the algebraic crossings on 98 successive transitions. All completed successfully. These finite checks test the derivation but are not an infinite certificate; the proof above supplies the quantifiers for all admissible \(a,b\) and all circle configurations.

## Relationship to prior work
The circle Fourier criterion and positive-definite geodesic exponential baseline are classical; Gneiting's 2011 preprint (2013 publication) provides a standard comprehensive source. Otten, Nguyen and Watts (first posted August 5, 2026) establish positivity preservation under Bernstein interpolation of arbitrary circle kernels, rather than exact signed multiplication by a second harmonic. The published first-harmonic exponential modulation classification establishes an unbounded limiting-frequency staircase for \(e^{-a\theta}(1+b\cos\theta)\); it does not prove the present even-harmonic boundary or the stronger complete no-skips/only-adjacent-ties law. The first harmonic shifts Fourier coefficients between opposite parity classes, while the second harmonic cancels the parity factors and produces a different rational minimization and explicit successive algebraic crossings. A published damped-cosine classification treats \(e^{-a\theta}\cos(\omega\theta)\) without the unmodulated baseline; its integer-frequency positivity does not imply exact thresholds for negative mixtures. These distinctions are at the level of parameter implications, not mere title differences.

## Limitations
Only the second angular harmonic on the circle is classified. The argument does not characterize joint multiple-harmonic perturbations or spherical positive definiteness in dimensions at least two. An earlier derivation under a different name (including older circle covariance literature) remains a bibliographic priority risk; completeness of external literature searches is not claimed. The analogy with first-harmonic covariance modulation is strong, though that earlier result does not itself provide the present explicit all-mode crossing classification.

## References
1. M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836, first posted 2026-08-05, https://arxiv.org/abs/2608.04836 .
2. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, first posted 2011-11-30; Bernoulli 19 (2013), 1327–1349, https://arxiv.org/abs/1111.7077 .
3. *Sharp circle-covariance modulation threshold and an unbounded Fourier-mode staircase*, published result 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-circle-covariance-modulation-threshold-and-an-unbounded-fo--3df14ed06eed .
4. *Resonance windows for damped-cosine geodesic kernels on the circle*, published result 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-resonance-windows-for-damped-cosine-geodesic-kernels-on-the-circ--2d07956e836f .
