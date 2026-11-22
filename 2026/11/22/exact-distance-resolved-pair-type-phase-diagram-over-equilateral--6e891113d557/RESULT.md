# Exact distance-resolved pair-type phase diagram over equilateral bases in the three-distance Urysohn space

## Finding

Let \(\mathbb U\) be the countable Fraïssé limit of all finite metrics with positive distances in \(\{1,2,3\}\), viewed in the relational language naming each distance. Fix any individually named equilateral finite base \(A=\{a_1,\ldots,a_n\}\), with \(n\ge1\) and \(d(a_i,a_j)=\delta\) for distinct parameters, where \(\delta\in\{1,2,3\}\). Let \(P_{\delta,s}(n)\) count the complete types of ordered pairs \((x,y)\) over \(A\) where \(x,y\notin A\), \(x\ne y\), and \(d(x,y)=s\).

**Theorem (complete distance-resolved ordered-pair spectrum).** For every \(n\ge1\) the following values hold:

\[
\begin{array}{c|ccc}
\delta& s=1&s=2&s=3\\\hline
1&2\cdot4^n+2\cdot3^n-4\cdot2^n+1&4\cdot4^n-4\cdot2^n+1&3\cdot4^n+3^n-4\cdot2^n+1\\
2&7^n&9^n&8^n\\
3&4^n+3n4^{n-1}+n(n-1)4^{n-2}&(2^n+n2^{n-1})^2&4^n+4n4^{n-1}+n(n-1)4^{n-1}
\end{array}
\]

Terms with a zero factor \(n(n-1)\) vanish, including at \(n=1\). The numbers of nonalgebraic one-point types are, respectively,
\[
U_1(n)=2^{n+1}-1,\qquad U_2(n)=3^n,\qquad U_3(n)=2^n+n2^{n-1}.
\]

Under the uniform distribution on complete ordered pair types (not a uniform distribution on points of \(\mathbb U\)), the vector of probabilities for distances \(s=1,2,3\) has the three different limits
\[
\lim_{n\to\infty}\frac{(P_{\delta,1}(n),P_{\delta,2}(n),P_{\delta,3}(n))}{\sum_{s=1}^3P_{\delta,s}(n)}
=\begin{cases}
(2/9,4/9,1/3),&\delta=1,\\
(0,1,0),&\delta=2,\\
(1/9,4/9,4/9),&\delta=3.
\end{cases}
\]
For each fixed \(\delta\), the average number of possible mutual distances between an independently chosen ordered pair of unary types converges to \(9/4\), \(1\), or \(9/4\), respectively. For \(\delta=1\) one additionally has the exact identity \(P_{1,1}(n)+P_{1,2}(n)=2P_{1,3}(n)\).

## Assumptions and scope

Every point outside \(A\) has a positive distance vector \(p=(d(x,a_1),\ldots,d(x,a_n))\in\{1,2,3\}^n\). The admissible unary vectors satisfy the Katětov inequalities
\[
|p_i-p_j|\le\delta\le p_i+p_j\qquad(1\le i<j\le n).
\]
For \(\delta=1\) the admissible set is \(L\cup H\), where \(L=\{1,2\}^n\), \(H=\{2,3\}^n\), and \(L\cap H=\{(2,\ldots,2)\}\). For \(\delta=2\) it is all of \(\{1,2,3\}^n\). For \(\delta=3\) it consists precisely of the vectors with at most one coordinate equal to \(1\). This gives the unary counts above.

For two unary vectors \(p,q\) and proposed positive mutual distance \(s\), the pair-type exists exactly when for every coordinate
\[
|p_i-q_i|\le s\le p_i+q_i.
\]
All of these conditions are both necessary and sufficient: they verify every triangle in the finite diagram on \(A\cup\{x,y\}\); universality realizes the diagram and ultrahomogeneity makes it a unique complete pair type over named \(A\). No quotient by parameter permutations, no algebraic types, and no identification of \((x,y)\) with \((y,x)\) is made.

## Proof

**Local allowed pairs.** For the possible values \(s=1,2,3\), the allowed ordered pairs of coordinate letters are exactly: all nine except \((1,3),(3,1)\) for \(s=1\); all nine for \(s=2\); all nine except \((1,1)\) for \(s=3\). This follows immediately from the pair triangle inequalities, and is independent at distinct named coordinates once the unary vectors are valid.

**Case \(\delta=2\).** There are no restrictions on either unary vector, hence the local allowed-pair counts \(7,9,8\) give \(7^n,9^n,8^n\).

**Case \(\delta=1\).** Write \(Z=L\cap H\) for the single all-2 vector. To count pairs in \((L\cup H)^2\), use the indicator equality \(\mathbf1_{L\cup H}=\mathbf1_L+\mathbf1_H-\mathbf1_Z\) in both coordinates. For \(s=1\), the per-coordinate counts on \(L\times L,H\times H,L\times H,H\times L\) are \(4,4,3,3\); for \(s=2\), they are \(4,4,4,4\); and for \(s=3\), they are \(3,4,4,4\), respectively. Every \(L\times Z,H\times Z,Z\times L,Z\times H\) term has \(2^n\) allowed assignments, and \(Z\times Z\) contributes one. Summing with inclusion-exclusion proves exactly the first row of the table. Direct subtraction gives the stated all-\(n\) linear identity.

**Case \(\delta=3\).** Each unary vector has zero or one occurrence of \(1\). If \(s=2\), every two valid unary vectors are compatible, giving \((2^n+n2^{n-1})^2\). If \(s=1\), partition by the positions of the symbol \(1\) in \(p,q\): neither has one (\(4^n\) possibilities); only one has one (\(2n4^{n-1}\)); both have one at the same position (\(n4^{n-1}\)); or both have one at different positions (\(n(n-1)4^{n-2}\)). These four disjoint cases add to the displayed \(s=1\) formula. If \(s=3\), a shared occurrence of \(1\) is forbidden. With neither vector containing \(1\) there are \(4^n\) possibilities, with exactly one vector containing \(1\) there are \(4n4^{n-1}\), and with each vector containing one at distinct coordinates there are \(n(n-1)4^{n-1}\). Their sum is the displayed \(s=3\) formula.

**Limits and mean multiplicities.** The leading terms across \(s=1,2,3\) are \((2,4,3)4^n\) for \(\delta=1\), \((7^n,9^n,8^n)\) for \(\delta=2\), and \((1,4,4)n^2 4^{n-2}\) for \(\delta=3\). Dividing by their sum gives the three limiting laws. For each \(\delta\), divide \(\sum_sP_{\delta,s}(n)\) by \(U_\delta(n)^2\): using the explicit unary counts gives limits \(9/4,1,9/4\). This proves all assertions.

## Verification

The accompanying standalone `artifacts/verify.py` enumerates every positive distance vector of length \(n=1,\ldots,5\), filters unary vectors using all old-base triangle inequalities, and then directly tests every possible ordered pair at each proposed mutual distance, without using the closed forms in its enumeration. It compares the resulting numbers with the theorem's independent formulas and the unary type counts, and checks the exact linear identity. These finite computations are corroboration; the all-size proof is the preceding partition and inclusion-exclusion argument.

## Relationship to prior work

Norbert Sauer's 2010 work on finite-distance Urysohn spaces explicitly formulates Katětov functions, the pairwise distance inequalities, and the finite extension property. These foundational results guarantee that the finite diagrams counted here are realized but do not state a distance-resolved enumeration for ordered pairs over equilateral bases. The previously published 2026 study *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space* gives an exact unary polynomial and sharp unary extrema on old metrics with distances \(1,2\), including the two unary counts obtained above for \(\delta=1,2\). It does not state the pair spectra or the three conditional limiting mutual-distance laws. The present calculation does not challenge those prior results and uses their basic framework.

## Limitations

The result is only for equilateral named bases, the three-letter distance alphabet, and complete types of ordered pairs of distinct new points. It does not give pair-type counts for arbitrary finite bases or simultaneous realizability of three or more new points. The limiting distributions are on *finite sets of logical types*, not on a hypothetical uniform measure on the countable space. The derivation is elementary finite-alphabet counting, and equivalent enumerations in older metric-extension or constraint-satisfaction literature may exist; no historical uniqueness or independent verification is claimed.

## References

1. N. W. Sauer, *Vertex partitions of metric spaces with finite distance sets*, arXiv:1010.4212, first publicly posted 2010-10-20, especially Section 2 on Katětov functions and the extension property. https://arxiv.org/abs/1010.4212
2. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, public research record, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989/RESULT.md
