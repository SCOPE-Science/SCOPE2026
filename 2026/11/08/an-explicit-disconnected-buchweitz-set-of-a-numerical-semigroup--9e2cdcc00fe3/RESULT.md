# An explicit disconnected Buchweitz set of a numerical-semigroup gapset

## Finding

There is a numerical semigroup whose Buchweitz set is not an interval of integers. More precisely, let
\[
G=\{1,2,\ldots,59\}\cup\{74,112,113,119\},
\qquad S=\mathbb Z_{\ge0}\setminus G.
\]
Then \(G\) is the gapset of \(S\), its genus is \(63\), and its Buchweitz set is **exactly**
\[
\boxed{\mathcal B(G)=\{3,6,7\}.}
\]
Writing \(nG=\{g_1+\cdots+g_n:g_i\in G\}\) and
\[
\beta_G(n)=|nG|-(2n-1)(|G|-1),
\]
we have the exact all-index formula
\[
\boxed{\beta_G(2)=0,\quad\beta_G(3)=1,\quad
\beta_G(4)=\beta_G(5)=0,\quad
\beta_G(6)=\beta_G(7)=1,\quad
\beta_G(n)=48-6n\ (n\ge8).}
\]
Consequently the Buchweitz set of a numerical-semigroup gapset need not be an interval, and the associated Buchweitz function need not be unimodal. These give negative answers to Questions 4.1 and 4.2 of Eliahou, García-García, Marín-Aragón and Vigneron-Tenorio (2020) for the **gapset** case, not merely for arbitrary finite subsets of integers.

## Assumptions and scope

Every interval \([a,b]\) denotes all integers between its endpoints, inclusive. The numerical semigroup \(S\subseteq\mathbb Z_{\ge0}\) contains zero and every integer at least \(120\). Its positive elements are at least \(60\); hence the sum of any two positive elements is at least \(120\), and \(S\) is closed under addition. Its complement is the displayed finite set \(G\), so \(G\) is a genuine gapset. There are \(59+4=63\) gaps, and \(119\) is the largest gap.

Define the shifted set
\[
H=G-1=[0,58]\cup\{73,111,112,118\}.
\]
For every integer \(n\ge1\), \(nG=n+nH\) and therefore \(|nG|=|nH|\). The proof below establishes all cardinalities, including every \(n\ge8\); it is not an extrapolation from finite data.

## Proof

**Step 1: exact finite sumsets.** Represent a finite sumset by its maximal disjoint integer intervals. If \(I,J\) are such interval lists, their Minkowski sum is obtained by forming \([a+c,b+d]\) for each \([a,b]\in I\) and \([c,d]\in J\), and merging overlapping or adjacent intervals. Starting with
\[
I_1=\{[0,58],[73,73],[111,112],[118,118]\},
\]
this rule computes \(I_{n+1}\) from \(I_n\) exactly. The full resulting lists for \(n=2,\ldots,8\), in machine-checkable form, are included in `interval_certificate.tsv`. The exact cardinalities are:

| \(n\) | \(|nG|\) | \(\beta_G(n)\) |
|---:|---:|---:|
|2|186|0|
|3|311|1|
|4|434|0|
|5|558|0|
|6|683|1|
|7|807|1|
|8|930|0|

In particular, the complete interval list for \(8H\) is
\[
[0,914]\cup[916,920]\cup[923,926]\cup
[930,932]\cup[937,938]\cup\{944\}.
\]
Let
\[
E=\{1,2,3,4,5,8,9,10,11,15,16,17,22,23,29\}.
\]
The displayed base-eight list is exactly
\[
8H=[0,944]\setminus\{944-d:d\in E\}.\tag{1}
\]
This can be checked directly from the interval merging rule, with no probabilistic or tolerance-dependent step.

**Step 2: the exact high-index complement.** Let \(T=\langle6,7\rangle\), the additive semigroup of nonnegative sums of \(6\) and \(7\). Its gaps are exactly \(E\). Indeed, direct inspection of the thirty integers \(0,\ldots,29\) gives precisely this list, and \(30,31,32,33,34,35\in T\), whence all integers at least \(30\) belong to \(T\) by repeatedly adding \(6\).

Every possible *deficit* of a summand from the maximum \(118\) is in \(T\):
\[
118-H=[60,118]\cup\{45,7,6,0\}\subseteq T;
\]
for instance \(45=4\cdot6+3\cdot7\). Thus, whenever \(x\in nH\), its deficit \(118n-x\in T\). It follows that
\[
\{118n-d:d\in E\}\cap nH=\varnothing\qquad(n\ge1).\tag{2}
\]
We prove by induction, starting with (1), that for **every** \(n\ge8\),
\[
\boxed{nH=[0,118n]\setminus\{118n-d:d\in E\}.}\tag{3}
\]
Assume (3) at some \(n\ge8\). As every element of \(E\) is below \(30\), the entire interval \([0,118n-30]\) is contained in \(nH\). Adding \([0,58]\subset H\) covers \([0,118n+28]\); adding \(118\in H\) to that same interval covers \([118,118n+88]\). These two integer intervals overlap, so their union covers
\[
[0,118n+88]=[0,118(n+1)-30].\tag{4}
\]
It remains to determine the final thirty points \(118(n+1)-d\) with \(0\le d\le29\). By (2), such a point is absent if \(d\in E\). If \(d\notin E\), then \(d\in T\), so \(d=6u+7v\) for nonnegative integers \(u,v\). Since \(d\le29\), necessarily \(u+v\le4\le n+1\). Taking \(u\) copies of \(112\in H\), \(v\) copies of \(111\in H\), and \(n+1-u-v\) copies of \(118\in H\), gives the sum \(118(n+1)-d\). Together with (4) this proves (3) for \(n+1\).

**Step 3: Buchweitz function.** The set in (3) is an integer interval of length \(118n+1\) with exactly \(|E|=15\) deleted points. Therefore
\[
|nG|=|nH|=118n-14\qquad(n\ge8).
\]
Since \(|G|-1=62\), this gives
\[
\beta_G(n)=118n-14-(2n-1)62=48-6n\qquad(n\ge8).
\]
The finite table from Step 1 supplies the remaining indices \(2\le n\le7\). The positive values occur precisely at \(n=3,6,7\). In particular \(3,6\in\mathcal B(G)\) while \(4,5\notin\mathcal B(G)\); thus \(\mathcal B(G)\) is not an integer interval. The values \(1,0,0,1\) at \(n=3,4,5,6\) also contradict unimodality. \(\square\)

## Verification

`verify_sumsets.py` implements the exact integer-interval Minkowski recursion, checks the complete lists for \(n=2,\ldots,8\), confirms identity (1), and verifies the enumeration of the fifteen gaps of \(\langle6,7\rangle\). Its expected output is `sumset_output.txt`. `verify_direct.py` independently constructs the sets \(nG\) using direct integer membership for \(2\le n\le14\), verifies semigroup closure on the only potentially nontrivial finite range, and compares all computed Buchweitz values with the theorem. Its output is `direct_output.txt`. Both checkers use Python's standard library and exact integer operations. Their finite runs check the base data; Step 2 is the separate general argument justifying all infinitely many indices.

To replay in a directory containing the embedded files, run `python3 verify_sumsets.py` and `python3 verify_direct.py`. The programs have no external dependencies.

## Relationship to prior work

The original definition, finiteness theorem, interval constructions and the explicit interval/unimodality questions appear in Eliahou, García-García, Marín-Aragón and Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup*, arXiv:2011.09187 (first submitted 18 November 2020), especially Section 4, Questions 4.1 and 4.2. Marín-Aragón's July 2024 lecture, *Studying the Buchweitz Set of Numerical Semigroups*, slide 18, continues to pose the gapset interval question. Their positive interval constructions, e.g. \(\mathcal B(G)=[3,k+3]\), do not imply the existence or nonexistence of the disconnected set exhibited here. The proof is self-contained; use of the \(\langle6,7\rangle\) coin semigroup is an elementary internal device rather than an asserted prior theorem.

## Limitations

The example answers the interval and unimodality questions negatively by one explicit gapset, but does **not** classify all possible Buchweitz sets or answer the general realizability problem (Question 4.3) for arbitrary prescribed finite sets. It does not establish that \(\{3,6,7\}\) is a smallest or minimal example. Although no equivalent earlier construction was identified in the inspected primary literature and searches, unindexed subsequent work could contain one. Independent external mathematical audit has not yet been performed.

## References

1. S. Eliahou, J. I. García-García, D. Marín-Aragón, A. Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup*, arXiv:2011.09187 (submitted 18 November 2020), https://arxiv.org/abs/2011.09187; *Bulletin of the Brazilian Mathematical Society*, DOI 10.1007/s00574-022-00322-8.
2. D. Marín-Aragón, *Studying the Buchweitz Set of Numerical Semigroups*, Jerez, July 2024, slide 18, https://imns2024.uca.es/wp-content/uploads/2024/07/Marin_Aragon_Jerez_24.pdf.
3. J. I. García-García, D. Marín-Aragón, F. Torres, A. Vigneron-Tenorio, *On reducible non-Weierstrass semigroups*, *Open Mathematics* (2021), DOI 10.1515/math-2021-0111.
