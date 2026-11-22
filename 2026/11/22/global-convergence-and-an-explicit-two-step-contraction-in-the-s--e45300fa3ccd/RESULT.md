# Global convergence and an explicit two-step contraction in the supercritical two-player maxima map

## Finding

For every real parameter \(\alpha>2\), the two-player maxima map of Satur [1] has **global winner–loser convergence from every off-diagonal interior initial condition**. If the first coordinate initially exceeds the second, its limit is the asymmetric fixed point
\[
(x_*,y_*)=\left(1-\frac{1}{\alpha(\alpha-1)^2},\ 1-\frac1\alpha\right).
\]
The reversed initial order gives the reversed limit. The larger coordinate always retains its ordering; the first component always follows the preserving branch, while the smaller component enters the switching branch in finite time and never leaves it. A concrete finite-time bound and a global two-step contraction in logarithmic odds are proved below. This supplies a rigorous global-attraction statement for the parameter region that [1, §3, after Theorem 3] explicitly leaves open.

## Assumptions and scope

Fix \(\alpha>2\). The map acts on the square \([1/2,1)^2\), and its coordinates are
\[
\Phi_\alpha(x,y)=\left(
\frac{\max\{\alpha x(1-y),1-x\}}{\alpha x(1-y)+1-x},
\frac{\max\{\alpha y(1-x),1-y\}}{\alpha y(1-x)+1-y}
\right).
\]
The theorem concerns **all** initial \((x_0,y_0)\in(1/2,1)^2\) with \(x_0\ne y_0\) (not merely almost all such points). It concerns the maxima map, not convergence of a spatially extended system. The invariant diagonal and initial values with coordinates equal to \(1\) are excluded. The boundary \(1/2\) may be attained transiently; the map is defined there and this presents no problem.

Assume first that \(x_0>y_0\), put
\[
z_t=\frac{1-x_t}{x_t},\qquad w_t=\frac{1-y_t}{y_t},\qquad r_t=\frac{w_t}{z_t},
\]
and define the smaller coordinate's branch ratio
\[
R_y(t)=\frac{\alpha z_t}{w_t(1+z_t)}.
\]
Let \(T\) be the first nonnegative integer with \(R_y(T)\le1\). It exists and obeys
\[
T\le T_0:=\max\left\{0,\left\lceil\frac{\log((\alpha-1)/(r_0-1))}{\log(3/2)}\right\rceil\right\}.
\]
At every \(t\ge T\), the branch formulas are
\[
z_{t+1}=\frac{z_t(1+w_t)}{\alpha w_t},\qquad
w_{t+1}=\frac{\alpha z_t}{w_t(1+z_t)}.
\]
Let
\[
z_*=\frac{1}{\alpha(\alpha-1)^2-1},\quad w_*=\frac{1}{\alpha-1},\quad
U_t=\log z_t,\quad V_t=\log w_t,\quad U_*=\log z_*,\quad V_*=\log w_*.
\]
Define the finite norm of deviations (with \(D_t=(U_t-U_*)-(V_t-V_*)\))
\[
N_t=\max\{|U_t-U_*|,\ |V_t-V_*|,\ |D_t|\}.
\]
Then for every integer \(t\ge T\),
\[
N_{t+1}\le N_t,\qquad
N_{t+2}\le c_\alpha N_t,\qquad
c_\alpha=\frac34+\frac{1}{2\alpha}<1.
\]
In particular, \(N_{T+k}\le c_\alpha^{\lfloor k/2\rfloor}N_T\) for all integers \(k\ge0\). The same assertions hold after swapping the two coordinate names when \(x_0<y_0\).

## Proof

**Step 1. Exact branch geometry and order preservation.** With \(x>y\), the odds satisfy \(0<z<w\le1\). The active-versus-passive numerator ratios for the two coordinates are
\[
R_x=\frac{\alpha w}{z(1+w)},\qquad
R_y=\frac{\alpha z}{w(1+z)}.
\]
Since \(w>z\),
\[
R_x>\frac\alpha{1+w}\ge\frac\alpha2>1,\qquad R_x>R_y,
\qquad R_xR_y=\frac{\alpha^2}{(1+z)(1+w)}>1.
\]
The new odds for each coordinate are \(\min\{R,1/R\}\). If \(R_y\ge1\), the first coordinate's new odds are \(1/R_x\), while the second coordinate's are \(1/R_y\); their order follows from \(R_x>R_y\). If \(R_y\le1\), the new odds are \(1/R_x\) and \(R_y\), respectively; their order follows from \(R_xR_y>1\). Thus \(0<z_{t+1}<w_{t+1}\le1\) for all times, including at a branch tie. In particular, the initially larger maximum stays larger, and its own active numerator is always strictly dominant.

**Step 2. Finite entry into the smaller coordinate's switching branch.** Whenever \(R_y>1\), both active numerators dominate. The odds evolve as
\[
z'=\frac{z(1+w)}{\alpha w},\qquad
w'=\frac{w(1+z)}{\alpha z}.
\]
For \(r=w/z>1\), the exact identity is
\[
r'=r^2\frac{1+z}{1+w},\qquad
r'-1=(r-1)\left(1+\frac{r}{1+w}\right)\ge\frac32(r-1),
\]
where the last inequality uses \(r>1\) and \(w\le1\). Once \(r\ge\alpha\),
\[
R_y=\frac\alpha{r(1+z)}<1.
\]
If the smaller coordinate were not yet switching after \(T_0\) steps, the previous growth inequality would force \(r_{T_0}-1\ge(3/2)^{T_0}(r_0-1)\ge\alpha-1\), hence \(R_y(T_0)<1\), a contradiction. This proves the explicit bound for \(T\), including the case \(T_0=0\).

**Step 3. Switching is permanent.** If \(R_y\le1\), the new odds are precisely
\[
z'=\frac{z(1+w)}{\alpha w},\qquad w'=\frac{\alpha z}{w(1+z)}.
\]
The following step's ratio is
\[
R_y'=\frac{\alpha z'}{w'(1+z')}=\frac{(1+w)(1+z)}{\alpha(1+z')}.
\]
The denominator exceeds its numerator, since
\[
\alpha(1+z')-(1+w)(1+z)
=\alpha-(1+w)+\frac{z(1+w)(1-w)}{w}
\ge\alpha-2>0.
\]
Thus \(R_y'<1\), proving permanent entry. Further, \(R_y\le1\) implies \(z\le w/(\alpha-w)\le1/(\alpha-1)\), while \(0<w\le1\) always. These bounds hold for both the orbit and the asymmetric fixed point below.

**Step 4. Fixed point and contraction.** Substitution shows that
\[
w_*=\frac1{\alpha-1},\qquad z_*=\frac1{\alpha(\alpha-1)^2-1}
\]
is fixed by the displayed switched-branch formulas and satisfies the same branch inequalities. In log odds, that branch is
\[
F(U,V)=\left(U-V+\log(1+e^V)-\log\alpha,
                  U-V+\log\alpha-\log(1+e^U)\right).
\]
Compare one orbit point with the fixed point, writing \(u=U-U_*\), \(v=V-V_*\), and \(d=u-v\). The mean value theorem gives numbers \(a,b\) such that
\[
u'=(1-a)u+ad,\qquad v'=bd-(1-b)v,
\qquad d'=(1-b)u+(1-a)v,
\]
with
\[
a=\frac1{1+e^{\xi_V}}\in[1/2,1],\qquad
b=\frac1{1+e^{\xi_U}}\in[(\alpha-1)/\alpha,1].
\]
Here the intermediate logs are on segments between orbit and fixed-point logs, so their bounds follow from \(w,w_*\le1\) and \(z,z_*\le1/(\alpha-1)\). For \(N=\max\{|u|,|v|,|d|\}\), these three identities give
\[
|u'|\le N,\quad |v'|\le N,\quad |d'|\le q_\alpha N,
\quad q_\alpha=\frac12+\frac1\alpha<1.
\]
Apply them again. Both \(u''\) and \(v''\) are convex combinations in absolute value of a quantity bounded by \(N\) and a quantity bounded by \(q_\alpha N\), with the coefficient of the latter at least \(1/2\). Hence
\[
\max\{|u''|,|v''|\}\le\frac{1+q_\alpha}{2}N.
\]
Also \(|d''|\le q_\alpha N\). Since \(q_\alpha\le(1+q_\alpha)/2\), we obtain the claimed two-step estimate with \(c_\alpha=(1+q_\alpha)/2=3/4+1/(2\alpha)\). Its strict inequality \(c_\alpha<1\) follows from \(\alpha>2\). Iteration proves convergence to the fixed point in log odds, hence in \((x,y)\). Finally, coordinate exchange symmetry proves the assertion for \(x_0<y_0\). \(\square\)

## Verification

The accompanying `CHECK.py` uses exact rational arithmetic to verify the original map and reciprocal-odds branch identities, the switching-time bound, and permanent switching for hundreds of nontrivial starting points. Separate floating-point comparisons verify the quantitative two-step estimate against the fixed point for 12,000 independent parameter/initial-value tests, including parameters approaching the boundary \(\alpha=2\). These finite computations verify examples and detect implementation mistakes but are not substituted for the all-parameter proof in the preceding section. Run from the package directory using `python CHECK.py` (Python standard library only).

## Relationship to prior work

Satur [1] introduced the maxima map, derived the asymmetric fixed points, proved their **local** asymptotic stability for \(\alpha>2\) (Theorem 3), and explicitly noted that a rigorous proof of **global** convergence for \(\alpha>2\) remained open (paragraph following that theorem). The present result preserves the original model and fixed points while proving convergence from every off-diagonal interior initial point, a finite branch-selection time, and a fully uniform rate after switching. The previously studied critical case \(\alpha=2\) is a distinct dynamical regime and is not extended by merely substituting a new parameter into its proof. Other studies of max-type difference equations may use related transformations, but no equivalent theorem for this specific map was established in the inspected literature. Priority should be checked independently before publication.

## Limitations

No claim is made for the diagonal \(x_0=y_0\), for initial maxima equal to \(1\), or for \(\alpha\le2\). The contraction rate is a valid explicit global upper bound, not asserted to be the sharp asymptotic multiplier or the shortest possible transient bound. The exact fixed-point expressions originate in [1]. The extension to original two-component probability vectors follows their model where dominant components remain identifiable, but no claim here resolves a positional tie in the original vectors. Independent mathematical verification and exhaustive historical priority verification have not been performed.

## References

[1] O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1, first posted November 9, 2026, https://arxiv.org/abs/2611.13318 . See equation (1), Lemma 2, Theorem 3, and the paragraph following Theorem 3.

[2] Published published-finding corpus record, *Nonlinear critical-collapse amplitudes and a quadratic phase law in two-player maxima dynamics*, November 17, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-nonlinear-critical-collapse-amplitudes-and-a-quadratic-phase-law--8b71d315903b . This treats the critical parameter \(\alpha=2\) rather than supercritical global attraction.
