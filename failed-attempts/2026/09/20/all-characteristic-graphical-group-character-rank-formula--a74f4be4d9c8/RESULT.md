# All-characteristic character rank formula for graphical groups

Let \(\Gamma=(V,E)\) be a finite simple graph with \(n=|V|\) and \(m=|E|\), and let
\[
G=\mathbf G_\Gamma(\mathbf F_q)
\]
be its graphical group over the finite field \(\mathbf F_q\). Order \(V=\{v_1,\dots,v_n\}\). For
\(y=(y_e)_{e\in E}\in\mathbf F_q^E\), let \(B_\Gamma(y)\) be the \(n\times n\) alternating matrix with
\[
(B_\Gamma(y))_{jk}=
\begin{cases}
y_{\{v_j,v_k\}},&j<k,\ \{v_j,v_k\}\in E,\\
-y_{\{v_j,v_k\}},&j>k,\ \{v_j,v_k\}\in E,\\
0,&\text{otherwise}.
\end{cases}
\]
In characteristic \(2\), this is still alternating: its diagonal is zero and
\(B_\Gamma(y)^T=-B_\Gamma(y)=B_\Gamma(y)\).

For \(i\ge 0\), write
\[
\operatorname{ch}(\Gamma,i;q)
=
\#\{\chi\in\operatorname{Irr}(G):\chi(1)=q^i\}.
\]

## Theorem

For every prime power \(q\), including even \(q\),
\[
\boxed{
\operatorname{ch}(\Gamma,i;q)
=
q^{\,n-2i}\,
\#\{y\in\mathbf F_q^E:\operatorname{rank}B_\Gamma(y)=2i\}.
}
\]

Consequently every irreducible character degree of \(G\) is a power \(q^i\).

For odd \(q\), the rank-count description is implicit in O'Brien--Voll's orbit-method formula and is the formulation recorded by Rossmann. The point here is that the same formula holds in characteristic \(2\), where the class-\(<p\) hypothesis used by that orbit-method argument is unavailable.

## Proof

Rossmann's Proposition 2.3 gives, over every commutative ring and hence over every finite field,
\[
G'=\mathbf F_q E
\quad\text{and}\quad
G/G'\cong \mathbf F_q V
\]
as additive groups. Moreover \(G'\) is central, and the group commutator agrees with the graphical Lie bracket. Thus \(G\) is a central extension
\[
1\longrightarrow C\longrightarrow G\longrightarrow A\longrightarrow 1,
\qquad
C=\mathbf F_qE,\quad A=\mathbf F_qV.
\]

We first record a finite twisted-group-algebra lemma.

### Lemma

Let \(A\) be a finite abelian group, let \(\alpha:A\times A\to\mathbf C^\times\) be a normalized
\(2\)-cocycle, and let \(T=\mathbf C^\alpha[A]\). Put
\[
\beta(a,b)=\frac{\alpha(a,b)}{\alpha(b,a)}
\]
and
\[
R=\operatorname{rad}\beta
=\{a\in A:\beta(a,b)=1\text{ for every }b\in A\}.
\]
Then \(T\) has exactly \(|R|\) simple modules, and every simple module has dimension
\[
\sqrt{|A|/|R|}.
\]

#### Proof of the lemma

Let \(u_a\) denote the standard basis element of \(T\) indexed by \(a\in A\).
Since \(A\) is abelian,
\[
u_a u_b=\beta(a,b)\,u_bu_a.
\]
Hence a basis vector \(u_a\) is central exactly when \(a\in R\), and therefore
\[
Z(T)=\operatorname{span}_{\mathbf C}\{u_r:r\in R\},
\qquad
\dim_{\mathbf C}Z(T)=|R|.
\]
The usual averaging proof of Maschke's theorem applies to finite twisted group algebras over
\(\mathbf C\), so \(T\) is semisimple. Thus its commutative center is a product of
\(|R|\) copies of \(\mathbf C\) and has \(|R|\) primitive idempotents.

Choose representatives for \(A/R\). Multiplication by \(u_r\), \(r\in R\), only moves a basis
element inside its \(R\)-coset, so \(T\) is free over \(Z(T)\) of rank \(|A/R|\).
If \(e\) is a primitive idempotent of \(Z(T)\), then
\[
\dim_{\mathbf C}(Te)=|A/R|.
\]
The algebra \(Te\) is a simple finite-dimensional \(\mathbf C\)-algebra, hence \(Te\cong
M_d(\mathbf C)\) for some \(d\). Therefore
\[
d^2=|A/R|=|A|/|R|.
\]
Each primitive central idempotent contributes one simple module, proving the lemma. \(\square\)

Return to \(G\). For each linear character \(\lambda\in\widehat C\), let
\[
e_\lambda=\frac1{|C|}\sum_{c\in C}\lambda(c)^{-1}c\in\mathbf CG.
\]
Because \(C\) is central, \(\mathbf CG e_\lambda\) is a block corresponding exactly to irreducible
representations whose restriction to \(C\) has central character \(\lambda\). Choosing a section
\(s:A\to G\) identifies this block with a twisted group algebra
\[
\mathbf CG e_\lambda\cong \mathbf C^{\alpha_\lambda}[A].
\]
Its commutator bicharacter is
\[
\beta_\lambda(a,b)=\lambda([s(a),s(b)]).
\]

Fix a nontrivial additive character \(\psi_0:\mathbf F_p\to\mathbf C^\times\), where
\(q=p^f\). The trace pairing identifies \(y\in\mathbf F_q^E\) with
\[
\lambda_y(z)
=
\psi_0\!\left(
\operatorname{Tr}_{\mathbf F_q/\mathbf F_p}
\sum_{e\in E}y_ez_e
\right),
\qquad z\in C.
\]
This is a bijection \(\mathbf F_q^E\to\widehat C\).

For \(x,x'\in A=\mathbf F_q^V\), Rossmann's commutator formula gives
\[
\beta_{\lambda_y}(x,x')
=
\psi_0\!\left(
\operatorname{Tr}_{\mathbf F_q/\mathbf F_p}
\bigl(x^TB_\Gamma(y)x'\bigr)
\right).
\]
The field-trace pairing is nondegenerate, so the radical of this bicharacter is precisely
\[
R_y=\ker B_\Gamma(y).
\]
If \(r=\operatorname{rank}B_\Gamma(y)\), then
\[
|R_y|=q^{n-r}.
\]
Since \(B_\Gamma(y)\) is alternating, \(r\) is even over every field, including characteristic
\(2\); write \(r=2i\).

Applying the lemma to the \(\lambda_y\)-block, that block has
\[
|R_y|=q^{n-2i}
\]
irreducible representations, and each has degree
\[
\sqrt{\frac{|A|}{|R_y|}}
=
\sqrt{\frac{q^n}{q^{n-2i}}}
=
q^i.
\]
Summing over all \(y\) of rank \(2i\) proves the formula. \(\square\)

As a check, each \(y\)-block contributes
\[
q^{n-2i}(q^i)^2=q^n=|G/G'|
\]
to the sum of squares of irreducible degrees; summing over all \(q^m\) central characters gives
\(q^{n+m}=|G|\), the known order of the graphical group.

## Corollary 1: complete bipartite graphs

Let \(\Gamma=K_{a,b}\). After ordering the two vertex classes,
\[
B_{K_{a,b}}(y)=
\begin{pmatrix}
0&M\\
-M^T&0
\end{pmatrix},
\qquad M\in M_{a\times b}(\mathbf F_q),
\]
so
\[
\operatorname{rank}B_{K_{a,b}}(y)=2\operatorname{rank}M.
\]
Let
\[
N_{a,b,r}(q)
=
\#\{M\in M_{a\times b}(\mathbf F_q):\operatorname{rank}M=r\}.
\]
The standard rectangular-matrix count is
\[
N_{a,b,r}(q)
=
\prod_{j=0}^{r-1}
\frac{(q^a-q^j)(q^b-q^j)}{q^r-q^j}
=
{a\brack r}_q\,{b\brack r}_q\,|\operatorname{GL}_r(q)|.
\]
Hence, for \(0\le r\le\min(a,b)\),
\[
\boxed{
\operatorname{ch}(K_{a,b},r;q)
=
q^{a+b-2r}N_{a,b,r}(q),
}
\]
and the count is zero for larger \(r\).

Thus Rossmann's character-enumeration question has an explicit polynomial answer for every complete
bipartite graph and every prime power \(q\).

## Corollary 2: complete graphs in all characteristics

For \(\Gamma=K_n\), the matrices \(B_\Gamma(y)\) are exactly all alternating \(n\times n\) matrices.
The number of such matrices of rank \(2r\) is
\[
{n\brack 2r}_q\,
\frac{|\operatorname{GL}_{2r}(q)|}{|\operatorname{Sp}_{2r}(q)|}
=
{n\brack 2r}_q\,
q^{r(r-1)}
\prod_{j=1}^{r}(q^{2j-1}-1).
\]
Therefore, for \(0\le 2r\le n\),
\[
\boxed{
\operatorname{ch}(K_n,r;q)
=
q^{\,n-2r+r(r-1)}
{n\brack 2r}_q
\prod_{j=1}^{r}(q^{2j-1}-1).
}
\]
This extends the previously recorded complete-graph formula from odd \(q\) to all prime powers.

## Scope and limitations

The theorem converts character enumeration for every graphical group into an alternating-matrix
rank-count problem in every characteristic. It does **not** imply that
\(\operatorname{ch}(\Gamma,i;q)\) is polynomial in \(q\) for an arbitrary graph: rank counts for
support-constrained alternating matrix spaces may still have complicated dependence on the field.

The twisted-group-algebra argument itself is classical representation theory. The contribution here
is its application to graphical groups to remove the odd-characteristic restriction, together with
the resulting explicit complete-bipartite family. Originality is asserted only to the best of our
knowledge.

## References

1. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*,
   Bulletin of the London Mathematical Society **54** (2022), 1923--1943.
   DOI: 10.1112/blms.12665.
2. E. A. O'Brien and C. Voll, *Enumerating classes and characters of p-groups*,
   Transactions of the American Mathematical Society **367** (2015), 7775--7796.
   DOI: 10.1090/tran/6276.
3. R. C. Busby and H. A. Smith, *Representations of Twisted Group Algebras*,
   Transactions of the American Mathematical Society **149** (1970), 503--537.
   DOI: 10.1090/S0002-9947-1970-0264418-8.
