# Exact common-zero insertion distance for binary words of weight two

## Finding

For two binary words \(u,v\in\{0,1\}^n\) containing exactly two ones each, let \(\eta(u,v)\) be the least number of zeros that can be inserted at identical gaps in both words so that the resulting equal-length words are cyclic rotations of one another. The insertions in either word must be identical in number and position; only zeros may be inserted. Index original positions by \(\mathbb Z_n\), and let \(P,Q\) be the two-element supports of \(u,v\).

For \(n\ge2\), write \(P=\{p_0<p_1\}\), \(Q=\{q_0<q_1\}\), and let \(A=[p_0,p_1)\), \(B=[q_0,q_1)\), interpreted as sets of cyclic edges. For subsets of these edges put

\[
\Lambda(C,D)=\begin{cases}
0,&C=D,\\
\bigl||C\setminus D|-|D\setminus C|\bigr|,&C\setminus D\ne\varnothing\text{ and }D\setminus C\ne\varnothing,\\
+\infty,&\text{otherwise}.
\end{cases}
\]

Then the **exact instance-wise optimum** is

\[
\boxed{\eta(u,v)=\min\{\Lambda(A,B),\Lambda(A,B^c)\}.}
\]

Every optimum can be realized by putting **all inserted zeros into one common gap** (and no insertion when the optimum is zero). In particular, for every \(n\ge4\),

\[
\boxed{\max_{|u|_1=|v|_1=2}\eta(u,v)=n-3.}
\]

Exactly \(4n\) **ordered** pairs \((u,v)\) attain this maximum. Their two supports share exactly one position \(a\), and their other positions are \(a+1,a+2\), or \(a-1,a-2\), modulo \(n\), assigned to the two words in either order. At \(n=2\) or \(n=3\), the maximum is zero.

## Assumptions and scope

The alphabet is \(\{0,1\}\). Both input words have the same length \(n\ge2\) and exactly two occurrences of \(1\). A simultaneous zero insertion at any gap adds the same number of zeros at the corresponding position in both words; there are \(n+1\) linear gaps before, between, or after input letters. Cyclic equivalence means equality up to one rotation, not reversal or symbol complementation. The number of inserted zeros is the **number inserted in each word**, not the sum across both words.

In the formula, a cyclic edge \(i\) is the gap going from original position \(i\) to position \(i+1\pmod n\). The complementary arc \(B^c\) is taken within all \(n\) cyclic edges. All maxima and extremizer counts refer to labeled input positions and ordered input pairs.

## Proof

**1. Reduction to positive circular gaps.** Choose nonnegative integers \(z_0,\ldots,z_{n-1}\), where \(z_i\) zeros are inserted between consecutive original positions \(i\) and \(i+1\pmod n\), and define \(g_i=1+z_i\). The expanded circle has length \(L=\sum_i g_i=n+\sum_i z_i\). This captures all linear simultaneous insertions: zeros inserted before the first or after the last input symbol belong to the same circular gap, and their division changes only the common choice of origin. The distance in clockwise positions between the two original ones of \(u\) is \(\sum_{i\in A}g_i\), and similarly for \(v\) using \(B\). Two two-point sets on a circle are translates exactly when one clockwise separation equals one of the two clockwise separations of the other set. Therefore the expanded words are rotations exactly when

\[
\sum_{i\in A}g_i=\sum_{i\in B}g_i
\quad\text{or}\quad
\sum_{i\in A}g_i=\sum_{i\in B^c}g_i.
\]

**2. Exact cost of one arc equality.** For a fixed choice of arcs \(C,D\), cancel their common edges. The equality becomes

\[
\sum_{i\in C\setminus D}(1+z_i)=
\sum_{i\in D\setminus C}(1+z_i).
\]

If the two exclusive sets are both empty, the cost is zero. If exactly one is empty, equality is impossible because all gap lengths are positive. Otherwise, the baseline side sizes differ by \(\bigl||C\setminus D|-|D\setminus C|\bigr|\); at least that many zeros must be added on the smaller side. Inserting precisely that number in **one** of its edges attains equality. Thus the minimum for this orientation is \(\Lambda(C,D)\), proving the instance-wise formula and the single-gap optimality assertion. At least one of the two orientations is feasible, as the following cases show.

**3. Supports sharing one position.** If \(P=Q\), no insertion is needed. Otherwise suppose \(P=\{a,b\}\), \(Q=\{a,c\}\), where \(a,b,c\) are distinct. Put \(r=b-a\pmod n\) and \(s=c-a\pmod n\), in \(\{1,\ldots,n-1\}\). Matching the shared \(a\) to itself would force distinct points \(b,c\) to have the same circular position, which is impossible. The only remaining orientation equates the clockwise arcs \(a\to b\) and \(c\to a\). Their exclusive edge sets are nonempty, and the difference in their baseline lengths is \(r-(n-s)=r+s-n\). Therefore

\[
\boxed{\eta(u,v)=|r+s-n|\qquad(|P\cap Q|=1).}
\]

Because \(r,s\) are distinct elements of \(\{1,\ldots,n-1\}\), their sum lies between \(3\) and \(2n-3\), and hence the cost is at most \(n-3\). For \(n\ge4\), equality holds exactly when \(\{r,s\}=\{1,2\}\) or \(\{n-2,n-1\}\).

**4. Disjoint supports.** List the four one-positions around the circle as \(x_0,x_1,x_2,x_3\). Their four clockwise interpoint distances \(\alpha,\beta,\gamma,\delta\) are positive integers summing to \(n\). Up to a cyclic relabeling and exchange of the two words, the membership pattern is either grouped \(P,P,Q,Q\) or alternating \(P,Q,P,Q\). In the grouped case, choose the direct arcs between the two consecutive \(P\) positions and between the two consecutive \(Q\) positions; their exclusive sets are gaps of sizes \(\alpha\) and \(\gamma\). In the alternating case, choose the arcs from the first to second \(P\) and from the first to second \(Q\); these overlap in their middle gap, leaving exclusive sets of sizes \(\alpha\) and \(\gamma\). The corresponding orientation therefore has insertion cost

\[
|\alpha-\gamma|\le \alpha+\gamma-2\le n-4.
\]

This is a constructive bound; the exact cost for either membership pattern is already given by the two-orientation formula from Step 2. In particular, no disjoint-support pair can attain \(n-3\).

**5. Sharpness and counting.** For \(n\ge4\), choose any shared position \(a\). There are two distinct choices for the unordered pair of other positions, \(\{a+1,a+2\}\) and \(\{a-1,a-2\}\) modulo \(n\), and two assignments of these positions to \(u\) and \(v\). Step 3 shows that each has cost \(n-3\), while Steps 3 and 4 rule out all other extremizers. The common position is uniquely determined, so these choices count each ordered pair exactly once, giving \(n\cdot2\cdot2=4n\). For \(n=3\), every two-one word is a rotation of every other such word, so the optimum is zero; the case \(n=2\) is immediate.

## Verification

The standalone script `VERIFY.py` implements (i) the oriented cyclic-arc formula, (ii) separate endpoint case formulas, (iii) an explicit optimal one-gap construction, and (iv) an independent brute-force enumeration of all allocations of up to the claimed optimal padding. Run with `python3 VERIFY.py` from the directory containing the script. No external libraries or network access are required.

The recorded run checked \(93{,}992\) ordered pairs through length \(18\) against both formulas and the constructed padded words; all \(1{,}595\) ordered pairs through length \(8\) against independent exhaustive insertion allocations; and \(10{,}000\) larger random pairs through length \(199\). The finite runs corroborate the theorem; its all-length proof is Steps 1--5 above.

## Relationship to prior work

Thongjarast (2026, arXiv:2607.18452, first public July 20) proved existence of simultaneous **zero-only** padding for two same-weight binary words. Its Theorem 12 gives a polynomial output-length bound, and Section 10.1 explicitly asks for the exact minimum length. That primary text was inspected in detail. The result here answers the question for the complete natural weight-two stratum, with an optimal algorithm and exact extremizer count; it does not answer the general-weight problem.

Shinagawa and Nuida (2025, arXiv:2507.04916) proved the original binary equalizability criterion allowing unrestricted common insertions; Thongjarast, Pasiphol, and Ruangwises (2026, arXiv:2604.19504) extended the criterion to arbitrary alphabets using unrestricted inserted letters. Neither existence criterion logically determines the zero-only optimum. The latter two papers were compared using available abstracts and public research descriptions rather than complete primary texts; that access limitation remains a priority risk.

## Limitations

The theorem treats exactly two ones per binary input word. It does not determine the worst-case minimum insertion cost when the weight grows with \(n\), nor does it resolve the general polynomial-bound question. It classifies optimal **costs**, and the \(4n\) worst ordered pairs, not all distinct padding patterns for a given input. An earlier unindexed quantitative result is possible. The mathematical review is not independent external validation.

## References

1. Sarunyu Thongjarast, *0-Cyclic Equalizability of Binary Words Characterized by Hamming Weight*, arXiv:2607.18452 (first posted July 20, 2026), https://arxiv.org/abs/2607.18452 ; openly readable text https://academ.us/article/2607.18452/ .
2. Sarunyu Thongjarast, Sarit Pasiphol, Suthee Ruangwises, *Cyclic Equalizability Characterized by Parikh Vectors*, arXiv:2604.19504 (first posted April 21, 2026), https://arxiv.org/abs/2604.19504 .
3. Kazumasa Shinagawa and Koji Nuida, *Cyclic Equalizability of Words and Its Application to Card-Based Cryptography*, arXiv:2507.04916 (first posted July 7, 2025), https://arxiv.org/abs/2507.04916 .
