# Exact enumeration of dominating–locating-dominating partitions of cycles

## Finding

Let \(c_n\) be the number of **ordered, labelled** partitions \(V(C_n)=D\mathbin{\dot\cup}L\), where \(D\) is dominating and \(L\) is locating-dominating, for the simple cycle on \(n\ge3\) vertices. Then

\[
\boxed{\sum_{n\ge3}c_n z^n=-z\frac{d}{dz}\log(1-z^2-z^3-z^4-z^5-z^6)-2z^2-2z^4.}
\]

For every \(n\ge5\), encode the membership of vertex \(i\) by \(b_i=0\) for \(D\) and \(b_i=1\) for \(L\). The partition is valid if and only if the cyclic binary word avoids all three patterns \(000\), \(111\), and \(00100\). For \(n=3\), there are \(c_3=3\) partitions. For \(n=4\), there are \(c_4=4\): the two alternating words satisfy those forbidden-word rules but are invalid.

Writing \(\rho\) for the unique solution in \((0,1)\) of \(\rho+\rho^3+\rho^5=1\), the count satisfies
\[
\boxed{c_n\sim \rho^{-n},\qquad \rho^{-1}\approx1.57014731219605.}
\]
In particular, the proportion \(c_n/2^n\) of all ordered vertex bipartitions tends exponentially to zero, although valid partitions exist for every length. The initial counts for lengths \(3\) through \(16\) are \(3,4,10,17,21,38,57,92,143,225,351,555,868,1366\).

## Assumptions and scope

The graph \(C_n\) is the simple undirected cycle with *distinguished labelled vertices* \(0,1,\ldots,n-1\), with indices read modulo \(n\) and \(n\ge3\). A set \(S\) is dominating if each vertex outside \(S\) has a neighbour in \(S\). It is locating-dominating if it is dominating and the sets \(N(u)\cap S\), for distinct vertices \(u\) outside \(S\), are pairwise distinct. Here \(N(u)\) denotes the **open** neighbourhood. The two parts are distinguished, so exchanging them is not an identification. No quotient by rotations or reflections is taken.

## Proof

**1. Exact local characterization.** Since \(D\) must dominate \(L\), three consecutive vertices in \(L\) are forbidden: the cyclic pattern \(111\) cannot occur. Since \(L\) must dominate \(D\), the pattern \(000\) cannot occur. Fix \(n\ge5\). If two distinct vertices \(u,v\in D\) have equal nonempty sets of neighbours in \(L\), those two signatures must be singletons: two distinct vertices of \(C_n\) have at most one common neighbour for \(n\ge5\). Thus there is a vertex \(w\in L\) such that \(u=w-1\), \(v=w+1\), while their other neighbours \(w-2\) and \(w+2\) lie in \(D\). These five vertices are distinct for \(n\ge5\), and their consecutive membership pattern is \(00100\). Conversely, every occurrence of \(00100\) gives exactly such a pair with equal singleton signatures. Hence all three forbidden patterns are necessary and sufficient.

The triangle and square are checked directly against the open-neighbourhood definition. The triangle has precisely three partitions, each with one vertex in \(D\). The square has precisely four, represented by the cyclic rotations of \(0011\); the alternating words \(0101\) and \(1010\) satisfy the three pattern exclusions but give opposite vertices of \(D\) identical \(L\)-signatures. There are no other exceptions at these lengths.

**2. Runs and a two-state transfer matrix.** In every cyclic word avoiding \(000\) and \(111\), maximal zero-runs and maximal one-runs alternate, and each has length \(1\) or \(2\). Let \(a_i\in\{1,2\}\) be the length of the \(i\)-th zero-run and \(b_i\in\{1,2\}\) the length of the following one-run. The pattern \(00100\) occurs precisely when a one-run of length \(1\) lies between two zero-runs both of length \(2\). Thus, with consecutive zero-run lengths indexed by \(a,a'\), the allowed contribution is \(z^a(z+z^2)\), except for \(a=a'=2\) when it is \(z^4\). The resulting transfer matrix is

\[
M(z)=\begin{pmatrix}
z^2+z^3 & z^2+z^3\\
z^3+z^4 & z^4
\end{pmatrix},\qquad
\det(I-M(z))=1-z^2-z^3-z^4-z^5-z^6.
\]

For a cycle with \(k\) zero-runs, \(\operatorname{tr}(M(z)^k)\) counts cyclic ordered run-data with one distinguished zero-run. The weight of each word is \(z^n\), where \(n\) is the number of vertices. A fixed labelled word has \(k\) choices for its distinguished zero-run and \(n\) possible absolute starting vertex positions; therefore, the coefficient of \(z^n\) contributed by \(k\) runs equals \((n/k)[z^n]\operatorname{tr}(M(z)^k)\). Consequently, summing over all positive \(k\) gives

\[
\sum_{k\ge1}\frac{z}{k}\frac{d}{dz}\operatorname{tr}(M(z)^k)
=-z\frac{d}{dz}\log\det(I-M(z)).
\]

This formal power-series identity follows from \(-\log\det(I-M)=\sum_{k\ge1}\operatorname{tr}(M^k)/k\), valid because every entry of \(M\) has positive \(z\)-valuation. The transfer count contributes two purely formal length-two words \(01\) and \(10\), for which there is no simple \(C_2\): subtract \(2z^2\). It also includes precisely the two alternating length-four words rejected in step 1: subtract \(2z^4\). At length three it agrees with the direct count. This proves the generating function for the entire specified range.

**3. Exponential asymptotic.** Factor the determinant:
\[
1-z^2-z^3-z^4-z^5-z^6=(1+z)(1-z-z^3-z^5).
\]
The polynomial \(1-z-z^3-z^5\) has a unique positive zero \(\rho\in(0,1)\), since \(t+t^3+t^5\) strictly increases from \(0\) to \(3\) on \((0,1)\). For any complex zero \(w\), \(1=|w+w^3+w^5|\le|w|+|w|^3+|w|^5\) implies \(|w|\ge\rho\). Equality requires all three summands to have the same positive real argument, so \(w=\rho\). Thus \(\rho\) is the unique zero of minimum modulus, it is simple, and \(1+z\) introduces only a zero at \(-1\). The principal term in the logarithmic derivative is \(z/(\rho-z)\), with coefficient \(\rho^{-n}\). All remaining singularities lie strictly farther from the origin, while the finite polynomial corrections do not affect asymptotics. Hence \(c_n\sim\rho^{-n}\); since \(\rho^{-1}<2\), the fraction among all binary memberships decreases exponentially.

## Verification

The self-contained Python 3 script `verify.py` independently checks the graph-theoretic partition predicate by computing the actual open-neighbourhood signatures of vertices, separately checks the cyclic forbidden-word predicate, and implements two independent formal-series calculations: polynomial matrix traces and the determinant-induced coefficient recurrence. The script enumerated all \(131064\) binary assignments on labelled cycles of lengths \(3\) through \(16\), asserted equivalence of the local and graph-theoretic tests for every length at least five, and reproduced the two exact length-four exceptions. It also matched all coefficients through degree \(30\) from the two algebraic methods. Recorded output is in `verification_output.txt`.

## Relationship to prior work

Chakraborty, Foucaud, Henning and Laihonen (2026) prove that every isolate-free graph admits an ordered partition into a dominating set and a locating-dominating set and give an existence algorithm. Their inspected twelve-page article does not enumerate such partitions, even for cycles. The present claim is an exact enumeration, a local-language characterization, and an asymptotic for all labelled cycles; it is not the general existence result.

Foucaud, Maniya, Paul and Pradhan (2025/2026) study the stronger *two locating-dominating parts* existence question on specified graph classes; they do not give this mixed-partition generating function. Chen, Lu and Miao (2009/2011) study minimum sizes of locating-dominating and identifying codes on paths and cycles, using radius-dependent signatures; those extremal code-size statements do not count complementary mixed partitions. Standard transfer-matrix and binary-word methods are used, not claimed as new tools.

## Limitations

The graph enumeration theorem applies only to labelled simple cycles of length at least three, and counts ordered partitions rather than necklaces or dihedral equivalence classes. No formula for arbitrary graphs or graphs with chords is asserted. Experimental enumeration through length sixteen supports the formal combinatorial argument but does not replace its infinite proof. Publication priority beyond the inspected closely relevant primary literature remains subject to independent bibliographic verification; no independent validation of this result has been performed.

## References

1. D. Chakraborty, F. Foucaud, M. A. Henning, and T. Laihonen, *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*, Electronic Journal of Combinatorics **33**(1), P1.51 (published 2026-03-13). DOI: https://doi.org/10.37236/14049; article/PDF: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p51 .
2. F. Foucaud, P. V. Maniya, K. Paul, and D. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933 (initially public 2025-06-15); https://arxiv.org/abs/2506.12933 .
3. C. Chen, C. Lu, and Z. Miao, *Identifying codes and locating-dominating sets on paths and cycles*, arXiv:0908.2750 (2009); https://arxiv.org/abs/0908.2750 .
