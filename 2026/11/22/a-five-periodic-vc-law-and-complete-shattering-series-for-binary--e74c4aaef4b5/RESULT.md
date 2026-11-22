# A five-periodic VC law and complete shattering series for binary words avoiding `0011`

## Finding

For each integer \(n\geq0\), let \(\mathcal H_n\subseteq\{0,1\}^n\) be **all** binary words that avoid the contiguous factor `0011`. These words are Boolean concepts under queries of individual coordinates. Put
\[
\Phi_n(z)=\sum_{S\subseteq[n]:\,\mathcal H_n\text{ shatters }S}z^{|S|},\qquad
F(t,z)=\sum_{n\ge0}\Phi_n(z)t^n.
\]
Then the full, coefficientwise shattering series is the following rational function, with exact integer coefficients:
\[
\boxed{
F(t,z)=\frac{1+t(1-t)z+t^2(1-t^2)z^2+t^3(1+t-t^2+t^3)z^3-t^6z^4}{1-t+t^2(t-2)z-t^4(1-t)z^2-t^5(1-t)^2z^3}.
}
\]
Moreover, its maximum degree has a *five-periodic* sharp law:
\[
\boxed{\operatorname{VCdim}(\mathcal H_n)=\left\lfloor\frac{3n+6}{5}\right\rfloor\quad(n\ge1),}\qquad \operatorname{VCdim}(\mathcal H_0)=0.
\]
Equivalently, the VC dimension increases by exactly three when the word length increases by five, for every \(n\ge1\). For instance,
\[
\begin{aligned}
\Phi_8(z)&=1+8z+28z^2+56z^3+61z^4+28z^5+z^6,\\
\Phi_{10}(z)&=1+10z+45z^2+120z^3+197z^4+186z^5+78z^6+4z^7.
\end{aligned}
\]
The proof gives an explicit seven-accepting-state automaton which recognizes the **indicator word of every shattered support** at every length. It is not merely an asymptotic or rank-only result.

## Assumptions and scope

All coordinates are labeled and linearly ordered (no cyclic wrap). The word `0011` is forbidden as a consecutive block, not as a scattered subsequence. A support \(S\subseteq[n]\) is shattered precisely when
\[\forall\lambda:S\longrightarrow\{0,1\}\quad \exists w\in\mathcal H_n\quad\forall i\in S:\ w_i=\lambda(i).\]
Completions at the unqueried coordinates may depend on the labeling. The empty support is counted and is shattered since an all-zero word is admissible at every length. A support indicator has bit one at queried positions and bit zero at unqueried positions; this indicator is distinct from the underlying hypothesis word.

## Proof

**1. Four-state suffix recognizer.** Define states \(0,1,2,3\) as the lengths of the longest suffix of the already-read hypothesis equal to a proper prefix of `0011`. Beginning at state \(0\), the transitions for appending hypothesis bits \(0\) and \(1\), respectively, are
\[
\begin{array}{c|cc}q&0&1\\\hline
0&1&0\\1&2&0\\2&2&3\\3&1&\bot
\end{array}.
\]
The rejecting transition \(\bot\) occurs exactly when `0011` has just appeared. Each of the four ordinary states is accepting, so a partial hypothesis is extendible if and only if at least one of its current states remains possible.

**2. Alternating-quantifier subset families.** Represent a nonempty set of suffix states by a four-bit mask \(Q\). Let \(T_b(Q)\) be the union of nonrejecting one-bit successors of elements of \(Q\), for \(b\in\{0,1\}\). For a *family* \(\mathscr F\) of such nonempty sets, define updates at a support-indicator symbol by
\[
U_0(\mathscr F)=\{T_0(Q)\cup T_1(Q):Q\in\mathscr F\},
\qquad
U_1(\mathscr F)=\{T_0(Q),T_1(Q):Q\in\mathscr F\}.
\]
Repeated family members are identified, and any occurrence of the empty set sends the process to a permanent rejecting sink. Start from \(\mathscr F_0=\{\{0\}\}\). The update \(U_0\) existentially completes an unqueried coordinate, while \(U_1\) retains both possible prescribed query bits. Induction on the scanned indicator prefix shows that \(\mathscr F\) comprises exactly the possible suffix-state sets for all prescribed assignments on previously queried coordinates. Since every ordinary suffix state accepts the empty continuation, the indicator is accepted if and only if **every** prescribed labeling has an admissible completion. This proves that the resulting deterministic finite automaton recognizes exactly the shattered supports, without approximation or finite-length assumptions.

**3. Explicit exact quotient.** Breadth-first closure of these two operations yields exactly \(26\) nonrejecting reachable subset-family states. Their complete masks, targets, and equivalence classes are in `state_certificate.txt`. Partitioning these states by equality of future acceptance languages yields **seven** nonrejecting quotient states, labeled \(0,\ldots,6\), and sink \(7\). The full transition table is
\[
\begin{array}{c|cc}
q&\text{unqueried }0&\text{queried }1\\\hline
0&0&1\\1&0&4\\2&0&5\\3&0&6\\4&2&6\\5&1&7\\6&3&7\\7&7&7
\end{array}.
\]
The initial quotient state is \(0\); all states \(0,\ldots,6\) are accepting. Every row of the certificate can be checked by the four-state transition table in Step 1 and the two displayed family updates. The claimed quotient can be checked by comparing class labels on both transitions. Conversely, successive future-acceptance partition refinements distinguish all eight displayed classes, so the quotient is exact. This supplies a finite, explicitly reproducible certificate of the only nonstandard finite reduction used below.

**4. Full enumerator.** Let \(H_q(t,z)\) count accepted indicator continuations from quotient state \(q\); the empty continuation contributes one in every accepting state, and \(H_7=0\). A zero indicator symbol has weight \(t\); a one has weight \(tz\). The table gives
\[
\begin{array}{lll}
H_0=1+tH_0+tzH_1,&H_1=1+tH_0+tzH_4,&H_2=1+tH_0+tzH_5,\\
H_3=1+tH_0+tzH_6,&H_4=1+tH_2+tzH_6,&H_5=1+tH_1,\\
H_6=1+tH_3.&&
\end{array}
\]
This system has a unique formal power-series solution because its transition terms are divisible by \(t\). Solving these seven linear equations gives the displayed rational expression for \(H_0=F(t,z)\). The exact integer-polynomial cross-multiplications in `verify_0011.py` verify the seven equations using an explicit common denominator, not a numerical series fit.

**5. Exact maximum-degree law.** On the same seven states form a maximum-plus matrix \(A\): the edge read as a zero support-indicator symbol has weight \(0\), the edge read as one has weight \(1\), and missing edges have weight \(-\infty\). The \((i,j)\)-entry of \(A^k\) equals the maximum number of selected coordinates in any accepted length-\(k\) indicator path from \(i\) to \(j\). Direct max-plus multiplication of the explicit seven-state table yields the following *entrywise* identity:
\[
\boxed{A^{11}=A^6+3.}
\]
Here \(+3\) adds three to every finite matrix entry. Both matrices are printed in `state_certificate.txt`, so this is a finite check of \(49\) integer equalities. Multiplication on the right by \(A^j\) proves \(A^{11+j}=A^{6+j}+3\) for all \(j\ge0\). Taking the maximum of row zero shows that the maximum support size increases by three every five lengths beginning at length six. The direct initial maxima for lengths \(1,2,\ldots,10\) are
\[
1,2,3,3,4,4,5,6,6,7,
\]
which agree with \(\lfloor(3n+6)/5\rfloor\). The matrix identity and these ten base cases establish the formula for **every** positive length. The empty-length case is immediate.

## Verification

Run `python3 verify_0011.py` with Python 3.9 or later; it uses only the standard library and requires no network connection. The script reconstructs the 26 reachable subset-family states, checks their exact quotient and distinct future-acceptance classes, verifies all seven polynomial identities, verifies \(A^{11}=A^6+3\), and exhaustively compares the actual traces of **every** support with the automaton decision for all lengths \(0\le n\le12\) (\(8{,}191\) support decisions). Direct enumeration also independently checks every coefficient of each corresponding shattering polynomial. Finite brute force corroborates, rather than substitutes for, the symbolic all-length proof. `state_certificate.txt` records the complete finite reductions.

## Relationship to prior work

Johnson's 2021 *Binary strings of finite VC dimension* studies translate/subword families obtained from an **individual fixed binary word**; Section 2's exact definitions do not give the coordinate-shattering complex of the **entire language** avoiding `0011`. Its first public version was posted 2021-01-16 (arXiv:2101.06490), which motivates the string-complexity question but does not imply the two boxed formulas. The 2016 article by Itsykson, Okhotin, and Oparin, *Computational and Proof Complexity of Partial String Avoidability*, gives complexity results for avoiding collections of partial words in two-sided infinite strings. This is a different quantifier/input model and does not calculate the present all-length coordinate-support enumeration. The public result *A regular shattering complex for binary words with no monochromatic triple* classifies the **different** language avoiding both `000` and `111`, whose rational series and rank law are not equal to those above. These comparisons concern actual objects, assumptions, and implications; similarity of titles alone is not evidence.

The method of deterministic-automaton determinization is established theory and is **not** claimed as an invention. The claim assessed here is the exact unusually small quotient, the explicit coefficientwise rational generating function, and the sharp five-periodic rank law for the natural two-run forbidden factor `0011`. No complete published statement inspected in this search contains or implies these specific assertions. Priority remains subject to independently checking unindexed or inaccessible equivalent publications.

## Limitations

The result does not concern cyclic boundary conditions, multiple forbidden factors, scattered avoidance, online Littlestone dimension, or one fixed input word. In particular, the rank law is not asserted for all length-four forbidden patterns. The finite automaton has been independently enumerated but there is no independently commissioned mathematical audit. The work does not establish publication priority in all historical sources.

## References

- H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490 (first public version 2021-01-16), https://arxiv.org/abs/2101.06490.
- D. Itsykson, A. Okhotin, V. Oparin, *Computational and Proof Complexity of Partial String Avoidability*, MFCS 2016, Article 51, https://doi.org/10.4230/LIPIcs.MFCS.2016.51.
- B. Chornomaz, *What Convex Geometries Tell About Shattering-Extremal Systems*, Electronic Journal of Combinatorics 29(3) (2022), Article P3.40, https://doi.org/10.37236/10750.
- *A regular shattering complex for binary words with no monochromatic triple*, publicly indexed mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-regular-shattering-complex-for-binary-words-with-no-monochroma--a86c7bc37664/RESULT.md.
