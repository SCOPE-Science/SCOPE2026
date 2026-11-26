# Exact three-level Burrows–Wheeler run spectrum of binary weight-three words

## Finding
For an integer \(n\ge4\), consider all binary words \(w\) of length \(n\) having exactly three ones. Form the cyclic-rotation Burrows–Wheeler last column \(B(w)\): arrange the \(n\) rotations of \(w\) lexicographically using \(0<1\), then read their final symbols in order. Let \(\rho(w)\) be the number of nonempty maximal constant-symbol blocks in \(B(w)\), and let \(R_r(n)=\#\{w: \rho(w)=r\}\). The complete spectrum is
\[
(R_2(n),R_4(n),R_6(n))=
\begin{cases}
\big(n/3,\ n(n-3),\ n(n-3)(n-6)/6\big),&3\mid n,\\
\big(n,\ n(n-4),\ n(n-4)(n-5)/6\big),&3\nmid n.
\end{cases}
\]
Every other run count has multiplicity zero. In particular, \(R_6(n)/\binom n3\to1\). All words, not merely distinct necklaces, are counted; the three choices of one-position support determine a word, and ties between equal rotations do not alter the last column.

There is also a complete structural criterion. Write a circular word with three ones by its cyclically ordered triple of nonnegative intervening zero-gap lengths \((g_0,g_1,g_2)\), whose sum is \(n-3\). Three equal gaps, or three gaps with exactly two equal and remaining gap differing by one, give two BWT runs. Exactly two equal gaps with difference at least two give four BWT runs. For three distinct gaps \(x<y<z\), choose the rotation beginning at the smallest gap: the orientation \((x,y,z)\) gives six runs exactly if \(z-y\ge2\); the reverse orientation \((x,z,y)\) gives six runs exactly if \(y-x\ge2\). Otherwise those distinct-gap orientations give four runs.

## Assumptions and scope
The transform is the original cyclic-rotation BWT, **without a unique end-marker**. Its output is a binary word, and its **linear**, not circular, maximal-run count is measured. The input alphabet is \(\{0,1\}\), with \(0<1\). The input has exactly three ones and at least one zero (\(n\ge4\)). The input is counted as a labeled length-\(n\) word, so its circular rotations are different inputs unless the words are identical. Equal rows of the BWT matrix have identical preceding symbols; ordering ties cannot change \(B(w)\). The all-one word of length three is excluded, since it has only one BWT run.

## Proof
**1. Sorting the rotation matrix.** Fix a gap triple \(g=(g_0,g_1,g_2)\) with cyclic subscripts modulo three. Index a rotation by the gap \(g_j\) immediately preceding its first one, and let \(\ell\) be the number of zeros remaining in that gap before this one. For \(1\le\ell\le g_j\), the rotation begins \(0^\ell1\); for \(\ell=0\), it starts at the one immediately following gap \(g_j\). It is preceded by a one precisely when \(\ell=g_j\), including the case \(\ell=g_j=0\).

For different \(\ell\), rotations sort in decreasing order of \(\ell\) (more initial zeros sorts first). For fixed \(\ell\), they sort by the **descending lexicographic order** of the cyclic gap-following triples
\[
(g_{j+1},g_{j+2},g_j).
\]
Indeed after their common initial \(0^\ell1\) (or initial one for \(\ell=0\)), a larger next zero gap forces an earlier lexicographic rotation; ties are resolved by successive gaps. Equal triples yield identical rotations and equal preceding symbols. Consequently the BWT column is obtained, for \(\ell=\max g_j,\ldots,0\), by listing all \(j\) with \(g_j\ge\ell\) in that descending order and outputting a one if and only if \(g_j=\ell\). This finite, exact sorting rule applies even when gaps are zero or repeated.

For any word containing both symbols, the lexicographically first cyclic rotation begins at the start of a maximal zero run, so its preceding letter is one. The last rotation begins at the start of a maximal one run, so its preceding letter is zero. Thus \(B(w)\) begins with one and ends with zero. It contains exactly three ones, so its linear run count is twice its number of one-blocks, hence belongs to \(\{2,4,6\}\).

**2. Detecting adjacent marked rows.** The preceding sorting rule leaves exactly three marked one-rows, one for each gap. For distinct gaps \(x<y<z\), marked rows arising from nonconsecutive gap lengths are separated by at least one zero-row. If \(z=y+1\), inspect the block with \(\ell=y\), which contains two rows (from the gaps \(y,z\)). In orientation \((x,y,z)\), the marked \(y\)-row has next gap \(z\), while the unmarked \(z\)-row has next gap \(x\); hence the marked row is first and adjoins the unique marked row of the immediately preceding \(\ell=z\) block. In orientation \((x,z,y)\), it is last, and the two marked rows are separated by a zero. Similarly, if \(y=x+1\), the marked \(y\)-row adjoins the marked \(x\)-row only in orientation \((x,z,y)\): the \(\ell=y\) group ends with its marked row and the next \(\ell=x\) group starts with its marked row. The opposite orientation has an intervening zero. These comparisons also cover \(x=0\), using the explicit \(\ell=0\) group. No other pair of marked rows can touch. Therefore orientation \((x,y,z)\) has six runs exactly when \(z-y\ge2\), and orientation \((x,z,y)\) has six runs exactly when \(y-x\ge2\); otherwise it has four.

For exactly two equal gaps, the two corresponding marked rows are consecutive under the same descending-triple order. Their pair adjoins the remaining marked row exactly when the distinct gap differs by one; if the difference is at least two, the intervening \(\ell\) group contains a zero-row. (If the repeated gaps are the larger ones, they form the first marked pair; if the repeated gaps are the smaller ones, they form the later marked pair. In either case, the tie between their next-gap values is broken in favor of the marked row.) Three equal gaps give three consecutive marked rows. This proves every case in the stated structural criterion.

**3. Counting circular classes and labeled words.** Every distinct-gap multiset \(x<y<z\) has exactly two cyclic orientations, each with \(n\) distinct length-\(n\) rotations. Set \(d_1=y-x\ge1\), \(d_2=z-y\ge1\). The sum of gaps is
\[
3x+2d_1+d_2=n-3.
\]
By Step 2, the number of six-run orientations within this multiset is \(\mathbf1_{d_1\ge2}+\mathbf1_{d_2\ge2}\). The ordinary generating series marking the gap sum for the number of six-run necklaces is
\[
\sum_{x\ge0}\sum_{d_1,d_2\ge1}
\big(\mathbf1_{d_1\ge2}+\mathbf1_{d_2\ge2}\big)
 z^{3x+2d_1+d_2}
 =\frac{z^4+z^5}{(1-z^3)(1-z^2)(1-z)}
 =\frac{z^4}{(1-z^3)(1-z)^2}.
\]
Thus
\[
R_6(n)=n\sum_{j=0}^{\lfloor(n-7)/3\rfloor}(n-6-3j),
\]
interpreting the sum as empty for \(n<7\). Evaluating this arithmetic progression gives \(n(n-3)(n-6)/6\) if \(3\mid n\), and \(n(n-4)(n-5)/6\) otherwise.

For two BWT runs, the only possibilities are three equal gaps, which occur exactly when \(3\mid n\), giving a periodic necklace with \(n/3\) distinct labeled rotations; or a multiset of two equal gaps and a neighboring integer, which occurs exactly once when \(3\nmid n\), giving \(n\) labeled rotations. Hence the stated \(R_2(n)\) follows. Finally, \(R_2(n)+R_4(n)+R_6(n)=\binom n3\), so subtraction gives the stated \(R_4(n)\). In either congruence class, \(R_4(n)=O(n^2)\) and \(R_2(n)=O(n)\) against \(\binom n3=\Theta(n^3)\), proving the asserted limit.

## Verification
The included standalone `verify.py` uses only the Python 3 standard library. It computes the BWT directly from all sorted cyclic rotations and independently by the zero-gap row-order rule, compares their entire output strings, checks the cyclic-gap run classification and the exact census on every length-four-through-length-22 word with three ones (8,854 input words), and also checks the gap criterion on 8,435 ordered triples with total gap sum from one through 35. Execute `python verify.py`; the expected final line begins `ALL_CHECKS_PASS`. The mathematical proof, not this finite test, establishes all lengths.

## Relationship to prior work
Burrows and Wheeler introduced the cyclic-rotation transformation in 1994. Mantaci, Restivo, Rosone, Sciortino, and Versari (2017) analyzed BWT clustering measured by equal-letter runs and proved general upper bounds, with examples on de Bruijn words; their sections 2–5 do not give an exact three-one input distribution or the two/four/six census. Mantaci, Restivo, Rosone, Russo, and Sciortino (2017) explicitly treated binary inputs containing three ones in the different **fixed-point** problem. Their Proposition 4.2 characterizes when the entire BWT output equals the input; equality is neither required nor implied here, and it does not tabulate the three possible BWT run counts. The classical perfect-clustering characterization covers the two-run portion but not the full distribution. The new contribution is the complete cyclic-gap criterion and all-length labeled-word three-level spectrum, not a restatement of the general run bound or a fixed-point criterion.

## Limitations
The formulas concern the original cyclic-rotation transform without a terminator and exactly three ones. They are not claims about the sentinel-based BWT, other alphabet orders, general weights, actual compression bit rates, or probabilistic source models beyond the stated uniform fixed-weight census. Earlier equivalent specialized enumerations may exist outside the inspected literature. No external independent audit or priority certification has been performed.

## References
1. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, Digital Equipment Corporation SRC Research Report 124, May 10, 1994.
2. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino, L. Versari, *Measuring the clustering effect of BWT via RLE*, Theoretical Computer Science 698 (2017), 79–87, DOI:10.1016/j.tcs.2017.07.015. Open postprint: https://arpi.unipi.it/retrieve/e0d6c92f-b120-fcf8-e053-d805fe0aa794/MRRSV_TCS2017.pdf
3. S. Mantaci, A. Restivo, G. Rosone, F. Russo, M. Sciortino, *On Fixed Points of the Burrows-Wheeler Transform*, Fundamenta Informaticae 154 (2017), 277–288, DOI:10.3233/FI-2017-1566. Open postprint: https://iris.unipa.it/retrieve/e3ad8925-ffc2-da0e-e053-3705fe0a2b96/FI_2017_postprint.pdf
