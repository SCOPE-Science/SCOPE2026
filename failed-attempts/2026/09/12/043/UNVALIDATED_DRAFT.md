# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Nichols algebra of the D8 reflection pair V2+W2: diagonalisation, relations, dimension 64

Basis: $a=e_s$, $b=e_{r^2s}$, $c=f_{rs}$, $d=f_{r^3s}$; $e_0=a+b$, $e_1=a-b$,
$e_2=c+d$, $e_3=c-d$. Base field algebraically closed, char $0$ (exact
rational checks; mod-prime cross-checks at $p=1000003,1000033,1000037$).

## 1. Braiding and diagonalisation

YD action (coset reps $x^V_s=1$, $x^V_{r^2s}=rs$, $x^W_{rs}=1$, $x^W_{r^3s}=s$):

$$s,\ r^2s:\ a\mapsto -a,\ b\mapsto -b,\ c\leftrightarrow d\ (+1),\qquad
rs,\ r^3s:\ a\leftrightarrow b\ (+1),\ c\mapsto -c,\ d\mapsto -d.$$

Hence, with $c(x\otimes y)=x_{(-1)}\cdot y\otimes x_{(0)}$:

$$\begin{aligned}
c(aa)&=-aa & c(ab)&=-ba & c(ac)&=+db & c(ad)&=+cb\\
c(ba)&=-ab & c(bb)&=-bb & c(bc)&=+da & c(bd)&=+ca\\
c(ca)&=+bd & c(cb)&=+ad & c(cc)&=-cc & c(cd)&=-dc\\
c(da)&=+bc & c(db)&=+ac & c(dc)&=-cd & c(dd)&=-dd.
\end{aligned}$$

The basis $e_0=a+b$, $e_1=a-b$, $e_2=c+d$, $e_3=c-d$ diagonalises $c$
monomially (exact check in `compute_braiding.py`):

$$c(e_i\otimes e_j)=q_{ij}\,e_j\otimes e_i,\qquad
q=\begin{pmatrix}-1&-1&+1&-1\\-1&-1&+1&-1\\+1&-1&-1&-1\\+1&-1&-1&-1\end{pmatrix}.$$

Yang-Baxter $c_1c_2c_1=c_2c_1c_2$ on $V^{\otimes3}$ verified exactly.
All $q_{ii}=-1$; $q_{ij}q_{ji}=+1$ on
$\{01,02,13,23\}$ and $-1$ on $\{03,12\}$. Cartan matrix:

$$A=\begin{pmatrix}2&0&0&-1\\0&2&-1&0\\0&-1&2&0\\-1&0&0&2\end{pmatrix},$$

Dynkin diagram $A_2\times A_2$ with components $\{e_0,e_3\}$ and $\{e_1,e_2\}$.

## 2. Quadratic Nichols relations (ledger)

$\ker(1+c)\subset V^{\otimes2}$ has exact dimension $8$ (sympy QQ rank 8/16).
In the $e$-basis the following $8$ independent relations span it
(independence: expanded $8\times16$ matrix has rank $8$; each lies in the
kernel by exact $S_2$-test after expansion to the old basis):

- $4$ squares: $e_i^2=0$ ($i=0,\dots,3$);
- $4$ $q$-commutators on disconnected pairs:
  $e_0e_1+e_1e_0=0$, $e_0e_2-e_2e_0=0$, $e_1e_3+e_3e_1=0$, $e_2e_3+e_3e_2=0$.

## 3. Serre and root-vector relations (ledger)

(a) Quantum Serre: for the two $A_2$ edges, with diagonal braided adjoint
$\mathrm{ad}_{e_i}(x)=e_ix-q_{i,\deg x}\,x\,e_i$:

$$\mathrm{ad}_{e_0}^2(e_3)=e_0^2e_3-(1+q_{00})e_0e_3e_0+q_{00}q_{03}e_3e_0^2
\ \text{etc.}$$

i.e. tensors $(0,0,3)-(3,0,0)$, $(3,3,0)-(0,3,3)$, $(1,1,2)-(2,1,1)$,
$(2,2,1)-(1,2,2)$, each verified in $\ker S_3$ exactly (expanded to old basis).

(b) Root vectors $z_{03}=e_0e_3+e_3e_0$ ($-q_{03}=+1$) and
$z_{12}=e_1e_2-e_2e_1$ ($-q_{12}=-1$) are nonzero in $B_2$
($S_2$-images have $4$ nonzero entries) with self-braidings
$q(z_{03},z_{03})=q(z_{12},z_{12})=-1$ (exact $N^4$-degree computation) and

$$z_{03}^2=0,\qquad z_{12}^2=0\quad\text{in }B_4\ (\text{exact }\ker S_4\text{ test}).$$

(c) Cross relations (exact kernel tests): $e_k$ $q$-commutes with the opposite
root vector and the two root vectors $q$-commute:

$$\begin{aligned}
e_1z_{03}-z_{03}e_1&=0, & e_2z_{03}+z_{03}e_2&=0,\\
e_0z_{12}+z_{12}e_0&=0, & e_3z_{12}-z_{12}e_3&=0,\\
z_{03}z_{12}+z_{12}z_{03}&=0,
\end{aligned}$$
in $B_3$ (first four) and $B_4$ (last), with $q$-factors read off total
$N^4$-degrees, e.g. $q(e_1,z_{03})=q_{10}q_{13}=+1$.

## 4. Dimension

Exact QQ symmetrizer ranks: $\dim B_1=4$, $\dim B_2=8$, $\dim B_3=12$,
$\dim B_4=14$ (sympy `.rank()` on $S_n$; $S_4$ is $256\times256$).
Per-multidegree diagonal blocks (float SVD $+$ mod-$p$ elimination agreeing):
$\dim B_5=12$ (3 large primes), $\dim B_6=8$, $\dim B_7=4$
(float and mod-$1000003$ agree; only top blocks
$(1,2,2,2)$-type survive with rank $1$ each).
Each $A_2$ factor ($q=\bigl(\begin{smallmatrix}-1&-1\\+1&-1\end{smallmatrix}\bigr)$
resp. $\bigl(\begin{smallmatrix}-1&+1\\-1&-1\end{smallmatrix}\bigr)$) has exact
factor ranks $1,2,2,2,1,0$ for $n=0,\dots,5$ (sympy), i.e. Hilbert series
$(1+t)^2(1+t^2)$ per factor, dimension $8$ per factor.
The two factors $q$-commute, so with convex orders $e_0<z_{03}<e_3$ and
$e_1<z_{12}<e_2$ the PBW monomials

$$e_0^{a_0}z_{03}^{a_{03}}e_3^{a_3}\,e_1^{a_1}z_{12}^{a_{12}}e_2^{a_2},
\qquad a_\bullet\in\{0,1\}$$

give $2^6=64$ PBW words. Their $N$-degrees give Hilbert series
$(1+t)^4(1+t^2)^2=1+4t+8t^2+12t^3+14t^4+12t^5+8t^6+4t^7+t^8$, matching every
computed symmetrizer rank ($1,4,8,12,14,12,8,4$ for $n=0,\dots,7$), hence the
relations above are complete and $\dim B(V_2\oplus W_2)=64$, concentrated in
degrees $0$--$8$.

## 5. Scripts and reproducibility

`output/artifacts/compute_braiding.py` (run: `python3 output/artifacts/compute_braiding.py`)
recomputes everything exact over QQ: YD table, $c$, Yang-Baxter, $q$-matrix,
Cartan matrix, $\ker S_2$ basis, all relation kernel memberships, exact ranks
$S_1$--$S_4$ and factor ranks; writes `output/artifacts/ledger.json`.
Multidegree tail ranks $n=5,6,7$ use float SVD cross-checked by mod-prime
elimination (three primes at $n=5$; one prime plus float agreement at $n=6,7$).
Char $0$ is used: divisions by $2$ (diagonal basis) and by $n!$ (symmetrizers).
