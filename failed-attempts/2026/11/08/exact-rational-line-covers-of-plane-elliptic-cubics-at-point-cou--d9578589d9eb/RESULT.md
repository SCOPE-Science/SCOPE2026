# Exact rational-line covers of plane elliptic cubics at point counts divisible by three

## Finding

Let \(E\subset\mathbb P^2_{\mathbb F_q}\) be a smooth plane cubic with an \(\mathbb F_q\)-rational flex \(O\), and put \(G=E(\mathbb F_q)\) and \(N=|G|\). Assume \(3\mid N\). Write \(\operatorname{cov}(E)\) for the minimum number of distinct \(\mathbb F_q\)-rational projective lines whose union contains every point of \(E(\mathbb F_q)\). Then

\[
\operatorname{cov}(E)=
\begin{cases}
N/3,&\text{if }G\text{ has no unique nonzero element of order }2,\\
N/3+1,&\text{if }G\text{ has exactly one nonzero element of order }2.
\end{cases}
\]

Thus the elementary degree-three lower bound is attained exactly when the finite elliptic-curve group has no unique involution. The unique-involution case has a sharp additive deficit of one, independent of the field size.

## Assumptions and scope

The field \(\mathbb F_q\) is any finite field; its characteristic is unrestricted. The embedded curve is smooth and geometrically integral. The choice of an \(\mathbb F_q\)-rational flex makes the plane embedding an embedding by \(|3O|\), so the chord-and-tangent group law says three **distinct** rational points lie on a rational line precisely when their sum is \(O\). The theorem assumes the exact arithmetic condition \(3\mid|E(\mathbb F_q)|\); it does not assert a formula outside this condition. The cover counts rational lines, not lines over an extension field.

## Proof

**1. Degree and equality obstruction.** A projective line has at most three distinct intersections with the smooth cubic. Therefore any cover has at least \(N/3\) lines. If exactly \(N/3\) lines suffice, each meets the rational curve in exactly three distinct points and their intersection sets form a partition of \(G\) into disjoint zero-sum triples. Summing every triple gives

\[\sum_{g\in G}g=O.\]

Pairing \(g\) with \(-g\) shows that this group sum is \(O\) unless there is a unique nonzero element \(t\) of order two, in which case the sum is \(t\ne O\). Indeed, the order-two subgroup is an elementary two-group; its elements sum to zero except when its rank is one. Consequently, in the unique-involution case equality in the lower bound is impossible, and integrality yields \(\operatorname{cov}(E)\ge N/3+1\).

**2. The zero-sum partition case.** A theorem on equal-size zero-sum partitions of finite abelian groups (Cichacz, Theorem 12) states that whenever \(3\mid|G|\), \(G\) admits a partition into disjoint triples summing to its identity if and only if its order is odd or it has more than one involution. These two alternatives are precisely the condition that \(G\) has no unique involution. Each triple consists of three distinct points and is collinear by the chord-and-tangent law. Its joining line is defined over \(\mathbb F_q\) because it contains two rational points. The resulting \(N/3\) lines cover \(G\), giving equality in this case.

**3. The unique-involution upper bound.** Suppose \(G\) has a unique involution and \(3\mid N\). Then \(N\) is divisible by six. A finite abelian group of order divisible by three has a surjective homomorphism \(\chi:G\to\mathbb Z/3\mathbb Z\). Set \(H=\ker\chi\) and \(m=|H|=N/3\); choose \(a\in G\) with \(\chi(a)=1\). The three cosets \(H\), \(a+H\) and \(-a+H\) partition \(G\).

By the near-transversal theorem for finite group Cayley tables (Goddyn--Halasz, Theorem 2), there are \(m-1\) pairs \((h_i,k_i)\in H\times H\) such that the first coordinates \(h_i\), the second coordinates \(k_i\), and the sums \(h_i+k_i\) are each pairwise distinct. For each pair consider

\[
T_i=\{h_i,\ a+k_i,\ -a-h_i-k_i\}.
\]

The three elements of \(T_i\) lie in different cosets and sum to \(O\). Different triples are disjoint because the row, column and symbol entries of the near transversal are distinct. Hence these \(m-1\) triples cover exactly \(3(m-1)=N-3\) points, and their \(m-1\) rational lines cover the same points. Three rational points remain. One rational line through two of them and one rational line through the third cover the rest, whether or not the first line also meets the third. Therefore \(\operatorname{cov}(E)\le(m-1)+2=m+1=N/3+1\), matching the lower bound.

**4. Explicit cyclic construction.** When \(G\cong\mathbb Z/(6k)\), the preceding near-cover can be made entirely explicit. For every integer \(0\le i\le2k-2\) put \(j_i=i\) if \(i<k\), and \(j_i=i+1\) otherwise; take \(\ell_i\) to be the unique residue in \(\{0,\ldots,2k-1\}\) congruent to \(-1-i-j_i\pmod{2k}\). Then

\[
\{3i,\ 3j_i+1,\ 3\ell_i+2\}
\quad(0\le i\le2k-2)
\]

are \(2k-1\) disjoint zero-sum triples in \(\mathbb Z/(6k)\). The three omitted residues are \(3(2k-1)\), \(3k+1\) and \(2\), whose sum is the unique involution \(3k\). This gives a concrete family of optimal covers in the cyclic unique-involution case.

## Verification

The accompanying standalone `verify.py` checks the explicit cyclic construction for \(1\le k\le500\) using exact integer arithmetic. It also enumerates all rational points and projective lines for six small smooth Weierstrass cubics, then calculates the **exact** minimum covering number by exhaustive dynamic programming on subsets of the rational point set. The six examples include both possible involution cases, and use fields with \(q\in\{5,7,11\}\). Run `python verify.py` using only the Python standard library. These finite checks support but do not replace the three general arguments above, whose external group-theoretic inputs are precisely identified.

## Relationship to prior work

Asgarli--Dassarma--Ghioca--MacLean--Stokdyk introduce the rational-line covering number and, in their discussion of smooth plane cubics, obtain \(N/3+O(1)\) for odd point counts using zero-sum partitions [1, Introduction]. They do not state the exact two-case formula above. Cichacz [2, Theorem 12] already proves the group-theoretic existence criterion for partitioning a finite abelian group into zero-sum triples. Goddyn--Halasz [3, Theorem 2] already proves the group Cayley-table near-transversal theorem. The contribution here is their combination with the plane-cubic line-covering problem, in particular the exact one-line defect for unique-involution groups and its all-field sharp construction. This result is an application of, not a strengthening of, either group-theoretic theorem. Earlier work on orchards in elliptic curves [4] studies the number of collinear triples rather than the minimum line cover.

## Limitations

The formula is restricted to smooth embedded plane elliptic cubics with a rational flex and point count divisible by three. The proof invokes two published existence theorems rather than reproving those theorems. It neither classifies all optimal covers nor gives a formula when \(3\nmid N\). Completeness of historical priority beyond the inspected literature is not guaranteed.

## References

[1] S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean and E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (first submitted 2026-10-09), introduction, especially discussion of smooth cubics.

[2] S. Cichacz, *Zero sum partition of Abelian groups into sets of the same order and its applications*, Electronic Journal of Combinatorics 25(1) (2018), Paper P1.20, Theorem 12. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v25i1p20/pdf/

[3] L. Goddyn and K. Halasz, *All group-based latin squares possess near transversals*, arXiv:1905.07071v2 (2019), Theorem 2.

[4] K. Padmanabhan and A. Shukla, *Orchards in elliptic curves over finite fields* (2020), study of collinear-triple configurations.
