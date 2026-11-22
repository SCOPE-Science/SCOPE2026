# The field-size threshold for universal \(m\)-ary evolution envelopes

## Finding

Fix an integer \(m\ge3\), an integer \(n\ge2\), and a field \(K\). A *commutative \(m\)-ary algebra* means an \(n\)-dimensional \(K\)-vector space \(A\) equipped with one symmetric \(K\)-multilinear multiplication \(\mu_A:A^m\to A\), with no associativity requirement. An *\(m\)-ary evolution algebra* means an \(m\)-ary algebra \(E\) with a basis \(u_1,\ldots,u_s\) such that \(\mu_E(u_{j_1},\ldots,u_{j_m})=0\) unless every index is the same. An ideal \(I\) obeys \(\mu_E(E,\ldots,E,I,E,\ldots,E)\subseteq I\) in every position.

**Theorem (sharp universal embedding boundary).** Every commutative \(m\)-ary algebra of dimension \(n\) over \(K\) embeds as an ideal of a finite-dimensional \(m\)-ary evolution algebra if and only if either \(K\) is infinite, or \(K=\mathbb F_q\) is finite and \(m\le q\). More precisely, in either positive case every such algebra embeds as an ideal in an \(m\)-ary evolution algebra of dimension at most

\[
N(n,m)=\binom{n+m-1}{m},
\]

and the ambient \(m\)-ary multiplication has image inside the embedded ideal (so the quotient has zero multiplication). If \(K=\mathbb F_q\) and \(m\ge q+1\), an explicit two-dimensional commutative \(m\)-ary algebra fails to embed even as a subalgebra in any \(m\)-ary evolution algebra, of any dimension.

The dimension-one case is exceptional: every one-dimensional commutative \(m\)-ary algebra is itself an \(m\)-ary evolution algebra over every field.

## Assumptions and scope

There is no requirement of \(m\)-ary associativity, unitality, nilpotency, or finite base-field characteristic. Homomorphisms and embeddings are \(K\)-linear and preserve the \(m\)-linear multiplication. In the negative assertion the failure holds already for subalgebra embeddings, hence also for ideal embeddings. The phrase "every algebra" is essential: it does not rule out special algebras embedding above the field-size threshold. The bound \(N(n,m)\) is a universal upper bound, not a claim that every algebra needs that dimension.

## Proof

### 1. The diagonal-tensor criterion

Choose a basis \(e_1,\ldots,e_n\) of \(A\). For every multi-index \(b=(b_1,\ldots,b_n)\in\mathbb N_0^n\) with \(\sum b_i=m\), let \(T_b\in A\) denote the value of \(\mu_A\) on a tuple containing exactly \(b_i\) copies of \(e_i\). Symmetry ensures these \(N(n,m)\) values determine \(\mu_A\) completely, in every characteristic.

For a vector \(a=(a_1,\ldots,a_n)\in K^n\), let \(\ell_a\in A^*\) be \(\ell_a(\sum x_ie_i)=\sum a_ix_i\). The pure symmetric \(m\)-linear scalar form \(\ell_a^{\otimes m}\) has value \(a^b=\prod_i a_i^{b_i}\) on the tuple indexed by \(b\). Therefore the span of these forms is all symmetric scalar \(m\)-linear forms if and only if the evaluation columns

\[
 (a^b)_{|b|=m},\qquad a\in K^n,
\]

span \(K^{N(n,m)}\). By elementary linear duality, this condition holds if and only if **no nonzero homogeneous polynomial of degree \(m\) in \(n\) variables vanishes on all of \(K^n\)**. This argument is in the invariant symmetric multilinear tensor space, not the diagonal polynomial \(x\mapsto\mu_A(x,\ldots,x)\); it remains valid when the characteristic divides \(m!\).

### 2. Constructing the evolution envelope whenever the columns span

Select \(N=N(n,m)\) vectors \(a^{(1)},\ldots,a^{(N)}\in K^n\) whose columns form a basis, and write \(\ell_j=\ell_{a^{(j)}}\). There are unique vectors \(v_1,\ldots,v_N\in A\) satisfying, for every \(b\) with \(|b|=m\),

\[
 T_b=\sum_{j=1}^{N}\left(\prod_i(a_i^{(j)})^{b_i}\right)v_j.
\]

By symmetry and multilinearity this gives, for arbitrary \(x_1,\ldots,x_m\in A\),

\[
 \mu_A(x_1,\ldots,x_m)=\sum_{j=1}^{N}\ell_j(x_1)\cdots\ell_j(x_m)v_j.
\]

Take the vector space \(E=K^N\) with distinguished basis \(u_1,\ldots,u_N\), and define \(\phi:A\to E\) by \(\phi(x)=\sum_j\ell_j(x)u_j\). This map is injective: if every \(\ell_j(x)=0\), then every scalar pure power \(\ell^{\otimes m}\) vanishes on \((x,\ldots,x)\), since these forms lie in their span. Thus \(\ell(x)^m=0\) for every \(\ell\in A^*\), which forces \(x=0\).

Define the \(m\)-ary multiplication on \(E\) by

\[
 \mu_E(u_j,\ldots,u_j)=\phi(v_j),\qquad
 \mu_E(u_{j_1},\ldots,u_{j_m})=0\quad\text{if the indices are not all equal},
\]

extended multilinearly. It is an \(m\)-ary evolution algebra by definition, and

\[
 \mu_E(\phi(x_1),\ldots,\phi(x_m))
 =\sum_j\ell_j(x_1)\cdots\ell_j(x_m)\phi(v_j)
 =\phi(\mu_A(x_1,\ldots,x_m)).
\]

Moreover, \(\mu_E(E^m)\subseteq\phi(A)\), so \(\phi(A)\) is an ideal, and the quotient algebra has zero multiplication.

### 3. Determining when the evaluation columns span

If \(K\) is infinite, the polynomial identity principle says that a polynomial vanishing on every \(K\)-point is zero. Hence the columns span for every \(m\).

Let \(K=\mathbb F_q\) and \(m\le q\). We prove by induction on \(n\) that a homogeneous polynomial \(P\in K[X_1,\ldots,X_n]\) of degree \(m\) vanishing on \(K^n\) is zero. For \(n=1\), evaluate at \(1\). If \(n\ge2\), restricting to \(X_n=0\) and using induction shows \(P(X_1,\ldots,X_{n-1},0)=0\) as a polynomial; hence \(P=X_n Q\), where \(Q\) is homogeneous of degree \(m-1<q\). For every \((x_1,\ldots,x_{n-1})\in K^{n-1}\), the equality \(P(x_1,\ldots,x_{n-1},1)=0\) forces \(Q(x_1,\ldots,x_{n-1},1)=0\). Since \(Q(X_1,\ldots,X_{n-1},1)\) has degree below \(q\) in every variable, repeated one-variable root counting makes it the zero polynomial. Homogeneity then gives \(Q=0\), hence \(P=0\). The construction in Part 2 applies and proves the uniform \(N(n,m)\) bound.

### 4. A sharp finite-field obstruction

Suppose \(K=\mathbb F_q\), \(n\ge2\), and \(m\ge q+1\). For any two elements \(x,y\) in any \(m\)-ary evolution algebra over \(K\), one has the universal identity

\[
 \mu_E(\underbrace{x,\ldots,x}_{m-1},y)
 =\mu_E(\underbrace{x,\ldots,x}_{m-q},\underbrace{y,\ldots,y}_{q}).
\]

Indeed, in a natural basis, each diagonal coordinate on the left is \(a^{m-1}b\) and that on the right is \(a^{m-q}b^q\), and these agree because \(a^q=a\) and \(b^q=b\) in \(\mathbb F_q\). This identity passes to every subalgebra.

Now define a symmetric \(m\)-linear product on \(A=K e_1\oplus K e_2\) by setting

\[
 \mu_A(\underbrace{e_1,\ldots,e_1}_{m-1},e_2)=e_1,
\]

for every permutation of the displayed tuple, and setting it equal to zero on every other basis multiset. The two multisets \((m-1,1)\) and \((m-q,q)\) are different because \(q\ge2\). The universal identity above fails on \(A\), with left side \(e_1\) and right side \(0\). Hence no injective homomorphism \(A\to E\) exists for any \(m\)-ary evolution algebra \(E\). For each \(n>2\), adjoin \(n-2\) further basis elements whose products with every tuple are zero; the same violated identity survives, giving the required \(n\)-dimensional counterexample. This completes the proof.

## Verification

The self-contained Python files `VERIFY.py`, `VERIFY_THRESHOLD.py`, and `VERIFY_EXTENSION_FIELD.py` use exact rational or finite-field arithmetic. `VERIFY.py` independently inverts the degree-\(m\) simplex-evaluation matrices and reconstructs arbitrary symmetric structure tensors over \(\mathbb Q\) and several prime fields of characteristic greater than \(m\). `VERIFY_THRESHOLD.py` checks full pure-tensor evaluation ranks in dimensions two and three over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\), across the positive boundary and first two negative arities. `VERIFY_EXTENSION_FIELD.py` repeats this rank experiment over \(\mathbb F_4\), using explicit irreducible-polynomial arithmetic. The output terminates respectively in `VERIFY_OK`, `THRESHOLD_VERIFY_OK`, and `EXTENSION_VERIFY_OK`.

These tests are finite corroboration, **not** the proof of the theorem for arbitrary fields, dimensions or arities. Every necessary infinite assertion is proved in Parts 1–4.

## Relationship to prior work

Costoya, Fernández Ouaridi, and Viruel (arXiv:2609.32784v1, first public 2026-09-26) prove the binary evolution-algebra ideal embedding theorem, provide a \(\binom{n+1}{2}\)-dimensional construction, study minimum binary envelopes via Waring decompositions, and pose their Question 4.7 about the \(m\)-ary extension. Their stated expectation includes characteristic zero and characteristic greater than \(m\). This theorem supplies an affirmative extension in all infinite-field characteristics, an exact finite-field threshold depending on the field size rather than only the characteristic, and explicit counterexamples beyond that threshold. The binary case and the elementary polynomial-evaluation principles are not claimed as new.

The nonvanishing condition for degree-\(m\) homogeneous polynomials over finite fields is classical and is closely related to the low-degree dimension of projective Reed–Muller evaluation codes (Sørensen, 1991). The result here is an algebraic interpretation of that boundary as a necessary and sufficient condition for **universal ideal embedding**, with an explicit natural-basis construction and sharp negative examples. We do not claim new results about projective Reed–Muller code dimensions themselves.

## Limitations

The theorem concerns symmetric multilinear products without additional associativity or Filippov identities. The negative examples are not asserted to satisfy any such extra identities. The given ambient dimension is an upper bound, not a minimum-dimension classification for individual algebras. No analogous positive statement is asserted over finite fields when \(m>q\) for every individual algebra; only the universal quantifier fails. Source-priority searches did not identify the specific full-field-size statement in earlier work, but unindexed specialized articles could establish equivalent coverage. No independent mathematical review has been performed.

## References

1. C. Costoya, A. Fernández Ouaridi, A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784v1 (first public 2026-09-26), especially Theorem 2.1, Section 4, and Question 4.7. https://arxiv.org/abs/2609.32784
2. A. B. Sørensen, *Projective Reed–Muller codes*, IEEE Transactions on Information Theory **37** (1991), 1567–1576, DOI:10.1109/18.104317. Classical coding-theory background on homogeneous finite-field evaluations.
3. R. San-José, *A recursive construction for projective Reed–Muller codes*, arXiv:2312.05072 (2023). Context on the known code-dimension literature.
