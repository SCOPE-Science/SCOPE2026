# Sharp two-period metric-ratio barrier for convex-subspace three-operator splitting

## Finding

Consider the metric-proximal three-operator update (specified below) on the convex feasibility problem
\[\min_{x\in\mathbb R^2}\;\iota_U(x)+\iota_V(x),\qquad U=\operatorname{span}(e_1),\quad V=\operatorname{span}(e_2).\]
Fix \(-1<\rho<1\) and positive numbers \(s_0,s_1\). At even and odd iterations respectively, use the positive-definite metrics
\[M_{2j}=s_0\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad M_{2j+1}=s_1\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.\]
Set \(q=s_1/s_0\), and suppose the starting primal and dual variables satisfy \(z_0\in V\), \(u_0\in U\) (which includes the standard compatible initialization \(u_0\in\partial\iota_V(z_0)\)).

**Exact two-period classification.** If \(0<|\rho|<1\), all such trajectories converge to the zero saddle point if and only if
\[
q+q^{-1}<\frac{1+3\rho^4}{\rho^2(1-\rho^2)}.
\]
At equality there is a nonzero alternating mode of two-step multiplier \(-1\), so universal convergence fails without exponential growth. On the strict reverse inequality there are initializations whose primal and dual iterates diverge exponentially. If \(\rho=0\), the state \( (z_k,u_k)\) reaches zero after the first update, for any \(q>0\) (the auxiliary \(x_k\) may require one further update).

**Sharp uniform ratio threshold.** Uniform convergence for every \(\rho\in(-1,1)\) and every compatible initialization holds if and only if
\[
\max\{q,q^{-1}\}<3+2\sqrt2.
\]
At the boundary, \(|\rho|=1/\sqrt3\) produces a nonconvergent alternating mode; for larger contrast that same correlation produces exponential divergence. Thus two bounded, fixed positive-definite metrics can each yield a convergent stationary iteration, yet their unconstrained periodic alternation can fail. The metric-ratio restriction is a sharp statement for this two-dimensional orthogonal-line family, not a universal metric-variation condition for arbitrary convex problems.

## Assumptions and scope

The functions are \(f=0\), \(g=\iota_U\), and \(h=\iota_V\), where \(\iota\) is the extended-valued convex indicator. For any SPD metric \(M\), let \(\operatorname{prox}_{M,g}(v)=\arg\min_x[g(x)+\tfrac12(x-v)^TM(x-v)]\). The iteration is
\[
\begin{aligned}
x_{k+1}&=\operatorname{prox}_{M_k,g}(z_k-M_k^{-1}u_k),\\
z_{k+1}&=\operatorname{prox}_{M_k,h}(x_{k+1}+M_k^{-1}u_k),\\
u_{k+1}&=u_k+M_k(x_{k+1}-z_{k+1}).
\end{aligned}
\]
The same proximal/dual update is used in Suh--Isaac's variable-metric three-operator splitting when the smooth term vanishes, but **this work deliberately removes that algorithm's adjacent-metric proposal safeguard**. Its sufficient-decrease test is automatically satisfied because \(f=0\); the alternating proposals are not admissible under its stated asymptotically shrinking metric-comparability rule. The theorem does not contradict the published convergence results.

We consider the complete two-dimensional family \(s_0,s_1>0\), \(|\rho|<1\), and all compatible \((z_0,u_0)\); no assertion is made for generic nonlinear convex objectives or arbitrary nonscalar metric switching.

## Proof

Write \(M=s\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\), \(z=(0,t)^T\), \(u=(w,0)^T\). The weighted projections onto the coordinate axes are
\[
\operatorname{prox}_{M,\iota_U}(v)=(v_1+\rho v_2,0)^T,\qquad
\operatorname{prox}_{M,\iota_V}(v)=(0,v_2+\rho v_1)^T.
\]
Substitution into the three update equations gives
\[
x_{k+1}=\left(\rho t_k-\frac{w_k}{s},0\right)^T,
\quad t_{k+1}=\rho^2t_k-\frac\rho s w_k,
\quad w_{k+1}=s\rho(1-\rho^2)t_k+\rho^2w_k.
\]
In particular, the asserted primal--dual subspaces remain invariant, and \((t,w)\) evolves by
\[
T_s=\begin{pmatrix}\rho^2&-\rho/s\\s\rho(1-\rho^2)&\rho^2\end{pmatrix},
\qquad\det T_s=\rho^2.
\]
Rescaling \(w\) by \(s_0\) reduces the two-period map to \(P=T_qT_1\), whose invariants, with \(p=\rho^2\in(0,1)\), are
\[
\operatorname{tr}P=2p^2-p(1-p)(q+q^{-1}),\qquad \det P=p^2.
\]
For any real monic quadratic \(\lambda^2-\tau\lambda+\delta\) with \(0<\delta<1\), both roots have modulus less than one precisely when \(1-\tau+\delta>0\) and \(1+\tau+\delta>0\) (the degree-two Schur/Jury criterion). Here
\[
1-\operatorname{tr}P+\det P=(1-p)\big(1+p+p(q+q^{-1})\big)>0,
\]
whereas
\[
1+\operatorname{tr}P+\det P=1+3p^2-p(1-p)(q+q^{-1}).
\]
This proves the claimed strict stability criterion. At equality the characteristic polynomial has the roots \(-1\) and \(-p^2\), furnishing a nonzero alternating eigenvector. If the second expression is negative, the polynomial evaluated at \(-1\) is negative and has a real root below \(-1\), furnishing exponentially divergent initializations. Since \(T_1\) is invertible when \(\rho\ne0\), decay or nondecay of two-step states is equivalent to the corresponding statement about the whole sequence; the explicit formula for \(x\) transfers these conclusions to the primal iterates.

Finally, for \(0<p<1\), the exact algebraic identity
\[
\frac{1+3p^2}{p(1-p)}=6+\frac{(3p-1)^2}{p(1-p)}
\]
shows that the smallest fixed-correlation threshold is six, attained only at \(p=1/3\). The inequality \(q+q^{-1}<6\) is equivalent to \(3-2\sqrt2<q<3+2\sqrt2\), or \(\max\{q,q^{-1}\}<3+2\sqrt2\). Equality and failure follow from the explicit eigenvalue behavior above. When \(\rho=0\), \(T_s=0\) directly.

## Verification

The attached `verify.py` independently reconstructs both metric proximal projections from the symbolic inverse metric, checks the invariant two-by-two state recursion, the period-product trace and determinant, the Schur endpoint identities, and the sharp minimization identity. It also tests 95 exact-rational stable combinations and verifies an explicit divergent rational example:
\[
\rho=\frac35,\quad q=6,\quad P=\begin{pmatrix}57/625&-63/250\\3024/3125&-783/625\end{pmatrix},
\quad\operatorname{spec}(P)=\left\{\frac{-363\pm42\sqrt{46}}{625}\right\}.
\]
The negative eigenvalue is below \(-1\), and \(\det(I+P)=-4/125\). The certificate returned `VERIFY_OK exact prox reduction, two-period spectrum, sharp threshold, critical endpoint, rational divergence witness, 95 rational-grid cases`. The mathematical proof of universal statements is the displayed analytic derivation, not the finite checks.

## Relationship to prior work

Suh and Isaac's 2026 variable-metric three-operator splitting provides the exact proximal/dual update used here and explicitly controls the relationship between successive metric proposals (Algorithm 1, line 15, and Theorem 3.5). It does not assert convergence for the unrestricted periodic switching studied here. Lorenz and Tran-Dinh (2018) analyze nonstationary Douglas--Rachford and ADMM under convergent stepsizes with summable increments; their convergence guarantees do not cover alternating unequal scales. Pedregosa and Gidel (2018) analyze safeguarded adaptive three-operator splitting. The fixed-metric subspace contraction theory describes each stationary map, not its switched product. The precise two-cycle polynomial and universal contrast \(3+2\sqrt2\) were not identified in the inspected sources; that negative literature comparison does not establish priority exhaustively.

## Limitations

The positivity and symmetry of both metrics, the 2-period pattern, the fixed correlation shape, exact arithmetic, and the indicator functions of orthogonal lines are essential to the stated classification. The result does not disprove any safeguard-respecting VMTOS theorem. The criterion concerns convergence for **every** compatible initialization; special initializations may converge at or beyond the boundary. It does not establish a sufficient condition for arbitrary sequences of changing metrics. Independent verification and a complete historical-priority audit have not been performed.

## References

1. H. Suh and T. Isaac, *Variable Metric Three Operator Splitting*, arXiv:2610.38935v1 (first submitted October 28, 2026), https://arxiv.org/html/2610.38935v1.
2. D. A. Lorenz and Q. Tran-Dinh, *Non-stationary Douglas--Rachford and alternating direction method of multipliers: adaptive stepsizes and convergence*, 2018 preprint, arXiv:1801.03765, https://optimization-online.org/wp-content/uploads/2018/01/6421.pdf.
3. F. Pedregosa and G. Gidel, *Adaptive Three Operator Splitting*, ICML/PMLR 80 (2018), https://proceedings.mlr.press/v80/pedregosa18a.html.
4. H. H. Bauschke, J. Y. Bello Cruz, T. T. A. Nghia, H. M. Phan, and X. Wang, *The rate of linear convergence of the Douglas--Rachford algorithm for subspaces is the cosine of the Friedrichs angle*, arXiv:1309.4709, https://arxiv.org/abs/1309.4709.
