# Arithmetic isolation at the neutral coupling of signed integer-slope Lorenz lattices

## Finding
For every integer \(q\ge3\), both signs \(s\in\{-1,1\}\), and the two neutral couplings \(c_{\pm}=(1\pm1/q)/2\), the two-node coupled map with \(f(u)=squ\pmod1\) has an exact nonconstant, continuous first integral
\[
 H_q(x,y)=\cos(2\pi q(x-y)).
\]
The more geometric first integral
\[
 \rho_q(x,y)=\operatorname{dist}(x-y,q^{-1}\mathbb Z)
\]
provides the permanent separation bound \(|x_n-y_n|\ge\rho_q(x_0,y_0)\) at **every** nonnegative integer time. Thus almost every initial pair never approaches the synchronization diagonal arbitrarily closely: neither synchronization nor intermittent synchronization occurs at either neutral endpoint. These equalities are explicitly outside the strict coupling intervals in the ternary map theorem of Zhang and Wang [1].

When the two initial coordinates are independent uniform variables on \([0,1]\), the invariant \(\rho_q\) is exactly uniform on \([0,1/(2q)]\). In particular, for \(0\le\varepsilon\le1/(2q)\),
\[
 \mathbb P\big(\exists n\ge0:\ |x_n-y_n|<\varepsilon\big)\le 2q\varepsilon.
\]
For any ergodic invariant Borel probability measure, \(\rho_q\) is almost surely constant and the measure is singular relative to planar Lebesgue measure. There is **no unique absolutely continuous invariant probability measure** at these endpoints: either none exists, or uncountably many distinct such measures exist. This does **not** assert their existence.

For the directly motivated ternary case \(q=3\), the endpoints are \(c=1/3\) and \(c=2/3\), the invariant is \(\cos(6\pi(x-y))\), and the exact uniform guaranteed-gap interval is \([0,1/6]\).

## Assumptions and scope
Fix an integer \(q\ge3\) and a slope sign \(s\in\{-1,1\}\). Use the floor convention
\[
 f(u)=squ-\lfloor squ\rfloor,\qquad 0\le u\le1,
\]
so the map lies in \([0,1)\) even at branch discontinuities. The coupled dynamics is
\[
 T_c(x,y)=\big((1-c)f(x)+cf(y),\; cf(x)+(1-c)f(y)\big),
\]
with \(c\in\{(1-1/q)/2,(1+1/q)/2\}\subset(0,1)\). The unit square is forward invariant because both coordinates are convex combinations of values of \(f\). No differentiability is assumed at branches; the proof uses exact integer arithmetic, including on boundaries. Lebesgue-a.e. always refers to two-dimensional area on the square.

## Proof
**Integer branch identity.** Let \(k(u)=\lfloor squ\rfloor\in\mathbb Z\), and let \(\delta=x-y\). Subtracting the two components gives the exact identity
\[
 \delta'=(1-2c)\big(sq\delta-[k(x)-k(y)]\big).
\]
At either specified coupling there is \(\eta\in\{-1,1\}\) such that \(1-2c=\eta/q\). Consequently
\[
 q\delta'=\eta s q\delta-\eta[k(x)-k(y)],
\]
so \(q\delta'\equiv \eta s q\delta\pmod{\mathbb Z}\). Both cosine and circular distance to the integer lattice are unchanged by sign reversal and integer translation. Therefore \(H_q(T_c(x,y))=H_q(x,y)\) and \(\rho_q(T_c(x,y))=\rho_q(x,y)\), for **all** points including discontinuity boundaries. Induction gives these invariances for every iterate.

**Nonapproach to the diagonal.** Because \(0\in q^{-1}\mathbb Z\), \(\rho_q(x_n,y_n)\le|x_n-y_n|\) at every time. The initial radius vanishes precisely on the finite union of line segments \(x-y=j/q\) meeting the square, which has planar Lebesgue measure zero. At every other initial pair the orbit is permanently at distance at least \(\rho_q(x_0,y_0)>0\) in coordinate-difference units. Thus both convergence of coordinate difference to zero and the zero-liminf criterion for intermittent synchronization are excluded almost everywhere. The invariant \(H_q\) is nonconstant, so the map is not topologically transitive on the full square either.

**Exact gap law.** If \(X,Y\) are independent uniform variables on \([0,1]\), the fractional parts of \(qX\) and \(qY\) are independent uniform variables on \([0,1)\). Their difference modulo one is uniform. Its distance to the nearest integer is uniform on \([0,1/2]\). Dividing by \(q\) shows \(\rho_q(X,Y)\sim\mathrm{Uniform}[0,1/(2q)]\); therefore \(\mathbb P(\rho_q<\varepsilon)=2q\varepsilon\) in the stated range. Any iterate with \(|x_n-y_n|<\varepsilon\) requires \(\rho_q<\varepsilon\), establishing the claimed union-over-all-times probability bound. This probability bound need not be an equality.

**Invariant-measure obstruction.** If a Borel probability measure \(\mu\) is invariant and ergodic, every invariant measurable observable is almost surely constant, hence \(\rho_q=t\) \(\mu\)-almost surely for some \(t\). Each level set of \(\rho_q\) is a finite union of line segments, null for planar Lebesgue measure. Thus \(\mu\) is singular. More generally, suppose an absolutely continuous invariant probability \(\nu\) exists. The pushforward distribution \((\rho_q)_*\nu\) has no atoms, because all levels have zero planar area. For every \(t\) for which \(0<\nu(\rho_q<t)<1\), the normalized restriction of \(\nu\) to \(\{\rho_q<t\}\) is another absolutely continuous invariant probability, since this set is exactly invariant under pullback. There are uncountably many such threshold values yielding distinct restrictions by non-atomicity. Consequently uniqueness is impossible, without assuming existence.

## Verification
The bundled standalone exact-rational checker evaluates both signed maps at both neutral couplings for a finite set of integer slopes, rational initial pairs, and repeated iterates, and checks the branch congruence, invariant distance, and pointwise gap bound. The analytic proof above handles arbitrary integer slopes and all real initial data; finite checks are supplementary rather than an infinite proof. Execute \(\texttt{python3 checks/verify_boundary.py}\).

## Relationship to prior work
Zhang and Wang [1, Theorems 1–2 and Sections IV–V] analyze the two-node maps with slopes \(2\) and \(\pm3\), proving intermittent synchronization outside the critical interval and synchronization strictly inside. Their ternary assertions use \(c<1/3\), \(c>2/3\), or \(1/3<c<2/3\); the endpoint equalities are omitted. The present result describes those omitted endpoints by a **global arithmetic first integral** rather than a transverse-exponent sign calculation. The earlier work of Li–Lin–Wang–Yau [2] treats continuous tent maps and does not provide this discontinuous Lorenz-map endpoint obstruction. Keller–Künzle–Nowicki [3] studied slope-two Lorenz-map lattices, including a full coupling-strength ergodic-component analysis for two sites; the claim here intentionally begins at \(q=3\), and no priority is claimed for the slope-two case. Full-text comparison with [3] was unavailable, a residual literature risk. The general signed-integer-slope formulation records the single arithmetic mechanism behind the ternary endpoint phenomenon, not independent repeated findings for each slope.

## Limitations
The result concerns exactly the two transverse-neutral coupling values and integer-slope, full-branch modular maps. It does not address perturbed nonlinear branches, more sites, noises, nor the existence or classification of absolutely continuous invariant probabilities. The initial-gap law is a law for the **guaranteed lower bound**, not the exact distribution of minimum achieved separations. Other invariant measures, possibly singular, may occur. Historical novelty is provisional because the full text of [3] could not be read; its identified slope-two statements do not directly entail the ternary assertion. Independent scientific validation has not been performed.

## References
[1] J. Zhang and Y. Wang, *Intermittent–synchronization in non-weakly coupled piecewise linear expanding map lattice: a geometric-combinatorics method*, arXiv:2507.14646v1, first public 2025-07-19. https://arxiv.org/abs/2507.14646

[2] T. Li, W.-W. Lin, Y. Wang, and S.-T. Yau, *Intermittent Behaviors in Coupled Piecewise Expanding Map Lattices*, Analysis in Theory and Applications **37** (2021), 481–519. DOI: 10.4208/ata.OA-2020-0020. https://www.global-sci.com/ata/article/view/8234

[3] G. Keller, M. Künzle, and T. Nowicki, *Some phase transitions in coupled map lattices*, Physica D **59** (1992), 39–51. DOI: 10.1016/0167-2789(92)90205-2. https://cris.fau.de/publications/119999044/
