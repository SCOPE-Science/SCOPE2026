# Cubic onset of the positive-observation region in an immigrating predator–prey map

## Finding

Consider the discrete map
\[
F(x,y)=\bigl(r x(1-x)-a x y+s,\;y(bx-d)\bigr),
\qquad r,a,b,d,s>0.
\]
Write \(t=d/b>1\), \(s_c=rt(t-1)\), and \(\varepsilon=s-s_c\). Let \(\mathcal I_s=F((0,\infty)^2)\cap(0,\infty)^2\), the set of **strictly positive one-step observations from strictly positive states**, and let \(A_s\) be its planar Lebesgue area.

**Theorem.** If \(s\le s_c\), then \(\mathcal I_s=\varnothing\) and \(A_s=0\). If \(\varepsilon>0\), put \(q=2t-1\) and
\[
R_t(u)=2qu+(5-t^{-1})u^2+2t^{-1}u^3,
\quad
Y_f(u)=\frac{rb}{at}(q+2u)u^2.
\]
For each \(X\in(0,\varepsilon)\), there exists a unique \(u_X>0\) with \(rR_t(u_X)=\varepsilon-X\). Then the positive observation set is **exactly**
\[
\mathcal I_s=\{(X,Y):0<X<\varepsilon,\quad0<Y\le Y_f(u_X)\}.
\]
Every target with \(0<Y<Y_f(u_X)\) has exactly **two distinct strictly positive** predecessors, every target on the upper fold \(Y=Y_f(u_X)\) has exactly **one**, and every target in the positive quadrant outside \(\mathcal I_s\) has **none**.

Let \(u_*>0\) be the unique root of \(rR_t(u_*)=\varepsilon\), and set
\[
P_t(u)=\frac{2q^2}{3}u^3+\frac{q(7-t^{-1})}{2}u^4
+\left(\frac{32}{5}-\frac2t\right)u^5+\frac2t u^6.
\]
The area has the **exact** formula and sharp threshold law
\[
\boxed{\displaystyle
A_s=\frac{r^2b}{at}P_t(u_*),\qquad
A_s=\frac{b}{12atr(2t-1)}\varepsilon^3+O_{r,a,b,d}(\varepsilon^4)
\quad(\varepsilon\downarrow0).}
\]
In rescaled observation variables \(U=X/\varepsilon\) and \(V=atr(2t-1)Y/(b\varepsilon^2)\), the closed positive-observation regions converge, with uniformly convergent upper boundaries, to
\[
0\le U\le1,\qquad0\le V\le(1-U)^2/4.
\]
For each fixed interior point \(0<U<1\), \(0<V<(1-U)^2/4\), its two predecessors have the limits
\[
\frac{r(2t-1)(x_\pm-t)}{\varepsilon}\longrightarrow
\frac{1-U\pm\sqrt{(1-U)^2-4V}}2,
\qquad
\frac{at y_\pm}{\varepsilon}\longrightarrow
\frac{1-U\mp\sqrt{(1-U)^2-4V}}2.
\]

## Assumptions and scope

Parameters \(r,a,b,d,s\) are fixed positive reals except when the immigration rate \(s\) approaches \(s_c\) from above; the strict assumption \(t=d/b>1\) is essential to this threshold theorem. Predecessors and observations are counted only in \((0,\infty)^2\). The result is an exact **one-step** inverse and image classification; it does not assert that every positive predecessor generates a trajectory remaining positive for all future times.

## Proof

**1. The sharp threshold.** A strictly positive predator observation \(Y=y(bx-d)>0\) from \(y>0\) forces \(x>t\). Set \(u=x-t>0\). Then
\[
g(t+u):=r(t+u)(1-t-u)+s
=\varepsilon-r(2t-1)u-ru^2=\varepsilon-rqu-ru^2.
\]
Since \(q>1\), \(g(t+u)<\varepsilon\) for all \(u>0\). The prey observation is \(X=g(t+u)-a(t+u)y<g(t+u)\). Hence no strictly positive observation exists when \(\varepsilon\le0\); when \(\varepsilon>0\), necessarily \(0<X<\varepsilon\). Conversely small \(u,y>0\) give both observations positive when \(\varepsilon>0\).

**2. Exact inverse census.** For a target \((X,Y)\) with \(Y>0\), every strictly positive predecessor must satisfy
\[
y=\frac{Y}{bu},\qquad
X=H_Y(u):=\varepsilon-rqu-ru^2-\frac{a(t+u)Y}{bu},\quad u>0.
\]
Differentiation yields
\[
H'_Y(u)=-rq-2ru+\frac{atY}{bu^2},\qquad
H''_Y(u)=-2r-\frac{2atY}{bu^3}<0.
\]
Also \(H_Y(u)\to-\infty\) at both \(u\downarrow0\) and \(u\to\infty\). Thus \(H_Y\) has a unique strict maximum and each horizontal level intersects it twice, once or never, according to whether it lies strictly below, at or above that maximum. The maximum decreases strictly with \(Y\), since \(H_Y(u)\) decreases at every \(u\). As \(Y\downarrow0\), it tends to \(\varepsilon\); as \(Y\to\infty\), it tends to \(-\infty\). Consequently, for every \(0<X<\varepsilon\), there is exactly one fold height, below which exactly two positive inverse states occur.

**3. Parameterization of the full fold.** Solve \(H'_Y(u)=0\):
\[
Y=Y_f(u)=\frac{rb}{at}(q+2u)u^2.
\]
Substitution gives
\[
X=X_f(u)=\varepsilon-r\left[2qu+(5-t^{-1})u^2+2t^{-1}u^3\right]=\varepsilon-rR_t(u).
\]
Since
\[
R'_t(u)=\frac{2(t+u)(2t+3u-1)}t>0\qquad (u\ge0,t>1),
\]
this parameterization runs once through the complete strictly positive caustic \(0<X<\varepsilon\). Its endpoint \(X=0\) occurs at unique \(u_*\). By the strict-concavity result, this is the sole boundary of the positive target image away from the coordinate axes, with the claimed inverse multiplicities. The Jacobian
\[
\det DF(x,y)=rb(1-2x)(x-t)+ad y
\]
vanishes precisely at the same fold. Its nonzero second derivative in the inverse variable confirms a regular quadratic fold at all \(u>0\).

**4. Exact area and threshold exponent.** The fold bounds the observation region vertically, so by the substitution \(X=X_f(u)\),
\[
A_s=\int_0^\varepsilon Y_f(u_X)\,dX
=\frac{r^2b}{at}\int_0^{u_*}(q+2u)u^2R'_t(u)\,du.
\]
Direct polynomial integration gives \(P_t(u_*)\) as stated. The defining cubic equation implies
\[
u_*=\frac{\varepsilon}{2rq}+O(\varepsilon^2),
\]
whence \(P_t(u_*)=2q^2u_*^3/3+O(u_*^4)\) proves the exact cubic-area coefficient and its \(O(\varepsilon^4)\) remainder.

**5. Universal limiting geometry.** The inverse relation \(rR_t(u_X)=\varepsilon(1-U)\) gives \(u_X=\varepsilon(1-U)/(2rq)+O(\varepsilon^2)\) uniformly for \(U\in[0,1]\). The rescaled fold height is therefore \(V_f(U)=(1-U)^2/4+O(\varepsilon)\) uniformly. For a fixed strict interior target, write \(u=\varepsilon\xi/(rq)\), \(y=\varepsilon\eta/(at)\). The two inverse equations become \(U=1-\xi-\eta+O(\varepsilon)\), \(V=\xi\eta\), uniformly on bounded positive scaled pairs. Their two distinct positive limiting solutions are the displayed roots, and the implicit-function theorem gives their persistence and limits away from the discriminant-zero boundary. This completes the proof.

## Verification

The accompanying standalone program `check.py` exactly verifies the fold identities, Jacobian identity, area primitive and limiting cubic coefficient using symbolic algebra. It also checks three positive parameter witnesses by independent numerical quadrature and inverse-root reconstruction. These computational tests are corroboration; all quantifiers and the continuum-area identity are established analytically above.

## Relationship to prior work

Kangalgil and Işık (2022) introduce exactly this prey-immigration map and study positive equilibria, stability, flip and Neimark–Sacker bifurcations. Their results do not state its complete strictly positive one-step image, two-sheet inverse census, exact image area or cubic immigration-onset law. Djellit, Sahari and Hachemi (2013) analyze inverse singularities and feasible basins for the related but different map without predator mortality or constant immigration, \((x,y)\mapsto(\alpha x(1-x)-\beta xy,\gamma xy)\); that study supplies relevant conceptual background rather than the stated threshold or coefficient. Standard generic critical-curve theory describes local two-sheet folds, but by itself does not give this model's global positive-observation region or its exact immigration-dependent area.

## Limitations

The assumption \(d/b>1\) is not relaxed. Coordinate-axis targets and their potentially different predecessor multiplicities are excluded. The target-area measure uses ordinary planar Lebesgue area in population-density coordinates, which depends on those units. The limiting caustic is not asserted to describe invariant sets, invariant measures, global ecological persistence, dynamics at later steps, or cryptographic properties. An unindexed prior equivalent formula remains possible; no independent audit has been performed.

## References

1. F. Kangalgil and S. Işık, *Effect of immigration in a predator-prey system: Stability, bifurcation and chaos*, AIMS Mathematics 7(8) (2022), 14354–14375, first published 2022-06-02, https://doi.org/10.3934/math.2022791 . Open full text: https://www.aimspress.com/aimspress-data/math/2022/8/PDF/math-07-08-791.pdf .
2. I. Djellit, M. L. Sahari and A. Hachemi, *Complex dynamics in 2-species predator-prey systems*, Journal of Applied Analysis and Computation 3(1) (2013), 11–20. Public full-text rendering: https://www.academia.edu/3749405/COMPLEX_DYNAMICS_IN_2_SPECIES_PREDATOR_PREY_SYSTEMS .
3. J. P. England, B. Krauskopf and H. M. Osinga, *Bifurcations of stable sets in noninvertible planar maps*, International Journal of Bifurcation and Chaos 15(3) (2005), 891–904, https://doi.org/10.1142/S0218127405012466 .
