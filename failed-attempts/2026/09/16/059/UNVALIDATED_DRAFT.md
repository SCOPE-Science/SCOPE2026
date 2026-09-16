# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# No irreducible hyperfinite A-infinity subfactor at index ~5.04892

## Target claim and answer

**Target.** Does there exist an irreducible hyperfinite subfactor $N \subset M$
(of / of the hyperfinite II$_1$ factor) with Jones index
$\lambda_0 \approx 5.04892$, the largest root of $x^3-6x^2+5x-1$,
and standard invariant Temperley--Lieb--Jones (both principal graphs
$A_\infty$, i.e.\ infinite depth with trivial standard invariant)?

**Answer (TARGET resolution by disproof). No.** Such a subfactor does not exist.
The abstract Temperley--Lieb--Jones planar algebra at loop parameter
$\delta_0=\sqrt{\lambda_0}>2$ exists, so there is no planar-algebraic
obstruction; the obstruction is exactly hyperfiniteness, via Popa's
amenability theorem: a finite-index hyperfinite inclusion with graph
$A_\infty$ must have index $\|A_\infty\|^2=4$, whereas $\lambda_0\in(5,6)$.

## Theorem

There is no irreducible inclusion $N\subset M$ of hyperfinite II$_1$ factors
(in particular no irreducible finite-index $N\subset R$ with $R$ the
hyperfinite II$_1$ factor) of index $\lambda_0$ with principal graphs
$(A_\infty,A_\infty)$, where $\lambda_0$ is the largest root of
$p(x)=x^3-6x^2+5x-1$.

## Proof

### Lemma 1 (location of $\lambda_0$; exact integer arithmetic).

$p(5)=125-150+25-1=-1<0$ and $p(6)=216-216+30-1=29>0$.
$p'(x)=3x^2-12x+5$ satisfies $p'(5)=20>0$ and $p''(x)=6x-12>0$ for $x\ge 5$,
so $p'$ is strictly increasing on $[5,\infty)$ hence $p'>0$ there, so $p$ is
strictly increasing on $[5,\infty)$. By the intermediate value theorem there
is exactly one root in the open interval $(5,6)$, and monotonicity plus
$p(6)>0$ excludes any root $\ge 6$; hence this root is the largest root:
$\lambda_0\in(5,6)$. In particular $\lambda_0>4$ and $\lambda_0\ne 4$.
Consequently $\delta_0:=\sqrt{\lambda_0}\in(\sqrt5,\sqrt6)\subset(2,2.5)$
(since $5>2^2$ and $6<25/4$), so $\delta_0>2$.
Certified by exact integer evaluations in `artifacts/verify_lambda0.py`.

### Lemma 2 (the graph norm $\|A_\infty\|=2$).

Let $\Delta$ be the adjacency operator of the half-line graph $A_\infty$
(vertices $0,1,2,\dots$, edges $n\sim n+1$) on $\ell^2(\mathbb N_0)$.
Upper bound: for a unit vector $\xi$,
$|\langle\xi,\Delta\xi\rangle|\le 2\sum_n|\xi_n||\xi_{n+1}|
\le\sum_n(|\xi_n|^2+|\xi_{n+1}|^2)\le 2\|\xi\|^2$,
so $\|\Delta\|\le 2$ (max-degree bound).
Lower bound: compression to the first $n$ vertices is the finite-path
adjacency $A_n$, whose norm is $2\cos(\pi/(n+1))$ (eigenvalues
$2\cos(k\pi/(n+1))$; see e.g.\ Goodman--de la Harpe--Jones,
*Coxeter graphs and towers of algebras*). Since corner compression does not
increase norm, $\|A_\infty\|\ge 2\cos(\pi/(n+1))$ for every $n$; letting
$n\to\infty$ gives $\|A_\infty\|\ge 2$. Hence $\|A_\infty\|=2$ and
$\|A_\infty\|^2=4$. (Numerically, $2\cos(\pi/(n+1))\nearrow 2$ is tabulated
in the artifact script.)

### Lemma 3 (hyperfinite + $A_\infty$ forces index $4$).

Suppose, for contradiction, $N\subset M$ is irreducible, both factors
hyperfinite (this covers both readings: $M=R$, or $N,M\cong R$), with
$[M:N]=\lambda_0<\infty$ and principal graph $A_\infty$.
Finite-index irreducible implies extremal (the two canonical traces agree
trivially on $N'\cap M=\mathbb C$). By Popa's amenability theorem
(S.\ Popa, *Classification of amenable subfactors of type II*,
Acta Math.\ 172 (1994), 163--255, \S\S 4--5; see also the textbook
expositions in Evans--Kawahigashi and Jones--Sunder):
(i) a finite-index inclusion with $M$ hyperfinite (injective) is an amenable
subfactor; (ii) an amenable extremal finite-index subfactor satisfies
$[M:N]=\|\Gamma\|^2$ where $\Gamma$ is the principal graph.
With $\Gamma=A_\infty$, Lemma 2 gives $[M:N]=4$.

### Contradiction.

Lemma 3 forces $[M:N]=4$, but Lemma 1 gives $[M:N]=\lambda_0\in(5,6)$,
absurd. Hence no such irreducible hyperfinite subfactor exists. Finite index
is essential and holds ($\lambda_0\approx 5.0489$); irreducibility is used
only to get extremality. This is a complete TARGET resolution
(rigorous impossibility proof). No literature search was used; the cited
Popa/Jones/GHJ theorems are standard black boxes.

## Remarks (context, not load-bearing)

1. There is no obstruction at the abstract planar-algebra level: for every
$\delta>2$ the Temperley--Lieb--Jones C$^*$-planar algebra $TLJ(\delta)$
exists (Jones) with principal graphs $(A_\infty,A_\infty)$; here
$\delta_0\approx 2.247>2$. The obstruction is specifically realization by a
hyperfinite inclusion.
2. Relatedly, $TLJ(\delta)$ for $\delta>2$ is realized by (necessarily
non-hyperfinite, non-amenable-realiz\-ing) subfactors in general
(reconstruction/embedding theorems); the index $\approx 5.0489$ itself is an
admissible Jones index ($>4$, continuous range). So the negative answer says
precisely: the $A_\infty$ standard invariant at this index cannot sit inside
the hyperfinite world.
3. For comparison, the hyperfinite $A_\infty$ subfactor does exist at index
$4$ ($\|A_\infty\|^2=4$), consistent with Lemma 3.

## Self-checks performed

- [x] Integer-exact certification: $p(5)=-1$, $p(6)=29$, monotonicity on
$[5,\infty)$ via $p',p''$ sign analysis; largest-root claim justified
(no roots $\ge 6$). Script: `artifacts/verify_lambda0.py` (ran clean).
- [x] $\delta_0$ bounds from pure integer comparisons
($5>4$, $6<25/4$); no floating-point trust needed for any logical step.
- [x] $\|A_\infty\|=2$ proved from both sides (row-sum/AM--GM upper bound;
$A_n$-corner lower bound with the classical $2\cos(\pi/(n+1))$ formula).
- [x] Irreducible $\Rightarrow$ extremal and Popa (i)+(ii) chain stated with
exact hypotheses; both readings of "hyperfinite subfactor" covered.
- [x] No overclaim: abstract $TLJ(\delta_0)$ existence and general
non-hyperfinite realizability are flagged as context, not proved here; the
impossibility of the *hyperfinite* realization is what is proved.
