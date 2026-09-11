# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Stall profile for component-revealing left-edge vertical-interface exploration of square box crossing

## 1. Setting (self-contained)

Work on the discrete proxy used by the admitted lane: the square is the
$16\times16$ grid of cells

$$Q_{16}=\{(r,c):0\le r,c\le 15\},$$

each cell independently colored red ($1$) with probability $p$ and blue ($0$)
with probability $1-p$. Let $H$ be the red left-right crossing event (a
$4$-adjacent red path joining column $0$ to column $15$). At the critical value
$p=1/2$ both colors are symmetric. This product model is the standard
fixed-$n$ discretization proxy for the intensity-$1$ Voronoi coloring at the
audit patch $n=16$; the target's audit-scale constants evaluate to

$$\delta_{16}:=0.20\cdot 16^{-1/4}=0.10,\qquad w_{16}:=0.70\cdot 16^{-1/4}=0.35,$$

against the trivial caps $1$ (revealment) and $0.5$ (window width on
$[0.25,0.75]$).

## 2. Algorithm class (canonical formalization of the named exploration)

The target bills a "vertically-started interface exploration" but never fixes
its code. We formalize the canonical representative $\mathcal A$:

- draw a start row $U$ uniformly from $\{0,\dots,15\}$, independently of the
  coloring;
- let $s=(U,0)$ be the seed cell and $\sigma\in\{0,1\}$ its color;
- reveal the full $4$-connected monochrome component $C(s,\sigma)$ of $s$ in
  color $\sigma$, together with its $4$-neighbour boundary layer $\partial C$
  (the non-$\sigma$ cells adjacent to $C$), and nothing else.

This determines the crossing status locally at the seed interface, mirrors the
billed "component-revealing interface trace", and is the representative any
auditor would code from the topic text. Its revealment of cell $v$ is

$$\delta_v := \mathbb P[\mathcal A\text{ queries }v],$$

the probability over both the coloring and the random start $U$.

## 3. Result (exact stall lemma)

**Theorem.** At $p=1/2$, for the midpoint left-edge cell $v=(8,0)$,

$$\delta_v \ge \frac{765}{4096} \approx 0.18677 > \frac{1}{10} = \delta_{16},$$

so the billed revealment ledger $\max_v\delta_v\le 0.10$ is violated with
exact margin

$$\frac{765}{4096}-\frac{1}{10}=\frac{1777}{20480}\approx 0.0868.$$

In particular no component-revealing exploration of this form can satisfy the
target's $0.20\,n^{-1/4}$ ledger at the audit scale $n=16$.

## 4. Proof

Fix $p=1/2$ and the cell $v=(8,0)$. Condition on the start row $U=u$. For the
algorithm to query $v$ it suffices that the entire column-$0$ segment between
rows $u$ and $8$ be monochrome: then $v$ lies in the seed's monochrome
component (if the segment matches the seed color) or is its boundary (it is
adjacent to it either way). Precisely, let $L=|u-8|+1$ be the segment length
(including both endpoints). The event

$$E_u=\{\text{cells }(r,0),\,r\text{ between }u\text{ and }8,\text{ are all red}\}\cup\{\text{all blue}\}$$

forces $v\in C\cup\partial C$, hence forces a query of $v$. Since cells are
independent with $p=1/2$,

$$\mathbb P[E_u\mid U=u]=2\cdot(1/2)^L=2^{1-L}.$$

Averaging over the uniform start,

$$\delta_v \ge \frac{1}{16}\sum_{u=0}^{15} 2^{-|u-8|}.$$

The sum is exact rational arithmetic:

$$\sum_{u=0}^{15}2^{-|u-8|}=1+2\sum_{k=1}^{7}2^{-k}+2^{-8}
=1+2\left(1-2^{-7}\right)+\frac{1}{256}=\frac{765}{256},$$

so

$$\delta_v \ge \frac{765}{256\cdot 16}=\frac{765}{4096}\approx 0.18677.$$

Since $765/4096 - 1/10 = (7650-4096)/40960 = 1777/20480 > 0$, the $0.10$ cap is
exceeded. The computation is replayed from scratch by
`output/artifacts/verify_stall.py` (exact `Fraction` arithmetic, prints
`VERIFY_OK`). ∎

## 5. Scope, limits, and what is NOT claimed

- The lemma is proved for the canonical component-revealing formalization
  $\mathcal A$ on the $16\times 16$ independent-bit proxy at $p=1/2$, not for
  the continuum Voronoi model directly and not for every conceivable
  exploration code: a smarter exploration that avoids revealing full monochrome
  components could have lower revealment. The target text never pins the code,
  so this is a stall profile for the natural reading, not a full disproof of
  the underspecified continuum conjunction.
- The complementary Monte-Carlo ledger (`output/artifacts/probe_n16.py`,
  seed $1046$, $2000$ trials per $p$) shows the same stall is worse
  off-critical (max revealment $\approx 0.76$ at $p=0.25,0.75$ and
  $\approx 0.41$ at $p=0.5$) and that the window half of the target is loose
  but true; these numbers are reported as computed evidence, not proved bounds.
- No claim is made about the true Voronoi one-arm exponent, SLE limits, or any
  preset fallback (none exists in this lane).

## 6. Novelty and value

No tabulated percolation source records this exact per-cell stall number
$765/4096$ for the left-edge interface exploration at $n=16$; the admitted
priors (Ahlberg et al.\ qualitative window, Tassion RSW non-degeneracy,
Duminil-Copin OSSS framework) contain no such finite-patch ledger. The lemma
redirects the threshold program concretely: any future proof of an explicit
Voronoi revealment ledger must use a non-component-revealing exploration or a
corrected exponent/constant, and $765/4096$ vs $1/10$ is the citable
finite-scale obstruction the canonical route must beat.
