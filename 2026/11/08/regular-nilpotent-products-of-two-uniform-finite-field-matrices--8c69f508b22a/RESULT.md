# Regular-nilpotent products of two uniform finite-field matrices: exact count and persistent large-rank density

## Finding
Let \(q\) be a prime power, \(n\ge2\), and \(A,B\in M_n(\mathbb F_q)\) independent and uniformly distributed. Set
\[
L_{n,q}=\prod_{i=0}^{n-2}(q^n-q^i).
\]
The number of ordered pairs \((A,B)\) for which the product is **regular nilpotent**—meaning \((AB)^n=0\) and \((AB)^{n-1}\ne0\), or equivalently one nilpotent Jordan block—is precisely
\[
\boxed{L_{n,q}^2q^{n-1}(2q-1).}
\]
Consequently, among pairs with nilpotent product, the exact probability that the nilpotency index is the maximum possible value \(n\) is
\[
\boxed{R_{n,q}=\frac{2-q^{-1}}{2-q^{-n}}\prod_{j=2}^{n}(1-q^{-j})^2.}
\]
For each fixed \(q\), this quantity has the strictly positive limit
\[
\boxed{\lim_{n\to\infty}R_{n,q}=\left(1-\frac1{2q}\right)\prod_{j=2}^{\infty}(1-q^{-j})^2>0.}
\]
As \(q\to\infty\), uniformly for \(n\ge2\), it equals \(1-1/(2q)+O(q^{-2})\).

## Assumptions and scope
Matrices are square and sampled independently with replacement from all \(q^{n^2}\) matrices over the same finite field, **not** only invertible, upper triangular, nilpotent, or rank-constrained matrices. The field size \(q\) may be any prime power; the formula depends only on cardinality, not characteristic. The index of a nilpotent matrix is the least positive exponent at which its power vanishes. A nilpotent matrix has maximal index \(n\) precisely when it has a single size-\(n\) nilpotent Jordan block. The conditional event has positive probability for all stated parameters.

## Proof
**1. Number of target matrices.** Every regular nilpotent matrix is conjugate over \(\mathbb F_q\) to the standard nilpotent Jordan block \(J_n\) with ones on its first superdiagonal. Its invertible centralizer consists precisely of the polynomials
\[
c_0 I+c_1J_n+\cdots+c_{n-1}J_n^{n-1},\qquad c_0\ne0;
\]
this has \(q^{n-1}(q-1)\) elements. By orbit–stabilizer, the number of possible regular-nilpotent products is
\[
\frac{|\operatorname{GL}_n(\mathbb F_q)|}{q^{n-1}(q-1)}
=\prod_{i=0}^{n-2}(q^n-q^i)=L_{n,q}.
\]
Here \(|\operatorname{GL}_n(\mathbb F_q)|=\prod_{i=0}^{n-1}(q^n-q^i)\).

**2. All factorizations of a fixed Jordan block.** Fix \(AB=J_n\). Since \(\operatorname{rank}J_n=n-1\), the rank of \(A\) is either \(n\) or \(n-1\), with no other possibility.

If \(A\) is invertible, there are exactly \(|\operatorname{GL}_n(\mathbb F_q)|\) choices and, for each, the unique solution is \(B=A^{-1}J_n\).

If \(A\) has rank \(n-1\), its image must equal the fixed hyperplane \(U=\operatorname{im}J_n\), because \(\operatorname{im}J_n\subseteq\operatorname{im}A\) and the dimensions agree. Such maps are exactly the surjections \(\mathbb F_q^n\twoheadrightarrow U\). Choosing a basis for \(U\), their number is the count of full-row-rank \((n-1)\)-by-\(n\) matrices,
\[
L_{n,q}=\prod_{i=0}^{n-2}(q^n-q^i).
\]
For each such \(A\), every column of \(J_n\) has exactly \(|\ker A|=q\) preimages, independently of the other columns. Hence there are \(q^n\) compatible matrices \(B\). The total factorization fiber therefore has size
\[
|\operatorname{GL}_n(\mathbb F_q)|+q^nL_{n,q}
=q^{n-1}(2q-1)L_{n,q}.
\]

**3. Multiply all fibers.** The transformations \((A,B)\mapsto(SAS^{-1},SBS^{-1})\) send a factorization of \(J_n\) bijectively to one of \(SJ_nS^{-1}\), so every regular nilpotent target has the same fiber size. Multiplying by the \(L_{n,q}\) target matrices gives
\[
T_{n,q}=q^{n-1}(2q-1)L_{n,q}^2.
\]

**4. Condition on nilpotency.** The classical matrix-product nilpotence probability (already known, and not claimed here) is
\[
\Pr(AB\text{ nilpotent})=1-(1-q^{-n})^2
=2q^{-n}-q^{-2n}.
\]
Thus the nilpotent-product pair count is \(q^{2n^2-2n}(2q^n-1)\). Using
\[
L_{n,q}=q^{n(n-1)}\prod_{j=2}^{n}(1-q^{-j}),
\]
we divide \(T_{n,q}\) by the nilpotent-product pair count to obtain
\[
R_{n,q}=\frac{2-q^{-1}}{2-q^{-n}}\prod_{j=2}^{n}(1-q^{-j})^2.
\]

**5. Limits.** For fixed \(q\ge2\), the positive infinite product exists and is nonzero because \(\sum_{j=2}^{\infty}q^{-j}<\infty\). Therefore the fixed-field \(n\to\infty\) limit exists and is strictly positive. For \(q\to\infty\), the product differs from one by \(O(q^{-2})\) uniformly in the upper endpoint \(n\); also \((2-q^{-n})^{-1}=1/2+O(q^{-2})\) uniformly for \(n\ge2\). Hence \(R_{n,q}=1-1/(2q)+O(q^{-2})\) uniformly. Every step uses exact integer counts or uniform elementary estimates.

## Verification
Run \(`python3 verify_regular.py`\) from this package and compare standard output with `regular_output.txt`. The standalone checker enumerates all \(334{,}497\) ordered matrix pairs over \((q,n)=(2,2),(3,2),(4,2),(2,3)\), including extension-field arithmetic for \(\mathbb F_4\). It separately enumerates all \(262{,}144\) pairs over \(\mathbb F_2\) in dimension three to check the factorization fiber of the standard nilpotent Jordan block, and algebraically compares two expressions for the closed probability at \(203\) parameter pairs. No finite experiment replaces the all-parameter proof above. Typical exact counts are \(54\) regular-product pairs among \(256\) pairs for \((q,n)=(2,2)\), and \(960\) among \(6{,}561\) for \((q,n)=(3,2)\).

## Relationship to prior work
Sarma and Subedi's 2026 treatment of nilpotent product probability motivates asking for strata within the nilpotent event; it gives a union event, not the maximal-index stratum. Kovács's 1987 *Some enumeration problems for matrices over a finite field* gives the general \(k\)-factor nilpotency probability and idempotency probabilities, according to its accessible abstract; that supplies background for the conditioning denominator. The full 1987 article was not inspected, so implicit treatment of the more refined event is a priority risk. Fine–Herstein-style enumeration of nilpotent matrices concerns single uniform matrices and is not the factorization-weighted distribution of a product. Classical Jordan-form and centralizer results are used as known mathematical inputs. Separate earlier counts for **upper triangular** products with maximal nilpotency index concern a genuinely different sampling model. Their index-\(n\) conditional mass can decay exponentially with dimension, unlike the strictly positive limit proved here for **all** matrix factors. No claim of universal publication priority or independent certification is made.

## Limitations
The theorem computes only the regular-nilpotent (single Jordan-block) stratum conditional on nilpotency; it does not give the entire distribution of nilpotency indices, all Jordan partitions, fixed product matrices outside that conjugacy class, nonuniform factors, or products of three or more factors. The exact large-rank constant is specific to two unrestricted full-matrix factors. Historical originality is not a proof of absence from older matrix-product literature, especially an inaccessible full text of Kovács's 1987 work and his 1988 article *Products of matrices over a finite field*. Independent mathematical audit has not been performed.

## References
1. D. Sarma and T. Subedi, *Nilpotent Product Probability of Finite Rings*, arXiv:2610.07892v1 (first public October 6, 2026).
2. A. Kovács, *Some enumeration problems for matrices over a finite field*, Linear Algebra and its Applications **94** (1987), 223–236.
3. A. Kovács, *Products of matrices over a finite field*, Illinois Journal of Mathematics (1988), accessed bibliographic description only.
4. A. Kovács, *On the probability that the product of k n-by-n matrices over a finite field will be zero*, Journal of Combinatorial Theory A (1987), DOI:10.1016/0097-3165(87)90019-7.
