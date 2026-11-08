# A sharp eventual completeness threshold for nonadjacent centered nonagonal sums

## Finding
For every integer \(j\ge1\), let
\[
c_j=1+\frac{9j(j-1)}2
\]
be the \(j\)-th centered nonagonal number. A **legal** index set is a finite set \(J\subset\mathbb Z_{\ge1}\) in which no two distinct indices are consecutive. Let \(\mathcal R\) consist of all sums \(\sum_{j\in J}c_j\) over legal index sets, including the empty sum \(0\). Then
\[
\boxed{\max(\mathbb Z_{\ge0}\setminus\mathcal R)=9083.}
\]
Equivalently, \(9083\notin\mathcal R\), whereas every integer \(t\ge9084\) belongs to \(\mathcal R\).

This is a sparse-representation analogue of centered-polygonal additive universality: the summands must be distinct and, more restrictively, cannot have adjacent indices. It is a different invariant from unrestricted distinct-summand coverage.

## Assumptions and scope
All indices start at \(1\); in particular \(c_1=1\), \(c_2=10\), \(c_3=28\). There is no bound on the number of summands, but each index can be used at most once and two selected indices cannot differ by \(1\). All sums are finite and nonnegative. The result concerns centered nonagonal numbers only, not every centered polygonal family.

For \(n\ge0\), put
\[
B_n=\left\{\sum_{j\in J}c_j:J\subseteq\{1,\ldots,n\},\ \lvert i-j\rvert\ge2\text{ for distinct }i,j\in J\right\},
\]
and \(B_{-1}=B_0=\{0\}\). Thus \(\mathcal R=\bigcup_{n\ge0}B_n\).

## Proof
**Exact finite-state decomposition.** The largest index \(n\) in a legal set is either omitted or selected. If it is selected, \(n-1\) is omitted. Therefore, for every \(n\ge1\),
\[
B_n=B_{n-1}\cup(c_n+B_{n-2}). \tag{1}
\]
This identity is exact in both directions, not an inclusion.

**Finite base and obstruction.** Let \(L=9084\) and \(U_n=\lfloor n^3/4\rfloor\). Recurrence (1), evaluated exactly by integer bitsets with bit position \(t\) indicating membership, establishes the following finite statements:
\[
[L,U_{41}]=[9084,17230]\subseteq B_{41},
\qquad
[L,U_{42}]=[9084,18522]\subseteq B_{42}, \tag{2}
\]
and \(9083\notin B_{45}\). Two independently implemented dynamic programs compare all their membership bits through the relevant cutoffs; the standalone checker is supplied. Since \(c_{45}=8911\le9083<c_{46}=9316\) and \(c_j\) is increasing, no index greater than \(45\) can occur in a representation of \(9083\). Thus
\[
9083\notin\mathcal R. \tag{3}
\]

**Inductively expanding interval.** We prove \([L,U_n]\subseteq B_n\) for every \(n\ge41\). The two bases are (2). For any \(n\ge43\), the floor bounds yield
\[
U_n-U_{n-2}<\frac{n^3-(n-2)^3}{4}+1
=\frac32n^2-3n+3\le c_n. \tag{4}
\]
The last inequality follows immediately from \(c_n=\frac92n(n-1)+1\) and \(n\ge43\). Further,
\[
U_{n-1}+1\ge L+c_n \quad(n\ge43). \tag{5}
\]
Indeed at \(n=43\), its left side is \(18523\) and the right side is \(17212\). For all \(n\ge43\),
\[
U_n-U_{n-1}>\frac{3n^2-3n+1}{4}-1>9n=c_{n+1}-c_n,
\]
so the margin in (5) strictly increases with \(n\).

Assume that \([L,U_{n-2}]\subseteq B_{n-2}\) and \([L,U_{n-1}]\subseteq B_{n-1}\). Equation (1) gives
\[
[L,U_{n-1}]\cup[L+c_n,U_{n-2}+c_n]\subseteq B_n.
\]
By (5), the two integer intervals overlap or touch; by (4), their union reaches at least \(U_n\). Since \(U_n\ge U_{n-1}\), the entire interval \([L,U_n]\) lies in \(B_n\). The induction is complete.

Finally, \(U_n\) grows without bound. Every \(t\ge L\) lies in \([L,U_n]\) for some \(n\), and so is representable. Together with (3), this proves the asserted exact largest obstruction.

## Verification
Run `python3 artifacts/verify.py` in the artifact directory. The checker prints `CHECKER_PASS` only after verifying both finite base intervals, nonrepresentation of \(9083\), cross-implementation agreement of the bitset and boolean-array membership algorithms, and additional arithmetic and degree spot checks. A separate recorded output is included as `artifacts/check_output.txt`.

The finite checks are exhaustive over the stated finite ranges, not extrapolations to infinity. The universal extension is exactly the algebraic induction (4)--(5). For illustration, \(9084=c_{13}+c_{30}+c_{32}=703+3916+4465\); its index gaps are at least two.

## Relationship to prior work
Kureš proved Pollock's conjecture that every positive integer is a sum of at most eleven centered nonagonal numbers, allowing repeated terms. In contrast, this result restricts both multiplicities and index gaps. OEIS A352349 records \(2648\) as the largest obstruction for sums of **distinct** centered nonagonal numbers, where consecutive indices are still allowed. Hence that known exact cutoff does not imply \(9083\), and the increase measures a concrete cost of the no-adjacent-indices rule.

Dantas e Moura and collaborators develop \(S\)-legal index-difference representations and recurrence criteria for the *greedily constructed* sequences determined by those constraints. Their accessible manuscript is inspected for definitions, examples and main results. The centered nonagonal sequence is a prescribed quadratic sequence and is not one of their greedy sequences; their theorem does not give the finite complement or the exact cutoff here.

## Limitations
The exact threshold is proved for the specified centered nonagonal sequence and the single forbidden index gap \(1\). No claim is made about other centered polygonal parameters, the number of representations, uniqueness, or the optimal size of a summand set. Computation certifies finite bases, while the infinite range uses a symbolic induction. The relevant short 2023 centered-nonagonal article was available as a bibliographic preview, not accessible full text; additional unindexed material remains a literature risk. There has been no independent scientific audit.

## References
1. G. Z. Dantas e Moura, A. Keisling, A. Lilly, A. Mauro, S. J. Miller, M. Phang, S. Velazquez Iannuzzelli, *Recurrence Relations for \(S\)-Legal Index Difference Sequences*, arXiv:2210.10577, first submitted 19 October 2022. https://arxiv.org/html/2210.10577v2 .
2. M. Kureš, *A Proof of Pollock's Conjecture on Centered Nonagonal Numbers*, *Mathematical Intelligencer* 46 (2024), 234--235; first published 27 October 2023. https://doi.org/10.1007/s00283-023-10307-0 .
3. I. Gutkovskiy, OEIS A352349, *Largest integer not representable as a sum of distinct centered polygonal numbers*, created 12 March 2022. https://oeis.org/A352349 .
