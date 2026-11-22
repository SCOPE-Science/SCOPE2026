# Sharp token-slide freeze-out for minimum zero forcing on equal-arm theta graphs

## Finding

Let \(\Theta_\ell\), for an integer \(\ell\ge 3\), consist of two distinct terminals \(u,v\) joined by three internally vertex-disjoint paths of length \(\ell\). Write their internal vertices \(x_i^1,\ldots,x_i^{\ell-1}\) in order from \(u\) to \(v\), where \(i\in\{1,2,3\}\).

The minimum ordinary zero-forcing sets of \(\Theta_\ell\) are **exactly** these two disjoint classes:

- **Terminal class:** \(\{h,x_i^a,x_j^b\}\), where \(h\in\{u,v\}\), \(i\ne j\), \(a,b\in\{1,\ell-1\}\), and at least one of \(a,b\) denotes a neighbor of \(h\).
- **Interior class:** \(\{x_i^k,x_i^{k+1},x_j^e\}\), where \(i\ne j\), \(1\le k\le\ell-2\), and \(e\in\{1,\ell-1\}\).

In particular, \(Z(\Theta_\ell)=3\), and the number of distinct labelled minimum zero-forcing sets is exactly \(12\ell-6\). Let \(\mathcal J_\ell\) join two minima if they differ by replacing one selected vertex by any unselected vertex; let \(\mathcal S_\ell\) impose the additional requirement that the replaced vertices be adjacent in \(\Theta_\ell\). Then \(\mathcal J_\ell\) is connected for every \(\ell\ge3\), whereas

\[
\mathcal S_\ell\cong
\begin{cases}
3C_{10},&\ell=3,\\
(12\ell-6)K_1,&\ell\ge4.
\end{cases}
\]

Hence one additional subdivision per arm (from length three to four) destroys **all** legal optimum-preserving token slides without destroying connectivity under unrestricted single-token exchanges.

## Assumptions and scope

All graphs are finite, simple and undirected. Ordinary zero forcing starts from a blue vertex set. A blue vertex with exactly one white neighbor may recolor that neighbor blue; a zero-forcing set eventually colors the whole graph. An optimum is a set of minimum cardinality. The endpoint restriction \(\ell\ge3\) is essential for the stated enumerator and slide dichotomy; the length-two graph is not included. The two reconfiguration relations operate only among optima, not through intermediate larger sets.

For clarity, in the terminal class, the neighbor of \(u\) on arm \(i\) is \(x_i^1\), and the neighbor of \(v\) is \(x_i^{\ell-1}\). Each terminal-class set has internal vertices on two different arms. The interior class has exactly two consecutive selected vertices on one arm and exactly one extreme internal vertex on another arm.

## Proof

**1. Three initial blue vertices are necessary.** With at most two initially blue vertices, the first force requires an adjacent pair containing an internal vertex, because the terminals have degree three and all internal vertices have degree two. If the pair consists of a terminal and its adjacent internal vertex, forcing can fill that arm and reach the opposite terminal, but the other two arms remain uncolored: both terminals retain two white neighbors. If the pair consists of consecutive internal vertices on one arm, propagation can fill that arm toward both terminals, with the same obstruction on the remaining two arms. Nonadjacent initial vertices make no first force. Thus \(Z(\Theta_\ell)\ge3\).

**2. Classification with a terminal selected.** Two selected terminals and one internal vertex cannot force both unused arms: a possible initial force can fill at most the arm containing the selected internal vertex, after which neither terminal has a unique white neighbor. Suppose exactly one terminal, say \(u\), is initially blue. If both other selected vertices lie on one arm, the other two arms likewise remain uncolored. Thus they lie on distinct arms. At least one must be at the position \(1\), or no force is initially possible. A seed at position \(1\) can propagate along its arm to color \(v\). Unless the other initial internal seed is at position \(1\) or \(\ell-1\), the other seed has two white neighbors, while each terminal retains two white neighbors; forcing halts before the other two arms are colored. Conversely, if the other seed is at position \(1\), the terminal \(u\) can immediately force the third arm. If it is at position \(\ell-1\), then, after the first arm reaches \(v\), the second arm can propagate back toward \(u\) and the third arm can be forced from a terminal. Both patterns succeed. The \(v\)-case is symmetric. This proves the terminal class.

**3. Classification without a terminal.** A first force requires two consecutive internal seeds on one arm. If all three initial seeds are on this arm, the two unoccupied arms cannot be entered after the first arm is filled. Therefore the third seed is on another arm. The consecutive pair can propagate in both directions, eventually coloring \(u\) and \(v\). If the third seed is neither the first nor the last internal vertex of its arm, then it retains two white neighbors, while each terminal retains two white neighbors; the process is stuck. If instead the third seed is adjacent to \(u\) or \(v\), the corresponding terminal eventually sees two blue neighboring arms, can force the remaining arm, and the seeded second arm can complete from its selected endpoint. Thus exactly the interior class succeeds.

**4. Count.** Choose a terminal in two ways and an unordered arm pair in three ways. On each pair there are exactly three permitted endpoint-position patterns, giving \(2\cdot3\cdot3=18\) terminal-class sets. Choose the arm of the consecutive pair in three ways, the other arm in two ways, the adjacent position in \(\ell-2\) ways, and its extreme seed in two ways; this gives \(12(\ell-2)\) interior-class sets. The classes are disjoint. Their sum is \(12\ell-6\).

**5. All one-token exchanges connect.** Within the terminal class with terminal \(u\), every set is one exchange from a set \(\{u,x_i^1,x_j^1\}\); the three such pairs form a connected triangle of exchanges. Hence all terminal-class sets containing \(u\) are connected. The same holds for \(v\). An interior set \(\{x_i^k,x_i^{k+1},x_j^e\}\) can change its consecutive pair from positions \((k,k+1)\) to \((k-1,k)\) by one exchange whenever \(k>1\), and repeat until the pair is at \((1,2)\). Replacing \(x_i^2\) by \(u\) then reaches the terminal class. Moreover, fixing \(j\ne i\) and \(e=1\), this same chain connects \(\{u,x_i^1,x_j^1\}\) to \(\{v,x_i^{\ell-1},x_j^1\}\) by exchanging its leftmost internal vertex for \(v\) at the final pair. Thus the two terminal-class components and every interior set lie in one connected exchange graph.

**6. Adjacent-token slides.** For \(\ell\ge4\), moving an extreme selected internal vertex one step inward destroys its extremal position; moving a member of a consecutive internal pair one step either breaks its consecutiveness or replaces it by a terminal, leaving an internal vertex that is not extreme. Moving a terminal into an unoccupied arm produces selected vertices on three arms; moving it into an occupied arm cannot create the required consecutive pair unless the two extreme internal vertices on that arm are adjacent, which happens only when \(\ell=3\). Finally, moving an internal seed onto a terminal leaves either both terminals selected or two internal seeds on the same arm with a terminal. Checking these cases against the exhaustive classification of steps 2–3 shows that no adjacent move produces another optimum for \(\ell\ge4\).

For \(\ell=3\), each optimum occupies internal vertices from exactly two of the three arms. Every permitted adjacent slide preserves this unordered arm pair. Fixing a pair \(i,j\), its ten optima form the explicit slide cycle (subscripts denote positions):

\[
\begin{aligned}
&\{u,x_i^1,x_j^1\},\ \{u,x_i^2,x_j^1\},\ \{x_i^1,x_i^2,x_j^1\},\\
&\{x_i^1,x_i^2,x_j^2\},\ \{v,x_i^1,x_j^2\},\ \{v,x_i^2,x_j^2\},\\
&\{v,x_i^2,x_j^1\},\ \{x_i^2,x_j^1,x_j^2\},\\
&\{x_i^1,x_j^1,x_j^2\},\ \{u,x_i^1,x_j^2\},
\end{aligned}
\]

followed by the starting set. Each successive step (including the last) slides along one original edge. The classification shows that the listed ten configurations exhaust this arm-pair class and each has precisely the two displayed legal slides. There are three choices of arm pair, proving \(\mathcal S_3\cong3C_{10}\).

## Verification

The self-contained script `verify_theta.py` builds the theta graph directly, computes zero-forcing closures without relying on the classification, enumerates every triple and every pair for path lengths \(3\) through \(12\), and independently builds both one-token reconfiguration graphs. It checks exact agreement with both classified families, \(Z=3\), the count \(12\ell-6\), connectivity under unrestricted exchanges, and the slide component sizes. It reports `VERIFY_OK` on completion. The exhaustive experiment verifies only the listed finite lengths; the all-length theorem follows from the case analysis above.

## Relationship to prior work

Geneson, Haas and Hogben (arXiv:2009.00220, first posted 2020-09-01) initiate token-jump reconfiguration of minimum zero-forcing sets and classify familiar base graphs, including paths and cycles; they do not provide the equal-arm theta census or the slide freeze-out. Alishahi, Rezaei-Sani and Sharifi (arXiv:1903.08614, first posted 2019-03-20; Discrete Applied Mathematics 284, 2020) establish general maximum-degree-three structural criteria for zero-forcing number three. The value \(Z=3\) here is not asserted as novel. Bong and collaborators (arXiv:2205.09668, first posted 2022-05-19) study token addition/removal for zero forcing, not the present minimum-basis sliding classification.

The contribution assessed here is the complete equality-case enumeration and the connected-exchange/frozen-slide transition for the symmetric family, not the previously known existence of a three-vertex forcing set. Comparisons with indexed results concerning other theta-graph metrics and zero-forcing reconfiguration of ladders are non-implications because their graph families or feasibility predicates differ.

## Limitations

The theorem assumes three internally disjoint paths of the same length at least three. It does not classify every minimum set for unequal arms, positive semidefinite zero forcing, or reconfiguration through nonminimum sets. Indexed comparisons and accessible primary text do not certify full publication priority; independent mathematical assessment has not been performed.

## References

1. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020), https://arxiv.org/abs/2009.00220 .
2. M. Alishahi, E. Rezaei-Sani and E. Sharifi, *Maximum nullity and zero forcing number on graphs with maximum degree at most three*, Discrete Applied Mathematics **284** (2020), 179–194, https://arxiv.org/abs/1903.08614 .
3. N. H. Bong, J. Carlson, B. Curtis, R. Haas and L. Hogben, *Isomorphisms and properties of TAR reconfiguration graphs for zero forcing and other X-set parameters*, arXiv:2205.09668 (2022), https://arxiv.org/abs/2205.09668 .
