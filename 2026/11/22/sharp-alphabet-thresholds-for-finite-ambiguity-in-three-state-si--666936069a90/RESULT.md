# Sharp alphabet thresholds for finite ambiguity in three-state singleton-component automata

## Finding
Let \(A_{3,k}\) be the greatest degree of ambiguity among all **trim, finitely ambiguous**, epsilon-free nondeterministic finite automata with states \(q_1,q_2,q_3\), initial state \(q_1\), sole final state \(q_3\), exactly \(k\ge1\) input symbols, and transitions only \(q_i\to q_i\) or \(q_i\to q_{i+1}\). A word's ambiguity is the number of distinct accepting state paths on that word, and an automaton's degree is the supremum over all input words. Then
\[
A_{3,k}=\begin{cases}1,&k=1,\\3,&k=2,\\4,&k\ge3.\end{cases}
\]
In particular, ternary is the smallest alphabet attaining the unrestricted three-state maximum. The binary bound has a complete labeled transition-table census: exactly 246 of the 1024 ordered binary pairs of possible transition relations are trim and finitely ambiguous; 216 have degree 1, 28 have degree 2, and two have degree 3.

There is also a structural classification: every finitely ambiguous transition-type alphabet is contained in one of two explicitly defined maximal permissible alphabets, each comprising 23 of the 32 possible single-letter transition relations. Their integer-matrix product closures each contain exactly 48 matrices, whose largest \((1,3)\) entry is 4.

## Assumptions and scope
Input symbols are distinct labels, although two labels may encode the same transition relation. Every allowed edge is either a loop or an adjacent forward edge, and no epsilon transitions, multiplicity-weighted parallel edges, skip edges \(q_1\to q_3\), additional initial/final states, or reverse edges are permitted. The two forward edges must each appear for the automaton to be trim; in this graph this is also sufficient. Empty words have zero accepting paths. The maximum is over all automata and all finite input words; no word-length restriction is imposed.

Encode a letter by a five-bit integer \(t\in\{0,\dots,31\}\), with bit positions 0, 1, 2, 3, 4 indicating respectively the edges \(q_1\to q_1\), \(q_1\to q_2\), \(q_2\to q_2\), \(q_2\to q_3\), \(q_3\to q_3\). The corresponding ordinary integer path-count matrix is
\[
M_t=\begin{pmatrix}\ell_1&u&0\\0&\ell_2&v\\0&0&\ell_3\end{pmatrix}.
\]
For a word \(w\), its accepting-run count is the \((1,3)\) entry of \(M_w\), where \(M_w\) is the ordered product of its letter matrices.

## Proof
**1. An obstruction classification.** Define the following forbidden local patterns among the letters of an alphabet:

- \(P_{12}\): a letter carrying simultaneously \(\ell_1=\ell_2=u=1\);
- \(P_{23}\): a letter carrying simultaneously \(\ell_2=\ell_3=v=1\);
- \(X\): a letter with \(\ell_1=\ell_3=u=1\);
- \(Y\): a letter with \(\ell_1=\ell_3=v=1\).

A trim automaton with \(P_{12}\) has unbounded ambiguity: repeating that letter produces arbitrarily many paths from \(q_1\) to \(q_2\), after which a fixed suffix reaches \(q_3\). The dual prefix argument handles \(P_{23}\). If both \(X\) and \(Y\) are represented (possibly by the same symbol), take letters \(x\in X,y\in Y\). A block \(xy\) admits loops from \(q_1\) to itself and from \(q_3\) to itself, as well as a path from \(q_1\) to \(q_3\). The words \((xy)^m\) therefore have at least \(m\) distinct accepting paths, according to which block performs the passage. Thus every finitely ambiguous alphabet avoids \(P_{12}\), avoids \(P_{23}\), and omits all letters of \(X\) or all letters of \(Y\).

Define \(T_X\) to be the 32 letter types with the three conditions \(\neg P_{12}\), \(\neg P_{23}\), \(\neg X\), and define \(T_Y\) analogously using \(\neg Y\). The preceding argument proves that every finitely ambiguous alphabet is a subset of \(T_X\) or \(T_Y\), including alphabets with duplicated transition types.

**2. Exhaustive but finite algebraic upper certificate.** The sets of permitted type integers are

\(T_X=\{0,1,2,3,4,5,6,8,9,10,11,12,13,14,16,17,18,20,21,22,24,25,26\}\),

\(T_Y=\{0,1,2,3,4,5,6,8,9,10,11,12,13,14,16,17,18,19,20,21,22,24,26\}\).

A six-tuple \((a,b,c,d,e,f)\) represents the upper-triangular matrix with rows \((a,b,c),(0,d,e),(0,0,f)\). The product of two six-tuples \((a,b,c,d,e,f)\) and \((A,B,C,D,E,F)\) is
\[
(aA,\ aB+bD,\ aC+bE+cF,\ dD,\ dE+eF,\ fF).
\]
Starting with the identity \((1,0,0,1,0,1)\) and closing under right multiplication by the 23 letter matrices gives exactly 48 six-tuples for each of \(T_X,T_Y\). The full two explicit lists are `matrices_X.csv` and `matrices_Y.csv`. Each contains the identity and all generators, is closed under every required right multiplication, and has maximum third coordinate 4. These verifiable finite properties prove \(A_{3,k}\le4\) simultaneously for every finite alphabet size, without extrapolation over word length. They also show that each of the two maximal allowed alphabets is itself finitely ambiguous, completing the obstruction classification.

**3. Sharp alphabet restrictions.** To handle at most two letters, enumerate the 32 possible single-letter types and every ordered pair of types. For each pair that has both adjacent bridges and lies wholly in \(T_X\) or wholly in \(T_Y\), compute the matrix closure from the identity; finiteness is guaranteed by step 2. Exactly 216 of the 1024 labeled ordered pairs have ambiguity degree 1, 28 degree 2, and two degree 3. No permitted binary pair has degree 4. For one letter, the only trim finite types are \(10,11,14,26\), and each has degree 1. Both finite enumerations follow from precisely specified 32- or 1024-case loops in the independent verifiers, with no unspecified external data.

Finally, type 10 repeated twice (`aa`) gives one accepting run. On the two-letter alphabet represented by types \(11,26\), `aabb` has exactly three runs. On the three-letter alphabet represented by types \(3,14,24\), `abbc` has exactly four runs. Each witness avoids all three unbounded-ambiguity obstructions, hence is finitely ambiguous by step 2. Adding unused duplicate letter types preserves the ternary witness for every \(k>3\). This proves every sharp bound and completes the theorem.

## Verification
Run `python3 verify.py` in the same directory as both CSV files. It independently constructs the two matrix orbits and verifies that each supplied 48-element set is complete, includes the identity and generators, is closed under right multiplication, and has maximal accepting count four. It then checks every ordered binary transition pair, the exact distribution \((216,28,2)\), the unary bound, and all three witnesses. Separately compile `verify.cpp` with `g++ -O2 -std=c++17 verify.cpp -o verify_cpp` and run `./verify_cpp`; it uses full three-by-three integer matrices rather than the six-coordinate implementation, and independently recomputes both semigroups, binary distribution and witnesses. Both programs terminate with `VERIFY_OK` on successful verification. This is a finite certificate of the infinite-word upper bound because closure under the entire generator set contains the matrix of **every** finite word.

## Relationship to prior work
Weber and Seidl (1991, Sections 3 and 5, Table 1 and Lemma 5.5) establish the IDA characterization and alphabet-dependent asymptotic bounds for unitary-component chain automata. In particular, their three-letter lower bound \(2^{n-1}\) already yields four accepting paths at \(n=3\); that lower bound and the obstruction method are not claimed as new here. Their Table 1 does not supply the matching sharp three-state upper bound or the exact unary/binary/ternary threshold.

Kiefer, Mazowiecki, Ryzhikov and Wiśniewski (arXiv:2610.08525, initially public October 6, 2026), Section 3, define \(A_n\) and prove \(A_3\le12\) using a recursive bound, while Section 5 treats asymptotic lower bounds. The present theorem closes that three-state gap to \(A_3=4\) and establishes the sharp alphabet dependence \(A_{3,1}=1\), \(A_{3,2}=3\), \(A_{3,k}=4\) for \(k\ge3\). The result does not claim a better all-state exponential bound.

## Limitations
The theorem concerns only three-state trim chain NFAs with singleton strongly connected components and **adjacent-only** forward bridges, not all three-state NFAs or all singleton-SCC NFAs allowing skip edges. It does not determine \(A_n\) for \(n\ge4\). All computations use integer path counts, not Boolean matrix multiplication. The exhaustive certificate is for 32 letter types and their two 48-element closures; it is mathematically exhaustive only because of the preceding reduction to those two generating alphabets. No external independent audit or external equivalence classification has been performed.

## References
1. S. Kiefer, F. Mazowiecki, A. Ryzhikov and A. Wiśniewski, *Stronger bounds on the degree of ambiguity of finite automata* (first posted October 6, 2026), https://arxiv.org/abs/2610.08525, especially Sections 2, 3 and 5.
2. A. Weber and H. Seidl, *On the degree of ambiguity of finite automata*, Theoretical Computer Science 88 (1991), 325–349, https://doi.org/10.1016/0304-3975(91)90381-B; open author-hosted version https://fmazowiecki.github.io/course/WS91.pdf, especially Section 5, Table 1 and Lemma 5.5.
