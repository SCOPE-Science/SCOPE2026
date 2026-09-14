# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Relative quasi-isometric rigidity for rigid JSJ pieces of planar hyperbolic right-angled Coxeter groups

## 1. Class and statement

Let $\Gamma$ be finite, connected, triangle-free, planar, with no separating
vertex or edge, no induced 4-cycle, not a cycle, and admitting a cut pair.
Write $W_\Gamma$ for the right-angled Coxeter group with nerve $\Gamma$.
Then $W_\Gamma$ is one-ended (Davis, Thm 8.7.2), hyperbolic (Moussong /
Davis Cor 12.6.3, square-free), not cocompact Fuchsian (triangle-free, so
Fuchsian iff $\Gamma$ is a cycle of length $\ge 5$; Dani–Thomas Cor A.3),
and splits over a 2-ended subgroup (Mihalik–Tschantz: splittings over
2-ended subgroups are, up to conjugacy and finite index, over special
subgroups $\langle a,b\rangle$ of cut pairs $\{a,b\}$). Its Bowditch JSJ
tree $T_\Gamma$ over 2-ended subgroups is nontrivial. Call this class
$\mathcal C$.

**Visual JSJ (Dani–Thomas, Thm 3.37).** $W$-orbits of vertices/edges of
$T_\Gamma$ correspond to explicit vertex subsets of $\Gamma$:
V1 $\approx$-pairs are cut pairs with $\ge 3$ complementary components
(Cor 3.5, with the single-vertex-component refinement giving valence
$2(k-1)$); V1 $\sim$-pairs and V2 infinite $\sim$-classes are sets $A$
satisfying (A1)–(A3) of Prop 3.10, distinguished by whether
$\langle A\rangle$ is 2-ended (stabiliser a cut-pair dihedral, possibly
with the unique common neighbour $c$) or infinite non-2-ended (maximal
hanging Fuchsian stabiliser $\langle A\rangle$, Prop 3.24); V3 stars are
sets $B$ of essential vertices satisfying (B1)–(B3) of Prop 3.25
($|B|\ge 4$, maximal non-separation), with rigid stabiliser
$\langle B\rangle$ (Prop 3.35). Every edge stabiliser is 2-ended, the
intersection of its endpoint stabilisers.

**Theorem (relative rigidity, TARGET).** Let $W_\Gamma,W_\Lambda\in
\mathcal C$ with type-preservingly isomorphic Bowditch JSJ trees.
Regard each rigid vertex stabiliser together with the family of incident
2-ended edge stabilisers (conjugates of visual cut-pair dihedrals) as a
pair $(R,\mathcal P)$. Then:

- (Necessity) Every quasi-isometry $W_\Gamma\to W_\Lambda$ induces the
  type-preserving tree isomorphism and restricts (up to bounded distance
  and group translation) to a relative quasi-isometry of each matched
  rigid pair. In particular, matched rigid pairs of quasi-isometric
  groups are relatively quasi-isometric.
- (Sufficiency) If, under the tree matching, every matched rigid pair
  is relatively quasi-isometric (and matched hanging pairs are
  relatively quasi-isometric, which is the flexible Behrstock–Neumann /
  Malone case), then $W_\Gamma$ and $W_\Lambda$ are quasi-isometric.

## 2. Proof

*Necessity.* A quasi-isometry of 1-ended hyperbolic groups induces a
homeomorphism of visual boundaries, hence an equality of coloured JSJ
trees (Bowditch). By Papasoglu, quasi-isometries preserve splittings
over 2-ended subgroups and send rigid (non-hanging, non-elementary)
vertex stabilisers to within bounded Hausdorff distance of rigid vertex
stabilisers, bijecting the incident universally elliptic 2-ended
peripheral cosets. Via the visual identification, those peripherals are
exactly the $W$-conjugates of the cut-pair dihedral special subgroups
incident to the rigid vertex (Thm 3.37; Lemma 3.7; Props 3.24, 3.35).
Adjusting by group elements gives, on each rigid vertex space, a
quasi-isometry coarsely preserving the peripheral family: a relative
quasi-isometry of rigid pairs.

*Sufficiency.* Fix the type-preserving isomorphism of JSJ trees. Build
a global quasi-isometry as a tree of quasi-isometries
(Behrstock–Neumann fattened-tree / Malone / Cashen–Martin machine):
cylinder (2-ended) pieces are standard dihedral models, matched by the
Mihalik–Tschantz uniqueness of the cut pair per splitting; hanging MHF
pieces are flexible (Behrstock–Neumann/Malone: peripheral-respecting
quasi-isometries exist once the tree matching fixes the peripheral
pattern); rigid pieces are relatively quasi-isometric by hypothesis.
Edge spaces are uniformly quasi-isometrically embedded lines matched by
the tree isomorphism, so the piece maps glue to a quasi-isometry of
Davis complexes, hence of the groups.

## 3. Content: planar wheels with stars (original verification)

Both of the following graphs satisfy every hypothesis of the target
literally (machine-verified, `artifacts/hypothesis_check.json`):
$\Gamma=$ 2-subdivided wheel $W_5$ (26 vertices, 30 edges) and
$\Lambda=$ 2-subdivided wheel $W_6$ (31 vertices, 36 edges): planar,
triangle-free, no induced $C_4$, connected, no cut vertex/edge, not a
cycle, with cut pairs (30 resp 36; every essential cut pair has exactly
2 complementary components, so there are no $\approx$-pairs).

Their JSJ shapes (computed cut-pair census + (B1) verification):
$B_\Gamma$ = 6 essential vertices and $B_\Lambda$ = 7 satisfy (B1) and
are maximal, hence give V3 rigid stars with stabilisers
$R_6=(\mathbb Z/2)^{*6}$ (virtually $F_5$) and
$R_7=(\mathbb Z/2)^{*7}$ (virtually $F_6$); essential cut pairs inside
$B$ are 10 (5 spoke + 5 rim) resp 12 (6+6), each yielding a valence-2
$\sim$-pair; no larger essential set satisfies (A1), and the triple
$\{h,r_i,r_j\}$-type sets satisfying (A1) fail (A2) against the
subdivided-$K_4$ on $\{h,r_i,r_j,r_k\}$. So both trees have one rigid
orbit, two valence-2 pair orbits, no $\approx$-pairs — the same
type-pattern (stars present, so Dani–Thomas Thm 1.4 does not apply and
Appendix B's non-planar incompleteness is the correct background, not a
contradiction). The theorem therefore says: global QI of these two
wheel groups is equivalent (modulo flexible hangings) to relative QI
of $(R_6,10\text{ dihedrals})$ vs $(R_7,12\text{ dihedrals})$.

*Computed evidence.* Index-2 free subgroups $F_5,F_6$ with line patterns
$L_5=\{y_i\}\cup\{y_i^{-1}y_j:C_5\text{ edges}\}$,
$L_6=\{y_i\}\cup\{y_i^{-1}y_j:C_6\text{ edges}\}$; Whitehead graphs built
and min edge-cuts computed: the method reproduces Appendix B
($K_4$-pattern 3, $K_5$-pattern 4) and gives min-cut 3 for both wheel
patterns (10 cuts isolating a vertex for $W_5$, 12 for $W_6$). Hence the
crude Whitehead min-cut size does **not** separate the wheel rigid
pairs; the theorem is stated as an equivalence, not a decision
procedure.

## 4. Limitations and attribution

- The engines (Bowditch QI-invariance; Papasoglu splitting/rigid
  preservation; Dani–Thomas visual JSJ; Behrstock–Neumann/Malone
  hanging flexibility; Cashen–Martin gluing) are cited, not reproved;
  the contribution is their assembly into the planar-class relative
  rigidity statement plus the verified wheel-pair analysis.
- Sufficiency hypothesises relative QI for hanging pairs alongside
  rigid pairs; only the rigid direction is the target's emphasis.
- No claim is made that the bare (undecorated) JSJ tree is complete in
  the planar class, nor that the wheel rigid pairs are (non-)relatively
  QI: finer decomposition-space invariants are left open.
- The V2-absence and V3-uniqueness for the wheels are argued from the
  computed (A1)/(B1) census and Dani–Thomas lemmata, not from a
  certified full implementation of (A2)/(A3)/(B2) maximality over all
  subsets.
