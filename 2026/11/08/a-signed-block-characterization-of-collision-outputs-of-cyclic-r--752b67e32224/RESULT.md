# A signed-block characterization of collision outputs of cyclic Rule 30

## Finding

Let \(n\ge3\) be an integer. For a binary indexed word \(y\in\{0,1\}^n\), write \(b_n(y)=|F_n^{-1}(y)|\), where \(F_n\) is cyclic Rule 30. Then

\[
 b_n(y)\ge2 \quad\Longleftrightarrow\quad
 y=0^n\quad\text{or}\quad
 \exists\text{ a cyclic rotation }y'=(11\,0^{m_1}b_1)\cdots(11\,0^{m_k}b_k),
\]

with \(k\ge1\), \(m_j\in\mathbb Z_{\ge0}\), \(b_j\in\{0,1\}\), and

\[
 \sum_{j=1}^k\mathbf1_{\{b_j=0\}}\equiv0\pmod2.
\]

The bars between blocks are conceptual; a factorization may be nonunique. An output is counted by its **indexed** word, not by its necklace. The theorem holds for words with nontrivial rotational periods. Its essential feature is a parity restriction on the blocks ending in zero; omitting that restriction admits false collision candidates.

For example, \(1101\) has the one-block decomposition \(11\,0\,1\), whereas \(110\) has one block ending in zero and fails the parity condition. The all-zero output is a separate exception. The known predecessor-frequency classification implies that the only three-predecessor outputs are \(1^n\) for multiples of three, but this pre-existing frequency result is **not** the claim established here.

## Assumptions and scope

Index all coordinates modulo \(n\). Rule 30 is exactly

\[
(F_n(x))_i=f(x_{i-1},x_i,x_{i+1}),\qquad f(a,b,c)=a\oplus(b\lor c).
\]

Distinct predecessors means distinct indexed words in \(\{0,1\}^n\), not rotations of one another. Two words which differ only by rotation are distinct unless the rotation fixes the word. The theorem concerns one simultaneous update, not multi-step ancestors or bi-infinite predecessors. We assume \(n\ge3\), so each local neighborhood has the usual three positions.

## Proof

**1. Ordered collision graph.** To detect a pair \(x\ne x'\) with \(F_n(x)=F_n(x')\), use states \((a,b;c,d)\in\{0,1\}^4\) representing adjacent input pairs \((x_{i-1},x_i)=(a,b)\) and \((x'_{i-1},x'_i)=(c,d)\). There is an edge to \((b,e;d,h)\) labeled \(t\) precisely when \(f(a,b,e)=f(c,d,h)=t\). Closed length-\(n\) labeled walks are in bijection with ordered predecessor pairs with that output. If two such words share two consecutive coordinates, left permutivity of \(f\) forces equality one position to the left, repeatedly around the ring, contradicting distinctness. Hence every vertex of a genuine collision lies off the diagonal \((a,b)=(c,d)\).

There are twelve off-diagonal states. A direct enumeration of the two possible next bits in each predecessor yields precisely eight vertices lying on a directed cycle:

\[
\begin{gathered}
(00;01),(01;00),\ (00;10),(10;00),\\
(00;11),(11;00),\ (01;10),(10;01).
\end{gathered}
\]

The other four off-diagonal states have no closed walk. Their absence is checked directly from the complete rule table, not inferred from a finite trajectory experiment.

**2. Orientation-preserving quotient.** Interchanging \(x\) and \(x'\) pairs the eight recurrent vertices. Choose representatives

\[
 A=(00;01),\qquad B=(00;10),\qquad C=(00;11),\qquad D=(01;10).
\]

For each quotient edge record its output label and an orientation-flip bit, equal to one if its lifted endpoint is the swapped representative. The complete edge set is:

| Source | Output | Destination | Flip |
|---|---|---|---|
| \(A\) | \(1\) | \(D\) | \(0\) |
| \(D\) | \(1\) | \(B\) | \(1\) |
| \(D\) | \(1\) | \(C\) | \(1\) |
| \(B\) | \(0\) | \(A\) | \(0\) |
| \(B\) | \(1\) | \(A\) | \(1\) |
| \(C\) | \(0\) | \(B\) | \(0\) |
| \(C\) | \(0\) | \(C\) | \(0\) |

In a closed quotient walk, the sum of flip bits must be even to lift to a closed **ordered** predecessor pair on the same \(n\)-ring. Conversely, an even-flip closed quotient walk has two ordered closed lifts, giving two distinct length-\(n\) predecessors. This is why simply checking for a quotient cycle without signs would be incorrect.

**3. Decomposition of quotient walks.** Any closed quotient walk avoiding \(A\) is the \(0\)-loop at \(C\); the corresponding output is \(0^n\), and it has an even-flip lift. Every other closed quotient walk visits \(A\) and decomposes at successive visits to \(A\). Each return segment follows

\[
 A\xrightarrow{1}D\xrightarrow{1}(B\text{ or }C)\xrightarrow{0^{m}}B\xrightarrow{b}A,
\]

where the notation allows \(m=0\) if the first state after \(D\) is \(B\). Thus its output block is \(11\,0^m b\) for a unique integer \(m\ge0\) within that chosen segment and a final bit \(b\in\{0,1\}\). The edge leaving \(D\) has flip one; the final edge from \(B\) has flip one exactly when \(b=1\); all zero-labeled intermediate edges have flip zero. Consequently the total flip of a return block is \(1+\mathbf1_{\{b=1\}}\), which modulo two equals \(\mathbf1_{\{b=0\}}\). An even lift exists exactly when the number of terminal zero bits is even. Allowing a cyclic cut at any visit to \(A\) gives the stated rotation condition. Both necessity and sufficiency follow.

**4. Recognition.** For a fixed output \(y\), propagate each of the four possible starting quotient states with an orientation parity bit under the seven labeled edges in the table. A collision exists exactly if a state returns with parity zero. This uses eight Boolean states and \(O(n)\) transitions, and also recognizes the \(0^n\) exception without separate handling. The mathematical statement does not rely on the running time of the independent finite verifier.

## Verification

The attached standard-library script `verify_signed_language.py` derives the twelve-state off-diagonal ordered pair graph directly from \(f\), proves by exact finite graph traversal that precisely the claimed eight states occur on a directed cycle, and derives both orientations of the seven signed quotient transitions rather than assuming them. It separately implements (i) the signed-graph closed-lift condition, (ii) exhaustive rotation/block-factorization recognition with parity, and (iii) direct one-step predecessor enumeration, and compares all three methods for every indexed output at every length \(3\le n\le16\) (\(131{,}064\) outputs total). It also checks the bound of at most three predecessors and the exceptional three-predecessor position in that finite range. Expected output:

```
INDEPENDENT_PAIR_GRAPH_REDUCTION_OK 12 offdiagonal, 8 recurrent
SIGNED_BLOCK_LANGUAGE_EQUIVALENCE_OK 3..16 131064 targets
```

The general assertion follows from the explicitly enumerated finite graph and the arbitrary-length closed-walk argument above; the bounded exhaustive tests are regression checks, not an infinite proof.

## Relationship to prior work

The original Rule 30 and its left-permutivity are classical (Wolfram, 1983). Wolfram's later note explicitly describes predecessor multiplicities, their aggregate growth rate, and a generic inverse-construction algorithm; it does not state a parity-restricted block-language classification of the individual ambiguous outputs. Jeras and Dobnikar (2007) give general de Bruijn network algorithms that count and list predecessors of an arbitrary target; their material addresses Rule 110 examples and does not state this Rule-30-specific finite signed quotient. Powley and Stepney (2010) focus on homogeneous-target predecessor counts. These methods are structurally relevant, not independent novelty claims. Here the claim is the explicit intrinsic output-language description and the small signed graph, not general decidability, the standard de Bruijn technique, aggregate predecessor counts, or the known exceptional all-one triple-predecessor case.

## Limitations

The theorem covers one-step indexed periodic Rule 30 on rings of length at least three, not infinite spatial configurations, other rules, or iterates. It says which output words have at least two predecessors; it does not claim a new full predecessor-frequency formula, entropy, image size, or optimal time complexity. An unindexed equivalent structural classification or a derivation hidden in older literature remains a historical-priority risk. The cited early broad survey was available only as an abstract; specialized sources were read at the indicated material scope. Independent mathematical audit has not been performed.

## References

- S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics 55 (1983), 601–644, DOI: https://doi.org/10.1103/RevModPhys.55.601 (published July 1, 1983).
- S. Wolfram, *A New Kind of Science* (2002), Chapter 10 note, “Cryptographic properties of Rule 30”, https://www.wolframscience.com/nks/notes-10-10--cryptographic-properties-of-rule-30/.
- I. Jeras and A. Dobnikar, *Algorithms for computing preimages of cellular automata configurations*, Physica D 233 (2007), 95–111; open author preprint https://rattus.info/al/files/preimages.pdf (dated October 5, 2007).
- E. J. Powley and S. Stepney, *Counting Preimages of Homogeneous Configurations in 1-Dimensional Cellular Automata*, Journal of Cellular Automata 5 (2010), 353–381, https://www.researchgate.net/publication/220440963_Counting_Preimages_of_Homogeneous_Configurations_in_1-Dimensional_Cellular_Automata.
- *Global Reversibility of Cellular Automata*, https://www.mathpages.com/home/kmath439/kmath439.htm (background discussion of cyclic Rule 30 predecessor examples; not treated as a primary new theorem source).
