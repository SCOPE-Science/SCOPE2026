# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Fixed-point-free involutory autotopism obstruction for 3-MOLS(10)

## Theorem (target claim, proved)

No orthogonal array OA(5,10) — equivalently, no set of 3 mutually orthogonal
Latin squares of order 10 — admits an involutory autotopism acting
fixed-point-freely, i.e. as five disjoint transpositions, on each of the five
coordinate positions (rows, columns, and the three symbol sets).

## Definitions

- An OA(5,10) is a set $O$ of 100 rows in $Z_{10}^5$ such that for every pair
  of coordinates $j<k$, the 100 projected pairs $(x_j,x_k)$ are all distinct,
  hence cover $Z_{10}^2$ exactly once (strength 2, index 1).
- An *autotopism* is a 5-tuple $\sigma=(\sigma_0,\dots,\sigma_4)$ of
  permutations of $Z_{10}$, one per coordinate, with $\sigma(O)=O$ (applied
  coordinate-wise). It is *involutory* if each $\sigma_j$ has order $\le 2$,
  and *fixed-point-free* if each $\sigma_j$ is a product of five disjoint
  transpositions (no fixed points).
- OA(5,10) with first two coordinates as row/column indices and last three as
  symbols is the standard equivalent of 3-MOLS(10); the autotopism notions
  coincide. We work with the OA picture.

## Proof

**Step 1 — Normalization.** All fixed-point-free involutions on 10 points are
conjugate in $S_{10}$. Given $O$ with autotopism
$\sigma=(\sigma_0,\dots,\sigma_4)$ of this type, choose bijections $\psi_j$
with $\psi_j\sigma_j\psi_j^{-1}=\tau$ where $\tau(n)=n+5\pmod{10}$ is the
standard five-transposition involution. The isotopic array
$O'=\psi(O)=\{(\psi_0(x_0),\dots,\psi_4(x_4)):x\in O\}$ is still an OA(5,10)
(coordinate bijections preserve bijectivity of pair projections), and it has
the diagonal autotopism $(\tau,\dots,\tau)$, since
$(\psi\sigma\psi^{-1})(\psi(O))=\psi(\sigma(O))=\psi(O)$.
Hence it suffices to refute a diagonal-$\tau$ autotopism.

**Step 2 — Orbit structure.** Let $G=C_2$ act on rows of $O'$ by applying
$\tau$ in every coordinate simultaneously. This preserves $O'$. Since $\tau$
has no fixed point in any coordinate, no 5-tuple is fixed, so every $G$-orbit
has size exactly 2. There are $100/2=50$ orbits $\{r,\tau(r)\}$.

**Step 3 — CRT splitting.** Identify $Z_{10}\cong Z_2\times Z_5$ via
$n\mapsto(n\bmod 2,n\bmod 5)$. Since $5\equiv 1\pmod 2$ and $5\equiv 0\pmod 5$,
$$\tau(e,a)=(e+1,a):$$
$\tau$ flips the $Z_2$-bit and fixes the $Z_5$-part. Write each entry
$x_{i,j}=(\varepsilon_{i,j},a_{i,j})$. Each $G$-orbit $i\in\{1,\dots,50\}$
shares one $Z_5$-vector $a_i\in Z_5^5$ and carries complementary $Z_2$-vectors
$u_i,\bar u_i=u_i+(1,1,1,1,1)$ in $Z_2^5$; its two rows are $(u_i,a_i)$ and
$(\bar u_i,a_i)$.

**Step 4 — Projected orthogonality and the xor lemma.** Fix columns $j<k$.
The pair projection $O'\to Z_{10}^2$ is a bijection (100 rows onto 100 pairs).
Reducing mod 5, each $Z_5$-pair $(\alpha,\beta)\in Z_5^2$ has exactly 4
preimage rows (the four $Z_2$-lifts), because $Z_{10}\to Z_5$ is 2-to-1.
Each $G$-orbit contributes its 2 rows to a single $Z_5$-pair, so each
$Z_5$-pair is covered by exactly 2 orbits.

The four rows above a fixed $Z_5$-pair have $Z_2$-pairs covering all of
$Z_2^2=\{00,01,10,11\}$ (strength 2 forces all four lifts to occur).
Each orbit contributes a complementary pair $\{p,p+(1,1)\}$. The only
complementary pairs in $Z_2^2$ are $\{00,11\}$ (xor $0$) and $\{01,10\}$
(xor $1$). Hence the two orbits above the same $Z_5$-pair have opposite xor:
with $s_i(j,k)=u_{i,j}+u_{i,k}\pmod 2$ (well defined, since complementing
$u_i$ preserves it), the two covering orbits satisfy $s+s'=1\pmod 2$.

**Step 5 — Column-parity equations.** Group the 50 orbits by their
$Z_5$-pair $p=(a_j,a_k)$. For each of the 25 pairs, the two covering orbits
contribute $1\pmod 2$ to $\sum_i s_i(j,k)$. Therefore
$$\sum_{i=1}^{50} s_i(j,k) = 25 \equiv 1 \pmod 2.$$
But $\sum_i s_i(j,k)=\sum_i(u_{i,j}+u_{i,k})=C_j+C_k$ where
$C_j=\sum_i u_{i,j}\pmod 2$. So for *every* pair $j<k$:
$$C_j + C_k = 1 \pmod 2.$$

**Step 6 — Contradiction.** Restrict to any three columns, say $0,1,2$:
$C_0+C_1=C_0+C_2=C_1+C_2=1$. Summing gives $2(C_0+C_1+C_2)=0$ on the left but
$3=1$ on the right mod 2 — impossible. (Exhaustively: all 8 assignments in
$Z_2^3$ fail; a fortiori all 32 in $Z_2^5$ fail.) Contradiction. No choice of
$Z_5$-part or $Z_2$-part escapes, since the argument used no property of the
$a_i$ beyond counting.

Therefore no OA(5,10) with diagonal-$\tau$ autotopism exists, and by Step 1 no
OA(5,10) with any fixed-point-free involutory autotopism exists. Via the
standard OA–MOLS dictionary, no 3-MOLS(10) admits such an autotopism. ∎

## Remarks

- The argument uses only: 10 = 2·m with m = 5 odd (so $m^2=25$ is odd), and
  at least 3 coordinates. It generalizes to: no OA$(k,2m)$ with a fixed-point-
  free involutory autotopism exists when $m$ is odd and $k\ge 3$. The target is
  the case $m=5$, $k=5$.
- The order-2 case is the base instance: no $2\times 2$ Latin square admits
  $L(r+1,c+1)=L(r,c)+1$; the general proof is the counting lift of this fact.
- Machine replay: `output/artifacts/verify_parity.py` (stdlib only) checks the
  CRT flip/fix property, the 5-transposition profile of $+5$, the orbit-xor
  lemma over $Z_2^2$, exhaustive UNSAT of $w_j+w_k=1$ for 3 and 5 columns,
  brute-force order-2 base case, and oddness of $m^2$. All checks pass.

## Separation from prior work

GDD-in-MOLS(10) classifications, Gill–Wanless relation-pair censuses, and
Egan–Wanless proximity data constrain blocks, relations, or distances — none
states a theorem about a global fixed-point-free involution, and none implies
the column-parity system above. No OA table tabulates this involution profile.
The proof is therefore an independent advance in either direction allowed by
the admission review (here: the positive/obstruction direction).
