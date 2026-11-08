# A regular shattering complex for binary words with no monochromatic triple

## Finding

Let \(\mathcal H_n\) be the set of binary words \(w_1\ldots w_n\), \(n\geq 0\), that contain neither \(000\) nor \(111\) as a consecutive factor. Treat the words as Boolean concepts on the coordinate set \([n]\). For \(S\subseteq[n]\), encode queried positions by the indicator word \(b(S)\in\{0,1\}^n\).

**Exact support theorem.** The set \(S\) is VC-shattered by \(\mathcal H_n\) if and only if (a) \(b(S)\) has no factor \(111\), and (b) between any two distinct factors \(11\) of \(b(S)\) there is a factor \(00\). Equivalently, the minimal forbidden factors in the support indicator are \(111\) and all \(11\,0(10)^r\,11\), for integers \(r\geq0\). Here the symbols in these indicator words describe queried and unqueried positions, not hypothesis labels.

Write \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\), including the empty support. Then the exact bivariate generating function is

\[
\sum_{n\geq0}\Phi_n(z)t^n
=\frac{1+tz-t^2z+t^2z^2}{1-t-2t^2z+t^3z}.
\]

Equivalently, \(\Phi_0=1\), \(\Phi_1=1+z\), \(\Phi_2=(1+z)^2\), and for all \(n\geq3\),

\[
\Phi_n(z)=\Phi_{n-1}(z)+2z\Phi_{n-2}(z)-z\Phi_{n-3}(z).
\]

For every \(n\geq1\), \(\operatorname{VCdim}(\mathcal H_n)=\lfloor n/2\rfloor+1\); the empty-domain dimension at \(n=0\) is zero. For instance, \(\Phi_5(z)=1+5z+10z^2+7z^3\) and \(\Phi_8(z)=1+8z+28z^2+50z^3+41z^4+8z^5\).

For comparison, call \(S\) *fixed-background free* if one assignment to every coordinate outside \(S\) works simultaneously with every binary labeling of \(S\). For \(n\geq3\), this stronger property holds exactly when each three consecutive positions contain at most one member of \(S\), and its maximum possible size is \(\lceil n/3\rceil\). Thus the difference between existential VC-shattering and the fixed-background notion grows linearly in word length.

## Assumptions and scope

All words are finite and indexed linearly, not cyclically. A word is admissible precisely when no three consecutive symbols coincide. Shattering means \(\forall\lambda:S\to\{0,1\}\ \exists w\in\mathcal H_n\ \forall i\in S:\,w_i=\lambda(i)\); the completion outside \(S\) may depend on \(\lambda\). The generating function counts labeled coordinate supports, not isomorphism classes. The displayed characterization includes the short lengths \(n=0,1,2\).

## Proof

**Obstruction.** A support with three consecutive queried positions cannot be shattered: label those three equally. Suppose two factors \(11\) in its indicator have no factor \(00\) between them, and assume no indicator factor \(111\). Taking consecutive such factors, the subword from the first pair to the second has the form \(11\,0(10)^r\,11\), \(r\geq0\). Assign equal hypothesis bits to the left pair, say \(0,0\), forcing the next unqueried position to be \(1\). At each intervening isolated queried position assign the bit already forced at its immediately preceding unqueried position; to avoid a monochromatic triple the next unqueried position is forced to be the complement. Finally give the right queried pair the bit forced at its immediately preceding unqueried position. No completion then avoids a monochromatic triple. Hence this support cannot be shattered.

**One-double extension lemma.** In any indicator segment with no factor \(00\) and at most one factor \(11\), every assignment to its queried positions extends to a word avoiding \(000\) and \(111\). If there is one queried adjacent pair, complete unqueried coordinates on its left with the complement of the nearest queried symbol to the right, and those on its right with the complement of the nearest queried symbol to the left. Every three-coordinate window then contains two opposite symbols: if it includes the queried pair and a hole, the hole is its complement; in other cases an isolated hole is opposite a neighboring queried bit. Without a queried pair, complement the nearest queried bit to the right for each hole (or to the left at the right endpoint); the same window check applies. The all-unqueried cases of lengths zero through two are immediate.

**Bridge lemma.** Any two admissible binary fragments separated by \(g\geq2\) consecutive unqueried coordinates can be joined without a monochromatic triple. If both fragments are nonempty, choose the first bridging bit opposite the left fragment's final bit and the last bridging bit opposite the right fragment's first bit. For \(g=2\) this completes the bridge. For \(g\geq3\), alternate the first \(g-1\) bridge bits and choose the last as prescribed; the final three bridge bits cannot all be equal because the preceding two alternate. At the two boundaries, the chosen bit differs from the adjacent fragment bit. If a fragment is empty, an alternating extension suffices. This proves the lemma.

Now remove each pair of consecutive unqueried positions as a separator. The remaining maximal segments have no factor \(00\), and, by the support criterion, have at most one factor \(11\). Apply the one-double lemma independently to each segment and join them by the bridge lemma. This realizes *every* prescribed labeling of \(S\), proving sufficiency and the exact support theorem.

**Enumerator.** Read the support indicator left to right. After two symbols, use six states: \(A=00\), \(B=01\) and \(C=10\) when no \(11\) has appeared since the last \(00\); and \(D=11\), \(E=01\), \(F=10\) when a \(11\) has appeared since the last \(00\). An appended indicator bit \(1\) carries weight \(z\), and \(0\) carries weight \(1\). The allowed transitions are

\[
A\xrightarrow{0}A,\ A\xrightarrow{1}B;\quad
B\xrightarrow{0}C,\ B\xrightarrow{1}D;\quad
C\xrightarrow{0}A,\ C\xrightarrow{1}B;
\]
\[
D\xrightarrow{0}F;\quad E\xrightarrow{0}F;\quad
F\xrightarrow{0}A,\ F\xrightarrow{1}E.
\]

The initial length-two state weights in order \(A,B,C,D,E,F\) are \((1,z,z,z^2,0,0)\). Let \(f_U\) count all weighted future continuations from state \(U\), including the empty continuation, with length variable \(t\). The transition equations yield \(f_A=f_C\), \(f_B=f_F\), \(f_D=f_E=1+tf_B\), and

\[
f_A=1+tf_A+tzf_B,\qquad f_B=1+tf_A+tz(1+tf_B).
\]

Solving gives

\[
f_B=\frac{1+tz-t^2z}{1-t-2t^2z+t^3z}.
\]

Adding the empty support at length zero, the two length-one words, and the initial length-two state contributions gives

\[
1+(1+z)t+t^2\bigl((1+z)f_A+zf_B+z^2f_D\bigr)
=\frac{1+tz-t^2z+t^2z^2}{1-t-2t^2z+t^3z},
\]

as required. Extracting coefficients of \(t\) establishes the recurrence.

**Sharp dimension.** Let \(k=|S|\) and \(r\) be the number of maximal queried runs of length two. The criterion forbids longer runs. If \(r=0\), at least \(k-1\) unqueried positions separate its singleton runs, hence \(n\geq2k-1\). If \(r\geq1\), there are \(k-r\) queried runs. At least \(k-r-1\) unqueried coordinates separate successive runs, and the separation of successive double runs requires at least \(r-1\) additional unqueried coordinates. Hence \(n\geq k+(k-r-1)+(r-1)=2k-2\). Therefore \(k\leq\lfloor n/2\rfloor+1\). Equality is attained for \(n\geq2\) by the indicator \(11(01)^{k-2}\), padded with zeros at the right when necessary, taking \(k=\lfloor n/2\rfloor+1\). For \(n=1\), the singleton support is shattered.

**Fixed-background comparison.** In any three-coordinate window containing at least two free coordinates, an adversarial assignment can make all three bits equal, irrespective of the fixed background. Conversely, if every such window has at most one free coordinate, assign the other coordinates alternately in their natural increasing order. The two fixed coordinates of any window with one free coordinate are consecutive among fixed positions and hence differ; in a window with no free coordinates, consecutive fixed bits differ. Thus all choices of free coordinates are admissible. A three-separated set of positions has maximum size \(\lceil n/3\rceil\) for \(n\geq3\).

## Verification

Run `python3 verify.py` with Python 3.9 or newer. It independently enumerates all admissible hypothesis words and all support subsets for each \(0\leq n\leq15\), compares every shattering decision against the forbidden-indicator characterization, and checks the complete polynomial recurrence at every such length. It also independently checks all 16 two-bit bridge boundary patterns and the fixed-background size bound through length ten. The script prints `NO_MONOCHROMATIC_TRIPLE_SHATTERING_PASS` only after all assertions succeed. These finite tests corroborate, but do not replace, the all-length proofs above.

## Relationship to prior work

Johnson, *Binary strings of finite VC dimension* (arXiv:2101.06490, first posted January 16, 2021), studies complexity obtained from the substrings of an **individual** binary string and their translates; that differs from the coordinate traces of the **entire constrained language** considered here. Louidor, Marcus and Pavlov, *Independence entropy of \(\mathbb Z^d\)-shift spaces* (2013), define multi-choice shifts with one **fixed** filling outside free positions. That notion directly motivates the last comparison but does not imply existential VC-shattering: already at length three, two adjacent query positions can be shattered with completion depending on their labels, though no fixed third bit serves both constant labelings. Chornomaz (2022) develops general forbidden-projection characterizations for shattering-extremal systems, not this language's specific forbidden supports or coefficientwise enumerator. The all-order support classification, generating function and growing fixed-background gap are the specific claims assessed here.

## Limitations

The theorem concerns linear finite words and forbids exactly the two constant triples. It does not determine Littlestone dimension, other run-length constraints, cyclic boundary conditions, or asymptotic independence entropy for arbitrary shifts. The full historical priority of the specialized support characterization remains subject to further independent literature review; no claim of independent certification is made.

## References

- H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first posted 2021-01-16. https://arxiv.org/abs/2101.06490.
- E. Louidor, B. Marcus, R. Pavlov, *Independence entropy of \(\mathbb Z^d\)-shift spaces*, Acta Applicandae Mathematicae 126 (2013), 297–317, DOI: 10.1007/s10440-013-9819-2.
- B. Chornomaz, *What Convex Geometries Tell About Shattering-Extremal Systems*, Electronic Journal of Combinatorics 29(3) (2022), #P3.40, DOI: 10.37236/10750.
- S. Hu, N. Weinberger, O. Shayevitz, *On the VC-Dimension of Binary Codes*, SIAM Journal on Discrete Mathematics, DOI: 10.1137/18M116486X.
