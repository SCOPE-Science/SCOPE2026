# Exact signed and logarithmic relaxation at the first Hénon flip

## Finding
Consider the real planar Hénon map
\[
F_{a,b}(x,y)=(1-a x^2+y,\,b x),\qquad 0<b<1,
\]
at its first flip threshold
\[
a=a_b=\frac{3(1-b)^2}{4},\qquad (x_*,y_*)=\left(\frac{2}{3(1-b)},\frac{2b}{3(1-b)}\right).
\]
There exists a neighborhood of this fixed point in which all orbits converge to it. On the one-dimensional local strong-stable manifold they do so exponentially. For every other initial point in a sufficiently small neighborhood, there is an eventual constant sign \(\sigma\in\{-1,1\}\) of \(x_{2n}-x_*\), and a finite, orbit-dependent real constant \(C\), such that
\[
\boxed{\frac{1}{(x_{2n}-x_*)^2}=K_b n+\sigma H_b\sqrt n+L_b\log n+C+o(1)}
\qquad(n\to\infty),
\]
where the three universal coefficients are
\[
K_b=\frac{9(1-b)^3}{4(1+b)},\qquad
H_b=\frac{9(1-b)^{5/2}}{8\sqrt{1+b}},\qquad
L_b=\frac{9(1-b)^2(11b^2-2b+11)}{64(1+b)^2}.
\]
In particular \(K_b,H_b,L_b>0\) for every \(0<b<1\). Thus the experimentally observed inverse-square critical clock has a genuine sign-dependent square-root correction and a strictly positive logarithmic correction in the original Hénon coordinate and original even-iteration clock, for all dissipative positive Jacobian magnitudes \(b\in(0,1)\).

## Assumptions and scope
All parameters and initial conditions are real. The statement concerns exactly \(a=a_b\), not a varying bifurcation parameter. The iterate \(x_{2n}\) means the first coordinate after precisely \(2n\) original Hénon steps. The local neighborhood may depend on \(b\); the constant \(C\) depends on the initial condition and \(b\). Initial points in the strong-stable manifold are excluded from the inverse-square law because they approach exponentially. No global-basin conclusion is claimed. The sign \(\sigma\) is the eventual sign of the even-iterate first-coordinate displacement; it is not a free choice in the formula.

## Proof
**1. Critical parameter and eigensplitting.** A fixed point has \(y=bx\) and satisfies \(a x^2+(1-b)x-1=0\). Its Jacobian \(\begin{pmatrix}-2ax&1\\ b&0\end{pmatrix}\) has eigenvalue \(-1\) exactly when \(2ax=1-b\). Solving these equations yields \(a_b\), \((x_*,y_*)\), and the second eigenvalue \(b\in(0,1)\).

Write \(u=x-x_*\), \(v=y-y_*\), set
\[
z=\frac{u-v}{1+b},\qquad w=\frac{u+v/b}{1+b},\qquad c=\frac{a_b}{1+b}=\frac{3(1-b)^2}{4(1+b)}.
\]
Then \(u=z+bw\), \(v=b(-z+w)\), and **exactly**
\[
z'=-z-c(z+bw)^2,\qquad w'=bw-c(z+bw)^2.\tag{1}
\]
The eigenvalues are \(-1\) and \(b\). By the smooth center-manifold and stable-tracking theorems for maps with one center and one strictly contracting eigenvalue, a local smooth invariant center graph \(w=h(z)\), tangent to \(w=0\), and an exponentially contracting stable foliation exist. The ensuing positive cubic center normal form makes the fixed point locally attracting; a point not on the strong-stable leaf tracks a nontrivial center orbit with exponentially small error.

**2. Explicit center graph.** Solving the exact invariance identity
\[
h(-z-c(z+b h(z))^2)=b h(z)-c(z+b h(z))^2
\]
coefficient by coefficient gives
\[
\begin{aligned}
h(z)&=h_2 z^2+h_3 z^3+h_4 z^4+O(z^5),\\
h_2&=\frac{c}{b-1},\qquad h_3=\frac{2c^2}{b-1},\\
h_4&=\frac{5c^3(b^2-b+1)}{(b-1)^3}.
\end{aligned}
\]
All displayed denominators are nonzero because \(0<b<1\). Consequently the reduced center map \(z'=f(z)\) has coefficients through order five
\[
\begin{aligned}
f(z)&=-z+f_2z^2+f_3z^3+f_4z^4+f_5z^5+O(z^6),\\
f_2&=-c,\quad f_3=\frac{2bc^2}{1-b},\\
f_4&=-\frac{bc^3(5b-4)}{(1-b)^2},\\
f_5&=\frac{2bc^4(7b^2-7b+5)}{(1-b)^3}.
\end{aligned}
\]
These identities can be checked by direct polynomial substitution into (1), without numerical differentiation.

**3. A fixed normalization of the flip coordinate.** Define a local coordinate \(s\) by the invertible polynomial change
\[
z=s+u_2s^2+u_4s^4,\qquad
u_2=-\frac c2,\quad
u_4=-\frac{c^3(5b^2-6b+5)}{8(1-b)^2}.
\]
(The symbols \(u_2,u_4\) are coefficients, not dynamical variables.) By substituting the preceding coefficients of \(f\), the conjugate map is
\[
s'=-s+p s^3+q s^5+O(s^6),\tag{2}
\]
where
\[
p=\frac{c^2(1+b)}{1-b}>0,\qquad
q=\frac{c^4(1+b)(17b^2-2b+5)}{4(1-b)^3}.
\]
This establishes locally attracting flip dynamics: for small nonzero \(s\), successive signs alternate and the absolute value decreases. The second iterate satisfies
\[
s_{2n+2}=s_{2n}-2p s_{2n}^3+(3p^2-2q)s_{2n}^5+O(s_{2n}^6).\tag{3}
\]
Because \(p>0\), every sufficiently small nonzero center orbit tends to zero, preserving the sign on its even subsequence.

**4. The inverse-square clock.** Put \(S_n=s_{2n}^{-2}\). Equation (3), with a uniform smooth remainder, implies
\[
S_{n+1}-S_n=4p+\frac{6p^2+4q}{S_n}+O(S_n^{-3/2}).\tag{4}
\]
Its increments tend to \(4p>0\), hence \(S_n/(4pn)\to1\). Summing (4) first yields \(S_n=4pn+O(\log n)\); reinserting this estimate gives
\[
S_n=4pn+\left(\frac{3p}{2}+\frac qp\right)\log n+C_s+o(1).\tag{5}
\]
Indeed, the difference between (4) and the forward difference of the displayed linear-plus-logarithm expression is \(O((\log n)/n^2+n^{-3/2})\), an absolutely summable sequence. Thus the remaining constant exists; this is not just a bound of order \(O(1)\).

**5. Return to the original physical coordinate.** From \(u=z+b h(z)\) and the chosen \(z(s)\),
\[
x-x_*=s+A s^2+B s^3+O(s^4),\quad
A=-\frac{c(1+b)}{2(1-b)},\quad B=-\frac{bc^2}{1-b}.
\]
Consequently, along center orbits,
\[
\frac1{(x_{2n}-x_*)^2}=S_n-2A\,s_{2n}^{-1}+(3A^2-2B)+O(|s_{2n}|).
\]
Since \(s_{2n}^{-1}=\sigma\sqrt{S_n}\), (5) implies
\[
\frac1{(x_{2n}-x_*)^2}=4pn+\sigma(-2A)\sqrt{4p}\,\sqrt n+
\left(\frac{3p}{2}+\frac qp\right)\log n+C+o(1).
\]
The exponentially small errors from the stable foliation do not alter this expansion: multiplying such errors by at most a polynomial factor while taking inverse squares still gives \(o(1)\). Substituting \(c=3(1-b)^2/[4(1+b)]\) gives the advertised \(K_b,H_b,L_b\). Lastly, \(11b^2-2b+11>0\) for every real \(b\), proving strict positivity in the claimed range.

## Verification
The accompanying `verify.py` checks the center-graph and normal-form coefficients using exact rational polynomial arithmetic and symbolic identities, and independently computes finite Hénon trajectories at sample damping parameters. It checks the stated coefficients and a decreasing residual trend after subtracting all three universal asymptotic terms. Run `python verify.py` with Python 3 and SymPy. These tests support algebraic reproducibility; the proof above, not finite numerical iteration, establishes the asymptotic statement for arbitrarily large times.

## Relationship to prior work
Leonel, Ferreira and Oliveira (2026, arXiv:2602.04091v1, Section 3.1) study this same real Hénon map at \(b=0.3\) and approximately \(a=0.367495\), demonstrating the universal critical distance exponent near \(-1/2\) numerically and its local center-manifold explanation. The exact flip parameter \(a_b\) is an elementary established consequence of the fixed point Jacobian and is **not** a novelty claim. Their formulas do not provide the three explicit coefficients above or a finite residual limit in the original Hénon coordinate. Teixeira et al. (2015, arXiv:1502.06437v1) establish scaling exponents for scalar logistic-like maps, not these two-dimensional parameter-dependent physical-coordinate amplitudes.

A published study of the canonical quadratic flip establishes a finite-time susceptibility crossover and the leading Lyapunov logarithm, not the Hénon coordinate relaxation coefficients. A published rational positive flip example establishes a signed square-root plus logarithmic inverse-square expansion for a different scalar recurrence, demonstrating that the **generic method and type of asymptotic are prior art**, not a new general theorem. A published higher-dimensional Hénon fold result concerns dimensions at least three, an eigenvalue \(+1\), and a different fold parameter. Such results do not imply the explicit physical-coordinate coefficients here. General parabolic germ and center-manifold theory provide background tools; no novelty is claimed for these methods.

## Limitations
The statement is local to the first flip, restricted to \(0<b<1\); it is neither uniform as \(b\) approaches the endpoints nor a global classification of Hénon dynamics. On the strong-stable curve the inverse-square asymptotic is inapplicable. The orbit-dependent constant \(C\) is not given in elementary closed form. A completely exhaustive historical priority determination is not asserted; general parabolic normal-form machinery and unindexed older Hénon calculations are residual originality risks. Independent scientific review has not been performed.

## References
1. E. D. Leonel, J. P. C. Ferreira and D. F. M. Oliveira, *A phenomenological description of critical slowing down at period-doubling bifurcations*, arXiv:2602.04091v1, first public 2026-02-04. https://arxiv.org/abs/2602.04091.
2. R. M. N. Teixeira, D. S. Rando, F. C. Geraldo, R. N. Costa Filho, J. A. de Oliveira and E. D. Leonel, *Convergence towards asymptotic state in 1-D mappings: a scaling investigation*, arXiv:1502.06437v1, first public 2015-02-23. https://arxiv.org/abs/1502.06437.
3. *Exact finite-time susceptibility crossover at a quadratic flip threshold*, published published-finding corpus mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-finite-time-susceptibility-crossover-at-a-quadratic-flip-t--acec857a2ec3.
4. *Global signed and logarithmic critical relaxation in a positive rational flip map*, published published-finding corpus mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-signed-and-logarithmic-critical-relaxation-in-a-positive--741941f8eb7b.
5. *Global recurrence threshold and logarithmic fold relaxation for generalized Hénon maps*, published published-finding corpus mathematical finding (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-global-recurrence-threshold-and-logarithmic-fold-relaxation-for--edd60670a63c.
