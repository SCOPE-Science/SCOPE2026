# Cubic Rota–Baxter operators and finite-field orbits on square-zero local algebras

## Finding
Let \(k=\mathbb F_q\), let \(V\) be \(n\)-dimensional over \(k\) with \(n\ge2\), and let \(A=k\oplus V\) be the unital algebra with \(V^2=0\). A *weight-zero Rota–Baxter operator* is a \(k\)-linear map \(P:A\to A\) satisfying
\[
P(a)P(b)=P(P(a)b+aP(b))\qquad(a,b\in A).
\]
All such operators have the unique form
\[
P(c+v)=c u+T(v),\qquad u\in V,\quad T\in\operatorname{End}_k(V),\quad T^2=0,
\]
subject to \(2Tu=0\). In particular, in characteristic two there is **no restriction** on \(u\), whereas in odd characteristic \(u\in\ker T\).

Put
\[
F_{n,r}(q)=\begin{bmatrix}n\\r\end{bmatrix}_q
\begin{bmatrix}n-r\\r\end{bmatrix}_q
\prod_{i=0}^{r-1}(q^r-q^i),\qquad 0\le r\le\lfloor n/2\rfloor.
\]
Here the brackets are Gaussian binomial coefficients, and an empty product is one. The numbers of labeled weight-zero Rota–Baxter operators are exactly
\[
\#\mathrm{RB}_0(A)=
\begin{cases}
q^n\displaystyle\sum_{r=0}^{\lfloor n/2\rfloor}F_{n,r}(q),&\operatorname{char}k=2,\\
\displaystyle\sum_{r=0}^{\lfloor n/2\rfloor}F_{n,r}(q)q^{n-r},&\operatorname{char}k\ne2.
\end{cases}
\]

Every such \(P\) satisfies \(P^3=0\). **Exactly in characteristic two**, operators with \(P^2\ne0\) occur, and, for fixed \(r=\operatorname{rank}T\), their number is
\[
F_{n,r}(q)(q^n-q^{n-r}).
\]
This number is nonzero precisely for \(r\ge1\). Hence the maximal nilpotency index of these operators is three in characteristic two, but at most two in odd characteristic.

Under conjugation by unital algebra automorphisms \(\operatorname{Aut}_k(A)=\operatorname{GL}(V)\), each admissible pair \((T,u)\) is classified by \(r=\operatorname{rank}T\) and exactly one of the mutually exclusive vector positions
\[
u=0,\quad 0\ne u\in\operatorname{im}T,\quad u\in\ker T\setminus\operatorname{im}T,\quad u\notin\ker T.
\]
The last position occurs only in characteristic two, the third only when \(n>2r\), and the second only when \(r>0\). Each nonempty position is one orbit. For fixed \(r\), its orbit cardinality is \(F_{n,r}(q)\) times, respectively,
\[
1,\quad q^r-1,\quad q^{n-r}-q^r,\quad q^n-q^{n-r}.
\]
Consequently, the number of isomorphism classes of weight-zero Rota–Baxter algebra structures on the fixed underlying algebra \(A\) is
\[
\begin{cases}
2n+1,&\operatorname{char}k=2\text{ and }n\text{ even},\\
2n,&\operatorname{char}k=2\text{ and }n\text{ odd},\\
3n/2+1,&\operatorname{char}k\ne2\text{ and }n\text{ even},\\
(3n+1)/2,&\operatorname{char}k\ne2\text{ and }n\text{ odd}.
\end{cases}
\]

## Assumptions and scope
The ground field \(k\) is a finite field, \(n\ge2\), and all maps and automorphisms are \(k\)-linear and unital where appropriate. The algebra multiplication is \((a,v)(b,w)=(ab,aw+bv)\). An isomorphism of two operators is an algebra automorphism \(g\) satisfying \(gPg^{-1}=P'\); equivalence under arbitrary linear similarity on \(A\) is not asserted. The statements about operator normal forms and vector orbits hold over arbitrary fields, while the displayed counts require finite fields.

## Proof
**Reduction of the Rota–Baxter identity.** Write \(P(1)=\alpha+u\), and \(P(v)=\ell(v)+Tv\) for \(v\in V\), with scalar functional \(\ell:V\to k\). Applying the Rota–Baxter identity to \(v,w\in V\) and comparing scalar parts yields \(\ell(v)\ell(w)=2\ell(v)\ell(w)\). Taking \(v=w\) proves \(\ell=0\) over any field. Applying the identity to \((1,1)\) gives \(\alpha^2=2\alpha^2\), hence \(\alpha=0\); its radical component gives \(2Tu=0\). The identity on \((1,v)\) gives \(T^2v=0\). Conversely, if \(T^2=0\) and \(2Tu=0\), both sides are zero: for \(a=c+v\) and \(b=d+w\), the right side is \(2cdTu+cT^2w+dT^2v=0\), while the left side is zero because \(P(A)\subseteq V\) and \(V^2=0\). This proves necessity and sufficiency without dividing by two.

**Rank-stratified count.** If \(T^2=0\) and \(\operatorname{rank}T=r\), then \(I=\operatorname{im}T\subseteq K=\ker T\), with \(\dim I=r\), \(\dim K=n-r\), and \(T\) induces an isomorphism \(V/K\to I\). Choose \(I\), then \(K\), then that isomorphism. These choices number \(F_{n,r}(q)\). For each \(T\), characteristic two permits all \(q^n\) vectors \(u\), whereas odd characteristic permits the \(q^{n-r}\) vectors of \(K\). Also \(P^2(1)=Tu\) and \(P^2(V)=0\), so precisely the \(q^n-q^{n-r}\) vectors outside \(K\) yield nilpotency index three.

**Orbit decomposition.** The maximal ideal \(V\) is characteristic in the unital local algebra \(A\), and each \(g\in\operatorname{GL}(V)\) extends uniquely to a unital automorphism of \(A\). Conjugation maps \((T,u)\) to \((gTg^{-1},gu)\). All square-zero endomorphisms of rank \(r\) are similar. Choose a Jordan-chain basis \(e_1,f_1,\dots,e_r,f_r,z_1,\dots,z_s\), with \(Te_i=f_i\), \(Tf_i=Tz_j=0\), and \(s=n-2r\). The centralizer of \(T\) is transitive on each nonempty vector position listed in the finding: a nonzero vector of \(\operatorname{im}T\) can be chosen as \(f_1\); a vector of \(\ker T\setminus\operatorname{im}T\) can be chosen as \(z_1\); and a vector outside \(\ker T\) can be chosen as \(e_1\), after extending it and its nonzero image to a Jordan-chain basis. The zero vector is fixed. Their sizes in \(V\) are \(1\), \(q^r-1\), \(q^{n-r}-q^r\), and \(q^n-q^{n-r}\). Multiplication by the number \(F_{n,r}(q)\) of possible \(T\) gives the orbit sizes. Summing the nonempty positions over \(r\) gives the four formulas for orbit counts.

## Verification
The standalone script `verify.py` builds the algebra multiplication and checks the defining identity on every basis pair for every candidate linear map of the form specified above, without using the defining-equation simplification as its test. It exhaustively checks \((n,q)=(2,2),(2,3),(2,4),(3,2)\), using an explicit model of \(\mathbb F_4\). The resulting operator totals are \(16,33,256,176\), respectively. It separately enumerates conjugacy orbits under the full \(\operatorname{GL}_n(\mathbb F_q)\) action for \((n,q)=(2,2),(2,3),(3,2)\), giving \(5,4,6\) orbits. Run `python3 verify.py`; successful execution prints `VERIFY_OK`. Finite-field testing supplements the all-dimensional algebraic proof and does not establish it on its own.

## Relationship to prior work
Guo, Rosenkranz and Zheng (arXiv:1402.3702v1, publicly submitted 15 February 2014) classified weight-zero Rota–Baxter operators on semigroup algebras of orders two and three over characteristic-zero fields; its tables do not state the arbitrary-rank characteristic-two local-algebra orbit census. Farooq (arXiv:2605.15670v1) explicitly classifies weight-zero operators on the **same radical-square-zero unital algebra in characteristic zero**, obtaining \(T^2=0\) and \(Tu=0\). This pre-existing reduction is not claimed as new in odd characteristic. The present new portion removes the characteristic-zero restriction, identifies the exact characteristic-two failure of \(P^2=0\), and counts and classifies every resulting finite-field orbit in all dimensions. The ordinary Jordan classification of square-zero endomorphisms is used as a standard ingredient, not claimed as original.

## Limitations
This result addresses weight zero, radical-square-zero commutative unital algebras, and conjugacy under unital algebra automorphisms. It makes no claim for nonzero weights, non-square-zero radicals, or general finite-dimensional algebras. Searches cannot establish absolute priority; a specialized positive-characteristic Rota–Baxter classification not located here could overlap.

## References
1. L. Guo, M. Rosenkranz and S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702v1 (15 February 2014), https://arxiv.org/abs/1402.3702.
2. A. Farooq, *Rota Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (15 May 2026), https://arxiv.org/abs/2605.15670.
3. L. Guo, *An Introduction to Rota–Baxter Algebra*, Surveys of Modern Mathematics 4, International Press (2012), for the basic identity and terminology.
