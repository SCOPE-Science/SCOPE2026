# Pairwise-annihilating two-dimensional representations: components and finite-field census

## Finding

Let \(k\) be any field and let \(m\ge1\). Define the **reduced** affine variety
\[
\mathcal Z_m(k)=\{(X_1,\ldots,X_m)\in M_2(k)^m:X_iX_j=X_jX_i=0\text{ whenever }i\ne j\}_{\mathrm{red}}.
\]
Equivalently, this is the reduced variety of two-dimensional unital representations of
\[
R_m=k[t_1,\ldots,t_m]/(t_it_j:i\ne j),
\]
the coordinate-ring fibre product of \(m\) affine lines at their origins. In particular, no individual square-zero condition is imposed.

**Theorem.** For every algebraically closed \(k\), the geometrically irreducible components of \(\mathcal Z_m\) are precisely the following, with all varieties defined over the original field:

1. For each \(i\), the coordinate axis \(A_i=\{X_j=0\text{ for }j\ne i\}\cong\mathbb A^4\).
2. For each unordered pair \(\{i,j\}\), the component \(B_{ij}\) obtained by setting the other matrices to zero and requiring \(X_iX_j=X_jX_i=0\), \(\det X_i=\det X_j=0\). It is geometrically irreducible of dimension \(4\).
3. **Only for \(m\ge3\):** the cone \(C_m\) of tuples \(X_i=a_iN\) with one common square-zero \(N\in M_2(k)\) and arbitrary coefficients \(a_i\). It is geometrically irreducible of dimension \(m+1\), the affine cone over the Segre–Veronese image of \(\mathbb P^1\times\mathbb P^{m-1}\) by \(\mathcal O(2,1)\).

For \(m=1\) there is one component; for \(m=2\) exactly three; for every \(m\ge3\), exactly
\[
m+\binom m2+1
\]
components. The variety is equidimensional **if and only if** \(1\le m\le3\). In particular, at three variables it has seven components of dimension four; at four variables it has ten components of dimension four and one of dimension five. It is connected because all components contain the zero tuple.

For any finite field \(\mathbb F_q\), including characteristic two, the exact number of ordered tuples is, for every \(m\ge0\),
\[
\boxed{\#\mathcal Z_m(\mathbb F_q)=1+m(q^4-1)+(q+1)(q^m-1-m(q-1))+\binom m2 q(q+1)(q-1)^2.}
\]
For \(m=0\) the variety is a point. The pair case specializes to \(3q^4-2q^2\), whereas the new higher-arity terms reflect the cone of common square-zero directions.

The same finite stratification yields an equality in the Grothendieck ring of varieties over any field, where \(\mathbb L=[\mathbb A^1]\):
\[
[\mathcal Z_m]=1+m(\mathbb L^4-1)+(\mathbb L+1)(\mathbb L^m-1-m(\mathbb L-1))+\binom m2\mathbb L(\mathbb L+1)(\mathbb L-1)^2.
\]

## Assumptions and scope

The matrices are labeled and ordered; the relations apply to distinct indices in **both orders**. A matrix may be invertible, nonnilpotent singular, nilpotent, or zero. The component statement concerns the reduced variety after passage to an algebraic closure and makes no assertion about radicality of the raw defining ideal. Every assertion holds in characteristic two as well as in other characteristics; the point formula holds for prime powers \(q\). The algebra \(R_m\) is finitely generated but generally infinite-dimensional; the representation variety is nevertheless finite-type.

## Proof

**1. Two-dimensional annihilator dichotomy.** Let \(0\ne X\in M_2(\overline k)\). If \(XY=YX=0\) with \(Y\ne0\), then \(X\) must have rank one. If \(\operatorname{tr}X\ne0\), Cayley–Hamilton gives \(X^2=(\operatorname{tr}X)X\). Writing \(P=X/\operatorname{tr}X\), the rank-one idempotent \(P\) projects onto \(\operatorname{im}X\) along \(\ker X\), and
\[
XY=YX=0\ \Longleftrightarrow\ Y=\beta(I-P)\quad\text{for some }\beta\in\overline k.
\]
For two distinct nonzero choices of \(Y\), their product is nonzero. If \(\operatorname{tr}X=0\), then rank one implies \(X^2=0\) and \(\operatorname{im}X=\ker X=L\); the same two annihilation equations force \(\operatorname{im}Y\subseteq L\subseteq\ker Y\), hence \(Y\) is a scalar multiple of \(X\), automatically square-zero. These statements use no division by two.

**2. Exhaustion.** Suppose \((X_i)\) is a solution. If an invertible matrix occurs, every other matrix vanishes, so the tuple belongs to an axis. Otherwise all nonzero matrices have rank one. If a nonnilpotent one occurs, at most one further nonzero matrix can occur, by Step 1. These tuples belong to the corresponding \(B_{ij}\) (or to an axis). If every nonzero matrix is nilpotent, Step 1 forces all of them to be multiples of one nonzero square-zero matrix, so the tuple belongs to \(C_m\). Hence the named closed loci cover the reduced variety.

**3. Irreducibility of the pair components.** Rank-one idempotents are parametrized by ordered pairs of distinct lines \((L,K)\in\mathbb P^1\times\mathbb P^1\setminus\Delta\): there is a unique projection \(P_{L,K}\) onto \(L\) along \(K\). The dense open subset of \(B_{ij}\) with both matrices nonzero and nonnilpotent consists exactly of
\[
X_i=\alpha P_{L,K},\qquad X_j=\beta(I-P_{L,K}),\qquad \alpha,\beta\in\mathbb G_m.
\]
It is irreducible of dimension \(2+2=4\). Every rank-one zero-product pair lies in its closure: nonnilpotent axes arise by setting one scalar to zero; if the nonzero matrices are nilpotent, conjugate their common direction to \(N=E_{12}\) and take
\[
P_t=\begin{pmatrix}1&t^{-1}\\0&0\end{pmatrix},\quad \alpha_t=t\alpha+t^2,\quad\beta_t=-t\beta+t^2.
\]
The pair \((\alpha_tP_t,\beta_t(I-P_t))\) tends to \((\alpha N,\beta N)\), including cases where one or both scalars are zero. Both scalar functions are nonzero over \(k(t)\), even if a limiting coefficient vanishes. This is a regular family at \(t=0\) after multiplication, so it proves Zariski closure. Thus \(B_{ij}\) is irreducible of dimension four.

**4. The nilpotent cone.** Every nonzero square-zero \(2\times2\) matrix has one line \(L=\operatorname{im}N=\ker N\). For fixed \(L\), such matrices comprise the nonzero elements of the one-dimensional space \(\operatorname{Hom}(k^2/L,L)\). The projectivization of this cone is \(\mathbb P^1\) embedded by the quadratic Veronese map, including in characteristic two. For an \(m\)-tuple of scalar multiples of such a matrix, projectivization gives \(\mathbb P^1\times\mathbb P^{m-1}\) embedded by \(\mathcal O(2,1)\). Therefore \(C_m\) is geometrically irreducible, closed and of dimension \(m+1\).

**5. Maximality and the threshold.** Each \(A_i\) contains a tuple with one invertible matrix; such a point lies in no other named locus. Each \(B_{ij}\) contains a tuple with exactly two nonzero nonnilpotent rank-one matrices; it lies in no other named locus. For \(m\ge3\), the locus \(C_m\) contains a tuple with three nonzero square-zero matrices; this point lies in no axis or pair locus. Since the closed irreducible loci cover the variety and none is included in another, they are exactly the irreducible components. Their dimensions are four except for \(\dim C_m=m+1\), giving the stated component counts and the sharp threshold.

**6. Arithmetic and motivic stratification.** Count solutions by exact number of nonzero entries. The all-zero tuple contributes one; tuples with exactly one nonzero matrix contribute \(m(q^4-1)\). For an exact support of size \(r\ge2\) consisting of nilpotents, choose the common image/kernel line (\(q+1\) possibilities) and one nonzero element of \(\operatorname{Hom}(\mathbb F_q^2/L,L)\) at each selected index (\((q-1)^r\) possibilities). These total
\[
(q+1)\sum_{r=2}^m\binom mr(q-1)^r=(q+1)(q^m-1-m(q-1)).
\]
The remaining solutions have exact support two and complementary nonnilpotent rank-one matrices. An ordered pair of distinct lines has \(q(q+1)\) possibilities; the two nonzero eigenvalues contribute \((q-1)^2\), yielding the last term of the formula. Replacing finite-field cardinalities by classes of the corresponding locally trivial strata (\(\mathbb P^1\), \(\mathbb G_m\), and \(\mathbb P^1\times\mathbb P^1\setminus\Delta\)) yields the displayed motivic identity.

## Verification

The standalone program `verify.py` enumerates all \(2\times2\) matrices over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\) and \(\mathbb F_7\), using explicit multiplication in each field. It counts admissible tuples by intersecting directly computed two-sided annihilator neighborhoods; this does not use the theorem to select legal matrices. Twenty-seven tuple-length/field configurations were checked through lengths six (depending on the field). It also individually classifies every legal tuple in selected cases \((q,m)=(2,4),(3,3),(4,3)\), confirming the predicted exact-support strata. The recorded output is `verify_output.txt`; run `python3 verify.py` to reproduce it.

## Relationship to prior work

General representation-variety methods were developed by Crawley-Boevey and Schröer, and by Huisgen-Zimmermann and Goodearl; the latter's archival paper motivates an explicit component calculation for a specific two-dimensional representation problem. The complete **pair** zero-product variety is classical, and Schröer's 2002 preprint explicitly states its rank-stratified components for arbitrary matrix size. Huang's 2021 preprint provides a finite-field generating series for **pairs** of mutually annihilating matrices across all sizes. Related classifications of **all-square-zero tuples**, requiring \(X_i^2=0\) as well as \(X_iX_j=0\), and clique counts restricted to nonzero square-zero matrices, determine only the common-nilpotent sublocus of this problem; they omit both arbitrary one-coordinate matrices and complementary nonnilpotent pair components. These antecedents settle aspects of \(m=2\) or a proper sublocus, not the complete all-arity component transition or the full formula for each \(m\ge3\) in the present fixed-size representation family. The formula at \(m=2\) is included for consistency, not claimed new. The value lies in classifying the new common-nilpotent component, identifying the first non-equidimensional arity, and obtaining the uniform higher-arity arithmetic/motivic census. Kinser and Lőrincz’s node-splitting results concern algebras in which all length-two paths through a split node vanish; here each individual loop square survives, so their stated node hypothesis does not apply. An earlier unlocated multi-branch representation result could overlap; absence of a search hit is not proof of priority.

## Limitations

The theorem is specific to \(2\times2\) matrix representations, not higher-dimensional matrix rings. It describes the **reduced** geometric components and does not establish that the full representation scheme is reduced or determine intersection multiplicities. The finite-field and motivic counts distinguish these loci as subsets but do not classify conjugacy orbits or representation-isomorphism classes. Historical publication priority is provisional, and no independent review has been performed.

## References

1. B. Huisgen-Zimmermann and K. R. Goodearl, *Irreducible components of module varieties: projective equations and rationality*, arXiv:1108.2833, first submitted 2011-08-14 (primary mathematical motivation; MSC 16G10, 16G20). https://arxiv.org/abs/1108.2833
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293, first submitted 2002-11-19 (includes the known unrestricted pair variety in the introduction). https://arxiv.org/abs/math/0211293
3. Y. Huang, *Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity*, arXiv:2110.15566, first submitted 2021-10-29 (enumerates mutually annihilating pairs over finite fields). https://arxiv.org/abs/2110.15566
4. W. Crawley-Boevey and J. Schröer, *Irreducible components of varieties of modules*, arXiv:math/0103100, first submitted 2001-03-15 (general module-variety framework). https://arxiv.org/abs/math/0103100
5. R. Kinser and A. C. Lőrincz, *Representation varieties of algebras with nodes*, arXiv:1810.10997, first submitted 2018-10-25 (node-splitting theory with different defining relations). https://arxiv.org/abs/1810.10997
