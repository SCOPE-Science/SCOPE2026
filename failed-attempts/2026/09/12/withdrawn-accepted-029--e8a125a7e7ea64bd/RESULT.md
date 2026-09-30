# Doubled rotation-class Nichols algebra over D8 is the 16-dimensional exterior algebra

## Context

Let $k$ be algebraically closed of characteristic zero and
$D_8=\langle r,s\mid r^4=s^2=1,\ srs=r^{-1}\rangle$, $|D_8|=8$.
The rotation class $\mathcal O_r=\{r,r^3\}$ has centralizer
$C(r)=\langle r\rangle\cong C_4$. Let $\xi:\langle r\rangle\to k^\times$,
$\xi(r)=-1$ (order two), $X=M(\mathcal O_r,\xi)$ the associated
2-dimensional simple Yetter–Drinfeld module, and $U_3=X\oplus X$
($\dim U_3=4$). The admitted target asked whether $\mathcal B(U_3)$ is
infinite-dimensional via an explicit affine Cartan diagonal subsystem
(or minimal infinite Weyl-groupoid word), or finite-dimensional with a
complete Cartan graph and Nichols-relation ledger.

## Definitions

Fix the section $t_r=1$, $t_{r^3}=s$ (valid since $srs^{-1}=r^3$).
Write the basis $x_1=a_1$, $x_2=b_1$ (first copy), $x_3=a_2$, $x_4=b_2$
(second copy) with degrees $\deg(x_1)=\deg(x_3)=r$,
$\deg(x_2)=\deg(x_4)=r^3$. For diagonal braidings write
$c(x_i\otimes x_j)=q_{ij}\,x_j\otimes x_i$ and
$\widetilde q_{ij}=q_{ij}q_{ji}$. Generalized Cartan entries are
$a_{ii}=2$ and
$a_{ij}=-\min\{m\ge 0:(m+1)_{q_{ii}}(1-q_{ii}^m\widetilde q_{ij})=0\}$.

## Result

$\mathcal B(U_3)$ is finite-dimensional of dimension $16$, the exterior
algebra on its 4-dimensional space. The target infinitude claim is
false. Precisely:

- The full $4\times 4$ braiding-scalar matrix is uniformly $-1$:
  $c(x_i\otimes x_j)=-x_j\otimes x_i$ for all $i,j$ ($c=-\tau$).
- The generalized Cartan matrix is $A=I_4$, Dynkin type
  $A_1^{\times 4}$ (four isolated $(-1)$-nodes), positive-definite,
  $\det A=1$.
- Every nonempty diagonal subset-subsystem ($2^4-1=15$) has Cartan
  $I_k$, finite type $A_1^k$; no affine diagram occurs.
- The Weyl groupoid has a single object with Weyl group
  $(\mathbb Z/2)^4$ of order $16$; the longest word has length $4$; no
  infinite reduced word exists.
- $\dim\mathcal B(U_3)=2^4=16$,
  $\mathrm{Hilb}(t)=(1+t)^4=1+4t+6t^2+4t^3+t^4$.
- Defining relations: $x_i^2=0$ ($4$) and $x_ix_j+x_jx_i=0$ ($6$),
  $10$ quadratic relations spanning $\ker S_2$ (nullity $10$).
- PBW basis $\{x_1^{e_1}x_2^{e_2}x_3^{e_3}x_4^{e_4}:e_i\in\{0,1\}\}$.

## Proof / evidence

Model $D_8$ as pairs $(i,j)$, $r^is^j$, with
$(i_1,j_1)(i_2,j_2)=(i_1+(-1)^{j_1}i_2,j_1+j_2)$.
Machine verification confirms $r^4=s^2=1$, $srs^{-1}=r^3$, and the
centralizer of $r$ is $\{(i,0)\}$, size $4$. The character
$\xi(r^i)=(-1)^i$ gives $\xi(r)=\xi(r^3)=-1$, $\xi(r^2)=+1$.
For $h\in D_8$, $u\in\mathcal O_r$, decomposing $hu=t_{u'}c$ gives:
$r$ and $r^3$ fix both fibers with coefficient $-1$; $s$ swaps fibers
with $+1$; $r^2$ fixes with $+1$. Since
$\deg(x_i)\in\{r,r^3\}$ centralize $\mathcal O_r$ pointwise,
$c(x_i\otimes x_j)=\deg(x_i)\triangleright x_j\otimes x_i=-x_j\otimes x_i$.
The script checks all $16$ pairs, yielding $q$ all $-1$.
Then $q_{ii}=-1$, $\widetilde q_{ij}=1$ ($i\ne j$) gives
$1-\widetilde q_{ij}=0$ at $m=0$, hence all $a_{ij}=0$ ($i\ne j$) and
$A=I_4$. All subset subsystems and reflection invariance are enumerated.
By Heckenberger's classification of arithmetic root systems /
finite-dimensional diagonal Nichols algebras (Invent. Math. 164 (2006);
Adv. Math. 220 (2009)), Cartan type $A_1^4$ with $q_{ii}=-1$ gives root
system $\{\alpha_1,\dots,\alpha_4\}$ each of height
$N_i=\mathrm{ord}(q_{ii})=2$, so dimension $2^4=16$, equivalently
$\mathcal B(U_3)=\Lambda(V)$ since $c=-\tau$.
Quantum-symmetrizer check: $\mathrm{rank}\,S_2=6=\binom42$,
$\mathrm{rank}\,S_3=4=\binom43$, matching exterior slices.

## Limitations

Computations assume the stated algebraically closed characteristic-zero
setting so $\xi(r)=-1$ has order two. The final dimension count cites
Heckenberger's classification rather than re-proving it. No other $D_8$
classes or characters were analyzed.

## Reproducibility

```
python3 output/artifacts/braiding_cartan.py
python3 output/artifacts/quantum_symmetrizer.py
```

## References

- Andruskiewitsch–Schneider, Pointed Hopf algebras (AMS, 2002):
  $M(\mathcal O,\rho)$, braiding formula.
- Heckenberger, Weyl groupoid of a Nichols algebra of diagonal type,
  Invent. Math. 164 (2006); Classification of arithmetic root systems,
  Adv. Math. 220 (2009).
- Fantino–García, On pointed Hopf algebras over dihedral groups,
  Pacific J. Math. 252 (2011); scope $m=4t$, $t\ge 3$, hence excluding
  $D_8$ — contrasted for originality.
- Andruskiewitsch–Fantino, On pointed Hopf algebras associated with
  alternating and dihedral groups, arXiv:math/0702559: $D_n$
  irreducible table; no doubled $D_8$ entry.
- García–Vay, Simple modules of small quantum groups at dihedral
  groups, arXiv:2012.09323 / Documenta Math. 29 (2024), Theorem 4.5.
