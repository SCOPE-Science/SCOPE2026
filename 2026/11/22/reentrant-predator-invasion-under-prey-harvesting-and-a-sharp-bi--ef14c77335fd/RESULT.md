# Reentrant predator invasion under prey harvesting and a sharp bifurcation-direction threshold

## Finding

Consider a predator–prey system with prey retaliation, a saturating functional response, and saturation harvesting. Increasing prey harvest can change rare-predator invasion from impossible to possible and then back to impossible, with **exactly two** thresholds. At the first threshold, the emerging positive coexistence branch can be either forward or backward, according to a single sharp predator-self-limitation threshold; at the second threshold it is always forward. These are statements about local invasion and local equilibria, not universal long-term extinction or persistence.

Write
\[
 P=a(1-n),\quad B=b(1-n),\quad A=eP,\quad
 G(x)=\frac{Ax}{1+Bx}-d-vx,
 \quad H(x)=r\left(1-\frac{x}{K}\right)(1+qx).
\]
Suppose the strictly positive parameters satisfy \(0<n<1\), \(0<e<1\), \(qK\leq1\), and \(0<h<r\). The prey-only equilibrium is \((x_h,0)\), where \(H(x_h)=h\), and its predator invasion exponent is \(G(x_h)\).

Define \(T=A-v-dB\). If
\[
 A>(\sqrt v+\sqrt{dB})^2,
\]
let
\[
 x_{\pm}=\frac{T\pm\sqrt{T^2-4vBd}}{2vB},\qquad 0<x_-<x_+.
\]
When \(K>x_+\), the predator can invade the prey-only equilibrium **if and only if**
\[
 \boxed{H(x_+)<h<H(x_-).}
\]
The prey-only equilibrium is locally asymptotically stable outside the closed threshold values and is unstable within the open invasion interval. If the radical inequality fails, there is no positive invasion exponent at any harvesting level. If it holds but \(K\leq x_-\), no positive invasion exponent occurs; if \(x_-<K\leq x_+\), invasion occurs precisely for \(0<h<H(x_-)\). Equality at an endpoint is neutral and is not classified as strict invasion.

At either simple threshold \(x_0\in\{x_-,x_+\}\), define
\[
 R(x_0)=\frac{f_y(x_0,0)}{f_x(x_0,0)}>0,
 \qquad Q(x_0)=-m-G'(x_0)R(x_0),
\]
where \(f(x,y;h)\) denotes the prey right-hand side, with \(h=H(x_0)\). At the **high-harvest** threshold \(H(x_-)\), \(Q(x_-)<0\) for every \(m>0\); a locally attracting positive coexistence equilibrium exists immediately below that threshold. At the **low-harvest** threshold \(H(x_+)\), put
\[
 \boxed{m_{\rm crit}=-G'(x_+)R(x_+)>0.}
\]
If \(m<m_{\rm crit}\), the positive coexistence branch lies immediately **below** \(H(x_+)\), where the prey-only state is also attracting, and the positive branch is a saddle (backward transcritical). If \(m>m_{\rm crit}\), it lies immediately **above** \(H(x_+)\) and is a locally attracting sink (forward transcritical). The degenerate equality \(m=m_{\rm crit}\) is excluded from the branch-direction assertion.

An exact rational example is
\[
 (r,K,q,k,a,b,n,e,d,v,m)
 =\left(2,5,\frac1{10},\frac15,\frac32,1,\frac12,\frac12,\frac3{20},\frac1{10},\frac1{100}\right).
\]
For this example, \(x_-=1\), \(x_+=3\), and the two harvest thresholds are precisely \(26/25\) and \(44/25\). The low-harvest onset is backward because \(m_{\rm crit}=299/5500>1/100\). The local positive branches satisfy
\[
 y_*(h)=\frac{125}{61}\left(\frac{26}{25}-h\right)+O\!\left(\left(h-\frac{26}{25}\right)^2\right)
 \quad\text{as }h\uparrow\frac{26}{25},
\]
\[
 y_*(h)=\frac{125}{118}\left(\frac{44}{25}-h\right)+O\!\left(\left(h-\frac{44}{25}\right)^2\right)
 \quad\text{as }h\uparrow\frac{44}{25}.
\]
The first branch consists of saddles and the second of attracting sinks sufficiently close to their respective thresholds.

## Assumptions and scope

The integer-order (ordinary-differential-equation) specialization of the ecological model is
\[
 \begin{aligned}
 \dot x&=f(x,y;h)
 =\frac{rx}{1+ky}\left(1-\frac{x}{K}\right)
   -\frac{Pxy}{1+Bx}-\frac{hx}{1+qx},\\
 \dot y&=y\left(\frac{Ax}{1+Bx}-d-vx-my\right).
 \end{aligned}
\]
All constants \(r,K,q,k,a,b,d,v,m\) are strictly positive, \(0<n<1\), \(0<e<1\), and \(P,B,A\) are defined above. The assumption \(qK\le1\) selects the monotone prey-only branch; it is not claimed necessary for reentrant invasion in other harvesting regimes. Only harvesting \(0<h<r\) is considered. The results concern local stability of equilibria and invasion by an infinitesimal predator population. For the fractional-order ecological extension, no center-manifold or periodic-orbit assertion is made here.

## Proof

**1. Unique prey-only branch.** For \(y=0\), a positive prey equilibrium solves \(h=H(x)\). Since
\[
 H'(x)=\frac rK\big(qK-1-2qx\big)<0
 \quad\text{for }0<x<K,
\]
\(H\) decreases strictly from \(r\) to zero on \((0,K)\). Hence every \(0<h<r\) determines exactly one \(x_h\in(0,K)\). The prey-direction eigenvalue at \((x_h,0)\) is
\[
 f_x(x_h,0)=\frac{r x_h\big(q(K-2x_h)-1\big)}{K(1+qx_h)}<0.
\]
The other eigenvalue is \(G(x_h)\). Thus its sign exactly gives strict predator invasion or non-invasion, and negative \(G\) makes the whole prey-only equilibrium a hyperbolic sink.

**2. Exact number of invasion windows.** Multiplication by the strictly positive denominator gives
\[
 (1+Bx)G(x)=-vBx^2+(A-v-dB)x-d.
\]
This strictly concave quadratic is positive somewhere on \((0,\infty)\) precisely when \(T>0\) and \(T^2>4vBd\), equivalently \(A>(\sqrt v+\sqrt{dB})^2\). In that case its roots are exactly \(x_-,x_+\), both positive, and \(G(x)>0\) exactly for \(x_-<x<x_+\). Composing this interval with the strictly decreasing bijection \(h\mapsto x_h\) proves all stated carrying-capacity cases and the uniqueness of both thresholds when \(K>x_+\). If the strict criterion fails, the quadratic is never positive; at equality it can touch zero without creating an invasion interval.

**3. The bifurcation direction.** Direct differentiation at a prey-only equilibrium gives
\[
 f_y(x,0)=-rkx\left(1-\frac xK\right)-\frac{Px}{1+Bx}<0,
 \quad R(x)=\frac{f_y(x,0)}{f_x(x,0)}>0.
\]
At a simple zero \(x_0\) of \(G\), the Jacobian has one negative eigenvalue and one simple zero eigenvalue. On the local center manifold, measured by the predator coordinate \(y\), the prey coordinate has first-order displacement \(x-x_h=-R(x_0)y+O(y^2+|h-H(x_0)|y)\). Substitution into the predator equation yields
\[
 \dot y=\lambda(h)y+Q(x_0)y^2
 +O\big(|h-H(x_0)|y^2+|y|^3\big),
 \quad\lambda(h)=G(x_h),
\]
with \(Q(x_0)=-m-R(x_0)G'(x_0)\). By the simple-root factorization
\[
 G(x)=\frac{-vB(x-x_-)(x-x_+)}{1+Bx},
\]
\(G'(x_-)>0\), \(G'(x_+)<0\). Also \(\lambda'(H(x_0))=G'(x_0)/H'(x_0)\ne0\). Therefore the simple transcritical branch has
\[
 y_*(h)=-\frac{\lambda'(H(x_0))}{Q(x_0)}\big(h-H(x_0)\big)
 +O\big((h-H(x_0))^2\big),
\]
when \(Q(x_0)\ne0\). Its small eigenvalue has the opposite sign to \(\lambda(h)\). At \(x_-\), \(Q<-m<0\) and \(\lambda'<0\), so the branch is positive for \(h<H(x_-)\) and is attracting. At \(x_+\), \(\lambda'>0\) and \(Q=m_{\rm crit}-m\), proving the stated backward/forward alternative and local stability. These arguments are local and do not imply that a positive equilibrium exists throughout the entire invasion interval.

**4. Rational certificate.** For the displayed parameters,
\[
 (1+Bx)G(x)=-\frac1{20}(x-1)(x-3),
 \quad H(3)=\frac{26}{25},\quad H(1)=\frac{44}{25}.
\]
The exact derivatives and center coefficients are
\[
 \begin{array}{c|ccccc}
 x_0&H'(x_0)&G'(x_0)&R(x_0)&Q(x_0)&\lambda'(H(x_0))\\\hline
 3&-11/25&-1/25&299/220&61/1375&1/11\\
 1&-7/25&1/15&451/140&-118/525&-5/21
 \end{array}
\]
so the two slopes and the nondegenerate stability claims follow exactly. The standalone \(\texttt{CHECK.py}\) asserts these identities symbolically and checks two nearby positive equilibria and their Jacobian signs numerically.

## Verification

Run \(\texttt{python CHECK.py}\) with SymPy installed. The checker verifies the algebraic closure, denominator identity, exact thresholds, strict root derivatives, the sharp self-limitation cutoff, and both branch coefficients with exact rational arithmetic. As supplementary finite numerical checks it solves for coexistence states at \(h=10399/10000\) and \(h=17599/10000\), testing the predicted saddle and sink signs. The proof above, rather than these finite tests, establishes the universal statements.

## Relationship to prior work

Govindan and Singh (2026) introduce the fractional ecological model, derive its prey-only stability condition and analyze coexistence and harvest effects. Their prey-only condition contains the predator growth exponent \(G\), but does not classify its exact two harvest crossings or give the branch-direction cutoff \(m_{\rm crit}\). This is a new result for their classical-order specialization, not a claim that the existence of reentrant invasion is new in ecological theory. A published 2026 study of age-structured predator maturation obtains reentrant invasion through a different renewal mechanism and does not imply the present two-dimensional equilibrium/branch classification. Qin and Dong (2024) analyze a state-dependent impulsive pest-control system, while Öztürk (2026) analyzes invasion in a three-species fear system; neither examined set of equations contains the present combination of saturating prey harvest and prey-density-proportional predator retaliation. The 2025 anti-predator/refuge/additional-food study by Ojha and coauthors is related but its complete text was unavailable for comparison; it remains a priority risk.

## Limitations

The finding applies to a deterministic, autonomous two-species ODE at fractional order one, and to infinitesimal invasion and local equilibria. It does not prove global predator extinction outside the invasion interval, global persistence inside it, a global hysteresis loop, or statements for fractional-order memory dynamics. The case \(m=m_{\rm crit}\) requires higher-order analysis. Published literature may contain unlocated equivalent local bifurcation statements, especially in inaccessible comparative ecological models; absolute historical priority and independent validation are not established.

## References

- M. K. Govindan and A. K. Singh, “Dynamics and optimal harvesting of a fractional predator–prey system with fear and anti-predator mechanisms,” *PLOS ONE* 21 (2026), e0360316, published October 14, 2026. https://doi.org/10.1371/journal.pone.0360316
- W. Qin and Z. Dong, “The impact of resource limitation on the pest-natural enemy ecosystem with anti-predator behavior and fear effect,” *Advances in Continuous and Discrete Models* (2024), article 10. https://doi.org/10.1186/s13662-024-03804-9
- H. M. Öztürk, “Fear-mediated invasion dynamics in a two-predator–one-prey model,” *European Physical Journal Plus* 141 (2026), article 674. https://doi.org/10.1140/epjp/s13360-026-07832-0
- A. Ojha, S. Mandal, R. Singh, N. K. Thakur, and P. K. Tiwari, “Predator–prey dynamics in autonomous and nonautonomous settings: Impacts of anti-predator behavior, refuge, and additional food,” *Chaos, Solitons & Fractals* 196 (2025), 116409. https://doi.org/10.1016/j.chaos.2025.116409 (full text not inspected).
