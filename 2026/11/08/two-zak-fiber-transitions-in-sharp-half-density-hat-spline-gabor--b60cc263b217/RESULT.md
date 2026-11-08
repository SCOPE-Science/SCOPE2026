# Two Zak-fiber transitions in sharp half-density hat-spline Gabor frame bounds

## Finding
Let \(g(t)=(1-|t|)_+\) and let \(a=1/(2b)\) with \(1\le b\le 3/2\). The optimal squared Gabor frame bounds for the system \(\{e^{2\pi i mbt}g(t-na):m,n\in\mathbb Z\}\) are
\[
 A(b)=\begin{cases}
 \dfrac{1}{2b^3},&1\le b\le 2-\dfrac{\sqrt{10}}4,\\[3pt]
 \dfrac{4(2-b)^2}{5b^3},&2-\dfrac{\sqrt{10}}4\le b\le\dfrac{19-\sqrt{10}}{12},\\[3pt]
 \dfrac{(7-4b)^2}{8b^3},&\dfrac{19-\sqrt{10}}{12}\le b\le 3/2,
 \end{cases}
 \qquad
 B(b)=\frac{(3b-2)^2+(2b-1)^2}{b^3}.
\]
In particular every indicated system is a frame, and its optimal squared frame condition number is exactly \(B(b)/A(b)\). The minimizing Zak-fiber locations undergo two genuine switches, at
\[
 b_0=2-\frac{\sqrt{10}}4,\qquad b_1=\frac{19-\sqrt{10}}{12}.
\]
For \(b<b_0\) and \(b>b_1\), a minimizing physical Zak coordinate is \(y=a/2\). For \(b_0<b<b_1\), the two distinct minimizing coordinates are \(y=(a+1)/5\) and \(y=a-(a+1)/5\). All these lower extrema occur at Zak phase \(\theta=1/2\); at each switch both the centered and the pair of off-center coordinates are minimizing. An upper extremum occurs at \(y=0\), Zak phase \(\theta=0\). These statements exhibit the locations but do not assert uniqueness among all phases at degenerate endpoints.

## Assumptions and scope
The real compactly supported window is \(g(t)=\max\{1-|t|,0\}\), without additional normalization. Modulations use \(e^{2\pi i mbt}\); the rectangular lattice parameters satisfy \(ab=1/2\), \(1\le b\le3/2\). The optimal lower and upper bounds are respectively the largest \(A\) and smallest \(B\) for which, for every \(f\in L^2(\mathbb R)\),
\[
 A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i mb(\cdot)}g(\cdot-na)\rangle|^2\le B\|f\|_2^2.
\]
Set \(u=1-2a\), \(v=3a-1\); then \(1/3\le a\le1/2\), \(u,v\ge0\), \(u+v=a\). For convenience \(x_+=\max\{x,0\}\).

## Proof
**1. Exact scalar Zak fiberization.** Define the unitary Zak transform at step \(1/b\) by
\[
 Z_b(x,\theta)=b^{-1/2}\sum_{k\in\mathbb Z}g((x-k)/b)e^{2\pi i k\theta}.
\]
At integer oversampling factor two, the Zibulski–Zeevi (equivalently unitary Zak) representation makes the squared frame-bound extrema the minimum and maximum of the continuous scalar fiber
\[
 H_b(x,\theta)=|Z_b(x,\theta)|^2+|Z_b(x+1/2,\theta)|^2
\]
on the unit torus. The two summands interchange after shifting \(x\) by \(1/2\) (using Zak quasiperiodicity), so write \(x=by\) with \(0\le y\le a\). The above normalizations are fixed: no unmentioned factor of two appears in \(H_b\).

**2. Exact finite Laurent polynomials.** Write \(z=e^{2\pi i\theta}\). Since \(1/b=2a\), and the hat function is supported on \([-1,1]\), direct enumeration for \(0\le y\le a\) gives
\[
 \begin{aligned}
 b^{1/2}Z_b(by,\theta)&=(u-y)_+z^{-1}+(1-y)+(u+y)z,\\
 b^{1/2}Z_b(by+1/2,\theta)&=(1-a-y)+(1-a+y)z+(y-v)_+z^2.
 \end{aligned}
\]
The coefficients are nonnegative. In the first Laurent polynomial the middle coefficient exceeds the sum of the other coefficients by
\[
 E(y)=2a-2y-(u-y)_+\ge0.
\]
In the second polynomial the corresponding excess is \(2y-(y-v)_+=E(a-y)\ge0\). These inequalities hold throughout \(0\le y\le a\), including all support-boundary cases.

**3. Exactly minimize and maximize the phase.** For any three nonnegative numbers \(p,q,r\) satisfying \(q\ge p+r\), the polynomial \(p+qz+rz^2\) has minimum modulus \(q-p-r\) on \(|z|=1\), attained at \(z=-1\), and maximum modulus \(p+q+r\), attained at \(z=1\). Multiplication by a unit power of \(z\) does not change modulus. Both Zak polynomials satisfy this criterion with the SAME minimizing and maximizing phase. Consequently, exactly for all \(y\in[0,a]\),
\[
 \min_{\theta}H_b(by,\theta)=\frac{E(y)^2+E(a-y)^2}{b},
\]
\[
 \max_{\theta}H_b(by,\theta)=\frac{(2-2a+(u-y)_+)^2+(2-2a+(y-v)_+)^2}{b}.
\]
The second expression is symmetric about \(a/2\) and convex in \(y\): each squared term is the square of a nonnegative convex piecewise-affine function. It therefore attains its maximum at \(y=0\) or \(a\). At \(y=0\), the two unsquared terms equal \(3-4a\) and \(2-2a\). Thus
\[
 B(b)=b^{-1}[(3-4a)^2+(2-2a)^2]
 =\frac{(3b-2)^2+(2b-1)^2}{b^3}.
\]

**4. Reduce the lower envelope to two competing minima.** Since \(E(y)^2+E(a-y)^2\) is symmetric under \(y\leftrightarrow a-y\), restrict to \(y\ge a/2\). The function
\[
 E(y)=\begin{cases}4a-1-y,&y\le u,\\2a-2y,&y\ge u\end{cases}
\]
is continuous, nonnegative, and decreasing. There is a central region on which both \(E(y)\) and \(E(a-y)\) are governed by the same affine branch. On that region their squared sum is minimized at \(y=a/2\), with normalized value
\[
 A_{\rm center}=
 \begin{cases}
 1/(2b^3),&a\ge2/5,\\
 (7-4b)^2/(8b^3),&a\le2/5.
 \end{cases}
\]
On the only possible outer region (\(y\ge u\) and \(a-y\le u\)), the unnormalized squared sum is the strictly convex quadratic
\[
 (2a-2y)^2+(3a-1+y)^2.
\]
Its unrestricted minimum occurs at \(y_*=(a+1)/5\), with normalized value
\[
 A_{\rm off}=\frac{4(4a-1)^2}{5b}=\frac{4(2-b)^2}{5b^3}.
\]
This stationary point belongs to the required outer interval and \([a/2,a]\) precisely when \(4/11\le a\le3/7\). Outside this feasibility interval the outer quadratic is minimized at its nearest endpoint, already belonging to the central region and therefore not beating the centered minimum. On the feasible interval the global minimum is consequently \(\min\{A_{\rm center},A_{\rm off}\}\).

**5. Sharp switches and endpoints.** For \(a\ge2/5\), the equality \(A_{\rm center}=A_{\rm off}\) simplifies to \(27a^2-16a+2=0\). The root in the feasible interval is \(a=(8+\sqrt{10})/27\), or \(b=b_0=2-\sqrt{10}/4\). For \(a\le2/5\), equality simplifies to \(117a^2-76a+12=0\). Its feasible root is \(a=(38+2\sqrt{10})/117\), or \(b=b_1=(19-\sqrt{10})/12\). Direct sign comparison of the continuous quadratic branches shows centered minimization for \(b\le b_0\), off-center minimization for \(b_0\le b\le b_1\), and centered minimization for \(b\ge b_1\). The indicated minima are distinct on both open transition-adjacent intervals, giving genuine optimizer switches. All formulas agree at the switches, and at the shared endpoint \(b=3/2\) the result gives \(A=1/27\), \(B=82/27\). The first bound is strictly positive on \([1,3/2]\); hence every lattice in the stated family is a frame.

## Verification
The accompanying standalone `verify.py` evaluates direct finite Zak sums, compares them with both exact fixed-phase envelopes, checks the global bound inequalities on deterministic meshes and additional phases, and uses rational arithmetic for the crucial coefficient-dominance identities. Run `python3 verify.py`. It prints `HAT_SPLINE_EXACT_BOUNDS_CHECKS_PASS 20242`. The finite tests are corroboration only; the proof above covers every real \(b\in[1,3/2]\) and every phase.

## Relationship to prior work
Atindehou, Frederick, Kouagou, and Okoudjou (arXiv:1806.05614, first publicly submitted 2018-06-14) establish frame regions for the hat spline and construct compactly supported dual windows, not the sharp, continuous optimal-bound functions or the two interior Zak-minimizer transitions above. Ghosh and Selvan (arXiv:2310.01141) prove different nonframe obstructions. Stangl and Frederick (arXiv:2609.00481) establish a complete qualitative frame-set criterion for integer-oversampling curves at \(b\ge3/2\) and identify Zak zeros; their inspected full paper proves no optimal bound formulas on the present open interval. A previously published published-finding corpus theorem on the same half-density lattice covers \(3/2\le b\le7/4\), and is explicitly acknowledged; the current proof covers the complementary interval \(1\le b\le3/2\), with agreement at the common endpoint. Another published-finding corpus theorem treats a quadratic lower-bound onset near \(b=2+1/(2q)\), outside the current regime. The distinction is quantitative optimal frame spectrum and optimizer geometry, not merely an existing frame/nonframe criterion.

## Limitations
The theorem covers the hat window and the continuous half-density segment \(1\le b\le3/2\); it does not extend to all lattice densities, other B-spline orders, or arbitrary windows. One newer related Zak-zero manuscript was accessible only through its abstract, leaving a residual priority risk from an unlocated or inaccessible sharp bound theorem. No claim of independent mathematical audit or automated formal proof is made.

## References
1. A. G. D. Atindehou, C. Frederick, Y. B. Kouagou and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614 (first submitted 2018-06-14), https://arxiv.org/abs/1806.05614.
2. R. Ghosh and A. A. Selvan, *Obstructions for Gabor frames of the second order B-spline*, arXiv:2310.01141 (2023), https://arxiv.org/abs/2310.01141.
3. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481 (first submitted 2026-08-31), https://arxiv.org/abs/2609.00481.
4. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (September 2026), https://arxiv.org/abs/2609.13116.
5. M. Zibulski and Y. Y. Zeevi, *Analysis of multiwindow Gabor-type schemes by frame methods*, Appl. Comput. Harmon. Anal. 4 (1997), 188–221.
6. *Sharp Gabor frame bounds and quadratic collapse for the hat spline at half-density*, published-finding corpus, 2026-10-11, public research record `SCOPE-sharp-gabor-frame-bounds-and-quadratic-collapse-for-the-hat-spli--c8f151d17e5c`.
7. *Sharp quadratic onset of the tent-spline Gabor lower frame bound*, published-finding corpus, 2026-10-11, public research record `SCOPE-sharp-quadratic-onset-of-the-tent-spline-gabor-lower-frame-bound--9587a4647148`.
