# Sharp two–one–three coexistence bounds for a saturating Allee predator–prey flow

## Finding

For the Gao–Ta saturating strong-Allee predator–prey system specified below, the maximum attainable number of strictly positive coexistence equilibria is two if \(\lambda<Ab\), one if \(\lambda=Ab\), and three if \(\lambda>Ab\). If there are three simple interior equilibria in the last regime, the middle one in prey-coordinate order is a saddle. A rational parameter choice realizes a repelling node, a saddle and an attracting focus; all three persist after sufficiently small parameter perturbations.

Under the original parametrization \(\lambda=\lambda_0b\), \(A=\lambda_0+a\), one has \(\lambda-Ab=-ab\). Positive cooperative hunting (\(a>0\)) thus corresponds to \(\lambda<Ab\). The three-equilibrium construction belongs to the formal inhibitory continuation \(a<0\), not to positive cooperation.

## Assumptions and scope

Let \(r_1,k_1,s,A,\lambda,b,h>0\), \(0<k_0<k_1\), and \(sh<1\). Consider
\[
\begin{aligned}
\dot x&=r_1x(1-x/k_1)(x-k_0)-\frac{(\lambda+Ay)xy}{b+y+hx(\lambda+Ay)},\\
\dot y&=\frac{(\lambda+Ay)xy}{b+y+hx(\lambda+Ay)}-sy.
\end{aligned}
\]
Only equilibria with \(x>0\), \(y>0\) are counted. The stability statements are local.

## Proof

**Equilibrium reduction.** Put \(c=1-sh\) and \(Y(x)=\frac{r_1}{s}x(1-x/k_1)(x-k_0)\). Since \(\dot x+\dot y=s(Y(x)-y)\), coexistence requires \(y=Y(x)>0\), hence \(k_0<x<k_1\). For \(\lambda\ne Ab\), the predator equation further requires
\[
y=Z(x):=\frac{\lambda cx-sb}{s-Acx}.
\]
Define \(x_b=sb/(\lambda c)\) and \(x_d=s/(Ac)\). The denominator cannot vanish at a coexistence equilibrium, as the numerator and denominator would then both vanish and imply \(\lambda=Ab\). If \(\lambda<Ab\), positivity requires \(x_d<x<x_b\); if \(\lambda>Ab\), it requires \(x_b<x<x_d\). In each case the feasible domain is the stated open interval intersected with \((k_0,k_1)\). On it, \(F=Y-Z=0\) is equivalent to a positive equilibrium, since the consumption denominator is positive.

**Cooperative regime.** If \(\lambda<Ab\), then \(Z'=sc(\lambda-Ab)/(s-Acx)^2<0\) and \(Z''=2sAc^2(\lambda-Ab)/(s-Acx)^3>0\) on the feasible interval. The quadratic \(Y'\) has negative leading coefficient and has one root in \((0,k_0)\) and one root \(x_m\) in \((k_0,k_1)\), by Rolle's theorem on \([0,k_0]\) and \([k_0,k_1]\). Thus \(Y'\ge 0\) on \((k_0,x_m]\) and \(Y''<0\) on \([x_m,k_1)\). It follows that \(F'>0\) before and at \(x_m\) wherever feasible and \(F'\) is strictly decreasing after \(x_m\). Therefore there can be at most two zeros of \(F\), by Rolle's theorem. For sharpness take
\[
(r_1,k_1,s,k_0,h,A,\lambda,b)=(1,1,1,1/10,1/5,20,1/10,1/10).
\]
Here \((1/10,1)\) is feasible and \(Z(x)=(2x/25-1/10)/(1-16x)\). The continuous extension to the endpoints satisfies \(F(1/10)=-23/150\), \(F(1/2)=16/175\), and \(F(1)=-1/750\), giving two roots. The cooperation increment is \(19\).

**Neutral regime.** At \(\lambda=Ab\), consumption reduces to \(Axy/(1+hAx)\), so predator balance fixes \(x=x_d\). There is exactly one coexistence equilibrium if \(x_d\in(k_0,k_1)\) and none otherwise. For example, \((r_1,k_1,s,k_0,h,A,\lambda,b)=(1,1,1,1/10,1/5,4,2/5,1/10)\) gives \(x_d=5/16\) in this interval.

**Inhibitory regime.** If \(\lambda>Ab\), then \(Z'''=6sA^2c^3(\lambda-Ab)/(s-Acx)^4>0\), whereas \(Y'''=-6r_1/(sk_1)<0\). Thus \(F'''<0\) throughout the feasible interval and three applications of Rolle's theorem exclude four distinct roots. For three simple roots \(x_1<x_2<x_3\), Hermite divided differences at the three roots with \(x_i\) repeated give
\[
\frac{F'(x_i)}{\prod_{j\ne i}(x_i-x_j)}=[x_1,x_2,x_3,x_i]F<0.
\]
Indeed, the divided difference equals \(F'''(\xi)/6\) for an intermediate \(\xi\). Hence the signs of \(F'(x_i)\) are \(-,+,-\).

To relate these signs to stability, write \(\dot y=yq(x,y)\), where \(q(x,y)=x(\lambda+Ay)/B(x,y)-s\) and \(B(x,y)=b+y+hx(\lambda+Ay)\). Direct differentiation gives \(q_y=x(Ab-\lambda)/B(x,y)^2<0\) in the inhibitory regime. At a positive equilibrium, adding the second row of the Jacobian to the first replaces the first row by the gradient of \(s(Y-y)\) without changing the determinant. The second row is \(y(q_x,q_y)\), since \(q=0\) there. Thus
\[
\det J=sy(Y'q_y+q_x)=syq_y(Y'-Z'),
\]
where the last equality uses \(q(x,Z(x))=0\) and its derivative. The determinants at the three roots have signs \(+,-,+\). In particular, the middle equilibrium is a hyperbolic saddle.

**Three-state example.** Set \((r_1,k_1,s,k_0,h,A,\lambda,b)=(1,1,1,1/10,9/10,1,2,21/1000)\). Then \(Z(x)=2(x-21/200)/(10-x)\) and the feasible interval is \((21/200,1)\). Clearing the positive denominator there yields
\[
P(x)=100x^4-1110x^3+1110x^2-300x+21=0.
\]
Rational evaluations give opposite signs at the ends of each of the intervals
\[
(0.109668415,0.109668417),\quad (0.276024322,0.276024325),\quad (0.692199537,0.692199540).
\]
The additional sign change from \(P(10)=-1979\) to the positive limit at infinity puts a fourth root above 10, outside the feasible domain. The four disjoint brackets and degree four show that all roots are simple. The positive predator coordinates are approximately \(0.0009440362\), \(0.0351758023\), and \(0.1261736413\).

At the feasible roots, the Jacobian trace and determinant have the formulas \(\operatorname{tr}J=T(x)/H(x)\), \(\det J=(200x-21)D(x)/H(x)\), with
\[
\begin{aligned}
H(x)&=1979000x(10-x),\\
T(x)&=5937000x^4-63743800x^3+44138000x^2-4416800x+251559,\\
D(x)&=300x^4-6220x^3+34410x^2-22200x+2979.
\end{aligned}
\]
The rational brackets certify signs \((+,+,+),(+,-,+),(-,+,-)\) for \((\operatorname{tr}J,\det J,(\operatorname{tr}J)^2-4\det J)\), respectively. The equilibria are therefore a hyperbolic repelling node, a saddle and an attracting focus. Nonzero determinants give persistence by the implicit-function theorem; positivity, the strict parameter inequalities and the stability signs are open conditions. The upper bound excludes additional coexistence equilibria for these nearby parameters.

## Verification

The companion `check.py` gives exact rational checks for the specified examples. In particular it reconstructs the quartic and Jacobian polynomials and certifies their signs on the three isolating intervals using a derivative bound on each polynomial. For a polynomial \(U(x)=\sum_k u_k x^k\) on an interval inside \([0,1]\) with midpoint \(m\) and radius \(e\), a comparison \(|U(m)|>e\sum_k k|u_k|\) proves that the midpoint sign is valid on the full interval. Use \(U=T,D,H,T^2-4H(200x-21)D\) for these tests, noting \(200x-21>0\). The general count and determinant arguments above are analytical, not extrapolations of the examples.

## Relationship to prior work and limitations

Gao and Ta's model and nullclines provide the starting point. The two-state bound above applies to the original interpretation of positive cooperation throughout \(0<k_0<k_1\), with no additional restriction on their ratio. The neutral and inhibitory cases distinguish two continuations outside positive cooperation. This distinction is specific to the stated response law, not a general claim about hunting cooperation or Allee effects. No assertions are made about global dynamics, experimentally calibrated mechanisms or models with changes to the functional response.

## References

1. Y. Gao and T. V. Ta, *Bifurcation Analysis of a Predator–Prey Model with Allee Effect and Cooperative Hunting*, arXiv:2601.10739v1, 9 January 2026, https://arxiv.org/html/2601.10739v1.
2. D. Sen, S. Ghorai, M. Banerjee and A. Morozov, *Bifurcation analysis of the predator–prey model with the Allee effect in the predator*, Journal of Mathematical Biology 84 (2022), https://pmc.ncbi.nlm.nih.gov/articles/PMC8718388/.
3. Y. Du, B. Niu and J. Wei, *Global dynamics in a predator-prey model with cooperative hunting and Allee effect and bifurcation induced by diffusion and delays*, arXiv:2007.12801, https://arxiv.org/abs/2007.12801.
