# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Two-term free-energy expansion for the two-periodic Aztec diamond

## 1. Model and result (scoped)

Let $Z_n(a)$ be the dimer partition function of the order-$n$ Aztec diamond with
2-periodic weights in the Chhita–Johansson convention: with Kasteleyn coordinates
$W=\{(i,j):i$ odd, $j$ even$\}$, $B=\{(i,j):i$ even, $j$ odd$\}$, every edge inside
the face $(i,j)$ (the $4$-cycle with corners $B(2i,2j{+}1)$, $W(2i{+}1,2j)$,
$B(2i{+}2,2j{+}1)$, $W(2i{+}1,2j{+}2)$) carries weight $a$ if $i{+}j$ is even and
weight $1$ if $i{+}j$ is odd (faces are checkerboard-uniform; Kasteleyn signs as in
Chhita–Johansson (2.3) with $b=1$). Faces are edge-disjoint: every edge lies in
exactly one face. The Aztec region is simply connected, so Kasteleyn's theorem
gives $Z_n(a)=|\det K_{a,1}|$ with a single Pfaffian; at $a=1$ this reproduces
$Z_n=2^{n(n+1)/2}$.

**Theorem (closed-form free-energy constants).** For every fixed $0<a<1$ (indeed
every $a>0$),
$$\frac1{n^2}\log Z_n(a)=F_0(a)+\frac{F_1(a)}n+o\!\left(\frac1n\right),
\qquad n\to\infty,$$
with explicit closed forms
$$F_0(a)=\tfrac14\log\!\big(2a(1{+}a^2)\big),\qquad F_1(a)=\tfrac12\log(2a).$$
In fact, with $Z_0:=1$,
$$\log Z_n(a)=F_0(a)\,n^2+F_1(a)\,n+C_{\,n\bmod 4}(a)\qquad(n\ge 0),$$
where $C_0=C_2=0$, $C_3=F_1-F_0$, $C_1=F_1-F_0+\log a$, so the remainder after the
two-term expansion is $O(1/n^2)$ along the full sequence with a single $F_1$.

*Scope.* The constants $F_0,F_1$ are identified here in closed form and checked
against Elkies–Kuperberg–Larsen–Propp at $a=1$ ($F_0=F_1=\tfrac12\log2$); a
separate derivation identifying $F_0$ with the Ronkin surface-tension integral,
resp. $F_1$ with the arctic-curve boundary constant, is not undertaken — the
theorem is scoped to the closed-form constants. All verification scripts are
retained (`artifacts/`).

## 2. Corrected four-step factor

Write face weights as $(x,y)$ and put $E(m)=\lceil m^2/2\rceil$,
$O(m)=\lfloor m^2/2\rfloor$. A face stores its four edge weights as
$(w_{00},w_{01},w_{10},w_{11})$ (edges $B_1W_1,B_1W_2,B_2W_1,B_2W_2$); the cyclic
order around the face is $(w_{00},w_{10},w_{11},w_{01})$, so the urban-renewal
cell factor for cyclic $(a,b,c,d)$ is $\Delta=ac+bd$. For $n\ge 4$,
$$\frac{Z_n(x,y)}{Z_{n-4}(x,y)}=K_n(x,y),\tag{$\star$}$$
$$K_n=(2x^2)^{E(n)}(2y^2)^{O(n)}(p^2{+}q^2)^{(n-1)^2}
(2X^2)^{E(n-2)}(2Y^2)^{O(n-2)}(P^2{+}Q^2)^{(n-3)^2}\lambda^{(n-4)(n-3)},$$
$$(p,q)=\Bigl(\frac1{2x},\frac1{2y}\Bigr),\quad
(X,Y)=T(x,y)=\Bigl(\frac{2xy^2}{x^2+y^2},\frac{2x^2y}{x^2+y^2}\Bigr),\quad
(P,Q)=\Bigl(\frac1{2X},\frac1{2Y}\Bigr),\quad
\lambda=\frac{4x^2y^2}{(x^2+y^2)^2}.$$
Correction: the cross-face pass contributes $(p^2{+}q^2)^{m^2}$ (cell factor
$\Delta=p^2+q^2$ for cyclic $(p,q,p,q)$), not $(2pq)^{m^2}$. At $(x,y)=(a,1)$,
$$K_n(a)=(4a^2)^{\,n-1}(1+a^2)^{\,2n-4}\qquad(n\ge 4),$$
i.e. $\log K_n(a)=(n{-}1)\log(4a^2)+(2n{-}4)\log(1{+}a^2)$, verified against exact
determinants to $\sim 10^{-13}$ (`verify_closedform.py`, `verify_double_step.py`).
Coefficient check: with $M=\log(2a)$, $N=\log(1+a^2)$,
$p^2{+}q^2=(1{+}a^2)/(4a^2)$, $2X^2=8a^2/(1{+}a^2)^2$,
$2Y^2=8a^4/(1{+}a^2)^2$, $P^2{+}Q^2=(1{+}a^2)^3/(16a^4)$,
$\lambda=4a^2/(1{+}a^2)^2$, collecting $\log2$, $M$-free $\log a$, $N$ parts and
using $E(k)+O(k)=k^2$ gives exactly $(2n{-}2)\log2+(2n{-}2)\log a+(2n{-}4)N$.
At $a=1$: $K_n=2^{4n-6}=Z_n/Z_{n-4}$, recovering E-K-L-P.

## 3. Proof by domino shuffling for general $m$

Moves: urban-renewal spider at a face, pendant removal (factor = pendant-edge
weight), degree-2 contraction (exact when both edges have weight 1), vertex gauge.
$Z^U_m(x,y)$: uniform checkerboard faces; $Z^C_m(p,q)$: cross faces
$(p,q,q,p)$ on even, $(q,p,p,q)$ on odd faces (storage order).

*Face counts.* Row $j$ has faces $(i,j)$, $0\le i<m$, even iff $i\equiv j\pmod2$;
summing rows gives $\#\mathrm{even}=E(m)=\lceil m^2/2\rceil$,
$\#\mathrm{odd}=O(m)=\lfloor m^2/2\rfloor$.

**Lemma 1 ($U\to C$, general $m$).** Spidering all $m^2$ uniform faces gives
$$Z^U_m(x,y)=(2x^2)^{E(m)}(2y^2)^{O(m)}\,
Z^C_{\,m-1}\!\Bigl(\frac1{2x},\frac1{2y}\Bigr).$$
*Proof.* A uniform face has $\Delta=2x^2$ (even) resp. $2y^2$ (odd); with the
opposite-edge wiring the four inner-square edges all equal $x/\Delta=1/(2x)$
resp. $1/(2y)$; legs have weight $1$. Reduction cascade: (i) the $4m$ boundary
tips each retain only their leg, so they are pendant; removing tip${}+{}$partner
pairs costs the leg weight $1$ each; (ii) exposed originals keep only legs
(their face-edges were all consumed by spiders), so subsequent degree-2
contractions are along two legs of weights $(1,1)$, factor $1$; the cascade moves
one layer inward until the Aztec$_{m-1}$ on inner vertices remains. Surgery
invariant: a vertex becomes pendant only along its leg (square edges are deleted
solely when a square-neighbour is removed as a partner), and no contraction ever
uses a square edge — hence total surgery factor $f=1$ and no gauge is needed,
the surviving inner edges already reading $(1/(2x),1/(2y))$. Face regrouping:
each surviving interior original lies in exactly two parent faces of opposite
parity (e.g. $B(2i,2j{+}1)$ in faces $(i,j),(i{-}1,j)$ of opposite parity), so the
new face there takes two inner edges from each parent, i.e. cross faces
$(p,q,q,p)$ on even and $(q,p,p,q)$ on odd positions. The reduction pattern was
additionally verified by explicit face census and graph isomorphism
(`iso2.py`, `twostep2.py`, `outer.py`). ∎

**Lemma 2 ($C\to U$, general $m$; corrected).** A cross face in storage order
$(p,q,q,p)$ is cyclic $(p,q,p,q)$, so $\Delta=p\cdot p+q\cdot q=p^2+q^2$;
spidering all $m^2$ faces gives
$$Z^C_m(p,q)=(p^2+q^2)^{m^2}\,
Z^U_{\,m-1}\!\Bigl(\frac{p}{p^2+q^2},\frac{q}{p^2+q^2}\Bigr).$$
*Proof.* Same cascade as Lemma 1 (legs weight $1$, surgery invariant, $f=1$, no
gauge); inner-square edges are $(p,q,p,q)/(p^2{+}q^2)$, and regrouping at old
vertices yields uniform faces with values $p/(p^2{+}q^2)$ (even) and
$q/(p^2{+}q^2)$ (odd), verified by face census (`fam2.py`: uniform faces
$1.08532\ldots=p/(p^2{+}q^2)$, $0.58440\ldots=q/(p^2{+}q^2)$ at the test point).
The previous draft's factor $(2pq)^{m^2}$ was incorrect and is replaced. ∎

*Two-step map and closure.* $U\to C\to U$ gives
$Z^U_m(x,y)=(2x^2)^{E(m)}(2y^2)^{O(m)}(p^2{+}q^2)^{(m-1)^2}Z^U_{m-2}(X,Y)$ with
$(X,Y)=T(x,y)$ since $(1/(2x),\,(1/(4x^2))+(1/(4y^2))^{-1}\!\cdot)$ simplifies to
$2xy^2/(x^2{+}y^2)$, resp. $2x^2y/(x^2{+}y^2)$. With $D=x^2{+}y^2$,
$S=X^2{+}Y^2=4x^2y^4/D^2+4x^4y^2/D^2=4x^2y^2/D$, and
$X_2=2XY^2/S=16x^5y^4D^{-3}/(4x^2y^2D^{-1})=4x^3y^2/D^2=\lambda x$,
$Y_2=\lambda y$, i.e.
$$T^2(x,y)=\lambda(x,y)\,(x,y),\qquad \lambda=4x^2y^2/(x^2{+}y^2)^2,$$
the period-4 return of the two-periodic orbit (Chhita–Young); also verified
symbolically (`verify_double_step.py`).

*Homogeneity.* Every tiling has exactly as many dimers as white vertices, and
$\#W=m(m+1)$ (the Kasteleyn matrix is $m(m+1)\times m(m+1)$, checked for
$m\le5$ in `verify_double_step.py`), so
$Z^U_m(tx,ty)=t^{m(m+1)}Z^U_m(x,y)$; the scale $\lambda$ from $T^2$ is absorbed
as $\lambda^{(n-4)(n-3)}$, completing $(\star)$ and hence $K_n(a)$.

**Induction.** Base values $Z_0=1$, $Z_1=2a^2$ (single $4$-cycle: two matchings of
weight $a^2$), $Z_2=4a^2(1+a^2)$, $Z_3=16a^4(1+a^2)^2$; with $Z_n=K_nZ_{n-4}$,
for $n=4k+r$,
$$\log Z_n=\sum_{j=1}^k\log K_{4j+r}+\log Z_r
=F_0n^2+F_1n-\frac{r(r+2)}4M-\frac{r^2}4N+\log Z_r,$$
$M=\log(2a)$, $N=\log(1+a^2)$, and
$\log Z_r=\frac{r(r+2)}4M+\frac{r^2}4N+C_r$ holds for $r=0,1,2,3$ by the base
values. Dividing by $n^2$ gives the Theorem.

## 4. Checks

- Single-spider $Z=\Delta Z'$ proved by matching enumeration and validated by
  brute force (`validate_ops.py`); all four inner wirings preserve $Z$
  (`shifttest.py`).
- $(\star)$, $K_n(a)$, and the exact closed form verified to $\sim10^{-13}$ for
  $a\in\{0.2,0.3,0.5,0.7,0.9,1.3\}$, $n\le12$ (`verify_closedform.py`,
  `verify_Kn2.py`, `verify_double_step.py`).
- Equivalent Kuo-type form $Z_nZ_{n-2}/Z_{n-1}^2=R_{\,n\bmod4}$,
  $R_0=1+a^2$, $R_1=R_3=2a^2$, $R_2=(1+a^2)/a^2$ (all $2$ at $a=1$).
- Convention note: results are in the face-checkerboard $(1,a)$ normalization;
  other $(1,a)$ normalizations differ by an explicit monomial gauge.
