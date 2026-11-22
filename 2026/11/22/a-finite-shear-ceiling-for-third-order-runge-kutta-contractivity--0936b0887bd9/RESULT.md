# A finite shear ceiling for third-order Runge–Kutta contractivity on Jordan planes

## Finding

Let
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
A_\gamma=-I_2+\gamma N,\quad \gamma\ge0,
\]
and let the one-step stability matrix of any three-stage, order-three Runge–Kutta method on the autonomous linear equation \(u'=A_\gamma u\) be
\[
T_{h,\gamma}=P_3(hA_\gamma),\qquad
P_3(z)=1+z+\frac{z^2}{2}+\frac{z^3}{6},\quad h\ge0.
\]
Here *contractive* means \(\|T_{h,\gamma}\|_2\le1\) in the Euclidean operator norm, with equality allowed. Set
\[
\begin{aligned}
r(h)&=1-h+\frac{h^2}{2}-\frac{h^3}{6},\\
p(h)&=1-h+\frac{h^2}{2},\\
G(h)&=\frac{1-r(h)^2}{hp(h)}\qquad(h>0).
\end{aligned}
\]
Let \(\beta=2.512745326618329\ldots\) be the unique positive solution of \(r(\beta)=-1\). Let \(\theta=0.479811179914857\ldots\) be the unique positive root of
\[
F(h)=3h^5-20h^4+67h^3-132h^2+150h-48,
\]
and put \(\gamma_*=G(\theta)=2.032159292685585\ldots\). Then the **entire set of contractive steps** is:

1. For \(0\le\gamma\le2\), precisely \([0,h_+(\gamma)]\), where \(h_+(\gamma)\) is the unique point of \([\theta,\beta]\) satisfying \(G(h_+)=\gamma\). At \(\gamma=0\) this is \(h_+=\beta\), and at \(\gamma=2\) it is \(h_+=0.692694281922299\ldots\).
2. For \(2<\gamma<\gamma_*\), precisely \(\{0\}\cup[h_-(\gamma),h_+(\gamma)]\), where the two distinct positive endpoints solve \(G(h)=\gamma\) and lie respectively in \((0,\theta)\) and \((\theta,\beta)\).
3. For \(\gamma=\gamma_*\), precisely \(\{0,\theta\}\): a single positive, nonexpansive but not strictly contracting step survives.
4. For \(\gamma>\gamma_*\), only \(\{0\}\). **No positive step can make RK3 Euclidean nonexpansive**, although both eigenvalues of \(A_\gamma\) are \(-1\), and \(|r(h)|<1\) for \(0<h<\beta\).

The transition is nondegenerate. As \(\gamma\uparrow\gamma_*\) from below, the two positive endpoints satisfy
\[
h_\pm(\gamma)=\theta\pm
\sqrt{\frac{2(\gamma_*-\gamma)}{-G''(\theta)}}
+O(\gamma_*-\gamma),
\quad G''(\theta)=-1.016470275286785\ldots.
\]
In particular, the interval length is asymptotic to \(2.805418470296674\ldots\sqrt{\gamma_*-\gamma}\). Also, as \(\gamma\downarrow2\) from above, \(h_-(\gamma)=\sqrt{3(\gamma-2)}+O(\gamma-2)\).

Unlike the fourth-order Taylor Runge–Kutta polynomial, which has a derivative zero inside its scalar stability interval and can become contractive at an intermediate step for arbitrarily large \(\gamma\), the third-order polynomial has the strictly positive derivative \(p(h)\), giving the *finite* ceiling \(\gamma_*\). This is a comparison of two different methods, not a claim about their relative numerical accuracy.

## Assumptions and scope

All matrices are real and of dimension exactly two; \(\gamma\) is nonnegative, \(h\) is nonnegative, and the norm is the unweighted Euclidean spectral norm. All three-stage, order-three explicit Runge–Kutta methods have the stated cubic stability polynomial on autonomous linear equations, so the classification covers their common endpoint propagator. Nothing is asserted about internal stages, nonlinear dynamics, other matrices, or arbitrary norms. This is a *one-step* nonexpansion criterion, not an error estimate.

The exact semigroup is \(e^{tA_\gamma}=e^{-t}(I+\gamma tN)\). Its norm is nonincreasing for all \(t\ge0\) if and only if \(\gamma\le2\), since the symmetric part of the generator has largest eigenvalue \(-1+\gamma/2\). Thus the detached positive-step interval for \(2<\gamma<\gamma_*\) occurs despite failure of *infinitesimal* physical contractivity. It does not imply the exact flow is expanding at those same finite times.

## Proof

**Polynomial reduction and norm criterion.** Since \(N^2=0\), polynomial calculus gives exactly
\[
T_{h,\gamma}=r(h)I_2+\gamma hp(h)N.
\]
For real \(a,d\), direct calculation of the two singular values of the upper-triangular matrix \(\begin{psmallmatrix}a&d\\0&a\end{psmallmatrix}\) yields
\[
\left\|\begin{pmatrix}a&d\\0&a\end{pmatrix}\right\|_2
=\frac{\sqrt{4a^2+d^2}+|d|}{2},\qquad
\|\cdot\|_2\le1\iff a^2+|d|\le1.
\]
The equivalence follows by requiring \(\sqrt{4a^2+d^2}\le2-|d|\), noting the right side is nonnegative whenever the final inequality holds, and squaring. As \(p(h)=((h-1)^2+1)/2>0\), the criterion is
\[
\boxed{r(h)^2+\gamma hp(h)\le1.}\tag{1}
\]

**Scalar interval.** We have \(r'(h)=-p(h)<0\), \(r(0)=1\), and \(r(h)\to-\infty\). Hence \(|r(h)|\le1\) holds exactly on \([0,\beta]\), where \(\beta\) solves \(h^3-3h^2+6h-12=0\). That cubic has derivative \(3((h-1)^2+1)>0\), so the endpoint is unique. For \(0<h<\beta\), (1) is equivalent to \(\gamma\le G(h)\), while \(h=0\) is always allowed and no \(h>\beta\) is allowed.

**The unique fold.** Exact algebra gives
\[
G(h)=-\frac{(h^2-3h+6)(h^3-3h^2+6h-12)}{18(h^2-2h+2)},
\quad
G'(h)=-\frac{hF(h)}{18(h^2-2h+2)^2}.
\]
The key positivity identity is
\[
\begin{aligned}
F'(h)&=15h^4-80h^3+201h^2-264h+150\\
&=15\left(h^2-\frac{8h}{3}+2\right)^2
+\frac{103}{3}\left(h-\frac{156}{103}\right)^2
+\frac{1158}{103}>0
\end{aligned}
\]
for *every real* \(h\). Since \(F(0)=-48\), \(F(1)=20\), there is exactly one real root \(\theta\) and it lies in \((0,1)\subset(0,\beta)\). Thus \(G\) strictly increases from \(G(0+)=2\) to its single maximum \(\gamma_*\) on \((0,\theta)\), then strictly decreases to \(G(\beta)=0\) on \((\theta,\beta)\). Intersecting horizontal lines \(\gamma\ge0\) with this graph proves all four cases, including equality and strict failure above \(\gamma_*\). The value \(h_+(2)\) solves \(h^3-6h^2+21h-12=0\), whose derivative is \(3((h-2)^2+3)>0\); the root on \((\theta,\beta)\) is unique.

**Sharp onset and collapse.** Taylor expansion gives \(G(h)=2+h^2/3-h^3/4+O(h^4)\) as \(h\downarrow0\), establishing the square-root onset of \(h_-\). At the unique maximum, \(G''(\theta)=-\theta F'(\theta)/[18(\theta^2-2\theta+2)^2]<0\). Taylor expansion about \(\theta\) and inversion on the two monotone branches give the stated nondegenerate square-root collapse and its coefficient. The decimal figures are only approximations to these exact definitions.

**Continuous-time comparison.** The symmetric part of \(A_\gamma\) has eigenvalues \(-1\pm\gamma/2\). This proves all-time contractivity of its exact semigroup exactly for \(\gamma\le2\); for \(\gamma>2\) an initial state in the top symmetric eigendirection has increasing squared norm at time zero. The cubic derivative \(P_3'(-h)=p(h)>0\) for all \(h\ge0\) has no annihilation point for the nilpotent part. In contrast, the fourth-order polynomial derivative has one positive real zero after substitution \(-h\), accounting for the different qualitative shear ceiling; no fourth-order phase-diagram result is required for the cubic theorem.

## Verification

The standalone standard-library Python file `verify.py` checks exact rational polynomial and derivative identities, including the sum-of-squares decomposition proving strict positivity; exact evaluation of \(P_3(hA_\gamma)\) by three matrix multiplications on 525 rational parameter pairs; and 11,537 independent direct singular-norm comparisons. It numerically isolates \(\beta\), \(\theta\), \(\gamma_*\), and \(h_+(2)\), and checks example supercritical and subcritical regimes. Run `python3 verify.py`. Its resulting exact output is included in `verification_output.txt`. The exact inequalities and root uniqueness in the proof establish the theorem for all real parameter values; no finite tests are substituted for them.

## Relationship to prior work

Sun and Shu [1] and Sun, Wei, and Wu [2] establish general strong-stability and energy-law frameworks for seminegative linear operators, including generic third-order conditional stability; these do not furnish an all-step, non-dissipative \(\gamma>2\) parameter phase diagram. Achleitner, Arnold, and Jüngel [3] provide further conditions for strongly stable explicit RK methods and examine weighted-norm Jordan examples, but not the present exact Euclidean cubic-shear ceiling.

A published technical note [4] classifies *fourth-order* RK on precisely the same planar Jordan family; it produces a contractive intermediate-step interval for **every** \(\gamma>2\), with an unbounded shear range. Its exact criterion uses \(P_4'(-h)\), which vanishes at a positive \(h\); none of the cubic threshold, the unique finite shear ceiling, the singleton critical point, or the square-root collapse follows from that result. We regard the common triangular-matrix singular-value identity and scalar RK stability facts as existing ingredients, not new results.

The inspected papers and published comparison do not identify the stated exact cubic phase diagram. This is a best-knowledge originality comparison, not a proof of global historical priority; other specialist RK stability literature may contain it.

## Limitations

The result concerns only autonomous linear systems generated by this \(2\times2\) Jordan family and its unweighted Euclidean one-step operator norm. It neither proves that a numerically contractive step accurately follows the exact flow nor extends to higher Jordan blocks, other norms, variable timesteps, nonlinear right-hand sides, or general stability polynomials. The numerical value \(\gamma_*-2\approx0.0321593\) is small, but the finite-shear cutoff and loss of every positive contractive step distinguish cubic RK qualitatively from fourth-order RK on the same natural test family.

## References

[1] Z. Sun and C.-W. Shu, *Strong Stability of Explicit Runge–Kutta Time Discretizations*, arXiv:1811.10680v1 (first posted 2018-11-26), https://arxiv.org/abs/1811.10680 .

[2] Z. Sun, Y. Wei, and K. Wu, *On Energy Laws and Stability of Runge–Kutta Methods for Linear Seminegative Problems*, arXiv:2201.06501v1 (first posted 2022-01-17), https://arxiv.org/abs/2201.06501 .

[3] F. Achleitner, A. Arnold, and A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge–Kutta methods*, arXiv:2308.05689v1 (first posted 2023-08-10), https://arxiv.org/abs/2308.05689 .

[4] *A sharp false-contractivity island for classical fourth-order Runge–Kutta on planar Jordan shears*, technical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-false-contractivity-island-for-classical-fourth-order-ru--8fe2a7f6e756 .
