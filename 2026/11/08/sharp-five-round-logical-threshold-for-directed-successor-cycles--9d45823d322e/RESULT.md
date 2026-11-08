# Sharp five-round logical threshold for directed successor cycles

## Finding
For each integer \(n\geq1\), let \(C_n\) be the directed cycle on \(\{0,\ldots,n-1\}\), equipped solely with the binary successor relation \(S_n(a,b)\) holding if and only if \(b\equiv a+1\pmod n\). Thus \(C_1\) has a loop, and \(C_2\) has two reciprocal directed edges. Let \(C_n\equiv_q C_m\) mean agreement on **every ordinary first-order sentence of quantifier rank at most \(q\)** in the language \(\{S\}\), with equality but without a linear order, counting quantifiers, constants, or additional predicates.

**Theorem.** For every \(q\in\{1,2,3,4,5\}\), the complete \(\equiv_q\)-partition of all finite directed successor cycles consists of the individual length classes \(\{1\},\ldots,\{T_q-1\}\) and the single remaining class \(\{n:n\geq T_q\}\), where
\[
(T_1,T_2,T_3,T_4,T_5)=(2,4,7,11,19).
\]
In particular, rank five distinguishes every two different cycle lengths below \(19\), distinguishes each of those lengths from all greater lengths, and cannot distinguish any two lengths at least \(19\). There are exactly \(19\) rank-five theories realized by this family.

## Assumptions and scope
This is a theorem about finite *single cycles*, not arbitrary disjoint unions of cycles or directed paths. Each edge is the graph of a successor permutation, but the logic sees only the binary relation \(S\), not the iterates as separate relation symbols. A quantifier rank bound is not a bound on the total number of quantifiers or formula size. The statement concerns ranks one through five only; it does not infer or propose a formula for the thresholds at larger ranks. The numerical cutoff \(19\) is an exact natural invariant of this signature and rank.

## Proof
**Step 1: exact rank-type recursion.** For a finite directed cycle \(C_n\), an ordered tuple \(\bar a=(a_1,\ldots,a_k)\), and an integer \(r\geq0\), define the quantifier-free atomic diagram \(A_n(\bar a)\) as the ordered array of the truth values \(a_i=a_j\) and \(S_n(a_i,a_j)\) for all ordered pairs \((i,j)\). Define a finite signature recursively:
\[
T_n^{(0)}(\bar a)=A_n(\bar a),\qquad
T_n^{(r+1)}(\bar a)=\left(A_n(\bar a),\ \{T_n^{(r)}(\bar a,c):c\in C_n\}\right).
\]
Each signature includes its tuple arity. By induction on \(r\), two tuples (possibly from different cycles) have the same \(T^{(r)}\)-signature if and only if they satisfy the same first-order formulas of quantifier rank at most \(r\), with their free variables assigned to the tuples. At rank zero this is atomic-diagram equivalence. The inductive step follows because the sets of extension signatures agree precisely when all existential rank-\(r+1\) tests agree; negation covers universal tests, and Boolean combinations do not increase quantifier rank. Conversely, each distinct extension type has a finite characteristic formula by the same induction, so the criterion is an *if and only if*. This is also the standard \(r\)-round back-and-forth characterization. In particular, \(T_n^{(q)}(())\) exactly identifies the rank-\(q\) theory of \(C_n\).

**Step 2: exhaustive finite computation, not sampling.** The accompanying standalone `checker.py` computes these signatures with equality-tested structural keys. It recursively enumerates *every* extension vertex and every needed tuple state for each integer \(1\leq n\leq32\) and each \(1\leq q\leq5\); signatures are interned by their complete structural records, never by matching a truncated numerical hash. Rotation normalization is sound because translation modulo \(n\) is an automorphism of \(C_n\). The checker verifies the following entire classes within \(1\leq n\leq32\):

| Rank \(q\) | Individually distinguishable lengths | Single remaining class in the computation |
|---|---|---|
| \(1\) | \(1\) | \(2\) through \(32\) |
| \(2\) | \(1,2,3\) | \(4\) through \(32\) |
| \(3\) | \(1\) through \(6\) | \(7\) through \(32\) |
| \(4\) | \(1\) through \(10\) | \(11\) through \(32\) |
| \(5\) | \(1\) through \(18\) | \(19\) through \(32\) |

To cross-check an independent formulation, the checker also directly solves the adversarial Spoiler/Duplicator game by recursive minimax for all pairs of lengths through \(7\) and all ranks through \(3\), confirming exactly the same equivalence partition. These computations are exhaustive for the indicated **finite** ranges and are verified by executing the included code; they are not a substitute for the next argument, which treats every larger length.

**Step 3: infinite-tail Ehrenfeucht–Fraïssé lemma.** For every integer \(q\geq1\), Duplicator wins the \(q\)-round EF game between any two directed cycles of lengths at least \(2^q\). After the first move, map the selected vertex to its response. Both cyclic gaps between this single selected point and itself are of length at least \(2^q\). With \(r=q-1\) rounds remaining, maintain a cyclic-order-preserving bijection of the distinct selected vertices such that corresponding directed gaps have **either equal positive edge length or both length at least \(2^{r+1}\)**. Repeated selections are matched identically. If Spoiler selects a new point inside a pair of equal gaps, copy its directed offset. Otherwise both gaps have length at least \(2^{r+1}\). In the gap Spoiler splits, if a new side has length strictly below \(2^r\), give the matching side exactly that length; the other new sides in both structures have length at least \(2^r\). If neither new side is short, split the response gap with both sides at least \(2^r\), possible because its length is at least \(2^{r+1}\). Thus the invariant holds with \(r-1\) moves remaining. At \(r=0\), equalities of selected vertices agree and a directed adjacency between selected vertices is exactly a directed gap of length one; the invariant preserves these because unequal but paired large gaps have length at least two. The final mapping is a partial isomorphism. This proves the lemma for arbitrary lengths, including those beyond the computation.

**Step 4: combine the bounds.** Every cycle of length at least \(32=2^5\) is rank-five equivalent to \(C_{32}\), and hence also rank-\(q\) equivalent for each smaller \(q\). Step 2 determines the exact rank partitions for all lengths through \(32\), including the comparisons of \(C_{32}\) with all shorter cycles. Transitivity of \(\equiv_q\) now extends the finite table to *every* positive cycle length. All five claimed thresholds, including sharpness at each boundary, follow.

## Verification
Run `python3 checker.py` using ordinary Python 3. The last two output lines are `DIRECT_GAME_CHECKS_OK` and `ALL_CHECKS_OK`. The code requires only the Python standard library. Its exact recursive type census covers all cycle lengths through \(32\), ranks through \(5\), and an independent direct-game cross-check for the smaller lengths. The infinite-tail lemma is a written proof and is not asserted to follow merely from the finite run. The integer intern IDs used by the program encode equality of complete finite recursive records, not probabilistic checksums.

## Relationship to prior work
Classical finite-model-theoretic EF games and Gaifman locality provide the conceptual setting and general bounds. Grohe and Schweikardt's June 2026 work gives a rank-preserving Gaifman normal form, with a later generalization to weighted structures by van Bergerem, Grohe, Lenz, and Schweikardt. Neither investigated material states the exact \(19\)-vertex rank-five threshold in the relation-only directed-cycle family. A separate published exact result treats *directed paths* and a \(2^q\) rank threshold there; it does not imply the present cycle classification because paths have endpoints and cycles do not. This theorem makes no claim to a new EF method or a new general locality theorem; the new subject is the sharp complete finite-cycle profile through rank five.

## Limitations
This classification makes no assertion for quantifier rank above five, other signatures (such as a named start vertex or a linear order), or unions of several cycles. The cutoff is verified through an exhaustive finite computation combined with a standard but explicitly proved infinite-tail EF argument. Historical priority is not conclusively established: an earlier specialized account of finite successor cycles might already contain the same rank-five table. Some potentially related source texts were not accessible in full. No independent mathematical validation has been performed.

## References
- Martin Grohe and Nicole Schweikardt, *A Rank-Preserving Gaifman Normal Form*, arXiv:2606.11993, first public submission June 10, 2026, https://arxiv.org/abs/2606.11993.
- Steffen van Bergerem, Martin Grohe, Charlotte Lenz and Nicole Schweikardt, *A Rank-Preserving Gaifman Normal Form for First-Order Logic on Weighted Structures*, arXiv:2609.37337, first public submission September 29, 2026, https://arxiv.org/abs/2609.37337.
- Leonid Libkin, *Elements of Finite Model Theory*, Springer, 2004 (EF games, rank types, and locality).
- *Exact quantifier-rank threshold for finite directed paths*, public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112.
