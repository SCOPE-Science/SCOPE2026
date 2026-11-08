# The first sparse Garden-of-Eden layer of cyclic Rule 22

## Finding
Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be elementary cellular automaton Rule 22 with indexed periodic boundary conditions, defined for \(n\ge3\) by
\[
(F_n(x))_i=1\quad\Longleftrightarrow\quad x_{i-1}+x_i+x_{i+1}=1,
\]
where indices are taken modulo \(n\) and the sum is over ordinary integers. An output is *unreachable* if its inverse image under \(F_n\) is empty. Distinct cyclic shifts count as distinct indexed outputs.

**Theorem.** For every \(n\ge5\), every output with Hamming weight zero, one, or two has a predecessor. For every \(n\ge10\), a weight-three output is unreachable **if and only if** the three positive distances between its consecutive ones in the fixed forward cyclic orientation, considered up to cyclic rotation but not reversal, belong to
\[
(2,3,n-5),\qquad (2,n-5,3),\qquad (3,3,n-6).
\]
Consequently, there are exactly \(3n\) unreachable indexed outputs of weight three for every \(n\ge10\). The threshold is sharp: the counts for \(n=5,6,7,8,9\) are respectively \(5,12,14,16,21\), so \(3n\) fails at \(n=9\).

In particular, among output Hamming weights, three is the first at which a periodic Rule 22 state can be unreachable for any \(n\ge5\).

## Assumptions and scope
All words are binary; the ring is labeled, synchronous, and has one update. Both source and target use the same length and periodic boundary conditions. The result concerns *existence* of at least one predecessor; it does not count the number of predecessors. A gap is a positive clockwise index distance from one target one to the next, so the three gaps sum to \(n\); this is not the number of zeros between ones (which is one less than the gap). A Garden-of-Eden state here means a finite-ring state with no length-\(n\) periodic predecessor, not a finite forbidden block with free boundary conditions or a state that has no ancestor at any number of steps.

## Proof
**1. A four-state exact predecessor test.** Index the four overlapping source-pair states by \(00,01,10,11\). When a triple \(abc\) produces output \(s\), connect state \(ab\) to state \(bc\) by an edge labeled \(s\). The two Boolean adjacency matrices, with row and column order as just stated, are
\[
B_0=\begin{pmatrix}1&0&0&0\\0&0&0&1\\0&1&0&0\\0&0&1&1\end{pmatrix},\qquad
B_1=\begin{pmatrix}0&1&0&0\\0&0&1&0\\1&0&0&0\\0&0&0&0\end{pmatrix}.
\]
Use Boolean matrix multiplication, where sums are logical OR and products are logical AND. A source word of length \(n\) mapping to target \(y\) determines a closed walk of length \(n\) with edge labels \(y_0,\ldots,y_{n-1}\), and every such closed walk conversely determines a periodic predecessor. Hence \(y\) is reachable exactly when \(B_{y_0}\cdots B_{y_{n-1}}\) has a nonzero diagonal entry.

Direct Boolean multiplication yields
\[
B_0^4=B_0^5=\begin{pmatrix}1&0&0&0\\0&1&1&1\\0&1&1&1\\0&1&1&1\end{pmatrix}.
\]
Multiplying again shows that \(B_0^k=B_0^4\) for every \(k\ge4\). Thus each positive inter-one gap \(d\) can be replaced, without affecting reachability, by \(\min(d,5)\). For target gap vector \((d_1,\ldots,d_r)\), the exact test is whether
\[
\operatorname{diag}\bigl(B_1B_0^{d_1-1}\cdots B_1B_0^{d_r-1}\bigr)
\]
has a nonzero entry. The zero-weight target is reachable from the zero source.

**2. Weights one and two.** At weight one the only gap is \(n\); the capped test fails only for gap lengths \(1,3,4\), so succeeds for \(n\ge5\). At weight two, the exhaustive capped test fails only for ordered pairs \((1,1),(1,2),(2,1)\). Each of these has actual total length at most three, so none occurs at \(n\ge5\). These are exact finite Boolean-matrix consequences, not deductions from an experimental length cutoff.

**3. Complete weight-three certificate.** Let \(a,b,c\in\{1,2,3,4,5\}\) be capped gap lengths. The following table lists, for every pair \((a,b)\), the *complete set* of values of \(c\) for which \(B_1B_0^{a-1}B_1B_0^{b-1}B_1B_0^{c-1}\) has zero diagonal. A dash denotes an empty set. Each of the 125 cases follows by multiplying the displayed four-state matrices; the standalone verifier recomputes the table from the local rule, not from a stored list of outputs.

| \(a\) / \(b\) | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | – | 2,3 | 2,3 | – | – |
| 2 | 2,3 | 1,3,4 | 1,2,3,4,5 | 2,3 | 3 |
| 3 | 2,3 | 1,2,3,4,5 | 1,2,3,4,5 | 2,3 | 2,3 |
| 4 | – | 2,3 | 2,3 | – | – |
| 5 | – | 3 | 2,3 | – | – |

Up to cyclic permutation of the three entries (and *not* reflection), the forbidden capped triples are exactly
\[
\begin{gathered}
(1,2,2),(1,2,3),(1,3,2),(1,3,3),\\
(2,2,3),(2,2,4),(2,3,3),(2,3,4),\\
(2,3,5),(2,4,3),(2,5,3),\\
(3,3,3),(3,3,4),(3,3,5).
\end{gathered}
\]
If the actual three positive gaps sum to \(n\ge10\), only the three capped families \((2,3,5),(2,5,3),(3,3,4\text{ or }5)\) can occur, exactly yielding the three families in the theorem. The stated small-length counts come from the same finite list with \(n=5,\ldots,9\).

**4. Indexed count and sharp cutoff.** Each of the three listed gap types for \(n\ge10\) has an orbit of exactly \(n\) distinct indexed output words under rotation, and the orbits are disjoint: the two triples with entries \(2,3,n-5\) are opposite oriented cyclic orders, while the third has two entries equal to three. Therefore the exact count is \(3n\). For \(n=9\) the analogous equal-gap type \((3,3,3)\) instead has a three-word rotational orbit, yielding a different total, \(21\). This proves the claimed sharp threshold and completes the proof.

## Verification
Run `python3 verify_rule22.py` with Python 3 and no dependencies. The script reconstructs both Boolean matrices from the eight possible source neighborhoods; proves the stabilization identity by Boolean multiplication; verifies the complete 125-case table, the one- and two-gap tests, and the three-family characterization for lengths \(10\) through \(60\). Independently, it evaluates Rule 22 on all \(262136\) binary source words of lengths \(3\) through \(17\) and compares reachable outputs of Hamming weight at most three against the transfer-matrix test. The completed run printed `VERIFY_OK capped_cases=125 ring_lengths=5..60 gap_cases=34136 direct_inputs=262136`. The proof for unbounded \(n\) uses matrix stabilization and the finite table, not finite extrapolation.

## Relationship to prior work
Gravner and Griffeath's 2010 study of the Exactly 1 cellular automaton investigates finite seeds, replication, periodicity and entropy, and exhibits an orphan block (`10101001`). Martínez and collaborators' later study of Rule 22 supplies de Bruijn and subset diagrams and lists Garden-of-Eden expressions, including the short word `10110`. Thus examples of short forbidden configurations were known. These support the general finite-automaton approach but do not give the complete low-weight *periodic-ring image* classification for all lengths, its sharp stable cutoff, or the \(3n\) indexed count. The distinction between an infinite-line forbidden block and a periodic-ring output is essential. General image-testing procedures are not by themselves an enumeration of the three constrained gap orbits. No claim of independent historical priority or independent validation is made.

## Limitations
Only one synchronous step of elementary Rule 22 is considered. The count is for indexed rings, not rotation classes of outputs, and does not describe weights four or higher, predecessor multiplicities, or the image size without a weight restriction. The known de Bruijn/subset machinery may make parts of the analysis accessible by other routes, and an unindexed equivalent classification cannot be ruled out. The finite table and standalone code are supplied to make the exact case reduction independently reproducible; no external mathematical audit has been conducted.

## References
1. J. Gravner and D. Griffeath, *The One-Dimensional Exactly 1 Cellular Automaton: Replication, Periodicity, and Chaos from Finite Seeds*, Journal of Statistical Physics **142** (2011), 168–200. First published online 2010-12-10. DOI: https://doi.org/10.1007/s10955-010-0103-9 . Open-access full text: https://link.springer.com/content/pdf/10.1007/s10955-010-0103-9.pdf .
2. G. J. Martínez, A. Adamatzky, R. Hoffmann, D. Désérable and I. Zelinka, *On Patterns and Dynamics of Rule 22 Cellular Automaton*, Complex Systems **28** (2019), 125–174. https://doi.org/10.25088/ComplexSystems.28.2.125 ; open preprint https://arxiv.org/abs/2005.01480 .
3. M. Schuele and R. Stoop, *A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata*, arXiv:1107.2080 (first submitted 2011-07-11). https://arxiv.org/abs/1107.2080 .
