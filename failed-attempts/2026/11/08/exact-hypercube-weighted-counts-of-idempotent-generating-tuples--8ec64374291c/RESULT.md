# Exact hypercube-weighted counts of idempotent generating tuples in finite triangular algebras

## Finding
For every finite field \(k=\mathbb F_q\), integer \(n\ge2\), and integer \(m\ge2\), let \(T_n(k)\) be the unital algebra of upper triangular \(n\)-by-\(n\) matrices, and let \(G_{n,m}(q)\) count **ordered** \(m\)-tuples of idempotents that generate \(T_n(k)\) as a unital \(k\)-algebra. For an ordered list of binary words \(b_1,\ldots,b_n\in\{0,1\}^m\), write \(h_{ij}=d_H(b_i,b_j)\) for Hamming distance. Then the complete exact finite-sum enumeration is

\[
G_{n,m}(q)=\sum_{\substack{(b_1,\ldots,b_n)\in(\{0,1\}^{m})^n\\ b_i\ne b_j\ (i\ne j)}}q^{\sum_{1\le i<j-1\le n-1}h_{ij}}\prod_{i=1}^{n-1}\bigl(q^{h_{i,i+1}}-q\bigr).
\]

The exponent is precisely the sum of Hamming distances over all **nonadjacent** index pairs \((i,j)\) with \(j-i\ge2\); this latter description also defines the formula when \(n=2\) (empty sum). A term is zero when two consecutive words differ in one coordinate. The formula is valid in characteristic two.

In particular,
\[
\begin{aligned}
G_{2,2}(q)&=4q(q-1),\\
G_{3,3}(q)&=48q^3(q-1)^2(2q+1),\\
G_{4,3}(q)&=24q^6(q-1)^3(4q^3+7q^2+7q+2),\\
G_{5,3}(q)&=48q^{11}(q-1)^4(q+1)(9q^2+3q+2).
\end{aligned}
\]

The count is positive exactly when \(m=2,n=2\), or when \(m\ge3\) and \(2\le n\le2^m\). The positivity threshold itself is a known minimum-generator phenomenon; the new assessed contribution is the exact number of **labeled ordered tuples** in every parameter range, together with its explicit Hamming-distance weights.

## Assumptions and scope
All fields are finite fields of prime-power order \(q\ge2\). The matrices are upper triangular in a **fixed ordered basis**, without quotienting by conjugation or permutation of generators; the identity is allowed in a tuple. Algebra generation includes arbitrary finite sums, products, scalar multiplication and the identity. The binary word \(b_i\) records the \(i\)-th diagonal entries of the \(m\) idempotents. This theorem does not count tuples of arbitrary matrices or just unordered sets of generators.

## Proof
**Lemma 1 (idempotent parameterization).** For one prescribed binary diagonal \(\delta_1,\ldots,\delta_n\), the entries \(p_{ij}\) of an upper triangular idempotent \(P\) with \(i<j\) and \(\delta_i\ne\delta_j\) can be selected independently and arbitrarily in \(k\); every remaining strict upper diagonal entry is determined uniquely by them. Indeed, the \((i,j)\)-entry of \(P^2-P=0\) reads
\[
(\delta_i+\delta_j-1)p_{ij}+\sum_{i<r<j}p_{ir}p_{rj}=0.
\]
When \(\delta_i=\delta_j\), the coefficient is \(+1\) or \(-1\), and gives a unique solution. When \(\delta_i\ne\delta_j\), the coefficient vanishes but the remaining sum vanishes automatically: the identity \([P,P^2-P]=0\), together with vanishing of all shorter-distance equations, forces \((\delta_i-\delta_j)(P^2-P)_{ij}=0\). Since \(\delta_i-\delta_j\) is a unit, the present equation imposes no constraint. Induction on \(j-i\) proves the lemma over every characteristic. In particular, fixing any compatible first superdiagonal leaves exactly one free field parameter for each nonadjacent opposite-diagonal pair.

**Lemma 2 (generation test).** Let \(A_1,\ldots,A_m\in T_n(k)\), let \(c_i\in k^m\) be their joint diagonal vector at position \(i\), and let \(u_i\in k^m\) be their joint first-superdiagonal vector at \((i,i+1)\). They generate \(T_n(k)\) if and only if (a) the \(c_i\) are pairwise distinct, and (b) \(u_i\notin k(c_i-c_{i+1})\) for each \(i<n\).

To see necessity, the diagonal quotient \(T_n/J\cong k^n\) is generated precisely if its evaluation characters are distinct (finite-field multivariable interpolation). In each adjacent two-by-two quotient, if \(u_i\) is a scalar multiple of \(c_i-c_{i+1}\), every generator is simultaneously conjugate to a diagonal matrix by a single upper unipotent matrix, and the image is not the whole triangular two-by-two algebra. Conversely, (a) implies the generated algebra \(B\) surjects onto \(k^n\). Its Jacobson radical is \(B\cap J\); idempotent lifting in the finite-dimensional split algebra \(B\) gives orthogonal primitive idempotents projecting to each diagonal coordinate. After simultaneous conjugation by one invertible upper triangular matrix, these idempotents are the diagonal units \(E_{ii}\). The adjacent condition (b) forces each adjacent block \(E_{i,i+1}\) to lie in the conjugated algebra. Their products yield all \(E_{ij}\), so the conjugated algebra is \(T_n(k)\), as required. This argument works for any finite field, including fields of characteristic two.

**Counting.** For idempotent generators, the joint diagonal vectors \(c_i\) are exactly the binary words \(b_i\). Given distinct words, the vector \(u_i\) has zero entries in the coordinates where consecutive bits agree, and otherwise is arbitrary. Thus \(u_i\) lies in a coordinate subspace of dimension \(h_{i,i+1}\), containing \(c_i-c_{i+1}\ne0\). Of its \(q^{h_{i,i+1}}\) possible values, exactly \(q\) lie on the forbidden one-dimensional span. By Lemma 1, after choosing the adjacent entries, all remaining entries in all \(m\) idempotents contribute independently the factor
\[
q^{\sum_{\substack{1\le i<j\le n\\ j-i\ge2}}h_{ij}}.
\]
Multiplying the \(n-1\) adjacent factors and summing over all injective lists of binary words proves the displayed count. The special polynomials follow from finite symbolic expansion of the explicit sum; the included standalone code proves these finite polynomial identities by symbolic coefficient expansion over all admissible word tuples; evaluations at four field orders provide additional checks.

For positivity, the adjacent differences must have Hamming distance at least two. With \(m=2\), the distance-at-least-two graph has two disjoint edges, so its longest simple path has two vertices. With \(m\ge3\), the complement of the \(m\)-cube graph has a spanning path: list the even-parity words, ending with the zero word, followed by odd-parity words, starting with a word of Hamming weight three. Any two distinct words of a common parity have distance at least two; the joining step has distance three. Every prefix gives a suitable word list of length \(n\le2^m\). This completes all cases.

## Verification
The standalone, standard-library script `verify_generating_idempotents.py` independently enumerates literal upper triangular matrices, tests idempotence and algebra generation via iterative multiplication and finite-field linear rank, and compares with the word-weight formula. It exhaustively checks all ordered tuples for \((n,q,m)=(2,2,2),(2,3,2),(2,4,2),(3,2,3)\), obtaining respectively \(8,24,48,1920\) generating tuples. It also checks 320 deterministic random three-tuples at \((n,q)=(4,2)\) and evaluates the three displayed higher-degree polynomials for \(q=2,3,4,5\). The extension field \(\mathbb F_4\) uses an explicit irreducible quadratic, not integer arithmetic modulo four. The script also expands each of the three displayed higher-degree identities as a symbolic polynomial over the integers and compares every coefficient, independently of evaluating at finitely many field orders. The stored output ends with `ALL_IDEMPOTENT_GENERATOR_CHECKS_PASS`. Exact finite tests corroborate the unrestricted two-lemma proof; sampling does not establish a universal statement.

## Relationship to prior work
Kelarev, van der Merwe and van Wyk (1998), *The Minimum Number of Idempotent Generators of an Upper Triangular Matrix Algebra*, established the **minimum number** needed to generate, including its sharp hypercube bound. Their entire accessible article was compared; its minimum-generation and constructive statements are not an exact labeled-tuple enumeration. The present positivity condition is credited as known and is not offered as the original claim.

Kolegov (2024), *Idempotent Generators of Incidence Algebras*, obtains analogous minimum numbers over commutative rings and describes the complement-of-hypercube criterion. Only its accessible abstract and bibliographic material could be inspected, so unforeseen stronger formulas in the inaccessible full text remain a priority risk. Gargate and Gargate (2020), *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras*, enumerate individual potent matrices, not generating tuples. Kolegov (2025), *On the Probability of Generating Matrix Incidence Rings*, gives the unrestricted random-matrix generation probability, which does not condition all generators to be idempotent. An independent weighted generating-tuple formula would be potentially dominating, but was not identified in the sources inspected.

## Limitations
This counts ordered idempotent generating tuples in the full chain algebra \(T_n(\mathbb F_q)\), not isomorphism classes, similarity-orbits, general incidence posets, nonfield coefficient rings, or tuples generating a proper subalgebra. The short symbolic specializations do not replace the complete finite-sum theorem. Independent mathematical validation and exhaustive historical priority checks have not been carried out. Full-text access to Kolegov's 2024 paper was unavailable, leaving residual originality risk.

## References
1. A. V. Kelarev, A. B. van der Merwe, L. van Wyk, *The Minimum Number of Idempotent Generators of an Upper Triangular Matrix Algebra*, Journal of Algebra **205** (1998), 605–616, doi:10.1006/jabr.1997.7405.
2. N. A. Kolegov, *Idempotent Generators of Incidence Algebras*, Bulletin of the Australian Mathematical Society **110** (2024), 488–497, doi:10.1017/S0004972724000078.
3. I. Gargate, M. Gargate, *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243 (2020).
4. N. A. Kolegov, *On the Probability of Generating Matrix Incidence Rings*, arXiv:2509.00252 (2025).
