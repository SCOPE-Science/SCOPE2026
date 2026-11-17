# Composition-selected focus and node relaxation in dissipative Lotka–Volterra stars

## Finding

A stably dissipative Lotka–Volterra star can have a whole positive equilibrium manifold, yet **every strictly positive trajectory converges to one equilibrium selected exactly by its conserved leaf ratios**. The terminal equilibrium may be a transverse stable node or a stable focus, depending on the *initial composition* rather than on a change of coefficients. Both behaviors occur among strictly positive initial conditions for the same coefficients if and only if a sharp inequality involving the least and greatest leaf response rates holds. In the focus regime, the asymptotic number of crossings of the central equilibrium level per unit time has an exact, composition-dependent value.

For each integer \(m\ge2\), fix \(U,d>0\), \(b_j,c_j,p_j>0\) for \(1\le j\le m\), and put \(S=\sum_j b_jp_j\). Consider
\[
\dot u=u\left[-d(u-U)-\sum_{j=1}^m b_j(v_j-p_j)\right],\qquad
\dot v_j=c_jv_j(u-U),
\]
with arbitrary strictly positive initial data. There exists a unique real \(a\) satisfying
\[
\sum_{j=1}^m b_jv_j(0)e^{c_ja}=S.
\]
Every trajectory converges to the equilibrium \((U,v_1^*,\ldots,v_m^*)\), where \(v_j^*=v_j(0)e^{c_ja}\). On the two-dimensional invariant leaf determined by the initial ratios \(v_i^{1/c_i}/v_j^{1/c_j}\), this equilibrium has transverse characteristic polynomial
\[
\lambda^2+Ud\lambda+UB,\qquad B=\sum_{j=1}^m b_jc_jv_j^*.
\]
Set \(\tau=Ud^2/(4S)\) and \(c_{\min}=\min_jc_j\), \(c_{\max}=\max_jc_j\). Nonempty open sets of positive initial states selecting a node and a focus coexist **if and only if**
\[
c_{\min}<\tau<c_{\max}.
\]
For a nonstationary trajectory selecting a focus (equivalently \(4UB>(Ud)^2\)), let \(N(T)\) be the number of distinct positive-time crossings \(u(t)=U\) within \((0,T]\). Then
\[
\lim_{T\to\infty}\frac{N(T)}{T}
=\frac{\sqrt{4UB-U^2d^2}}{2\pi}.
\]
If \(4UB<(Ud)^2\), every nonstationary trajectory has only finitely many such crossings. The equality case has a repeated negative eigenvalue and is not asserted to have either strict focus or distinct-node behavior.

**An explicit three-species basin divider.** Set \(U=1\), \(d=6\), \(b_1=b_2=1\), \(c_1=1\), \(c_2=9\), and \(p_1=p_2=1\). The positive equilibria are \((1,2-w,w)\), \(0<w<2\). The conserved quantity
\[
R=\frac{v_2(0)}{v_1(0)^9}
\]
selects the unique \(w\) determined by \(R=w/(2-w)^9\). Define \(R_*=7\cdot8^8/9^9\). Then \(R<R_*\) selects a distinct stable node, \(R>R_*\) a stable focus with exact crossing rate \(\sqrt{8w-7}/\pi\), and \(R=R_*\) a repeated real eigenvalue. This basin partition is independent of \(u(0)>0\).

## Assumptions and scope

All parameters and all initial components are strictly positive; \(m\) is a finite integer \(\ge2\). The graph is a star with a self-damped central vertex and zero diagonal entries at leaves; each edge has predator–prey signs. A ``node'' or ``focus'' here refers to the two nonzero eigenvalues and dynamics **within a conserved two-dimensional leaf**. In the full phase space the equilibrium manifold has \(m-1\) additional zero directions; individual equilibria are not isolated full-space attractors. The crossing count excludes stationary solutions, whose central coordinate is constantly \(U\). A positive-time zero is counted once, not by multiplicity.

## Proof

**1. Exact conservation and the equilibrium selected by each leaf.** Along a positive solution, \(d(\log v_j)/dt=c_j(u-U)\). Thus all \(\log v_i/c_i-\log v_j/c_j\) are conserved. Writing \(Y(t)=\int_0^t (u(s)-U)\,ds\), every leaf coordinate is \(v_j(t)=v_j(0)e^{c_jY(t)}\). The function \(a\mapsto\sum_j b_jv_j(0)e^{c_ja}\) is continuous, strictly increasing from zero to infinity. Its equation with right-hand side \(S>0\) has exactly one solution \(a\). Hence the conserved leaf intersects the positive equilibrium manifold \(\{u=U,\ \sum_jb_jv_j=S\}\) in exactly one point, namely the claimed \(v^*\).

**2. No escape and global convergence.** Define \(\Phi(z;q)=z-q-q\log(z/q)\), positive away from \(z=q\) and diverging as \(z\downarrow0\) or \(z\to\infty\). With the fixed reference equilibrium \((U,p_1,\ldots,p_m)\), put
\[
L(u,v)=\Phi(u;U)+\sum_j\frac{b_j}{c_j}\Phi(v_j;p_j).
\]
Direct differentiation gives the exact identity
\[
\dot L=(u-U)\left[-d(u-U)-\sum_jb_j(v_j-p_j)\right]
+\sum_jb_j(v_j-p_j)(u-U)=-d(u-U)^2.
\]
Every positive sublevel of \(L\) is compact inside the positive orthant. Therefore the positive solution exists for all forward time and remains in a compact positive region. The zero-dissipation set is \(u=U\). To remain in that set a full forward trajectory must satisfy \(\dot u=-U\sum_jb_j(v_j-p_j)=0\); all leaf derivatives then vanish. Hence its maximal invariant subset is precisely the equilibrium manifold. LaSalle's invariance argument forces the omega-limit set into that manifold, while the conserved-ratio argument in Step 1 leaves only one possible point. Therefore the entire trajectory converges to \((U,v^*)\); in particular \(Y(t)\to a\).

**3. Exact transverse spectrum.** On a conserved leaf set \(z=Y-a\), \(w=u-U\), and define \(G(z)=\sum_j b_jv_j^*(e^{c_jz}-1)\). Then
\[
\dot z=w,\qquad \dot w=(U+w)[-dw-G(z)],\qquad G(0)=0,\quad G'(0)=B>0.
\]
The linearization in \((z,w)\) has matrix \(\left(\begin{smallmatrix}0&1\\-UB&-Ud\end{smallmatrix}\right)\), with the claimed polynomial. Both roots have negative real parts, with a distinct real pair when \(4UB<(Ud)^2\), complex pair when \(4UB>(Ud)^2\), and a repeated real root at equality.

**4. Sharp coexistence criterion.** On the positive equilibrium manifold, the variables \(q_j=b_jv_j^*/S\) satisfy \(q_j>0\), \(\sum_jq_j=1\), and \(B/S=\sum_jc_jq_j\). If at least two response rates differ, these strictly positive weighted means fill exactly the open interval \((c_{\min},c_{\max})\). Indeed any strictly interior target is realized by a strictly positive convex combination (put small positive weight on every nonextremal coordinate, then allocate the remainder to extreme coordinates). Every such equilibrium is selected by a nonstationary open set of positive initial data: continuity of the unique scalar root makes the terminal composition continuous, and one may initialize near the equilibrium with \(u(0)\ne U\). The discriminant has the same sign as \(\tau-B/S\). Therefore both strict signs occur precisely when \(c_{\min}<\tau<c_{\max}\), as claimed. If all \(c_j\) coincide, \(B/S\) is fixed and coexistence is impossible.

**5. Infinite focus crossings and finite node crossings.** In the focus case an invertible real linear coordinate change takes the planar linear part to \(-Ud/2\,I+\omega J\), where \(J\) is a quarter-turn and \(\omega=\sqrt{UB-U^2d^2/4}>0\). The nonlinear remainder is \(O(\|z,w\|^2)\). In polar coordinates near zero, \(\dot r=-Ud\,r/2+O(r^2)\) and \(\dot\varphi=\pm\omega+O(r)\). Step 2 places every nonstationary orbit eventually in that neighborhood; exponential decay makes \(r\) integrable. Consequently \(\varphi(t)=\pm\omega t+\varphi_\infty+o(1)\). The equation \(u-U=w=0\) is one fixed line through the transformed origin. Its intersections occur once per angular increment \(\pi\), giving \(N(T)=\omega T/\pi+O(1)\). No nonstationary orbit can reach the origin at a finite time, by uniqueness.

When the roots are real and distinct, the standard planar stable-node asymptotic-direction argument applies. In eigenvector coordinates \(\dot\xi_i=\lambda_i\xi_i+O(\|\xi\|^2)\): away from the one-dimensional strong-stable curve the slow eigenvector is the limiting direction, while on that curve the fast eigenvector is the limiting direction. This follows from variation of constants and the local invariant-curve theorem (equivalently, the planar stable-node phase portrait). Both eigenvectors of the displayed matrix have a nonzero \(w\) component because their eigenvalues are nonzero. Hence \(w(t)\) has a constant sign for all sufficiently large \(t\), so only finitely many level crossings occur. Analyticity and isolation of zeros away from equilibria rule out infinitely many crossings in an earlier compact time interval.

**6. The explicit boundary.** For the given parameters, \(S=2\) and \(B=v_1^*+9v_2^*=2+8w\). The discriminant is \(36-4(2+8w)=4(7-8w)\). Its zero is \(w=7/8\), at which \(v_1^*=9/8\). The first integral \(v_2/v_1^9\) is strictly increasing as a function of \(w\) on the equilibrium segment, so the exact initial-data dividing value is \(R_*= (7/8)/(9/8)^9\). In the focus basin, \(\omega^2=B-9=8w-7\). These calculations prove the asserted basin and crossing formulas.

## Verification

The standalone `check_star.py` recomputes the entropy-dissipation identity, a logarithmic first integral, the full three-species Jacobian characteristic polynomial, and the exact basin-divider arithmetic using symbolic expressions. It also integrates three finite trajectories to test their predicted terminal compositions and transverse spectral regimes. Run it with `python check_star.py` in an environment with SymPy and SciPy. Finite integration neither proves all-time convergence nor certifies infinitely many crossings; those follow from the preceding argument.

## Relationship to prior work

Du, Lu, Xu and Yang classify stably dissipative Lotka–Volterra interaction graphs and recall Volterra–Lyapunov/LaSalle and earlier global-convergence theory; the one-damped-center star is a natural graph in that framework. The global convergence mechanism is **not claimed as a general new theorem**, and the underlying dissipative foliation is established in older work by Redheffer, Zhou, Duarte and Peixe. The specific contribution assessed here is the complete *composition-selected* transverse node/focus criterion, the sharp multi-leaf coexistence condition, the all-trajectory asymptotic crossing clock in the focus basin, and the explicit invariant-defined three-species basin divider. The cited graph and rank results alone do not state this quantitative spectral/basin classification. The full journal text of Zhao and Luo (2010) was not available for comparison, leaving residual priority uncertainty.

## Limitations

The equations require a single damped central vertex, no leaf self-interaction, positive edge strengths and a positive reference equilibrium. The result does not describe arbitrary stably dissipative graphs, perturbed leaf self-damping, or the critical repeated-eigenvalue crossing count. The node/focus names refer to conserved leaves, not isolated full-phase equilibria. Published priority is provisional and no independent proof review has been performed.

## References

1. Y. Du, Z. Lu, J. Xu, M. Yang, *A complete classification for n-species Lotka–Volterra stably dissipative systems based on a generalized AHU algorithm*, arXiv:2611.00772v1 (public 2026-10-31), https://arxiv.org/html/2611.00772v1.
2. P. Duarte and T. Peixe, *Rank of Stably Dissipative Graphs*, arXiv:1104.0600 (2011); Linear Algebra and Its Applications 437 (2012), 2573–2586, https://arxiv.org/abs/1104.0600.
3. X. Zhao and J. Luo, *Classification and dynamics of stably dissipative Lotka–Volterra systems*, International Journal of Non-Linear Mechanics 45 (2010), 603–607, https://doi.org/10.1016/j.ijnonlinmec.2009.07.006.
4. R. Redheffer and Z. Zhou, *Global asymptotic stability for a class of many-variable Volterra prey–predator systems*, Nonlinear Analysis 5 (1981), 1309–1329, https://doi.org/10.1016/0362-546X(81)90108-5.
