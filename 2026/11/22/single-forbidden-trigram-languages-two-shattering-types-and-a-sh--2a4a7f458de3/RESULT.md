# Single-forbidden-trigram languages: two shattering types and a sharp extremality dichotomy

## Finding

For every integer \(n\geq0\) and every binary word \(w\) of length three, let \(\mathcal L_n(w)\) consist of all binary words of length \(n\) that avoid \(w\) as a **contiguous** factor. A Boolean concept selects exactly the coordinates where its word has symbol \(1\). A coordinate support \(Q\subseteq[n]\) is shattered when every assignment \(Q\to\{0,1\}\) extends to a word in \(\mathcal L_n(w)\).

All eight forbidden factors fall into the following exact classes.

**Class A:** For \(w\in\{000,010,101,111\}\), the support \(Q\) is shattered if and only if it contains no three consecutive coordinates. With \(A_n(z)=\sum_{Q\text{ shattered}}z^{|Q|}\),
\[
\sum_{n\geq0}A_n(z)t^n=\frac{1+zt+z^2t^2}{1-t-zt^2-z^2t^3},\qquad
\operatorname{VCdim}(\mathcal L_n(w))=\left\lceil\frac{2n}{3}\right\rceil.
\]

**Class B:** For \(w\in\{100,011\}\), the support \(Q\) is shattered if and only if it contains no \(i<j\) with \(i,j,j+1\in Q\). For \(w\in\{001,110\}\), reverse the order of the coordinates: there must be no \(i+1<j\) with \(i,i+1,j\in Q\). The two orientations have the same face polynomial:
\[
B_n(z)=1+nz+\sum_{k=2}^{\lfloor(n+2)/2\rfloor}\binom{n-k+2}{k}z^k.
\]
For every \(n\geq1\), their VC dimension is \(\lfloor(n+2)/2\rfloor\); at \(n=0\), the dimension is zero.

The shattering complexes of classes A and B are respectively the independence complexes of a consecutive-triple hypergraph and an oriented-triple hypergraph; all minimal nonfaces are triples. Although the class-A factors \(000\) and \(010\) have **identical** shattered-support complexes at every length, their word counts differ. The Sauer-type extremality equality \(|\mathcal L_n(w)|=|\operatorname{Sh}(\mathcal L_n(w))|\) holds for all lengths for \(000,111,001,011,100,110\), but fails for \(010,101\) at every \(n\geq4\) (and holds at \(n\leq3\)). More precisely,
\[
\sum_{n\geq0}\bigl(|\operatorname{Sh}(\mathcal L_n(010))|-|\mathcal L_n(010)|\bigr)t^n
=\frac{t^4}{(1-t-t^2-t^3)(1-2t+t^2-t^3)}.
\]
Every coefficient from degree four onward is strictly positive.

## Assumptions and scope

Words are linear (not cyclic); forbidden occurrences are contiguous, allow overlap, and may begin at any of the first \(n-2\) positions. For \(n<3\) the avoidance condition is vacuous. Each queried position is a binary coordinate, and \(\operatorname{Sh}(\mathcal L_n(w))\) is the family of coordinate sets whose traces contain all \(2^{|Q|}\) labelings. The empty support is shattered since the concept class is nonempty. Complementing all word symbols and reversing all coordinates act bijectively on concept families and preserve the sizes and shattering properties of their supports, with reversal carrying a support to its reflected copy.

## Proof

### A. The two support predicates

For the forbidden factor \(000\), if \(Q\) contains a consecutive triple, the assignment zero to its three coordinates cannot extend. Otherwise take any labeling of \(Q\) and put \(1\) at every unqueried coordinate. Every zero then occurs on \(Q\), so no forbidden triple appears. Complementing the symbols proves the identical support statement for \(111\).

For \(010\), a queried consecutive triple can be labeled \(010\) and is therefore not shattered. Conversely suppose \(Q\) has no consecutive triple, and fix an arbitrary labeling of \(Q\). Keep its prescribed symbols. Consider the gaps of remaining positions between consecutive prescribed zeros, as well as the initial and terminal gaps. Fill every unqueried position with \(1\), except that in an internal gap consisting of precisely one position, fill that position with \(0\) when it is unqueried. If an internal one-position gap is queried and labeled \(1\), its two neighboring prescribed zeros would give a forbidden consecutive triple lying in \(Q\), contrary to the hypothesis. Every maximal run of ones between zeros now has length either zero or at least two, while a run touching either word boundary may have length one. Hence no \(010\) occurs. Symbol complementation proves the same criterion for \(101\).

For \(100\), if \(i<j\) and the three coordinates \(i,j,j+1\) are queried, prescribing a one at \(i\) and zeros at \(j,j+1\) is impossible: any extension has a last one at or before \(j-1\), followed by a string of zeros containing \(j,j+1\), and hence a contiguous \(100\). Conversely, assume no such triple belongs to \(Q\). Given any assignment on \(Q\), if there is no prescribed one, fill every remaining position with zero. Otherwise let \(i\) be its first prescribed one, put zero in every unqueried position before \(i\), and put one in every unqueried position from \(i\) onward. All zeros after the first one are prescribed, and no two of them can be adjacent because that would produce queried positions \(i,j,j+1\). Thus the resulting word avoids \(100\). Complementation gives \(011\), while reversal gives \(001\) and \(110\) and reverses the stated forbidden triple.

These arguments prove both necessary and sufficient conditions, not merely upper bounds. Because each prohibited triple is itself a minimal nonface, the asserted three-uniform descriptions follow.

### B. Face enumeration and dimensions

For class A, a support is a binary indicator word with no run of three ones. Splitting according to its final run of ones of length zero, one or two gives, for \(n\geq3\),
\[
A_n(z)=A_{n-1}(z)+zA_{n-2}(z)+z^2A_{n-3}(z),
\]
with \(A_0(z)=1\), \(A_1(z)=1+z\), and \(A_2(z)=(1+z)^2\), producing the generating function above. Each disjoint group of three positions contains at most two selected positions; choosing the pattern \(110110\cdots\), truncated to length \(n\), attains \(n-\lfloor n/3\rfloor=\lceil2n/3\rceil\).

For class B in the \(100\) orientation, once the smallest selected position \(i\) is fixed, every further selected position lies in \(\{i+1,\ldots,n\}\), and no two of these may be adjacent. Therefore for every \(k\geq2\) the number of \(k\)-element supports is
\[
\sum_{i=1}^n\binom{n-i-(k-1)+1}{k-1}=\binom{n-k+2}{k},
\]
where out-of-range binomial coefficients vanish. There is one empty support and \(n\) singleton supports. The binomial coefficient is positive exactly when \(n-k+2\geq k\), equivalently \(2k-2\leq n\). An extremal support starts with two adjacent selected coordinates and then leaves a gap of one unselected coordinate between subsequent selected coordinates, thereby realizing size \(\lfloor(n+2)/2\rfloor\). This proves the sharp VC dimension. Reversal preserves all counts.

### C. Equality and strictness in the shattering inequality

For class A, \(|\operatorname{Sh}(\mathcal L_n(w))|=A_n(1)\). The supports counted by \(A_n(1)\) are in bijection (by coordinatewise complementation) with the words avoiding \(000\); therefore \(|\mathcal L_n(000)|=|\mathcal L_n(111)|=A_n(1)\).

For class B take \(w=100\). Either a word is all zeros, or the position of its first one is fixed and its remaining suffix contains no adjacent pair of zeros. The number of length-\(m\) binary words avoiding \(00\) is the Fibonacci number \(F_{m+2}\), where \(F_0=0,F_1=1\). Thus
\[
|\mathcal L_n(100)|=1+\sum_{m=0}^{n-1}F_{m+2}=F_{n+3}-1.
\]
The same sum counts class-B shattered supports: choose their smallest coordinate, then an independent subset of the remaining path. Hence \(|\operatorname{Sh}(\mathcal L_n(100))|=F_{n+3}-1\). Symmetries give the other three members of class B.

Finally, write \(c_n=|\mathcal L_n(010)|\). A four-state automaton tracking the final two letters, with states \(00,01,10,11\), has transition matrix (rows source, columns target)
\[
T=\begin{pmatrix}
1&1&0&0\\
0&0&0&1\\
1&1&0&0\\
0&0&1&1
\end{pmatrix},
\]
where the excluded transition is \(01\to10\). Starting with one word per state at length two and including \(c_0=1,c_1=2\), a direct geometric-series calculation gives
\[
\sum_{n\geq0}c_nt^n=\frac{1+t^2}{1-2t+t^2-t^3}.
\]
Subtracting this from \(\sum_{n\ge0}A_n(1)t^n=(1+t+t^2)/(1-t-t^2-t^3)\) yields the defect series in the theorem. Its first denominator has the positive-coefficient inverse \(\sum_{k\ge0}(t+t^2+t^3)^k\). Its second denominator has the positive-coefficient inverse
\[
\frac1{(1-t)^2-t^3}=\sum_{h\ge0}\frac{t^{3h}}{(1-t)^{2h+2}}.
\]
Both inverse series have strictly positive coefficients at all nonnegative degrees. Consequently the defect is zero through degree three and strictly positive from degree four onward. Complementation transfers this exact conclusion to \(101\).

## Verification

Two standalone implementations exhaustively compare predicted supports with all traces of every avoidance language, for all eight forbidden triples. The Python implementation checks all lengths \(0\) through \(9\); the separately implemented C++17 program checks all lengths \(0\) through \(11\). Each also checks face coefficients and equality/strictness against concept counts. To reproduce from the accompanying files:

```sh
python3 verify_binary_trigrams.py
c++ -O2 -std=c++17 verify_binary_trigrams.cpp -o verify_binary_trigrams
./verify_binary_trigrams
```

Expected final markers: `PYTHON_CHECK_PASS` and `CPP_CHECK_PASS`. The complete finite tests corroborate but do not substitute for the all-length mathematical argument above.

## Relationship to prior work

Coordinate shattering of binary codes and the Sauer–Shelah inequality are established subjects, as in Hu, Weinberger and Shayevitz [1]. Shattering-extremal set systems and their general inequality are developed by Mészáros and Rónyai [2]. Chandgotia, Marcus, Richey and Wu [4], building on Guibas and Odlyzko [5], establish that standard autocorrelation data determine all single-forbidden-word **avoidance counts**; those counts are treated here as established background, not a new pattern-count theorem. Their dynamical invariants and conjugacy results do not supply coordinate-shattering faces. Work on VC dimensions of automata recognizing equal-length words [3] concerns word-set classifiers, rather than the coordinate concept family of a fixed factor-avoidance language. An available study of words simultaneously avoiding \(000\) and \(111\) treats a strictly smaller hypothesis family and does not determine the eight single-forbidden-factor classes. No claim is made that the general shattering inequality, Fibonacci avoidance counts, or the use of complement/reversal symmetries is new. The claimed addition is the combined exact eight-case support classification, its two face polynomials and the sharp same-face/different-extremality dichotomy.

## Limitations

This result applies only to one forbidden contiguous **binary** word of length three and to coordinate queries. It gives no general classification for longer forbidden factors, simultaneous forbidden factors, larger alphabets or non-coordinate queries. It does not determine online Littlestone dimensions. An indexed literature search and inspection of relevant primary texts do not exclude earlier equivalent statements in unindexed theses or appendices; the originality assessment is provisional and independent review has not occurred. Numerical program outputs are finite tests; universal claims rest on the proofs above.

## References

[1] Sihuang Hu, Nir Weinberger, Ofer Shayevitz, “On the VC-Dimension of Binary Codes”, arXiv:1703.01586 (initial public version 2017-03-05), https://arxiv.org/abs/1703.01586 .

[2] Tamás Mészáros and Lajos Rónyai, “Shattering-Extremal Set Systems of Small VC-Dimension”, *The Scientific World Journal* (2013), article 126214, https://doi.org/10.1155/2013/126214 .

[3] Bjørn Kjos-Hanssen, Clyde James Felix, Sun Young Kim, Ethan Lamb and Davin Takahashi, “VC-dimensions of nondeterministic finite automata for words of equal length”, ISAIM 2020, https://isaim2020.cs.ou.edu/papers/ISAIM2020_Kjos-Hanssen_etal.pdf .

[4] Nishant Chandgotia, Brian Marcus, Jacob Richey, Chengyu Wu, “Shifts of Finite Type Obtained by Forbidding a Single Pattern”, arXiv:2409.09024 (initial public version 2024-09-13), https://arxiv.org/abs/2409.09024 .

[5] L. J. Guibas and A. M. Odlyzko, “String overlaps, pattern matching, and nontransitive games”, *Journal of Combinatorial Theory, Series A* 30 (1981), 183–208, https://doi.org/10.1016/0097-3165(81)90005-4 .
