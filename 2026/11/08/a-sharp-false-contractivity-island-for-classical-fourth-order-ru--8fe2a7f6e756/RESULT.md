# A sharp false-contractivity island for classical fourth-order Runge–Kutta on planar Jordan shears

## Finding

Let \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\) and \(A_\gamma=-I+\gamma N\) for \(\gamma\ge0\). Write \(P_4(z)=\sum_{j=0}^4 z^j/j!\). The classical RK4 one-step matrix \(T_{h,\gamma}=P_4(hA_\gamma)\), with step \(h\ge0\), is **Euclidean contractive** exactly on the following sets:

- If \(0\le\gamma\le2\), then \(\|T_{h,\gamma}\|_2\le1\) if and only if \(0\le h\le h_+(\gamma)\).
- If \(\gamma>2\), then \(\|T_{h,\gamma}\|_2\le1\) if and only if \(h=0\) or \(h_-(\gamma)\le h\le h_+(\gamma)\).

Here \(\beta\in(2,3)\) is the unique positive root of \(\beta^3-4\beta^2+12\beta-24=0\), and \(\zeta\in(1,2)\) is the unique positive root of \(1-\zeta+\zeta^2/2-\zeta^3/6=0\). Define

\[
r(h)=1-h+\frac{h^2}{2}-\frac{h^3}{6}+\frac{h^4}{24},\qquad
q(h)=1-h+\frac{h^2}{2}-\frac{h^3}{6},\qquad
\Phi(h)=\frac{1-r(h)^2}{h|q(h)|}.
\]

For \(\gamma>2\), \(h_-(\gamma)\in(0,\zeta)\) is the unique solution of \(\Phi(h)=\gamma\) on that interval. For every \(\gamma>0\), \(h_+(\gamma)\in(\zeta,\beta)\) is the unique solution of \(\Phi(h)=\gamma\) on that interval; set \(h_+(0)=\beta\) and \(h_-(\gamma)=0\) for \(0\le\gamma\le2\). More precisely, \(\Phi\) is strictly increasing from \(2\) to \(+\infty\) on \((0,\zeta)\), and strictly decreasing from \(+\infty\) to \(0\) on \((\zeta,\beta)\).

The time-continuous semigroup \(e^{tA_\gamma}\) is contractive for all \(t\ge0\) if and only if \(\gamma\le2\). Thus for **every** \(\gamma>2\), the RK4 numerical step is noncontractive at all sufficiently small positive steps, yet is contractive over a nonempty, sharply determined intermediate interval. At the common center \(h=\zeta\) the RK4 update is exactly \(r(\zeta)I\), independent of \(\gamma\), with \(r(\zeta)\approx0.270394765205184\). Nevertheless \(\|e^{\zeta A_\gamma}\|_2\to\infty\) as \(\gamma\to\infty\).

The endpoints have sharp scaling laws:

\[
h_-(\gamma)=\sqrt{3(\gamma-2)}+O((\gamma-2)^{3/2})
\quad(\gamma\downarrow2),
\]

and, with \(C=(1-r(\zeta)^2)/(\zeta|q'(\zeta)|)\approx0.856975420961165\),

\[
h_\pm(\gamma)=\zeta\pm\frac{C}{\gamma}+O(\gamma^{-2})
\quad(\gamma\to\infty),
\]

where the minus sign corresponds to \(h_-\). In particular, the spurious contraction interval has width \(2C/\gamma+O(\gamma^{-2})\) for large shear.

## Assumptions and scope

All matrices and vector spaces are real, all norms are Euclidean operator norms, \(\gamma\ge0\), and \(h\ge0\). This is a one-step operator-norm result for the classical four-stage, fourth-order explicit Runge–Kutta method on the fixed family of \(2\times2\) defective, exponentially stable matrices \(A_\gamma=-I+\gamma N\). The statement is not about positivity, algebraic stability, relative error, internal RK stages, or arbitrary nonnormal matrices. The eigenvalues of \(A_\gamma\) are both \(-1\), irrespective of \(\gamma\).

## Proof

**1. Exact reduction to an upper-triangular norm.** Since \(N^2=0\), polynomial functional calculus gives

\[
P_4(hA_\gamma)=P_4(-h)I+\gamma hP_4'(-h)N
=r(h)I+\gamma hq(h)N.
\]

For real \(a,d\), direct singular-value calculation (or positivity of \(I-T^\mathsf{T}T\)) gives

\[
\left\|\begin{pmatrix}a&d\\0&a\end{pmatrix}\right\|_2
=\frac{\sqrt{4a^2+d^2}+|d|}{2},
\qquad
\|T\|_2\le1\iff a^2+|d|\le1.
\]

The second equivalence follows by squaring the first expression after checking its nonnegative right side. Hence the exact RK4 criterion is

\[
r(h)^2+\gamma h|q(h)|\le1.
\tag{1}
\]

**2. The relevant scalar interval.** The identity

\[
24r(h)=(h^2-2h+2)^2+4((h-2)^2+1)>0
\]

proves strict positivity of \(r\). Moreover

\[
24(r(h)-1)=h\,(h^3-4h^2+12h-24).
\]

The cubic in parentheses is strictly increasing, since its derivative \(3h^2-8h+12\) is positive for every real \(h\); it crosses zero precisely once at \(\beta\in(2,3)\). Thus \(r(h)^2\le1\) exactly for \(h\in[0,\beta]\). Also

\[
q'(h)=-(1-h+h^2/2)<0,
\]

so \(q\) has one simple zero \(\zeta\in(1,2)\), with \(q>0\) to the left and \(q<0\) to the right. At \(h=\zeta\), (1) holds for every \(\gamma\), since \(q(\zeta)=0\) and \(0<r(\zeta)<1\).

**3. Uniqueness and the global phase diagram.** For \(0<h<\beta\) and \(h\ne\zeta\), criterion (1) is equivalent to \(\gamma\le\Phi(h)\). Set \(\Psi(h)=(1-r(h)^2)/(hq(h))\), with sign retained. Exact differentiation yields

\[
\Psi'(h)=\frac{h^3 B(h)}{3456(hq(h))^2},
\]

where

\[
\begin{aligned}
B(h)={}&4h^8-39h^7+212h^6-786h^5+2112h^4\\
&-4176h^3+5760h^2-4608h+2304.
\end{aligned}
\]

A completely positive polynomial certificate proves \(B(h)>0\) on \((0,3)\). Let \(t=h/(3-h)>0\), so \(h=3t/(1+t)\); direct expansion gives

\[
\begin{aligned}
(1+t)^8 B\!\left(\frac{3t}{1+t}\right)
={}&2304+4608t+19584t^2+37008t^3+62352t^4\\
&+47754t^5+32274t^6+4041t^7+3141t^8>0.
\end{aligned}
\]

Hence \(\Psi'>0\) for all \(0<h<\beta\), \(h\ne\zeta\). Since \(q\) changes sign at \(\zeta\), \(\Phi=\Psi\) strictly increases on \((0,\zeta)\), and \(\Phi=-\Psi\) strictly decreases on \((\zeta,\beta)\). Direct limits give \(\Phi(0+)=2\), \(\Phi(\zeta\pm)=+\infty\), and \(\Phi(\beta-)=0\). Thus the level sets \(\gamma\le\Phi(h)\) have precisely the asserted topology, with \(h=0\) always an isolated solution for \(\gamma>2\). This proves the exact classification for all \(h,\gamma\) in scope.

**4. The physical semigroup and spurious contraction.** As \(N^2=0\),

\[
e^{tA_\gamma}=e^{-t}(I+\gamma tN),\qquad
\|e^{tA_\gamma}\|_2=e^{-t}\frac{\sqrt{4+\gamma^2t^2}+\gamma t}{2}.
\]

For \(t>0\), the logarithmic derivative of this norm equals \(-1+\gamma/\sqrt{4+\gamma^2t^2}\). It is nonpositive at every time exactly when \(\gamma\le2\), and it is positive at sufficiently small times for \(\gamma>2\). At \(t=h=\zeta\), the RK4 polynomial instead annihilates the \(N\) coefficient, yielding \(r(\zeta)I\); the exact semigroup norm grows linearly as \(e^{-\zeta}\gamma\zeta\) for large \(\gamma\).

**5. Sharp endpoint laws.** Exact Taylor division near zero gives

\[
\Phi(h)=2+\frac{h^2}{3}+O(h^4),\qquad h\downarrow0.
\]

The increasing branch therefore has \(h_-(\gamma)=\sqrt{3(\gamma-2)}+O((\gamma-2)^{3/2})\) as \(\gamma\downarrow2\). Since \(q'(\zeta)\ne0\), the singular expansion near \(\zeta\) is

\[
\Phi(h)=\frac{C}{|h-\zeta|}+O(1),\qquad
C=\frac{1-r(\zeta)^2}{\zeta|q'(\zeta)|}>0.
\]

Inversion on each monotone branch gives \(h_\pm(\gamma)=\zeta\pm C/\gamma+O(\gamma^{-2})\), completing the proof.

## Verification

The standalone, standard-library-only `verify.py` checks the rational polynomial identities; the positive transform's nine integer coefficients; the first five Taylor coefficients; all specified root brackets; and 13,000+ direct comparisons between the sharp criterion and independently computed singular norms on a parameter grid. It also checks numerical root and asymptotic values. Invoke it with `python3 verify.py` from the directory containing this file. All infinite and universal claims in the finding follow from the displayed analytic argument, not from finite grid tests. Computed numerical benchmarks: \(\zeta\approx1.596071637983319\), \(\beta\approx2.785293563405282\), \(C\approx0.856975420961165\); at \(\gamma=4\), \((h_-,h_+)\approx(1.308291193571,1.772631404754)\).

## Relationship to prior work

General RK spectral and strong-stability theory is developed in Tadmor [1], Sun--Shu [2,3], and Achleitner--Arnold--Jüngel [4]. Tadmor explicitly discusses Jordan-block failure of spectral-only arguments for method-of-lines stability. Sun and Shu show that RK4 can fail one-step strong stability on semidissipative linear systems, including a three-state counterexample. Achleitner and collaborators establish structural conditions and limitations for RK4 strong stability on entire classes of semidissipative matrices. None of the inspected passages supplies the present exact two-state \(\gamma\)-dependent Euclidean one-step region, its detached intermediate-step component for nondissipative systems, or its two endpoint scaling laws. The classical scalar RK4 stability interval \([0,\beta]\), the exact \(2\times2\) shear norm identity, and qualitative sensitivity to Jordan blocks are not claimed new on their own. A prior result on continuous-time \(L^p\) contractivity of triangular shears gives a related but different physical-semigroup criterion, not this discrete RK4 classification.

## Limitations

This does not establish that deliberately choosing a numerically contractive intermediate step improves approximation. Indeed, for large \(\gamma\) the exact solution norm can be arbitrarily larger than the RK4 norm at \(h=\zeta\): contraction here can be deceptive. The theorem concerns only the classical fourth-order stability polynomial and the fixed real \(2\times2\) Jordan family, and does not imply a universal RK4 strong-stability theorem. More specialized earlier studies could independently contain the same exact phase diagram; publication priority is not claimed conclusively. The symbolic positive-coefficient identity and numerical tests are independently reproducible; a separate human/external audit has not been performed.

## References

[1] E. Tadmor, *Runge--Kutta methods are stable*, arXiv:2312.15546v1 (first public 2023-12-24), https://arxiv.org/html/2312.15546v1 .

[2] Z. Sun and C.-W. Shu, *Stability of the fourth order Runge--Kutta method for time-dependent partial differential equations*, Annals of Mathematical Sciences and Applications 2 (2017), 255--284, https://intlpress.com/site/pub/files/_fulltext/journals/amsa/2017/0002/0002/AMSA-2017-0002-0002-a003.pdf .

[3] Z. Sun and C.-W. Shu, *Strong stability of explicit Runge--Kutta time discretizations*, SIAM Journal on Numerical Analysis 57 (2019), 1158--1182; arXiv:1811.10680, https://arxiv.org/abs/1811.10680 .

[4] F. Achleitner, A. Arnold and A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge--Kutta methods*, arXiv:2308.05689 (2023), https://arxiv.org/abs/2308.05689 .
