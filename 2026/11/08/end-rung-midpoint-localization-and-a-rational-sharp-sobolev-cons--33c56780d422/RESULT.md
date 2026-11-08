# End-rung midpoint localization and a rational sharp Sobolev constant on metric ladders

## Finding
Let \(L_n=P_n\square K_2\) be the metric ladder with \(n\ge3\) rungs, where every edge is a unit interval, every vertex has standard continuity conditions, and arclength is unweighted. Its total length is \(m=3n-2\). For every real continuous edgewise-\(H^1\) function with \(\int_{L_n}f\,ds=0\), the **sharp** inequality is
\[
\|f\|_{\infty}^{2}\le
\boxed{\frac{18n^{3}-18n^{2}-9n+10}{12(3n-2)^{2}}}
\int_{L_n}|f'|^{2}\,ds.
\]
Exactly two evaluation points attain the squared norm of the evaluation functional: the midpoints of the first and last rungs. There are no other maximizers, including vertices or points on the rails. Equality for a nonzero function occurs exactly for a scalar multiple of the centered Kirchhoff Green representer of evaluation at one of these two midpoints.

There is also an exact **off-end-rung gap**. Let \(\mathcal K_n\) denote the boxed constant and let \(\mathcal K_n^{\mathrm{off}}\) be the supremum of squared evaluation-functional norms over the complement of the two *open* end rungs. Define \(\eta=\operatorname{arcosh}(2)\). Then
\[
\mathcal K_n-\mathcal K_n^{\mathrm{off}}
=\frac{3n-3-(3n-2)r_{\mathrm{end}}}{4(3n-2)}
=\frac14\left(2-\sqrt3\coth(n\eta)-\frac1{3n-2}\right)>0,
\qquad r_{\mathrm{end}}=\sqrt3\coth(n\eta)-1.
\]
In particular, this positive gap tends to \((2-\sqrt3)/4\). The smallest ladder \(L_2\) is a four-edge circle; its squared sharp constant is \(1/3\), with **every** point maximizing, rather than just two midpoints.

## Assumptions and scope
The graph is the Cartesian product of the unweighted combinatorial path on \(n\) vertices and the two-vertex graph, each edge metrized to length one. All edges are included in the arclength integral. The energy is first order, real-valued, and has no added \(L^2\) term. Functions are continuous at vertices and belong to \(H^1\) on each edge. The integral-zero condition removes constants. The sharp constant is the squared operator norm of the inclusion of this energy Hilbert space into \(C(L_n)\). The choice of edge orientations is immaterial.

## Proof
**1. Evaluation and resistance.** Let \(r(x,y)\) be the effective resistance on the unit-conductance metric network and \(k_x\) the unique mean-zero energy representer of evaluation at \(x\). The resistance polarization identity is
\[
r(x,y)=\|k_x-k_y\|_{\mathcal H}^{2}.
\]
Since \(\int k_y\,ds_y=0\) in the energy Hilbert space, integration first in \(y\), then in \(x\), gives
\[
\|k_x\|_{\mathcal H}^{2}=
\frac{F(x)}m-\frac{J}{2m^{2}},\qquad
F(x)=\int_{L_n}r(x,y)\,ds_y,\qquad
J=\iint_{L_n\times L_n}r(y,z)\,ds_y\,ds_z.
\]
Thus locating the sharp Sobolev extremizers is exactly the maximization of \(F\).

**2. An edgewise quadratic.** For a unit edge \(e=uv\), write \(x_t\) for the point at parameter \(t\in[0,1]\), and \(r_e=r(u,v)\). Resistance can be represented by a Gaussian field that linearly interpolates the vertex network field and has independent standard Brownian bridges on the edges. For every different edge, the integrated resistance to \(x_t\) exceeds the linear interpolation of its endpoint integrals by \((1-r_e)t(1-t)\). On the same edge, the difference is \(-r_e t(1-t)\). Summing the \(m\) contributions proves the exact identity
\[
F(x_t)=(1-t)F(u)+tF(v)+C_e t(1-t),\qquad C_e=m-1-mr_e.
\]
Every ladder edge lies on a unit square, so it is connected in parallel with a path of three other unit edges. Rayleigh monotonicity yields \(r_e\le3/4\), hence \(C_e\ge m/4-1>0\) for \(n\ge3\). Consequently each edge profile is strictly concave and is at most \(\max\{F(u),F(v)\}+(m-1)/4\).

**3. Vertex potential decreases toward the middle.** Label the rungs \(j=1,\ldots,n\), and the two vertices at rung \(j\) by \(v_{j,+},v_{j,-}\). Let \(D\) be the ordinary path Laplacian, \(G=D^\dagger\) its zero-row-sum pseudoinverse, and \(H=(D+2I)^{-1}\). Symmetric and antisymmetric row coordinates diagonalize the ladder Laplacian, so its pseudoinverse is
\[
Q=\frac12\begin{pmatrix}G+H&G-H\\G-H&G+H\end{pmatrix}.
\]
For the diagonal entries we have
\[
G_{jj}=\frac1n\sum_{i=1}^n|i-j|-\frac{n^2-1}{6n},\qquad
H_{jj}=\frac{\cosh((j-\tfrac12)\eta)\cosh((n-j+\tfrac12)\eta)}{\sinh\eta\sinh(n\eta)},\quad\cosh\eta=2.
\]
The second formula follows by solving the tridiagonal Green recurrence, with reflecting path endpoints. Both diagonals decrease strictly as the rung moves from an endpoint toward the middle (with the two central rungs tied when \(n\) is even).

Integrating resistance from a vertex over each unit edge gives
\[
F(v)=\frac12\sum_{w}\deg(w)r(v,w)+\frac16\sum_{e}(1-r_e).
\]
Using \(Q\mathbf1=0\) and the degrees \((2,3,\ldots,3,2)\) in each row reduces this to
\[
F(v_{j,+})=F(v_{j,-})=\frac{3n}{2}G_{jj}+\frac m2H_{jj}+B,
\]
where \(B\) does not depend on \(j\). If \(F_j\) denotes this common value, reflection and strict decrease imply \(F_1=F_n>F_2=F_{n-1}\ge F_j\) for all interior rung indices. Moreover
\[
\Delta:=F_1-F_2=\frac32(n-2)+\frac m2(H_{11}-H_{22})>
\frac{m-1}{4}.
\]
For \(n=3\), the last inequality is strict because \(H_{11}>H_{22}\); for larger \(n\) even the first summand is greater than \((m-1)/4\).

**4. Exhaustive edge comparison.** Every edge not incident to an end vertex has both endpoints with \(F\le F_2\). Its entire interior therefore satisfies \(F(x)\le F_2+(m-1)/4<F_1\). It remains to inspect the four end rails and two end rungs. The first-row resolvent equations give \(3H_{11}-H_{12}=1\) and \(H_{22}=3H_{12}\). Therefore the resistance of an end rail and that of the adjacent end rung coincide:
\[
r_{\mathrm{end\ rail}}=\frac{1+H_{11}+H_{22}-2H_{12}}2
=2H_{11}=r_{\mathrm{end\ rung}}>\frac23.
\]
(The strict last inequality uses \(H_{12}>0\).) Consequently their common \(C_e\) is less than \(m/3-1=n-5/3\), whereas \(\Delta>3(n-2)/2>n-5/3\). Along an end rail, the quadratic profile decreases strictly away from the end vertex, so its maximum is \(F_1\). On an end rung the endpoints both have value \(F_1\), giving
\[
F(x_t)=F_1+C_{\mathrm{end}}t(1-t),\qquad C_{\mathrm{end}}>0.
\]
Its unique maximizing point is its midpoint. The two end rungs have equal maxima by reflection. Every point off the open end rungs has \(F(x)\le F_1\), with equality at their endpoint vertices, which also proves the stated exact gap after division by \(m\). The identity \(r_{\mathrm{end}}=\sqrt3\coth(n\eta)-1\) follows directly from the tridiagonal formula for \(H_{11}\).

**5. Exact constant without resistance sums.** Use independent centered Gaussian vectors \(u,v\) with covariances \(G,H\) and independent standard unit-interval Brownian bridges \(B_e\). At the vertices set \(\phi_{j,\pm}=(u_j\pm v_j)/\sqrt2\), interpolating along each edge and adding \(B_e\). Then \(\mathbb E(\phi(x)-\phi(y))^2=r(x,y)\). The squared mean-zero evaluation norm equals \(\operatorname{Var}(\phi(x)-m^{-1}\int\phi)\). At an end-rung midpoint the antisymmetric \(v\) part cancels. Set \(d=(2,3,\ldots,3,2)^\mathsf T=3\mathbf1-e_1-e_n\), and
\[
g=G_{11}=\frac{(n-1)(2n-1)}{6n},\qquad
h=G_{11}+G_{1n}=\frac{(n-1)(n-2)}{6n}.
\]
Since \(G\mathbf1=0\), the variance of the vertex-linear part is
\[
\frac12(e_1-d/m)^\mathsf TG(e_1-d/m)=\frac g2+\frac hm+\frac h{m^2}.
\]
A bridge at the midpoint has variance \(1/4\); its covariance with the arclength average of all bridges equals \(1/(8m)\), and that average has variance \(1/(12m)\). Its centered variance is therefore \(1/4-1/(6m)\). Adding independent components gives
\[
\mathcal K_n=\frac14-\frac1{6m}+\frac g2+\frac hm+\frac h{m^2}
=\frac{18n^3-18n^2-9n+10}{12(3n-2)^2}.
\]
Finally, the Hilbert-space Cauchy–Schwarz equality condition gives exactly the stated Green-representer extremizers. For \(n=2\), the ladder is a circle of length four, whose mean-zero evaluation norm is constantly \(4/12=1/3\).

## Verification
The accompanying `check_ladder.py` uses only the Python standard library. It independently constructs the rational vertex Laplacian pseudoinverse, computes all vertex-to-vertex effective resistances, integrates resistance on every ordered pair of edges, maximizes every exact edge quadratic, and checks both the maximizing edges and closed formula for every \(2\le n\le9\). The exact output includes \(307/588\) at \(n=3\) and \(419/600\) at \(n=4\). These finite checks test the algebra; the proof above, not the tests, covers every integer \(n\ge3\).

## Relationship to prior work
Baker and Faber establish the general Laplacian, resistance, and potential-theoretic framework for metric graphs [1]; none of their general results is claimed as new. Cinkir explicitly studies **this same ladder family** and gives discrete vertex effective resistances, the Kirchhoff index, the tau constant, and admissible invariants [2]. These supply relevant prior calculations but do not state the arclength-mean-zero sharp first-order Sobolev constant, the continuous two-midpoint localization theorem, or the off-end-rung gap. Carmona, Encinas and Mitjana investigate a broader weighted ladder-like family and its vertex Green functions [3]; the accessible material did not permit a complete text comparison, so an implicit-coverage risk remains. In particular, resistance formulas alone do not specify where a continuous arclength evaluation functional has its maximum: the necessary edgewise optimization and strict comparison are given here.

## Limitations
All edges must have equal unit lengths and uniform arclength energy and mean; the proof makes no claim for weighted rails, unequal rungs, extra boundary masses, Dirichlet constraints, or higher-order Sobolev energies. The exact source comparison to [3] was limited to its public abstract and bibliographic information; no claim of priority against unseen text is made. No independent mathematical review has been performed.

## References
[1] M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, original arXiv posting July 25, 2004, arXiv:math/0407428, https://arxiv.org/abs/math/0407428.

[2] Z. Cinkir, *Effective Resistances, Kirchhoff index and Admissible Invariants of Ladder Graphs*, original arXiv posting March 21, 2015, arXiv:1503.06353, https://arxiv.org/abs/1503.06353. Journal version: *J. Math. Chem.* 54 (2016), 955–966.

[3] A. Carmona, A. M. Encinas and M. Mitjana, *Effective resistances for ladder-like chains*, *Int. J. Quantum Chem.* 114 (2014), 1670–1677, DOI:10.1002/qua.24740.
