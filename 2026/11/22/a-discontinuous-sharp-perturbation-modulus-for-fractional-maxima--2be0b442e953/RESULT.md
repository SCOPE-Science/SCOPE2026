# A discontinuous sharp perturbation modulus for fractional maximal averaging on the three-vertex path

## Finding

Let \(P_3\) be the unweighted three-vertex path with central vertex \(0\) and leaves \(1,2\), and let \(M_\alpha\) be centered fractional Hardy–Littlewood averaging with counting measure and \(0<\alpha<1\). For arbitrary complex vertex signals \(f,g\), put
\[
V_2(F)^2=|F(1)-F(0)|^2+|F(2)-F(0)|^2,
\qquad
L_\alpha=\sup_{f\ne g}\frac{V_2(M_\alpha f-M_\alpha g)}{\|f-g\|_{\ell^2(P_3)}}.
\]
Set \(a=2^{\alpha-1}\), \(h=3^{\alpha-1}\), and let \(\alpha_*\in(0,1)\) be the unique solution of
\[
2^{\alpha_*-1}+3^{\alpha_*-1}=1.
\]
Then the **exact sharp two-input stability law** is
\[
\boxed{
L_\alpha^2=
\begin{cases}
\displaystyle\frac{3-2h+3h^2+\sqrt{(1+2h-3h^2)^2+4}}{2}, & 0<\alpha<\alpha_*,\\[6pt]
2-4h+6h^2, & \alpha_*\le\alpha<1.
\end{cases}}
\]
Every value is attained by two distinct **strictly positive real** signals. In particular, the best Lipschitz constant jumps down at the interior exponent:
\[
\alpha_*=0.212115088974\ldots,\qquad
\lim_{\alpha\uparrow\alpha_*}L_\alpha=1.593842169144\ldots,
\qquad L_{\alpha_*}=\lim_{\alpha\downarrow\alpha_*}L_\alpha=1.174412023764\ldots.
\]
Here the left limit uses \(\alpha<\alpha_*\) and the right limit uses \(\alpha>\alpha_*\). Thus \(\alpha\mapsto M_\alpha\) is continuous as a finite-dimensional nonlinear map on bounded inputs, but its *global two-input Lipschitz modulus* is discontinuous.

## Assumptions and scope

For \(u=(x,y,z)\in[0,\infty)^3\) write \(S=x+y+z\). The standard centered ball definition is
\[
(M_\alpha f)(v)=\max_{r\ge0}|B(v,r)|^{\alpha-1}\sum_{w\in B(v,r)}|f(w)|.
\]
At the hub and leaves respectively this becomes
\[
(M_\alpha u)(0)=\max\{x,hS\},\quad
(M_\alpha u)(1)=\max\{y,a(x+y),hS\},\quad
(M_\alpha u)(2)=\max\{z,a(x+z),hS\}.
\]
Every undirected edge is counted once in \(V_2\), and the input is measured in unnormalized vertex \(\ell^2\). There are no restrictions on the phases of the complex inputs. The finding concerns this *two-input vertex-to-edge* norm, not the usual one-input inequality with edge variation on both sides.

## Proof

**1. Reduction to feasible linear pieces.** Since \(M_\alpha f=M_\alpha|f|\) and \(\||f|-|g|\|_2\le\|f-g\|_2\), it suffices for the upper bound to consider \(u,v\ge0\). On each strict selection cell, \(B M_\alpha u=Du\), where \(B\) has rows \((-1,1,0)\) and \((-1,0,1)\). A line segment in the nonnegative orthant has finitely many linear pieces; hence the global Lipschitz coefficient is bounded by the largest Euclidean operator norm of \(D\) on a feasible strict cell. Lower bounds come from perturbing an interior point of a cell in a top right-singular-vector direction. Lower-dimensional tie sets cannot increase the global modulus because the map is continuous and is piecewise linear.

Use symbols \(O,P,G\) for, respectively, a singleton, two-point-ball, or full-graph branch at a leaf; use \(O,G\) at the hub. Since \(\beta=1-\alpha\in(0,1)\), we have \(1/2<a<1\), \(1/3<h<a<1\). Strict concavity and strict subadditivity give
\[
2\cdot2^\beta>1+3^\beta,
\qquad 2^\beta+1>3^\beta.
\]
The first is equivalent to \(2h/a-1>h\); the second to \(h(1+a)>a\).

**2. Infeasible selector combinations.** If the hub selects \(O\) and a leaf selects \(O\), then \(x\ge hS\) and that leaf's value is at least \(ax/(1-a)\). If both leaves select \(O\), these inequalities force \(h\le(1-a)/(1+a)<1/3\), impossible. If the other leaf selects \(P\), normalize by \(x>0\) and put \(t=z/x\). The hub-singleton and leaf-pair inequalities, together with \(y\ge ax/(1-a)\), yield
\[
h\le\frac{\min\{1,a(1+t)\}}{1/(1-a)+t}
\le\frac{a(1-a)}{1-a+a^2}\le\frac13.
\]
Indeed, the first expression increases until \(t=(1-a)/a\) and decreases thereafter; the last inequality follows from \(3a(1-a)\le1-a+a^2\), equivalently \((2a-1)^2\ge0\). This contradicts \(h>1/3\). For the remaining possibility \((O;O,G)\), a necessary condition is \(h\le1-a\). Strict-cell feasibility requires \(h<1-a\), equivalent to \(\alpha<\alpha_*\).

If the hub selects \(G\), a leaf selecting \(O\) and the other selecting \(P\) would force \(S\ge hS+(h/a)S>S\), using \(h(1+a)>a\). If both leaves select \(P\), adding their pair inequalities gives \(x\ge(2h/a-1)S>hS\), contradicting the hub's \(G\) selection. Thus, up to leaf exchange, the only possibly nondegenerate pieces are
\[
\begin{array}{ll}
\text{hub }O:&(O,G)\text{ only when }a+h<1,\ (P,P),\ (P,G),\ (G,G),\\
\text{hub }G:&(O,O),\ (O,G),\ (P,G),\ (G,G).
\end{array}
\]
No assertion that all listed lesser branches have open cells is needed.

**3. Spectral bound on all remaining pieces.** Put
\[
o=(-1,1,0),\quad p=(a-1,a,0),\quad
r=(h-1,h,h),\quad t=\|r\|_2^2=1-2h+3h^2.
\]
The \((O;O,G)\) branch has output rows \(o,r\), with \(\|o\|_2^2=2\) and \(\langle o,r\rangle=1\). Its largest squared singular value is exactly
\[
A(h)=\frac{3-2h+3h^2+\sqrt{(1+2h-3h^2)^2+4}}2.
\]
The \((O;G,G)\) branch repeats the row \(r\), and its squared norm is
\[
H(h)=2t=2-4h+6h^2.
\]
We show that every other surviving piece has squared norm at most \(H(h)\). With the hub selecting \(O\), two \(P\)-rows have squared norm \(a^2+2(1-a)^2\le1<H(h)\); one \(P\)-row and one \(G\)-row have squared norm at most their sum of squared row lengths, \(\|p\|_2^2+t\le2t=H(h)\). For the last inequality, if \(h\ge2/3\), then \(t\ge1\ge\|p\|_2^2\). If \(h\le2/3\), use \(h\le a\le3h/2\), convexity of \((1-a)^2+a^2\), and its two endpoint values; both are at most \(t\) because their deficits are \(h^2\) and \(h(1-3h/2)\).

With the hub selecting \(G\), an \(O\)-leaf gives the row \((-h,1-h,-h)\), of squared norm \(t\); a \(P\)-leaf gives \((a-h,a-h,-h)\), of squared norm \(2(a-h)^2+h^2\le2(1-h)^2+h^2\le H(h)\); a \(G\)-leaf gives zero. The \((G;O,O)\) two-row Gram matrix has eigenvalues \(1\) and \(H(h)-1\), each no larger than \(H(h)\), since \(H(h)\ge4/3\). This proves the bound for every feasible selection.

**4. Attainment and the phase boundary.** The region \((O;G,G)\) is open and nonempty for every \(0<\alpha<1\): normalize \(S=1\), choose
\[
h<x<\frac{2h}{a}-1,\qquad y=z=\frac{1-x}{2}.
\]
Strict concavity guarantees the interval is nonempty. Both leaves strictly prefer the global branch to their singleton and two-point branches, while the hub prefers its singleton branch. A sufficiently small perturbation along \(r\) gives exactly the ratio \(\sqrt{H(h)}\).

If \(a+h<1\), the \((O;O,G)\) region is also open and nonempty. For \(S=1\), start with
\[
x=h,\qquad y=\frac{ah}{1-a},\qquad z=1-\frac h{1-a}>0,
\]
and then take \(x=h+\varepsilon\), \(y=a x/(1-a)+\varepsilon\), \(z=1-x-y\) for sufficiently small \(\varepsilon>0\). The remaining leaf strictly prefers its global branch: at the starting point \(h>z\) and \(h>a(x+z)\), since \(h>1/3\) and \(a(1-a)/(1-a+a^2)\le1/3\); these inequalities persist under a sufficiently small perturbation. The hub and first leaf then strictly prefer singleton branches. Perturbing this positive signal along the top singular vector of rows \(o,r\) attains \(\sqrt{A(h)}\).

For \(a+h<1\), \(h<1/2\), so \(A(h)\ge2>H(h)\). For \(a+h\ge1\), the high-gain \((O;O,G)\) cell is impossible and all remaining cells have squared norm at most \(H(h)\), attained as above. This gives the stated two-branch formula. The strict monotonicity of \(a+h\) establishes the uniqueness of \(\alpha_*\); substitution at the boundary gives the two distinct one-sided values. \(\square\)

## Verification

Run the standalone standard-library checker with `python3 checker.py`. It independently constructs the graph-ball branches and the two-row Gram eigenvalues, verifies strict positive witnesses at parameter values on both sides of the transition, checks 110,000 randomized branch/difference cases, and prints the transition values. These finite calculations are diagnostic tests, **not** substitutes for the universal analytic proof. The displayed decimals are numerical evaluations of the exact formulas; no formal computer-assisted proof or independent mathematical certification is asserted.

## Relationship to prior work

Liu–Lian–Wang (arXiv:2611.15377v1; first public 2026-11-11), especially its fractional star-graph one-input variation estimates and Section 4, motivates the question. Their variation constants compare \(V_p(M_\alpha f)\) with \(V_q(f)\) for one input, whereas this result concerns \(V_2(M_\alpha f-M_\alpha g)\) divided by a vertex \(\ell^2\) difference. The distinction cannot be removed by substituting \(f-g\), since \(M_\alpha\) is nonlinear.

González-Riquelme–Kovač–Madrid (arXiv:2603.12462v1) and Lu–Zhao (arXiv:2611.24180v1 and 2611.24189v1, first public 2026-11-18) also concern one-input variation. An already available exact ordinary-maximal two-input star norm determines \(\alpha=0\), and previously established fractional star bounds determine a large-degree asymptotic, but neither implies the full interior-exponent piecewise formula or the jump at \(2^{\alpha-1}+3^{\alpha-1}=1\). A published sharp variation result for a weighted three-vertex path uses another normalization and is likewise not an exact vertex-to-edge two-input fractional estimate. Priority is assessed against the inspected work; an unindexed equivalent treatment is a residual risk.

## Limitations

The exact formula is for the **three-vertex path** only, with counting-measure balls and quadratic vertex-to-edge norms. No formula for other path lengths, arbitrary weights, or edge-to-edge two-input norms is asserted. The discontinuity refers to the *optimal global Lipschitz constant* rather than discontinuity of \(M_\alpha f\) for fixed input. Independent audit is not yet performed.

## References

1. F. Liu, Y. Lian, Y. Wang, *Sharp \(L^p\) and variation inequalities for maximal operators on finite connected graphs*, arXiv:2611.15377v1, first public 2026-11-11. https://arxiv.org/abs/2611.15377
2. C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, first public 2026-03-12. https://arxiv.org/abs/2603.12462
3. S. Lu, F. Zhao, *Variational Estimates for the Fractional Maximal Operator on Finite Graphs*, arXiv:2611.24189v1, first public 2026-11-18. https://arxiv.org/abs/2611.24189
4. S. Lu, F. Zhao, *Variational Estimates for the Hardy–Littlewood Maximal Operator on Finite Graphs*, arXiv:2611.24180v1, first public 2026-11-18. https://arxiv.org/abs/2611.24180
5. C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, J. Math. Anal. Appl. 506 (2022), 125647. https://doi.org/10.1016/j.jmaa.2021.125647
