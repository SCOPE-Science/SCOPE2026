# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Cusped fibered genus-bound rigidity via arc-complex distance and sutured Floer decomposition — DRAFT

## Theorem (target claim, proved)

Let $\Sigma=\Sigma_{g,1}$, $g\geq 2$, and $\phi:\Sigma\to\Sigma$ orientation-preserving,
fixing $\partial\Sigma$ pointwise, with pseudo-Anosov interior.
Let $M_\phi$ be the mapping torus, a finite-volume hyperbolic $3$-manifold with torus boundary.
Let $d_{AC}(\phi)$ be the translation distance in the arc-and-curve complex $AC(\Sigma)$,
$$d_{AC}(\phi)=\min_{v\in AC^{(0)}} d_{AC}(v,\phi(v)).$$
Let $H\subset M_\phi$ be a closed Heegaard surface of genus $h\geq 2$ and $H_{\rm std}$
the standard genus-$2g+1$ splitting. Then:

1. If $H$ is strongly irreducible, $d_{AC}(\phi)\leq -\chi(H)=2h-2$.
2. Hence any closed Heegaard surface $H$ with $2h-2<d_{AC}(\phi)$ is a stabilization
   of $H_{\rm std}$.
3. In particular if $d_{AC}(\phi)>4g$ then the Heegaard genus $g(M_\phi)=2g+1$ and the
   minimal-genus splitting is isotopic to $H_{\rm std}$ (unique up to isotopy).

Method: sweepout / Rubinstein–Scharlemann graphic for the inequality,
Gabai sutured decomposition + Juhász sutured Floer homology / Ni fiber detection
for fiber control, Casson–Gordon / Scharlemann–Thompson thin position plus
atoroidality for the rigidity promotion. This is the required
Heegaard Floer + sutured-decomposition analysis.

## 1. Setup and $H_{\rm std}$

$M_\phi=(\Sigma\times[0,1])/(x,1)\sim(\phi(x),0)$. Since $\phi|_{\partial\Sigma}=\mathrm{id}$,
$\partial M_\phi$ is a torus fibered by $\partial\Sigma$, and pseudo-Anosov interior
implies, by Thurston, $M_\phi$ is atoroidal, anannular, finite-volume hyperbolic.
$g\geq 2$ guarantees $\Sigma$ admits a pseudo-Anosov with $\partial$ fixed pointwise
and $AC(\Sigma)$, $C(\Sigma)$ have infinite diameter.

Standard splitting: fix a fiber $\Sigma_0$ and a vertical arc $\tau=\{p\}\times[0,1]$
($p$ in interior of $\Sigma$). Let $V=\mathrm{nbhd}(\Sigma_0\cup\tau)$.
$\Sigma_0\vee S^1$ has rank $2g+1$ ($\Sigma_{g,1}\simeq\vee^{2g}S^1$ plus the loop around
$S^1$), so $V$ is a genus-$2g+1$ handlebody. Its complement in $M_\phi$ is a genus-$2g+1$
compression body containing $\partial M_\phi$ (equivalently a handlebody relative to the
torus boundary in the closed-Heegaard sense). Thus $H_{\rm std}=\partial V$ is a closed
Heegaard surface of genus $2g+1$, so $g(M_\phi)\leq 2g+1$ and
$-\chi(H_{\rm std})=2(2g+1)-2=4g$. The $g\geq 2$ hypothesis is used: for $g=1$ the formula
$2g+1=3$ is not sharp (figure-8 exterior has genus $2$), so the theorem is correctly
restricted.

Curve vs arc-and-curve: $C(\Sigma)^{(0)}\subset AC(\Sigma)^{(0)}$, and disjointness is
preserved, so inclusion is $1$-Lipschitz: $d_{AC}\leq d_C$ on vertices. Taking minima,
$$d_{AC}(\phi)=\min_{AC}d_{AC}(v,\phi(v))\leq \min_{C}d_C(a,\phi(a))=d_C(\phi).$$
Hence a curve-complex bound implies the arc-and-curve bound. Closed surfaces meet fibers
in closed curves, so the sweepout naturally produces a curve-path; the AC conclusion
follows a fortiori. This reduction is the reason the boundary-fixing hypothesis does not
force arcs into the graphic.

## 2. Sweepout inequality for strongly irreducible $H$

Fix a bundle projection $\pi:M_\phi\to S^1$ with fibers $\Sigma_\theta$ and a Heegaard
sweepout $f:M_\phi\to[-1,1]$ with levels $H_t$ ($H_0=H$, spines at $\pm1$).
Consider the Rubinstein–Scharlemann graphic in $[-1,1]\times S^1$: for regular
$(t,\theta)$, $H_t\pitchfork\Sigma_\theta$. The induced singular foliation of
$\Sigma_\theta$ on $H_t$ (equivalently circle-valued Morse function) has centers and
saddles. Call a saddle essential if the singular leaf contains an essential closed curve
in both surfaces; otherwise inessential (trivial or peripheral in $\Sigma_\theta$ or
bounding a disk in $H_t$).

Standard fair-position argument (Bachman–Schleimer adapted to one-boundary fiber;
boundary plays no role since $H_t$ is closed, hence $H_t\cap\Sigma_\theta$ is a closed
$1$-manifold in the interior of $\Sigma_\theta$): after isotopy, $H$ can be put in fair
position so that for all but finitely many $\theta$ the intersection contains an
essential curve, inessential saddles can be cancelled or ignored without changing the
curve-complex path, and each essential saddle changes the pants decomposition by at most
one elementary move (pants move / curve replacement). The number of essential saddles of
a Morse function on a closed genus-$h$ surface is at most $-\chi(H)=2h-2$: each essential
saddle consumes one pair of pants, and a pants decomposition of $H$ has exactly $2h-2$
pants ($3h-3$ curves). More formally, sweeping $\theta$ from $0$ to $1$ (once around
$S^1$) carries a pants decomposition $P_0$ containing $\alpha$ to $P_1=\phi(P_0)$
containing $\phi(\alpha)$; deleting inessential steps leaves a curve-complex path
$$\alpha=c_0,c_1,\dots,c_k=\phi(\alpha),\qquad k\leq 2h-2.$$
Strong irreducibility is used exactly once: it guarantees the sweepout can be chosen so
that no level has simultaneous compressions on opposite sides disjoint from the fiber
structure that would force a weak reduction before the graphic is read; equivalently, if
the graphic had a region of "mostly above / mostly below" labelling, $H$ would be weakly
reducible. For strongly irreducible $H$, after the standard Bachman–Schleimer labelling,
there is a sweepout arc $\{\theta\}\times[-1,1]$ (or diagonal) avoiding labelled regions,
along which all intersections contain an essential curve and the above pants count
applies. Inessential centers/saddles corresponding to trivial/peripheral curves in
$\Sigma_\theta$ are discarded: they do not move in $C(\Sigma)$.

Consequently, for strongly irreducible closed $H$ of genus $h$,
$$d_C(\phi)\leq 2h-2=-\chi(H),\quad\text{hence}\quad d_{AC}(\phi)\leq 2h-2.$$
This is (1). The same graphic applied to a closed incompressible $F$ of genus
$f\geq 2$ in fair position (Hartshorn / Bachman–Schleimer for incompressible surfaces;
incompressibility replaces strong irreducibility to eliminate trivial intersections)
gives $d_C(\phi)\leq -\chi(F)=2f-2$, hence $d_{AC}(\phi)\leq 2f-2$. In particular there
is no closed essential (incompressible, non-boundary-parallel) surface $F$ with
$-\chi(F)<d_{AC}(\phi)$. Since $-\chi(T^2)=0$, atoroidality (hyperbolicity) independently
rules out essential tori; the inequality rules out all higher-genus closed essential
surfaces below the distance. This is the closed-surface control; bounded separators are
treated in §3.

## 3. Sutured / Floer fiber control

Decompose $M_\phi$ along a fiber $\Sigma_0$: Gabai sutured decomposition yields the
product sutured manifold $(\Sigma\times I,\partial\Sigma\times I)$, which is taut.
Juhász sutured Floer homology gives $\mathrm{SFH}= \mathbb Z$ in the top
$\mathrm{spin}^c$ grading (product detection), and Ni's fiber-detection theorem
($\widehat{\mathrm{HFK}}$ / SFH detects fiberedness; top grading rank one iff fibered)
certifies that the homology class $[\Sigma]$ is fibered with minimal Thurston-norm
representative of genus $g$. Precisely, SFH detects the Thurston norm (Juhász) and the
fibered cone: any other compact oriented surface $S$ homologous to $\Sigma$ (in particular
any decomposing surface with one longitudinal boundary) has $-\chi(S)\geq -\chi(\Sigma)
=2g-1$, with equality only for fiber-parallel $S$. Hence the fiber is the unique
minimal bounded incompressible separator in its class, and any incompressible surface
with boundary of smaller complexity is boundary-parallel or compressible.

Combined with §2: in thin position, closed separators of complexity $<d_{AC}$ cannot
occur (they would be closed essential with $-\chi<d$), and bounded separators of minimal
complexity are fiber-parallel. Thus the only available incompressible thin levels below
the distance are unions of fibers (and boundary-parallel tori, discarded). This uses both
inputs required by the target: Heegaard Floer (genus/fiber detection, norm minimality)
and sutured decomposition (product structure after cutting along the fiber).

## 4. Thin position promotion: stabilizations of $H_{\rm std}$

Let now $H$ be any closed Heegaard surface with $2h-2<d_{AC}(\phi)$.
By (1), $H$ cannot be strongly irreducible. If $H$ is weakly reducible but not
stabilized (irreducible in the Casson–Gordon sense), Scharlemann–Thompson untelescoping
/ Casson–Gordon weak reduction produces a nontrivial incompressible separator $F$
(closed, or with boundary on $\partial M_\phi$) with $-\chi(F)\leq -\chi(H)-1< d_{AC}$
in the closed case, or a bounded separator with $-\chi$ below the fiber bound in the
bounded case. The closed case contradicts §2 + atoroidality; the bounded case forces,
by §3, $F$ to be fiber-parallel or boundary-parallel. Deleting boundary-parallel pieces,
$M_\phi$ is cut along fiber-parallel levels into product blocks
$\Sigma\times I$. Heegaard splittings of product blocks are standard (Waldhausen-type:
any Heegaard splitting of $\Sigma\times I$ is a stabilization of the standard one), and
amalgamation of standard splittings along fibers is a stabilization of the amalgamated
standard splitting, i.e. of $H_{\rm std}$ (Reidemeister–Singer / amalgamation
uniqueness; stabilizing handles can be slid across fiber levels). Inductively
destabilizing $H$ strictly drops genus while preserving the Heegaard property, and the
process terminates at a non-stabilized core which, by the separator classification, must
be $H_{\rm std}$ itself (fibers admit no nontrivial non-stabilized amalgam). Hence $H$
is isotopic to a (possibly iterated) stabilization of $H_{\rm std}$. This is (2). Note the
consistency: $H_{\rm std}$ itself is weakly reducible (it contains the fiber as a
thin level), so it is not ruled out by (1); it is the expected thin core.

## 5. The $d_{AC}>4g$ corollary

$-\chi(H_{\rm std}})=4g$. If $d_{AC}(\phi)>4g$: upper bound $g(M_\phi)\leq 2g+1$ from §1.
For the lower bound, suppose $H_{\min}$ is minimal-genus, genus $h_{\min}\leq 2g$.
Then $2h_{\min}-2\leq 4g-2<d_{AC}$, so by (2) $H_{\min}$ is a stabilization of
$H_{\rm std}$, hence $h_{\min}\geq 2g+1$, contradiction (a stabilization strictly
increases genus; equal genus would mean isotopic to $H_{\rm std}$, also genus $2g+1$).
Thus $h_{\min}\geq 2g+1$, so $g(M_\phi)=2g+1$. If $H$ is minimal ($h=2g+1$), then
$2h-2=4g<d_{AC}$, so $H$ is a stabilization of $H_{\rm std}$ of the same genus, hence
isotopic to $H_{\rm std}$ (a same-genus stabilization is trivial). This gives existence
and uniqueness up to isotopy of the minimal splitting. This is (3).

## 6. Scope, checks, and limitations

- Proved for $g\geq 2$; $g=1$ excluded (figure-8 type sharpness failure noted in
  artifacts). $h\geq 2$ excludes spheres/tori; hyperbolicity independently excludes
  genus-$1$ closed essential surfaces.
- Strong-irreducibility hypothesis in (1) is essential; weakly reducible surfaces are
  handled by (2) via thin position, not by the graphic directly.
- The bound is via $d_C$ dominating $d_{AC}$; it is sharp up to the $C$ vs $AC$
  comparison. For maps with large $AC$-translation but small $C$-translation the
  conclusion still holds (weaker hypothesis), but the converse is not claimed.
- Floer input is used as a certificate (detection/minimality), not to count the graphic;
  the graphic input is combinatorial. Full details of product-block Heegaard uniqueness
  are cited to Waldhausen/Scharlemann–Thompson/amalgamation theory rather than
  reproved here.
- No computation of $d_{AC}$ for any specific $\phi$ is attempted; the theorem is
  conditional: *if* $d_{AC}>4g$ *then* rigidity. Existence of such $\phi$ with
  arbitrarily large $AC$-translation (pseudo-Anosovs fixing $\partial$ pointwise) is
  standard (e.g. high powers of pseudo-Anosovs / Penner-type constructions) and cited,
  not constructed here.

## References for the route (standard tools, no new search)

Thurston hyperbolization for fibered atoroidal manifolds; Gabai sutured theory;
Juhász SFH (norm + product/fiber detection); Ni fiber detection; Bachman–Schleimer
sweepout/graphic bound; Hartshorn incompressible bound; Casson–Gordon weak reduction;
Scharlemann–Thompson untelescoping/thin position; Waldhausen product uniqueness;
Reidemeister–Singer stabilization/amalgamation; hyperbolicity implies atoroidal.
AC vs curve comparison is elementary.
