# Sharp Poisson ultra-log-concavity threshold for four-dimensional circular cones

## Finding

For \(0<\alpha<\pi/2\) let
\[
C_\alpha=\{x\in\mathbb R^4:x_4\ge \|x\|_2\cos\alpha\},
\]
and let \(v_k(\alpha)\), \(0\le k\le4\), denote its conic intrinsic volumes. For an everywhere-positive finite sequence \((a_0,\ldots,a_4)\), **Poisson ultra-log-concavity** means
\[
a_k^2\ge\frac{k+1}{k}a_{k-1}a_{k+1},\qquad k=1,2,3.
\]
Set
\[
R(x)=\frac{\pi^2\sin^3x}{8\cos x\,[x-\sin x\cos x]},\qquad0<x<\pi/2.
\]
There is exactly one \(\beta_*\in(0,\pi/2)\) satisfying \(R(\beta_*)=2\). Write \(\alpha_*=\pi/2-\beta_*\); numerically
\[
\beta_*=0.5861771479686968\ldots,\quad
\alpha_*=0.9846191788261998\ldots\ \text{radians}
=56.4145233743781\ldots^\circ.
\]
Then the **entire conic intrinsic-volume sequence is Poisson ultra-log-concave exactly for \(0<\alpha\le\alpha_*\)**. For \(0<\alpha<\alpha_*\) all three inequalities are strict; at \(\alpha=\alpha_*\) equality occurs precisely at \(k=1\); for \(\alpha_*<\alpha<\pi/2\) the inequality at \(k=1\) fails, while those at \(k=2,3\) remain strict.

In contrast, **binomial ultra-log-concavity in ambient dimension four never holds** for any \(0<\alpha<\pi/2\). Indeed the central intrinsic-volume quotient is aperture-independent:
\[
\frac{v_2(\alpha)^2}{v_1(\alpha)v_3(\alpha)}=\frac{16}{\pi^2}
<\frac94.
\]
This is a complete classification within the fixed four-dimensional circular-cone family, not a statement about arbitrary cones or other dimensions.

## Assumptions and scope

All cones are closed, full-dimensional and pointed, with \(0<\alpha<\pi/2\). Conic intrinsic volumes use the normalization \(\sum_{k=0}^4v_k(C)=1\) and spherical-Gaussian (not Euclidean-body) intrinsic volumes. Every \(v_k\) is positive in the stated open interval. The binomial ULC\((4)\) condition is log-concavity of \(v_k/\binom4k\), equivalently
\[
v_k^2\ge\frac{(k+1)(5-k)}{k(4-k)}v_{k-1}v_{k+1},\qquad k=1,2,3.
\]
At the excluded degenerate endpoints \(\alpha=0,\pi/2\), zeros change the support, so no assertion using the displayed positive-entry quotients is made.

## Proof

**1. Intrinsic volumes.** The circular-cone formula of Amelunxen–Lotz–McCoy–Tropp, Appendix C.1, gives, when \(d=4\), the three interior entries \(v_1=\cos^2\alpha/2\), \(v_2=2\sin\alpha\cos\alpha/\pi\), and \(v_3=\sin^2\alpha/2\). The endpoints are spherical-cap probabilities of the cone and its polar (whose half-opening angle is \(\beta=\pi/2-\alpha\)), so integration of the \(\sin^2t\) spherical density yields
\[
\begin{aligned}
v_0&=\frac{\beta-\sin\beta\cos\beta}{\pi},&
v_1&=\frac{\cos^2\alpha}{2},&
v_2&=\frac{2\sin\alpha\cos\alpha}{\pi},\\
v_3&=\frac{\sin^2\alpha}{2},&
v_4&=\frac{\alpha-\sin\alpha\cos\alpha}{\pi}.
\end{aligned}
\]
All entries are positive. Their sum is one because \(\alpha+\beta=\pi/2\) and \(\sin\beta\cos\beta=\sin\alpha\cos\alpha\). This independently checks endpoint and interior normalizations.

**2. The three Poisson quotients.** Straight substitution gives
\[
\frac{v_1^2}{v_0v_2}=R(\beta),\qquad
\frac{v_2^2}{v_1v_3}=\frac{16}{\pi^2},\qquad
\frac{v_3^2}{v_2v_4}=R(\alpha).
\]
The corresponding Poisson requirements are, in order, \(R(\beta)\ge2\), \(16/\pi^2\ge3/2\), and \(R(\alpha)\ge4/3\).

**3. Sharp monotonicity of the critical quotient.** Since \(x-\sin x\cos x>0\) for \(0<x<\pi/2\) (its derivative is \(2\sin^2x>0\)), \(R(x)\) is well-defined and positive. An explicit logarithmic derivative is
\[
\frac{R'(x)}{R(x)}=
\frac{x(1+2\cos^2x)-3\sin x\cos x}
{\sin x\cos x\,[x-\sin x\cos x]}.
\]
Denote the numerator by \(F(x)\). Then \(F(0)=0\) in the continuous extension, and
\[
F'(x)=4\sin x\,(\sin x-x\cos x)>0
\]
because \(\sin x-x\cos x=\int_0^x t\sin t\,dt>0\). Hence \(R'(x)>0\) for every interior \(x\). Taylor expansion, or three applications of l'Hôpital's rule, shows
\[
\lim_{x\downarrow0}R(x)=\frac{3\pi^2}{16},\qquad
\lim_{x\uparrow\pi/2}R(x)=+\infty.
\]
Since \(\pi^2<32/3\), the left limit is below two, and a unique \(\beta_*\) satisfies \(R(\beta_*)=2\). Because \(\beta=\pi/2-\alpha\), the first Poisson inequality holds exactly when \(\alpha\le\pi/2-\beta_*\). The middle inequality is always strict because \(\pi^2<32/3\) implies \(16/\pi^2>3/2\). The final inequality is always strict since \(R(\alpha)>3\pi^2/16>4/3\) (using \(\pi>3\)). This proves the full phase classification and equality assertions.

**4. Complete binomial failure.** At \(k=2\) the binomial ULC\((4)\) factor is \(\binom42^2/(\binom41\binom43)=9/4\). But the universal central quotient \(16/\pi^2<9/4\) since \(\pi>3\). Thus every nondegenerate four-dimensional circular cone violates ULC\((4)\), independent of its aperture. This includes all cones on both sides of the Poisson transition.

## Verification

The accompanying standalone `verify.py` recomputes the five intrinsic volumes by separate formulas for interior and endpoint values, checks normalization and quotient identities at 181 interior apertures, brackets the unique positive root \(R(\beta)=2\), checks the signs of all three Poisson inequalities around the threshold, and reproduces the motivating \(\alpha=\pi/3\) counterexample. It tests identities at finitely many values only; strict inequalities and uniqueness on the entire open interval follow from the preceding analytic argument. Running `python verify.py` requires only the Python standard library.

## Relationship to prior work

Fu and Wang (arXiv:2607.17278, first public version 2026-07-19) prove general refined log-concavity and exhibit one four-dimensional circular cone of angle \(\pi/3\) that violates Poisson ULC, hence binomial ULC. Their full Section 4 does not give the sharp admissible aperture interval, its unique equality angle, the location of the only failing Poisson index, or the aperture-independent central binomial obstruction. The paper uses the circular-cone formula from Amelunxen–Lotz–McCoy–Tropp (2013/2014), which already determines all five entries. The present classification does not claim those entry formulas or the specific \(\pi/3\) counterexample as new. The additional content is a complete sharp parameter theorem with a monotonicity certificate and strict boundaries. Amelunxen's 2018 computational notes give the more general beta-function expressions and discuss ordinary log-concavity; they do not establish this Poisson-ULC phase diagram.

## Limitations

Only circular cones in \(\mathbb R^4\), and only apertures strictly between zero and \(\pi/2\), are covered. The threshold is exactly defined by a transcendental scalar equation and its decimal is an approximation. The statement is not a conjectural universal inequality for arbitrary convex cones. The newness claim is based on inspection of the identified primary results and searches, not a proof of historical priority or independent validation.

## References

1. H. Fu and S. Wang, *Log-Concavity of Conic Intrinsic Volumes*, arXiv:2607.17278, initial public version 2026-07-19, https://arxiv.org/abs/2607.17278. Main theorem and Section 4, “Limits of ultra-log-concavity.”
2. D. Amelunxen, M. Lotz, M. B. McCoy and J. A. Tropp, *Living on the edge: Phase transitions in convex programs with random data*, arXiv:1303.6672, 2013; Appendix C.1, formula (C.2), https://arxiv.org/abs/1303.6672.
3. D. Amelunxen, *Conic intrinsic volumes and the (bivariate) chi-bar-squared distribution*, 2018-04-12, sections “Examples: circular cones” and “Log-concavity conjecture”, https://damelunx.github.io/conivol/articles/conic-intrinsic-volumes.html.
