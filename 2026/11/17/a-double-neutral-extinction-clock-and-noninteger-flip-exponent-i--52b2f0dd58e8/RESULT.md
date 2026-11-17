# A double-neutral extinction clock and noninteger flip exponent in the Ricker–Kolmogorov predator–prey map

## Finding

Consider the positive population map of Niu and Wang
\[
 x_{n+1}=\frac{x_n\exp(r-x_n)}{1+c y_n},\qquad
 y_{n+1}=s y_n+\frac{c b_0 x_n y_n}{(1+\gamma x_n)(1+c y_n)}.
\]
Fix \(\gamma>0\), \(0<c<1\) and
\[
 0<s<\frac{3+4\gamma}{5+8\gamma},\quad r=2,\quad
 b_0=\frac{(1-s)(1+2\gamma)}{2c}.
\]
Define \(L=1-s\), \(D=L/[2(1+2\gamma)]\),
\[
 \kappa=c(L+D),\qquad a=c(1+D),\qquad
 p=\frac a\kappa=\frac{1+D}{L+D} \in(1,2),
 \qquad w_n=x_n-2+c y_n.
\]
There exist constants \(M>0\) and \(\delta>0\), depending only on the parameters, such that every initial condition satisfying
\[
 0<y_0<\delta,\qquad |x_0-2+c y_0|<M y_0
\]
produces a strictly positive forward orbit converging to \((2,0)\) and obeying
\[
 \lim_{n\to\infty}n y_n=\frac1\kappa,\qquad
 \lim_{n\to\infty}n(x_n-2)=-\frac c\kappa,
 \qquad
 \lim_{n\to\infty}(-1)^n n^p w_n=C(x_0,y_0)\in\mathbb R.
\]
The limit \(C\) is not identically zero on this wedge: it is strictly positive on a nonempty relatively open set of initial states and strictly negative on another. In particular, this codimension-two simultaneous prey flip and predator-neutrality boundary supports a continuously parameter-dependent noninteger alternating exponent \(p\), while predator extinction remains asymptotically inverse-time.

## Assumptions and scope

All parameters are fixed and real. The state is \(x_n>0,y_n>0\); the local wedge is genuinely two-dimensional and open in the positive quadrant. The statement does not assert attraction for arbitrary initial populations, for parameter values outside the displayed range, or for the boundary case \(p=2\). The two eigenvalues of the Jacobian at \((2,0)\) are exactly \(-1\) and \(+1\), so ordinary hyperbolic linearization is inconclusive. The exponent is measured using full generations, not two-step return numbers.

## Proof

**1. Exact neutral boundary and quadratic coordinates.** Put \(v=y\) and \(w=x-2+cv\). Set \(Q(x)=cb_0 x/(1+\gamma x)\). Under the parameter relation, \(Q(2)=L\), and \(Q'(2)=D\). Write the map in the new coordinates as \((w,v)\mapsto(W,V)\), with
\[
 x=2+w-cv,\quad X=\frac{x e^{2-x}}{1+cv},\quad
 V=v\left(s+\frac{Q(x)}{1+cv}\right),\quad W=X-2+cV.
\]
The scalar Ricker factor has the expansion \((2+u)e^{-u}=2-u+u^3/6+O(u^4)\), in particular its quadratic coefficient vanishes. Direct Taylor expansion at \((w,v)=(0,0)\) therefore gives
\[
 W=-w+a wv+c^2(s-D)v^2+O((|w|+v)^3),
 \qquad V=v+Dwv-\kappa v^2+O((|w|+v)^3).
 \tag{1}
\]
Here \(a=c(1+D)\) and \(\kappa=c(L+D)\); notably \(a-\kappa=cs>0\). All remainders are uniform on a sufficiently small closed neighborhood. The map is analytic there since its denominators stay positive.

**2. The two-step cancellation.** Compose (1) with itself. The linear action is \((w,v)\mapsto(-w,v)\); hence both the \(wv\) and the \(v^2\) cross-parity contributions can be tracked exactly. The second iterate satisfies
\[
 W^{[2]}=w-2a wv+O((|w|+v)^3),\qquad
 V^{[2]}=v-2\kappa v^2+O((|w|+v)^3). \tag{2}
\]
In particular, there is *no* second-order term independent of \(w\) in \(W^{[2]}\), and there is *no* \(wv\) term in \(V^{[2]}\). Both cancellations are essential; replacing one iterate by a continuous-time approximation would not justify them.

**3. Construction and trapping of an open positive wedge.** Consider even generations and write \(W_j=w_{2j}\), \(V_j=y_{2j}\), \(H_j=W_j/V_j\). Fix any \(M>0\) small enough to keep \(x=2+w-cv>0\) for \(0<v<\delta\) and \(|w|\le Mv\). By (2), whenever \(|H_j|\le M\),
\[
 V_{j+1}=V_j-2\kappa V_j^2+O_M(V_j^3),\qquad
 W_{j+1}=(1-2aV_j)W_j+O_M(V_j^3),
\]
so, uniformly in this cone,
\[
 H_{j+1}=(1-2cs V_j)H_j+O_M(V_j^2). \tag{3}
\]
Choose \(\delta\) sufficiently small that \(0<V_{j+1}<V_j\) and the error in (3) is smaller than \(csM V_j\) when \(|H_j|\le M\). Then \(|H_{j+1}|\le M\), proving forward invariance for all two-step returns by induction. The intermediate odd iterates remain positive because both components of the original biological map are positive whenever \(x,v>0\), and remain near \((2,0)\) by (1). Thus the complete forward orbit is defined and stays close to the boundary equilibrium.

**4. The inverse-time extinction clock.** The first recurrence of step 3 gives
\[
 \frac1{V_{j+1}}-\frac1{V_j}=2\kappa+O_M(V_j).
\]
As \(V_j\downarrow0\), averaging gives \(jV_j\to1/(2\kappa)\). More precisely, the same recurrence first yields two-sided estimates \(V_j\asymp (1+j)^{-1}\); summing the displayed error then gives
\[
 V_j=\frac1{2\kappa j}+O_M\!\left(\frac{\log j}{j^2}\right).
 \tag{4}
\]
The one-step equation for \(v\) changes \(v\) by \(O(v^2)\) within the invariant wedge. Hence (4) implies \(ny_n\to1/\kappa\) along even and odd times. Equation (3), a strict contraction with cumulative decrement \(\sum_j V_j=\infty\) and summable error \(O(V_j^2)\), gives \(H_j\to0\). The odd-step ratio also tends to zero by (1), so \(w_n/y_n\to0\). Since \(x_n-2=w_n-cy_n\), the prey limit follows.

**5. The noninteger flip clock.** On the invariant wedge write
\[
 W_{j+1}=(1-2aV_j)W_j+E_j,\qquad |E_j|\le K V_j^3. \tag{5}
\]
For \(\delta\) still smaller if needed, all factors \(1-2aV_j\) are positive. Let
\[
 P_0=1,\quad P_j=\prod_{k=0}^{j-1}(1-2aV_k).
\]
By (4), \(2aV_j=p/j+O(\log j/j^2)\), so \(j^pP_j\to P_\infty\in(0,\infty)\). The variation-of-constants identity
\[
 \frac{W_j}{P_j}=W_0+\sum_{k=0}^{j-1}\frac{E_k}{P_{k+1}}
\]
has an absolutely convergent right side: its summands are \(O(k^{p-3})\) and \(p<2\). Hence \(j^pW_j\) has a finite limit \(C_e\). The one-step formula (1), \(W_{2j+1}=-W_j+O_M(V_j^2)\), shows
\[
 \lim_{n\to\infty}(-1)^n n^p w_n=2^pC_e.
\]
Here the odd correction vanishes because \(p<2\).

**6. Nontriviality of the constant.** Uniformly for sufficiently small \(V_0>0\) within a fixed wedge, the reciprocal recurrence gives \(V_j\asymp V_0/(1+jV_0)\), and the multiplicative factors obey \(P_j\asymp (V_j/V_0)^p\), with comparison constants independent of \(V_0\). It follows that
\[
 \sum_{j\ge0}|E_j/P_{j+1}|=O_M(V_0^2).
\]
If \(W_0=\theta V_0\) for a fixed \(\theta\in(-M,M)\setminus\{0\}\), this error is smaller than \(|W_0|/2\) for sufficiently small \(V_0\). Consequently \(C_e\) has the sign of \(\theta\). Continuous dependence of the finite orbit and uniform convergence of the renormalized variation-of-constants series on compact subwedges provide nonempty relatively open sets of each sign.

## Verification

The accompanying \(check.py\) uses symbolic derivatives of the exact map to verify all quadratic Taylor coefficients in (1), checks the second-iterate quadratic cancellations algebraically, and runs independent finite-time simulations for admissible parameter triples. The computation does not prove asymptotic limits; the infinite-time statements are deduced from the invariant-wedge, reciprocal, and summable-variation arguments above. Run `python check.py` in an environment with Python 3 and SymPy.

## Relationship to prior work

Niu and Wang, arXiv:2405.11806 (public May 20, 2024), define the same model in their equation (4). Their Lemma 3.3 locates the locally attracting predator-free equilibrium only for \(r<2\) and a *strict* predator invasion inequality; their positive-equilibrium global theorem requires the existence of a positive equilibrium and \(r\le1\). Neither covers the double equality \(r=2\) and \(s+2cb_0/(1+2\gamma)=1\). Their paper is also the source of the model's 2020-MSC tags 37G10 and 37N25. A distinct earlier result on this same Niu–Wang map concerns prey-only two-cycles when \(r>2\), particularly their transverse invasion threshold; it does not imply the double-neutral interior extinction rates at \(r=2\). Standard Ricker flip asymptotics on the invariant predator-free axis treat \(y_0=0\), whereas here every initial predator density is strictly positive. Earlier results for other predator–prey maps identify some inverse-time or fractional exponent laws, but their distinct update rules do not imply (1)–(5) for this system.

## Limitations

The theorem is local and restricted to \(1<p<2\). It does not classify global basins, the parameter-resonant case \(p=2\), the subcritical transition beyond the stated parameter interval, higher-order corrections to the amplitude, or stochastic populations. The exponent's sharpness is asserted on nonempty open sets, not uniformly for every initial point in the wedge: exceptional initial states can have \(C=0\). Searches cannot establish absolute absence of equivalent unindexed results; independent review is not yet performed.

## References

- L. Niu and S. Wang, *Global stability and period-doubling bifurcations of a discrete Kolmogorov predator-prey model with Ricker-type prey growth*, arXiv:2405.11806, first posted 2024-05-20, https://arxiv.org/abs/2405.11806 (full-text equations (4), Lemma 3.3, Theorem 3.16, and Section 4 inspected).
- A. S. Ackleh, M. I. Hossain, A. Veprauskas and A. Zhang, *Long-term dynamics of discrete-time predator–prey models: stability of equilibria, cycles and chaos*, Journal of Difference Equations and Applications **26** (2020), 693–726, DOI: 10.1080/10236198.2020.1786818 (related Beverton–Holt-type dynamics; distinct prey growth).
- A. S. Ackleh, P. Salceanu and A. Veprauskas, *A nullcline approach to global stability in discrete-time predator–prey models*, Journal of Difference Equations and Applications **27** (2021), 1120–1133, DOI: 10.1080/10236198.2021.1963440 (related positive-equilibrium stability in a different prey-growth model).
