# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp Szemerédi–Trotter Constant for the 4×4 Integer Grid: 0.71 Suffices and Is Best Possible to 0.01

## Abstract
Let $G=\{0,1,2,3\}^2\subset\mathbb{R}^2$, $|G|=16$, and
$L(G)$ be the set of Euclidean lines meeting $G$ in at least two points.
We enumerate $L(G)$: $|L(G)|=62$, consisting of 10 lines with 4 points,
4 lines with 3 points, and 48 lines with 2 points, with total incidences
$I(G,L(G))=148$. For $P\subset G$ and finite $L$, let $I(P,L)$ be incidences,
$N=|P|$, $M=|L|$, excess $E=I-N-M$. We determine the optimal constant $C^*$
with $I\le C^*N^{2/3}M^{2/3}+N+M$ for all such $P,L$:
$$C^*=\frac{70}{992^{2/3}}=0.7037584\ldots,$$
attained uniquely at $P=G$, $L=L(G)$ ($E=70$). Hence $C=0.71$ always suffices
and any $C\le 0.70$ fails. Proof is by a prefix-optimality reduction plus
exhaustive check over all $2^{16}=65536$ subsets with exact integer arithmetic.
We tabulate per-$N$ maximum excess and maximum ratio and $D_4$-orbit
representatives. This improves the generic constant $\approx 2.5$ by
$\approx 3.5\times$ in the $4\times 4$ regime.

## 1. Setup and line census
Index $G$ by $i=x\cdot 4+y$. For distinct $p_1,p_2\in G$ write the line through
them as $Ax+By+C=0$ with $(A,B)=1$ primitive (divide by $\gcd$) and sign rule:
$A>0$, or $A=0$ and $B>0$. This normalization is bijective between Euclidean
lines and triples $(A,B,C)$.

**Lemma 1 (census).** $|L(G)|=62$: 10 lines contain 4 points of $G$,
4 contain 3 points, 48 contain 2 points.

*Proof by computation (auditable).* Enumerate the $\binom{16}{2}=120$ pairs,
normalize each, group by key. Result: 62 keys; size distribution 10/4/48.
Self-check: $\sum_l \binom{|l\cap G|}{2}=10\cdot 6+4\cdot 3+48\cdot 1=120$,
i.e. the line-sets partition the pairs. This equality certifies the
normalization in both directions: had one Euclidean line been split into two
keys, the sum would be $<120$; had two Euclidean lines been merged, it would
exceed 120 or a set would contain non-collinear points. An independent second
encoding (direction $(dx,dy)$ primitive with $dx>0$ or $dx=0,dy>0$, offset
$c=dy\cdot x-dx\cdot y$) yields identical point-sets. ∎

Explicitly, the 4-point lines are $x=k$, $y=k$ ($k=0,\dots,3$), $y=x$,
$x+y=3$ (10 lines). The 3-point lines are $y=x\pm 1$, $x+y=2$, $x+y=4$
(4 lines). No other slope admits 3 collinear grid points in $\{0,\dots,3\}^2$;
every remaining pair defines a unique 2-point line. Total incidences:
$10\cdot 4+4\cdot 3+48\cdot 2=148$.

## 2. Reduction to subsets of $L(G)$ and prefixes
Fix $P\subset G$, $N=|P|$. For finite $L$, $M=|L|$,
$E(P,L)=I(P,L)-N-M=\sum_{l\in L}(|l\cap P|-1)-N$.

**Lemma 2 (rich-line reduction).** For maximizing $E$ or
$R=E/(N^{2/3}M^{2/3})$ over $L$ with $E>0$, one may assume every
$l\in L$ satisfies $|l\cap P|\ge 2$, hence $L\subset L(G)$.

*Proof.* A line with $|l\cap P|=0$ contributes $-1$ to $E$; deleting it raises
$E$ by 1 and lowers $M$, strictly raising $R$ when $E>0$. A line with
$|l\cap P|=1$ contributes $0$ to $E$; deleting it keeps $E$ and lowers $M$,
strictly raising $R$ when $E>0$. Configurations with $E\le 0$ give $R\le 0$
and cannot beat the positive witness below. Lines with $\ge 2$ points of
$P\subset G$ lie in $L(G)$. ∎

**Lemma 3 (prefix optimality).** Fix $P$. Let $k_i=|l_i\cap P|$ over
$l_i\in L(G)$, sorted $k_{(1)}\ge k_{(2)}\ge\cdots$.
For each $M$, the maximum of $E$ over $|L|=M$ is the top-$M$ prefix excess
$E^*_M=\sum_{i\le M}k_{(i)}-M-N$, and the maximum of $R$ over all $L$ equals
$\max_M E^*_M/(N^{2/3}M^{2/3})$ over $M$ with $E^*_M>0$.

*Proof.* Exchange argument. Any $L$ of size $M$, after deleting $\le 1$-point
lines to $L'$ of size $M'\le M$ with $E(L')\ge E(L)$, satisfies
$E(L')\le E^*_{M'}$. If $E(L')\le 0$ it is not competitive; else
$R(L)\le R(L')\le E^*_{M'}/(N^{2/3}{M'}^{2/3})$. ∎

*Remark.* Since all $k_i\ge 2$ in the sorted rich list, $E^*_M$ is strictly
increasing in $M$ (each step adds $k-1\ge 1$), so per-$P$ maximum *excess* is
at the full rich set; but maximum *ratio* may be interior (dropping a 2-point
line loses 1 of $E$ but shrinks $M$). The two per-$N$ tables therefore differ
for $N\ge 8$; see §4.

**Corollary.** No $P$ with $|P|\le 3$ has positive excess. Indeed $N=1$: all
$k\le 1$; $N=2$: one rich line, $E=-1$; $N=3$: triangle gives $E=0$, collinear
triple $E=-1$. Exhaustion confirms maxima $-1,-1,0$.

## 3. Exhaustive verification and optimal constant
Scan all $65536$ bitmasks $P$. For each, bit-AND against the 62 line masks,
popcount to get $k_i$, sort descending, scan prefixes. Compare ratios by exact
integer arithmetic to avoid floating error:
$$R_1>R_2\iff E_1^3N_2^2M_2^2>E_2^3N_1^2M_1^2.$$

**Theorem.** Let $C^*=70/992^{2/3}=0.7037584\ldots$ Then for all $P\subset G$
and finite $L$,
$$I(P,L)\le C^*|P|^{2/3}|L|^{2/3}+|P|+|L|,$$
and $C^*$ is best possible. In particular $C=0.71$ always suffices and any
$C\le 0.70$ fails (witness $P=G$, $L=L(G)$: $I=148$, $N+M=78$, $E=70$).

*Proof.* Witness gives $R=70/(16^{2/3}62^{2/3})=70/992^{2/3}\approx 0.70376$,
so $C^*\ge$ that value, and $0.70$ fails since
$148>0.70\cdot 992^{2/3}+78$; in integers,
$(100\cdot 70)^3=343\,000\,000\,000>70^3\cdot 16^2\cdot 62^2=337\,533\,952\,000$,
equivalently $100^3=10^6>992^2=984064$, so any $C\le 0.70$ fails.
Exhaustion with Lemmas 2–3 shows no $(P,M)$ prefix exceeds this ratio
(exact integer comparison; single tie: the witness). For $C=0.71$,
$(100E)^3\le 71^3N^2M^2$ holds for every prefix with $E>0$ (0 violations;
witness has margin $71^3\cdot16^2\cdot62^2-(7000)^3=9\,207\,330\,304$).
Empty/small cases ($N=0$ or $M=0$, $E\le 0$) are trivial. ∎

Uniqueness is exact: only one $(P,\text{prefix})$ pair ties $C^*$
($P=G$, full $M=62$), verified by integer equality count. Up to the $D_4$
grid automorphisms this is a single orbit (full set is invariant).

## 4. Per-$N$ tables
Maximum *excess* per $N$ (attained at full rich set) and maximum *ratio* per
$N$ (attained at possibly truncated prefix):

| $N$ | max $E$ | $M$ | $I$ | $E$-ratio | ratio-optimal $(E,M,I,r)$ |
|---|---|---|---|---|---|
| 4 | 2 | 6 | 12 | 0.2404 | same |
| 5 | 5 | 10 | 20 | 0.3684 | same |
| 6 | 9 | 15 | 30 | 0.4481 | same |
| 7 | 14 | 21 | 42 | 0.5026 | same |
| 8 | 20 | 28 | 56 | 0.5422 | (14,16,38,0.5512) |
| 9 | 25 | 32 | 66 | 0.5733 | (19,20,48,0.5960) |
| 10 | 31 | 37 | 78 | 0.6015 | (26,27,63,0.6224) |
| 11 | 37 | 41 | 89 | 0.6291 | (30,29,70,0.6426) |
| 12 | 44 | 46 | 102 | 0.6539 | (38,36,86,0.6650) |
| 13 | 50 | 50 | 113 | 0.6663 | (46,43,102,0.6779) |
| 14 | 56 | 53 | 123 | 0.6833 | (52,47,113,0.6874) |
| 15 | 63 | 58 | 136 | 0.6913 | (62,56,133,0.6964) |
| 16 | 70 | 62 | 148 | 0.7038 | same |

Both ratio columns rise monotonically to $0.7038$ at $N=16$.
*Correction:* an earlier draft table $(2,5,9,14,14,19,26,30,38,46,52,62,70)$
understated $N\ge 8$; the table above is the verified maximum (e.g. 8-point
caps with no three collinear exist — 11 of them — giving $E=20$).

$D_4$-orbits (square symmetries, order 8; idx $=x\cdot4+y$): numbers of
$P$-achievers/orbits for max excess: $N=4$:1278/181, 5:1668/217, 6:998/142,
7:204/28, 8:11/4, 9:32/5, 10:10/3, 11:12/2, 12:2/1, 13:4/1, 14:14/3, 15:4/1,
16:1/1. Canonical (lexicographically minimal bitmask) reps are in
`artifacts/orbit_reps.txt` and `perN_excess.csv`; e.g. $N=8$ cap rep
`0011110000111100` $=\{(0,2),(0,3),(1,0),(1,1),(2,2),(2,3),(3,0),(3,1)\}$;
$N=12$ rep is $G\setminus\{(0,0),(1,2),(2,1),(3,3)\}$; $N=15$ is
$G\setminus\{(2,2)\}$; $N=16$ full grid.

## 5. Reproducibility
Run `python3 artifacts/verify.py` (stdlib only, ~2 s, deterministic): it
re-enumerates lines twice, checks 62/10/4/48 and pair partition, runs the
$65536\times\le 62$ prefix scan with integer comparisons, and asserts the
theorem, uniqueness, and tables. Line list and tables: `lines.csv`,
`perN_excess.csv`, `perN_ratio.csv`, `orbit_reps.txt`.

## 6. Limitations
Scope is $P\subset\{0,1,2,3\}^2$ only; no claim for larger grids or general
point sets (the constant $0.71$ is *not* a general Szemerédi–Trotter constant).
Optimality is relative to the stated $+|P|+|L|$ form. Uniqueness includes the
choice of $L$ (full $L(G)$); per-$N<16$ maximizers are highly non-unique
(hundreds of orbits for small $N$). Proof of the census and optimum is
computer-assisted (exhaustion); the accompanying lemmas are human-proved and
reduce the infinite $L$ search to the finite check.
