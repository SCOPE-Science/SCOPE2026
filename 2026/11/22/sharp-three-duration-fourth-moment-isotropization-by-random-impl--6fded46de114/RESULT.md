# Sharp three-duration fourth-moment isotropization by random implicit-midpoint steps

## Finding

Fix \(\omega>0\) and the harmonic oscillator \(\dot q=p\), \(\dot p=-\omega^2q\). Let \(H\geq0\) be an exogenous random implicit-midpoint duration, independent of the initial state, with finite mean. In energy coordinates \(u=(\omega q,p)\), say that the one-step law is *quartic-isotropizing* if, for every deterministic input \(u\) and every real homogeneous polynomial \(P\) of degree four, the expected value of \(P\) after the random update equals its uniform-angle average over the circle \(\{v:\|v\|=\|u\|\}\). The same property then holds for all homogeneous quadratic polynomials.

**Theorem (one sharp classification).** Quartic isotropization holds if and only if, with
\[
\theta(H)=2\arctan(\omega H/2)\in[0,\pi),
\]
one has both
\[
\mathbb E e^{2i\theta(H)}=0,\qquad \mathbb E e^{4i\theta(H)}=0.
\]
Every such law satisfies the sharp lower bound
\[
\boxed{\mathbb E H\geq\frac{8}{3\sqrt3\,\omega}.}
\]
Equality holds **only** for the equiprobable three-duration law
\[
\boxed{H\in\left\{0,\frac{2}{\sqrt3\,\omega},\frac{2\sqrt3}{\omega}\right\},\quad \Pr(H=h)=\frac13\text{ for each of its three values}.}
\]
At least three distinct durations are required by every quartic-isotropizing law. If a maximum duration \(L<\infty\) is imposed, a nonnegative-duration quartic-isotropizing law exists **if and only if** \(L\geq2\sqrt3/\omega\); at equality the displayed law is the only feasible one. Under the restriction \(H>0\) almost surely, the sharp mean bound is an unattained infimum, and a law under the cap exists precisely when \(L>2\sqrt3/\omega\).

For comparison, the sharp mean for second-moment isotropization alone is \(1/\omega\) [2]. Its two-duration extremizer fails the fourth-harmonic cancellation condition; the quartic requirement thus has a strictly greater sharp mean and support-size threshold.

## Assumptions and scope

The oscillator is real and linear with \(\omega>0\), and implicit midpoint is applied for a single independent random duration \(H\geq0\). Zero duration means the identity update. The law has finite expectation, though it may have unbounded support. A finite cap \(L\) is considered only for the cap part of the theorem. The isotropy target is the **uniform-angle average of even polynomial observables of degree at most four on a fixed energy circle**, not convergence of the entire output distribution to uniform measure. In particular, it does not require vanishing first or third angular harmonics.

The quantity optimized is mean represented physical duration per update, not solver cost, truncation error, or the distance between the random numerical endpoint and the exact flow evaluated at a fixed physical time. One-step results do not require independent identically distributed durations across multiple iterations.

## Proof

**Cayley rotation and the moment criterion.** With \(t=\omega H/2\), put
\[
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
M(t)=(I-tJ)^{-1}(I+tJ)
=\frac1{1+t^2}\begin{pmatrix}1-t^2&2t\\-2t&1-t^2\end{pmatrix}.
\]
Direct multiplication gives \(M(t)^\top M(t)=I\). Under the complex coordinate \(z=u_1+iu_2\), this matrix multiplies \(z\) by \(e^{-i\theta}\), with \(\theta=2\arctan t\). Every real homogeneous quartic polynomial restricted to a circle is a real linear combination of the constant function, \(\cos(2\varphi)\), \(\sin(2\varphi)\), \(\cos(4\varphi)\), and \(\sin(4\varphi)\). Conversely, these four nonconstant harmonics are restrictions of real homogeneous quartics: use the real and imaginary parts of \((u_1+iu_2)^4\) and of \((u_1^2+u_2^2)(u_1+iu_2)^2\). Hence universal quartic isotropization is exactly the two vanishing complex moments stated above, and it also removes the anisotropic quadratic harmonic.

**Sharp mean certificate.** Write \(t=\tan(\theta/2)\) and define the degree-four trigonometric polynomial
\[
G(\theta)=\frac{8\sqrt3}{9}
-\frac{4\sqrt3}{9}\bigl(\cos2\theta+\cos4\theta\bigr)
-\frac{16}{9}\sin2\theta-\frac49\sin4\theta.
\]
The following rational identity is exact for every \(t\geq0\):
\[
\begin{split}
2t-G(2\arctan t)={}&
\frac{2t\,(t-\sqrt3)^2(t-1/\sqrt3)^2}{3(1+t^2)^4}\\
&\quad\times(3t^4+8\sqrt3\,t^3+38t^2+24\sqrt3\,t+19)\geq0.
\end{split}
\]
All coefficients of the last factor are strictly positive; equality occurs only at \(t=0\), \(t=1/\sqrt3\), or \(t=\sqrt3\). The two vanishing harmonic moments force \(\mathbb EG(\theta)=8\sqrt3/9\). Since \(\omega H=2t\), integration gives \(\omega\mathbb EH\geq8\sqrt3/9=8/(3\sqrt3)\). Equality forces support on exactly the three listed duration candidates. Their phases \(e^{2i\theta}\) are the three cubic roots of unity; their weighted sum is zero only with masses \(1/3\) each, and those masses also cancel \(e^{4i\theta}\). Thus the lower bound and unique optimizer are established.

**Minimum support.** Put \(Z=e^{2i\theta}\) and \(v=(1,Z,Z^2)^\top\). The conditions \(\mathbb EZ=\mathbb EZ^2=0\), together with \(|Z|=1\), imply \(\mathbb E(vv^*)=I_3\). Any measure supported on fewer than three points would give a matrix of rank at most two, a contradiction.

**Sharp duration cap.** Assume \(0\leq H\leq L<\infty\), and set \(\alpha=2\arctan(\omega L/2)\in[0,\pi)\). Then \(\psi=2\theta-\alpha\in[-\alpha,\alpha]\). The pointwise inequality
\[
(\cos\psi-\cos\alpha)(1-\cos\psi)\geq0
\]
holds since cosine decreases on \([0,\pi]\). The two harmonic conditions yield \(\mathbb E\cos\psi=0\) and \(\mathbb E\cos^2\psi=1/2\). Therefore
\[
0\leq\mathbb E[(\cos\psi-\cos\alpha)(1-\cos\psi)]
=-\frac12-\cos\alpha.
\]
Hence \(\alpha\geq2\pi/3\), equivalently \(L\geq2\sqrt3/\omega\). At equality, the pointwise product must vanish almost surely, so \(\psi\in\{-\alpha,0,\alpha\}\), corresponding to exactly the three durations in the displayed law. Their weights are forced to be equal. For every larger cap the same law is feasible.

**Strict positivity.** For any sufficiently small \(\delta>0\), choose three equally likely angles \(\theta\in\{\delta,\delta+\pi/3,\delta+2\pi/3\}\). Both harmonic moments remain zero because a common phase multiplies each root-of-unity sum. The corresponding positive durations \(H=2\tan(\theta/2)/\omega\) converge to the optimal nonnegative triple as \(\delta\downarrow0\), and their maximum approaches \(2\sqrt3/\omega\) from above. This proves the unattained strict-positive mean infimum and its strict cap frontier.

## Verification

The standalone `verify.py` reconstructs the Cayley matrix, checks orthogonality and the exact nonnegative rational identity symbolically, verifies the two canceled moments and sharp mean at the three support points, and checks strictly positive rotated approximants. Optional numerical linear programming on discretized angles provides independent finite-grid diagnostics. Run `python -m pip install -r requirements.txt` and `python verify.py`. The universal inequalities and uniqueness are proved above; no finite search is treated as a proof for arbitrary probability laws.

## Relationship to prior work

Abdulle and Garegnani [1] introduced random-time-step integration preserving the geometric invariants of underlying Runge–Kutta methods, including implicit midpoint's quadratic invariants. Their paper studies convergence and pathwise conservation, not cost-optimal annihilation of multiple angular moments. A published sharp second-moment result [2] gives a two-atom design with mean \(1/\omega\) and cap \(2/\omega\), but explicitly stops at the second angular harmonic: its extremizer has nonzero fourth harmonic. This theorem simultaneously cancels the second and fourth harmonics and establishes different sharp duration, cap, and support-size frontiers. The roots-of-unity construction uses standard circular quadrature ideas; the global mean-cost inequality and cap necessity are proved by explicit certificates. No general theorem of unique optimality beyond the stated fourth-degree problem is asserted.

## Limitations

The theorem covers only a single oscillator frequency, exogenous one-step randomization, and even angular moments through order four. It does not produce a uniform one-step phase distribution, describe odd moments, optimize total numerical workload or physical-time accuracy, or extend automatically to coupled frequencies and nonlinear Hamiltonians. Unindexed classical trigonometric-design or quadrature literature could contain an equivalent cost-optimality statement; publication-priority assessment remains provisional. No independent validation has been performed.

## References

1. A. Abdulle and G. Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first public version 2018-01-04), especially Sections 2, 6, 7 and 9.5. https://arxiv.org/abs/1801.01340
2. *Minimum mean step for one-step second-moment isotropization under random-time implicit midpoint* (published 2026-10-13), full theorem and proof. https://github.com/published-finding corpus/2026/blob/main/2026/10/13/SCOPE-minimum-mean-step-for-one-step-second-moment-isotropization-unde--bb97d1702b8a/RESULT.md
3. W. B. Jones, O. Njåstad, and W. J. Thron, *Moment Theory, Orthogonal Polynomials, Quadrature, and Continued Fractions Associated with the Unit Circle*, Bull. Lond. Math. Soc. 21 (1989), 113–152, DOI:10.1112/blms/21.2.113 (background on trigonometric moment problems, not an asserted covering theorem).
