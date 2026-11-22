# Sharp convex-order envelope for fixed-mean Lipschitz endpoint paths

## Finding
Let \(L\ge1\), and consider every real \(L\)-Lipschitz function \(f:[0,1]\to[0,1]\) with \(f(0)=0\), \(f(1)=1\), and prescribed mean \(\int_0^1f(x)\,dx=m\). The function need **not** be monotone. When \(L=1\), the only path is \(f(x)=x\), with \(m=1/2\).

For \(L>1\), write
\[
q=1-\frac1L,\qquad r=\frac{m-1/(2L)}{q}.
\]
Such a path exists if and only if \(1/(2L)\le m\le1-1/(2L)\). More strongly, its pushforward of uniform Lebesgue measure is *exactly* any probability of the form
\[
f_{\#}\mathrm{Leb}_{[0,1]}=\frac1L\mathrm{Leb}_{[0,1]}+q\nu,
\qquad \nu\in\mathcal P([0,1]),\qquad\int_0^1t\,d\nu(t)=r.
\]
Here \(f_{\#}\mathrm{Leb}\) denotes the probability law of \(f(U)\) when \(U\) is uniform on \([0,1]\). Every displayed law is attained by an admissible *nondecreasing* path.

Consequently, for **every** continuous convex \(\varphi:[0,1]\to\mathbb R\), simultaneously,
\[
\boxed{\frac1L\int_0^1\varphi(t)\,dt+q\varphi(r)
\ \le\ \int_0^1\varphi(f(x))\,dx
\ \le\ \frac1L\int_0^1\varphi(t)\,dt
+q\bigl[(1-r)\varphi(0)+r\varphi(1)\bigr].}
\]
Subtracting \(\varphi(m)\) gives the corresponding sharp lower and upper Jensen-gap bounds. The two universal extremizers are, respectively,
\[
f_{\min}(x)=\begin{cases}
Lx,&0\le x\le r/L,\\
r,&r/L\le x\le r/L+q,\\
Lx-(L-1),&r/L+q\le x\le1,
\end{cases}
\]
and
\[
f_{\max}(x)=\min\{1,\max\{0,L(x-q(1-r))\}\}.
\]
For any strictly convex \(\varphi\) and \(L>1\), these extremizers are the only admissible ones; when \(r=0\) or \(r=1\) they coincide. In particular, when \(m=1/2\),
\[
\boxed{\frac1{12L}\le\int_0^1(f(x)-1/2)^2\,dx\le\frac14-\frac1{6L}.}
\]
Both variance endpoints are sharp and uniquely attained by the respective paths for \(L>1\).

## Assumptions and scope
All intervals have length one, the state and endpoint values are normalized to \([0,1]\), and \(L\) is a finite real number at least one. Lipschitz functions have their unique continuous endpoint traces. All probability laws and convex functions in the assertion are real-valued. The mean constraint is exactly as displayed. No nondecreasing hypothesis is assumed; the extremizers nevertheless are nondecreasing. For the finite-\(L\) bounds, no smoothness of \(\varphi\) beyond continuity and convexity is needed.

## Proof
**1. Forced uniform component.** Let \(\mu=f_{\#}\mathrm{Leb}_{[0,1]}\). For every continuous nonnegative \(\psi:[0,1]\to\mathbb R\), the Lipschitz chain rule gives, with \(\Psi(t)=\int_0^t\psi(u)\,du\),
\[
L\int\psi\,d\mu=L\int_0^1\psi(f(x))\,dx
\ge\int_0^1\psi(f(x))|f'(x)|\,dx
\ge\left|\int_0^1\psi(f(x))f'(x)\,dx\right|
=\int_0^1\psi(t)\,dt.
\]
Thus \(\mu\ge L^{-1}\mathrm{Leb}_{[0,1]}\) as measures, even if the path oscillates. If \(L>1\), the residual \(\nu=(\mu-L^{-1}\mathrm{Leb})/q\) is a probability. Taking first moments gives \(m=1/(2L)+qr\), which forces the stated feasible mean interval.

**2. No hidden restrictions on residual laws.** Conversely, fix any probability \(\nu\) with mean \(r\) and put \(\mu=L^{-1}\mathrm{Leb}+q\nu\). Let \(Q_\mu\) be its left-continuous generalized inverse distribution function (quantile). For \(0\le s<t\le1\), the domination \(\mu([a,b])\ge(b-a)/L\) implies \(0\le Q_\mu(t)-Q_\mu(s)\le L(t-s)\), by approximating either quantile with continuity points. Thus \(f=Q_\mu\) extends continuously to \([0,1]\), is nondecreasing and \(L\)-Lipschitz, and has \(f(0)=0\), \(f(1)=1\). Its pushforward is \(\mu\), and its mean is \(m\). This proves the claimed *exact* set of laws.

**3. Universal sharp convex-order envelope.** By Jensen's inequality for the residual law, \(\int\varphi\,d\nu\ge\varphi(r)\). By the chord bound for every \(t\in[0,1]\), \(\varphi(t)\le(1-t)\varphi(0)+t\varphi(1)\), whence \(\int\varphi\,d\nu\le(1-r)\varphi(0)+r\varphi(1)\). Adding the forced uniform component proves both bounds. Equality laws are \(\nu=\delta_r\) and \(\nu=(1-r)\delta_0+r\delta_1\), respectively. Their quantile maps are precisely the ramp/plateau paths displayed above, which establish sharpness for every convex \(\varphi\) simultaneously.

**4. Equality rigidity for strictly convex losses.** Strict convexity makes the residual equality law unique (Jensen for the minimum, the strict interior chord inequality for the maximum). If an admissible path with such a law were nonmonotone, then, since it starts at zero and ends at one, it would cross every value in some open interior interval at least three times. The one-dimensional area formula would then imply that its pushforward mass on that interval is at least three times its length divided by \(L\). Choosing a subinterval avoiding the residual law's finite support contradicts the exact uniform density \(1/L\) there. Hence every equality path is nondecreasing. Quantile uniqueness then gives the two functions as the only equality cases. At the feasible mean endpoints the residual law is forced to be a point mass and the two paths coincide.

**5. Variance.** For \(\varphi(t)=t^2\) and \(m=1/2\), we have \(r=1/2\). The common uniform contribution is \(1/(3L)\), while the two residual second moments are \(1/4\) and \(1/2\). Subtract \(m^2=1/4\) to obtain the displayed sharp interval. Finally, if \(L=1\), the endpoint Lipschitz bounds \(f(x)\le x\) and \(f(x)\ge1-(1-x)=x\) force the identity map.

## Verification
The standalone `check_lipschitz_jensen.py` is a deterministic corroboration, not a proof of the infinite statements. It checks 30 exact rational extremal moment identities over multiple slope and mean parameters, and 363 numerical convex-envelope comparisons including oscillatory clamped trigonometric paths and the convex losses \(t^2\), \(e^t\), and \(|t-0.3|\). Run `python check_lipschitz_jensen.py` in the directory containing the checker. All checks passed during preparation. The completeness of the attainable-law classification and the equality assertion follow analytically from Steps 1–4, not from sampling.

## Relationship to prior work
Costarelli and Spigler (2015) analyze Jensen gaps for general integrable inputs and convex losses, with curvature- and Lipschitz-of-the-*loss*-based estimates. Their fully available article does not impose endpoints, a slope cap, or fixed input mean and does not provide the exact family of attainable output laws derived here. Walker (2014) obtains different lower Jensen-gap refinements for certain convex losses; only an abstract/preview was accessible, leaving a limited historical-priority uncertainty. Kleiner, Moldovanu and Strack (2021) classify extreme points for monotone function majorization constraints, a different feasible set; the present path class allows oscillatory inputs and is characterized by a forced **uniform** pushforward component. Klebanov (2023) supplies general convex-graph bounds for arbitrary random variables, corresponding to the elementary residual Jensen/chord part of Step 3. Neither that general convex-envelope step nor the chain-rule inequality alone is claimed novel; the contribution is their exact realizable path-law characterization together with universal sharpness and rigidity.

## Limitations
This is a one-dimensional endpoint-normalized result with a *uniform* slope cap and uniform averaging in the domain. No claim is made for higher-dimensional domains, arbitrary nonlinear constraints, weighted domain measures, or a variable pointwise slope cap. For convex losses that are not strictly convex, equality can occur for additional paths; uniqueness is asserted only for strictly convex losses. The literature comparison does not exclude unindexed earlier equivalent formulations, and independent review is not yet performed.

## References
- D. Costarelli and R. Spigler, "How sharp is the Jensen inequality?", *Journal of Inequalities and Applications* **2015**, article 69, first online 2015-02-24, https://doi.org/10.1186/s13660-015-0591-x .
- S. G. Walker, "On a Lower Bound for the Jensen Inequality", *SIAM Journal on Mathematical Analysis* **46** (2014), 3151–3157, https://doi.org/10.1137/140954015 .
- A. Kleiner, B. Moldovanu and P. Strack, "Extreme Points and Majorization: Economic Applications", *Econometrica* **89** (2021), 1557–1593, https://doi.org/10.3982/ECTA18312 .
- I. Klebanov, "Graph Convex Hull Bounds as generalized Jensen Inequalities" (2023), https://arxiv.org/abs/2304.04856 .
