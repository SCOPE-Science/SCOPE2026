# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Single-Deletion Characteristic Polynomials of the Cone Extended Shi Arrangement of Type B — Certified Finite-`k` Table with the Extreme-Hyperplane Splitting Rule

## 1. Setting and notation

Let $l\ge 3$, $k\ge 1$, $S=\{-k+1,\dots,k\}$, and work in $\mathbb C^{l+1}$
with coordinates $(x_1,\dots,x_l,z)$.
The cone over the type-$B$ extended Shi arrangement is the central
arrangement $\mathcal A=\mathrm{cShi}(B_l,k)$ consisting of

- coordinate hyperplanes $x_i=mz$ ($1\le i\le l$, $m\in S$),
- difference hyperplanes $x_i-x_j=mz$ ($1\le i<j\le l$, $m\in S$),
- sum hyperplanes $x_i+x_j=mz$ ($1\le i<j\le l$, $m\in S$),
- the infinite hyperplane $z=0$.

Hence $|\mathcal A|=2kl+4k\binom l2+1=2kl^2+1$.
It is classical (Athanasiadis; Yoshinaga) that $\mathcal A$ is free with
exponents $(1,\underbrace{b,\dots,b}_{l\text{ times}})$ where

$$b=2kl\qquad\text{and}\qquad \chi(\mathcal A,t)=(t-1)(t-b)^l,$$

which is consistent with $|\mathcal A|=1+lb$.
For a hyperplane $H\in\mathcal A$ write $\mathcal D=\mathcal A\setminus\{H\}$
for the single-hyperplane deletion.

## 1bis. Coordinate-permutation symmetry lemma (lifting representatives)

Let $S_l$ act by permuting the coordinates $x_1,\dots,x_l$ and fixing $z$.
Each $\sigma\in S_l$ preserves $\mathcal A=\mathrm{cShi}(B_l,k)$ as a set:
coordinate hyperplanes $\{x_i=mz\}$ are permuted among themselves, and the
difference/sum families $\{x_i-x_j=mz\}$, $\{x_i+x_j=mz\}$ are likewise
permuted, since the defining conditions run over all $i$ (resp. all
$i<j$) and all $m\in S$; $z=0$ is fixed.
Hence for every $H\in\mathcal A$ and every $\sigma\in S_l$,
$\sigma(\mathcal A\setminus\{H\})=\mathcal A\setminus\{\sigma(H)\}$ is a
linearly isomorphic arrangement, so
$$\chi(\mathcal A\setminus\{\sigma(H)\},t)=\chi(\mathcal A\setminus\{H\},t),$$
and one deletion is free if and only if the other is.
Consequently the $6k+1$ computed representatives per block — the coordinate
deletions $x_1=mz$ ($2k$ values of $m$), the difference deletions
$x_1-x_2=mz$ ($2k$ values), the sum deletions $x_1+x_2=mz$ ($2k$ values),
and $z=0$ — determine $\chi$ and freeness for **every**
$H\in\mathcal A$ by $S_l$-transport. In particular a splitting (resp.
non-splitting) representative certifies splitting (resp. non-splitting and
hence non-freeness) for its entire $S_l$-orbit.

## 2. Theorem (certified scope)

Put $b=2kl$.
For every $(l,k)\in\{(3,1),(3,2),(3,3),(3,4),(4,1),(4,2)\}$ and every one
of the $6k+1$ coordinate-permutation ($S_l$) orbit representatives actually
computed per block — all translates $m\in S$ for $x_1=mz$, $x_1-x_2=mz$,
$x_1+x_2=mz$, plus $z=0$ — and hence, by the Lemma of §1bis, for every
$H\in\mathcal A$ ($2kl^2+1$ hyperplanes) via $S_l$-transport, the
characteristic polynomial of $\mathcal D=\mathcal A\setminus\{H\}$ is as
follows.

**(a) Splitting (extreme) representatives.** The representative $H$ is
$x_1-x_2=kz$ (difference family, top translate) or
$x_1+x_2=(-k+1)z$ (sum family, bottom translate) if and only if

$$\chi(\mathcal D,t)=(t-1)(t-b)^{\,l-1}(t-b+1). \tag{*}$$

There are exactly $2$ such orbit representatives in each certified block
($1$ difference-top and $1$ sum-bottom); the equality $(*)$ was verified
exactly (see §4). By $S_l$-symmetry this gives $l(l-1)$ splitting
hyperplanes per block ($6$ for $l=3$, $12$ for $l=4$).
The statement is for $S_l$-orbits only, not full $W(B_l)$-orbits:
indeed the sign flip $x_1-x_2=kz\leftrightarrow x_1+x_2=kz$ does **not**
preserve splitting — e.g. for $(l,k)=(3,2)$ the certified table gives
$x_1+x_2=2z$ (row `s_m2`)
$\chi=(t-1)(t^3-35t^2+411t-1618)$ with cofactor constant term $-1618$,
$8$ divisors checked, minimum $|Q(r)|=928\ne 0$, i.e. certified
non-splitting — so no $W(B_l)$-conjugacy version of the "if and only if"
holds.

**(b) All other deletions.** For every other representative $H$ (all
coordinate deletions, all remaining difference/sum translates, and $z=0$),
$\chi(\mathcal D,t)$ does **not** factor as a product of linear terms over
$\mathbb Z$.
Precisely, writing $\chi(\mathcal D,t)=(t-1)Q(t)$ (note $\chi(\mathcal D,1)=0$
since $\mathcal D$ is central of rank $l+1\ge 2$ after the deletion —
verified in the certificate), either

- (A) $Q$ is monic integral of degree $l$ with **no integer root**
  ($66$ cases), or
- (B) $\chi(\mathcal D,t)=(t-1)(t-r)R(t)$ with $r\ne 1$ an integer and $R$
  monic integral of degree $\ge 2$ with **no integer root** ($6$ cases:
  the $(3,3)$ deletions $x_1-x_2=0$, $x_1+x_2=0$, $x_1-x_2\in\{0,1\}$-adjacent
  pairs and their $(3,4)$ analogues listed in `chi_table.json`).

In either sub-case $\chi(\mathcal D,t)$ is not a product of $l+1$ integral
linear factors.

**(c) Non-freeness corollary.** Every deletion in class (b) is **not free**:
a free central arrangement satisfies Terao's factorization theorem,
$\chi=(t-d_1)\cdots(t-d_{l+1})$ with the $d_i$ the derivation exponents, so
non-factorization over $\mathbb Z$ implies non-freeness.
No freeness is asserted for the splitting class (a): Terao's theorem has no
converse, and no Saito basis is exhibited here.

### Remarks on orbit representatives vs. all hyperplanes
The certificate computes the $6k+1$ representatives of §2 directly
($2k$ coordinate-$x_1$ + $2k$ difference-$(1,2)$ + $2k$ sum-$(1,2)$ translates
plus $z=0$): 7 rows for $k=1$, 13 for $k=2$, 19 for $k=3$, 25 for $k=4$,
per block. The Lemma of §1bis lifts every row to its full $S_l$-orbit, so
$\chi$ and (non-)freeness are certified for all $2kl^2+1$ hyperplanes. The
computation confirms the expected symmetries
(e.g. for $l=3$: $c_m\leftrightarrow c_{1-m}$-type palindromies visible in
the raw fits) but the theorem does not depend on them.

## 3. Proof method

### 3.1 Finite-field computation of $\chi$ (Crapo–Rota)
For a complex arrangement, $\chi(\mathcal D,p)$ equals the number of
$\mathbb F_p$-points of the complement for all sufficiently large ("good")
primes $p$. The affine slice $z=1$ of $\mathrm{cShi}(B_l,k)$ has hyperplanes
$x_i=m$, $x_i-x_j=m$, $x_i+x_j=m$ ($m\in S$); the slice $z=c\ne 0$ is
isomorphic to it by scaling, while the $z=0$ slice is the Weyl arrangement
of type $B_l$ when $H\ne\{z=0\}$ (hence contributes $0$ points, since
$z=0$ is still present) and the $B_l$ Weyl complement when $H=\{z=0\}$.
Thus, with $N_{\mathrm{aff}}(p)$ the directly enumerated affine-slice
complement count,

$$\chi(\mathcal D,p)=(p-1)\,N_{\mathrm{aff}}(p)+\varepsilon\,N_{B_l}(p),
\qquad\varepsilon=\begin{cases}1&H=\{z=0\}\\0&\text{else,}\end{cases}$$

computed by exact enumeration over $\mathbb F_p^{\,l}$ in
`artifacts/chi_count.py`.

### 3.2 Good primes and interpolation
A prime is accepted as good only if the **full** arrangement count
reproduces the known freeness formula $(p-1)(p-b)^l$ at that prime; the
deletion fits use the same prime set (e.g. for $(3,4)$: all of
$29,31,\dots,73$; small primes with wrap-around disagree and are excluded).
The degree-$(l+1)$ interpolant through the good-prime values is solved
exactly over $\mathbb Q$ (SymPy) and accepted only when (i) all coefficients
are integers, (ii) it reproduces **every** good-prime count, and (iii)
$\chi(1)=0$ with exact divisibility by $(t-1)$. The script
`artifacts/cert_table.py` re-verifies all three conditions and writes
`chi_table.json` (84 certified rows).

### 3.3 From counts to the stated polynomials
Since the interpolated polynomial agrees with the true characteristic
polynomial at more than $\deg\chi=l+1$ values (at least $10$ good primes in
each block), it **is** the true characteristic polynomial. The splitting
equality $(*)$ is an exact symbolic identity of the interpolated
polynomial. The non-splitting certificates are exact: any integer root $r$
of a monic integral polynomial divides its constant term, so evaluating at
**every** divisor of $Q(0)$ (resp. $R(0)$) and finding no zero — together
with the exact SymPy $\mathbb Z$-factorization showing no linear factor —
proves non-factorization over $\mathbb Z$. The certificate records, for each
row, the constant term, the number of divisors checked, the minimum
$|Q(r)|>0$, and the full factor list.

### 3.4 Terao step
If $\mathcal D$ were free with exponents $(d_i)$, Terao's factorization
theorem gives $\chi(\mathcal D,t)=\prod_i(t-d_i)$ with $d_i\in\mathbb Z_{\ge0}$.
Contrapositively, the certified non-factorization implies non-freeness for
all $66+6$ class-(b) representative rows. This direction of Terao is unconditional.

## 4. Evidence summary (machine certificate)
- `chi_table.json`: 6 blocks $\times$ the $6k+1$ representatives = **84 rows**; each row:
  exact $\chi$ (integer coefficients), its $\mathbb Z$-factor list, and
  either the verified SPLIT identity $(*)$ (12 rows) or the divisor-exhaustion
  non-root certificate (72 rows: 66 kind A + 6 kind B with the extra root and
  residual recorded, including discriminants $353$ ($l=3$, residual
  $t^2-37t+353$) where quadratic).
- Reproduction: `python3 artifacts/cert_table.py` (needs `numpy`, `sympy`;
  deterministic; no randomness). Good-prime sets are recorded per block in
  the JSON file. Spot checks: the full arrangement always refits
  $(t-1)(t-b)^l$; extreme deletions refit $(*)$ with $Q(b)=0$ while e.g.
  coordinate-top deletions have $Q(b)=1$ and $z$-deletions have large
  $Q(b)$ (e.g. $399$ for $(3,4)$), consistent with the stated dichotomy.
- Representative values ($l=3,k=2$, $b=12$): coord-top
  $(t-1)(t^3-35t^2+410t-1607)$; diff-top
  $(t-1)(t-12)^2(t-11)$; sum-bottom same; $z$-deletion
  $(t-1)(t^3-35t^2+424t-1713)$; all verified non-split except the stated two.

## 5. Limitations and scope (read carefully)
- The **theorem is the finite table** in §2, not the all-$k$ target: the
  target's "all $k\ge 1$, $3\le l\le 6$ with Saito/addition–deletion proof"
  is **not** claimed. The closed $k$-polynomial patterns observed for
  $l=3$ (e.g. coord-top $\chi=t^4-18kt^3+(108k^2+6k+1)t^2-(216k^3+72k^2+1)t
  +(216k^3-36k^2+12k-1)$) are conjectural guides, not theorems, and are not
  part of the claim.
- Freeness of the 12 splitting representative rows is **not** claimed (would require
  exhibiting a Saito basis; Terao's converse is false in general).
- The full arrangement's freeness/exponents $(1,b,\dots,b)$ is used only to
  select good primes (self-check), never as a logical premise of the
  deletion identities: each deletion $\chi$ is certified by its own
  overdetermined interpolation.
- Finite-field counts assume the standard Crapo–Rota theorem for good
  primes; bad (small/wrap-around) primes are excluded by the
  full-arrangement agreement test, and every accepted fit is verified on all
  recorded good primes.
- Originality: a controlled literature-search call for the emergent claim
  failed mechanically (missing Serpent API key file); no literature novelty
  assertion beyond the verified computation is made. The value is the
  certified table and the sharp extreme-hyperplane splitting rule, both
  reproducible from the artifacts.
