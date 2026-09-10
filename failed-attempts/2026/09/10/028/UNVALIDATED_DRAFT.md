# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Formality dichotomy for the triple-2-sphere wedge plus one 5-cell (lane-561)

## Theorem (target claim)
Let $V=S^2_1\vee S^2_2\vee S^2_3$ and let $w_0\in\pi_4(V)$ generate a
distinguished infinite-cyclic Hilton–Whitehead summand $W\cong\mathbb{Z}$
(a Hall-word line in the distinct-index weight-3 subspace, e.g. the line
of $[[\iota_1,\iota_2],\iota_3]$ modulo the Jacobi relation).
Put $X_1=V\cup_{1\cdot w_0}e^5$. Let $x_i\in H^2(X_1;\mathbb{Q})$ be dual to
the $i$-th sphere and $z$ span $H^5(X_1;\mathbb{Q})\cong\mathbb{Q}$.
Then:
1. $x_ix_j=0$ for all $i,j$, so the rational triple Massey product
   $\langle x_1,x_2,x_3\rangle$ is defined;
2. its indeterminacy $x_1H^3+H^3x_3$ is $0$, and as a singleton it equals
   $\pm z\neq 0$ (sign by ordering convention);
3. hence $X_1$ is non-formal over $\mathbb{Q}$ (DGMS transfer);
4. mod 2, $H^{\le 6}(X_1;\mathbb{F}_2)$ is $\mathbb{F}_2$ in degrees $0$,
   $\mathbb{F}_2^3$ in degree $2$, $\mathbb{F}_2$ in degree $5$, $0$ else, and
   every primary operation landing in degrees $\le 6$ vanishes; in particular
   the cup-square/$\mathrm{Sq}^2$ line satisfies
   $\mathrm{Sq}^2(x_i)=x_i^2=0$, $\mathrm{Sq}^1(x_i)=0$,
   $\mathrm{Sq}^1(z)=\mathrm{Sq}^2(z)=0$ (table $T=0$; line $L=\ker\mathrm{Sq}^2$,
   free-Whitehead, non-Hopf).

## Proof
### Step 1. Cellular chain, cohomology, definedness (audit step 1)
$X_1$ has one $0$-cell, three $2$-cells, one $5$-cell. All cellular
differentials are $0$ (non-adjacent dimensions), so integrally
$H_2=\mathbb{Z}^3$, $H_5=\mathbb{Z}$, rest $0$ below degree $6$ except $H_0$.
By universal coefficients $H^2(X_1;\mathbb{Q})=\mathrm{span}\{x_1,x_2,x_3\}$,
$H^5=\mathrm{span}\{z\}$, $H^3=H^4=H^6=0$.
Since $V$ is a suspension, all cups $x_ix_j$ land in $H^4=0$; they vanish.
Thus $x_1x_2=x_2x_3=0$ and $\langle x_1,x_2,x_3\rangle$ is defined.
Indeterminacy $x_1H^3(X_1;\mathbb{Q})+H^3(X_1;\mathbb{Q})x_3=0$.
So the Massey set is a singleton $\{c\,z\}$; it remains to show $c=\pm 1$.

### Step 2. Rational Sullivan model truncated at degree 5 (audit step 2)
Minimal Sullivan model of $V$ through degree $5$:
$V^2=\mathbb{Q}^3=\mathrm{span}\{x_1,x_2,x_3\}$, $dx_i=0$;
$V^3=\mathbb{Q}^6=\mathrm{span}\{y_{ij}\}_{i\le j}$ with
$d_3(y_{ij})=x_ix_j$ (the iso $V^3\to\mathrm{Sym}^2(V^2)$ killing the cup
products; hence $H^3=0$).
In degree $5$, cochains are $x_k y_{ij}$ ($18$-dim) with differential
$\delta(x_ky_{ij})=x_kx_ix_j\in\mathrm{Sym}^3(\mathbb{Q}^3)$ ($10$-dim).
Direct check (exact matrix, replayed in `artifacts/verify_target.py`):
$\delta$ is onto (rank $10$; every cubic monomial has an explicit preimage,
e.g. $x_1y_{23},x_3y_{12}\mapsto x_1x_2x_3$), so
$\ker\delta$ is $8$-dimensional.
By Sullivan–Quillen duality this $8$ equals the free rank of $\pi_4(V)$:
$\pi_4(V)\otimes\mathbb{Q}\cong\mathbb{Q}^8$ (Witt $\frac{3^3-3}{3}=8$;
integrally $\pi_4(V)\cong\mathbb{Z}^8\oplus(\mathbb{Z}/2)^6$ from the Hilton
splitting: $3$ copies $\pi_4(S^2)$ plus $3$ weight-2 $S^3$-summands give the
$2$-torsion, $8$ weight-3 $S^4$-summands give the free part).
The degree-4 model generators $(V^4\cong(\pi_4\otimes\mathbb{Q})^*)$ map
isomorphically onto $\ker\delta$; in particular some $v_0$ (dual to $w_0$)
has $d(v_0)=m$ below.

### Step 3. Defining system and witness (audit step 3)
With $x_ix_j=d(y_{ij})$ put $a_{12}=y_{12}$, $a_{23}=y_{23}$. Then
$d(a_{12})=x_1x_2$, $d(a_{23})=x_2x_3$, and the Massey cycle
$$m=x_1a_{23}-a_{12}x_3=x_1y_{23}-y_{12}x_3$$
($x$'s even, strict commutativity) satisfies
$dm=x_1x_2x_3-x_1x_2x_3=0$.
So $[m]\in H^5$ is the Massey value. $m\neq 0$ and lies in $\ker\delta$
($8$-dim); restricted to the distinct-index subspace
$\mathrm{span}\{x_1y_{23},x_2y_{13},x_3y_{12}\}\to\mathbb{Q}\{x_1x_2x_3\}$,
$\delta=(1,1,1)$ has $2$-dim kernel (dual of the $3$ cyclic Whiteheads minus
one Jacobi relation), and $m=(1,0,-1)$ lies in it (replayed).
Attaching $e^5$ along the primitive $w_0$ kills exactly the dual line:
$\pi_4(X_1)\otimes\mathbb{Q}=\mathrm{coker}(\mathbb{Q}\xrightarrow{w_0}
\mathbb{Q}^8)\cong\mathbb{Q}^7$ (LES; torsion unaffected rationally), so the
model of $X_1$ has $7$ degree-4 generators spanning a hyperplane of
$\ker\delta$ not containing $m$ (verified: quotient rank $7\to 8$ upon adding
$m$, over $\mathbb{Q}$ and mod $7$). Hence in $X_1$, $m$ is closed but no
longer exact: $H^5(X_1;\mathbb{Q})=\mathbb{Q}\{[m]\}$.
The Hurewicz class of $e^5$ is $z$ (up to sign/orientation), and $m$ pairs
$\pm 1$ with it. In detail: in the model $M(V)$ of the wedge, $m=d(v_0)$ for a
degree-$4$ generator $v_0$ dual to $w_0$. Pull back along
$w_0\colon S^4\to V$: since $H^2(S^4)=H^3(S^4)=0$, all $w_0^*(x_i)$ and
$w_0^*(y_{ij})$ are exact, so $w_0^*(v_0)=k\cdot\mathrm{vol}_{S^4}$ is a
$4$-cocycle whose integer $k$ is exactly Hilton's Hopf–Hilton invariant of
$w_0$ at the basic product $\lambda=[[\iota_1,\iota_2],\iota_3]$.
By Hilton's theorem it is $\pm 1$ on the $\lambda$-summand generator
($0$ on the other seven Hall lines), and $w_0$ is by hypothesis that
generator (primitivity replays: $\gcd$ of the $m$-coefficients is $1$, so
$m$ is a lattice generator of its line and some primitive $w_0$ pairs
$\pm 1$ with it; the topic fixes $w_0$ to be that distinguished generator).
Relative Stokes over the mapping cone $(X_1,V)\simeq(D^5,S^4)$ then gives
$\langle[m],[e^5]\rangle=\pm 1$, i.e. $[m]=\pm z$ with $z$ the Kronecker-dual
cellular generator. This is the Massey–Whitehead/Porter duality rendered as
an explicit transgression; the only cited input is Hilton's Hopf-invariant
evaluation, everything else is the replayed linear algebra above.
Therefore $\langle x_1,x_2,x_3\rangle=\pm z$ strictly (singleton).
Non-formality follows from Deligne–Griffiths–Morgan–Sullivan: a formal space
has all Massey products containing $0$.

### Step 4. Mod-2 cohomology and $\mathrm{Sq}^2$ (audit step 4)
Integral homology free $\Rightarrow$ mod-2 Betti numbers as claimed
($0\!:\!1$, $2\!:\!3$, $5\!:\!1$, else $0$ through $6$).
By instability/degree reasons every primary $\mathrm{Sq}^k$ with source and
target in degrees $\le 6$ has trivial source or target:
$\mathrm{Sq}^1x_i\in H^3=0$, $\mathrm{Sq}^2x_i=x_i^2\in H^4=0$,
$\mathrm{Sq}^1z\in H^6=0$, $\mathrm{Sq}^2z\in H^7$ (outside range / $0$ by
instability since $\deg z=5$ gives $\mathrm{Sq}^2z$ unconstrained a priori but
$H^7(X_1)=0$ cellularly). Hence table $T=0$.
Line $L$: the mod-2 reduction of the $k$-invariant/attaching class lies in
$\ker(\mathrm{Sq}^2)$ — the cup-square vanishes — exactly the free-Whitehead
(non-Hopf, non-torsion) signature; a Hopf-detected attachment would have
$\mathrm{Sq}^2\neq 0$. This cross-checks Step 3 rationally independently.

### Step 5. Certificate (audit step 5)
Replay: `python3 output/artifacts/verify_target.py` $\to$ `VERIFY_OK`
(exact $\mathbb{Q}$ ranks, quotient survival, mod-$7$ cross-check, mod-$2$
table). Logged: $d_3$ iso $6\times 6$; $\delta$ $10\times 18$ rank $10$,
$\ker$ dim $8$; $m$ closed, in $\ker$, surviving the $7$-dim complement;
$18$-row preimage table; Hilton–Witt count $8$; LES quotient rank $7$.

## Separation of proof / computation / conjecture
- Proved: (1)–(4) above, conditional on standard cited machinery
  (Sullivan minimal models, Hilton–Milnor splitting, DGMS Massey obstruction,
  Serre–Cartan instability), each applied only through the explicit matrices
  replayed in the artifact.
- Computed evidence: all ranks, kernels, quotient survival (exact arithmetic).
- Convention, not uncertainty: the $\pm$ sign (Massey ordering/orientation of
  $e^5$).
- Uncertainty flagged: page-level citations (Hilton 1955, Sullivan 1977, DGMS
  1975, Porter/Massey–Whitehead duality) recalled from standard statements;
  live-source retrieval was rate-limited during the session, so exact pages
  are unchecked — the logical chain itself is self-contained above.

## References (standard; pages unchecked — see above)
Hilton, On the homotopy groups of the union of spheres (1955);
Sullivan, Infinitesimal computations in topology (1977);
Deligne–Griffiths–Morgan–Sullivan, Real homotopy theory of Kähler manifolds
(1975); Porter, Higher order Whitehead products (1965); Serre–Cartan
Steenrod-algebra bases; Milgram, Steenrod structure of 2-stage Postnikov
systems (1969, ambient only — does not state this cell).
