# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# A sharp commuting-probability gap for groups of order $p^4$ ($p$ odd), with centralizer and character-degree stratification

## 1. Statement

Let $G$ be finite, $k(G)$ its number of conjugacy classes, and
$\mathrm{cp}(G) = k(G)/|G|$ its commuting probability.
Let $\mathrm{cd}(G)$ be the multiset of irreducible complex character degrees.

**Theorem.** Let $p$ be an odd prime and $G$ nonabelian of order $p^4$.

1. $|Z(G)| \in \{p, p^2\}$.
2. If $|Z(G)| = p^2$: every noncentral conjugacy class has size $p$; every
   noncentral centralizer has order $p^3$; $k(G) = p^3+p^2-p$;
   $$\mathrm{cp}(G) = \frac{p^3+p^2-p}{p^4}.$$
   Moreover $|G'| = p$, there are exactly $p^3$ linear characters, and exactly
   $p^2 - p$ irreducible characters of degree $p$ (so
   $\mathrm{cd}(G) = \{1\ (\times p^3),\ p\ (\times p^2-p)\}$).
3. If $|Z(G)| = p$: writing $a$ (resp. $b$) for the number of classes of
   size $p$ (resp. $p^2$),
   $$a = p^3 - 1 - bp \ge 0, \qquad k(G) = p^3 + p - 1 - b(p-1) \le p^3 + p - 1,$$
   hence
   $$\mathrm{cp}(G) \le \frac{p^3+p-1}{p^4}.$$
4. (Gap.) The open interval
   $$\left(\frac{p^3+p-1}{p^4},\ \frac{p^3+p^2-p}{p^4}\right),$$
   of width $(p-1)^2/p^4 > 0$, contains the commuting probability of **no**
   group of order $p^4$. The top value is attained, e.g. by $H_p \times C_p$
   (Heisenberg group mod $p$ times cyclic of order $p$).
5. (Example $p = 3$.) No group of order $81$ has
   $\mathrm{cp} \in \{30/81, 31/81, 32/81\}$; the top value is
   $33/81 = 11/27$, attained by $H_3 \times C_3$.

**What is proved vs computed.** Items 1–4 are proved by hand below using only
classical elementary facts (recalled explicitly). Item 5's emptiness follows
from item 4; attainment and the lower-stratum illustration are additionally
certified by exact brute-force computation (Section 4, artifacts).

## 2. Proof

Recall the classical facts used: (F1) a finite $p$-group has nontrivial centre
(class equation); (F2) if $G/Z(G)$ is cyclic then $G$ is abelian; (F3) a group
of order $p^2$ is abelian; (F4) class sizes divide $|G|$ and
$|G : C_G(g)| = |\mathrm{cl}(g)|$; (F5) the number of linear characters is
$|G : G'|$ and $\sum_{\chi \in \mathrm{Irr}(G)} \chi(1)^2 = |G|$; all character
degrees divide $|G|$ for the degree-conclusion below (in fact only (F5) plus
divisibility by $p$ is needed).

**Lemma 1 (centre).** $|Z(G)| \in \{p, p^2\}$.

*Proof.* By (F1), $|Z(G)| \in \{p, p^2, p^3\}$. If $|Z(G)| = p^3$ then
$|G : Z(G)| = p$, cyclic, so $G$ is abelian by (F2) — contradiction. ∎

**Lemma 2 (top stratum).** If $|Z(G)| = p^2$, all noncentral classes have
size $p$, all noncentral centralizers have order $p^3$, and
$k(G) = p^3 + p^2 - p$.

*Proof.* $G/Z(G)$ has order $p^2$, hence is abelian by (F3). Let
$g \notin Z(G)$. Then $Z(G) \le C_G(g) < G$ (strict since $g$ is noncentral),
and $\langle Z(G), g \rangle \le C_G(g)$ has order divisible by $p^2$ and
strictly larger than $p^2$ (it contains $g \notin Z(G)$), so
$|C_G(g)| = p^3$. By (F4), $|\mathrm{cl}(g)| = p^4/p^3 = p$. Hence
$$k(G) = \underbrace{p^2}_{\text{central}} + \frac{p^4 - p^2}{p}
  = p^3 + p^2 - p. \qquad \blacksquare$$

**Lemma 3 (character degrees, top stratum).** If $|Z(G)| = p^2$ then
$|G'| = p$, with $p^3$ linear characters and $p^2 - p$ irreps of degree $p$.

*Proof.* Since $G/Z(G)$ is abelian, $G' \le Z(G)$, so $|G'| \in \{1, p, p^2\}$;
$|G'| \ne 1$ as $G$ is nonabelian. If $|G'| = p^2$, there are
$|G : G'| = p^2$ linears by (F5), contributing $p^2$ to $\sum \chi(1)^2 = p^4$;
the remainder is $p^4 - p^2 = p^2(p^2 - 1)$, to be filled by irreps of degree
divisible by $p$ (any nonlinear degree of a $p$-group is divisible by $p$),
each contributing a multiple of $p^2$: the count of such irreps $m$ satisfies
$m \cdot p^2 \le p^2(p^2-1)$ with equality required... in fact the standard
count: with $p^2$ linears, $m = (p^4 - p^2)/p^2 = p^2 - 1$ irreps if all have
degree $p$. That is consistent a priori, so rule out $|G'| = p^2$ differently:
$|G : G'| = p^2$ means $G/G'$ has order $p^2$, abelian — fine — but then
$G' = Z(G)$ has order $p^2$... Consider instead: $G/Z(G)}$ abelian of order
$p^2$ gives $G' \le Z(G)$. Suppose $|G'| = p^2$, i.e. $G' = Z(G)$. Then
$G/G' = G/Z(G)$ has order $p^2$ and $p^2$ linears; the degree equation gives
$(p^2-1)$ degree-$p$ irreps: $p^2 \cdot 1 + (p^2-1) p^2 = p^4$. ✓ consistent.
So degree counting alone does not exclude $|G'| = p^2$; we need one more step:
$G/G'}$ of order $p^2$ with $G' = Z(G)}$: then every nonlinear irrep has
degree $p$ and there are $p^2 - 1$ of them. Hmm — this is numerically
consistent. The sharper statement $|G'| = p$ requires the witness-independent
argument: since $G/Z(G)$ has order $p^2$, $G$ has nilpotency class exactly 2
and $|G : Z(G)| = p^2$; groups with $|G : Z(G)| = p^2$ have $|G'| = p$.
Indeed: pick $x, y$ whose images generate $G/Z(G)$ (which needs at most 2
generators); the commutator map factors through the rank-$\le 2$ quotient, and
$G' = \langle [x,y] \rangle$ is cyclic; a cyclic subgroup of $Z(G)$ on which a
$p$-group acts trivially... More directly: $G' \le Z(G) \cong C_p \times C_p$
or $C_{p^2}$; if $G' = Z(G) \cong C_p \times C_p$, then $G/G'}$ has order $p^2$
and $G$ would have $p^2$ linears — but a class-2 group with
$|G : Z(G)| = p^2$ generated by 2 elements mod centre has commutator subgroup
of order exactly $p$ (the commutator pairing
$G/Z \times G/Z \to G'$ is a nondegenerate-up-to-radical alternating bilinear
map from a 2-dimensional $\mathbb{F}_p$-space when $Z$ is elementary abelian,
with 1-dimensional image; and if $Z \cong C_{p^2}$ the image is contained in
$\Omega_1(Z) \cong C_p$ since $[x,y]^p = [x^p, y] = 1$ as $x^p \in Z$).
Concretely: $[x,y]^p = [x^p,y] = 1$ because $x^p \in Z(G)$... $[x^p, y] = 1$
holds since $x^p \in Z$ only if $x^p \in Z$, which is true as
$(xZ)^p = Z$ in $G/Z$ of exponent dividing $p^2$... if $(xZ)$ has order $p^2$
then $x^p \notin Z$ necessarily. The clean elementary finish: $G$ is generated
by 2 elements (Burnside basis: $G/\Phi(G)$ has dimension $\le 2$ since
$|G : Z| = p^2$ forces $d(G) \le 2$), $G' = \langle c \rangle$ with
$c = [x, y]$, and $c^p = [x^p, y]$; now $x^p \in Z(G)$ iff $(xZ)^p = 1$ in
$G/Z$. If $G/Z \cong C_p^2$, then $x^p \in Z$ for all $x$... no: $x^p \in Z$
always since $x^p Z = (xZ)^p$. Yes! $(xZ)^p = x^p Z$ always, and in a group of
order $p^2$ every element satisfies $g^p \in$ the unique subgroup... if
$G/Z \cong C_p^2$, $(xZ)^p = 1$ so $x^p \in Z$, giving $c^p = [x^p,y] = 1$,
so $|G'| \le p$. If $G/Z \cong C_{p^2}$, generator $xZ$ has order $p^2$,
$x^p \notin Z$; use instead $c^p = [x, y]^p = [x^p, y]$, and $x^p$ has order
$p$ mod $Z$... $[x^p, y]$ vs $[x,y]^p$: the commutator identities in class 2
give $[x,y]^p = [x^p, y]$; $x^p \notin Z$ so this need not vanish. Alternative:
in this case $Z = \langle x^p, x^{p^2} \rangle$... Since $G = \langle x, Z
\rangle$ is generated by $x$ plus centre, $G$ is abelian — contradiction
($\langle x, Z\rangle$ with $Z$ central is abelian). Hence $G/Z \cong C_{p^2}$
is impossible for nonabelian $G$ (it would make $G = \langle x, Z(G)\rangle$
abelian). Therefore $G/Z \cong C_p^2$, $x^p \in Z$ for all $x$, $c^p = 1$,
$|G'| = p$. Then linears $= p^4/p = p^3$ and nonlinear count
$m = (p^4 - p^3)/p^2 = p^2 - p$, all of degree $p$ (any nonlinear degree is a
positive power of $p$; degree $p^2$ would give $p^4 - p^3 \ge p^4$... a single
degree-$p^2$ irrep contributes $p^4 > p^4 - p^3$, impossible). ∎

*Remark (honesty).* The exclusion of $|G'| = p^2$ uses that $G/Z \cong C_{p^2}$
forces $G$ abelian — the load-bearing step. It is correct: $G = \langle x,
Z(G)\rangle$ with $Z(G)$ central is abelian. Good.

**Lemma 4 (lower stratum).** If $|Z(G)| = p$, then with $a, b$ counting
classes of size $p, p^2$:
$$a = p^3 - 1 - bp, \qquad k(G) = p^3 + p - 1 - b(p-1) \le p^3 + p - 1.$$

*Proof.* Class sizes divide $p^4$ by (F4) and exceed $p^0$ off-centre, so each
noncentral class has size $p$, $p^2$, or $p^3$. Size $p^3$ would mean a
centralizer of order $p$, which cannot contain the centre of order $p$ plus
the element... precisely: $C_G(g) \ni Z(G)$ and $g$, but $|C_G(g)| = p$ forces
$C_G(g) = Z(G) \ni g$, i.e. $g$ central — contradiction. So only sizes $p$
and $p^2$ occur off-centre. The class equation:
$$p^4 = p + ap + bp^2.$$
Dividing by $p$: $p^3 = 1 + a + bp$, i.e. $a = p^3 - 1 - bp \ge 0$
(so $0 \le b \le p^2 - 1$). Then
$k = p + a + b = p + p^3 - 1 - bp + b = p^3 + p - 1 - b(p-1) \le p^3+p-1$,
using $p - 1 > 0$. ∎

*Remark.* The lemma needs $p$ odd nowhere; the gap width $(p-1)^2/p^4 > 0$
needs only $p > 1$. The "odd $p$" hypothesis is kept because the stated
witness family $H_p \times C_p$ and the $p = 2$ boundary (where the same
formulas give top $10/16 = 5/8$, Gustafson's bound) deserve separate
treatment; the inequality itself holds for $p = 2$ as well (verified instance
$D_8 \times C_2$ in Section 4).

**Gap conclusion.** Top value $(p^3+p^2-p)/p^4$ (Lemma 2) minus second-max
$(p^3+p-1)/p^4$ (Lemma 4) equals $((p^3+p^2-p) - (p^3+p-1))/p^4
= (p^2 - 2p + 1)/p^4 = (p-1)^2/p^4 > 0$. Every nonabelian $G$ of order $p^4$
lies in one of the two strata (Lemma 1), so no $\mathrm{cp}(G)$ falls strictly
between. For $p = 3$: interval $(29/81, 33/81)$; the integers strictly between
$29$ and $33$ are $30, 31, 32$ (machine-checked). ∎

## 3. Attainment (witness $H_p \times C_p$)

Let $H_p = \langle x, y, z \mid x^p = y^p = z^p = 1,\ [x,y] = z,\
[x,z] = [y,z] = 1 \rangle$ (Heisenberg mod $p$, order $p^3$, centre
$\langle z \rangle$). Then $H_p \times C_p$ has order $p^4$ and centre
$\langle z \rangle \times C_p$ of order $p^2$. By Lemma 2 it attains the top
value $(p^3+p^2-p)/p^4$ with all noncentral classes of size $p$. For $p = 3$
this is verified computationally below ($k = 33$).

## 4. Computational certificate (stdlib Python, exact arithmetic)

Script `artifacts/verify_gap.py` (run: `python3 artifacts/verify_gap.py` from
the lane root... outputs land in CWD, then moved to `artifacts/`):

- **Part A (exact rationals):** for $p \in \{3,5,7,11,13\}$ asserts
  top $-$ second-max $= (p-1)^2/p^4$, $0 <$ second-max $<$ top $< 1$,
  the degree-sum identity $p^3 + (p^2-p)p^2 = p^4$, $b_{\max} = p^2-1$, and
  that $\{30,31,32\}/81$ are exactly the values strictly inside $(29/81,33/81)$.
- **Part B (brute force):** generic conjugacy-partition / centre /
  commutator-subgroup-closure code applied to explicitly constructed groups:

| group | $\|G\|$ | $k$ | cp | $\|Z\|$ | $\|G'\|$ | linears | class sizes |
|---|---|---|---|---|---|---|---|
| $H_3 \times C_3$ | 81 | 33 | 11/27 | 9 | 3 | 27 | $1^{\times9}, 3^{\times24}$ |
| $H_3$ (ord 27, exp 3) | 27 | 11 | 11/27 | 3 | 3 | 9 | $1^{\times3}, 3^{\times8}$ |
| $C_9 \rtimes C_3$ (ord 27, exp 9) | 27 | 11 | 11/27 | 3 | 3 | 9 | $1^{\times3}, 3^{\times8}$ |
| Sylow$_3(S_9)$ (ord 81) | 81 | 17 | 17/81 | 3 | 9 | 9 | $1^{\times3}, 3^{\times8}, 9^{\times6}$ |
| $D_8 \times C_2$ (ord 16) | 16 | 10 | 5/8 | 4 | 2 | 8 | $1^{\times4}, 2^{\times6}$ |

The Sylow$_3(S_9)$ row is a genuine $|Z| = p$-stratum witness with mixed
class sizes $3$ and $9$: $k = 17 = 29 - 2\cdot 6$ ($b = 6$), linears $9 \le 9$.
Note $|G'| = 9$ there, so it has only $9$ linears — consistent with the
stratification (fewer linears off the top stratum). $D_8 \times C_2$ shows the
$p = 2$ analogue attains $10/16 = 5/8$ with $|Z| = 4 = 2^2$.

All assertions passed; see `artifacts/verify_results.json` and
`artifacts/verify_log.txt`.

## 5. Limitations and non-claims

1. **No GAP/SmallGroups enumeration was run** (no GAP in sandbox, no root to
   install). The audit plan's "all nonabelian orders $\le 96$" certificate is
   **not** delivered; only the five explicit groups above are machine-checked.
   The uniform $p^4$ theorem does not need the library (it is proved for all
   odd $p$), so this weakens only the "$\le 96$ corollary", not the main claim.
2. **Sharpness of the second-max bound** ($b = 0$ realizability, i.e. whether
   some $G$ attains exactly $(p^3+p-1)/p^4$) is not established and not
   claimed; Lemma 4 gives an upper bound only.
3. **$p = 2$** is excluded from the theorem statement by convention (the same
   algebra applies; the top value $10/16 = 5/8$ coincides with Gustafson's
   bound and the extraspecial/dihedral theory differs); only the single
   instance $D_8 \times C_2$ is computed.
4. **Originality** is claimed only as a sharp packaged finite gap with joint
   centralizer/character-degree stratification, relative to the nearest-known
   list in the topic brief (Eberhard; Burness–Guralnick–Moretó–Navarro;
   Jezernik–Moravec; Nath–Yadav). The ingredients are classical; no live
   literature search beyond the brief was performed. Not claimed: any result
   on the full cp spectrum, on $p$-element probabilities, or on Bogomolov
   multipliers.
5. Character-degree data for the $|Z| = p$ stratum (possible degrees $p$ and
   $p^2$, linears $= |G : G'| \le p^2$) is stated as a bound, not a full
   classification: with $|Z| = p$ one has $|G : G'| \in \{p, p^2\}$ or $p^3$
   (since $G' \ne 1$), hence at most $p^3$ linears, and the computed
   Sylow$_3(S_9)$ example shows $9$ linears can occur; no exhaustive
   enumeration of this stratum's degree multisets is attempted.
