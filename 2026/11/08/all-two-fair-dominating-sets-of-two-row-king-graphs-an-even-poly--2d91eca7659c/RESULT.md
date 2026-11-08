# All two-fair dominating sets of two-row king graphs: an even polynomial and a three-residue optimum census

## Finding
Let \(R_{2,n}=P_2\boxtimes P_n\) be the two-row rectangular king graph, \(n\ge1\), with vertices \((r,j)\), \(r\in\{1,2\}\) and \(1\le j\le n\). Two distinct vertices are adjacent when the differences in both coordinates are at most one. A set \(D\) is *two-fair dominating* if every vertex outside \(D\) has exactly two neighbors in \(D\). Include \(D=V\), for which this condition holds vacuously. Define \(F_n(z)=\sum_D z^{|D|}\) over all two-fair dominating sets.

**Theorem.** For every \(n\ge1\), every exponent of \(F_n(z)\) is even, and
\[
F_n(z)=\sum_{k=1}^{n}z^{2k}\sum_{a=0}^{k-1}\binom{k-1}{a}\sum_{b,c\in\{0,1\}}\mathbf1\{n=3k-2-2a+b+c\}
+\mathbf1\{n\equiv2\pmod3\}\,4^{(n+1)/3}z^{2(n+1)/3}.
\]
In particular, the minimum size is \(2\lceil n/3\rceil\), and the number \(N_n\) of minimum two-fair dominating sets is
\[
N_{3m}=1\quad(m\ge1),\qquad N_{3m+1}=m+1\quad(m\ge0),\qquad N_{3m+2}=4^{m+1}+2\quad(m\ge0).
\]
The formula counts *labelled vertex subsets*, not row-symmetry classes.

## Assumptions and scope
The graph is the *strong product* of two paths, with both diagonals joining adjacent columns; it is not the ordinary Cartesian ladder. The graph may have \(n=1\) (a single edge). For a subset \(D\), encode column \(j\) by \(s_j\in\{0,1,2\}\), the number of its selected vertices. A column labelled \(1\) has two possible choices of selected row; columns labelled \(0\) or \(2\) have one. Set \(s_0=s_{n+1}=0\). An omitted vertex in column \(j\) sees every selected vertex of columns \(j-1,j,j+1\), hence the two-fair condition is exactly
\[
s_j<2\ \Longrightarrow\ s_{j-1}+s_j+s_{j+1}=2 \quad(1\le j\le n).
\]
No constraint is imposed at columns with \(s_j=2\), since these have no omitted vertex. The theorem covers all feasible sets and all sizes, not only minima.

## Proof
**1. Dichotomy of column words.** If \(s_j=1\), the displayed condition requires \(s_{j-1}+s_{j+1}=1\); thus a \(1\) must have exactly one neighboring \(1\) and the other neighboring symbol is \(0\). If \(s_j=0\), its two adjacent symbols must sum to \(2\). Starting at the left boundary, if \(s_1=1\), then \(s_2=1\) and the local conditions force the entire word to be \(11(011)^m\), ending validly only when \(n=3m+2\). Conversely, this word satisfies every local condition for all \(m\ge0\). If \(s_1=0\), then \(s_2=2\); if \(s_1=2\), its next symbol cannot be \(1\). Once a symbol \(2\) occurs, any following zero-run must have length zero or exactly two before the next \(2\), since a \(0\) must have a single adjacent \(2\) (rather than zero or two) in a word lacking \(1\)'s. The same local constraints exclude any subsequent \(1\). Thus every remaining feasible word uses only \(0\)'s and \(2\)'s. The argument includes the one-column boundary case directly.

**2. All zero/two words.** A feasible zero/two word has \(k\ge1\) occurrences of \(2\). Its \(k-1\) internal gaps contain either zero or two zero-symbols; its initial and final zero-runs have length \(b,c\in\{0,1\}\). If \(a\) of the internal gaps are empty, the total length is
\[
n=k+2(k-1-a)+b+c=3k-2-2a+b+c.
\]
Conversely, every such arrangement is feasible: each zero has exactly one adjacent full column and each full column has no omitted vertex. Choosing the \(a\) empty gaps among \(k-1\) locations gives \(\binom{k-1}{a}\) distinct vertex subsets, each of size \(2k\).

**3. The one-only word.** When \(n=3m+2\), the forced word \(11(011)^m\) has \(2m+2\) one-columns. Each has two independent choices of row, giving exactly \(2^{2m+2}=4^{m+1}\) vertex subsets, all of size \(2m+2\). No such word exists for other lengths. Summing the two disjoint cases proves the complete polynomial and even support.

**4. Minimum layer and sharp residue counts.** A zero/two word with \(k\) full columns has length at most \(3k\). Therefore its size \(2k\) is at least \(2\lceil n/3\rceil\). The one-only word, when feasible, also has exactly that size. Equality is attained by suitable zero/two words at every length, establishing the minimum without using a previous theorem. Write \(k=\lceil n/3\rceil\), and \(\delta=3k-n\in\{0,1,2\}\). Equality in the length equation requires \(\delta=2+2a-b-c\). If \(\delta=0\), only \((a,b,c)=(0,1,1)\) works, giving one optimum. If \(\delta=1\), only \(a=0,b+c=1\) works, giving two zero/two optima, plus the \(4^k\) one-only choices. If \(\delta=2\), either \(a=0,b=c=0\) (one word) or \(a=1,b=c=1\) (\(k-1\) words) works, giving \(k\) optima. Substituting the three residues proves the stated count.

## Verification
The supplied `artifacts/verify.py` uses independent direct enumeration of all subsets of the \(2n\) labelled vertices for \(1\le n\le9\), without using the column-word condition to decide validity. It compares every coefficient with the explicit formula. It additionally exhausts all ternary column words through \(n=12\) and checks minimum-layer and parity identities through \(n=200\). Run `python3 artifacts/verify.py` from the package root. Its successful terminal line is `VERIFY_OK`. These finite computations corroborate the proof; the unrestricted quantifiers follow from the local-word dichotomy and exact gap count, not numerical extrapolation.

## Relationship to prior work
Two-fair domination requires exactly two selected neighbors at every omitted vertex, rather than merely domination or total domination. The known cardinality \(\gamma_{2\mathrm{fd}}(R_{2,n})=2\lceil n/3\rceil\) appears in the 2025 work of Hung and in Hung's 2026 treatment. Their relevant results give the minimum size and selected constructions, not the complete polynomial, parity classification, or exact multiplicity at each residue. The present theorem is a strictly finer enumeration: knowing the least degree of a generating polynomial does not determine the other coefficients or the number of minimizers. Ordinary domination-polynomial and king-graph optimum tables count different families, because two-fairness imposes an exact number of neighbors. Historical priority remains subject to unindexed literature.

## Limitations
Only two-row rectangular king graphs are classified here. No assertion is made for three or more rows, for Cartesian ladders, or for other fairness parameters. The result is proved internally and computationally corroborated, but has not undergone independent mathematical validation. The historic first appearance of a coincident enumerator in unindexed sources cannot be ruled out.

## References
1. R.-W. Hung, *The 2-Fair Domination in Extended Supergrid and Planar Graphs*, conference paper, IIHMSP 2025 (conference October 15–17, 2025), Section 3, Lemma 2 and Theorem 7. Publicly accessible document: https://iihmsp25.csie.cyut.edu.tw/Download/23-SimilarityReport.pdf .
2. R.-W. Hung, *Fair Domination on Extended Supergrid Graphs: Complexity, Linear-Time Algorithms, and ILP Formulations*, *Mathematics* 14 (2026), 947, Section 4, Lemma 14. https://doi.org/10.3390/math14060947 .
3. S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, arXiv:2408.08053 (2024); ordinary minimum dominating-set table https://oeis.org/A350815 .
