# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Borel 3-edge-coloring collapse for the odometer fiber-ladder H0 (lane-509)

## 1. Object and claim

Let $X=2^{\mathbb N}$ with product topology, $T:X\to X$ the dyadic (binary)
odometer: add one with carry; $T(1^\infty)=0^\infty$. Let
$k(x)=(\min\{n:x(n)=1\})\bmod 3$ for $x\ne 0^\infty$, $k(0^\infty)=0$.
Let $Y=X\times\{0,1,2\}\times\{0,1\}$ and let $H_0$ be the graph with edges

- **fiber edges:** $((x,i,0),(x,i+k(x)+t,1))$, indices mod 3, $t\in\{0,1\}$;
- **link edges:** $((x,i,0),(T(x),i,1))$ for all $x,i$.

**Theorem (target collapse (i)).** $H_0$ is a Borel, 3-regular, side-bipartite,
hyperfinite graph whose fibers are 6-cycles, and it admits an explicit Borel
proper 3-edge-coloring
$$c(e)=\begin{cases}0 & e\text{ link},\\ 2 & e\text{ fiber of type }t=0,\\
1 & e\text{ fiber of type }t=1,\end{cases}$$
together with an explicit toast-scaffold layer/diameter log (Section 5) on
which $c$ restricts properly with trivial (identity) interface maps.
Hence alternative (ii) (Borel-versus-Baire gap) does not occur; a
Baire-measurable 3-edge-coloring exists a fortiori by restriction.

## 2. Basic verification

**Lemma 1 (Borel data).** $T$ is a homeomorphism of $X$ (hence a Borel
isomorphism), $k$ is Borel, and the edge relation of $H_0$ is Borel.

*Proof.* Bit $m$ of $T(x)$ is $x(m)\oplus\bigwedge_{n<m}x(n)$ (with the
all-ones point mapping to all-zeros), a continuous function of $x(0..m)$;
preimages of cylinders are clopen. Inverse = subtract-one, same form.
For $k$: $\{k=j\}=\bigcup_{n\equiv j(3)}(\{x(n)=1\}\cap\bigcap_{m<n}
\{x(m)=0\})$, plus $\{0^\infty\}$ when $j=0$; countable unions of clopen
sets plus a closed singleton, hence Borel. Edge relation: for each
$i,t$ the map $(x,i,0)\mapsto(x,i+k(x)+t,1)$ is Borel (finite Borel
case distinction on $k$); similarly $(x,i,0)\mapsto(T(x),i,1)$. The edge
set is a finite union of Borel graphs. ∎

**Lemma 2 ($T$ fixed-point-free).** $T(x)\ne x$ for all $x$.

*Proof.* If $x\ne1^\infty$, let $n$ be the first $0$; $T$ flips bit $n$
$0\to1$. If $x=1^\infty$, $T(x)=0^\infty\ne x$. ∎

**Lemma 3 (regularity, bipartiteness, simplicity, fibers).**
$H_0$ is simple, 3-regular, bipartite by side $\{s=0\}$ vs $\{s=1\}$,
and each fiber $\{x\}\times\{0,1,2\}\times\{0,1\}$ induces a 6-cycle.

*Proof.* All edges join side 0 to side 1. Fiber edges have equal
$X$-coordinates, link edges distinct $X$-coordinates (Lemma 2), so the
two types never coincide. For fixed $x,i$, the two fiber neighbours have
tracks $i+k(x)$, $i+k(x)+1$, distinct mod 3; the link neighbour has
$X$-coordinate $T(x)\ne x$. Hence $\deg(x,i,0)=3$ with distinct
neighbours. At $(x,j,1)$, fiber preimages are $(x,j-k(x),0)$ ($t=0$) and
$(x,j-k(x)-1,0)$ ($t=1$), distinct; the link preimage is
$(T^{-1}(x),j,0)\ne$ both. So $\deg=3$. No loops or multiedges by the
unique recovery formulas above. Fiber: with $A_i=(i,0)$, $B_j=(j,1)$,
$A_i\sim B_{i+k},B_{i+k+1}$; the closed walk
$A_0B_{k+1}A_1B_{k+2}A_2B_kA_0$ visits all 6 vertices exactly once and
every vertex has fiber-degree 2. Hence a $C_6$. ∎

**Lemma 4 (hyperfiniteness).** The connectivity relation $E_{H_0}$ is
hyperfinite.

*Proof.* Let $\pi:Y\to X$ be projection and $E_T$ the odometer orbit
equivalence. Every $H_0$-edge projects to $\{x,x\}$ or $\{x,T(x)\}$, so
$E_{H_0}\subseteq\pi^{-1}(E_T)$. $E_T$ is the orbit equivalence of a Borel
$\mathbb Z$-action, hence hyperfinite (Connes–Feldman–Weiss). Pullback
along the 6-to-1 Borel map $\pi$ preserves hyperfiniteness: if
$E_T=\bigcup_m E_m$ with $E_m$ finite Borel, then $\pi^{-1}(E_m)$ are
finite (class size $6|E_m\text{-class}|$), Borel, increasing, with union
$\pi^{-1}(E_T)$. A Borel subequivalence of a hyperfinite equivalence is
hyperfinite (Dougherty–Jackson–Kechris). Hence $E_{H_0}$ is hyperfinite. ∎

*Remark (the wrap point).* $T(1^\infty)=0^\infty$ joins two distinct tail
classes; thus $E_T$ strictly exceeds tail equivalence. The CFW route
above handles this with no ad hoc merging; cf. WORKLOG stress test C.

## 3. The Borel 3-edge-coloring (collapse rule)

For a fiber edge $e=((x,i,0),(x,j,1))$ put $t(e)=j-i-k(x)\bmod3\in\{0,1\}$.
A link edge is recognised by differing $X$-coordinates (Lemma 2 makes
this discriminator exact). Define $c$ as in the Theorem.

**Proposition 5.** $c$ is Borel and proper; every vertex sees palette
$\{0,1,2\}$.

*Proof.* The link/fiber discriminator is Borel (diagonal in $X\times X$
is closed). On fiber edges $t(e)$ is Borel (Lemma 1: $k$ Borel, tracks
clopen). Hence $c$ is Borel. At $(x,i,0)$: fiber edges have $t=0,1$
(colors 2,1), link has 0. At $(x,j,1)$: the two fiber incidences have
$t=j-(j-k)-k=0$ and $t=j-(j-k-1)-k=1$ (colors 2,1), link has 0. All three
distinct. ∎

*Why aperiodicity is no obstruction.* A constant-phase rule would indeed
be defeated by $k(x)$ varying. The rule above is $k$-relative: it colors
by the offset $t=j-i-k(x)$, i.e. it tracks the pattern. Since $k$ is
Borel, tracking it costs nothing. The aperiodic modulation changes which
physical track-pair gets color 1 vs 2, but the vertex palette is
$\{1,2\}$ on fibers for every $k$ (checked for $k=0,1,2$ in replay A).

Since $H_0$ is 3-regular, $\chi'(H_0)\ge3$; Proposition 5 gives
$\chi'_{\text{Borel}}(H_0)=3$ exactly.

## 4. Finite replay (machine check)

`output/artifacts/verify_collapse.py` replays, printing `ALL VERIFY_OK`:
- **A.** Pure fiber combinatorics for each $k\in\{0,1,2\}$: $C_6$ walk,
  fiber palettes $\{1,2\}$, $t$-recovery $\{0,1\}$ at every $B$-vertex.
- **B.** Truncated-odometer model $M=64$: simplicity, 3-regularity (384
  vertices, 576 edges), side-bipartiteness, fiber $C_6$'s, global
  properness of $c$ (palette $\{0,1,2\}$ everywhere), color census
  192/192/192, edge-type discriminator exactness. Stress-tested at
  $M=128,256$ (regular + proper), $k$-partition census, $T$ bijectivity
  and tail-class tower accounting (see WORKLOG).
- **C.** Toast-tower log table plus two-phase covering check.

## 5. Toast-scaffold layer/diameter log

Use tail blocks $B_{m}(c)=\{x:x\!\upharpoonright\![m,\infty)=c\}\times
\{0,1,2\}\times\{0,1\}$ ($2^{m}$ $X$-points, $6\cdot2^{m}$ vertices each),
which are $H_0$-connected ladder segments. At scale $m\ge0$ put
$H_m=2^{m+3}$, $r_m=m+1$, shrunken $T$-length $L_m=H_m-2r_m$ (drop $r_m$
levels at each end). Tiles = shrunken blocks $\times$ full 6-fiber.
Two phases: standard tower and tower shifted by $H_m/2$; every
$x$ is at orbit-distance $\ge r_m$ from the cuts in at least one phase
since $\max(d_A,d_B)\ge H_m/4=2^{m+1}\ge m+1=r_m$.

| $m$ | $H_m$ | $r_m$ | $T$-len $L_m$ | verts/tile | diam $\le2L_m+2$ | sep $\ge2r_m$ |
|---|---|---|---|---|---|---|
| 0 | 8 | 1 | 6 | 36 | 14 | 2 |
| 1 | 16 | 2 | 12 | 72 | 26 | 4 |
| 2 | 32 | 3 | 26 | 156 | 54 | 6 |
| 3 | 64 | 4 | 56 | 336 | 114 | 8 |
| 4 | 128 | 5 | 118 | 708 | 238 | 10 |

*Diameter.* Each $H_0$-edge advances the $T$-orbit by $\le1$ (fiber edges
$0$, link edges $1$). Walk-cost lemma: from $(x,i,s)$ move to side 0
($\le1$ step); advance each $T$-step by link + an arbitrary fiber step
back to side 0 ($2$ steps, track uncontrolled); on arrival correct within
the terminal $C_6$ ($\le3$ steps, the $C_6$ diameter). For orbit-distance
$d\le L_m-1$ this gives $d_{H_0}\le1+2d+3\le2L_m+2$.
*Separation.* By the same orbit-displacement fact,
$d_{H_0}\ge d_T$ (orbit distance): any length-$\ell$ path moves $\le\ell$
along the orbit. Distinct same-layer shrunken tiles are $\ge2r_m$ orbit
steps apart (the $r_m$ margins on both sides of each cut), so
$d_{H_0}\ge2r_m$ across tiles.
*Interface maps and toast status.* The global rule $c$ restricts properly
to every tile; interfaces are consistent by identity — no recoloring is
needed. The two-phase tower family above is a toast scaffold (per-layer
separation + covering + diameter bounds). It upgrades to a genuine Borel
toast by standard thinning (discard/merge boundary-overlapping pieces
across scales; cf. Gao–Jackson, every hyperfinite Borel graph admits a
Borel toast with arbitrarily large separation): since $c$ is globally
consistent, every thinned piece inherits a proper coloring with identity
interfaces. This is the collapse certificate: a toast-compatible Borel
coloring with complete layer log.

## 6. Decision

Collapse side (i) verifies completely: Borel data (Lemmas 1–4),
properness (Proposition 5), toast log (Section 5 + replay C). Gap side
(ii) is therefore excluded as an exclusive alternative; a
Baire-measurable 3-edge-coloring exists trivially by restricting $c$ to
any comeager invariant set. Exact value: $\chi'_{\text{Borel}}(H_0)=3$.

## 7. Originality and limits

Admission-verified sources (Marks 1304.3830 vertex games; Brandt et al
2111.03683 general completeness; Conley et al 1611.02204 acyclic spectra;
Bernshteyn 2004.04905 LLL transfer; Bowen–Weilacher 2112.10222
$\Delta+1$ Baire bound; Csóka et al 1408.1973 measurable $d+1$) decide no
fixed fiber-ladder edge cell and publish no $(H_0,c,\text{toast})$ datum.
The cyclic $C_6$ fibers place $H_0$ outside acyclic classifications.
*Limits.* The collapse uses the very rigid aligned-link structure of
$H_0$; it does not decide edge-colorings of fiber-ladders with twisted
links, higher-degree fibers, or non-amenable base actions. The toast
scaffold is a verification layer over a globally consistent rule, not a
general toast-construction method. Computed replay is on truncated
models plus exact fiber combinatorics; the infinite-diameter and
hyperfiniteness arguments are proofs, not computations.

## 8. Replay

```
python3 output/artifacts/verify_collapse.py   # expect ALL VERIFY_OK
```

References: Kechris–Solecki–Todorčević; Marks arXiv:1304.3830;
Conley–Jackson–Marks–Seward–Tucker-Drob arXiv:1611.02204;
Bernshteyn arXiv:2004.04905; Bowen–Weilacher arXiv:2112.10222;
Csóka–Lippner–Pikhurko arXiv:1408.1973; Brandt et al arXiv:2111.03683;
Gao–Jackson toast; Connes–Feldman–Weiss; Dougherty–Jackson–Kechris.
