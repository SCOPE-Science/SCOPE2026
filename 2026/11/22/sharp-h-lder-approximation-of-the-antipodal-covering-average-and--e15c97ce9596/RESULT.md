# Sharp Hölder approximation of the antipodal covering average and a term-count reversal

## Finding
Let \(X=\mathbb R/\mathbb Z\) and \(Y=\mathbb R/(2\mathbb Z)\), with the connected two-sheet map \(q(y)=y\pmod 1\). Give \(Y\) its geodesic distance \(\rho(y,z)=\min_{\ell\in\mathbb Z}|y-z+2\ell|\), whose diameter is one. Let \(\phi:[0,1]\to[0,1]\) be continuous, strictly increasing, strictly concave, with \(\phi(0)=0\) and \(\phi(1)=1\), and equip \(Y\) with the snowflaked/concavely transformed metric \(d_\phi=\phi\circ\rho\). Define the fiber average \((Af)(x)=\bigl(f(x)+f(x+1)\bigr)/2\). For each integer \(m\ge1\) let
\[
E_m(\phi)=\inf_{h_1,\ldots,h_m\in C(X,Y)}\ \sup_{[f]_{\mathrm{Lip}(Y,d_\phi)}\le1}
\left\|Af-\frac1m\sum_{j=1}^{m}f\circ h_j\right\|_{C(X)}.
\]
Then the infimum is attained and
\[
\boxed{E_m(\phi)=\begin{cases}\phi(1/2)/m,&m\ \text{odd},\\1/m,&m\ \text{even}.\end{cases}}
\]
In particular, for each Hölder exponent \(0<\alpha<1\), with \(\phi(s)=s^\alpha\),
\[
\boxed{E_{2k+1}(\alpha)=\frac{2^{-\alpha}}{2k+1},\qquad E_{2k+2}(\alpha)=\frac1{2k+2}.}
\]
For every integer \(k\ge1\), adding one equal-weight composition term from \(2k+1\) to \(2k+2\) **increases** the optimal error precisely when
\[
\alpha>\log_2\!\left(\frac{2k+2}{2k+1}\right).
\]
Equality occurs at that threshold; below it the error decreases. For every fixed \(0<\alpha<1\), there are infinitely many such increases: they occur for all \(k\) with \(2k+1>(2^\alpha-1)^{-1}\). For example, at \(\alpha=1/2\) the best three-term error is \(\sqrt2/6\), strictly smaller than the best four-term error \(1/4\).

## Assumptions and scope
All functions and operator norms are real-valued. The Lipschitz constant is the seminorm of \(f\) with respect to \(d_\phi\); the error operator annihilates constants, so the displayed supremum is finite and may equivalently be taken on the quotient by constants. The \(m\) maps are continuous, may repeat, and have *exactly equal coefficients* \(1/m\); no regularity constraint is imposed on the maps beyond continuity. The infimum is over all such labelled families, without assuming they are fiberwise sections.

The distance \(d_\phi\) is a metric: positivity and symmetry are immediate. For a triangle with consecutive geodesic distances \(s,t\), if \(s+t\le1\), concavity, monotonicity, and \(\phi(0)=0\) yield \(\phi(\rho(u,w))\le\phi(s+t)\le\phi(s)+\phi(t)\). If \(s+t>1\), concavity and normalized endpoints give \(\phi(s)+\phi(t)\ge s+t>1\ge\phi(\rho(u,w))\).

## Proof
**1. Transport reduction.** At \(x\in X\), put \(a=x\), \(b=x+1\) in \(Y\), and let \(\mu_x=(\delta_a+\delta_b)/2\), \(\nu_x=m^{-1}\sum_j\delta_{h_j(x)}\). On a compact metric space, Kantorovich–Rubinstein duality yields
\[
\sup_{[f]_{\mathrm{Lip}(d_\phi)}\le1}\left|\int f\,d(\mu_x-\nu_x)\right|
 =W_1^{d_\phi}(\mu_x,\nu_x).
\]
Taking the supremum over \(x\) commutes with the supremum over \(f\), hence each family has operator error \(\sup_xW_1^{d_\phi}(\mu_x,\nu_x)\). Note that \(d_\phi(a,b)=1\).

**2. Odd-term lower bound.** Parametrize the base by \(t\in[0,1]\). For each labelled map define the relative position \(u_j(t)=h_j([t])-t\pmod2\) and the continuous distance \(r_j(t)=\rho(u_j(t),0)\). As \(h_j([1])=h_j([0])\), one has \(u_j(1)=u_j(0)-1\pmod2\), hence \(r_j(1)=1-r_j(0)\). The intermediate-value theorem produces \(t_j\) with \(r_j(t_j)=1/2\). At that base point, the entire mass \(1/m\) of the \(j\)-th sample lies at distance \(\phi(1/2)\) from *both* target fiber atoms. Every transport plan therefore spends at least \(\phi(1/2)/m\). This bound holds for every \(m\); it is sharp for odd \(m\) by Step 4.

**3. Even-term lower bound.** Put \(m=2k\). At a fixed \(t\), write \(c_j^a(t)=d_\phi(h_j(t),a(t))\) and \(c_j^b(t)=d_\phi(h_j(t),b(t))\). Sending each of the \(m\) source atomic units to either of two sinks with capacity \(k\) units is a linear program whose admissible fraction polytope is \(\{v\in[0,1]^m:\sum_jv_j=k\}\). Every vertex is a zero–one vector (otherwise two fractional coordinates could be perturbed); thus
\[
mW_1^{d_\phi}(\mu_t,\nu_t)=\min_{S\subseteq\{1,\ldots,m\},\ |S|=k}F_S(t),\quad
F_S(t)=\sum_{j\in S}c_j^a(t)+\sum_{j\notin S}c_j^b(t).
\]
For distinct \(k\)-subsets \(S,T\), the symmetric difference has at least two members; each member contributes \(c_j^a+c_j^b\ge d_\phi(a,b)=1\) to \(F_S+F_T\). Therefore \(F_S+F_T\ge2\). Whenever \(\min_S F_S(t)<1\), its minimizing subset is unique. If a family had global error strictly below \(1/m\), the minimizing subset would be unique at every \(t\), and by finiteness and continuity it would be constant along \([0,1]\). But the labels close around the circle while the ordered target sheets interchange, giving \(F_S(1)=F_{S^c}(0)\). Uniqueness would force its endpoint minimizer to be the complement of its starting minimizer, an impossibility for a fixed nonempty subset. Thus every even-term family has error at least \(1/m\).

**4. Sharp continuous constructions.** Use relative positions in \(\mathbb R/(2\mathbb Z)\), so a relative coordinate zero represents the first fiber point and one the second. Divide the parameter interval into \(m\) successive subintervals. On each, move exactly one *labelled* relative coordinate linearly from zero to one or from one to zero, leaving the other relative coordinates fixed. Every label moves exactly once, and each terminal coordinate equals one minus its starting coordinate. Consequently the physical maps \(h_j([t])=t+u_j(t)\pmod2\) satisfy \(h_j([1])=h_j([0])\) and descend to continuous maps on \(X\).

If \(m=2k+1\), begin with \(k+1\) labels at zero and \(k\) at one, moving alternately one zero-to-one label and one one-to-zero label and finishing with a zero-to-one label. Throughout any move there are \(k\) stationary labels at each fiber point. Their mass leaves a deficit \(1/(2m)\) at each sink, so split the moving atom equally between the sinks. At relative position \(s\in[0,1]\) the resulting transport cost is
\[
\frac{\phi(s)+\phi(1-s)}{2m}\le\frac{\phi(1/2)}m
\]
by concavity. Its maximum, attained at the midpoint of a move, equals the odd lower bound.

If \(m=2k\), begin with \(k\) labels at each fiber point, successively moving one zero-to-one label and then one one-to-zero label, repeating for all \(k\) pairs. During each move, \(k-1\) stationary atoms occupy the first fiber and \(k\) occupy the second. Send the moving atom entirely to the first fiber, at a cost at most \(d_\phi(a,b)/m=1/m\). This attains the even lower bound. All formulas remain valid at \(m=1\) and \(m=2\).

**5. Regularity-driven count reversal.** In the Hölder specialization, \(E_{2k+2}>E_{2k+1}\) is equivalent to \(2^\alpha>(2k+2)/(2k+1)\), giving exactly the stated threshold. The threshold belongs to \((0,1)\) precisely for \(k\ge1\). Equivalently, for each fixed \(0<\alpha<1\), all integers \(k\ge1\) with \(2k+1>(2^\alpha-1)^{-1}\) exhibit a strict increase, yielding infinitely many parity-induced reversals.

## Verification
The proof is analytic for all integers \(m\ge1\) and every admissible \(\phi\). The standalone `CHECK.py` uses finite extreme-point enumeration for the two-sink transport problem and checks the explicit continuous labelled paths for \(m=1,\ldots,9\), several strict-concavity profiles, and the arclength boundary case. Executing it with the Python standard library prints `CONCAVE_CIRCLE_TRANSPORT_DIAGNOSTIC_OK 2799`. This finite diagnostic is supplementary and does not certify the infinite family or bibliographic novelty.

## Relationship to prior work
Duru, İlter and Bilgin (2026) determine exact approximation errors of covering-graph fiber averages on \(C(Y)\) with the **supremum-norm operator topology**, using total-variation distances. Their norm and transport objective differ from the present Lipschitz-to-continuous error, where the dual is Wasserstein transport for a concave metric transform. The previously established intrinsic-arclength two-circle result gives the linear-cost endpoint \(\phi(s)=s\), with odd error \(1/(2m)\) and even error \(1/m\). That already-known endpoint is *not* asserted as new; the statement here concerns strictly concave metrics, their exact dependence on \(\phi(1/2)\), and the sharp Hölder-regularity threshold for an increase in the optimal error when one map is added. General topological approximation arguments do not by themselves specify these metric-dependent constants.

## Limitations
The result treats one specific connected double cover of circles, equal coefficients, and strictly concave normalized distance transforms; it neither determines the optimal error for arbitrary weights nor addresses higher-degree coverings or other graph metrics. The argument does not assert that the explicit labelled paths are the only minimizers. Literature and database searches cannot exclude every unindexed equivalent theorem, and no independent audit has been performed.

## References
- H. Duru, S. İlter, A. Bilgin, *Sharp Norm Approximation of Covering Markov Operators*, arXiv:2610.35575v1 (first posted 26 October 2026), https://arxiv.org/html/2610.35575v1.
- Kantorovich–Rubinstein duality for Wasserstein-one distance on compact metric spaces (standard transport duality, used only for the norm conversion).
