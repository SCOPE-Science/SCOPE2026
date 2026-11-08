# Exact enumeration of binary universal cycles for two-block set partitions

## Finding

For each integer \(n\ge3\), let \(\mathcal P(n,2)\) be the set of partitions of \(\{1,\ldots,n\}\) into exactly two nonempty, unlabeled blocks. Represent a partition by a binary word of length \(n\), identifying a word with its global bit complement. A **binary universal cycle** is a circular binary word of length \(L_n=2^{n-1}-1\) whose cyclic windows of length \(n\) represent every member of \(\mathcal P(n,2)\) exactly once. Rotation, but not reversal, preserves the orientation of a circular word.

**Theorem.** Binary universal cycles for \(\mathcal P(n,2)\), modulo rotation and global bit complementation, are in a canonical bijection with ordinary binary de Bruijn cycles of order \(n-1\), modulo rotation. Consequently their exact number is

\[
U_n=2^{\,2^{n-2}-n+1}\qquad(n\ge3).
\]

There are exactly \(2U_n\) such cycles modulo rotation alone and exactly \(2L_nU_n\) indexed binary circular words (with a distinguished starting position). The first values of \(U_n\), for \(n=3,4,5,6,7\), are \(1,2,16,2048,67108864\).

## Assumptions and scope

All binary words are over the **fixed two-symbol alphabet** \(\{0,1\}\). A circular word of length \(L\) is a function on \(\mathbb Z/L\mathbb Z\); its length-\(r\) window at index \(i\) is \(w_iw_{i+1}\cdots w_{i+r-1}\) with indices modulo \(L\). A global exchange \(0\leftrightarrow1\) does not change the set partitions, whereas local symbol renaming between different windows is **not** permitted. The count distinguishes reversal unless reversal happens to be achieved by the stated allowed symmetries. It does not count representations over alphabets with more than two global symbols.

For an integer \(m\ge2\), a binary de Bruijn cycle of order \(m\) is a circular word of length \(2^m\) containing every binary length-\(m\) word exactly once as a cyclic window. No special treatment of a root is implicit in the phrase “modulo rotation.”

## Proof

**Step 1 (adjacent differences encode bipartitions).** Put \(m=n-1\). Define the cyclic difference word \(d_i=w_i\oplus w_{i+1}\), where \(\oplus\) denotes addition modulo two. The \(m\) adjacent differences of a binary \(n\)-window determine that window up to a **single global complement**: choose its initial bit and then reconstruct each successor bit. All differences are zero exactly when the window is constant. Thus the \(2^{n-1}-1=2^m-1\) two-block partitions are in bijection with all nonzero binary \(m\)-words. The circular word \(w\) is universal exactly when its circular difference word \(d\) has each nonzero length-\(m\) word exactly once among its cyclic windows.

**Step 2 (every admissible difference word integrates).** Such a word \(d\) has exactly \(2^{m-1}\) ones: the first bits of its \(2^m-1\) windows include precisely the \(2^{m-1}\) nonzero \(m\)-words beginning with one. Since \(m\ge2\), this number is even. Consequently \(\bigoplus_{i=0}^{L_n-1}d_i=0\), which is precisely the consistency condition for a cyclic binary antiderivative \(w\). Choosing \(w_0\in\{0,1\}\) determines all of \(w\), yielding exactly two complementary antiderivatives. This construction respects rotation and is invertible modulo global complementation.

**Step 3 (insert precisely the missing zero loop).** Let \(B_m\) denote the directed binary overlap graph with vertices the length-\((m-1)\) words and one edge labeled by each binary \(m\)-word, from its \((m-1)\)-prefix to its \((m-1)\)-suffix. A cyclic difference word \(d\) with exactly the nonzero \(m\)-windows is an Eulerian circuit of the graph \(B_m\) after deleting its edge \(0^m\), a self-loop at vertex \(0^{m-1}\). In the deleted-loop graph the zero vertex has indegree and outdegree one; it is therefore visited exactly once per cyclic Euler tour. Insert the missing self-loop at that visit. This gives an Eulerian circuit of the entire graph \(B_m\), equivalently a binary de Bruijn cycle of order \(m\). Conversely, remove the uniquely occurring zero self-loop from any such Euler circuit. These two operations are inverse and commute with rotation, so they constitute the claimed canonical bijection.

**Step 4 (derive the exact count).** Write \(N=2^{m-1}\), and let \(A\) be the adjacency matrix of \(B_m\). Each vertex has indegree and outdegree two, including multiplicities. Every prescribed destination can be reached in exactly one directed walk of length \(m-1\), by appending its \(m-1\) bits. Hence \(A^{m-1}=J\), the all-ones matrix. The eigenvalues of \(A\), with algebraic multiplicities, are \(2\) once and \(0\) a total of \(N-1\) times. Thus the directed Laplacian \(2I-A\) has nonzero eigenvalues all equal to \(2\). Since the graph is Eulerian, the directed matrix-tree theorem yields the same number \(t\) of spanning in-arborescences at every root, with \(Nt=2^{N-1}\). Therefore \(t=2^{N-1}/N=2^{2^{m-1}-m}\).

Fixing the unique edge labeled \(0^m\) as the starting edge of a directed Euler tour removes rotation ambiguity. The directed BEST theorem counts tours with that distinguished start edge by \(t\prod_v(\deg^+(v)-1)!=t\), as every outdegree is two. Thus binary de Bruijn cycles of order \(m\) number \(2^{2^{m-1}-m}\), and substituting \(m=n-1\) proves the formula.

Finally, each difference word has full period \(L_n\): a shorter period would repeat some length-\(m\) window. Therefore no nonidentity rotation fixes an admissible word \(w\). Nor can a rotation carry \(w\) to its complement, since then the same rotation fixes \(d\) and must be the identity, which cannot complement \(w\). Hence the two complementary choices remain distinct modulo rotation alone, and every orbit under rotations and complementation has size \(2L_n\), giving the other two counts. \(\square\)

## Verification

Two standalone standard-library Python programs accompany this text. Execute `python3 verify_binary_ucycles.py` to exhaustively generate all \(2^{L_n}\) indexed circular binary words for \(n=3,4,5\), check the partition-window condition directly, test the difference-word characterization, and count orbits under rotation and complementation. The verified pairs (indexed words, rotation-plus-complement orbits) are \((6,1)\), \((28,2)\), and \((480,16)\).

Execute `python3 verify_tree_counts.py` to compute by exact Bareiss integer elimination the directed reduced-Laplacian determinants of the deleted-zero-loop overlap graphs, for difference-window orders \(m=2,3,4,5,6\). The counts are \(1,2,16,2048,67108864\). The two implementations test distinct portions of the proof. These finite checks do not substitute for the all-order graph and parity arguments.

## Relationship to prior work

Higgins, Kelley, Sieben, and Godbole proved that every Eulerian cycle of their two-block partition transition graph lifts to a universal cycle, and thereby established existence for the whole family; their full Section 3 and Theorem 12 do not state this all-order exact cycle count or the derivative/de Bruijn bijection. Chung, Diaconis, and Graham introduced the general set-partition universal-cycle framework. The exact de Bruijn sequence count and its directed matrix-tree/BEST derivation are classical and are explicitly used here, not claimed as novel. OEIS A016031 already records the numerical values as the numbers of binary de Bruijn cycles; the asserted connection to the two-block partition family, rather than novelty of the integer sequence, is the subject of this result.

The comparison is at the level of statements: known existence of two-block partition universal cycles does not itself specify their multiplicity; known enumeration of de Bruijn cycles does not by itself identify that multiplicity without the adjacent-difference and zero-loop bijections. The related 2011 work on restricted-word universal cycles establishes existence for different represented sets. Historical priority of this particular explicit correspondence is not independently certified; an unindexed earlier formulation remains possible.

## Limitations

The theorem applies to exactly two nonempty blocks, globally binary encodings, circular windows, and equivalence under rotation with or without global bit complement as specified. It does not enumerate representations using an enlarged alphabet, identify reversals, or supply a corresponding formula for three or more blocks. The number sequence is classical in its de Bruijn interpretation, and the count is not an independent new enumeration of de Bruijn cycles. No independent external audit has been performed.

## References

1. Z. Higgins, E. Kelley, B. Sieben, and A. Godbole, *Universal and Near-Universal Cycles of Set Partitions*, Electronic Journal of Combinatorics 22(4), P4.48 (2015). First public preprint: February 13, 2015, https://arxiv.org/abs/1502.04076 ; journal full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i4p48/pdf/ .
2. F. Chung, P. Diaconis, and R. Graham, *Universal Cycles for Combinatorial Structures*, Discrete Mathematics 110 (1992), 43–59, https://doi.org/10.1016/0012-365X(92)90699-G .
3. N. G. de Bruijn, *A Combinatorial Problem*, Indagationes Mathematicae 8 (1946), 461–467; earlier priority acknowledged to C. Flye Sainte-Marie (1894). The count is documented in OEIS A016031: https://oeis.org/A016031 .
4. *De Bruijn Sequence and Universal Cycle Constructions*, graph and counting overview, https://debruijnsequence.org/db/graph .
