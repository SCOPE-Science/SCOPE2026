# Component spectrum and constructive reachability of cyclic binary no-triple words

## Finding
For every integer \(n\ge3\), let \(H_n\) be the graph whose vertices are indexed binary circular words \(x=(x_0,\ldots,x_{n-1})\) satisfying
\[
 (x_i,x_{i+1},x_{i+2})\notin\{(0,0,0),(1,1,1)\}\qquad(i\in\mathbb Z/n\mathbb Z),
\]
with an edge when exactly one indexed bit is flipped and the resulting word is again admissible. Define the invariant
\[
 k(x)=\#\{i\in\mathbb Z/n\mathbb Z:x_i=x_{i+1}\}.
\]
All admissible values have \(0\le k\le\lfloor n/2\rfloor\) and \(k\equiv n\pmod 2\). Conversely, every integer satisfying those inequalities and parity occurs.

**Complete connected-component classification.** For every admissible \(k\) with \(1\le k<n/2\), the entire level \(\{x:k(x)=k\}\) is exactly one connected component, containing
\[
 V_{n,k}=\frac{2n}{k}\binom{n-k-1}{k-1}
 \quad\text{vertices and}\quad
 E_{n,k}=2n\binom{n-k-2}{k-1}\quad\text{edges}.
\]
If \(k=0\) (possible only when \(n\) is even), there are exactly two isolated alternating words. If \(k=n/2\) (possible only when \(4\mid n\)), there are exactly four other isolated words. These are all the components; in particular their number is
\[
 \operatorname{comp}(H_n)=
 \begin{cases}
 \left\lfloor(n+1)/4\right\rfloor,&n\text{ odd},\\
 2+\left\lfloor(n-2)/4\right\rfloor+4\mathbf 1_{\{4\mid n\}},&n\text{ even}.
 \end{cases}
\]
Two distinct admissible words are connected if and only if they have the same strictly interior value \(1\le k<n/2\). A constructive procedure produces a legal flip path in \(O(n^2)\) flips whenever such a path exists.

## Assumptions and scope
Words are indexed, not necklaces: rotations, reversals and bitwise complements are distinct unless literally equal as indexed vectors. Cyclic triples are checked with indices modulo \(n\), even at \(n=3\). The underlying graph is simple and undirected; no graph loops or simultaneous changes are permitted. All binomial coefficients appearing in the nontrivial case have nonnegative upper arguments. For isolated vertices, the only reachable word is the identical starting word. The theorem is for binary symbols and cyclic rather than linear boundaries.

## Proof
**Difference representation.** Put \(d_i=x_i\oplus x_{i+1}\) over \(\mathbb F_2\). A forbidden constant triple is exactly a pair \(d_i=d_{i+1}=0\). Hence the zero sites of \(d\) are independent (non-neighboring) sites in the length-\(n\) cycle. Their number is \(k=k(x)\), necessarily at most \(\lfloor n/2\rfloor\). Moreover \(\bigoplus_i d_i=0\), so the number \(n-k\) of one sites is even. Conversely, any zero set having no cyclic adjacent sites and satisfying \(n-k\) even determines exactly two words \(x\), differing by global complementation: choose \(x_0\) freely and recover the other bits successively. This also proves nonemptiness of every stated \(k\) level.

**Allowed moves.** Flipping \(x_i\) toggles exactly \(d_{i-1}\) and \(d_i\). The pair cannot be \(00\) before the flip (the original word would be invalid), and it cannot be \(11\) (the resulting word would be invalid). Therefore it must be \(01\) or \(10\), and its toggle exchanges the pair. The resulting word is valid exactly when the zero has moved one site without becoming adjacent to another zero. Thus each flip projects to one *token slide* in the graph of \(k\) independent tokens on the cycle. Every such slide has a unique flip lift from each choice of \(x\). The integer \(k\) is therefore invariant.

**Connectivity of the token-slide projection.** Assume \(1\le k<n/2\). Order the token positions cyclically and let \(g_j\ge1\) count one sites of \(d\) between token \(j\) and its clockwise successor. Then \(\sum_j g_j=n-k\), and the nonnegative surplus \(e_j=g_j-1\) has total \(n-2k>0\). A token may move one step clockwise exactly when its following surplus is positive; the move transfers one unit of surplus from that gap to the preceding gap. Transporting individual surplus units around this directed \(k\)-cycle puts all surplus in any desired gap. The resulting token placement is a translate of \(\{0,2,\ldots,2k-2\}\). Passing one surplus unit around all the gaps (moving the tokens in reverse cyclic order) translates every token clockwise by one without changing its gap vector, so any translate is reachable. Consequently the projected token-slide graph is connected.

**The two lifts meet.** It remains to prove that a word \(x\) and its complement \(\overline x\) lie in one component when \(1\le k<n/2\). By projected connectivity it is enough to do this above the canonical token set \(S=\{0,2,\ldots,2k-2\}\). Here is an explicit legal closed token-slide walk: move the token at \(2k-2\) to \(2k-1\), then those at \(2j\) to \(2j+1\) for \(j=k-2,k-3,\ldots,0\); next move the token at \(2k-1\) to \(2k\), then those at \(2j+1\) to \(2j+2\) in the same descending order; finally move the token at \(2k\) stepwise through \(2k+1,\ldots,n-1,0\). Since \(n>2k\), the token gaps never vanish. At the end the zero-site set is again \(S\). The walk uses each of the \(n\) edges of the site cycle exactly once: first the edges from even to following odd positions through \(2k-1\), then the odd-to-even edges through \(2k\), then the remaining edges through the wrap. Every such edge crosses exactly one bit coordinate \(x_i\), so the lifted walk flips each bit once and ends at \(\overline x\). Therefore the two-sheet lift over a connected projected level is connected. This argument is valid for either parity of \(n\).

**Frozen extreme levels.** If \(k=0\), all difference bits are one, so only the two alternating words exist (and only for even \(n\)); flipping any bit would create adjacent zero difference bits. If \(2k=n\), the zero sites themselves alternate around the difference cycle and no token can slide. Parity requires \(k\) even, equivalently \(4\mid n\); there are two alternating difference patterns and two original words above each, giving four isolated words. No other level contains isolated vertices, by the established connectivity and explicit moves.

**Vertex and edge enumerators.** An independent \(k\)-token set on the indexed site cycle has \(k\) choices for its distinguished token when represented by an ordered cyclic composition \(g_1+\cdots+g_k=n-k\) into positive parts, and \(n\) possible distinguished-token sites. Hence the number of zero sets is
\[
 \frac{n}{k}\binom{n-k-1}{k-1}.
\]
Each zero set lifts to two binary words, giving \(V_{n,k}\). To count undirected token-slide edges, orient each move by the clockwise direction of its moving token, which selects exactly one orientation of every edge. Such a move is specified by a zero at one of \(n\) sites followed by at least two one sites. The remaining \(k-1\) zeros form an independent set in an ordinary path with \(n-4\) sites, yielding \(\binom{n-k-2}{k-1}\) choices. The same formula also holds by direct inspection for \(n=3,k=1\). Each token-slide edge has two lifted flip edges; this gives \(E_{n,k}\).

**Algorithm and component count.** Compute \(k\) for both inputs in \(O(n)\). If the words are identical, return the empty path. Otherwise, a path exists precisely when their common \(k\) is strictly between the two extreme levels. For such a level, route surplus tokens into one gap (at most \(O(kn)\) unit transfers), rotate the resulting canonical placement to the chosen origin (at most \(O(kn)\) slides), and if the reconstructed bit layer disagrees, use the displayed \(n\)-flip complement loop. Reverse the corresponding construction for the target. Thus a path of \(O(n^2)\) flips is constructive. Counting odd admissible \(k\) for odd \(n\), and positive even \(k<n/2\) plus isolated extremes for even \(n\), gives the stated component formula.

## Verification
The accompanying standalone `check.py` independently enumerates literal indexed binary words and tests all cyclic triples; builds Hamming-one edges directly; obtains every connected component by breadth-first search; and compares its sector label, size and edge count with the formulas. It passes every length \(3\le n\le18\), including degenerate frozen cases. For lengths through \(13\), a second enumeration over cycle-independent zero sets independently checks the gap-composition counts. These finite tests check implementation and boundary cases; they are not used to infer any infinite-length statement.

To replay: `python3 check.py --max-n 18` (standard-library Python only).

## Relationship to prior work
Avis and Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (first submitted 2022-03-31), study independent-set token-slide reconfiguration. Their Proposition 14 constructs a length-\(n\) walk on an independent-token cycle as part of a girth argument. This establishes a closely related property of the **projected** token graph. The present claim concerns the different **two-to-one binary-difference lift**, including its component-merging monodromy, exact lifted component populations and edges, frozen states, and reachability algorithm; these are not statements of Proposition 14.

Mütze, *Combinatorial Gray codes—an updated survey*, arXiv:2202.01280 (first submitted 2022-02-02), Section 3.15 discusses factor-avoiding and circularly avoiding binary Gray codes, including one forbidden homogeneous pattern and certain constrained complements. The simultaneous avoidance of both cyclic constant triples under one-coordinate reconfiguration and its invariant-sector classification are different from the surveyed Hamilton-listing results. The broad literature on reconfiguration of local constraints may contain equivalent reformulations that remain to be compared by an independent specialist.

## Limitations
The theorem does not classify graph diameters, Hamiltonian paths or cycles **within** nontrivial components, and it does not assert connectivity across different values of \(k\). It treats indexed cyclic words, not linear words, and it proves no corresponding result for alphabets larger than two. Prior-art searching and self-review cannot establish historical priority or independent certification.

## References
- D. Avis and D. A. Hoang, “On Reconfiguration Graphs of Independent Sets under Token Sliding,” arXiv:2203.16861, first submitted 2022-03-31. https://arxiv.org/html/2203.16861v3
- T. Mütze, “Combinatorial Gray codes—an updated survey,” arXiv:2202.01280, first submitted 2022-02-02. https://arxiv.org/abs/2202.01280
- S. Fujii, Y. Iwamasa, K. Kimura and A. Suzuki, “Algorithms for Coloring Reconfiguration Under Recolorability Digraphs,” LIPIcs ISAAC 2022, doi:10.4230/LIPIcs.ISAAC.2022.4. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ISAAC.2022.4
