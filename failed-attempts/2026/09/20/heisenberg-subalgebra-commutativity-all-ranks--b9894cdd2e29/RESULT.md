# Exact subalgebra commutativity degrees for finite Heisenberg Lie algebras

## Statement

Let \(q\) be a prime power and let
\[
H_m(q)=V\oplus \mathbb F_q z,\qquad \dim_{\mathbb F_q}V=2m,
\]
be the \((2m+1)\)-dimensional Heisenberg Lie algebra, with
\[
[v,w]=\omega(v,w)z,
\]
where \(\omega\) is a nondegenerate alternating form on \(V\).  Write
\[
\binom nk_q
\]
for the Gaussian binomial coefficient, and let
\[
I_{m,r}(q)
 =\binom mr_q\prod_{i=0}^{r-1}(q^{m-i}+1)
 =\frac{\prod_{i=m-r+1}^{m}(q^{2i}-1)}{\prod_{i=1}^{r}(q^i-1)}
\]
be the number of totally isotropic \(r\)-subspaces of a symplectic \(2m\)-space.  Put \(I_{m,r}=0\) outside \(0\le r\le m\).

Define
\[
D_M(a,b)=\sum_{j=0}^{\min(a,b)}(-1)^j q^{\binom j2}
 \binom aj_q I_{M-j,b-j}(q),
\]
\[
C_m(r,s,t)=I_{m,t}(q)I_{m-t,r-t}(q)D_{m-t}(r-t,s-t),
\]
and, with \(d=r+s-t\),
\[
O_m(r,s,t)=
\begin{cases}
I_{m,d}(q)\binom dt_q\binom{d-t}{r-t}_q q^{(r-t)(s-t)},&d\le m,\\
0,&d>m.
\end{cases}
\]
Finally set
\[
S_m(q)=\sum_{k=0}^{2m}\binom{2m}{k}_q,
\qquad
G_m(q)=\sum_{r=0}^{m}q^r I_{m,r}(q),
\qquad
N_m(q)=S_m(q)+G_m(q),
\]
and
\[
B_m(q)=\sum_{r,s=0}^{m}\ \sum_{t=0}^{\min(r,s)}
\bigl(C_m(r,s,t)-O_m(r,s,t)\bigr)q^{r+s-t}.
\]
Then the subalgebra commutativity degree is exactly
\[
\boxed{\displaystyle
\operatorname{sd}(H_m(q))=1-\frac{B_m(q)}{N_m(q)^2}.}
\]
This formula is valid for every prime power \(q\), including characteristic two.

The formula extends the explicit \(m=1\) computation of Muhie--Otera--Russo (arXiv:2609.19086v1) to all Heisenberg ranks.  Their paper explicitly asks for the values of \(\operatorname{sd}(\mathfrak h(m))\) and proves only the \(m=1\) case.

## Structural classification of subalgebras

Every subalgebra of \(H_m(q)\) is of exactly one of the following two types.

1. **Center-containing:**
   \[
   W\oplus \mathbb F_qz,\qquad W\le V.
   \]
   Hence there are \(S_m(q)\) such subalgebras.

2. **Center-avoiding graph:**
   \[
   A(U,\alpha)=\{u+\alpha(u)z:u\in U\},
   \]
   where \(U\le V\) is totally isotropic and \(\alpha\in U^*\).  Thus the number with \(\dim U=r\) is \(q^r I_{m,r}(q)\), giving \(G_m(q)\) in total.

Indeed, if a subalgebra contains \(z\), subtracting central components shows that it is the full inverse image of its projection to \(V\).  If it does not contain \(z\), projection to \(V\) is injective; closure under brackets forces its image to be totally isotropic, and the subalgebra is the graph of a unique linear functional.

## Exact permutability criterion

Any pair for which at least one member contains \(z\) is permutable, because every bracket lies in \(\mathbb F_qz\).

For two graph subalgebras \(A(U,\alpha)\) and \(A(W,\beta)\), let \(T=U\cap W\).  Since all cross-brackets lie in the one-dimensional center,
\[
[A(U,\alpha),A(W,\beta)]\ne0
\quad\Longleftrightarrow\quad
\omega(U,W)\ne0.
\]
Moreover
\[
z\in A(U,\alpha)+A(W,\beta)
\quad\Longleftrightarrow\quad
(\alpha-\beta)|_T\ne0.
\]
Consequently the pair is nonpermutable exactly when
\[
\boxed{\omega(U,W)\ne0\quad\text{and}\quad(\alpha-\beta)|_{U\cap W}=0.}
\]
For fixed \(U,W\) of dimensions \(r,s\) with \(\dim(U\cap W)=t\), the second condition holds for exactly \(q^{r+s-t}\) ordered pairs \((\alpha,\beta)\).

## Counting the underlying isotropic pairs

For fixed dimensions \((r,s,t)\), \(C_m(r,s,t)\) is the number of ordered totally isotropic pairs \((U,W)\) with
\[
\dim U=r,\qquad \dim W=s,\qquad \dim(U\cap W)=t.
\]
To see this, choose \(T=U\cap W\), pass to the symplectic quotient \(T^\perp/T\), choose \(U/T\), and then count isotropic \(W/T\) disjoint from \(U/T\).  Möbius inversion on the subspace lattice of \(U/T\), whose Möbius function in dimension \(j\) is
\[
(-1)^j q^{\binom j2},
\]
gives exactly \(D_{m-t}(r-t,s-t)\).

Likewise, \(O_m(r,s,t)\) counts those pairs for which \(\omega(U,W)=0\).  In that case \(X=U+W\) is totally isotropic of dimension \(d=r+s-t\).  Choose \(X\), then \(T\le X\), then \(U/T\le X/T\); the number of complementary choices for \(W/T\) is
\[
q^{(r-t)(s-t)}.
\]
Thus \(C_m-O_m\) counts exactly the cross-nonorthogonal isotropic pairs, and multiplication by \(q^{r+s-t}\) counts the functional pairs that fail the permutability condition.  Summing proves the displayed formula for \(B_m(q)\) and hence the theorem.

## First new explicit case

For \(m=2\),
\[
N_2(q)=q^5+3q^4+5q^3+6q^2+4q+6,
\]
\[
B_2(q)=q^4(q+1)(q^2+1)(q^3+2q^2+4q+1),
\]
so
\[
\boxed{\displaystyle
\operatorname{sd}(H_2(q))=
\frac{3q^9+12q^8+34q^7+62q^6+91q^5+111q^4+108q^3+88q^2+48q+36}
{(q^5+3q^4+5q^3+6q^2+4q+6)^2}.}
\]
For \(m=1\), the general formula reduces to
\[
N_1(q)=q^2+2q+4,\qquad B_1(q)=q^3(q+1),
\]
and therefore recovers the known numerator
\[
3q^3+12q^2+16q+16.
\]

## Field-size phase transition

For fixed rank \(m\) and \(q\to\infty\), the exact formula gives
\[
\boxed{
\lim_{q\to\infty}\operatorname{sd}(H_m(q))=
\begin{cases}
0,&m=1,2,\\
5/9,&m=3,\\
1,&m\ge4.
\end{cases}}
\]
The first two limits follow from the explicit \(m=1,2\) formulas.  For \(m=3\),
\[
N_3(q)=3q^9+5q^8+7q^7+12q^6+13q^5+15q^4+12q^3+10q^2+6q+8
\]
and
\[
B_3(q)=q^5(q+1)(q^2-q+1)
(4q^{10}+7q^9+13q^8+21q^7+29q^6+35q^5+35q^4+27q^3+16q^2+5q+1),
\]
so the limit is \(1-4/9=5/9\).

For \(m\ge4\), the center-containing count has degree \(m^2\), while the degree of the \(r\)-th graph contribution is
\[
f_m(r)=\deg_q\big(q^rI_{m,r}(q)\big)
=\frac{r(4m-3r+3)}2.
\]
Its continuous maximum is \((4m+3)^2/24<m^2\) for \(m\ge4\).  Hence \(G_m(q)=o(S_m(q))\).  Since only graph--graph pairs can fail to permute,
\[
1-\operatorname{sd}(H_m(q))\le\left(\frac{G_m(q)}{N_m(q)}\right)^2\longrightarrow0.
\]

## Rank growth at fixed field

For every fixed prime power \(q\),
\[
\boxed{\displaystyle \lim_{m\to\infty}\operatorname{sd}(H_m(q))=1.}
\]
Indeed,
\[
S_m(q)\ge\binom{2m}{m}_q>q^{m^2}.
\]
For constants \(C_q,D_q<\infty\) depending only on \(q\), the standard product formulas give
\[
\binom mr_q\le C_q q^{r(m-r)},\qquad
\prod_{i=0}^{r-1}(q^{m-i}+1)\le D_q q^{rm-r(r-1)/2}.
\]
Therefore
\[
G_m(q)\le (m+1)C_qD_q q^{(4m+3)^2/24},
\]
so \(G_m(q)/S_m(q)\to0\), and the same graph--graph bound proves the claim.  Quantitatively this gives
\[
1-\operatorname{sd}(H_m(q))
=O_q\!\left(m^2q^{-2m^2/3+2m}\right).
\]

## Extraspecial group corollary

For an odd prime \(p\), the Lazard correspondent of \(H_m(p)\) is the exponent-\(p\) extraspecial group \(E_m(p)\) of order \(p^{2m+1}\).  Theorem 1.4 of arXiv:2609.19086v1 identifies subalgebra commutativity degree with subgroup commutativity degree under this correspondence.  Hence the same exact formula gives \(\operatorname{sd}(E_m(p))\), extending that paper's order-\(p^3\) corollary to every \(m\), and in particular
\[
\boxed{\displaystyle \lim_{m\to\infty}\operatorname{sd}(E_m(p))=1\qquad(p\text{ fixed odd}).}
\]

## Verification

`artifacts/verify_h2_prime_fields.py` independently enumerates every vector subspace of the 5-dimensional ambient space for \(q=2,3\), filters the Lie subalgebras, tests permutability directly from the bracket, and compares with the closed formula.  Its verified output is

```text
q=2: vector_subspaces=374, lie_subalgebras=158, permutable_ordered_pairs=18964, nonpermutable_ordered_pairs=6000
q=3: vector_subspaces=2664, lie_subalgebras=693, permutable_ordered_pairs=292329, nonpermutable_ordered_pairs=187920
all checks passed
```

The computation is supporting evidence only; the general result is proved by the classification and counting argument above.

## Literature context and limitations

Muhie--Otera--Russo introduce the subalgebra commutativity degree in arXiv:2609.19086v1, explicitly raise the problem of determining \(\operatorname{sd}(\mathfrak h(m))\), compute only \(m=1\), and prove a Lazard-transfer theorem to subgroup commutativity degree.  Their earlier work on factorization numbers and subgroup commutativity degree (arXiv:2304.08170) supplies general graph/spectral formulas but does not state the Heisenberg all-rank enumeration above.  Standard finite symplectic geometry supplies the formula for \(I_{m,r}(q)\); that ingredient is not claimed as new.

Targeted searches for the exact Heisenberg all-rank formula, equivalent symplectic-intersection formulations, and subgroup commutativity degrees of extraspecial \(p\)-groups did not locate prior coverage.  The main residual originality risk is older subgroup-lattice literature on extraspecial groups: explicit subgroup classifications are classical and could conceivably imply an equivalent formula without using the recent terminology.  No claim of exhaustive literature coverage or independent validation is made.

## References

1. S. K. Muhie, D. E. Otera, F. G. Russo, *On the number of modular pairs in finite dimensional Lie algebras on finite fields*, arXiv:2609.19086v1 (2026). https://arxiv.org/abs/2609.19086v1
2. S. K. Muhie et al., *Factorization number and subgroup commutativity degree via spectral invariants*, Comput. Appl. Math. 42 (2023), Art. 132. https://arxiv.org/abs/2304.08170
3. M. Tărnăuceanu, *Subgroup commutativity degrees of finite groups*, J. Algebra 321 (2009), 2508--2520.
4. M. Tărnăuceanu, *The subgroup commutativity degree of finite P-groups*, Bull. Aust. Math. Soc. 92 (2015), 337--343. https://arxiv.org/abs/1312.0296
5. For the standard symplectic count used in \(I_{m,r}(q)\), see e.g. the finite symplectic-space counting formula collected in Axioms 14 (2025), 614: https://www.mdpi.com/2075-1680/14/8/614
