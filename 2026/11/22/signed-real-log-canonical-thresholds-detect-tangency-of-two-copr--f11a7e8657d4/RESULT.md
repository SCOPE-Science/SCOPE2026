# Signed real log canonical thresholds detect tangency of two coprime cusp branches

## Finding
Fix an even integer \(p\ge2\), an odd integer \(q>p\) with \(\gcd(p,q)=1\), and an integer \(r>q\). For the real plane polynomial germ
\[
f_{p,q,r}(x,y)=(x^p-y^q)^2-y^{2r},
\]
the local signed real log canonical thresholds are exactly
\[
\boxed{\operatorname{rlct}^{+}_{0}(f_{p,q,r})=\frac{p+q}{2pq}},\qquad
\boxed{\operatorname{rlct}^{-}_{0}(f_{p,q,r})=\frac12-\frac{q(p-1)-p}{2pr}}.
\]
Their positive difference is
\[
\operatorname{rlct}^{-}_{0}(f_{p,q,r})-\operatorname{rlct}^{+}_{0}(f_{p,q,r})
=\frac{[q(p-1)-p](r-q)}{2pqr}>0.
\]
The two complex irreducible branches have the same Puiseux characteristic pair \((p,q)\), while their intersection multiplicity is \(pr\). Thus for fixed \((p,q)\) the positive signed threshold is constant, but the negative threshold strictly increases with their contact order \(r\), and it determines that order. This supplies an explicit Newton-degenerate, analytically reducible infinite family in which signed thresholds distinguish tangency not detected by either individual branch's Puiseux characteristic.

## Assumptions and scope
The polynomial and thresholds are germs at the origin of \(\mathbb R^2\), not global thresholds. For \(\sigma\in\{+,-\}\), define
\[
\operatorname{rlct}^{\sigma}_{0}(f)=\sup\{s>0:\mathbf1_{\{\sigma f>0\}}|f|^{-s}\text{ is locally Lebesgue integrable at }0\}.
\]
The zero set itself has measure zero and does not affect integration. The parameter assumptions \(p\) even, \(q\) odd, \(q>p\), \(\gcd(p,q)=1\), \(r>q\) are essential to the presented real-sign argument and branch characteristic statement. Let \(u=x^p-y^q\) and \(\gamma=q(p-1)/p\). Since \(q>p\), \(\gamma>1\); define \(\alpha=(p+q)/(2pq)\) and \(\beta=1/2-(\gamma-1)/(2r)\). Then \(0<\alpha<\beta<1/2\).

## Proof
**1. The negative-sign region.** A sufficiently small neighborhood satisfies \(|y|^{r-q}<1/2\). If \(y<0\), then \(u=x^p+|y|^q\ge|y|^q>|y|^r\), so \(f=u^2-y^{2r}>0\). For \(y>0\), \(f<0\) is exactly \(-y^r<u<y^r\). In this strip, \(x^p=y^q+u>0\), and there are two inverse branches \(x=\pm(y^q+u)^{1/p}\). Summing their absolute Jacobians gives
\[
\sum_{\pm}\left|\frac{\partial x}{\partial u}\right|=
\frac2p(y^q+u)^{1/p-1}\asymp y^{-\gamma},
\]
with constants independent of sufficiently small \(y,u\). For \(0<s<1\), the negative integral in a small box is consequently comparable to
\[
\begin{aligned}
\int_{0}^{\varepsilon}\!y^{-\gamma}\int_{-y^r}^{y^r}
(y^{2r}-u^2)^{-s}\,du\,dy
&=B(1/2,1-s)\int_0^\varepsilon
 y^{r(1-2s)-\gamma}\,dy.
\end{aligned}
\]
Here \(B\) is the usual beta integral, finite for \(s<1\). The last integral converges precisely when \(r(1-2s)-\gamma>-1\), equivalently \(s<\beta\); at equality it diverges logarithmically. Since \(\beta<1/2\), all higher exponents diverge by monotonicity on a neighborhood where \(|f|<1\). This proves the negative threshold.

**2. Divergence on the positive side.** Restrict to \(y=-t<0\), \(0<t<\varepsilon\), and \(|x|\le t^{q/p}\). Then \(t^q\le u=x^p+t^q\le2t^q\), so \(f=u^2-t^{2r}\asymp t^{2q}>0\) uniformly. The integral of \(f^{-s}\) over this wedge is bounded below by a positive constant times
\[
\int_0^\varepsilon t^{q/p-2qs}\,dt,
\]
which diverges when \(s\ge (p+q)/(2pq)=\alpha\). Hence \(\operatorname{rlct}^{+}_{0}(f)\le\alpha\).

**3. Convergence on the positive side.** Fix \(0<s<\alpha\). Divide a sufficiently small neighborhood into \(D_1=\{|u|<2|y|^r\}\) and its complement \(D_2\). For \(y<0\), \(D_1\) is empty after shrinking. For \(y>0\), the same two-root Jacobian estimate applies on \(D_1\); substituting \(u=y^rv\) bounds the positive-sign integral there by
\[
C_s\int_0^\varepsilon y^{r(1-2s)-\gamma}\,dy
\int_{\{1<|v|<2\}}(v^2-1)^{-s}\,dv,
\]
which is finite because \(s<\alpha<\beta<1/2\). On \(D_2\cap\{f>0\}\), one has \(f=u^2-y^{2r}\ge(3/4)u^2\). It is therefore enough to show \(|x^p-y^q|^{-2s}\in L^1_{\rm loc}(\mathbb R^2)\) for \(2s<1/p+1/q\). To verify this cusp estimate, put \(t=2s\) and note \(t<1/p+1/q<1\). For \(y=-z<0\), on \(|x|^p\le z^q\), \(|u|=|x|^p+z^q\asymp z^q\) and integration in \(x\) gives \(\int_0^\varepsilon z^{q/p-qt}\,dz\). In the complementary region \(z^q<|x|^p\), \(|u|\asymp|x|^p\) and integration in \(z\) gives \(\int_0^\varepsilon |x|^{p/q-pt}\,dx\). For \(y>0\), on \(|x|\le2y^{q/p}\), write \(x=y^{q/p}v\): the inner integral factors as \(\int_{-2}^2|v^p-1|^{-t}\,dv\), finite because \(t<1\), times \(\int_0^\varepsilon y^{q/p-qt}\,dy\). Outside that region, \(|u|\asymp|x|^p\) and \(0<y<( |x|/2)^{p/q}\), giving \(\int_0^\varepsilon |x|^{p/q-pt}\,dx\). Each resulting power integral is finite exactly when \(t<1/p+1/q\). Thus the positive integral is finite for every \(s<\alpha\), proving equality.

**4. Complex branches and contact.** Over \(\mathbb C\), the reduced equation splits as \(f=g_+g_-\) where \(g_\pm=x^p-y^q\pm y^r\). Each is analytically irreducible: its parametrization \(y=t^p,\ x=t^q(1\mp t^{p(r-q)})^{1/p}\), with the binomial series centered at one, has primitive first exponent \(q\) and \(\gcd(p,q)=1\), hence characteristic pair \((p,q)\). The two local equations yield the ideal \((x^p-y^q,y^r)\) since two is invertible in \(\mathbb C\). Its colength is \(pr\) because it is free of rank \(p\) over \(\mathbb C[[y]]/(y^r)\). Solving the negative-threshold formula gives
\[
r=\frac{q(p-1)-p}{p(1-2\operatorname{rlct}^{-}_{0}(f))},
\]
so the signed invariant recovers contact order once the common Puiseux pair is known.

## Verification
An accompanying `verify.py` checks exactly (with rational arithmetic) the formula, strict threshold order, contact inversion and exact integrability exponents on representative admissible families, and the algebraic factorization and intersection resultant for low degrees. These finite tests are consistency checks, not a proof of the all-parameter statement. The preceding integral and formal-local-algebra arguments provide that proof. Examples include \((p,q,r)=(2,3,4)\), which gives \((\alpha,\beta)=(5/12,7/16)\), and \((2,3,5)\), which gives \((5/12,9/20)\).

## Relationship to prior work
Jaudon (2026) introduces and studies signed real log canonical thresholds, giving formulas for Newton-nondegenerate germs (Theorem 4.12) and analytically irreducible plane germs (Theorem 5.12). This family lies outside both hypotheses: its compact Newton face is \((x^p-y^q)^2\), with a multiple zero and vanishing gradient on the real torus, and the germ has two irreducible complex branches. Jaudon's general resolution and signed-zeta framework applies abstractly but does not state the present two-formula contact-order law. Galindo--Hernando--Monserrat (2012/2016) give formulas for **unsigned complex** log canonical thresholds of reduced plane curves in terms of branch and contact data; their ordinary threshold is related to the first formula, but their result does not distinguish the signs or imply the negative-sign formula without an additional real analysis. Sergeant-Perthuis--Tsigaridas--Tsukahara (2026) provide a general exact computational procedure for **ordinary** bivariate real RLCTs; their abstract does not claim signed thresholds. Kosta--Windisch (2024/2026) treat real hyperplane arrangements, not these cusp branches. Searches of accessible indexed research statements and related primary literature did not locate this signed two-branch contact law. Such searches cannot establish absolute first-publication priority.

## Limitations
Only the stipulated coprime even--odd cusp family is proved; no formula is claimed for arbitrary reducible real plane curves, different signs/parities or higher-dimensional singularities. The exponents are local integrability thresholds, not asymptotic constants of the signed zeta functions. No independent audit has been performed. Abstract general resolution theory can recover these examples in principle; the specific closed formulas and contact recovery are the asserted additional results. Historical and unindexed publications may contain equivalent computations.

## References
1. T. Jaudon, *Real log canonical tresholds and real log canonical tresholds with signs*, arXiv:2611.17004v1 (first public 2026-11-12), Definitions 1.1--1.3, Theorems 4.12 and 5.12, Remark 5.14. https://arxiv.org/abs/2611.17004
2. C. Galindo, F. Hernando, F. Monserrat, *The log-canonical threshold of a plane curve*, arXiv:1211.6274 (2012); published in Math. Proc. Cambridge Philos. Soc. (2016). https://arxiv.org/abs/1211.6274
3. G. Sergeant-Perthuis, E. Tsigaridas, J. Tsukahara, *Exact Algebraic Computation of Learning Coefficients for Two-Dimensional Singular Models*, arXiv:2608.20183 (2026). https://arxiv.org/abs/2608.20183
4. D. Kosta, D. Windisch, *Classification of real hyperplane singularities by real log canonical thresholds*, arXiv:2411.13392 (2024; revised 2026). https://arxiv.org/abs/2411.13392
