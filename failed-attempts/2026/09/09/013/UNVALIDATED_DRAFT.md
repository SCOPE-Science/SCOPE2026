# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# First explicit non-unimodal lattice 3-pyramid witnesses and the sharp dip bound over 2992 box-generated pyramids

## 1. Committed window and objects (fixed before any computation)

Let $Q \subset \mathbb{R}^2$ be a lattice polygon with vertices in the box
$B=[0,3]^2 \cap \mathbb{Z}^2$, translated so $\min Q = (0,0)$ coordinatewise; only
convex lattice triangles and quadrilaterals are used. Two placements differing by a
translation are identified (translation-type census); unimodular
$\mathrm{GL}(2,\mathbb{Z}) + $translation classes are logged separately for the
generation record. For apex height $h \in \{1,2,3,4\}$ put

$$P(Q,h) = \mathrm{Pyr}(Q,h) = \mathrm{conv}(Q \times \{0\},\ A),\qquad
A = (0,0,h).$$

The window is the set of $2992$ pyramids over the $192$ triangle and $556$
quadrilateral translation types (grouped into $13$ triangle and $47$ quadrilateral
unimodular classes). No external database or catalogue is imported: every base is
generated de novo from the box. Interior points of kept bases satisfy
$i(Q) \le 4$ automatically in this box (verified: the maximum attained is $i=4$).

## 2. Theorems

Write $L_P(t) = |tP \cap \mathbb{Z}^3|$ and
$\mathrm{Ehr}_P(z) = \sum_{t \ge 0} L_P(t)z^t
= \bigl(\sum_{j=0}^3 h_j^* z^j\bigr)/(1-z)^4$.

**Theorem A (first explicit non-unimodal pyramid witnesses in the window).**
Exactly $9$ of the $2992$ pyramids are non-unimodal (in the peak sense:
no index $k$ with $h_0^* \le \cdots \le h_k^* \ge \cdots \ge h_3^*$).
Up to the logged translation placements they are the pyramids over the unimodular
unit triangle (normalized area $1$, $b=3$, $i=0$), at heights $h = 2,3,4$:

| height $h$ | $h^*(P)$ | $L_P = (L_0,\dots,L_6)$ | counted as |
|---|---|---|---|
| $2$ | $(1,0,1,0)$ | $(1,4,11,24,45,76,119)$ | $3$ placements |
| $3$ | $(1,0,2,0)$ | $(1,4,12,28,55,96,154)$ | $3$ placements |
| $4$ | $(1,0,3,0)$ | $(1,4,13,32,65,116,189)$ | $3$ placements |

Shortest representative (verified by both routes below): base
$Q_\triangle = \mathrm{conv}\{(0,1),(1,0),(1,1)\}$ (unit triangle, $(b,i)=(3,0)$),
apex $(0,0,2)$,

$$P_\triangle = \mathrm{conv}\{(0,1,0),(1,0,0),(1,1,0),(0,0,2)\}.$$

Its Ehrhart values are $L = (1,4,11,24,45,76,119)$, whence
$h^* = (1,0,1,0)$, which is non-unimodal ($1 > 0 < 1$). Its lattice width is
$1$ with primitive witness direction $(-1,-1,-1)$ (value range on the four
vertices $\{0,-1,-2,-1\}$, spread $1$). Normalized volume $2$.

**Theorem B (sharp $h_1^*-h_2^*$ dip bound with extremal and gap).**
Over all $2992$ pyramids in the window,

$$\max_P \bigl(h_1^*(P) - h_2^*(P)\bigr) = 9,$$

attained uniquely (as a translation type) by the height-$1$ pyramid over the
$3 \times 3$ square

$$P_{\max} = \mathrm{conv}\{(0,0,0),(3,0,0),(3,3,0),(0,3,0),(0,0,1)\},$$

with $L = (1,17,66,166,335,591,952)$, $h^* = (1,13,4,0)$, dip $13-4 = 9$,
normalized volume $18 = 1 \cdot 18$ ($\mathrm{area}_2(Q) = 18$), base
$(b,i) = (12,4)$, lattice width $1$ with witness $(0,0,-1)$.
The runner-up dip is $7$, attained by exactly two translation types,
$Q = \mathrm{conv}\{(0,0),(3,0),(3,2),(0,2)\}$ and
$Q = \mathrm{conv}\{(0,0),(2,0),(2,3),(0,3)\}$, both at $h=1$ with
$h^* = (1,9,2,0)$ and identical $L = (1,13,48,118,235,411,658)$; hence the
extremal gap is $9 - 7 = 2$. Every positive dip ($1333$ pyramids have
$h_1^* > h_2^*$) occurs at a peak-$1$ unimodal vector, so none of them is
genuinely non-unimodal; the $9$ non-unimodal pyramids all have $h_1^*-h_2^* < 0$.

**Corollary (width-versus-unimodality interaction).** Both the maximal-dip
extremal and every genuinely non-unimodal witness have lattice width $1$:
width $1$ does not protect against the $h_1^* > h_2^*$ dip (dip $9$ at width $1$)
nor against genuine non-unimodality ($(1,0,1,0)$ etc. at width $1$).

## 3. How it is proved (dual exact routes, reproducible in seconds)

Route A (`artifacts/pyr_census.py`, stdlib only): every convex lattice
triangle/quadrilateral vertex set in $[0,3]^2$ is enumerated; translation types
are stored ($192$ tri, $556$ quad) and exact $\mathrm{GL}(2,\mathbb{Z})$-equivalence
checked pairwise for the generation log ($13$ tri, $47$ quad classes).
For each $(Q,h)$, $L_P(t)$, $t = 0,\dots,6$, is counted by exact slice-scaling:
at height $z$, $tP \cap \{z\text{-coordinate } = z\}$ is $(tz/h)\cdot Q$ shifted,
tested by exact integer halfspace inequalities with denominator $h$ cleared.
$h^*$ is solved from $L_0,\dots,L_3$ via the degree-$3$ Ehrhart inversion, and
$L_4,L_5,L_6$ plus $\sum h_j^* = h\cdot\mathrm{area}_2(Q)$ are asserted.
Nonnegativity $h_j^* \ge 0$ (Stanley) is asserted for all $2992$ cases.
Lattice width is by exhaustive primitive-direction scan inside a proved radius:
Lemma — if $M$ is a nonsingular $3 \times 3$ integer matrix of edge differences
with adjugate row-norm $r$ and $|\det M| = d$, and $W_0$ the coordinate width,
then any primitive direction attaining width $< W_0$ satisfies
$\|u\|_\infty \le \lceil r W_0 / d \rceil$
(proof: $u = M^{-T}w$ with $w = Mu \in \mathbb{Z}^3$ a nonzero vector of
$|w_j| \le W_0$; $\|M^{-T}\|_\infty = r/d$).
The scanned optimum plus its direction are logged.

Route B (`artifacts/verify.py`, independent code, stdlib only): facets are
recomputed from all vertex triples by exact integer planes; $L_P(t)$ is recounted
by box scan; $h^*$ re-derived and $L_4,L_5,L_6$ re-predicted; normalized volume
recomputed by coning the apex over a fan triangulation of the base
($\sum |\det|$, exact integers) and checked against $\sum h^*$ and
$h\cdot\mathrm{area}_2(Q)$; Pick invariants $(b,\mathrm{area}_2,i)$ recomputed;
the width lemma radius recomputed and an independent brute-force scan
(radius $\max(B_{\mathrm{lemma}},6)$) confirms the logged width, and the logged
direction is re-evaluated. Global census invariants are asserted from
`census.json`: $2992$ pyramids, dip histogram max $9$ (unique), min $-20$,
$1333$ positive dips, exactly $9$ non-peak vectors, all of shape
$(1,0,m,0)$. The extremal, runner-up, and all $9$ non-unimodal witnesses print
`VERIFY_OK` agreement of every invariant across both routes; global line prints
`GLOBAL_OK`. Run: `python3 artifacts/pyr_census.py && python3 artifacts/verify.py`.

## 4. Separation from the literature (why this is new)

Dimension $2$ is settled: Pick's theorem forces every lattice polygon to
$h^* = (1, i+b-3, i)$, hence unimodal — the lane's blocked polygon census tested
nothing. The cited priors say nothing about $3$-dimensional pyramid $h^*$:
Haase–Schicho classifies $2$D $(a,b,i)$ triples; Batyrev–Nill classifies degree-$1$
polytopes structurally; Castryck–Cools develops polygon width/size theory;
Braun–Davis–Solus/Payne treat high-dimensional ($>5$) reflexive-simplex
thresholds. None publishes a pyramid-over-polygon $h_1^* > h_2^*$ witness, a
sharp dip bound over this box window, or the exact non-unimodal vectors
$(1,0,1,0)$, $(1,0,2,0)$, $(1,0,3,0)$ on unit-triangle pyramids. Every number
above is generated de novo inside the committed box, not imported from GRDB or
Kreuzer–Skarke.

## 5. Limits and what is not claimed

Window-bound, not an infinite-family theorem: maximality of dip $9$ and
uniqueness (one translation type; two runner-up types) hold over the committed
$2992$-pyramid window only. Regular-triangulation $h^*$ was not used as a third
route; instead two independent lattice-count routes plus volume/Pick identities
agree. Nonnegativity of all $h^*$ (Stanley) is machine-verified in-window, not
re-proved. The $9$ witnesses share one unimodular base class; minimality of
volume $2$ among all non-unimodal $3$-pyramids is not claimed beyond this window.

## 6. Artifacts

- `artifacts/pyr_census.py` — de novo generation, Route-A counts, widths, `census.json`.
- `artifacts/census.json` — all $2992$ records $(Q,h,L,h^*,\mathrm{dip},w,\text{dir})$ plus extremal/runner-up.
- `artifacts/verify.py` — independent Route-B recount; `GLOBAL_OK` + per-case `VERIFY_OK`.
- `artifacts/verify_log.json` — machine log of the $11$ headline recounts.
