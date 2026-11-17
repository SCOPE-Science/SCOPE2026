# A mod-four automorphism rigidity theorem for finite universal Fibonacci groupoids

## Finding

**Theorem.** Let \(G\) be a finite set of cardinality \(n\ge 1\) equipped with a binary operation \(*\). Assume there is a **universal Fibonacci sequence**, meaning a (one-sided or two-sided) sequence \(u\) satisfying \(u_{i+2}=u_i*u_{i+1}\) such that every Fibonacci sequence arising from any initial ordered pair of elements of \(G\) is a suffix of \(u\). Then

\[
\operatorname{Aut}(G,*)\cong \mathbf 1\quad\text{or}\quad C_2.
\]

The second possibility can occur **if and only if** \(n\equiv2\pmod4\). More precisely:

1. If the universal Fibonacci sequence is strictly preperiodic, the automorphism group is trivial.
2. If it is periodic and \(n\not\equiv2\pmod4\), the automorphism group is trivial.
3. If it is periodic and \(n\equiv2\pmod4\), its automorphism group is either trivial or \(C_2\), and for **every** such \(n\) there is an explicit periodic example with automorphism group \(C_2\).

The one-element case has trivial automorphism group. The source's uniqueness theorem gives the first assertion as a corollary; the new classification is the sharp upper bound and existence threshold for *periodic* examples.

## Assumptions and scope

A binary groupoid here means an arbitrary magma; no associative or cancellation law is assumed. Its automorphisms are bijections preserving \(*\). For finite nontrivial universal Fibonacci groupoids, the established classification says the universal sequence is either (a) periodic, with one period of length \(n^2\) containing each ordered pair of symbols exactly once as adjacent letters, or (b) one-sided strictly preperiodic, with a unique unshifted universal sequence [1, Theorems 3.15, 4.1 and 4.2]. In case (a), the period is a de Bruijn cycle of order two on an \(n\)-symbol alphabet. Conversely any such cycle determines an operation uniquely by \(u_i*u_{i+1}=u_{i+2}\), with indices interpreted cyclically [1, Theorems 3.8 and 4.2].

## Proof

**Step 1 (the nonperiodic case).** An automorphism \(f\) sends a universal Fibonacci sequence \(u\) to the sequence \(f(u)\), which is also universal. Uniqueness of the strictly preperiodic universal sequence [1, Theorem 3.15] forces equality term by term. Because every symbol of \(G\) appears in \(u\), \(f\) fixes all symbols. Hence the automorphism group is trivial.

**Step 2 (faithful cyclic action in the periodic case).** Let \(u_0,u_1,\ldots,u_{n^2-1}\) be a periodic universal cycle, with indices modulo \(n^2\). Define the successor map on ordered pairs
\[
T(a,b)=(b,a*b).
\]
It is a single \(n^2\)-cycle because the consecutive pairs \((u_i,u_{i+1})\) exhaust \(G^2\) without repetition. An automorphism \(f\) acts diagonally on \(G^2\) and commutes with \(T\). The centralizer in the symmetric group of a full \(n^2\)-cycle is its own cyclic group. Thus the homomorphism \(\operatorname{Aut}(G,*)\longrightarrow C_{n^2}\) sending \(f\) to its induced shift is injective (a zero shift fixes every ordered pair and hence every symbol).

Moreover, a nonidentity automorphism has **no fixed symbol**: a fixed symbol \(a\) gives a fixed ordered pair \((a,a)\), but a nontrivial power of a full cycle has no fixed pair. Consequently, if the automorphism group has order \(d\), its action on \(G\) is semiregular and \(d\mid n\).

**Step 3 (a voltage obstruction).** Suppose \(d>1\). Since the shift subgroup is the unique subgroup of order \(d\) inside \(C_{n^2}\), choose the generator \(\sigma\) whose induced shift is precisely \(L=n^2/d\). Put \(m=n/d\). The \(m\) symbol orbits of \(\sigma\) may be denoted by \(\{(A,t):t\in\mathbb Z/d\mathbb Z\}\), with \(\sigma(A,t)=(A,t+1)\). An ordered pair from \((A,t)\) to \((B,t+h)\) has an orbit under \(\sigma\) specified uniquely by the triple \((A,B,h)\). There are \(m^2d=L\) such edge orbits.

The first \(L\) consecutive ordered pairs of the de Bruijn cycle represent every such orbit **exactly once**: applying \(\sigma\) advances the starting index by \(L\), and the full \(n^2\) pair positions are all distinct. The first segment begins at \(u_0\) and finishes at \(u_L=\sigma(u_0)\), so its total change in the second, phase, coordinate equals \(1\pmod d\). Every traversed edge of type \((A,B,h)\) changes that coordinate by \(h\). Summing over the complete quotient edge set gives
\[
1\equiv m^2\sum_{h=0}^{d-1}h
 =m^2\frac{d(d-1)}2\pmod d.
\]
If \(d\) is odd, the right-hand side is zero. If \(d\ge4\) is even, it is either zero or \(d/2\pmod d\); neither equals one. Thus \(d=2\). In that case the congruence reads \(1\equiv m^2\pmod2\), forcing \(m\) odd and \(n=2m\equiv2\pmod4\). This proves the universal bound and necessary congruence.

**Step 4 (sharpness at every allowed cardinality).** Fix \(n=2m\) with \(m\ge1\) odd. Use the alphabet \(G=\{(A,t):A\in\{0,\ldots,m-1\},\ t\in\mathbb Z/2\mathbb Z\}\), and define \(\sigma(A,t)=(A,t+1)\). Form the directed multigraph \(D\) with vertices \(A\in\{0,\ldots,m-1\}\), having for every ordered pair of vertices \((A,B)\) two distinct directed arcs \((A,B,h)\), \(h\in\mathbb Z/2\mathbb Z\). It is strongly connected and every vertex has indegree and outdegree \(2m\), hence possesses a directed Euler circuit. Choose any such circuit, starting and ending at vertex \(A_0\); it uses all \(2m^2\) arcs exactly once.

Lift the Euler circuit to the alphabet by interpreting arc \((A,B,h)\) as \((A,t)\to(B,t+h)\). The first lift starts at \((A_0,0)\). Since the sum of its arc labels is \(m^2\equiv1\pmod2\), the lift ends at \((A_0,1)\). Repeat the same quotient circuit from phase one; its lift returns to \((A_0,0)\). The combined closed walk has length \(4m^2=n^2\). Every quotient arc was traversed once in each of the two phases, so the combined walk uses **every ordered pair of letters exactly once**. Reading its source vertices yields a de Bruijn cycle \(B(n,2)\), defining a periodic universal Fibonacci groupoid. The first half of this cycle is carried to its second half by \(\sigma\); therefore \(\sigma\) is a nontrivial automorphism. Step 3 rules out any further automorphisms, giving precisely \(C_2\).

The construction works unchanged for \(m=1\), in which case a cyclic word is \((0,0,1,1)\) up to labeling and rotation. If \(n=1\), the only permutation of the underlying set is the identity.

## Verification

`verify.py` is a standalone Python 3 program using only the standard library. Execute `python verify.py` in a directory containing it. The program independently:

- Exhausts **all** de Bruijn cycles on alphabets of sizes two, three, and four, obtaining respectively 1, 24, and 20,736 cyclic words, and computes their actual magma automorphism groups by checking all symbol permutations against the operation tables.
- Changes each entry of each such operation to every other symbol, testing all 436 resulting nonperiodic one-cell modifications for automorphism rigidity.
- Builds quotient Euler tours and their lifted cycles at \(n=2,6,10\), checks all \(n^2\) adjacent pairs, verifies the half-shift involution, and for \(n\le6\) tests the full automorphism group by brute-force symbol permutations.
- Constructs independent ordinary Euler-tour examples at \(n=3,4\) and checks their automorphism groups.

The accompanying `VERIFY_OUTPUT.txt` records the output of a replay from this package. These tests are finite corroboration; the argument above proves the arbitrary-cardinality theorem.

## Relationship to prior work

Klimov [1] introduces universal Fibonacci groupoids, proves uniqueness of the universal sequence and their classification through periodic de Bruijn cycles and strictly preperiodic sequences, and counts labeled examples. These facts are **used**, not claimed anew. In particular, rigidity in the strictly preperiodic case is an immediate consequence of [1, Theorem 3.15]. The distinct assertion here is a sharp bound on *automorphism groups of periodic objects* and the arithmetic criterion for nontrivial symmetry, proved using a quotient-voltage obstruction and a matching infinite construction.

The de Bruijn graph/Euler tour correspondence is classical [2,3]. The full automorphism group of the **ambient de Bruijn digraph** is much larger [4]; it is not the stabilizer of a particular directed Euler circuit, which is the group classified here. Existing orientable/universal-cycle constructions [5] do not assert the given cyclic-word stabilizer classification.

## Limitations

This theorem addresses **finite** universal Fibonacci groupoids only, not infinite ones. It establishes the possible automorphism-group isomorphism types and a sharp necessary-and-sufficient condition for the **existence** of a nontrivial example, but does not enumerate isomorphism classes of symmetric groupoids or the proportion possessing nontrivial symmetry. The asserted converse is existence, not a claim that every periodic example at the allowed cardinalities is symmetric. Historical priority is subject to literature coverage, especially de Bruijn-word symmetry under alphabet relabeling; comparison of statements, not absence of search hits, is essential.

## References

[1] Petr Klimov, *Universal Fibonacci sequences and UFS-groupoids*, arXiv:2604.05754v2 (first publicly posted 2026-04-07), especially Theorems 3.8, 3.15, 4.1, 4.2, and 4.6. https://arxiv.org/html/2604.05754v2

[2] N. G. de Bruijn and T. van Aardenne-Ehrenfest, *Circuits and trees in oriented linear graphs*, Simon Stevin 28 (1951), 203–217.

[3] *De Bruijn Sequences and Universal Cycles*, construction portal, https://debruijnsequence.org/db/graph (consulted 2026-11-06).

[4] W. Y. C. Chen, V. Faber, and B. Li, *Automorphisms of the cycle prefix digraph*, arXiv:1404.4907, 2014, https://arxiv.org/abs/1404.4907 (background on ambient graph automorphisms).

[5] A. Alhakim, C. J. Mitchell, J. Szmidt, and P. R. Wild, *Orientable sequences over non-binary alphabets*, Cryptography and Communications 16 (2024), 1309–1326, https://link.springer.com/article/10.1007/s12095-024-00742-x.
