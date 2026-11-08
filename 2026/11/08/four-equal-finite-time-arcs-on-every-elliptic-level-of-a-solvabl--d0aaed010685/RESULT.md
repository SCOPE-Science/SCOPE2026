# Four equal finite-time arcs on every elliptic level of a solvable rational planar flow

## Finding

Consider the real rational vector field
\[
\dot x=\frac{x+a y}{Q(x,y)},\qquad
\dot y=-\frac{y+b x}{Q(x,y)},\qquad
Q(x,y)=p x^2+(ap+bq)xy+q y^2,
\]
with real parameters \(a,b,p,q\), with \((p,q)\ne(0,0)\), on its regular domain \(U=\{(x,y)\in\mathbb R^2:Q(x,y)\ne0\}\). Let
\[
K(x,y)=\frac{p x^2-q y^2}{2}.
\]
For **every** choice of the parameters and every real classical solution in \(U\), the exact identity \(K(x(t),y(t))=K(x(0),y(0))+t\) holds as long as the solution exists. In particular, there are no nonconstant periodic trajectories, no nonempty compact invariant subsets of \(U\), and no invariant probability measures with compact support contained in \(U\).

In the **elliptic parameter region** \(ab>1\), put
\[
\sigma=\operatorname{sgn}(a)=\operatorname{sgn}(b),\quad
H(x,y)=\sigma(bx^2+2xy+ay^2),\quad
\Delta=(ap+bq)^2-4pq.
\]
Then \(H\) is a positive definite first integral, and \(\Delta>0\). Every positive level ellipse \(\{H=h\}\), \(h>0\), meets the singular set \(Q=0\) transversally at exactly four distinct points. Its regular part consists of precisely four complete maximal solution trajectories. **All four trajectories have the same finite original-time lifetime**
\[
\boxed{\mathcal T(h)=\frac{h\sqrt{\Delta}}{2(ab-1)}}.
\]
The value does not depend on the angular position, which of the four components is selected, or the direction of traversal. The four components alternate between \(Q>0\) and \(Q<0\).

Each regular trajectory approaches a finite, nonzero singular point at both ends of its maximal time interval. If \(X_*=(x_*,y_*)\) is either endpoint, \(B=\begin{psmallmatrix}1&a\\-b&-1\end{psmallmatrix}\), and \(q_*=(\nabla Q(X_*))\cdot(BX_*)\), then \(q_*\ne0\) and its sharp endpoint law is
\[
\boxed{\lim_{t\to t_*}\frac{\|X(t)-X_*\|}{\sqrt{|t-t_*|}}
=\|BX_*\|\sqrt{\frac{2}{|q_*|}}.}
\]
Here \(\|\cdot\|\) is the Euclidean norm, and the limit is from within the maximal real-time interval.

## Assumptions and scope

All claims refer to classical **real** solutions of the stated autonomous ODE on \(U\); no extension across \(Q=0\) is part of the original vector field. The exact clock and the compact-recurrence exclusion require only \((p,q)\ne(0,0)\). The four-arc census, common lifetime, and square-root terminal asymptotics additionally require \(ab>1\) and \(h>0\). The nonzero condition on \((p,q)\) excludes an identically vanishing denominator. The origin is never regular because \(Q(0,0)=0\).

## Proof

**1. An exact physical-time clock.** Set
\[
B=\begin{pmatrix}1&a\\-b&-1\end{pmatrix},\qquad X=\binom{x}{y}.
\]
The vector field is \(\dot X=BX/Q(X)\). Direct differentiation gives the exact polynomial identity
\[
\nabla K(X)\cdot BX
=px(x+ay)-qy(-bx-y)=Q(X).
\]
Division by \(Q(X)\) on \(U\) proves \(\dot K=1\). Consequently a periodic solution would give both \(K(t+T)=K(t)\) and \(K(t+T)=K(t)+T\) for \(T>0\), an impossibility. Any entire forward trajectory lying in a compact subset would similarly give an unbounded \(K\) on that compact set. A nonempty compact invariant set cannot exist; for an invariant probability measure with support compact in \(U\), integration of the identity \(\dot K=1\) contradicts stationarity (the generator acts on bounded, differentiable \(K\) on the compact support).

**2. Elliptic auxiliary geometry.** Assume \(ab>1\). Let \(\omega=\sqrt{ab-1}\), \(G=\sigma\begin{psmallmatrix}b&1\\1&a\end{psmallmatrix}\), and \(S=\begin{psmallmatrix}p&(ap+bq)/2\\(ap+bq)/2&q\end{psmallmatrix}\). Then \(G\) is positive definite, \(H(X)=X^TGX\), and \(Q(X)=X^TSX\). The exact identities
\[
B^2=-\omega^2 I,\qquad B^TG+GB=0
\]
show that \(H\) is invariant. Introduce an auxiliary variable \(s\) by \(X'(s)=BX(s)\), for which \(X(s)=\bigl(\cos(\omega s)I+\omega^{-1}\sin(\omega s)B\bigr)X(0)\). Define physical time by \(t'(s)=Q(X(s))\). Wherever \(Q\ne0\) this reconstructs the original ODE by the chain rule, and the direction of increasing physical time reverses on arcs where \(Q<0\).

**3. Four transverse singular intersections.** A direct matrix calculation gives
\[
\operatorname{tr}(G^{-1}S)=0,\quad
\det(G)=ab-1,\quad
\det S=-\frac{\Delta}{4}.
\]
The discriminant is strictly positive because
\[
\Delta=a^2p^2+(2ab-4)pq+b^2q^2
\]
is a positive definite quadratic form in \((p,q)\) when \(ab>1\): its top-left diagonal entry is positive and its determinant is \(4(ab-1)>0\). Thus the two real eigenvalues of the \(G\)-self-adjoint matrix \(G^{-1}S\) are
\[
\lambda_{\pm}=\pm\frac{\sqrt\Delta}{2\omega}.
\]
On \(H=h\), the auxiliary motion is a rigid rotation of angular speed \(\omega\) after a \(G\)-isometry. Consequently, for some phase \(\phi\) depending on the initial point,
\[
Q(X(s))=\frac{h\sqrt\Delta}{2\omega}\cos(2\omega s+\phi).
\]
There are exactly four simple zeros over one full auxiliary ellipse revolution \(2\pi/\omega\); each represents a distinct, transverse nonzero intersection of the ellipse with \(Q=0\). The four complementary open ellipse arcs are the maximal trajectories in \(U\). The transversality is equivalent to the nonzero derivative \(q_*\) at every zero.

**4. Identical original-time lifetimes.** Adjacent zeros of the preceding cosine are separated in auxiliary time by \(\pi/(2\omega)\). On any one of the four arcs, \(Q\) has a fixed sign. Its original-time duration is therefore
\[
\begin{aligned}
\mathcal T(h)
&=\left|\int_{s_-}^{s_+}Q(X(s))\,ds\right|\\
&=\frac{h\sqrt\Delta}{2\omega}\,
  \frac{1}{2\omega}\int_{\pi/2}^{3\pi/2}|\cos u|\,du\\
&=\frac{h\sqrt\Delta}{2\omega^2}
 =\frac{h\sqrt\Delta}{2(ab-1)}.
\end{aligned}
\]
The integral and hence lifetime are independent of the component. Each endpoint is reached in finite physical time. The ODE is undefined there, so no longer classical solution in \(U\) can extend it.

**5. The singular endpoint scaling.** In auxiliary time, near any terminal point at \(s=s_*\), Taylor expansion yields
\[
Q(X(s))=q_*(s-s_*)+O((s-s_*)^2),\quad
X(s)-X_*=BX_*(s-s_*)+O((s-s_*)^2),
\]
where \(q_*\ne0\). Integrating \(t'(s)=Q(X(s))\) shows
\[
|t-t_*|=\frac{|q_*|}{2}|s-s_*|^2+O(|s-s_*|^3).
\]
Since \(BX_*\ne0\) (because \(\det B=ab-1>0\) and \(X_*\ne0\)), eliminating \(s-s_*\) establishes the displayed square-root law. The proof is complete.

## Verification

The standalone file `verify.py` performs seven symbolic matrix and polynomial identity checks using SymPy. It then evaluates, using mpmath at 55-digit precision, the original-time integral on each of four arcs for six distinct parameter choices (24 numerical integral comparisons, including negative \(a,b\) and mixed-sign \(p,q\)). The checker passed all 31 checks. To reproduce with Python 3 and installed `sympy`, `mpmath`, run `python verify.py` from this package's extracted directory. The finite comparisons corroborate, but do not replace, the all-parameter analytic proof above.

## Relationship to prior work

Calogero and Payandeh (2022, arXiv:2209.05113), equations (1)–(3), introduce **exactly this rational vector field** (their \(\alpha_1=a\), \(\alpha_2=b\), \(\beta_1=p\), \(\beta_2=q\)) and give its explicit initial-value solutions as combinations of two radicals. They explicitly mention possible square-root singularities. Their paper does **not state** the exact global clock \(\dot K=1\), the entire elliptic real phase-portrait decomposition into four singular arcs, their equal maximal original-time lengths, or the endpoint coefficient. These are additional geometric and physical-time conclusions, not a reassertion of algebraic solvability.

Calogero and Payandeh's other 2022 article in *Theoretical and Mathematical Physics* discusses broader homogeneous solvable ODE families and some periodic variants, with particular explicit solutions under parameter/initial-data constraints. Its inspected relevant statements do not present the above full four-parameter rational flow's equal-flight-time theorem. The exact conclusion is specific to the coefficient relation in this model. The more general assertion that a rationally time-changed linear rotation can hit its singular set is not, by itself, an equal-duration formula for all four components.

## Limitations

No classification is claimed when \(ab\le1\), beyond the exact clock and recurrence exclusion. At the singular points, the ODE does not prescribe a continuation or a generalized Filippov flow; this theorem does not define one. No statement of uniqueness relative to every unpublished or unindexed result is possible. The equal-lifetime identity is a conclusion for the original four-parameter family and not for arbitrary quadratic time changes of linear centers. Independent mathematical audit has not been performed.

## References

1. F. Calogero and F. Payandeh, *New solvable systems of 2 first-order nonlinearly-coupled ordinary differential equations*, Open Communications in Nonlinear Mathematical Physics **2** (2022), 102–105, arXiv:2209.05113, https://arxiv.org/abs/2209.05113, https://doi.org/10.46298/ocnmp.10067. Public preprint dated 2022-09-12.
2. F. Calogero and F. Payandeh, *Explicitly solvable systems of first-order ordinary differential equations with homogeneous right-hand sides, and their periodic variants*, Theoretical and Mathematical Physics **213** (2022), 1317–1330, https://doi.org/10.1134/S0040577922100026. MathNet full text https://www.mathnet.ru/eng/tmf10222.
