# Exact census of maximum total outer-independent coalition partitions of cycles

## Finding

For every integer \(n\ge3\), the maximum total outer-independent (TOI) coalition number of the labelled cycle \(C_n\) is known to be three. Denote by \(N_n\) the number of *unordered* partitions of its fixed vertex set into three nonempty blocks forming a TOI-coalition partition. The exact answer is
\[
N_n=\frac{a_n+b_n-f_n}{2}-2\mathbf1_{3\mid n},
\]
where the three integer sequences are uniquely specified by
\[
\begin{aligned}
(a_0,a_1,a_2,a_3)&=(4,1,3,10), &a_n&=a_{n-1}+a_{n-2}+2a_{n-3}+a_{n-4}\quad(n\ge4),\\
(b_0,b_1,b_2)&=(3,0,-2), &b_n&=-b_{n-2}+b_{n-3}\quad(n\ge3),\\
(f_0,f_1,f_2)&=(3,1,1), &f_n&=f_{n-1}+2f_{n-3}\quad(n\ge3).
\end{aligned}
\]
Exactly \(\mathbf1_{3\mid n}\) such partitions have a triangular coalition graph; all others have a three-vertex path as coalition graph. The first counts, for \(n=3,\ldots,12\), are \(1,6,10,25,63,130,280,615,1298,2731\). Moreover,
\[
N_n\sim\tfrac12\lambda^n,\qquad
\lambda=2.06599489201647\ldots,
\]
where \(\lambda\) is the largest positive root of \(x^4-x^3-x^2-2x-1\).

## Assumptions and scope

The labelled graph \(C_n\) has vertex set \(\mathbb Z/n\mathbb Z\) and edges joining consecutive residues, with \(n\ge3\). A total outer-independent dominating set (TOIDS) \(D\) totally dominates the graph (every vertex has a neighbor in \(D\)) and leaves an independent complement. A TOI-coalition is a pair of nonempty disjoint sets, neither individually TOIDS, whose union is TOIDS. A TOI-coalition partition is a partition into nonempty blocks, each having another block as its TOI-coalition partner. The coalition graph has a vertex for every block, and edges for partnerships. We count each partition once as an unordered family of subsets, without quotienting by graph automorphisms. The known maximum number of blocks is three (Buntina--Golmohammadi, Theorem 2, cycle case); this result counts all maximizers rather than reproving their scalar maximum.

A **cyclic distance-three packing** (abbreviated a \(2\)-packing) is a subset whose distinct vertices have graph distance at least three. Equivalently, no two selected positions are separated by one or two steps along the cycle (including wraparound).

## Proof

**1. Domination--packing equivalence.** For \(D\subseteq V(C_n)\), its complement \(P=V(C_n)\setminus D\) is independent exactly when no two vertices of \(P\) are adjacent. Total domination further requires that a vertex of \(D\) not have both neighbors in \(P\); in other words, no two elements of \(P\) can be separated by one intervening vertex. These two restrictions are precisely that \(P\) is a \(2\)-packing. Conversely, those two restrictions guarantee both properties of a TOIDS. The empty packing is permitted and corresponds to \(D=V(C_n)\). Every \(2\)-packing has size at most \(\lfloor n/3\rfloor\). Thus a \(2\)-packing itself can never be a TOIDS: its complementary set of at least \(n-\lfloor n/3\rfloor>\lfloor n/3\rfloor\) vertices cannot also be a \(2\)-packing.

**2. Coalition graphs.** For three blocks \(A,B,C\), the union \(A\cup B\) is a TOIDS exactly when the omitted block \(C\) is a \(2\)-packing. No block is itself a TOIDS in a coalition partition. The partnership graph has three vertices and no isolated vertex, so it is either a three-vertex path or a triangle. In a path, its two leaf blocks are \(2\)-packings, whereas their union is not a \(2\)-packing (otherwise the center would itself be a TOIDS). In a triangle all three blocks are \(2\)-packings. Conversely, a three-part partition with two \(2\)-packing blocks whose union is not a \(2\)-packing produces a valid path coalition graph, and a partition into three \(2\)-packings produces a triangle.

**3. Count two disjoint packing colors.** Consider cyclic words \(w_0\cdots w_{n-1}\) in \(\{0,1,2\}\) for which positions of color \(1\) separately form a \(2\)-packing and positions of color \(2\) separately form a \(2\)-packing. Introduce the seven admissible ordered-pair states
\[
\mathcal S=((0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)).
\]
Define a zero-one matrix \(T\) indexed by \(\mathcal S\), with a transition from \((u,v)\) to \((v,w)\) exactly when \(w=0\) or \(w\notin\{u,v\}\). Every cyclic admissible word corresponds bijectively to a length-\(n\) closed walk in this state graph, hence their number is \(t_n=\operatorname{tr}(T^n)\). Direct exact determinant computation gives
\[
\det(xI-T)=(x^3+x-1)(x^4-x^3-x^2-2x-1).
\]
By the Cayley--Hamilton theorem and the initial power sums, \(t_n=a_n+b_n\) with the stated initial values and recurrences.

**4. Subtract the forbidden central block.** Among the words just counted, those whose union of colors \(1\) and \(2\) is itself a \(2\)-packing are obtained by selecting a binary cyclic \(2\)-packing and choosing independently one of the two colors for each selected position. Their total number is
\[
f_n=\operatorname{tr}(U^n),
\]
where \(U\) has states \((0,0),(0,1),(1,0)\) and transition weight \(2^w\) from \((u,v)\) to \((v,w)\) whenever it is admissible as a binary \(2\)-packing. Exact computation gives \(\det(xI-U)=x^3-x^2-2\), producing the stated recurrence and initial values. The number \(t_n-f_n\) therefore counts words for which the first two classes are \(2\)-packings but their union is not. Such a word automatically uses all three colors: if color \(1\) or \(2\) is absent, its union is a \(2\)-packing; if color \(0\) is absent, the cyclic triple-spacing rule cannot be satisfied using only two nonzero colors (every three successive positions must have pairwise distinct colors). Each valid word gives a three-block TOI coalition partition.

**5. Correct for the triangle multiplicity.** A triangular partition assigns each vertex one of three \(2\)-packing colors. Every three consecutive vertices must have different colors, and therefore the coloring is forced to be three-periodic. Such a partition exists exactly if \(3\mid n\), and then it is uniquely the unordered collection of three residue classes modulo three. A path partition appears twice among the \(t_n-f_n\) words, by exchanging its two leaves; the unique triangle partition appears six times, by choosing and ordering its two colored classes. Hence
\[
t_n-f_n=2S_n+6\mathbf1_{3\mid n},\qquad
N_n=S_n+\mathbf1_{3\mid n}
=\frac{t_n-f_n}{2}-2\mathbf1_{3\mid n}.
\]
This is the stated formula and the complete path/triangle classification.

**6. Exponential growth.** The nonnegative matrix \(T\) is primitive: its state digraph is strongly connected and the \((0,0)\)-state has a loop. Its Perron eigenvalue \(\lambda\) lies in the quartic factor and exceeds \(2\). All other roots of both factors have modulus less than \(\lambda\); the spectral radius of \(U\) is \(1.6956207695\ldots<\lambda\). Therefore \(\operatorname{tr}(T^n)=\lambda^n+o(\lambda^n)\) and \(\operatorname{tr}(U^n)=o(\lambda^n)\). The bounded triangular correction does not affect the leading term, proving \(N_n\sim\lambda^n/2\).

## Verification

Run `python3 verify.py` using only Python's standard library. It constructs the indicated \(7\)- and \(3\)-state matrices, verifies their characteristic polynomials by exact integer arithmetic, and compares the trace and recurrence formulas for \(3\le n\le45\). Separately, it enumerates all unordered three-partitions of the labelled cycles with \(3\le n\le12\) and tests domination and independence directly from the defining graph-neighborhood conditions, not from the packing or transfer formulas. All tests return `VERIFY_OK`. These finite tests verify stated computations and boundary behavior but do not replace the unrestricted argument above.

## Relationship to prior work

Buntina and Golmohammadi, *Total outer-independent coalition in graphs* (first arXiv submission July 26, 2026, arXiv:2607.23623), introduce the TOI-coalition invariant and prove the scalar maximum \(C_t^{oi}(C_n)=3\) in their Section 4, Theorem 2, part (iv). The novelty claimed here is the exact number of **all** unordered maximum partitions for every cycle, the path-versus-triangle coalition-graph split, and the recurrence/growth formula. That scalar theorem by itself does not imply a count. Krzywkowski, *Total outer-independent domination in graphs*, gives the minimum cardinality of a TOIDS on cycles but no enumeration of TOI-coalition partitions. Dobrynin and Golmohammadi, *The shortest cycle having the maximal number of coalition graphs*, consider ordinary domination-based coalition graphs and their isomorphism types, not total outer-independent coalitions or these labelled partitions. Historical priority requires independent confirmation; no claim of exhaustive literature coverage is made.

## Limitations

Counts are for labelled cycle vertices with unordered blocks, not modulo the dihedral automorphism group. Only the maximum three-block TOI-coalition partitions are counted; partitions of smaller cardinality and other coalition predicates are not enumerated. The spectral asymptotic concerns fixed cycle model with \(n\to\infty\). Finite computations are supporting checks, not proof for all orders. Historical novelty and the mathematical argument have not been independently audited.

## References

1. O. Buntina and H. Golmohammadi, *Total outer-independent coalition in graphs*, arXiv:2607.23623 (initial public submission July 26, 2026), https://arxiv.org/abs/2607.23623.
2. M. Krzywkowski, *Total outer-independent domination in graphs*, available preprint, https://krzywkowski.pl/sub4.pdf.
3. A. A. Dobrynin and H. Golmohammadi, *The shortest cycle having the maximal number of coalition graphs*, Discrete Mathematics Letters **14** (2024), 21--26, https://www.dmlett.com/archive/v14/DML24_v14_pp21-26.pdf.
