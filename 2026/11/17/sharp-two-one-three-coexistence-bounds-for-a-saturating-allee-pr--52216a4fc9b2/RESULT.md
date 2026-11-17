# Sharp two–one–three coexistence bounds for a saturating Allee predator–prey flow

## Finding
For the Gao–Ta saturating strong-Allee predator–prey system with \(0<k_0<k_1\) and \(sh<1\), the number of strictly positive coexistence equilibria has sharp bounds depending on the sign of \(\lambda-Ab\): at most two if \(\lambda<Ab\), at most one if \(\lambda=Ab\), and at most three if \(\lambda>Ab\). All three bounds are attained with positive formal parameters. In the last regime, if three simple interior equilibria occur, the middle equilibrium in prey-coordinate order is necessarily a saddle. An explicit rational parameter choice realizes a source, saddle, and attracting focus; all three persist after sufficiently small parameter perturbations.

The distinction has a biological qualification: with the paper's parametrization \(\lambda=\lambda_0b\), \(A=\lambda_0+a\), the cooperative-hunting increment \(a\) is positive precisely in the \(\lambda<Ab\) regime. The three-equilibrium example lies instead in the mathematically positive *inhibitory* continuation \(a<0\). It must not be interpreted as positive hunting cooperation.

## Assumptions and scope
For all fixed parameters \(r_1,k_1,s,A,\lambda,b,h>0\) and \(0<k_0<k_1\), consider
\[
\begin{aligned}
\dot x&=r_1x(1-x/k_1)(x-k_0)-\frac{(\lambda+Ay)xy}{b+y+hx(\lambda+Ay)},\\
\dot y&=\frac{(\lambda+Ay)xy}{b+y+hx(\lambda+Ay)}-sy.
\end{aligned}
\]
Assume \(sh<1\). A coexistence equilibrium means \(x>0\) and \(y>0\). For the count bounds there is no restriction on the values of the parameters other than those listed. Stability claims for the three-state example concern its hyperbolic equilibria, not a global phase portrait.

## Proof
Put \(c=1-sh>0\). At a positive equilibrium, the predator balance gives \(sy\) equal to consumption, and the prey balance then requires
\[
Y(x):=\frac{r_1}{s}x(1-x/k_1)(x-k_0)=y>0.
\]
Thus \(k_0<x<k_1\). If \(\lambda\ne Ab\), rearranging the predator balance gives
\[
Z(x):=\frac{\lambda cx-sb}{s-Acx}=y>0.
\]
Write \(x_b=sb/(\lambda c)\), \(x_d=s/(Ac)\). When \(\lambda<Ab\), one has \(x_d<x_b\), and positivity of \(Z\) requires \(x_d<x<x_b\). When \(\lambda>Ab\), one has \(x_b<x_d\), and positivity requires \(x_b<x<x_d\). Each feasible prey-coordinate set is therefore a single open interval, intersected with \((k_0,k_1)\). On it \(Y=Z\) is equivalent to the full two-equation equilibrium system; the consumption denominator stays strictly positive.

Differentiate explicitly:
\[
Z'(x)=\frac{sc(\lambda-Ab)}{(s-Acx)^2},\quad
Z''(x)=\frac{2sAc^2(\lambda-Ab)}{(s-Acx)^3},\quad
Z'''(x)=\frac{6sA^2c^3(\lambda-Ab)}{(s-Acx)^4},
\]
while \(Y'''(x)=-6r_1/(sk_1)<0\).

If \(\lambda<Ab\), the feasible denominator \(s-Acx\) is negative. Hence \(Z'<0\) and \(Z''>0\). The positive cubic \(Y\) has one maximum at some \(x_m\in(k_0,k_1)\): it increases before \(x_m\), decreases afterward, and \(Y''<0\) after \(x_m\). For \(F=Y-Z\), one has \(F'>0\) on the feasible portion before \(x_m\), and \(F''=Y''-Z''<0\) on the portion after \(x_m\). Therefore \(F\) is strictly increasing until at most one subsequent maximum and strictly decreasing thereafter, so it has at most two zeros.

If \(\lambda>Ab\), the feasible denominator is positive and \(Z'''>0\). Thus \(F'''=Y'''-Z'''<0\) throughout the feasible interval. Four distinct zeros of \(F\) would, by three successive applications of Rolle's theorem, force a zero of \(F'''\), a contradiction. Hence there are at most three equilibria. If three simple roots \(x_1<x_2<x_3\) exist, Hermite's divided-difference mean-value formula at the roots gives
\[
\operatorname{sgn}F'(x_1)=-1,\qquad
\operatorname{sgn}F'(x_2)=+1,\qquad
\operatorname{sgn}F'(x_3)=-1.
\]
For the vector field written as \(\dot x=xp(x,y)\), \(\dot y=yq(x,y)\), the Jacobian at a positive equilibrium obeys
\[
\det J=xy\,p_yq_y\,[Z'(x)-Y'(x)].
\]
Here \(p_y<0\); in the \(\lambda>Ab\) regime also \(q_y<0\), so the determinant signs at the three roots are \(+,-,+\). In particular, the middle equilibrium is a hyperbolic saddle.

At \(\lambda=Ab\), the consumption term reduces to \(Axy/(1+hAx)\), and predator growth is \(y[Ax/(1+hAx)-s]\), independent of \(y\) in the per-capita factor. Any coexistence equilibrium therefore has the uniquely specified coordinate \(x=x_d=s/[A(1-sh)]\) and \(y=Y(x_d)\); it exists if and only if \(k_0<x_d<k_1\). This proves the middle bound and its attainment.

To establish sharpness for positive cooperation, set
\[
(r_1,k_1,s,k_0,h,A,\lambda,b)=(1,1,1,1/10,1/5,20,1/10,1/10).
\]
Then \(a=A-\lambda/b=19>0\). The two nullclines are \(Y(x)=x(1-x)(x-1/10)\) and \(Z(x)=(2x/25-1/10)/(1-16x)\). Their difference has exact signs \(F(1/10)=-23/150<0\), \(F(1/2)=16/175>0\), \(F(1)=-1/750<0\); throughout \((1/10,1)\) the rational predator nullcline is positive. The intermediate-value theorem and the proved upper bound give exactly two positive coexistence equilibria.

For the neutral-response case, set \((r_1,k_1,s,k_0,h,A,\lambda,b)=(1,1,1,1/10,1/5,4,2/5,1/10)\). Then \(\lambda=Ab\) and \(x_d=5/16\in(1/10,1)\); there is exactly one positive equilibrium.

To attain three equilibria in the formal inhibitory regime, set
\[
(r_1,k_1,s,k_0,h,A,\lambda,b)=(1,1,1,1/10,9/10,1,2,21/1000).
\]
Here \(\lambda>Ab\) and \(a=A-\lambda/b<0\). The nullclines become \(Y(x)=x(1-x)(x-1/10)\) and \(Z(x)=2(x-21/200)/(10-x)\), with biologically positive coordinates only for \(21/200<x<1\). Equality is the quartic
\[
P(x)=100x^4-1110x^3+1110x^2-300x+21=0.
\]
Exact rational evaluations locate one root in each of the disjoint intervals
\[
(0.109668415,0.109668417),\quad
(0.276024322,0.276024325),\quad
(0.692199537,0.692199540).
\]
Moreover \(P(10)=-1979<0\) and \(P(x)\to+\infty\) as \(x\to+\infty\), giving a fourth real root above \(10\), which is outside the positive coexistence domain. Since \(P\) has degree four, these are all its real roots and each is simple. The corresponding predator coordinates are approximately \(0.0009440362\), \(0.0351758023\), and \(0.1261736413\).

The exact Jacobian trace and determinant at such a root, with \(H(x)=1979000x(10-x)>0\), are
\[
\operatorname{tr}J=\frac{T(x)}{H(x)},\quad
\det J=\frac{(200x-21)D(x)}{H(x)},
\]
where
\[
\begin{aligned}
T(x)&=5937000x^4-63743800x^3+44138000x^2-4416800x+251559,\\
D(x)&=300x^4-6220x^3+34410x^2-22200x+2979.
\end{aligned}
\]
The rational interval certificates in `check.py` prove that \((\operatorname{sgn}\operatorname{tr}J,\operatorname{sgn}\det J,\operatorname{sgn}[(\operatorname{tr}J)^2-4\det J])\) equals \((+,+,+)\), \((+,-,+)\), and \((-,+,-)\), respectively. The equilibria are therefore, in ascending prey coordinate, a hyperbolic repelling node, a saddle, and an attracting focus. All three persist under small independent perturbations of the eight parameters by the implicit-function theorem, and the bound of three continues to exclude additional equilibria.

## Verification
Run `python check.py` with SymPy installed. It exactly reconstructs the nullcline reductions, quartic and Jacobian identities; certifies root brackets and trace, determinant, discriminant signs via rational midpoint bounds on polynomial derivatives; checks the two-state cooperative example and the neutral example. The checker is independent of floating-point integration. Its `VERIFY_OK` lines report the checks performed. The analytical sign, Rolle, and implicit-function arguments establish the general statements; finite checking alone does not establish them.

## Relationship to prior work
Gao and Ta (2026), Theorem 2.4, prove an at-most-two interior-equilibrium result under additional hypotheses, including \(k_0>k_1/2\) in the strong-Allee case, and provide examples with zero, one, or two intersections. The present trichotomy removes that strong-Allee restriction on the genuine-cooperation side, isolates the neutral-response case, and proves a sharp three-state bound in the mathematically extended inhibitory regime. Their Jacobian formulas are consistent with the local calculations here but do not imply the root-count trichotomy. Earlier studies of cooperative hunting, fear and Allee effects use different response laws or place the Allee effect in the predator's numerical response.

## Limitations
The hypothesis \(sh<1\) is essential to the present nullcline-domain argument; no count bound is claimed when \(sh\ge1\). The three-state example uses \(a<0\), an interference/inhibition continuation, rather than genuine positive cooperation. No claim is made about global basins, periodic orbits, or an experimentally calibrated ecosystem. The general root-count theorem does not classify all stability types; only the middle saddle in a three-root case and the exact rational example are classified. Historical mathematical priority remains subject to independent review.

## References
1. Y. Gao and T. V. Ta, *Bifurcation Analysis of a Predator–Prey Model with Allee Effect and Cooperative Hunting*, arXiv:2601.10739v1, first public 2026-01-09, https://arxiv.org/html/2601.10739v1.
2. D. Sen, S. Ghorai, M. Banerjee and A. Morozov, *Bifurcation analysis of the predator–prey model with the Allee effect in the predator*, Journal of Mathematical Biology 84 (2022), https://pmc.ncbi.nlm.nih.gov/articles/PMC8718388/. Different Allee location and functional response.
3. Y. Du, B. Niu and J. Wei, *Global dynamics in a predator-prey model with cooperative hunting and Allee effect and bifurcation induced by diffusion and delays*, arXiv:2007.12801 (2020), https://arxiv.org/abs/2007.12801. Different model; abstract-level context only.
