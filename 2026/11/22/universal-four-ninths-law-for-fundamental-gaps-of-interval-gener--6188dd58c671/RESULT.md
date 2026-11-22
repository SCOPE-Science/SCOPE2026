# Universal four-ninths law for fundamental gaps of interval-generated numerical semigroups

## Finding
For every pair of integers \(a\ge2\) and \(1\le k<a\), let
\[
S_{a,k}=\langle a,a+1,\ldots,a+k\rangle,
\qquad
\operatorname{FG}(S_{a,k})=\{n\notin S_{a,k}:2n,3n\in S_{a,k}\}.
\]
Set \(A=\lceil a/2\rceil\) and \(B=\lceil 2a/3\rceil\). The **complete set** of fundamental gaps consists of the integers \(n=qa+r\) in the following two disjoint bands, and no others:
\[
\begin{array}{ll}
 A\le r<B,&
 \displaystyle\max\!\left(0,\left\lceil\frac{3r-a-k}{3k}\right\rceil\right)
 \le q\le\left\lceil\frac r k\right\rceil-1,\\[5pt]
 B\le r<a,&
 \displaystyle\max\!\left(0,\left\lceil\frac{2r-a-k}{2k}\right\rceil\right)
 \le q\le\left\lceil\frac r k\right\rceil-1.
\end{array}
\]
Each band contains only integer \(q\ge0\); an empty index interval contributes no elements.

Writing \(F(a,k)=|\operatorname{FG}(S_{a,k})|\), the band description is an **exact finite formula**:
\[
\begin{split}
F(a,k)={}&\sum_{r=A}^{B-1}
\max\left(0,\left\lceil\frac r k\right\rceil-
\max\left(0,\left\lceil\frac{3r-a-k}{3k}\right\rceil\right)\right)\\
&+\sum_{r=B}^{a-1}
\max\left(0,\left\lceil\frac r k\right\rceil-
\max\left(0,\left\lceil\frac{2r-a-k}{2k}\right\rceil\right)\right).
\end{split}
\]
The genus (total number of gaps) satisfies \(g(a,k)=\sum_{r=1}^{a-1}\lceil r/k\rceil\), and, **uniformly in all permitted \(a,k\)**,
\[
\left|F(a,k)-\frac{2a^2}{9k}\right|<3a,
\qquad
\left|g(a,k)-\frac{a^2}{2k}\right|<a.
\]
Consequently, for *every* sequence of parameters with \(a\to\infty\) and \(k=o(a)\),
\[
\boxed{\displaystyle\frac{F(a,k)}{g(a,k)}\longrightarrow\frac49.}
\]
The limiting constant is independent of the growth rate of the interval width, provided that width is sublinear in \(a\).

## Assumptions and scope
The generators are **all** consecutive integers from \(a\) to \(a+k\), inclusive. The integers satisfy \(a\ge2\), \(1\le k<a\); no coprimality assumption beyond consecutive generation is needed. All gaps and fundamental gaps are nonnegative integers. The exact two-band description, genus and absolute estimates apply for every parameter pair; the ratio limit requires \(k=o(a)\). The result does not claim the same limit when \(k/a\) stays bounded away from zero.

## Proof
**1. Membership lemma.** Write any nonnegative integer uniquely as \(n=qa+r\) with \(q\ge0\) and \(0\le r<a\). Then
\[
n\in S_{a,k}\quad\Longleftrightarrow\quad r\le qk.
\]
Indeed, if \(n\) is a sum of \(m\) generators, then \(m\le q\) and \(n\le m(a+k)\le q(a+k)\), whence \(r\le qk\). Conversely, when \(r\le qk\), distribute an excess of \(r\) over \(q\) summands, each between \(a\) and \(a+k\), to represent \(n\). In particular, the gaps are exactly \(n=qa+r\) with \(1\le r<a\) and \(0\le q<\lceil r/k\rceil\). Summing their numbers by residue gives the genus formula.

**2. Double and triple tests.** For a gap \(n=qa+r\), put \(c_j=\lfloor jr/a\rfloor\) for \(j=2,3\). The membership lemma at \(jn=(jq+c_j)a+(jr-ac_j)\) says
\[
jn\in S_{a,k}\quad\Longleftrightarrow\quad
q\ge \left\lceil\frac{jr-(a+k)c_j}{jk}\right\rceil.
\]
If \(2r<a\), the double test reduces to \(r\le qk\), contradicting that \(n\) is a gap. Hence \(r\ge A\). If \(A\le r<B\), then \(c_2=c_3=1\) and the triple-test lower bound dominates the double-test lower bound (it subtracts the smaller quantity \((a+k)/(3k)\) from \(r/k\)). If \(B\le r<a\), then \(c_2=1,c_3=2\), and the double-test lower bound dominates. Combining the controlling bound with \(q\ge0\) and \(q<\lceil r/k\rceil\) proves both bands, including their endpoints. Counting integers \(q\) gives the exact finite formula.

**3. Uniform error.** Every ceiling differs from its argument by a quantity in \([0,1)\), giving \(|g(a,k)-a^2/(2k)|<a\). For \(a\ge3k\), both controlling lower bounds in the bands are nonnegative, and each number of admissible \(q\)'s differs by less than one from \((a+k)/(3k)\) on the first band and from \((a+k)/(2k)\) on the second. Because \(B-A=a/6+\epsilon_1\) and \(a-B=a/3+\epsilon_2\) with \(|\epsilon_1|,|\epsilon_2|<1\), it follows that
\[
\left|F(a,k)-\frac{2a^2}{9k}\right|
< a+\frac a2+\frac a{3k}+\frac a{2k}<3a.
\]
For \(a<3k\), use \(0\le F(a,k)\le g(a,k)<a^2/(2k)+a<5a/2\), while \(0\le2a^2/(9k)<2a/3\), to get the same bound. Dividing the two asymptotic formulas shows the ratio tends to \(4/9\) whenever \(k/a\to0\).

## Verification
A standalone Python 3 checker, `check_fundamental_gap_bands.py`, computes membership by an *independent unbounded-coin dynamic program* instead of the membership lemma. It exhaustively compares both predicted bands against the direct fundamental-gap predicate for all \(2\le a<110\) and \(1\le k<a\). It also verifies the exact count and both stated uniform inequalities. The successful run covered **5,886 parameter pairs, 2,793,328 gap candidates and 566,195 fundamental gaps**. The checker prints sample ratios at \(a=720\). The mathematical proof establishes every parameter pair without relying on finite tests.

## Relationship to prior work
The classical gap and Apéry-set approach to consecutive-generator numerical semigroups underlies the setting; Komatsu and Ying's 2022 work develops generalized Frobenius and genus formulas for triples in arithmetic progression, but not fundamental-gap bands. Rosales and coauthors (2004) introduced fundamental gaps and gave general bounds and methods for arbitrary semigroups. Moreno-Frías and Rosales (published December 2024) develop fixed-fundamental-gap classes and algorithms. Those results give foundational definitions and generic procedures rather than the two-band classification or the width-independent \(4/9\) limit asserted here. Closely related published interval-semigroup classifications concern other statistics, such as residue counts, isolated gaps or pseudo-Frobenius gaps; those are different predicates.

## Limitations
The bound \(3a\) is a safe, non-sharp absolute error estimate. It does not describe the ratio for \(k\) proportional to \(a\), nor does the result determine every lower-order periodic fluctuation of \(F(a,k)\). Priority cannot be ruled out for an unindexed earlier specialization of general numerical-semigroup algorithms. No independent external mathematical audit has been performed.

## References
1. T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052v1 (first public 2022-06-27), primary MSC 11D07. https://arxiv.org/abs/2206.13052
2. J. C. Rosales, P. A. García-Sánchez, J. I. García-García and J. A. Jiménez Madrid, *Fundamental gaps in numerical semigroups*, Journal of Pure and Applied Algebra 189 (2004), 301–313. https://doi.org/10.1016/j.jpaa.2003.10.024
3. M. Á. Moreno-Frías and J. C. Rosales, *Numerical Semigroups with a Fixed Fundamental Gap*, Mathematics 13 (2025), 95 (online 2024-12-29). https://doi.org/10.3390/math13010095
