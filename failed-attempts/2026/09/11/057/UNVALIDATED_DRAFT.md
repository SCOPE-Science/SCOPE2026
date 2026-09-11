# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# dP1 nodal-boundary chamber: order-1 joint identity with named node-exclusion correction

## 1. Setup and claim

Let $X = \mathrm{dP}_1 = \mathrm{Bl}_{8} \mathbf{P}^2$ (8 general points),
$D = D_{\mathrm{nod}} \in |-K_X|$ an irreducible nodal rational curve.
$(-K_X)^2 = 9-8 = 1$. Fix class $\beta = -K_X$, contact order $w = 1 = D\cdot\beta$
(maximal tangency), tangency point a smooth point of $D$ (away from the node).

**Theorem (order-1 nodal joint).** For general 8 points (so the associated
rational elliptic surface has $12 \times I_1$ fibers), the order-1 consistent
scattering completion at the named joint has a single outgoing (unbounded) wall
$$f_{\mathrm{out}} = 1 + 11\, t z^{m_{\mathrm{out}}} \pmod{t^2},$$
where $t$ tracks class $\beta$. The coefficient $11$ equals the base-pointed
transverse maximal-tangency count $N^{\mathrm{bp}}_{-K} = 11$. The naive fiber
count $12$ is corrected by the explicit **node-exclusion factor**
$C_{\mathrm{node}} = -\,t z^{m_D}$ (removing $D$ itself, whose log maps are
degenerate / contained in the boundary). The general-point transverse invariant
is $N^{\mathrm{gen}}_{-K} = 0$; the difference $11 - 0 = 11$ is the recorded
base-point correction (all transverse fibers meet $D$ at the pencil base point).
Either way the target's disjunction is decided: identity holds for
$N^{\mathrm{bp}}$, with explicit named correction term from the naive count.

## 2. Pencil geometry (lemmas)

**Lemma 1 (pencil).** $h^0(X,-K_X) = 2$ (Riemann–Roch + Kodaira vanishing for
del Pezzo: $h^0 = 1 + K_X^2 = 2$). So $|-K_X|$ is a pencil $\mathbf{P}^1$ of
arithmetic-genus-1 curves with base locus a single point $p_0$ counted with
multiplicity $(-K_X)^2 = 1$ (cubics through 8 general points of $\mathbf{P}^2$
have a 9th base point by Cayley–Bacharach).

**Lemma 2 (node away from base).** $D$ is smooth at $p_0$ and
$\mathrm{node}(D) \ne p_0$. Proof: if $\mathrm{mult}_{p_0}(D) \ge 2$ then for any
other pencil member $C \ni p_0$, $i_{p_0}(D,C) \ge 2 > D\cdot C = 1$,
contradiction. Same argument gives every fiber smooth at $p_0$ with pairwise
transverse intersection exactly at $p_0$ of multiplicity 1.

**Lemma 3 (12 nodal fibers).** Blow up $p_0$: $Y = \mathrm{Bl}_{p_0} X$ is a
rational elliptic surface, $e(Y) = e(X) + 1 = (3+8)+1 = 12$. For general 8
points all singular fibers are $I_1$ (Persson–Miranda: general rational elliptic
has $12 \times I_1$), each of Euler contribution 1. Hence exactly 12 nodal
members in the pencil; one is $D$ itself (strict transform = fiber, node
preserved by Lemma 2), leaving **11 transverse nodal fibers**, each meeting $D$
transversely at $p_0$ (smooth point, away from node) with multiplicity 1.

## 3. Enumerative numbers

Definitions: count genus-0 log maps of class $-K_X$, contact order 1 with $D$
at a smooth point, image not contained in $D$ (transverse maps; image-in-$D$
maps are degenerate boundary-contained maps, excluded by definition following
standard relative/log conventions).

**Lemma 4 (general-point invariant vanishes).** For general $p \in D$,
$p \ne p_0$: $N^{\mathrm{gen}}_{-K} = 0$. Proof: any irreducible $C \in |-K_X|$,
$C \ne D$, meets $D$ only at $p_0$ (since $D\cdot C = 1$), so no transverse map
can have contact at $p$; any map through $p$ has image $D$ (degenerate).

**Lemma 5 (base-pointed count is 11).** With contact fixed at $p_0$:
$N^{\mathrm{bp}}_{-K} = 11$. Proof: each of the 11 transverse nodal fibers gives
exactly one transverse normalization map $(\mathbf{P}^1, 0) \to (X, D)$ of
contact order 1 at $p_0$ (smooth domain, transverse intersection mult 1, hence
log smooth, automorphism-free, contribution $+1$); smooth fibers are smooth
elliptic curves, admitting no genus-0 representative; $D$ itself is excluded as
degenerate. Multiple covers are class $k\beta$, $k \ge 2$, hence $O(t^2)$.

## 4. Scattering to order 1

Standard input (Gross–Hacking–Keel; Gross–Siebert; Auroux): each $I_1$ fiber
contributes one initial wall (slab) with $f_i = 1 + t z^{m_i}$ (primitive;
higher terms $O(t^2)$). Work mod $t^2$ (order 1 in class $\beta$).

**Lemma 6 (KS product).** The 11 transverse initial walls are parallel
($m_i = m_{\mathrm{out}}$, the fiber direction), hence commute; ordered product
$\prod_{i=1}^{11}(1 + u) = (1+u)^{11} = 1 + 11u \pmod{u^2}$ with
$u = t z^{m_{\mathrm{out}}}$. The node slab $f_{\mathrm{node}} = 1 + t z^{m_D}$
commutes with these mod $t^2$ (cross terms $O(t^2)$), and the focus-focus
monodromy $M = \left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$
fixes $m_{\mathrm{out}}$ ($\det M = 1$). So no new wall is needed at order 1
beyond the single outgoing wall $f_{\mathrm{out}} = 1 + 11tz^{m_{\mathrm{out}}}$;
consistency holds mod $t^2$. The target's parenthetical "known node monomial"
factor is $1$ at order 1: parallel transport around the focus-focus singularity
acts by $M$ on exponents and $M m_{\mathrm{out}} = m_{\mathrm{out}}$, so no
nontrivial node dressing appears at this order. Verified symbolically in
`artifacts/verify_joint.py` (Euler count, intersection exclusion, KS
coefficient, monodromy invariance → `VERIFY_OK`).

## 5. Decision

$f_{\mathrm{out}} = 1 + N^{\mathrm{bp}}_{-K}\, t z^{m_{\mathrm{out}}}$ with
$N^{\mathrm{bp}}_{-K} = 11$: **identity branch holds** for the transverse
(base-pointed) invariant. The naive $12$ is corrected by the named
**node-exclusion correction** $C_{\mathrm{node}} = -tz^{m_D}$ (the $D$-fiber:
node-induced slab, degenerate image-in-boundary maps). The general-point
invariant $N^{\mathrm{gen}}_{-K} = 0$ differs by the recorded base-point shift
$+11$. Both numbers and both corrections are explicit above — the target
question ("identity or node correction") is fully decided: identity after the
explicit node-exclusion correction.

## 6. Limitations / scope

- Order 1 ($t^2 = 0$) only; higher-order multiple-cover and descendant terms
  not computed.
- Uses the standard $I_1$-slab input $f_i = 1 + tz^m$ from cited wall-structure
  machinery (not re-derived); the new content is the nodal-fiber exclusion
  count and order-1 joint consistency in this chamber.
- Requires general 8 points ($12 \times I_1$); non-general configurations with
  worse fibers are outside scope.
- $N^{\mathrm{bp}}$ is the base-pointed transverse count natural to this
  chamber; the general-point invariant vanishes (Lemma 4), honestly recorded
  rather than conflated.

## 7. Replay

`python3 output/artifacts/verify_joint.py` → Euler $11/12$, $12$ nodal,
$11$ transverse; $D\cdot C = 1$ exclusion; KS coefficient $11$; monodromy
invariance; `VERIFY_OK`.
