# Exact run spectrum of the circular Burrows–Wheeler transform for binary words with three ones

## Finding

Let \(n\ge4\). For a binary word \(w\in\{0,1\}^n\), form its **circular Burrows–Wheeler transform** \(B(w)\): sort all \(n\) cyclic rotations of \(w\) lexicographically with \(0<1\), retaining multiplicity, and concatenate their last characters. Let \(r(w)\) be the number of maximal constant-letter blocks (*linear runs*) of \(B(w)\). For each \(j\), write \(N_j(n)=|\{w:|w|=n,\ |w|_1=3,\ r(w)=j\}|\), where positions are indexed, so rotations of a word are counted as separate inputs when distinct.

**Theorem.** The support of this conditional run distribution is contained in \(\{2,4,6\}\), and the complete distribution for every \(n\ge4\) is

\[
\begin{array}{c|ccc}
 &N_2(n)&N_4(n)&N_6(n)\\\hline
3\mid n&n/3&n(n-3)&n(n-3)(n-6)/6\\
3\nmid n&n&n(n-4)&n(n-4)(n-5)/6.
\end{array}
\]

In particular, for uniformly sampled \(W_n\) conditioned to have three ones,
\[
\Pr\{r(W_n)=6\}=1-\frac6n+O(n^{-2}).
\]
The formulas include zero-size classes for small admissible lengths. They concern the **circular** transform without an appended terminal symbol; the common suffix-array transform with a unique end marker is a different statistic.

## Assumptions and scope

The binary alphabet has fixed order \(0<1\); length \(n\) is an integer at least four. Every word has exactly three occurrences of \(1\), hence at least one \(0\). The circular BWT is a multiset-based sort of all rotations, including repeated rotations of periodic words. Linear runs are counted without identifying the first and last positions of the output. A word and its rotations need not be distinct, but all distinct **indexed words** of length \(n\) are separate sample points.

Write a representative of the circular word starting at one of its three ones as
\[
1\,0^a\,1\,0^b\,1\,0^c,\qquad a,b,c\in\mathbb Z_{\ge0},\quad a+b+c=s=n-3\ge1.
\]
The ordered triple \((a,b,c)\) is a **rooted gap triple**. The theorem counts indexed words, not gap triples or necklaces.

## Proof

**Step 1: a three-gap reconstruction of the BWT.** Label the cyclic zero gaps \(g_0,g_1,g_2\), indexed modulo three. Each gap contributes one rotation for each integer \(t\) satisfying \(0\le t\le g_i\): the rotation begins with \(t\) zeros followed by the next \(1\); the choice \(t=0\) begins with that \(1\). Its BWT last character is \(1\) if and only if \(t=g_i\). If \(t>0\), the rotation begins inside the zero gap; if \(t=0=g_i\), it begins at a one whose predecessor is also a one, so the same criterion holds.

Rotations with larger \(t\) sort first, since \(0^t1\) precedes \(0^{t'}1\) when \(t>t'\). For equal \(t\), they are sorted by the cyclic pair \((g_{i+1},g_{i+2})\) in **decreasing lexicographic order**, since the corresponding next blocks after their common prefix are zeros. If these pairs tie, the entire cyclic triples (and therefore the rotations) tie; their BWT last characters agree. Thus the following specification reconstructs \(B(w)\) exactly, also in the periodic case:

For \(t\) descending from \(\max(g_i)\) to zero, take all \(i\) with \(g_i\ge t\), ordered by decreasing \((g_{i+1},g_{i+2})\), and append \(1\) exactly when \(g_i=t\), otherwise \(0\). (A directly executable implementation is in `verify.py`.)

Because the word contains both letters, the lexicographically smallest rotation begins at the longest zero run and is preceded by a one, and the largest rotation begins at the longest one run and is preceded by a zero. Hence \(B(w)\) starts with \(1\) and ends with \(0\). It has precisely three ones. Its number of linear runs is therefore twice the number of groups of consecutive ones, and belongs to \(\{2,4,6\}\).

**Step 2: adjacency classification.** Let \(x\le y\le z\) be the sorted triple of gap lengths. Inspect the three BWT positions carrying a \(1\), using the row ordering from Step 1.

If \(z-x\le1\), those three positions are consecutive, so \(r=2\). If exactly two gaps coincide but the third differs by at least two, the equal-gap positions are adjacent, and the third is separated from them; hence \(r=4\).

Suppose \(x<y<z\). Two marked rows from different gap lengths can be adjacent only when their gap lengths differ by one: any intermediate \(t\)-level contains at least one row ending in zero. The possible consecutive pairs have an orientation condition. When \(y=x+1\), the \(x\)- and \(y\)-marked rows meet precisely for the three cyclic orders of \((x,z,y)\). Indeed the \(y\)-marked row must be last within its level, and the \(x\)-marked row first within its level, which is equivalent to the successor gap of \(x\) being \(z\). When \(z=y+1\), the \(y\)- and \(z\)-marked rows meet precisely for the three cyclic orders of \((x,y,z)\). For a triple of consecutive gap lengths, the two orientation conditions are disjoint and together cover all six arrangements: each produces exactly one adjacent marked pair. In all other distinct-gap orders no marked rows are adjacent. Thus \(r=4\) exactly in the described cases, and \(r=6\) otherwise. This classification also covers gaps of length zero.

**Step 3: counting rooted gap triples.** There are \(\binom{s+2}{2}\) nonnegative ordered triples with sum \(s\). Exactly \(b_s=1\) if \(3\mid s\), or \(b_s=3\) otherwise, have maximum minus minimum at most one. By Step 2 these are precisely the \(r=2\) triples.

For two equal gaps, write the pair as \(u,u\) and the other as \(s-2u\). There are \(\lfloor s/2\rfloor+1\) choices of \(u\), and exactly one has \(|s-3u|\le1\). Every remaining choice gives three ordered arrangements and \(r=4\). Their total contribution is \(3\lfloor s/2\rfloor\).

For three distinct gaps, each permitted adjacent consecutive pair contributes exactly three cyclic arrangements, with no double count. Let \(P_s\) be the number of triples \(x<y<z\) of sum \(s\) with \(y=x+1\), and \(Q_s\) the number with \(z=y+1\). Direct integer bounds give
\[
P_s=\left\lfloor\frac s3\right\rfloor,\qquad
Q_s=\left\lfloor\frac{s-1}{2}\right\rfloor-\left\lceil\frac s3\right\rceil+1.
\]
The latter expression is nonnegative for \(s\ge1\). Hence the \(r=4\) rooted gap count is
\[
a_s=3\left\lfloor\frac s2\right\rfloor+3(P_s+Q_s)
=\begin{cases}3s,&3\mid s,\\3s-3,&3\nmid s.\end{cases}
\]
The \(r=6\) rooted count is the remainder \(\binom{s+2}{2}-a_s-b_s\).

**Step 4: converting rooted gaps to indexed words.** For each rooted ordered gap triple and a chosen starting position among \(n\) positions, place the three ones and fill their gaps. This gives an indexed word together with a designated one. Conversely, every indexed word with three ones has exactly three choices of designated one. This argument holds even for periodic words, since the three *designated positions* remain distinct. Therefore the number of indexed words in any run class equals \(n/3\) times its rooted gap-triple count. Substitute \(s=n-3\) and simplify; divisibility by three is unchanged. The three formulas follow, and their sum is \(\binom n3\).

Finally, dividing \(N_6(n)\) by \(\binom n3\) yields \(1-6/n+O(n^{-2})\). This completes the proof.

## Verification

Run `python3 verify.py` with Python 3.9 or later. The script independently sorts all circular rotations and constructs the BWT from the gap ordering. It checks their entire transform strings and the gap-level case classification on all \(8{,}435\) rooted gap triples with \(1\le s\le35\). It independently enumerates all \(10{,}625\) indexed words with three ones at lengths \(4\) through \(23\), comparing exact run histograms with the formulas. Expected final line: `ALL_CHECKS_PASSED`. The infinite statement is proved above; these bounded checks do not replace the proof.

## Relationship to prior work

The two-run characterization itself is **not new**. Simpson and Puglisi (2008), revisiting a theorem of Mantaci and coauthors, identify binary words whose BWT has one run of each symbol with standard/Christoffel conjugates and powers. In the three-one population this explains the balanced-gap subfamily. Our theorem addresses a distinct question: the complete **finite-length frequency distribution** of the two-, four-, and six-run outcomes among all indexed weight-three words, with a gap-order characterization and exact expressions for the four- and six-run classes.

Later work on BWT-run sensitivity to reversal (Giuliani and colleagues, 2020) and on morphisms preserving or increasing BWT runs (Fici and colleagues, 2023) studies different operations and quantifiers. Those papers do not provide the stated fixed-composition population law. A search of accessible literature and mathematical finding records did not identify an equivalent enumeration; this is evidence of non-coverage by the checked material, not proof of global uniqueness.

## Limitations

The result uses the circular BWT (not the terminal-sentinel BWT), exactly three ones, and the binary order \(0<1\). It does not classify general weights, distinguish which nonconjugate words yield the same transform, or calculate analogous distributions for a bijective or extended BWT. Some unindexed or differently phrased literature may still contain an equivalent case. No independent mathematical audit has been performed.

## References

1. Jamie Simpson and Simon J. Puglisi, *Words with Simple Burrows–Wheeler Transforms*, Electronic Journal of Combinatorics **15** (2008), R83; published June 20, 2008, DOI: https://doi.org/10.37236/807 . Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r83/pdf .
2. Sara Giuliani, Shunsuke Inenaga, Zsuzsanna Lipták, Nicola Prezza, Marinella Sciortino, and Anna Toffanello, *Novel Results on the Number of Runs of the Burrows–Wheeler-Transform*, arXiv:2008.08506 (2020), https://arxiv.org/abs/2008.08506 .
3. Gabriele Fici, Giuseppe Romana, Marinella Sciortino, and Cristian Urbina, *On the Impact of Morphisms on BWT-Runs*, CPM 2023, https://doi.org/10.4230/LIPIcs.CPM.2023.10 .
