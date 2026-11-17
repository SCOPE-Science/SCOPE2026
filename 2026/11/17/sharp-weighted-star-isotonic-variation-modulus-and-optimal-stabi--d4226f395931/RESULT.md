# Sharp weighted star isotonic variation modulus and optimal stabilizing edge weights

## Finding
Let \(m\ge2\), let \(\mu_0,\mu_1,\ldots,\mu_m>0\) and \(v_1,\ldots,v_m>0\). On real vertex data \(x=(x_0,\ldots,x_m)\), define the rooted-star isotonic least-squares map
\[
P_\mu x=\mathop{\arg\min}_{z_0\le z_i\ (1\le i\le m)}\frac12\sum_{i=0}^m\mu_i(z_i-x_i)^2,
\]
and the weighted edge-variation seminorm \(V_v(h)=\sum_{i=1}^m v_i|h_i-h_0|\). Its **sharp attained two-input variation modulus** is
\[
\boxed{\operatorname{Lip}_{V_v}(P_\mu)=\max\left\{1,\max_{1\le i\le m}\frac{\mu_i\sum_{j\ne i}v_j}{(\mu_0+\mu_i)v_i}\right\}.}
\]
In particular \(P_\mu\) is variation nonexpansive exactly when
\[
\boxed{\sum_{i=1}^m\frac{\mu_i}{\mu_0+2\mu_i}\le1}
\]
**for some** positive choice of edge weights \(v\); for a fixed choice, the necessary and sufficient inequalities are \(\mu_i\sum_{j\ne i}v_j\le(\mu_0+\mu_i)v_i\) for all \(i\).

The best attainable modulus over all positive edge weights is \(\max\{1,\rho_*\}\), where \(\rho_*>0\) is the unique solution of
\[
\sum_{i=1}^m\frac{\mu_i}{\rho_*(\mu_0+\mu_i)+\mu_i}=1.
\]
The strictly positive weights \(v_i^*=\mu_i/[\rho_*(\mu_0+\mu_i)+\mu_i]\), normalized to sum to one, attain this optimum and uniquely minimize the untruncated auxiliary amplification \(\max_i \mu_i(\sum_{j\ne i}v_j)/[(\mu_0+\mu_i)v_i]\). If \(\rho_*\ge1\), this optimizer is also the unique normalized minimizer of the actual Lipschitz modulus; if \(\rho_*<1\), every normalized positive vector satisfying the fixed-weight nonexpansivity inequalities is optimal.

For unit-mass leaves, a positive stabilizing variation weighting exists exactly when \(\mu_0\ge m-2\); in this case equal variation weights already achieve nonexpansivity. For \(\mu_0<m-2\) no positive edge weighting can prevent amplification. This is a sharp root-mass threshold for branching stars.

For equal observation masses and equal variation weights, the formula reduces to \(\max\{1,(m-1)/2\}\); this unweighted specialization follows from earlier unweighted-tree classifications and is not presented as a new result.

## Assumptions and scope
The star has one root \(0\), \(m\ge2\) leaves, and all directed inequalities point from the root to its leaves. All vertex least-squares masses \(\mu_i\) and edge-variation weights \(v_i\) are finite, real and strictly positive. Input vectors are arbitrary real vectors. The modulus is the supremum of \(V_v(P_\mu x-P_\mu y)/V_v(x-y)\) over \(V_v(x-y)>0\). Translation invariance \(P_\mu(x+c\mathbf1)=P_\mu x+c\mathbf1\) ensures the map descends to the finite-dimensional quotient by constant vectors, whose weighted variation seminorm is a norm.

## Proof
**1. Piecewise-affine root representation.** Fix an input \(x\). Given the root fit \(c\), the optimal leaf fit is \(z_i=\max\{x_i,c\}\). The strictly convex scalar objective
\[
\Phi_x(c)=\tfrac12\mu_0(c-x_0)^2+\tfrac12\sum_{i=1}^m\mu_i(\max\{x_i,c\}-x_i)^2
\]
has a unique minimizer. In a chamber where \(S=\{i:x_i<c\}\), differentiation gives
\[
c=\frac{\mu_0x_0+\sum_{i\in S}\mu_i x_i}{\mu_0+\sum_{i\in S}\mu_i}.
\]
Consequently the projection is continuous, piecewise affine, and has finitely many chambers indexed by \(S\subseteq\{1,\ldots,m\}\). Every subset occurs on a nonempty open chamber: take \(x_0=0\), \(x_i=-2\) for \(i\in S\), and \(x_j=2\) otherwise. The cases \(S=\varnothing\) and \(S\) equal to all leaves are included.

**2. Exact derivative norms.** Write \(d_i=x_i-x_0\), let \(M_S=\mu_0+\sum_{i\in S}\mu_i\), and consider a perturbation in \(d\)-coordinates. On chamber \(S\), the output root-to-leaf differences are
\[
(P_\mu x)_j-(P_\mu x)_0=\begin{cases}0,&j\in S,\\d_j-\sum_{i\in S}(\mu_i/M_S)d_i,&j\notin S.\end{cases}
\]
The induced norm between weighted \(\ell^1\) coordinate spaces is the largest weighted absolute column sum of this matrix, namely
\[
\max\left(\{1:j\notin S\}\cup\left\{\frac{\mu_i\sum_{j\notin S}v_j}{M_Sv_i}:i\in S\right\}\cup\{0\}\right).
\]
For each \(i\in S\), the latter ratio is bounded by \(\mu_i\sum_{j\ne i}v_j/[(\mu_0+\mu_i)v_i]\), because enlarging \(S\) increases the denominator and decreases the complementary weight sum. The no-pooling chamber gives norm one. Each singleton chamber \(S=\{i\}\) attains its displayed ratio by varying only \(d_i\) through a sufficiently short segment inside that chamber. Joining arbitrary inputs by a line segment across finitely many chambers proves the global upper bound. The singleton and no-pooling witnesses prove exact finite attainment.

**3. Stabilization and optimal weights.** Put \(t_i=\mu_i/(\mu_0+\mu_i)\) and normalize \(\sum_i v_i=1\). The nontrivial portion of the modulus is
\[
R(v)=\max_i t_i\frac{1-v_i}{v_i}.
\]
For \(\rho>0\), \(R(v)\le\rho\) is equivalent to \(v_i\ge t_i/(\rho+t_i)\) for all \(i\). Such positive normalized weights exist if and only if \(F(\rho):=\sum_i t_i/(\rho+t_i)\le1\). For \(m\ge2\), \(F\) decreases continuously and strictly from \(m\) to zero; therefore it has exactly one root \(\rho_*>0\), and its equality weights are the unique minimizer of \(R\). Taking \(\rho=1\) yields the stated existence condition because \(t_i/(1+t_i)=\mu_i/(\mu_0+2\mu_i)\). The remaining statements about \(\operatorname{Lip}=\max\{1,R\}\) follow directly. This also proves the optimality and uniqueness assertions without numerical optimization.

## Verification
The included standalone `check_star.py` uses Python standard-library exact rational arithmetic. It independently evaluates all active subsets and their weighted matrix norms for 280 positive-mass/weight test instances with two through eight leaves, checks explicit finite extremal pairs, and tests 11,200 weighted finite-pair comparisons and face-related identities. It separately checks the equal-mass degree transition through twelve leaves. Execute `python check_star.py` with Python 3. These finite checks corroborate, but do not replace, the proof for arbitrary positive weights and all finite star degrees.

## Relationship to prior work
Agarwal, Phillips and Sadri (arXiv:0912.5182v1, publicly submitted 28 December 2009), in their full sections on paths and rooted trees, develop algorithms for tree isotonic and Lipschitz-isotonic fitting, not weighted edge-variation perturbation constants or minimax selection of variation weights. A. B. Németh and S. Z. Németh (arXiv:1503.08458v1, submitted 29 March 2015) study order-isotonic projections of regression cones; their order preservation concerns coordinatewise inequalities between inputs, not sharp variation of a difference of two projections. An existing unweighted-tree variation classification already entails the uniform-star special case and is not claimed as novel. Known variation results for isotonic regression on paths or cycle-cover orders use different topologies; their formulas do not imply the arbitrary-mass weighted-star result or the new optimal edge-weight design. Exact historical priority remains subject to the listed risks.

## Limitations
Only depth-one rooted stars with a common minimum-root constraint, positive squared-error masses and positive edge-total-variation weights are treated. The formula does not address reverse or mixed orientations, non-star trees, other regression loss functions, statistical risk, or numerical stability under finite precision. The general equal-mass/unweighted-edge star special case is already known. Independent external mathematical validation has not been undertaken.

## References
- Agarwal, P. K., Phillips, J. M., and Sadri, B., *Lipschitz Unimodal and Isotonic Regression on Paths and Trees*, arXiv:0912.5182v1 (publicly submitted 2009-12-28), https://arxiv.org/html/0912.5182v1 .
- Németh, A. B., and Németh, S. Z., *Isotonic regression and isotonic projection*, arXiv:1503.08458v1 (publicly submitted 2015-03-29), https://arxiv.org/abs/1503.08458 .
- AMS Mathematics Subject Classification 2020, code 47H09, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=47H .
