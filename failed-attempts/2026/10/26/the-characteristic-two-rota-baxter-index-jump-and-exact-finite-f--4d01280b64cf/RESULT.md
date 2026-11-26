# The characteristic-two Rota–Baxter index jump and exact finite-field moduli of square-zero local algebras

## Finding
Let \(K\) be any field, let \(n\geq 1\), and set \(A=K\oplus V\), where \(\dim_KV=n\), \(V^2=0\), and \(1\in K\) is the unit. A *weight-zero Rota–Baxter operator* is a \(K\)-linear map \(P:A\to A\) satisfying
\[
P(x)P(y)=P(xP(y)+P(x)y)\quad(x,y\in A).
\]
Every such operator, in every characteristic, has a unique presentation
\[
P(a+u)=a v+L(u),\qquad L^2=0,\quad 2L(v)=0
\]
with \(v\in V\), \(L\in\operatorname{End}_K(V)\). In particular, \(P^3=0\) always; \(P^2=0\) in characteristic different from \(2\), whereas in characteristic \(2\) and dimension \(n\ge2\), operators with \(P^2\ne0\) exist. Thus the least uniform nilpotency exponent for weight-zero operators on \(A\) is exactly \(2\) outside characteristic \(2\), exactly \(3\) in characteristic \(2\) when \(n\ge2\), and \(2\) for \(n=1\).

For \(K=\mathbb F_q\), let \(N_{n,r}(q)\) denote the number of rank-\(r\) square-zero endomorphisms of \(V\), for \(0\le r\le\lfloor n/2\rfloor\). Then
\[
N_{n,r}(q)={n\brack r}_q{n-r\brack r}_q\lvert\mathrm{GL}_r(\mathbb F_q)\rvert,
\]
and the number \(B_{n,q}\) of weight-zero Rota–Baxter operators is
\[
B_{n,q}=
\begin{cases}
\displaystyle\sum_{r=0}^{\lfloor n/2\rfloor}N_{n,r}(q)q^{n-r},&q\text{ odd},\\[3pt]
\displaystyle q^n\sum_{r=0}^{\lfloor n/2\rfloor}N_{n,r}(q),&q\text{ even}.
\end{cases}
\]
Their isomorphism classes, where isomorphism means conjugation by a \(K\)-algebra automorphism of \(A\), are completely classified by rank \(r\) and the position of \(v\) in the flag \(0\subseteq\operatorname{im}L\subseteq\ker L\subseteq V\). The permitted types are \(v=0\), \(0\ne v\in\operatorname{im}L\), and \(v\in\ker L\setminus\operatorname{im}L\); in characteristic \(2\) there is the additional type \(v\notin\ker L\). In a type for which its defining set is empty, no orbit occurs. The exact number of isomorphism classes is
\[
\begin{cases}
2\lfloor n/2\rfloor+\lceil n/2\rceil+1,&q\text{ odd},\\
3\lfloor n/2\rfloor+\lceil n/2\rceil+1,&q\text{ even}.
\end{cases}
\]
For a given \(r\), the respective *labeled* orbit sizes are \(N_{n,r}(q)\), \(N_{n,r}(q)(q^r-1)\), \(N_{n,r}(q)(q^{n-r}-q^r)\), and (only in characteristic \(2\)) \(N_{n,r}(q)(q^n-q^{n-r})\).

Finally, if \(q\) is even and fixed, a uniformly random weight-zero Rota–Baxter operator on \(A\) has \(P^2\ne0\) with probability tending to \(1\) as \(n\to\infty\). More precisely,
\[
\Pr(P^2=0)=\frac{\sum_rN_{n,r}(q)q^{-r}}{\sum_rN_{n,r}(q)}
\le q^{-n/4}+O_q(nq^{-n^2/8}).
\]

## Assumptions and scope
All vector spaces, endomorphisms and algebra automorphisms are over the specified field \(K\). The algebra \(A\) is a split unital local algebra with square-zero radical \(V\), equivalently the degree-one truncated polynomial algebra \(K[x_1,\ldots,x_n]/(x_1,\ldots,x_n)^2\). The enumeration and probability statements require a finite field \(\mathbb F_q\). The isomorphism relation fixes the unit and the coefficient field. No assumption of algebraic closure is needed.

## Proof
**1. Identity classification in arbitrary characteristic.** Write
\(P(1)=\alpha+v\) and \(P(u)=f(u)+L(u)\) for \(u\in V\), where \(\alpha\in K\), \(v\in V\), \(f:V\to K\) is linear, and \(L:V\to V\) is linear. Apply the identity to \(u,w\in V\). Comparing scalar components gives \(f(u)f(w)=2f(u)f(w)\), hence \(f(u)f(w)=0\). Taking \(w=u\) yields \(f=0\) over every field. With \(P(V)\subseteq V\), the scalar component of the identity at \((1,1)\) gives \(\alpha^2=2\alpha^2\), so \(\alpha=0\). The radical component at \((1,1)\) gives \(2L(v)=0\). Applying the identity to \((1,u)\), using \(V^2=0\), gives \(0=L^2(u)\).

Conversely, for \(P(a+u)=a v+L(u)\) with \(L^2=0\) and \(2L(v)=0\), both outputs lie in \(V\), so their product vanishes. The other side is
\[
P\bigl(2abv+aL(w)+bL(u)\bigr)
=2abL(v)+aL^2(w)+bL^2(u)=0.
\]
Thus all and only the displayed operators satisfy the identity. Moreover \(P^2(a+u)=aL(v)\), and hence \(P^3=0\). If \(\operatorname{char}K\ne2\), the condition implies \(P^2=0\). In characteristic \(2\), take \(n\ge2\), choose a basis \(e_1,e_2,\ldots\), let \(L(e_1)=e_2\), \(L(e_j)=0\) for \(j\ne1\), and take \(v=e_1\). Then \(P^2(1)=e_2\ne0\). When \(n=1\), any square-zero \(L\) is zero, giving the remaining boundary case.

**2. Rank counts.** A square-zero \(L\) of rank \(r\) has image \(U\) of dimension \(r\), kernel \(W\) of dimension \(n-r\), and \(U\subseteq W\). First select \(U\), in \({n\brack r}_q\) ways. Then select \(W/U\), a subspace of dimension \(n-2r\) of \(V/U\) (dimension \(n-r\)), in \({n-r\brack r}_q\) ways. Finally \(L\) is uniquely determined by an isomorphism \(V/W\to U\), with \(\lvert\mathrm{GL}_r(\mathbb F_q)\rvert\) choices. The allowed \(v\) comprise \(\ker L\), of size \(q^{n-r}\), outside characteristic \(2\), and all \(V\), of size \(q^n\), in characteristic \(2\). This proves both counting formulas.

**3. Orbits under algebra automorphisms.** Every unital \(K\)-algebra automorphism fixes \(1\), preserves the unique maximal ideal \(V\), and restricts to an arbitrary element of \(\mathrm{GL}(V)\). Conjugation sends \((L,v)\) to \((gLg^{-1},gv)\). Fix rank \(r\), put \(s=n-2r\), and choose a Jordan decomposition with coordinates \((u,z,w)\in K^r\oplus K^r\oplus K^s\), such that \(L(u,z,w)=(0,u,0)\). Every invertible linear map commuting with \(L\) has precisely the form
\[
(u,z,w)\longmapsto
(Au,Cu+Az+Dw,Eu+Fw),
\]
where \(A\in\mathrm{GL}_r(K)\), \(F\in\mathrm{GL}_s(K)\), and \(C,D,E\) are arbitrary matrices of the indicated sizes. Thus the centralizer is transitive separately on the zero vector, the nonzero vectors in \(\operatorname{im}L\), the vectors in \(\ker L\setminus\operatorname{im}L\), and the vectors outside \(\ker L\). For instance, a nonzero \(u\) can be normalized by \(A\) and the other coordinates cleared by \(C,E\); similarly a nonzero \(w\) can be normalized by \(F\) and the \(z\) coordinate cleared by \(D\). These are precisely all possible types, and their sizes for each fixed \(L\) are
\[
1,\quad q^r-1,\quad q^{n-r}-q^r,\quad q^n-q^{n-r}.
\]
The last is admissible only in characteristic \(2\). Multiplying by the number of \(L\)'s gives the labeled orbit sizes. For ranks \(0\le r\le t=\lfloor n/2\rfloor\) there are \(t+1\) zero orbits, \(t\) nonzero-image orbits, \(\lceil n/2\rceil\) kernel-nonimage orbits, and in characteristic \(2\) another \(t\) outside-kernel orbits, proving the asserted totals.

**4. Generic index three.** For even \(q\), the exact probability of \(P^2=0\) is the stated ratio by Step 1. Let \(c_q=\prod_{j=1}^{\infty}(1-q^{-j})>0\). The formula from Step 2 gives, uniformly in \(n,r\),
\[
c_q^2q^{2r(n-r)}\le N_{n,r}(q)\le c_q^{-1}q^{2r(n-r)}.
\]
Set \(t=\lfloor n/2\rfloor\); then \(2t(n-t)\ge(n^2-1)/2\). For \(r<n/4\), \(2r(n-r)\le3n^2/8\), so the ratio of the sum of these terms to \(\sum_rN_{n,r}(q)\) is \(O_q(nq^{-n^2/8})\). In the complementary ranks \(r\ge n/4\), one has \(q^{-r}\le q^{-n/4}\). Splitting the probability at this threshold proves the bound and limit.

## Verification
The standalone `verify.py` builds the multiplication table from the definition and tests every linear operator directly against the Rota–Baxter identity for prime fields \(\mathbb F_2\) and \(\mathbb F_3\) in dimensions \(n=1,2\), and for \(\mathbb F_2\) in dimension \(n=3\). It separately checks the classification conditions, the Gaussian-binomial count, the sizes of each rank/flag stratum, and transitivity of the predicted orbits via exhaustive automorphism groups. Direct output is `VERIFY_OK`.

For \((q,n)=(2,2),(3,2),(2,3)\), the total numbers of operators are respectively \(16,33,176\). For \((q,n)=(2,2)\) exactly \(6\) operators have \(P^2\ne0\), and for \((2,3)\) exactly \(84\) do. These small-dimensional checks do not establish the general theorem; Steps 1–4 do.

## Relationship to prior work
Azhar Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras* (arXiv:2605.15670, first public version 2026-05-15), proves the weight-zero description in characteristic zero, where \(P^2=0\). In particular, the characteristic-different-from-two identity description above is an extension in field scope, not a claim to rediscover Farooq's characteristic-zero theorem. The characteristic-two family with \(P^2\ne0\), the all-finite-field automorphism-orbit structure, the exact orbit sizes and the generic-index result are the contributions assessed here.

V. Gubarev, *Rota–Baxter operators on unital algebras* (arXiv:1805.00723, 2018), introduces the Rota–Baxter nilpotency index and proves general characteristic-zero nilpotency bounds for unital algebraic algebras. Those general bounds do not assert the present characteristic-two classification or finite-field orbit formulas. The Jordan decomposition and Gaussian-binomial formulas used here are standard algebraic tools, not claimed as independent inventions.

## Limitations
The operators have weight zero and act on the specified split square-zero local algebra; no assertion is made for higher truncations, non-split local algebras, arbitrary Rota–Baxter weights, or noncommutative radicals. Computation was exhaustive only for the listed small prime fields and dimensions. Novelty comparison is limited to the sources and searchable records identified in the accompanying review; coverage implicit in other general classifications remains a risk. No independent mathematical audit has been performed.

## References
1. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670 (2026-05-15), https://arxiv.org/abs/2605.15670. Relevant statements: Theorem 3.4 and Section 3.1; Sections 2 and 4 for setup and scope.
2. V. Gubarev, *Rota–Baxter operators on unital algebras*, arXiv:1805.00723 (2018), https://arxiv.org/abs/1805.00723. Relevant statements: introduction and Theorems 5.5, 5.8, 5.10.
