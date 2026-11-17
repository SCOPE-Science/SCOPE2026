# Exact junction density, central localization, and corner laws for two square transversals

## Finding
Let \(Q=[0,1]^2\). Independently and uniformly by unit arclength on the four respective sides, take \((0,U)\), \((1,V)\), \((W,0)\), and \((Z,1)\), where \(U,V,W,Z\) are independent \(\operatorname{Unif}(0,1)\) variables. Join the first pair and the second pair into spanning straight segments. Their unique intersection \((X,Y)\) has a full explicit spatial law.

For interior coordinates \(0<x,y<1\), define
\[
\delta_x=\min(x,1-x),\qquad\delta_y=\min(y,1-y),\qquad
u=\min(\delta_x,\delta_y),\quad v=\max(\delta_x,\delta_y).
\]
Then its density relative to planar area is
\[
\boxed{f(x,y)=\frac{u\,[4v(1-v)-u]}{4(1-u)^2v^2(1-v)^2}.}
\]
The unique global maximum is \(f(1/2,1/2)=4\). The boundary behavior has two distinct forms. For positive fixed \(\xi,\eta\), set \(k=\min(\xi,\eta)/\max(\xi,\eta)\). At a corner,
\[
\boxed{\lim_{t\downarrow0}f(t\xi,t\eta)=k(1-k/4),\qquad
\Pr\{X\le\varepsilon,Y\le\varepsilon\}=\frac5{12}\varepsilon^2+o(\varepsilon^2).}
\]
Along a complete side,
\[
\boxed{\Pr\{X<\varepsilon\}=\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).}
\]
Reflections give identical conclusions for the other three sides and corners. Thus the junction law is not area-uniform: its central density is four times the unit-square uniform density, its microscopic corner profile is direction dependent, and thin boundary strips have a logarithmically enhanced quadratic decay.

## Assumptions and scope
The two chord families are *distinguished*: one joins the left and right edges; the other joins bottom and top. Endpoints are chosen independently with uniform edge-length measures. This is neither motion-invariant isotropic line sampling nor perimeter-uniform unrestricted endpoint pairing. The square is of side one; every similarity-scaled square has the corresponding rescaled law. All assertions concern the almost-sure unique intersection of the two spanning segments and planar Lebesgue densities. Formulae at the boundary or diagonal seams are interpreted via interior limits; assigning an arbitrary value to a zero-area boundary does not change the law.

## Proof
Write the two supporting lines as
\[
y=ax+b,\qquad x=cy+d,\qquad a=V-U,\ b=U,\ c=Z-W,\ d=W.
\]
The transformation from the four independent uniform endpoints to \((a,b,c,d)\) has absolute Jacobian one. Every left-to-right continuous spanning segment intersects every bottom-to-top spanning segment in the square; the intersection is unique almost surely since the slopes satisfy \(|a|,|c|<1\), so \(1-ac>0\). At a candidate \((x,y)\), the intercepts must be \(b=y-ax\), \(d=x-cy\). Their change-of-variables Jacobian is \(1-ac\). The admissible slope intervals are
\[
I(x,y)=\left[\max\left(\frac{y-1}{x},-\frac{y}{1-x}\right),\;
\min\left(\frac{y}{x},\frac{1-y}{1-x}\right)\right],
\]
and \(I(y,x)\) for \(c\). Consequently
\[
f(x,y)=\int_{I(x,y)}\int_{I(y,x)}(1-ac)\,dc\,da.
\]
This identity is exact because the map from endpoint parameters to the intersection and the two slopes is one-to-one outside null sets.

By the endpoint and square symmetries, reduce to the wedge \(0<x<y\), \(x+y<1\). There the slope intervals simplify to
\[
I(x,y)=\left[-\frac{y}{1-x},\frac{1-y}{1-x}\right],\qquad
I(y,x)=\left[-\frac{x}{1-y},\frac{x}{y}\right].
\]
Their lengths are \(1/(1-x)\) and \(x/[y(1-y)]\); their means are \((1-2y)/[2(1-x)]\) and \(x(1-2y)/[2y(1-y)]\). Integration yields
\[
f(x,y)=\frac{x[4y(1-y)-x]}{4(1-x)^2y^2(1-y)^2}.
\]
The global formula follows from the four wedge symmetries: in the wedge \(u=x\), while \(v(1-v)=y(1-y)\). Normalization is automatic from the probability-preserving change of variables. Direct quadrature gives \(4\int_0^{1/2}\int_x^{1-x}f(x,y)\,dy\,dx=1\), independently checked numerically.

For the maximum, fix \(u\le v\le1/2\) and set \(T=v(1-v)\). Then
\[
f=\frac{u}{4(1-u)^2}\left(\frac4T-\frac{u}{T^2}\right).
\]
Since \(T\ge v/2\ge u/2\), its derivative with respect to \(T\) is nonpositive. Thus \(f(u,v)\le f(u,u)=(3-4u)/[4(1-u)^4]\). The last expression has derivative \((2-3u)/(1-u)^5>0\) on \(0<u\le1/2\), giving a unique maximum \(4\) at \(u=v=1/2\), i.e. the center.

For corner scaling, set \(x=t\xi\), \(y=t\eta\), with fixed positive \(\xi,\eta\). Then \(u=t\min(\xi,\eta)\), \(v=t\max(\xi,\eta)\) for small \(t\), giving the stated limit \(k(1-k/4)\). The uniform bound \(f\le4\) permits dominated convergence on a rescaled corner square:
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr(X,Y\le\varepsilon)}{\varepsilon^2}
=2\int_0^1\int_0^v\left(\frac uv-\frac{u^2}{4v^2}\right)du\,dv=\frac5{12}.
\]

For the strip law, fix \(0<x<1/2\). The two short intervals \(0<y<x\) and \(1-x<y<1\) contribute \(O(x)\) to the marginal density \(p_X(x)\), by \(f\le4\). In the remaining interval \(x<y<1-x\), use the wedge formula to obtain
\[
\begin{aligned}
p_X(x)&=\frac{x}{1-x}\int_x^{1-x}\frac{dy}{y(1-y)}
-\frac{x^2}{4(1-x)^2}\int_x^{1-x}\frac{(1-2y)^2\,dy}{y^2(1-y)^2}+O(x)\\
&=2x\log(1/x)+O(x),
\end{aligned}
\]
because the second integral is \(O(1/x)\). Integration from zero to \(\varepsilon\) proves the strip assertion and its error term.

## Verification
The supplied standalone `check.py` independently computes the intersection coordinates directly from four random endpoints, checks the exact density against region-wise quadrature, integrates the fundamental-wedge density to one, verifies central maximality on a grid, and tests the corner and logarithmic side-layer limits. It uses a deterministic random seed and a sample of 1,800,000 configurations. Execution printed `FORCED_SQUARE_TRANSVERSAL_DENSITY_CORNER_AND_LAYER_OK`. The analytic change-of-variables and limiting arguments, not simulation, establish the theorem.

## Relationship to prior work
Bäsel (2014) computes chord lengths under the motion-invariant line measure and distances between two independent interior points in regular polygons, not junction locations of independent spanning families. Böttcher (2019) studies intersections of independently positioned, fixed-length random needles with random orientations, rather than compulsory crossings of two opposite-side transversals. Egan's later square and polytope work studies which sides a line through two interior-random points intersects, not where two independent edge-to-edge chords intersect. The older rectangle-distance paper of Mathai, Moschopoulos and Pederzoli (1999) was available by abstract only; its described observable is interpoint distance. Earlier general intersection-change-of-variables identities are not claimed as new. The novel assessed statement is the explicit spatial density together with its exact central extremum and boundary/corner signatures, not the standard crossing-existence fact.

## Limitations
Historical priority is provisional; unindexed or inaccessible literature might contain the same specialized spatial law. No random orientation of the square, nonuniform endpoint distributions, curved transversals, or higher-dimensional generalization is asserted. Only one forced perpendicular-side pairing of two independent straight segments is considered. The numerical checks corroborate but do not replace proof or independent validation.

## References
1. U. Bäsel, *Random chords and point distances in regular polygons*, Acta Math. Univ. Comenianae 83 (2014), 1–18. Public date 2014-05-14. https://www.iam.fmph.uniba.sk/amuc/ojs/index.php/amuc/article/view/71
2. L. Böttcher, *A Random-Line-Graph Approach to Overlapping Line Segments*, arXiv:1911.10679 (first posted 2019-11-16). https://arxiv.org/abs/1911.10679
3. G. Egan, *Pick Two Points*, public article on line-through-point side-pair probabilities (2025). https://www.gregegan.net/SCIENCE/PickTwoPoints/PickTwoPoints.html
4. A. M. Mathai, P. G. Moschopoulos and G. Pederzoli, *Random points associated with rectangles*, Rend. Circ. Mat. Palermo 48 (1999), 163–190, DOI:10.1007/BF02844387 (abstract inspected only).
