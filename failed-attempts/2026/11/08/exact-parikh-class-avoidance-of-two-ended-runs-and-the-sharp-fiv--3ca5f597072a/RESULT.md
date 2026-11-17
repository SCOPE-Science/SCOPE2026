# Exact Parikh-class avoidance of two-ended runs and the sharp five-letter extremum

## Finding
For a finite word \(u\) on \(\{a,b\}\), write \(\lvert u\rvert_a=A\), \(\lvert u\rvert_b=B\), and let \(t=\binom{u}{ab}\) be the number of scattered \(ab\)-subsequences. Let \(L_{A,B,t}\) be the words with those three parameters. For every integer \(r\ge1\), let \(F_{A,B,r}(q)\) be the polynomial whose coefficient of \(q^t\) counts words in \(L_{A,B,t}\) *avoiding* the scattered pattern \(a b^r a\). For every \(A\ge2\) and \(B\ge0\),

\[
F_{A,B,r}(q)=\sum_{p=0}^{\min\{B,r-1\}}q^p\begin{bmatrix}A+p-2\\p\end{bmatrix}_{q}\sum_{v=0}^{B-p}q^{Av}.
\]

Here the Gaussian polynomial is normalized by \(\begin{bmatrix}n\\k\end{bmatrix}_q=\prod_{i=1}^{k}(1-q^{n-k+i})/(1-q^i)\) (as an integer polynomial), with the empty product \(1\). For \(A=0\) or \(A=1\), every class has one word and the avoidance polynomial is the full Gaussian polynomial \(\begin{bmatrix}A+B\\A\end{bmatrix}_{q}\).

For the first nontrivial case \(r=3\), i.e. the five-letter pattern \(abbba\), define

\[
h_A(s)=\begin{cases}\lfloor\min\{s,2A-s\}/2\rfloor,&2\le s\le2A-2,\\0,&\text{otherwise}.\end{cases}
\]

For all integers \(A\ge2\), \(B\ge0\), and \(0\le t\le AB\), its exact avoiding count is

\[
M_{A,B}(t)=1+\sum_{\substack{2\le s\le2A-2\\ s\equiv t\ (\mathrm{mod}\ A)\\0\le(t-s)/A\le B-2}}h_A(s).
\]

The sum has at most two nonzero terms, so the numerator is evaluated using a constant number of integer arithmetic operations. Moreover, for every \(A\ge2\), \(B\ge2\),

\[
\boxed{\max_{0\le t\le AB}M_{A,B}(t)=1+\lfloor A/2\rfloor,\qquad M_{A,B}(A)=1+\lfloor A/2\rfloor.}
\]

For \(A<2\) or \(B<2\), the corresponding maximum is \(1\). If \(U\) is uniform in a nonempty class \(L_{A,B,t}\), its exact containment probability for \(abbba\) is

\[
\Pr(abbba\preceq U)=1-\frac{M_{A,B}(t)}{[q^t]\begin{bmatrix}A+B\\A\end{bmatrix}_q}.
\]

This counts *words*, not embeddings of a pattern in a single word; a word containing the pattern multiple times contributes once to containment.

## Assumptions and scope
All parameters are nonnegative integers except \(r\ge1\). When \(A\ge2\), \(0\le t\le AB\); outside that interval \(L_{A,B,t}\) is empty and probabilities are not defined. Scattered subsequence containment means the existence of increasing indices matching all letters of the pattern, with no adjacency requirement. The formal variable \(q\) is unrelated to the alphabet size (which is two). The finding is for finite linear words, not cyclic words. It makes no statement about other length-five patterns.

## Proof
**Gap decomposition.** Every word with exactly \(A\ge2\) letters \(a\) has a unique expression

\[
u=b^{x_0}ab^{x_1}a\cdots ab^{x_{A-1}}ab^{x_A},\qquad x_i\in\mathbb Z_{\ge0},\quad\sum_{i=0}^{A}x_i=B.
\]

A letter \(b\) in the \(i\)-th gap has exactly \(i\) letters \(a\) preceding it, so \(t=\sum_{i=1}^{A}i x_i\). The pattern \(a b^r a\) occurs as a scattered subsequence precisely when there are at least \(r\) letters \(b\) strictly between the first and last occurrences of \(a\), namely when \(p:=x_1+\cdots+x_{A-1}\ge r\). Thus avoidance means \(0\le p\le\min\{B,r-1\}\).

For a fixed \(p\), the nonnegative interior gap lengths correspond to a nondecreasing sequence of \(p\) indices in \(\{1,\ldots,A-1\}\). The standard bounded-partition identity gives

\[
\sum_{\substack{x_1+\cdots+x_{A-1}=p\\x_i\ge0}}q^{\sum_{i=1}^{A-1}i x_i}=q^p\begin{bmatrix}A+p-2\\p\end{bmatrix}_q.
\]

The final gap is free to have \(v=x_A\) letters \(b\), where \(0\le v\le B-p\); the initial gap is then forced to have \(x_0=B-p-v\). Their contribution is \(q^{Av}\), proving the displayed formula for \(F_{A,B,r}\). For \(A\le1\), the pattern cannot occur and there is one word for each feasible \(t\), as claimed.

**The exact five-letter count.** With \(r=3\), allowed interior counts are \(p=0,1,2\). The contributions \(p=0\) and \(p=1\) together are precisely \(1+q+\cdots+q^{AB}\): for each \(t\), division \(t=Av+j\), \(0\le j<A\), gives exactly one term (a middle \(b\) if and only if \(j>0\)). For \(p=2\), an unordered interior index pair \(1\le i\le j\le A-1\) contributes \(s=i+j\), and the final gap contributes \(Av\) with \(0\le v\le B-2\). There are exactly \(h_A(s)=\lfloor\min\{s,2A-s\}/2\rfloor\) such pairs with a given integer sum \(s\), by counting \(i\) between \(\max\{1,s-(A-1)\}\) and \(\lfloor s/2\rfloor\). This gives the finite formula for \(M_{A,B}(t)\). Since \(2\le s\le2A-2\), fixing \(s\equiv t\pmod A\) leaves at most two possibilities.

**Sharp maximum.** Ignoring the allowable final-gap range can only increase the \(p=2\) count. Thus \(M_{A,B}(t)-1\) is at most the number of unordered pairs \(1\le i\le j\le A-1\) whose sum equals \(t\) modulo \(A\). To count these, start from ordered nonzero residues \(i,j\in\mathbb Z/A\mathbb Z\) satisfying \(i+j\equiv t\), and divide after correcting the fixed points \(i=j\). For odd \(A\), every residue \(t\) has exactly \((A-1)/2\) unordered pairs. For even \(A\), an even residue has exactly \(A/2\) pairs, and an odd residue has \(A/2-1\) pairs. Therefore \(M_{A,B}(t)\le1+\lfloor A/2\rfloor\). When \(B\ge2\) and \(t=A\), all \(\lfloor A/2\rfloor\) pairs with integer sum \(s=A\) occur with final gap \(v=0\), and the initial gap absorbs the other \(B-2\) letters. Hence equality holds. When \(A\le1\) or \(B\le1\), the pattern is impossible and every nonempty class has exactly one word. Finally the Gaussian coefficient counts every class by the same gap/partition correspondence, giving the probability formula.

## Verification
The standalone accompanying script `verify_twoended.py` constructs all words for \(A,B\le8\) with \(A+B\le14\). It independently tests scattered containment, independently computes the Parikh count, and compares exhaustive class-wise avoidance counts with the polynomial formula for multiple run lengths. It checks 333 parameter triples for the full polynomial and the exact five-letter formula for all eligible composition pairs. It separately tests the maximum and its equality case for every \(2\le A<160\) and \(B\in\{0,1,2,3,6,12,100\}\). The script prints `TWO_ENDED_PARIKH_VERIFY_OK 333` on success. These finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
Fazekas, Huang, and Mercaş (2026) formulate containment probabilities for arbitrary fixed subsequences in binary Parikh-matrix classes and prove an additive approximation scheme (Section 5), alongside general polynomial upper bounds for avoidance. Their full text supplies the underlying gap and Gaussian-partition model, but not the displayed exact avoidance polynomial or the sharp five-letter maximum. Their factoring-hardness example concerns the different alternating pattern \(abab\); the arithmetic behavior of \(abbba\) is distinguishable. Atanasiu (2007) studies binary amiable equivalence classes and the general linear gap system, without this pattern-filtered count. The classical unique maximal representative of each Parikh class is a special \(abba\)-avoider; accordingly, no novelty is claimed for that simpler representative or for the Gaussian coefficient itself. The present quantitative claim starts with the entire \(a b^r a\) family and the nontrivial \(r=3\) sharp bound.

## Limitations
The bound is for the exact five-letter scattered pattern \(abbba\) and the stated binary fixed-composition/Parikh classes. The general polynomial provides exact counts but does not imply a binary-bitlength polynomial-time algorithm to compute the entire Gaussian denominator. The elementary counting may have an implicit equivalent in unindexed restricted-partition literature; publication priority requires independent confirmation. No independent validation or formal proof certification has been performed.

## References
1. S. Z. Fazekas, X. Huang, R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, EPTCS 451 (2026), 140–154. DOI: https://doi.org/10.4204/EPTCS.451.10; manuscript https://arxiv.org/abs/2610.06717.
2. A. Atanasiu, *Binary Amiable Words*, International Journal of Foundations of Computer Science 18 (2007), 387–400. Accessible article text: https://paperzz.com/doc/8039966/january-26--2007-8-31-wspc-instruction-file-amiabile.
3. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, Theoretical Computer Science 1066 (2026), 115732, https://doi.org/10.1016/j.tcs.2025.115732 (bibliographic/abstract evidence; full text not inspected).
