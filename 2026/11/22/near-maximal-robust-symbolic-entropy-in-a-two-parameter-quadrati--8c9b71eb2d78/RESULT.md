# Near-maximal robust symbolic entropy in a two-parameter quadratic delay map

## Finding
Consider the polynomial planar map
\[
F_{a,b}(x,y)=\left(ax+\frac32y,\;bx(1-x)\right).
\]
For every integer \(m\ge3\), set
\[
J=[1/8,7/8],\qquad x_{m,j}=\sin^2\frac{j\pi}{2^{m+1}}
\quad(0\le j\le2^m),
\]
and define the explicit positive integer
\[
k_m=\#\left\{0\le j<2^m:\;
\frac18<x_{m,j}<x_{m,j+1}<\frac78\right\}.
\]
There is a number \(\varepsilon_m>0\) such that **every** real parameter pair satisfying
\[
0<a<\varepsilon_m,\qquad \left|b-\frac83\right|<\varepsilon_m
\]
has a compact subset \(\Lambda_{a,b,m}\subset\mathbb R^2\) on which \(F_{a,b}^{2m}\) is uniformly expanding and topologically conjugate to the one-sided full shift on \(k_m^2\) symbols. Consequently, there is a compact forward-invariant set \(K_{a,b,m}\) with
\[
h_{\mathrm{top}}(F_{a,b}|K_{a,b,m})\ge \frac{\log k_m}{m}.
\]
At \(m=3\), \(k_3=4\), so the sixth iterate has a full sixteen-symbol expanding Cantor repeller for every pair in some nonempty open parameter region with \(a>0\), and
\[
h_{\mathrm{top}}(F_{a,b}|K_{a,b,3})\ge\frac{\log4}{3}.
\]
More strongly,
\[
 k_m=\kappa 2^m+O(1),\qquad
\kappa=1-\frac4\pi\arcsin\frac1{\sqrt8}>0.
\]
Thus, **for every** \(\eta>0\) there is a nonempty open neighborhood on the strictly positive-coupling side of \((a,b)=(0,8/3)\) in which every map has a compact invariant subsystem with entropy exceeding \(\log2-\eta\). The statement is an existential open-parameter result; no common positive radius is asserted for all \(m\).

## Assumptions and scope
All states and parameters are real. The map is studied on its natural entire real-plane domain, without assuming a global invariant unit square at nonzero coupling. The condition \(a>0\) ensures that every parameter covered belongs to the published family, which requires nonzero parameters. The singular uncoupled map at \(a=0\) is used only as an analytic anchor, not as a substitute for the claimed nonzero-coupling systems. Topological entropy is always taken on an explicitly specified compact forward-invariant set. A one-sided full shift is intended, not an invertible two-sided Smale horseshoe or an attractor.

## Proof
**1. Exact decoupling.** Apply the invertible linear coordinate change \((u,v)=(x,3y/2)\) and write \(r=3b/2\). The conjugated map becomes
\[
G_{a,r}(u,v)=(au+v,\;r u(1-u)).
\]
At \((a,r)=(0,4)\), let \(L(t)=4t(1-t)\). Then
\[
G_{0,4}(u,v)=(v,L(u)),\qquad
G_{0,4}^{2m}(u,v)=(L^m(u),L^m(v)).
\]
The second formula follows by iterating \(G_{0,4}^{2}(u,v)=(L(u),L(v))\). On the unit interval the exact trigonometric identity
\[
L^m(\sin^2\theta)=\sin^2(2^m\theta),
\quad 0\le\theta\le\pi/2
\]
gives all \(2^m\) monotonicity intervals \([x_{m,j},x_{m,j+1}]\), each mapped bijectively onto \([0,1]\). The endpoints have alternating critical values zero and one.

**2. Quantified expanding inverse sheets.** Set \(J'=[1/16,15/16]\), so \(J\subset\operatorname{int}J'\). For every index counted by \(k_m\), the entire lap \([x_{m,j},x_{m,j+1}]\) lies strictly within \(J\). Restrict its inverse of \(L^m\) to \(J'\), calling the resulting smooth branch \(q_{m,j}:J'\to\operatorname{int}J\). From the preceding exact identity,
\[
\left|(L^m)'(\sin^2\theta)\right|
=2^m\frac{|\sin(2^{m+1}\theta)|}{\sin(2\theta)}.
\]
At any point whose \(L^m\)-image belongs to \(J'\), the numerator trigonometric factor is \(2\sqrt{s(1-s)}\) for some \(s\in J'\), and therefore at least \(\sqrt{15}/8\). Since \(0<\sin(2\theta)\le1\),
\[
\inf_{s\in J'} |(L^m)'(q_{m,j}(s))|
\ge\frac{2^m\sqrt{15}}8
\ge\sqrt{15}>1.
\]
Thus \(q_{m,j}\) is Lipschitz with constant at most \(8/(2^m\sqrt{15})<1\). The product branches
\[
Q_{m,i,j}(s,t)=(q_{m,i}(s),q_{m,j}(t))
\]
are defined on an open neighborhood of \(J^2\), are pairwise disjoint in image, map \(J^2\) compactly into its interior, and have operator-norm Lipschitz constants strictly below one. They are all the selected inverse sheets of \(G_{0,4}^{2m}\).

**3. Persistence at nonzero coupling.** Fix \(m\). The finitely many compact inverse-sheet graphs \(\{(Q_{m,i,j}(z),z):z\in J^2\}\) have nonzero Jacobian determinants and are mutually separated. Moreover, their preimages have positive distance from \(\partial(J^2)\), and the inverse differentials have norms bounded above by a number strictly smaller than one. Polynomial dependence of \(G_{a,r}^{2m}\) on its state and parameters implies \(C^1\) convergence to \(G_{0,4}^{2m}\) on a compact neighborhood of those graphs. The uniform inverse function theorem, applied on the compact target \(J^2\) and continued over finitely many local charts, therefore supplies for sufficiently small \(|a|+|r-4|\) exactly one smooth inverse sheet near every \(Q_{m,i,j}\). Each persists on all of \(J^2\), maps it into \(\operatorname{int}J^2\), stays separated from every other selected sheet, and has inverse differential norm below \(1/2\), since the unperturbed bound is at most \(1/\sqrt{15}<1/2\). All these inequalities are strict, hence hold on an open parameter neighborhood. Translating \(r=3b/2\) and intersecting that neighborhood with \(a>0\) gives \(\varepsilon_m>0\).

**4. Symbolic conjugacy and entropy.** Write \(H=G_{a,r}^{2m}\), and let \(q_1,\ldots,q_{k_m^2}:J^2\to\operatorname{int}J^2\) be its selected contracting inverse branches. Their images are disjoint. For any one-sided infinite symbol sequence \(\omega\), the nested images
\[
q_{\omega_0}\circ\cdots\circ q_{\omega_n}(J^2)
\]
have diameters tending uniformly to zero. Their intersection is a single point \(\pi(\omega)\). The coding map is continuous, injective because first-level images are disjoint, and onto its compact image \(\Lambda\), and it obeys \(H\circ\pi=\pi\circ\sigma\). The inequality on inverse norms makes \(H\) uniformly expanding on \(\Lambda\). Conjugate back to the original \((x,y)\) coordinates. This rescaling has condition number \(3/2\), so the inverse-differential bound \(<1/2\) in adapted coordinates becomes at most \(3/4<1\) in the original Euclidean norm. Uniform expansion therefore persists in the physical coordinates as well. With
\[
K=\bigcup_{j=0}^{2m-1}F_{a,b}^j(\Lambda),
\]
we have \(F_{a,b}(K)=K\) and \(\Lambda\subset K\), hence
\[
2m\,h_{\mathrm{top}}(F_{a,b}|K)
=h_{\mathrm{top}}(F_{a,b}^{2m}|K)
\ge h_{\mathrm{top}}(F_{a,b}^{2m}|\Lambda)
=\log(k_m^2).
\]
This proves the claimed entropy lower bound.

**5. Branch asymptotics and sharp entropy approach.** The endpoints \(x_{m,j}=\sin^2(j\pi/2^{m+1})\) increase with \(j\). Put \(\theta_0=\arcsin(1/\sqrt8)\). The condition defining \(k_m\) is equivalent, up to at most two rounding endpoints, to
\[
\frac{2\theta_0}{\pi}<\frac{j}{2^m}
<1-\frac{2\theta_0}{\pi}.
\]
Therefore the count is \(k_m=(1-4\theta_0/\pi)2^m+O(1)\); the constant is positive because \(\theta_0<\pi/4\). Hence \(\log k_m/m\to\log2\). For \(m=3\), the admitted lap indices are exactly \(j=2,3,4,5\), as the two extreme retained endpoints are
\[
x_{3,2}=\frac{2-\sqrt2}{4}>\frac18,\qquad
x_{3,6}=\frac{2+\sqrt2}{4}<\frac78.
\]
Choosing \(m\) with \(\log k_m/m>\log2-\eta\) and the associated \(\varepsilon_m\) finishes the all-accuracy assertion. At the limiting decoupled parameter the target value is intrinsic and sharp for compact dynamics: \(L\) on \([0,1]\) is conjugate by \(s\mapsto\sin^2(\pi s/2)\) to the full tent map of slopes \(\pm2\), and hence has entropy \(\log2\). Every real logistic orbit starting outside \([0,1]\) escapes to negative infinity, so all compact forward-invariant subsystems of \(G_{0,4}^2=(L,L)\) lie in \([0,1]^2\). Thus the compact-system entropy supremum of \(G_{0,4}\) equals \(\log2\) by product additivity and the iteration law. This limiting identity is contextual; the theorem asserts only lower bounds near the excluded parameter.

## Verification
The standalone `check_horseshoe.py` confirms the polynomial coordinate conjugacy, the exact retained indices for the sixth iterate, strict endpoint separation, the derivative lower bound, and the sequence of branch counts for \(3\le m\le10\). These checks corroborate finite algebraic steps. The theorem for every \(m\) and the persistence for every parameter in an open neighborhood are justified by the identities and compact inverse-function argument above, not by finite computation. The program needs Python's standard library only.

## Relationship to prior work
Liu and Zhong (2024) introduce this precise polynomial map and analyze fixed-point stability, local bifurcation types, and numerical trajectories. Their published article does not give the stated open-set symbolic coding or an entropy arbitrarily close to \(\log2\). The identity for the parameter-four logistic map and persistence of uniformly expanding inverse branches are classical tools, explicitly used rather than claimed as new general theory. Earlier mathematical results for this *same* polynomial map determine complex periodic-point multiplicities and some low-period real cycles; such counts do not locate a real compact uniformly expanding Cantor subsystem or prove its entropy persists on a nonzero-coupling parameter region. Published horseshoe theorems for Hénon diffeomorphisms and other two-dimensional noninvertible maps concern different equations or hypotheses, and do not directly imply the concrete branch count above.

## Limitations
The neighborhood radii \(\varepsilon_m\) are proved positive by compactness but are not numerically optimized or explicitly calculated. Their infimum as \(m\to\infty\) is not claimed positive, and no entropy lower bound of exactly \(\log2\) is claimed at a fixed nonzero coupling. The symbolic sets are expanding repellers, not necessarily physical attractors or positive-area sets. No assertion about cryptographic security, the entire noncompact phase space, or maximality of the ambient topological entropy is made. No independent mathematical audit has been performed. Unindexed results might contain equivalent source-specific claims.

## References
1. L. Liu and X. Zhong, *Research on Stability and Bifurcation for Two-Dimensional Two-Parameter Squared Discrete Dynamical Systems*, Mathematics **12** (2024), 2423, published August 4, 2024. https://doi.org/10.3390/math12152423
2. Y. Soula, H. Jahanshahi, A. A. Al-Barakati, and I. Moroz, *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics **11** (2023), 1517. https://doi.org/10.3390/math11061517
3. E. Bedford and J. Smillie, *A symbolic characterization of the horseshoe locus in the Hénon family*, Ergodic Theory and Dynamical Systems **37** (2017), 1389–1412. https://doi.org/10.1017/etds.2015.113
4. X. Zhang and G. Chen, *Diffeomorphisms with infinitely many Smale horseshoes*, Journal of Difference Equations and Applications **30** (2024), 1866–1884. https://doi.org/10.1080/10236198.2024.2368170
