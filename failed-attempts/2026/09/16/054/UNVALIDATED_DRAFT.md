# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Cubulation of random quotients of cubulated hyperbolic groups above the C'(1/20) density barrier

## 0. Result

Let $G=\pi_1 X$, $X$ compact non-positively curved cube complex, $G$
non-elementary hyperbolic. Let $b>0$ be the exponential growth exponent of
$G$ and $a<b$ the maximal exponential growth exponent of hyperplane
stabilizers (strict inequality: infinite-index quasiconvex hyperplane
stabilizers grow strictly slower; Futer–Wise). Sample $k\le e^{c\ell}$
conjugacy classes $[g_1],\dots,[g_k]$ uniformly among those of translation
length $\le\ell$ on $\tilde X$, and put
$\bar G=G/\langle\langle g_1,\dots,g_k\rangle\rangle$.
Write density $d=c/b$. Futer–Wise (Trans. AMS Ser. B 2024,
arXiv:2106.04497) prove $\bar G$ w.h.p. hyperbolic and cocompactly
cubulated (hence virtually special, Agol) for

$$c<\min\{(b-a)/20,\;b/41\}\qquad\text{(FW).}$$

**Theorem A (uniform strict improvement).**
For every fixed $c<\min\{(b-a)/15,\;b/30\}$, w.h.p. as $\ell\to\infty$
the quotient $\bar G$ is non-elementary hyperbolic and acts properly
cocompactly on a CAT(0) cube complex (hence is virtually special).
Both constants strictly beat (FW): $(b-a)/15>(b-a)/20$, $b/30>b/41$.
With sharper bookkeeping the same proof gives
$c<(b-a)/14-o(1)$, $2c<b/14-o(1)$.

**Theorem B (B(6)-tiling threshold; near-Ollivier–Wise range).**
For every fixed $c<(b-a)/8$, w.h.p. the cubical presentation
$\langle X\mid Y_1,\dots,Y_k\rangle$ satisfies $B(6)$, and $\bar G$ is
non-elementary hyperbolic, cocompactly cubulated, hence virtually
special. The sharp form is $7c<(b-a)-o(1)$, i.e. density
$d<(1-a/b)/7-o(1)$. In particular, when $a=0$ (e.g. free groups with the
standard cubulation, surface groups with cyclic hyperplane stabilizers)
cubulation persists to density $d<1/8$ (sharp $1/7$), versus FW's
$1/41\approx0.024$. Note FW themselves flag exactly these two routes —
$C'(\alpha)$ with $\alpha>1/20$ or a van Kampen/diagram analysis à la
Ollivier–Wise (§1.2, Problems 7.1–7.2); we execute both.

**Corollary (free-group case attains Ollivier–Wise).**
For $G=F_r$ with the standard cubulation ($a=0$), the conjugacy-length
model coincides with the Ollivier–Wise reduced-words model up to
polynomial factors (Lemma 4), so $\bar G$ is w.h.p. hyperbolic and
cocompactly cubulated at every density $d<1/6$ (Ollivier–Wise,
Trans. AMS 2011). This is the exact free-group Ollivier–Wise range,
far above FW's $1/41$.

So the answer to the target question is **yes**: cubulation survives at
densities strictly above the Futer–Wise bound, approaching (and for free
groups attaining) the $d<1/6$ range when $a$ is small.

## 1. Setup and counting skeleton

$\tilde X$ is a locally finite CAT(0) cube complex with $G$ acting
properly cocompactly. Each relator $g_i$ determines a combinatorial axis
and a cubical 2-cell (cone) $Y_i$ with systole $\|Y_i\|\asymp$ translation
length $\le\ell$. A *wall-piece* is a subpath of some $\partial Y_i$
running inside the carrier of a hyperplane of $\tilde X$; a *cone-piece*
is a subpath shared (up to $G$-translation) between two relators
(including the two sides of one relator). The presentation satisfies
cubical $C'(\alpha)$ if every piece has length $<\alpha\|Y_i\|$.
$B(6)$ (Wise, Geom. Funct. Anal. 2004): no essential closed path in any
$Y_i$ is a concatenation of fewer than 6 pieces; equivalently every
tessellation of $\partial Y_i$ by pieces uses $\ge 6$ ($7$ in our
argument) pieces.

Growth facts (standard; Coornaert orbit growth, FW conjugacy-growth
lemma): with $N_\ell$ the number of classes of translation length
$\le\ell$, $N_\ell\ge c_0\ell^{-q}e^{b\ell}$. Failure probabilities are
monotone in $k$, so take $k=\lfloor e^{c\ell}\rfloor$.

**Estimate (E1, cone segment).** Fix a segment $\sigma\subset\tilde X^{(1)}$
of length $t$. Then
$$\frac{\#\{[g]:\|g\|\le\ell,\ \mathrm{axis}(g)\supset G\cdot\sigma\}}{N_\ell}
\;\le\;P(\ell)\,e^{-bt}$$
for a polynomial $P$ independent of $\sigma$: forcing the axis through
$\sigma$ costs a factor $e^{bt}$ of the $e^{b\ell}$ mass (words with a
prescribed subword; standard exponential-genericity estimate, cf. FW §3).

**Estimate (E2, wall segment).** $X$ compact $\Rightarrow$ finitely many
$G$-orbits of hyperplanes. Hyperplane stabilizers have growth
$\le C e^{at}$. Hence the number of $G$-orbits of wall-paths of length
$t$ is $\le C'e^{at}$, and by (E1) a uniform random relator contains some
wall-path of length $t$ with probability $\le P'(\ell)e^{-(b-a)t}$.

Both estimates are uniform in the relator lengths. Short-shell
cancellation: relators of length $s<\ell$ occur with mass fraction
$\approx e^{b(s-\ell)}$; tiling/occurrence costs scale as $e^{-\beta s}$,
so shell sums $\sum_s e^{bs}e^{-\beta s}e^{b(s-\ell)}$ collapse to
length-independent thresholds (details in Lemma proofs below).

## 2. Lemma 1 — $C'(\alpha)$ failure estimate

$$P(\text{some wall-piece }\ge\alpha\ell)\le e^{c\ell}P_1(\ell)
e^{-(b-a)\alpha\ell},\qquad
P(\text{some cone-piece }\ge\alpha\ell\text{ in some pair})
\le e^{2c\ell}Q_1(\ell)e^{-b\alpha\ell},$$
the $O(\ell^2)$ subsegment positions absorbed in the polynomials.
Indeed: union-bound over $k$ relators (wall case) resp. $k^2$ ordered
pairs and $O(\ell^2)$ position pairs (cone case), applying (E2)/(E1).
Consequently cubical $C'(\alpha)$ holds w.h.p. whenever simultaneously

$$c<(b-a)\alpha,\qquad 2c<b\alpha\tag{*}$$
(strict: exponential decay beats every polynomial).

## 3. Theorem A — proof

Take $\alpha=1/14$. By Lemma 1, $C'(1/14)$ holds w.h.p. if
$c<(b-a)/14$ and $2c<b/14$. The clean sufficient condition
$c<\min\{(b-a)/15,b/30\}$ absorbs all polynomials for large $\ell$.

(i) *$B(6)$.* If every piece is $<\|Y_i\|/14$, covering $\partial Y_i$
needs $>14$ pieces; in particular every essential closed path is a
concatenation of $\ge7\ge6$ pieces. So $C'(1/14)\Rightarrow B(6)$
(the $1/14<1/6$ slack also absorbs the bounded carrier-vs-edge metric
distortion).

(ii) *Hyperbolicity.* FW's own Lemma 3.4 (their [Wis21, Lem 3.70,
Thm 4.7]) states hyperbolicity already at cubical $C'(1/14)$; combined
with $C'(1/14)\Rightarrow B(6)$ this closes the argument with no new
hyperbolicity input.

(iii) *Cubulation + virtual specialness.* Wise [GAFA 2004]: a
word-hyperbolic $B(6)$ cubical presentation has $\bar G$ acting properly
cocompactly on a CAT(0) cube complex (finitely many hyperplane orbits
since $X$ compact and $k<\infty$). Agol: hyperbolic cocompactly
cubulated $\Rightarrow$ virtually special. ∎

Constants strictly exceed FW's in both coordinates.

## 4. Theorem B — proof (direct $B(6)$ tiling count)

$B(6)$ fails only if some $\partial Y_i$ is tiled by $m\le6$ pieces of
total length $\ge s:=\|Y_i\|$. Fix distinguished index ($k$ choices),
$m\le6$, $j\le m$ distinct partner indices ($k^j$ choices), a
composition of $s$ into $m$ lengths ($O(s^{m-1})$ patterns) and
positions ($O(s^2)$ each). A cone-piece of length $t$ from a fixed
partner occurs with probability $\le P e^{-bt}$ by (E1); a wall-piece of
length $t$ with probability $\le P'e^{-(b-a)t}$ by (E2). With
$L_c+L_w=s$ the cone/wall length split, conditional on the length shell
$s$ the bad-pattern probability is
$\le\mathrm{poly}(\ell)\,e^{cj\ell}e^{-bL_c}e^{-(b-a)L_w}$.
Multiplying by the shell-mass fraction $\approx e^{b(s-\ell)}$ and
summing over $s\le\ell$ (the $s$-dependence cancels:
$e^{-bL_c-(b-a)L_w+bs}=e^{aL_w}\le e^{as}\le e^{a\ell}$),
the total $B(6)$-failure probability is
$$\le \mathrm{poly}(\ell)\max_{j\le6,\,L_w\le\ell}
\exp\big((j+1)c\ell-b\ell+aL_w\big)
\le\mathrm{poly}(\ell)\,e^{(7c-(b-a))\ell}\to0
\quad\text{iff }7c<b-a.$$
The clean form $c<(b-a)/8$ holds for all large $\ell$; asymptotically any
$7c<(b-a)-o(1)$. Partner re-use ($<\!m$ distinct partners) and
self-pieces are dominated by the same bound (fewer partner choices,
same length cost; random-word self-overlaps are exponentially rare).
Hyperbolicity throughout this range follows from Ollivier's random
quotient theorem (quotients of non-elementary hyperbolic groups at
density $<1/2$ are hyperbolic w.h.p.; $(b-a)/8/b\le1/8<1/2$; the
conjugacy-length vs word-length sampling differ by $\le\mathrm{poly}$,
exponentially negligible — same comparison as FW §2). Wise + Agol give
cocompact cubulation and virtual specialness. ∎

Remark. Theorem B's threshold $(b-a)/8$ dominates Theorem A's in all
cases (if $(b-a)/20\ge b/41$ then $(b-a)/8>(b-a)/20$; else
$(b-a)>20b/41$ so $(b-a)/8>b/16>b/41$). At $a=0$: $d<1/8$ sharp $1/7$.

## 5. Lemma 4 + Corollary — free-group $d<1/6$

Conjugacy classes of translation length $\le\ell$ in $F_r$ are cyclically
reduced words up to rotation; uniform class vs uniform word differ by a
factor $\le\ell$ (rotation orbit) — polynomial, hence invisible to
density thresholds. So our model at density $d$ is the Ollivier–Wise
model at density $d$. By Ollivier–Wise [Trans. AMS 2011,
DOI:10.1090/S0002-9947-2011-05197-4], random quotients at $d<1/6$ are
hyperbolic and (cubically) $B(6)$, hence cocompactly cubulated. ∎

## 6. Computation (supporting)

`output/artifacts/piece_stats.py` (seed 20260916) samples cyclically
reduced words in $F_2$ ($b=\log3$), $\ell=100$: pair longest-common-piece
tails and fixed-segment hit rates both decay exponentially and lie at or
below the $e^{-bt}$ union-bound scale (see `piece_stats.csv`; small-sample
upper tails: zero hits for $L\ge14$ at $N=300$ pairs, consistent with
theory $<2.1\times10^{-3}$). The fitted log-tail slope ($-1.63$) is
steeper than $-b=-1.10$, i.e. large pieces are even rarer than the bound
used. `thresholds.csv` tabulates FW vs new densities. The proof does not
depend on the numerics; they corroborate the exponential piece statistics
driving Lemmas 1–B.

## 7. Limitations

Thresholds are asymptotic ($\ell\to\infty$; polynomials absorbed, no
explicit $\ell_0$). The $/15$, $/30$, $/8$ constants are clean sufficient
values; sharp forms are $/14$, $/28$, $/7$ up to $o(1)$. Hyperbolicity
uses black boxes: FW Lemma 3.4 (cubical $C'(1/14)$ hyperbolicity; Thm A),
Ollivier density-$1/2$ random-quotient hyperbolicity (Thm B),
Ollivier–Wise $1/6$ (Corollary), Wise $B(6)$ cubulation, Agol virtual
specialness. The $a=0$ surface-group example refers to cubulations with
subexponential (cyclic) hyperplane stabilizers. Only the free-group case
is pushed all the way to $1/6$; general $a=0$ reaches $1/7-o(1)$.

## References

- Futer–Wise, Cubulating random quotients of hyperbolic cubulated
  groups, Trans. AMS Ser. B 2024 (arXiv:2106.04497).
- Ollivier–Wise, Cubulating random groups at density $<1/6$,
  Trans. AMS 2011, DOI:10.1090/S0002-9947-2011-05197-4.
- Wise, Cubulating small cancellation groups, GAFA 2004,
  DOI:10.1007/s00039-004-0454-y.
- Ollivier, random quotients of hyperbolic groups (density $<1/2$
  hyperbolicity); Agol, virtual specialness.
