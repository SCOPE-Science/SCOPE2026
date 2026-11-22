# An antipodal escape threshold for the scalar Prox-NAG-GS method

## Finding

Consider the constant-damping Prox-NAG-GS iteration of [1] on the strongly convex composite objective
\[
F(x)=\frac{\mu}{2}x^2+\lambda |x|,\qquad \mu,\lambda>0.
\]
Fix a coupling parameter \(0<a<1\), a proximal curvature \(h>0\), and the prescribed constant damping initialization \(\gamma_0=h\). Write \(k=\mu/h\), \(b=1-a\), \(c=(2-a)/a\), \(\theta=a\lambda/h\), and
\[
k_*(a)=1+\left(\frac{2-a}{a}\right)^2.
\]
The method acts on its two scalar states as
\[
 x^+=bx+av,\qquad
 v^+=S_\theta\bigl(bv+a(1-k)x^+\bigr),
 \quad S_\theta(u)=\operatorname{sgn}(u)(|u|-\theta)_+.
\]

**Theorem (sharp escape frontier and antipodal cycle).** For every \(a\in(0,1)\) and every \(\mu,\lambda,h>0\):

1. The minimizer \((x,v)=(0,0)\) is locally exponentially attracting, for *every* curvature ratio \(k>0\), including arbitrarily large ratios. In sufficiently small neighborhoods the proximal state becomes zero after one update and the other state subsequently decays by the factor \(1-a\).
2. If \(0<k<k_*(a)\), *every* orbit from any two-state initialization remains bounded. In particular this holds for the source-prescribed initialization \(v_0=x_0\).
3. If \(k>k_*(a)\), the algorithm has exactly one nonzero **antipodal** two-cycle (a period-two orbit satisfying \((x^+,v^+)=-(x,v)\)). Up to swapping its two points, it is
\[
 (x,v)=(X,-cX),\quad (-X,cX),\qquad
 X=\frac{\theta}{a(k-k_*(a))}=\frac{\lambda}{\mu-hk_*(a)}.
\]
It is an explicit separator for an invariant escape cone. In particular, an entire open ray of the prescribed diagonal initializations \(x_0=v_0=R>0\) escapes to infinity in alternating signs. A sufficient exact choice is
\[
R>\max\left\{X,\frac{\theta}{ak-2/a}\right\}.
\]
The divergence is exponential after the first step. The cycle amplitude tends to infinity as \(k\downarrow k_*(a)\).
4. At and below \(k_*(a)\), there is no nonzero antipodal two-cycle. No general boundedness or convergence classification is asserted *at equality* \(k=k_*(a)\). The result does not classify non-antipodal periodic orbits.

Consequently, the positive \(\ell_1\) regularizer creates a locally attracting minimizer even in a regime where arbitrarily large, prescribed-start trajectories diverge. Below the exact linear Schur frontier every trajectory is bounded; above it unbounded prescribed-start trajectories coexist with that local attractor. The two opposite-side statements are strict, with the equality case deliberately left open.

## Assumptions and scope

This is a scalar deterministic statement, with exact arithmetic, a time-independent \(a\), \(\mu,\lambda,h>0\), and constant damping \(\gamma_0=h\) as in [1, Algorithm 1, constant-parameter reduction]. The smooth part is \(f(x)=\mu x^2/2\), the proximable part is \(r(x)=\lambda|x|\), and the unique composite minimizer is zero. The source parameter \(\alpha=a/(1-a)\) is positive; its parameter denoted \(\widehat\mu\) equals \(h\) here. There are no stochastic gradients, floating-point rounding, time-varying damping, or higher-dimensional claims. The paper initializes \(v_0=x_0\); the theorem proves both two-state boundedness and escaping examples satisfying that initialization.

## Proof

**1. Exact recurrence and local attraction.** With \(\gamma_0=h\), Algorithm 1 has \(b_k=a_k=a\), and hence
\[
x^+=bx+av,\quad z^+=bv+ax^+,\quad
v^+=\operatorname{prox}_{(a/h)\lambda|\cdot|}(z^+-(a/h)\mu x^+).
\]
The proximal map is \(S_\theta\), giving precisely the displayed recurrence. Since its pre-threshold argument is continuous and vanishes at the origin, there exists \(\varepsilon>0\) such that for all \(|x|,|v|<\varepsilon\), the next proximal state is zero. Shrink \(\varepsilon\), if necessary, to ensure that \(|a b(1-k)x|<\theta\) throughout \(|x|<\varepsilon\). Because \(x^+=bx+av\) is a strict convex combination, \(|x^+|<\varepsilon\). Thus subsequent proximal states stay zero and \(x\) is repeatedly multiplied by \(b\in(0,1)\). This proves the local claim for all \(k>0\).

**2. Boundedness below the frontier.** Put \(u=bv+a(1-k)x^+\). The nonlinearity satisfies \(|S_\theta(u)-u|\le\theta\). Hence the state recursion is
\[
\begin{pmatrix}x^+\\v^+\end{pmatrix}
=A\begin{pmatrix}x\\v\end{pmatrix}+
\begin{pmatrix}0\\d\end{pmatrix},\qquad |d|\le\theta,
\quad
A=\begin{pmatrix}b&a\\ab(1-k)&b+a^2(1-k)\end{pmatrix}.
\]
The trace and determinant of \(A\) are
\[
T=2b+a^2(1-k),\qquad \det A=b^2.
\]
The three strict Schur inequalities are exactly
\[
1-b^2>0,\qquad 1-T+b^2=a^2k>0,\qquad
1+T+b^2=a^2(k_*(a)-k)>0.
\]
Thus \(A\) is Schur stable for \(0<k<k_*\). Consequently \(\sum_{j\ge0}\|A^j\|<\infty\) in any fixed matrix norm. Iterating the bounded-input representation gives the explicit finite bound
\[
\sup_{n\ge0}\|(x_n,v_n)\|
\le\sup_{n\ge0}\|A^n\|\|(x_0,v_0)\|
+\theta\sum_{j=0}^{\infty}\|A^j(0,1)^\top\|.
\]
This proves global boundedness, not convergence.

**3. Unique antipodal cycle.** Suppose \((x^+,v^+)=(-x,-v)\) and \((x,v)\ne(0,0)\). The first equation forces \(v=-cx\) and \(x\ne0\). By oddness we take \(x>0\). Then \(v^+=cx>0\), so the soft-threshold input must equal \(cx+\theta\). Direct substitution gives
\[
 b(-cx)+a(1-k)(-x)=\bigl[a(k-1)-bc\bigr]x.
\]
The equality \(\bigl[a(k-1)-bc-c\bigr]x=\theta\) reduces to
\[
 a(k-k_*(a))x=\theta.
\]
There is a positive solution exactly when \(k>k_*\), and it is \(x=X\). Oddness then produces its antipodal partner. Uniqueness within the antipodal class and nonexistence for \(k\le k_*\) follow.

**4. Exact invariant escape cone.** Now assume \(k>k_*\), put \(\Delta=k-k_*>0\), and define
\[
\Gamma=a^2(k-1)-(3-2a)
=b^2+a^2\Delta>0.
\]
Consider any state \(x\ge X\), \(v=-cx-w\), \(w\ge0\). The update obeys
\[
x^+=-x-aw,
\]
while its prethreshold argument is positive and satisfies
\[
u-\theta-c(x+aw)
=a\Delta(x-X)+\Gamma w\ge0.
\]
It follows that \(v^+=c(-x^+)+w^+\), where
\[
w^+=a\Delta(x-X)+\Gamma w\ge0.
\]
Thus this positive cone maps into its negative, and oddness maps the negative cone back into the positive cone. Denote the absolute first-state magnitude by \(Y_n=|x_n|\), and the cone slack by \(w_n\). Along successive cone steps,
\[
\begin{pmatrix}Y_{n+1}-X\\w_{n+1}\end{pmatrix}
=\begin{pmatrix}1&a\\a\Delta&\Gamma\end{pmatrix}
\begin{pmatrix}Y_n-X\\w_n\end{pmatrix}.
\]
The positive matrix has one Perron eigenvalue strictly larger than one: indeed its characteristic polynomial at one is \(-a^2\Delta<0\). Every nonzero vector in the closed positive quadrant expands exponentially, by positivity and the Perron eigenvectors (or by direct two-step comparison). The zero vector gives precisely the antipodal cycle.

Finally, start with \(x_0=v_0=R>0\). The first step gives
\[
x_1=R,\qquad v_1=S_\theta((1-ak)R).
\]
For \(R>\max\{X,\theta/(ak-2/a)\}\), the denominator is positive because \(k>k_*\) and \(ak_*-2/a=2b^2/a>0\). The threshold is active on the negative branch and
\[
v_1=(1-ak)R+\theta<-cR.
\]
This state lies strictly inside the escape cone, giving exponential divergence in alternating signs. The claimed threshold properties follow.

## Verification

`checker.py` uses only Python's exact-rational standard library. Run `python checker.py`; it checks all antipodal identities, cone transforms, diagonal-start inequalities, and the Schur polynomial identities on 160 rational parameter cases. The source recurrence itself and all crucial algebra are printed above, so the proof does not depend on any numerical test. For a concrete rational instance take \(a=1/2\), \(\mu/h=11\), \(\theta=1/4\). Then \(k_*=10\), \(c=3\), \(X=1/2\), and \((1/2,-3/2)\leftrightarrow(-1/2,3/2)\). Starts \(x_0=v_0=R>1/2\) satisfying the displayed sufficient inequality escape, while sufficiently small states approach zero.

## Relationship to prior work

[1] defines the composite Prox-NAG-GS update, proves convergence under \(h\ge L\), and reports deterministic and stochastic experiments. That sufficient condition covers \(k\le1\) on the current objective, while the present work describes a different, sharp *boundedness-versus-escape* frontier \(k_*(a)>1\), identifies an exact nonzero antipodal cycle for \(k>k_*\), and proves prescribed-start divergence despite local stability. The bounds of [1] alone do not imply these conclusions. [2] studies the smooth NAG-GS quadratic iteration and determines its Schur interval, which agrees with the matrix used for the bounded-input argument above; it has no soft-threshold regularizer, no locally stabilized zero beyond that interval, and no finite-amplitude antipodal threshold cycle. Classical proximal and inertial methods provide context [3,4], but the result is method-specific. It does not claim that the smooth spectral boundary itself is new.

## Limitations

The all-initialization statement below the frontier is only **boundedness**, not convergence. Behavior exactly at \(k=k_*\) is not classified; no all-orbit classification above the frontier is claimed. The unique-cycle assertion covers antipodal cycles, not arbitrary two-cycles. The result assumes positive \(\lambda\); setting \(\lambda=0\) changes local stability and eliminates the finite-amplitude cycle. It does not apply directly to time-varying coupling, multivariate correlated losses, or noise. Source-priority comparisons are qualified by the possibility of older analyses of equivalent piecewise-affine inertial proximal maps.

## References

[1] S. G. Wiykiynyuy, K. A. Ekuri, V. Leplat, *Prox-NAG-GS: A Semi-Implicit Proximal Method for Composite Optimization*, arXiv:2605.26260, first public version May 25, 2026. https://arxiv.org/abs/2605.26260

[2] V. Leplat, D. Merkulov, A. Katrutsa, D. Bershatsky, O. Tsymboi, I. Oseledets, *NAG-GS: A Semi-Implicit Stochastic Optimizer with Large-Step Stability*, arXiv:2209.14937 (originally posted Sep. 29, 2022; revised Oct. 27, 2026). https://arxiv.org/abs/2209.14937

[3] N. Parikh and S. Boyd, *Proximal Algorithms*, Foundations and Trends in Optimization 1 (2014). https://web.stanford.edu/~boyd/papers/prox_algs.html

[4] A. Beck and M. Teboulle, *A Fast Iterative Shrinkage-Thresholding Algorithm for Linear Inverse Problems*, SIAM Journal on Imaging Sciences 2 (2009), 183–202. https://doi.org/10.1137/080716542
