# Lucas congruences govern maximal adjoint Jordan chains in niltriangular Lie algebras

## Finding
Let \(k=\mathbb F_q\) be any finite field with \(q=p^f\), \(n\ge3\), and \(L=\mathfrak n_n(k)\) the Lie algebra of strictly upper-triangular \(n\times n\) matrices, with \([A,B]=AB-BA\). Write \(D_X(Y)=[X,Y]\), \(d=n(n-1)/2\), \(m=n-1\) and
\[
 I=\{i\in\{1,\ldots,m\}:\binom{n-2}{i-1}\not\equiv0\pmod p\},\qquad M=|I|.
\]
If \(n-2=\sum_{j=0}^r b_jp^j\), then \(M=\prod_{j=0}^r(b_j+1)\). For each \(X\in L\), \(D_X^{n-1}=0\), and there is at most one Jordan block of length \(n-1\). The following conditions are equivalent:

1. \(D_X\) has a Jordan block of length \(n-1\).
2. \(D_X^{n-2}\ne0\).
3. Writing \(a_i=X_{i,i+1}\), either every \(a_i\) is nonzero, or exactly one is zero and its index belongs to \(I\).

The number of such elements and its probability under the uniform distribution on \(L\) are exactly
\[
 \boxed{N_{n,q}=q^{d-m}(q-1)^{m-1}(q-1+M)},\qquad
 \boxed{\Pr(D_X^{n-2}\ne0)=\frac{(q-1)^{m-1}(q-1+M)}{q^m}}.
\]
Thus a maximal Jordan block exists in every characteristic and dimension, but its frequency depends on the base-\(p\) digits of \(n-2\).

There is also a scheme-theoretic statement over any field of characteristic \(p\), independent of finite-field cardinality. The zero scheme \(Z_{n,p}\) of the matrix entries of \(D_X^{n-2}\) is a reduced union of coordinate affine subspaces. With \(J=\{1,\ldots,m\}\setminus I\), its irreducible components are exactly
\[
 H_j=\{X:a_j=0\}\quad(j\in J),\qquad
 P_{ik}=\{X:a_i=a_k=0\}\quad(i<k,\ i,k\in I).
\]
All the coordinates beyond the first superdiagonal are unconstrained. Consequently the number of irreducible components is
\[
 \boxed{|J|+\binom M2=m-M+\binom M2}.
\]
The codimension of \(Z_{n,p}\) is one if \(J\ne\varnothing\), and two if \(J=\varnothing\). The latter condition holds **exactly** when \(n-1=c p^r\) for some integer \(r\ge0\) and \(1\le c\le p-1\). In particular, the dimension of the nonmaximal-index locus alternates between \(d-1\) and \(d-2\) along an explicit infinite sequence of ambient sizes in every fixed positive characteristic.

## Assumptions and scope
The theorem concerns the Jordan form of \(D_X\) **on the Lie algebra \(L\)**, not the Jordan form of the \(n\times n\) matrix \(X\) on its defining vector space. It covers all prime powers, including characteristic two and extension fields, and all integers \(n\ge3\). The geometric assertion refers to the full zero scheme of the \(d\times d\) matrix of \(D_X^{n-2}\), without taking a reduced support in advance. No claim is made for arbitrary Borel nilradicals of other root systems, nor for the entire Jordan partition of \(D_X\).

## Proof
**Step 1: the top adjoint power has rank at most one.** For each \(s\ge1\), let \(F^s\subseteq L\) be the vector space of strictly upper-triangular matrices with all entries \(X_{ij}=0\) whenever \(j-i<s\). The associative product satisfies \(F^rF^s\subseteq F^{r+s}\); therefore \([L,F^s]\subseteq F^{s+1}\), and \(F^{n-1}=k E_{1n}\), \(F^n=0\). It follows that \(D_X^{n-2}(L)\subseteq kE_{1n}\) and \(D_X^{n-1}=0\). An operator killed by its \((n-1)\)-st power has one block of size \(n-1\) for every rank-one contribution to its \((n-2)\)-nd power. Here that contribution is at most one.

**Step 2: calculate every potentially nonzero column.** In the full matrix algebra, the commuting left- and right-multiplication operators give the binomial identity, valid over \(\mathbb Z\) and hence in any characteristic,
\[
 D_X^s(Y)=\sum_{t=0}^s(-1)^t\binom st X^{s-t}YX^t.
\]
Taking \(s=n-2\), an input in \(F^2\) is killed because its image lies in \(F^n\). Hence it suffices to use \(Y=E_{i,i+1}\), \(1\le i\le m\). For a term \(X^{s-t}E_{i,i+1}X^t\) to have a nonzero \((1,n)\)-entry, the left factor must connect \(1\) to \(i\) and the right factor \(i+1\) to \(n\). Their minimum required lengths are respectively \(i-1\) and \(n-i-1\), whose sum is exactly \(s\). Thus only \(t=n-i-1\) contributes and the paths must take single steps throughout. Denoting \(a_j=X_{j,j+1}\), we obtain the **exact** formula
\[
 \boxed{D_X^{n-2}(E_{i,i+1})=(-1)^{n-i-1}\binom{n-2}{i-1}\prod_{\substack{1\le j\le m\\j\ne i}}a_j\ E_{1n}.}
\]
In particular all entries beyond the first superdiagonal of \(X\) disappear from this power. The matrix of \(D_X^{n-2}\) has precisely the displayed potentially nonzero coefficients, all in its one central output row.

**Step 3: count maximal-block elements.** The displayed coefficient at index \(i\) is nonzero iff \(i\in I\) and all \(a_j\) for \(j\ne i\) are nonzero. This is equivalent to the two alternatives in the finding. There are \((q-1)^m\) fully nonzero tuples and \(M(q-1)^{m-1}\) tuples having a single zero at a permitted index; the two sets are disjoint. The other \(d-m\) entries of \(X\) are arbitrary, proving both finite-field formulas. Lucas's congruence \(\binom sk\not\equiv0\pmod p\) iff each base-\(p\) digit of \(k\) does not exceed the corresponding digit of \(s\) proves \(M=\prod(b_j+1)\).

**Step 4: determine the full zero scheme and its components.** The equations of \(D_X^{n-2}=0\), up to nonzero scalars, generate the squarefree monomial ideal
\[
 \mathcal I=(\prod_{j\ne i}a_j:i\in I)\ \subseteq\ k[a_1,\ldots,a_m,\text{higher-diagonal variables}].
\]
A point of its zero set has either (a) a zero at some \(j\in J\), or (b) at least two zeros indexed by \(I\). Indeed, with no zero in \(J\), fewer than two zeros in \(I\) would leave at least one allowed product nonzero. Conversely, either (a) or (b) kills all generators. Each squarefree monomial ideal is radical (membership of a monomial power implies membership of that monomial), so this set-theoretic description is scheme-theoretic. Its minimal monomial primes are exactly \((a_j)\) for \(j\in J\), and \((a_i,a_k)\) for distinct \(i,k\in I\), with no containment between these primes. This proves the irreducible-component list and counts.

**Step 5: locate the modular codimension transition.** The set \(J\) is empty precisely if every binomial coefficient \(\binom{n-2}{j}\), \(0\le j\le n-2\), is nonzero modulo \(p\). Lucas's digit criterion says this is precisely when every base-\(p\) digit of \(n-2\) below the most significant digit is \(p-1\). Equivalently \(n-2=c p^r-1\) for some \(1\le c\le p-1\), proving the claimed congruence characterization. Since \(M\ge2\) for \(n\ge3\), the pair components always exist, giving codimension two when \(J\) is empty.

## Verification
The companion standalone `check_pascal_adjoint.py` computes iterated matrix commutators, not merely the binomial formula. It exhaustively tests every first-superdiagonal assignment in eighteen \((q,n)\) instances: \((2,3),\ldots,(2,9)\); \((3,3),\ldots,(3,7)\); \((4,4),\ldots,(4,6)\); \((5,4),(5,5),(9,4)\). It additionally tests forty randomly chosen assignments of the higher-diagonal entries in each instance. The field implementations include \(\mathbb F_4\) and \(\mathbb F_9\). All displayed top-power coefficients, zero/nonzero decisions and exact counts agree; the complete console output is embedded as `check_pascal_adjoint_output.txt`. These finite computations verify representative specializations, **not** the infinite theorem; the proof above establishes the general assertion.

As a known boundary check, the \(n=5\) case recovers the previously recorded joint rank-power census: \(M=2\) when \(p=3\), giving \(q^6(q-1)^3(q+1)\) maximal blocks and three nonmaximal-locus components with two codimension-one components; for all other primes \(M=4\), giving \(q^6(q-1)^3(q+3)\) maximal blocks and six codimension-two components. This boundary is credited as previously determined, not claimed new.

## Relationship to prior work
The binomial identity for adjoint powers and Lucas's theorem are classical ingredients. Bolsinov–Zhang, *Jordan–Kronecker invariants of finite-dimensional Lie algebras* (2012), discusses generic adjoint operators but develops coadjoint pencils rather than this finite-field niltriangular maximal-Jordan census. Cagliero–Szechtman, *Jordan–Chevalley decomposition in Lie algebras* (2015), works in characteristic zero on solvable matrix Lie algebras and does not give the positive-characteristic top-adjoint-rank distribution. Fuchs–Kirillov, *Jordan types of triangular matrices over a finite field* (2022), counts Jordan partitions of \(X\) itself, which are not the Jordan partitions of \(\operatorname{ad}_X\). The 2022 *Strongly Ad-Nilpotent Elements of the Lie Algebra of Upper Triangular Matrices* concerns ad-nilpotence and similarity classification over complex upper-triangular algebras rather than finite-field counts and the modular zero scheme. An earlier \(n=5\) calculation already establishes the special characteristic-three component behavior; the contribution here is its complete all-\(n\) Lucas-controlled extension with a universal exact cardinality and geometry.

## Limitations
Only the maximal possible Jordan-block length of \(D_X\) and its associated nonmaximal locus are classified; other Jordan-block multiplicities are not determined. The theorem is about type-A strictly upper-triangular Lie algebras, not general nilpotent Lie algebras. The original-comparison assessment is based on accessible literature and mathematical records, and does not exclude an unindexed older derivation of the same binomial-monomial criterion. An independent audit has not been performed.

## References
1. A. V. Bolsinov and P. Zhang, *Jordan–Kronecker invariants of finite-dimensional Lie algebras*, preprint first posted 2012-11-02, https://arxiv.org/abs/1211.0579.
2. L. Cagliero and F. Szechtman, *Jordan–Chevalley decomposition in Lie algebras*, preprint first posted 2015-12-30, https://arxiv.org/abs/1512.09096.
3. D. Fuchs and A. Kirillov, *Jordan types of triangular matrices over a finite field*, preprint first posted 2022-03-31, https://arxiv.org/abs/2204.00066.
4. *Strongly Ad-Nilpotent Elements of the Lie Algebra of Upper Triangular Matrices*, 2022, https://doi.org/10.1155/2022/3484381.
5. Classical Lucas congruence for binomial coefficients modulo primes; the proof above needs only the standard digitwise nonvanishing criterion.
