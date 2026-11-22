# Sharp quadratic edge variation for centered maximal averaging on \(C_4\)

## Finding

Let \(C_4=K_{2,2}\) be the unweighted four-cycle with each undirected edge counted once. Define the centered graph-ball maximal operator and quadratic edge variation by
\[
(Mf)(v)=\max_{r=0,1,2}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|,
\qquad V_2(f)=\left(\sum_{\{v,w\}\in E(C_4)}|f(v)-f(w)|^2\right)^{1/2}.
\]
For every nonconstant complex-valued function on the four vertices,
\[
\boxed{V_2(Mf)\le C_*V_2(f),\qquad C_*^2=\lambda_*:=\frac{41+\sqrt{1537}}{144}.}
\]
The coefficient is optimal. Put \(\beta=(31+\sqrt{1537})/24\). All equality cases, modulo automorphisms of \(C_4\), are precisely
\[
(f(a_+),f(a_-),f(b_+),f(b_-))
=e^{i\theta}\bigl(c+2\beta h,\ c,\ c+(\beta-1)h,\ c+(\beta-1)h\bigr),
\quad c\ge0,\ h>0,\ \theta\in\mathbb R,
\]
where \(\{a_+,a_-\}\) and \(\{b_+,b_-\}\) are the opposite-vertex pairs.
Numerically, \(C_*\approx0.746308468618788\), strictly below \(3/4\), the known sharp first-variation constant on the same graph.

## Assumptions and scope

The graph is the simple, unweighted cycle with four vertices. Balls are closed graph-distance balls at radii zero, one, and two, averaged against counting measure. The input is any nonconstant function \(f:V(C_4)\to\mathbb C\), and every edge is counted exactly once. The theorem concerns individual-signal quadratic edge variation, not the global \(\ell^2\) norm of the maximal operator and not a two-input Lipschitz coefficient. The characterization includes arbitrary common phase and nonnegative additive modulus baseline; the zero entries carry no independent phase.

## Proof

**Reduction and coordinates.** Since \(M|f|=Mf\) and \(V_2(|f|)\le V_2(f)\), it suffices first to consider nonnegative real data. Permute vertices within each bipartition class and, if needed, exchange the classes to write their values as
\[
 f(a_\pm)=\mu+\frac{t}{2}\pm x,\qquad
 f(b_\pm)=\mu-\frac{t}{2}\pm y,\qquad t,x,y\ge0.
\]
For the classification, \(\mu\) is a common centering constant, not assumed nonnegative; only the displayed original vertex values are nonnegative. Every ball average translates by \(\mu\), so it can be omitted when computing edge differences. Direct calculation gives
\[
 V_2(f)^2=4(t^2+x^2+y^2).
\]
Writing \(Mf(a_\pm)=\mu+A_\pm\) and \(Mf(b_\pm)=\mu+B_\pm\), the three ball radii give
\[
 A_+=\frac t2+x,\quad A_-=(\tfrac t2-x)_+,\qquad
 B_+=\max\{\tfrac t6+\tfrac y3,\ y-\tfrac t2\},\quad
 B_-=(\tfrac t6-\tfrac y3)_+.
\]
The three independent output contrasts are
\[
 d=\frac{A_++A_--B_+-B_-}{2},\qquad
 u=\frac{A_+-A_-}{2},\qquad w=\frac{B_+-B_-}{2},
\]
so \(V_2(Mf)^2=4F\), where \(F=d^2+u^2+w^2\). Hence we must establish \(F\le\lambda_*(t^2+x^2+y^2)\) on the nonnegative parameter cone. The formulas have precisely six quadratic branches, according to \(x\le t/2\) or \(x\ge t/2\), and \(y\le t/2\), \(t/2\le y\le t\), or \(y\ge t\).

**Regions with \(x\le t/2\).** In the three successive \(y\)-regions, direct substitution yields
\[
\begin{aligned}
F_1&=t^2/9+x^2+y^2/9,\\
F_2&=13t^2/72+x^2+y^2/18-ty/9,\\
F_3&=5t^2/8+x^2+y^2/2-ty.
\end{aligned}
\]
Set \(Q=\lambda_*(t^2+x^2+y^2)-F\). Because \(x^2\le t^2/4\), the first two branches obey
\[
\begin{aligned}
Q_1&\ge(5\lambda_*/4-13/36)t^2+(\lambda_*-1/9)y^2,\\
Q_2&\ge(5\lambda_*/4-31/72)t^2+(\lambda_*-1/18)y^2+ty/9.
\end{aligned}
\]
All displayed coefficients are positive. For the third branch, substitute \(y=t+v\) with \(v\ge0\); then
\[
Q_3\ge(9\lambda_*/4-3/8)t^2+2\lambda_*tv+(\lambda_*-1/2)v^2.
\]
Again the coefficients are positive. Thus these regions have strict inequality for every nonconstant input.

**Regions with \(x\ge t/2\).** For \(y\le t/2\), \(F\) has the symmetric matrix
\[
E_{\mathrm{low}}=\begin{pmatrix}5/72&1/6&0\\1/6&1/2&0\\0&0&1/9\end{pmatrix}
\]
in coordinates \((t,x,y)\). The upper eigenvalue of its upper-left block is exactly \(\lambda_*\), since the block's characteristic equation is \(144z^2-82z+1=0\). The third eigenvalue \(1/9\) and the other block eigenvalue are strictly smaller. The top eigenvector is \((1,\beta,0)\), because \(\beta=24/(\sqrt{1537}-31)>1/2\). Consequently \(Q\ge0\) here, with equality exactly on the admissible ray \(t>0,x=\beta t,y=0\).

For \(t/2\le y\le t\), substitute \(x=t/2+u\), \(y=t/2+v\), where \(t,u,v\ge0\). The symmetric matrix of \(Q\) becomes
\[
Z_{\mathrm{mid}}=\begin{pmatrix}
(11+3\sqrt{1537})/288&(\sqrt{1537}-79)/288&(\sqrt{1537}+49)/288\\
(\sqrt{1537}-79)/288&(\sqrt{1537}-31)/144&1/12\\
(\sqrt{1537}+49)/288&1/12&(33+\sqrt{1537})/144
\end{pmatrix}.
\]
Its upper-left two-by-two block is positive definite, with determinant \((127-\sqrt{1537})/13824>0\). The remaining diagonal entry and both entries coupling \(v\) to \(t,u\) are strictly positive. Therefore \(Q>0\) on this cone away from the origin.

For \(y\ge t\), put \(x=t/2+u\), \(y=t+v\), again with \(t,u,v\ge0\). Now \(Q\) has matrix
\[
Z_{\mathrm{high}}=\begin{pmatrix}
(17+\sqrt{1537})/64&(\sqrt{1537}-67)/288&\lambda_*\\
(\sqrt{1537}-67)/288&(\sqrt{1537}-31)/144&1/4\\
\lambda_*&1/4&(\sqrt{1537}-31)/144
\end{pmatrix}.
\]
The upper-left two-by-two determinant equals \((383+\sqrt{1537})/10368>0\), with both diagonals positive. The remaining diagonal and its couplings are positive. Thus \(Q>0\) again outside the origin. All six regions are exhausted, including their boundaries.

**Equality.** The sole possible equality ray is \(t>0\), \(x=\beta t\), \(y=0\); subtracting its smallest original value produces exactly the announced \((2\beta t,0,(\beta-1)t,(\beta-1)t)\) profile, with arbitrary common nonnegative offset. Conversely this profile attains the upper-block eigenvalue and hence equality. For complex data, equality in \(V_2(|f|)\le V_2(f)\) forces equal phases at the endpoints of every edge with both endpoint moduli positive. The positive support of the stated profile is connected, so all positive entries share one phase, proving the complete complex equality classification.

## Verification

The algebraic checker supplied as `checker.py` independently expands all six branch quadratic forms using exact rational arithmetic, tests the defining eigenvalue identity and strict cone-sign inequalities, checks 5,000 deterministic nonnegative input samples by direct graph-ball computation, and tests the proposed equality ray. Run `python3 checker.py`; the expected output ends with `PASS` and prints the sharp constant. The exact general theorem and uniqueness depend on the analytical six-cone proof above, not on the finite sampling.

## Relationship to prior work

González-Riquelme, Kovač and Madrid (2026, arXiv:2603.12462v1, Theorem 2 and §3.1) prove that every four-vertex connected graph has sharp *first*-variation constant \(3/4\), explicitly treating the four-cycle. This does not imply the sharp quadratic edge-variation constant or its equality rays. Lu and Zhao (2026, arXiv:2611.24180v1) provide general graph bounds and sharp star-graph constants for all exponents, leaving the exact centered four-cycle quadratic constant beyond their theorems. Their star formula gives \(\sqrt{11}/4\) on the four-vertex star, contrasting with \(3/4\) on the complete graph and the value here. Earlier sharp strong \(\ell^2\) maximal-operator norms on the four-cycle concern vertex norms rather than edge variation; they do not determine this quotient. The distinction between centered graph-distance balls and uncentered arc averages is essential.

## Limitations

This is an exact result for a single canonical graph, not a formula for all cycles or all bicliques, and it is an individual-signal inequality rather than a two-input Lipschitz theorem. The quadratic-variation constant cannot be inferred from the \(\ell^2\) signal norm or the previously determined first-variation constant. Published results involving equivalent branchwise optimizations may exist outside the inspected sources; bibliographic originality is assessed only relative to the cited and searched record. No independent mathematical audit is asserted.

## References

1. S. Lu and F. Zhao, *Variational Estimates for the Hardy–Littlewood Maximal Operator on Finite Graphs*, arXiv:2611.24180v1, first public 18 November 2026. https://arxiv.org/html/2611.24180v1
2. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy-Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, first public 12 March 2026. https://arxiv.org/html/2603.12462v1
3. F. Liu, Y. Lian and Y. Wang, *Sharp \(L^p\) and variation inequalities for maximal operators on finite connected graphs*, arXiv:2611.15377v1, first public 11 November 2026. https://arxiv.org/html/2611.15377v1
4. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, Journal of Mathematical Analysis and Applications (2021), DOI: 10.1016/j.jmaa.2021.125647.
