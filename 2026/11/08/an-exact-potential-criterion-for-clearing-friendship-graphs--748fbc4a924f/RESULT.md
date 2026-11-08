# An exact potential criterion for clearing friendship graphs

## Finding
For each integer \(m\geq 1\), let \(F_m=K_1\vee(mK_2)\) be the friendship graph: its common vertex is \(o\), and its \(m\) paired outer edges have endpoints \(a_i,b_i\), \(1\leq i\leq m\). A pebbling move removes two pebbles from one vertex and places one on an adjacent vertex; a configuration is *clearable* if such moves can leave exactly one pebble in the whole graph. Write \(c\) for the number of pebbles at \(o\), and \(x_i,y_i\) for the two outer counts of blade \(i\).

Define the defect function \(q:\mathbb{Z}_{\geq0}^2\to\{0,1,2,3,4\}\) by the following disjoint cases, evaluated in the listed order:

\[
q(x,y)=\begin{cases}
4,&(x,y)=(1,1),\\
0,&x,y\text{ are both even},\\
1,&x,y>0\text{ and }x+y\text{ is odd},\\
2,&x,y\text{ are both odd},\\
3,&\min(x,y)=0\text{ and }x+y\text{ is odd}.
\end{cases}
\]

Put \(w(x,y)=(x+y-q(x,y))/2\) and
\[
\Phi(c;x_1,y_1,\ldots,x_m,y_m)=c+\sum_{i=1}^{m}w(x_i,y_i).
\]

**Exact reachability theorem.** For every nonnegative integral configuration on \(F_m\), a configuration of size one is already clear. For every configuration of size at least two, it is clearable **if and only if** \(\Phi\geq1\) and the configuration is not exactly three pebbles at \(o\), with all outer vertices empty. Thus the test consists of \(m\) independent constant-time evaluations and one exception test; its arithmetic operation count is \(O(m)\).

**Sharp threshold and critical obstructions.** For all \(m\geq1\),
\[
\operatorname{clear}(F_m)=4m.
\]
For every \(m\geq2\), exactly \(2m\) labelled configurations of size \(4m-1\) are not clearable. These are precisely the configurations with zero pebbles at \(o\), exactly \(2m+1\) pebbles at one chosen outer vertex, none at its partner, and one pebble at each of the other \(2m-2\) outer vertices. In particular they form a single automorphism orbit. The \(m=1\) case recovers the known value \(\operatorname{clear}(K_3)=4\), and is not claimed as a new graph-family instance.

## Assumptions and scope
All graphs are finite and simple. Pebbles are indistinguishable, counts are nonnegative integers, the direction of any legal pebbling move is unrestricted, and success means *exactly one pebble in total*, at any vertex. No pebbles may be discarded except by legal moves. The critical count \(2m\) refers to configurations on labelled vertices, not to orbits. The new infinite-family assertion concerns \(m\geq2\); formulas and the reachability theorem also hold at \(m=1\).

## Proof
**1. A move-monotone potential.** The defect table is exhaustive: parity gives the first four nonexceptional possibilities, and the special pair \((1,1)\) is separated from the ordinary odd–odd case. In particular, \(q\in\{0,1,2,3,4\}\), and \(q=4\) holds precisely at \((1,1)\). Directly from this five-case table, for all \(x,y\geq0\), the following inequalities hold whenever the indicated move exists:
\[
\begin{aligned}
q(x-2,y)&\geq q(x,y)&&\text{if }x\geq2,\\
q(x-2,y+1)&\geq q(x,y)-1&&\text{if }x\geq2,\\
q(x+1,y)&\geq q(x,y)-3.&&
\end{aligned}
\tag{1}
\]
The same statements hold after exchanging \(x\) and \(y\). For transparency, the smallest possible new defect in the three lines of (1), as the old defect runs through \(0,1,2,3,4\), is respectively \((0,1,2,3,\text{inapplicable})\), \((1,0,1,2,\text{inapplicable})\), and \((1,0,1,0,1)\). These five-entry checks follow simply by considering parity, whether a coordinate is zero, and the exceptional pair \((1,1)\); the defect is unchanged when two are added to a coordinate already at least two (equivalently, \(w\) increases by one), so no unbounded case is omitted.

If an outer vertex sends a pebble to the common vertex, the resulting change in \(\Phi\) is \((q_{\rm old}-q_{\rm new})/2\). If an outer vertex sends a pebble to its partner, it is \((q_{\rm old}-q_{\rm new}-1)/2\). If \(o\) sends a pebble to an outer vertex, it is \((q_{\rm old}-q_{\rm new}-3)/2\). The three inequalities (1) therefore prove that **\(\Phi\) never increases under a legal move**.

A clearable configuration of size at least two must reach a configuration of size two and then make one last move. Before that last move, exactly two pebbles are at one vertex: its potential is \(2\) if that vertex is \(o\), and \(1\) if it is outer. Monotonicity consequently forces \(\Phi\geq1\) in every clearable initial configuration of size at least two. Moreover, three pebbles concentrated at \(o\) cannot clear: the only first move leaves one pebble at \(o\) and one at an outer vertex, with no further move possible.

**2. Exact extraction from outer pairs.** The same function \(w\) describes an attainable net transfer to the common vertex when clearing an outer pair. The following explicit procedures suffice, and each is confined to one triangular blade.

If both outer counts are even, send every possible pair directly to \(o\); the hub gains \((x+y)/2=w(x,y)\). If one count is odd and the other is a positive even integer, send a pair from the even count to the odd count. Both become even, and direct transfers to \(o\) yield \(\lfloor(x+y)/2\rfloor=w(x,y)\) hub pebbles. If both counts are odd but not \((1,1)\), some count is at least three. Send two pebbles from that vertex to its partner, obtaining the previous mixed-parity case and net gain \((x+y)/2-1=w(x,y)\).

If a blade has \((2k+1,0)\), with \(k\geq2\), send \(k\) pairs to \(o\), leaving one pebble outside and gaining \(k\) at \(o\). Send one pair back from \(o\) to that outer vertex and then one pair from that vertex to \(o\); the blade is empty and its net hub gain is \(k-1=w(2k+1,0)\). This procedure starts with no hub pebbles.

Three remaining nonempty types require a hub reserve. For \((3,0)\), starting with at least one hub pebble, send a pair to the hub, then one back to the remaining outer pebble, and finally the resulting outer pair to the hub; net hub change zero, agreeing with \(w(3,0)=0\). For \((1,0)\), starting with at least two hub pebbles, send one hub pair to the occupied outer vertex and its new pair back; the hub loses one, agreeing with \(w(1,0)=-1\). For \((1,1)\), starting with at least two hub pebbles, send a hub pair to one outer vertex, that outer pair to its partner, and the resulting pair from the partner to the hub; again the net hub change is minus one. The empty pair does nothing. The symmetric orientations of these cases are identical.

Call all blades in the first four procedures *free*, and let \(k\) count blades of type \((1,0)\) or \((1,1)\), up to swapping endpoints. Every free nonempty blade has \(w\geq1\). Perform all free extractions first. Then perform all neutral \((3,0)\) extractions, and finally the \(k\) negative extractions. If initial \(\Phi\geq1\), the hub reserve just before the negative extractions equals \(\Phi+k\geq k+1\); it is also at least one before the neutral procedures. Each negative extraction starts with at least two hub pebbles. The construction therefore terminates with **all pebbles at \(o\)** and exactly \(\Phi\) of them. This proves a constructive exact extraction statement for every configuration with \(\Phi\geq1\).

**3. Removing the exceptional central stack of size three.** A central stack of size one is already clear; one of size two clears in one move. Every central stack of size at least four also clears. To see this, work inside any triangle containing \(o\): stacks of sizes four, five, and six have explicit reductions to one pebble. For four, move twice from \(o\) to one neighbor and once back. For five, make those three moves and one more move from \(o\) to that neighbor. For six, send two pairs from \(o\) to one neighbor, one pair from \(o\) to the other, then one pair from the first neighbor to the second and a pair from the second back to \(o\). For any larger stack, the first three moves in the four-pebble construction reduce the central stack size by three; induction completes the argument.

It remains to treat an initial configuration with \(\Phi=3\) that is not the pure three-pebble stack at \(o\). We give an explicit way to lower its potential to one or two without falling below one. If some blade is free and nonempty, the following preparatory operations preserve \(\Phi\) until a final move lowers it by one or two:

For an even–even positive pair, send a pair from an even occupied vertex to its partner; the potential drops by one if the source had at least four pebbles and by two if it had exactly two. For a mixed-parity pair with a positive even count, repeatedly send pairs from that even count to \(o\) until it is two, and send its last pair to \(o\); the last move lowers \(\Phi\) by one. For a nonexceptional odd–odd pair, first send a pair from an odd count of at least three to its partner, giving the preceding mixed-parity case while preserving \(\Phi\). For a pair \((2k+1,0)\) with \(k\geq2\), send two pairs successively from the odd count to its partner; this yields a mixed-parity pair with one positive even count, without changing \(\Phi\), so the preceding operation applies.

If no free nonempty blade exists but a \((3,0)\) blade exists, send one of its outer pairs to its outer partner. This turns it into \((1,1)\) and lowers \(\Phi\) by one. Finally, if every nonempty blade is of negative type, let \(k\geq1\) be their number. Then \(\Phi=3\) forces at least \(k+3\geq4\) pebbles at \(o\). On a \((1,0)\) blade, one move from \(o\) to its empty outer vertex lowers \(\Phi\) by two. On a \((1,1)\) blade, two moves from \(o\) to the same outer vertex turn the pair into \((3,1)\) and lower \(\Phi\) by two. If no nonempty blade at all exists, the configuration is precisely the excluded three-pebble stack. In every other case the resulting potential is one or two. Apply the extraction procedure of step 2, and finish clearing the central stack. This proves the if direction and the complete reachability criterion.

**4. The sharp threshold and the exceptional orbit.** Put \(t=c+\sum_i(x_i+y_i)\). The defect identity gives
\[
2\Phi=t+c-\sum_{i=1}^m q(x_i,y_i).\tag{2}
\]
Since every defect is at most four, at total size \(t=4m\) the right-hand side is nonnegative. If it were zero, then \(c=0\) and every defect would equal four, forcing every outer pair to be \((1,1)\) and hence total size \(2m\), contrary to \(t=4m\). Thus integrality gives \(\Phi\geq1\). These configurations have size at least four, so none is the excluded three-pebble central stack. The reachability theorem clears all of them; the same argument clears every larger total size.

Now suppose \(m\geq2\) and \(t=4m-1\). An uncleared configuration cannot be the central three-stack. It therefore has \(\Phi\leq0\). Equation (2) implies \(c\leq1\). If \(c=1\), then \(\sum q\geq4m\), forcing every pair to equal \((1,1)\), but this would give \(t=2m+1\), not \(4m-1\). Thus \(c=0\). Because \(t\) is odd, \(\sum q\) is odd. With \(\sum q\leq4m\) and \(2\Phi\leq0\), it follows that \(\sum q=4m-1\). Exactly one blade must then have defect three, and all other blades defect four. Thus the other blades are \((1,1)\), the exceptional blade has one zero outer count and one odd outer count, and the total-size equation fixes that count as \(2m+1\). This configuration has \(\Phi=0\), so step 1 proves it is not clearable. There are exactly \(2m\) choices of the heavily loaded labelled outer vertex. Hence \(\operatorname{clear}(F_m)=4m\), and the critical census and uniqueness up to automorphism follow. For \(m=1\), the known complete-triangle value follows directly from steps 1–3.

## Verification
The accompanying `verify.py` independently enumerates all labelled pebble configurations through total sizes 11, 12, and 12 for \(m=1,2,3\), respectively, and computes clearability by exact directed reachability in the finite acyclic state graph of all pebbling moves. It compares every result to the potential criterion. It also checks the defect monotonicity and affine periodicity identities over a large integer test grid, and checks the explicit critical configurations through \(m=9\). Running `python3 verify.py` must finish with `VERIFY_OK`.

The complete theorem does not rely on finite enumeration: the five-case defect inequalities, explicit blade extraction sequences, and exceptional-stack argument prove it for every allowed integer parameter and configuration.

## Relationship to prior work
Csernák and Soukup introduced the undirected stacking and clearing parameters in *Stacking and Clearing in Graph Pebbling*, arXiv:2604.22341v1 (first publicly submitted April 24, 2026). The primary text establishes existence criteria, general bounds, and exact clearability thresholds on complete graphs and complete multipartite graphs. In particular, their \(\operatorname{clear}(K_3)=4\) includes \(m=1\) above. Friendship graphs with \(m\geq2\) are not complete multipartite: outer vertices from different blades are nonadjacent, but the two vertices of each blade are adjacent. The present exact potential, complete configuration criterion, sharp \(4m\) threshold, and critical orbit count do not follow from those stated complete-multipartite formulas.

Earlier work on the ordinary pebbling number, cover pebbling number, and edge pebbling of friendship graphs studies different reachability requirements. In particular, obtaining a pebble at a prescribed vertex or covering every vertex does not imply that every other pebble can be removed. Literature and public mathematical-record searches did not identify a theorem with the same full-configuration criterion. The priority comparison remains provisional, not a formal uniqueness certification.

## Limitations
The exact potential depends on the common-vertex triangle bouquet structure and does not automatically extend to triangular cactus graphs with multiple cut vertices, generalized windmills with larger blades, or arbitrary graphs. The formula concerns clearing, not the unrelated cover-pebbling/optimal-pebbling invariant. The finite verifier confirms finite instances only. No independent mathematical audit has been performed, and historical priority may change with additional source discovery.

## References
1. T. Csernák and L. Soukup, *Stacking and Clearing in Graph Pebbling*, arXiv:2604.22341v1, first public submission 2026-04-24, https://arxiv.org/abs/2604.22341 . Primary MSC2020: 05C57.
2. T. Csernák and L. Soukup, *Stacking and Clearing in Directed Graph Pebbling*, arXiv:2606.04659v1, 2026-06-03, https://arxiv.org/abs/2606.04659 . A directed-graph companion, not a theorem covering the present undirected family.
3. P. Paul and S. S. A. Fathima, *A Study on Edge Pebbling Number, Covering Cover Edge Pebbling Number of Friendship Graphs, Odd Path and Even Path*, Indian Journal of Science and Technology 16 (2023), 2480–2484, https://indjst.org/articles/a-study-on-edge-pebbling-number-covering-cover-edge-pebbling-number-of-friendship-graphs-odd-path-and-even-path . The definitions and targets differ from clearing.
