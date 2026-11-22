# Sharp cyclic covering length for class-alternating words

## Finding
Let \(A\) and \(B\) be disjoint nonempty finite alphabets of cardinalities \(a\) and \(b\). For \(n\ge2\), let \(M_{a,b}(n)\) denote the least length of a nonempty circular word that alternates between \(A\) and \(B\) at every cyclic adjacency and has **every** alternating word of length \(n\), beginning in either alphabet, as a cyclic factor. Then

\[
M_{a,b}(n)=\begin{cases}
2(ab)^{n/2},&n\text{ even},\\
2(ab)^{(n-1)/2}\max\{a,b\},&n\text{ odd}.
\end{cases}
\]

In particular, for odd \(n=2r+1\), the precise minimum excess above the number \((ab)^r(a+b)\) of distinct required factors is \((ab)^r|a-b|\). If \(a>b\), one optimal cover is obtained by using every required length-\(n\) factor once and each factor starting and ending in the same symbol of \(B\) an **additional** \(a-b\) times. If \(b>a\), interchange the roles of \(A\) and \(B\). These multiplicities are sufficient to realize a single circular alternating word, not merely a collection of cycles.

## Assumptions and scope
Alphabets are labeled, nonempty, disjoint and finite. All words and circular positions are indexed by symbols, not by equivalence classes under rotation; only the covering host is considered circular. Every adjacent pair of the host, including its final-to-initial pair, has one symbol from each alphabet. The required set includes both kinds of initial symbol, even when \(n\) is odd. Covers may contain a factor more than once. The minimum is among single nonempty circular hosts, not unrestricted strings or a family of circles. The statement includes \(a=1\), \(b=1\), and \(n=2\).

## Proof
Define the order-\(n\) alternating overlap digraph \(G\). Its vertices are all alternating words of length \(n-1\); each alternating length-\(n\) word \(x_1\cdots x_n\) is a directed edge from \(x_1\cdots x_{n-1}\) to \(x_2\cdots x_n\). Thus a circular alternating host determines a closed directed edge walk in \(G\), whose edge multiplicity records the full multiset of its cyclic length-\(n\) factors. Conversely, the first symbols of an Euler circuit in an edge-multiplicity expansion of \(G\) give such a host. This correspondence remains valid at \(n=2\), where vertices are single letters.

The digraph \(G\) is strongly connected: from any vertex, append any alternating continuation long enough to incorporate the prescribed letters of a target vertex in the desired starting class (a single placeholder symbol can adjust the parity), and shift until the target vertex is reached. Since each alphabet is nonempty, every required intermediate edge exists.

If \(n=2r\) is even, the vertices have odd length and begin and end in the same alphabet. At any vertex the incoming and outgoing degrees both equal the cardinality of the opposite alphabet. Hence \(G\) is balanced, and strong connectivity gives an Euler circuit using each required edge once. There are \(2(ab)^r\) required edges. This is also a lower bound on the number of cyclic windows and hence on host length.

Suppose now that \(n=2r+1\) is odd, where \(r\ge1\). Vertices have even length \(2r\). Each vertex beginning in \(A\) and ending in \(B\) has outdegree \(a\) and indegree \(b\); each vertex beginning in \(B\) and ending in \(A\) has outdegree \(b\) and indegree \(a\). There are exactly \((ab)^r\) vertices of each type. Assume \(a>b\). The mandatory single copy of every edge leaves an outgoing-degree deficit \(a-b\) at each \(B\)-first vertex and an incoming-degree deficit \(a-b\) at each \(A\)-first vertex. Every additional edge occurrence increases total outgoing degree among \(B\)-first vertices by at most one. Therefore any balanced closed covering walk needs at least \((ab)^r(a-b)\) additional edges beyond the \((ab)^r(a+b)\) mandatory edges. The same lower bound, with signs exchanged, holds for \(b>a\).

For \(a>b\), for every \(B\)-first vertex \(v=v_1\cdots v_{2r}\) append \(v_1\in B\), thereby duplicating the existing edge \(v_1\cdots v_{2r}v_1\) exactly \(a-b\) additional times. This moves from \(v\) to the \(A\)-first vertex \(T(v)=v_2\cdots v_{2r}v_1\). Rotation \(T\) is a bijection between the two classes of vertices: its inverse is the right rotation. Consequently every outgoing-degree deficit at a \(B\)-first vertex and every incoming-degree deficit at an \(A\)-first vertex is met exactly. The expanded directed multigraph is balanced and remains strongly connected because it retains every original edge. It therefore possesses an Euler circuit. Its cyclic edge labels produce a single alternating cover of length

\[
(ab)^r(a+b)+(ab)^r(a-b)=2a(ab)^r.
\]

If \(b>a\), duplicate the edges obtained by appending the first \(A\)-symbol to each \(A\)-first vertex, each \(b-a\) additional times. If \(a=b\), no extra edge is needed. This proves the odd formula and the claimed explicit factor multiplicities.

## Verification
A standalone Python 3 script `verify.py` constructs the exact mandatory edge multiset and prescribed additional edges, independently checks the balanced in/out degrees, runs an Euler circuit, reads its cyclic length-\(n\) windows, checks the full factor multiset and the claimed length, and confirms coverage. It has no nonstandard dependencies. Run `python3 verify.py` from the directory containing the script. It checks 80 alphabet-size/window-length parameter families (sizes one through four, lengths two through six within its 20,000-position cap) and independently rules out every shorter alternating circular host by exhaustive enumeration in eight selected small families. Observed output: `VERIFY_OK: 80 constructive tour families and 8 exact exhaustive shorter-cover obstructions`. These finite checks are not the proof for unbounded parameters; the degree bound and Eulerian construction above are.

## Relationship to prior work
Champlin, Godbole and Tomlinson (2013, Theorem 4) proved the existence of a class-alternating universal cycle in the balanced cases (even length, or odd length with equal alphabet sizes), using the same underlying overlap-graph degree obstruction. They did not state or prove the shortest repeated-factor covering length for the imbalanced odd case. The present result credits their graph and obstruction and gives an exact optimized Eulerization, including the minimal surplus and a fully explicit duplicate-edge scheme. Kreitzer, Nica and Pereira (2023, Definitions 4–6, Theorem 3 and Corollary 1) introduced an *asymmetric* alternating de Bruijn sequence: an odd-length window starting and ending in one designated alphabet must appear once, but windows starting in the other alphabet need not all appear. Their construction has a related length, but its covering requirement is strictly weaker; their Example 6 explicitly omits a window of the opposite starting type. Later papers on restricted-word and run-limited cyclic covers use different permitted factor languages, so their stated formulas do not specialize to the all-orientation, unequal-alphabet problem.

## Limitations
The exact formula concerns single cyclic hosts required to alternate at every cyclic adjacency. It does not characterize the number of optimal cyclic hosts, their rotational equivalence classes, or optimal *linear* superstrings in which forbidden factors may appear. It does not assert a new existence result for the previously covered balanced universal-cycle cases. Search-based originality comparison cannot exclude all unindexed equivalent results. No independent external mathematical validation has been performed.

## References
1. M. Champlin, A. Godbole, B. Tomlinson, *Universal Cycles of Complementary Classes*, 2013, arXiv:1303.3323 (public version March 14, 2013), https://arxiv.org/abs/1303.3323 .
2. M. Kreitzer, M. Nica, R. Pereira, *Using alternating de Bruijn sequences to construct de Bruijn tori*, 2023, arXiv:2306.01498, https://arxiv.org/abs/2306.01498 .
