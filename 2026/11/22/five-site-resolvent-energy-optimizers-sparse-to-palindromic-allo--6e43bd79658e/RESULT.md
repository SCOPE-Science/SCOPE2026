# Five-site resolvent energy optimizers: sparse-to-palindromic allocation

## Finding
Let \(S\) be a nilpotent weighted shift on \(\mathbb C^5\), with \(Se_j=w_j e_{j+1}\) for \(1\le j\le4\) and \(Se_5=0\). The complex weights may vanish. Fix any energy \(E=\sum_{j=1}^4|w_j|^2>0\). We determine the largest squared Hilbert–Schmidt norm of its resolvent \(R=(I-S)^{-1}\), together with **every** optimizing weight-magnitude profile.

Define
\[
 y_E=\frac{E-4+\sqrt{E^2+4E+16}}6,\qquad B(E)=y_E(y_E+2)(E-2y_E).
\]
Set \(s=E/2\). There is exactly one \(u_E\in(0,s)\) satisfying
\[
 (u_E+1)(s-u_E)^2-u_E(u_E+2)(s-u_E)-u_E=0.
\]
Set \(v_E=s-u_E\) and
\[
 P(E)=s^2-u_E^2+u_E(u_E+2)v_E^2.
\]
Then the sharp value is
\[
 \boxed{\max_{\sum |w_j|^2=E}\|R\|_{S_2}^{\,2}=5+E+\max\{B(E),P(E)\}.}
\]
If \(B(E)>P(E)\), the **only** squared-magnitude profiles of maximizers are
\[
 (y_E,E-2y_E,y_E,0),\qquad(0,y_E,E-2y_E,y_E).
\]
If \(P(E)>B(E)\), the **only** profile is
\[
 (u_E,v_E,v_E,u_E).
\]
At equality, precisely the union of these profiles maximizes. Every assignment of complex phases to nonzero weights is allowed. In particular, the optimizing support is asymmetric and has three consecutive active edges for \(0<E<3/8\), whereas the unique profile is palindromic and has four active edges for \(E\ge10\). Thus at least one genuine support/symmetry transition occurs as the energy increases. No uniqueness of the transition energy is asserted.

## Assumptions and scope
The norm is the Schatten \(S_2\) (Frobenius, Hilbert–Schmidt) norm on \(\mathbb C^5\). The constraint is equality of the squared Frobenius norm of \(S\) to \(E>0\), not a spectral-norm or fixed-multiset constraint. All weights are finite complex numbers, zero weights are admissible, and \(R\) always exists because \(S^5=0\). The classification is exact for every real \(E>0\), including possible ties between the two explicit branches.

## Proof
**1. Resolvent energy is a consecutive-products polynomial.** Since \(R=I+S+S^2+S^3+S^4\), its squared entry moduli are products of squared edge magnitudes. Writing \((a,b,c,d)=(|w_1|^2,|w_2|^2,|w_3|^2,|w_4|^2)\), direct entrywise summation gives
\[
 \|R\|_{S_2}^2=5+(a+b+c+d)+Q(a,b,c,d),
 \quad Q=ab+bc+cd+abc+bcd+abcd.
\]
Thus \(a,b,c,d\ge0\), \(a+b+c+d=E\), and the phases disappear exactly.

**2. A symmetrize-or-break lemma.** Fix the two pair sums \(A=a+d\), \(B=b+c\), and put \(p=a-d\), \(q=b-c\). Then \(A+B=E\), \(|p|\le A\), \(|q|\le B\). A polynomial identity yields
\[
 16\{Q(a,b,c,d)-Q(A/2,B/2,B/2,A/2)\}
 =-B^2p^2-(A+2)^2q^2+p^2q^2+8pq. \tag{1}
\]
Changing signs if necessary shows that a maximizing difference pair may be taken with \(p,q\ge0\). For a fixed \(0<q<B\), the right side is a strictly concave quadratic in \(p\), maximized at
\[
 p=\min\left\{A,\frac{4q}{B^2-q^2}\right\}.
\]
Whenever this optimizer is strictly smaller than \(A\), the optimized value is
\[
 H(z)=\frac{16z}{B^2-z}-(A+2)^2z,\qquad z=q^2.
\]
Its second derivative is \(H''(z)=32B^2/(B^2-z)^3>0\). Hence on every interval where the optimal \(p\) lies inside \((0,A)\), there is no strictly positive interior maximum in \(z\): improvement is possible by moving to \(z=0\) or to the boundary \(p=A\). If \(q=0\), the best choice is \(p=0\); if \(q=B\), the best choice is \(p=A\). The cases \(A=0\) or \(B=0\) already have a vanishing outer weight or are strictly suboptimal, respectively. Consequently **every global maximum** is either fully palindromic \(a=d,b=c\), or has at least one vanishing outer weight \(a=0\) or \(d=0\). Strict convexity rules out any other maximizer. This is a global reduction, not a local stationarity heuristic.

**3. Maxima with a broken outer edge.** By reflection take \(d=0\). Then
\[
 Q=b(a+c)+abc=b(E-b)+abc\le b(E-b)+\frac{b(E-b)^2}{4},
\]
with equality, for \(b>0\), exactly when \(a=c=(E-b)/2=y\). This reduces to \(Q=y(y+2)(E-2y)\), \(0\le y\le E/2\). Its derivative is \(2E+2Ey-8y-6y^2\), which has exactly one positive root, \(y_E\) above, strictly inside that interval. The maximal value is \(B(E)\). In particular, the maximizer really has three positive consecutive edges. Configurations with additional zero edges cannot tie, because the displayed maximum is strictly larger than the best two-edge value \(E^2/4\).

**4. Palindromic maximum and its unique positive root.** With \(a=d=u\), \(b=c=v\), \(u+v=s\), substitution yields
\[
 Q=2uv+v^2+2uv^2+u^2v^2=s^2-u^2+u(u+2)(s-u)^2.
\]
Its derivative with respect to \(u\) equals \(2F(u,s-u)\), where
\[
 F(u,v)=(u+1)v^2-u(u+2)v-u.
\]
For each \(u>0\), the quadratic \(F(u,v)\) has one positive root \(v_*(u)\). Since \(F(u,u+2)=(u+2)^2-u>0\), that root is smaller than \(u+2\). At the root, \(F_v>0\) and \(F_u=v_*^2-(2u+2)v_*-1<0\), hence \(v_*'(u)>0\). Also \(v_*(0)=0\). Therefore \(u+v_*(u)\) is strictly increasing from zero to infinity, so \(s=u+v_*(u)\) has exactly one solution \(u_E\in(0,s)\). As the derivative of \(Q\) is positive at \(u=0\) and negative at \(u=s\), this is the unique global maximum of the palindromic branch, with value \(P(E)\).

Combining steps 2–4 proves the exact formula and the complete equality classification.

**5. A forced change of optimal support.** For \(0<E\le1\), the palindromic value for a trial \(u\) is bounded by
\[
 Q\le\frac{E^2}{4}-\frac34u^2+\frac{E^2}{2}u\le\frac{E^2}{4}+\frac{E^4}{12}.
\]
The broken-edge trial \(y=E/4\) gives
\[
 B(E)\ge\frac{E^2}{4}+\frac{E^3}{32}.
\]
Thus \(B(E)>P(E)\) throughout \(0<E<3/8\). On the other hand, the inequalities \(2y(E-2y)\le E^2/4\) and \(y^2(E-2y)\le E^3/27\) give \(B(E)\le E^2/4+E^3/27\). Choosing \(u=v=E/4\) gives
\[
 P(E)\ge\frac{3E^2}{16}+\frac{E^3}{32}+\frac{E^4}{256}.
\]
Their difference is positive for \(E\ge10\), since \(-1/16-5E/864+E^2/256>0\) there. Continuity of both exact branches forces at least one tie and corresponding optimizer-support transition at an intermediate budget.

## Verification
The accompanying standalone `CHECK.py` uses standard Python rational arithmetic to verify identity (1) on thousands of randomly selected rational quadruples, checks both explicit candidate profiles and their energies, stress-tests random points of the full simplex over multiple energy scales, and checks the small- and large-budget rational inequalities. Run with `python3 CHECK.py`. Its finite checks corroborate the displayed algebra but are **not** used as proof of the universal optimization or root uniqueness.

## Relationship to prior work
Szehr, *Eigenvalue estimates for the resolvent of a non-normal matrix* (first arXiv posting 2013), studies resolvent spectral/operator-norm bounds under contraction or power-boundedness assumptions; this provides the natural nonnormal-resolvent motivation but does not optimize the Hilbert–Schmidt norm of a five-site shift at fixed squared-weight budget. Sievewright, *Spectral radius algebras and weighted shifts of finite multiplicity* (2015), addresses invariant-subspace structure rather than the present finite-budget extremum. A previously published four-site result on Schatten-norm rearrangement for fixed weight magnitudes optimizes **order of a prescribed multiset**; it does not allow reallocation under a sum-of-squares budget or yield the five-site broken-versus-palindromic competition. A five-site weighted-shift result concerning fixed numerical shadows concerns a different constraint and operator norm. The current claim is an exact global design classification rather than a general resolvent upper bound.

## Limitations
The classification concerns exactly five state coordinates and the Hilbert–Schmidt resolvent norm; neither operator-norm nor higher-dimensional analogues follow. It proves existence but **not uniqueness** of the energy at which the optimizing branch changes. If all four edge weights are required to be strictly nonzero, the small-budget value remains the supremum but is not attained. Historical priority is not certified: an equivalent result in classical path-polynomial or bidiagonal-inverse optimization literature could remain unindexed.

## References
1. O. Szehr, *Eigenvalue estimates for the resolvent of a non-normal matrix*, arXiv:1305.7208 (first submitted 2013-05-30); J. Spectr. Theory **4** (2014), 783–813, doi:10.4171/JST/86.
2. D. Sievewright, *Spectral radius algebras and weighted shifts of finite multiplicity*, J. Math. Anal. Appl. **429** (2015), 658–675, doi:10.1016/j.jmaa.2015.04.027.
3. *Strict Schatten rearrangement for four-site weighted-shift resolvents*, publicly indexed mathematical finding (2026), distinguished here by its fixed-multiset constraint and four-site domain.
4. *Two sharp norm transitions within a five-site numerical-shadow fibre*, publicly indexed mathematical finding (2026), distinguished here by its numerical-shadow constraint and operator-norm objective.
