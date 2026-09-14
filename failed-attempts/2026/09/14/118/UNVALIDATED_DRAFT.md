# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Divergence spectra are not universally two-point in the planar exponential regime

## Self-contained disproof of the universal claim (TARGET route)

**Admitted target.** Let $\Gamma$ satisfy the Nguyen–Tran Standing Assumptions
(connected, triangle-free, planar, $\ge 5$ vertices, no separating vertex or
edge) and be non-CFS. Then $G_\Gamma$ is relatively hyperbolic over CFS
right-angled Coxeter subgroups with global divergence $\sim \exp$. Let
$\mathrm{Spec}(G_\Gamma)$ be Tran's divergence spectrum: asymptotic classes of
lower divergences $\mathrm{ldiv}_\alpha$ over Morse bi-infinite geodesics
$\alpha$. The target asks whether universally
$\mathrm{Spec}(G_\Gamma)=\{[r^2],[\exp]\}$ (quadratic from CFS peripherals,
exponential from a non-peripheral periodic Morse geodesic), and whether the
spectrum is blind to peripheral-tree structure inside the exponential regime.

**Result (proved).** The universal two-point claim is **false**. The graph
$\Gamma=C_5$ satisfies all Standing Assumptions, is non-CFS, has global
divergence $\sim\exp$, yet
$$\mathrm{Spec}(G_{C_5})=\{[\exp]\},$$
a singleton. In particular $[r^2]$ is absent, the CFS peripheral collection is
empty so the "realized in peripherals" clause is vacuous, and the spectrum
already distinguishes hyperbolic members from peripheral-bearing members — it
is not blind inside the exponential regime. The finer question of whether it
refines visual-tree bisimilarity among non-hyperbolic members is left open and
is not needed for the disproof.

### 1. The counterexample graph

Let $\Gamma=C_5$, the 5-cycle. We verify each Standing Assumption by hand
(machine-checked in `output/artifacts/c5_check.py`):

- *Connected, 5 vertices, planar:* evident; a cycle embeds in the plane.
- *Triangle-free:* $C_5$ has no $K_3$ subgraph; max clique size 2.
- *No separating vertex:* deleting any vertex leaves $P_4$, connected.
- *No separating edge:* deleting any edge leaves $P_5$, connected.
- *Non-CFS:* use the Dani–Thomas criterion. For triangle-free $\Gamma$,
  $\Gamma$ is CFS iff the square-graph $\square(\Gamma)$ (vertices = induced
  4-cycles, edges = pairs sharing a diagonal, i.e. two nonadjacent vertices of
  $\Gamma$) has a connected component whose support (union of vertices
  contained in its squares) is all of $V(\Gamma)$. Any 4 vertices of $C_5$
  induce $P_4$ (3 edges), never $C_4$; hence there are **zero** induced
  4-cycles, $\square(C_5)=\varnothing$, support $=\varnothing\ne V$. So $C_5$
  is non-CFS (vacuously square-free).

Thus $C_5$ is an admitted non-CFS planar graph, and the target's universal
claim applies to it.

### 2. $G_{C_5}$ is (non-elementary) hyperbolic with empty peripherals

By Moussong's hyperbolicity criterion for right-angled Coxeter groups, for
triangle-free $\Gamma$, $G_\Gamma$ is Gromov-hyperbolic iff $\Gamma$ has no
induced 4-cycle. Since $C_5$ is square-free, $G_{C_5}$ is hyperbolic
(Moussong 1988). Equivalently, in Nguyen–Tran's relative-hyperbolicity
picture the CFS peripheral collection is empty, and relative hyperbolicity
over $\varnothing$ is ordinary hyperbolicity.

$G_{C_5}$ is infinite, and one-ended (for RACGs, $\Gamma$ connected with no
separating vertex/complete subgraph gives one-endedness; concretely $G_{C_5}$
is virtually a closed-surface group — see §3 — hence one-ended and not
virtually cyclic). So it is non-elementary hyperbolic; its global divergence
is $\sim\exp$ (Olshanskii–Osin–Sapir), i.e. it genuinely lies in the
exponential regime of the target's premise.

### 3. $G_{C_5}$ is quasi-isometric to $\mathbf{H}^2$

Let $n=5$ and consider abelianization $G_{C_5}\to(\mathbb Z/2)^5$,
$s_i\mapsto e_i$. Its kernel $K_0$ (index $32$) is torsion-free: torsion in a
RACG lies in conjugates of finite special subgroups (cliques), and the map is
injective on each clique subgroup (vertices $\mathbb Z/2$, edges
$(\mathbb Z/2)^2$). $K_0$ acts freely and cocompactly on the CAT(0) Davis
complex $\Sigma$ (finite index in a cocompact action), so $K_0=\pi_1$ of a
compact aspherical 2-complex.

The nerve of $(G_{C_5},\{s_i\})$ is $C_5$, a triangulation of $S^1$; by Davis's
manifold criterion $\Sigma$ is a 2-manifold, so the compact quotient
$\Sigma/K_0$ is a closed aspherical 2-manifold, i.e. a closed surface $S$.
Its orbifold Euler characteristic is
$$\chi^{\mathrm{orb}}(G_{C_5}) = 1-\frac{5}{2}+\frac{5}{4} = -\tfrac14$$
(empty set, 5 vertices, 5 edges), so
$\chi(K_0)=32\cdot(-1/4)=-8=2-2g$, i.e. $g=5$. Hence $K_0\cong\pi_1(S_5)$,
a hyperbolic surface group acting geometrically on $\mathbf{H}^2$.
By Milnor–Schwarz, $K_0$, hence $G_{C_5}$ (finite index over $K_0$), is
quasi-isometric to $\mathbf{H}^2$.

### 4. Spectrum of $\mathbf{H}^2$ is the singleton $\{[\exp]\}$

Recall Gersten asymptotic equivalence and Tran's lower divergence: for a
bi-infinite geodesic $\alpha$,
$\rho_\alpha(r,t)$ = infimum of lengths of paths from $\alpha(t-r)$ to
$\alpha(t+r)$ avoiding $B(\alpha(t),r)$,
$\mathrm{ldiv}_\alpha(r)=\inf_t\rho_\alpha(r,t)$; $\mathrm{Spec}$ collects
$\asymp$-classes over Morse $\alpha$ (all geodesics are Morse in hyperbolic
spaces). All $a^r$, $a>1$, are one $\asymp$-class $[\exp]$.

In $\mathbf{H}^2$ all bi-infinite geodesics are isometric (homogeneity), so it
suffices to compute one. Fix $\alpha$, $m=\alpha(t)$, $x=\alpha(t-r)$,
$y=\alpha(t+r)$ (antipodal at distance $r$ from $m$). In polar coordinates
$ds^2=d\rho^2+\sinh^2\!\rho\,d\theta^2$, any curve
$\sigma(s)=(\rho(s),\theta(s))$ with $\rho\ge r$ from $x$ ($\theta=0$) to $y$
($\theta=\pi$) has
$$L(\sigma)=\int\!\sqrt{\rho'^2+\sinh^2\!\rho\,\theta'^2}
  \ge \int \sinh\!\rho\,|\theta'|
  \ge \sinh r\cdot\pi,$$
since total angular variation is $\ge\pi$. The circle arc
$\rho\equiv r$, $\theta\in[0,\pi]$ attains $\pi\sinh r$. Hence
$\rho_\alpha(r,t)=\pi\sinh r=\tfrac{\pi}{2}(e^r-e^{-r})$ for every $t$, so
$$\mathrm{ldiv}_\alpha(r)=\pi\sinh r \asymp e^r.$$
Every geodesic gives $[\exp]$; Morse boundary is nonempty; thus
$\mathrm{Spec}(\mathbf{H}^2)=\{[\exp]\}$.

### 5. Transfer and conclusion

Tran's theorem: the divergence spectrum (set of $\asymp$-classes) is a
quasi-isometry invariant. Since $G_{C_5}$ is quasi-isometric to
$\mathbf{H}^2$,
$$\mathrm{Spec}(G_{C_5})=\mathrm{Spec}(\mathbf{H}^2)=\{[\exp]\}.$$
Consequences:

1. $[\exp]$ **is** realized (e.g. by the axis of any infinite-order element
   of $K_0$ — a periodic, hence Morse, geodesic); the exponential clause
   holds.
2. $[r^2]$ **is absent**: no Morse geodesic has quadratic lower divergence.
   The clause "$[r^2]$ realized by Morse geodesics in CFS peripherals" fails
   — indeed there are no CFS peripherals at all.
3. Hence $\mathrm{Spec}(G_{C_5})=\{[\exp]\}\ne\{[r^2],[\exp]\}$: the universal
   two-point claim is **disproved**.
4. Blindness is refuted at the coarse level: the spectrum already separates
   hyperbolic members (singleton $\{[\exp]\}$) from members carrying genuine
   CFS peripherals. Whether it further refines visual-tree bisimilarity among
   peripheral-bearing graphs remains open.

### References (cited as black boxes; proofs not reproduced)

- Moussong 1988: RACG hyperbolicity $\iff$ no induced $C_4$ (triangle-free case).
- Dani–Thomas: CFS characterization via square-graph support.
- Nguyen–Tran: relative hyperbolicity over CFS subgroups under Standing Assumptions.
- Olshanskii–Osin–Sapir: hyperbolic groups have $\sim\exp$ divergence.
- Tran: lower-divergence spectrum and its quasi-isometry invariance.
- Davis: manifold criterion; RACG torsion and Euler characteristic.
- Bridson–Haefliger: thin-triangle/H$^2$ geometry (polar computation above is direct).

### Limitations and scope

- Disproof is existential via $C_5$; it does not compute spectra of
  peripheral-bearing planar graphs nor settle tree-bisimilarity refinement.
- Quasi-isometry invariance of Tran's spectrum, Moussong's criterion, and the
  Dani–Thomas CFS criterion are cited, not re-proved.
- The genus-5 identification is a bonus; only quasi-isometry to
  $\mathbf{H}^2$ is load-bearing.
