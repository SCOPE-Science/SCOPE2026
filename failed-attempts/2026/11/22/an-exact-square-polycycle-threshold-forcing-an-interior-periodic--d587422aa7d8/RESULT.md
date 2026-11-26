# An exact square-polycycle threshold forcing an interior periodic orbit in a quartic flow

## Finding

Consider the quartic planar differential system
\[
\begin{aligned}
\dot x&=(1-x^2)(\lambda x-y+a x^2+bxy-a y^2),\\
\dot y&=(1-y^2)(x+\lambda y+c x^2+dxy+e y^2),
\end{aligned}
\]
with real parameters \((\lambda,a,b,c,d,e)\), as introduced by Grau and Szántó [1]. Put \(S=[-1,1]^2\) and \(g=c+e\). Assume the explicitly checkable strict directed-edge chamber
\[
\boxed{|\lambda|+|a|+|b|<1,\qquad
|\lambda|+|c|+|d|+|e|<1.}\tag{A}
\]
Then the boundary of \(S\) is one counterclockwise heteroclinic four-saddle cycle. Its exact characteristic product is
\[
\boxed{\rho=\frac{((1+\lambda)^2-b^2)((1+\lambda)^2-(g+d)^2)}
{((1-\lambda)^2-b^2)((1-\lambda)^2-(g-d)^2)}.}\tag{1}
\]
The transverse first-return map \(\mathcal R\), measured on any fixed inward section of an open edge, satisfies
\[
\boxed{\lim_{r\downarrow0}\frac{\log\mathcal R(r)}{\log r}=\rho.}\tag{2}
\]
In particular, the square cycle is asymptotically attracting from the interior for \(\rho>1\), whereas for \(\rho<1\) it is locally transversely repelling. There is no claim at \(\rho=1\). Formula (1) depends on \(c,e\) only through their sum and does not depend on \(a\), although the flow in the open edges does depend on them.

For the explicit two-parameter slice
\[
(\lambda,a,b,c,d,e)=(-\varepsilon,0,0,h,-h,0),
\qquad 0<\varepsilon<1,\quad 0<h<\frac{1-\varepsilon}{2},\tag{3}
\]
put
\[
h_{\mathrm{crit}}(\varepsilon)=
\frac{\sqrt{2\varepsilon(1+\varepsilon^2)}}{1+\varepsilon}.
\]
The square is attracting if and only if \(h>h_{\mathrm{crit}}(\varepsilon)\), and is transversely repelling if and only if \(h<h_{\mathrm{crit}}(\varepsilon)\). **Whenever**
\[
\boxed{h_{\mathrm{crit}}(\varepsilon)<h<(1-\varepsilon)/2,}\tag{4}
\]
there exists at least one nonconstant periodic orbit entirely inside \((-1,1)^2\). The origin is simultaneously a hyperbolic attracting focus, and there is no other equilibrium in the open square. Thus the existence follows from coexistence of two disjoint attracting invariant sets and is not a local Hopf-bifurcation assertion. One exact instance is \(\varepsilon=1/100\), \(h=1/4\), for which
\[
\rho=\frac{32019867}{26185967}>1.
\]

## Assumptions and scope

All assertions concern the real autonomous vector field printed above in *original physical time*, with coefficients satisfying (A); (3)--(4) are additional conditions only for the forced-periodic-orbit statement. The square is positively and negatively invariant wherever solutions exist; since it is compact and the vector field is smooth, its internal solutions exist for all time. A *heteroclinic square cycle* means the four corner saddles and the four open edges connecting them counterclockwise. The characteristic product is the product of the absolute stable-to-unstable eigenvalue ratios at the four saddles. A section coordinate \(r>0\) is a regular smooth transverse distance into the square near a chosen noncorner point. Changing sections modifies multiplicative factors but not the exponent in (2).

The strict chamber (A) is a convenient sufficient condition that forbids other edge equilibria. It is not claimed to describe *every* parameter choice with a directed square. No classification is claimed at the characteristic equality \(\rho=1\), and no uniqueness, Floquet type, or count beyond existence is claimed for interior periodic orbits.

## Proof

**1. A directed square without other boundary equilibria.** On the bottom edge \(y=-1\), the first parenthetical factor in \(\dot x\) is
\[
1+\lambda x+a(x^2-1)-bx>0
\]
for \(-1\le x\le1\), because its difference from \(1\) has absolute value at most \(|\lambda|+|a|+|b|<1\). The same factor is negative on the top edge \(y=1\), where it equals \(-1+\lambda x+a(x^2-1)+bx\). Hence the bottom edge runs rightward and the top edge leftward. On the right edge \(x=1\), the second parenthetical factor is \(1+\lambda y+c+dy+ey^2>0\); on the left it is \(-1+\lambda y+c-dy+ey^2<0\). Their deviations from \(\pm1\) are bounded by the second strict inequality in (A). Thus the right edge runs upward and the left downward. The only stationary points on the boundary are its four corners, and the entire boundary is one directed heteroclinic cycle.

**2. Corner eigenvalues.** Since \(1-x^2=1-y^2=0\) at every corner, its Jacobian is diagonal in the ambient \((x,y)\) axes. Write \(\sigma\) for the positive magnitude of the eigenvalue stable along the *incoming* edge, and \(\mu\) for the positive eigenvalue unstable along the *outgoing* edge. In cyclic order:

| Corner | Incoming stable rate \(\sigma\) | Outgoing unstable rate \(\mu\) |
| --- | --- | --- |
| \((1,-1)\) | \(2(1+\lambda-b)\) | \(2(1-\lambda+g-d)\) |
| \((1,1)\) | \(2(1+\lambda+g+d)\) | \(2(1-\lambda-b)\) |
| \((-1,1)\) | \(2(1+\lambda+b)\) | \(2(1-\lambda-g+d)\) |
| \((-1,-1)\) | \(2(1+\lambda-g-d)\) | \(2(1-\lambda+b)\) |

All eight rates are strictly positive by (A). Multiplying the four ratios \(\sigma/\mu\) gives exactly (1), using paired differences of squares. Each corner is therefore a hyperbolic saddle, with precisely the connecting stable and unstable separatrices prescribed by the invariant edges.

**3. The return exponent and its dynamical consequences.** At one hyperbolic saddle choose local coordinates \((u,v)\) with incoming edge \(u=0\), outgoing edge \(v=0\), and positive interior \(u,v\). After straightening the smooth local stable and unstable invariant manifolds, the equations factor as \(\dot u=u(\mu+O(\|(u,v)\|))\) and \(\dot v=v(-\sigma+O(\|(u,v)\|))\). For a small incoming displacement \(r\), the local passage to a fixed outgoing section satisfies
\[
\lim_{r\downarrow0}\frac{\log r_{\mathrm{out}}}{\log r}=\frac{\sigma}{\mu}.
\]
One may derive this without assuming nonresonant smooth linearization: choose an arbitrarily small saddle box, bound the logarithmic derivatives between \(\mu\pm\eta\) and \(-\sigma\pm\eta\), integrate from one transverse side to the other, and then let the box size (hence \(\eta\)) tend to zero. Smooth regular passage along each compact open edge has positive finite transverse derivative and contributes exponent one. Composing all four local passages yields (2). For \(\rho>1\), (2) implies \(0<\mathcal R(r)<r\) for every sufficiently small positive \(r\), with successive iterates tending to zero; the edge passages then give attraction to the entire square as a compact set and an open inner collar in its basin. For \(\rho<1\), the inequalities reverse sufficiently close to the cycle, giving transverse repulsion. Neither argument resolves the resonant equality.

**4. Exact slice transition.** Substituting (3) into (1) gives
\[
\rho(\varepsilon,h)=
\frac{(1-\varepsilon)^4}
{(1+\varepsilon)^2((1+\varepsilon)^2-4h^2)}.
\]
Its denominator is positive by the strict range in (3). Clearing this denominator, \(\rho>1\) is equivalent to
\[
4h^2(1+\varepsilon)^2>8\varepsilon(1+\varepsilon^2),
\]
which is equivalent to \(h>h_{\mathrm{crit}}(\varepsilon)\) because \(h>0\). The reverse strict inequality gives the repelling branch.

**5. Interior equilibrium and periodic-orbit existence.** Inside \(S\), the stationary equations on slice (3) reduce to
\[
y=-\varepsilon x,\qquad
x\bigl(1+\varepsilon^2+h(1+\varepsilon)x\bigr)=0.
\]
Their solutions are the origin and the formal second root \(x=- (1+\varepsilon^2)/(h(1+\varepsilon))\). By \(h<(1-\varepsilon)/2\), this root is strictly less than \(-1\); hence there is exactly one equilibrium in the open square. The linearization at the origin is
\[
\begin{pmatrix}-\varepsilon&-1\\1&-\varepsilon\end{pmatrix},
\]
whose eigenvalues are \(-\varepsilon\pm i\), so the origin has an open attracting basin. If (4) holds, the heteroclinic boundary has an open attracting interior collar disjoint from that basin. Thus the origin's basin, considered inside the open square, is a nonempty proper open invariant set whose closure is separated from the square boundary. Its nonempty topological boundary \(K\) is consequently a compact invariant subset of the open square disjoint from the origin. There are no other equilibria anywhere in the open square. Choose any \(z\in K\). The positive orbit of \(z\) stays inside \(K\), so its nonempty compact \(\omega\)-limit set contains no equilibrium. By the Poincaré--Bendixson theorem it must be a periodic orbit, and it lies strictly inside the square. This proves the existence statement without asserting the orbit is unique or hyperbolic.

For the rational witness, direct arithmetic yields \(\rho=32019867/26185967\) and the two inequalities (3)--(4), so its existence assertion is nonvacuous. \(\square\)

## Verification

Run `python3 VERIFY.py` beside this file. The standalone Python-standard-library checker evaluates corner Jacobians and saddle ratios with exact rational arithmetic, verifies the exact positive-ratio witness, the strict square-edge hypotheses, the unique-interior-equilibrium algebra, and a rational contrasting parameter point with \(\rho<1\). Its finite mesh checks of edge orientation are diagnostics only; the all-real sign bounds and return-map argument above constitute the proof. Expected output: `SQUARE_HETEROCLINIC_VERIFY_OK`.

## Relationship to prior work

Grau and Szántó [1, especially their defining equation (3) and Theorems 1--2] introduced the exact six-parameter quartic family and studied centers and local limit-cycle bifurcations. Their existence of at least five small-amplitude cycles for other parameter choices does **not** imply a characteristic-product formula at the invariant boundary or existence on the explicit two-parameter chamber (4). Gasull, Gouveia and Santana [2] studied a broader class of quartic flows with invariant squares, proving center bounds and several multi-cycle realizations, but did not establish this boundary transition. Closely related published boundary analyses [3, 4] classify, respectively, the total number of boundary equilibria in the same restricted family and the maximal number of hyperbolic boundary sinks in a broader family. Neither determines a four-saddle heteroclinic return exponent or forces an interior orbit from the coexistence of the sink and an attracting square.

The general saddle characteristic-product method and Poincaré--Bendixson theorem are classical inputs; the contribution claimed here is their explicit, all-parameter algebraic evaluation in this natural published family, together with the specified forced-cycle region and exact witness. No blanket priority or exhaustive literature coverage is claimed.

## Limitations

The coefficient chamber (A) is sufficient, not necessary, for a directed square; outside it extra edge equilibria can occur, invalidating the four-saddle description. No conclusion is offered for \(\rho=1\) or for the number, stability, or amplitude of interior cycles. The proof establishes existence without computing an orbit explicitly. The periodic orbit is not a global attractor claim. An equivalent classification in literature not located in the inspected sources remains possible. No independent mathematical audit has been performed.

## References

1. M. Grau and I. Szántó, *A Polynomial System of Degree Four with an Invariant Square Containing At Least Five Limit Cycles*, *Qualitative Theory of Dynamical Systems* **23**, 247 (first public online 2024-07-26), https://doi.org/10.1007/s12346-024-01106-9 . Complete open-access mathematical article, including equation (3) and the primary theorems, examined.
2. A. Gasull, L. F. S. Gouveia and P. Santana, *On the limit cycles of a quartic model for evolutionary stable strategies*, arXiv:2410.15354v1 (2024-10-20), https://arxiv.org/abs/2410.15354 . Complete accessible arXiv text examined.
3. *Sharp eleven-equilibrium boundary chamber in a quartic invariant-square flow*, public research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-eleven-equilibrium-boundary-chamber-in-a-quartic-invariant--d9a0fbcc188c . Its complete result/proof inspected for the different boundary-equilibrium-count claim.
4. *Five is the sharp boundary-sink capacity of quartic invariant-square flows*, public research record (2026-11-17), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-five-is-the-sharp-boundary-sink-capacity-of-quartic-invariant-sq--114cf2c96c23 . Its complete result/proof inspected for the different boundary-sink-count claim.
