# An exact cycle-potential metric for sliding near-perfect bipartite matchings

## Finding
For every integer \(n\ge 2\), form the graph \(\mathcal R_n\) whose vertices are all matchings of cardinality \(n-1\) in the complete bipartite graph \(K_{n,n}\). Adjacent states differ by replacing one matching edge with another **sharing one endpoint** with it, while preserving the matching condition. This is the token-sliding rule in the line graph of \(K_{n,n}\), not unrestricted token jumping.

The distance between any two states is given by an exact formula in the cycles of a single permutation. Relabel the two sides independently so that the source state is \(S=\{(i,i):0\le i<n-1\}\), and put \(H=n-1\). Let \(h\) and \(c\) be the unique unmatched row and column of the target state \(T\). Complete the partial row-to-column matching bijection to a permutation \(\pi\in S_n\) by setting \(\pi(h)=c\). Denote by \(c(\pi)\) the number of permutation cycles, including fixed points, and by \(q_H(\pi)\) the number of nontrivial cycles *not containing* \(H\). Put \(\epsilon=1\) exactly if \(h\ne H\) and \(\pi(h)=h\), and otherwise put \(\epsilon=0\). Then

\[
\boxed{d_{\mathcal R_n}(S,T)=n-c(\pi)+2q_H(\pi)+2\epsilon.}
\]

Moreover, \(\mathcal R_n\) is connected, vertex-transitive and regular of degree \(2(n-1)\), with \(n^2(n-1)!\) vertices, and
\[
\boxed{\operatorname{diam}(\mathcal R_n)=\operatorname{rad}(\mathcal R_n)=\left\lfloor\frac{3n}{2}\right\rfloor-1.}
\]
The distance can be evaluated in \(O(n)\) operations after a relabelling of the source, and the proof yields a shortest sequence of slides in time polynomial in \(n\).

## Assumptions and scope
The two partite sets are labelled with \(\{0,\ldots,n-1\}\), and all matchings are *unlabelled sets of edges* (no identities assigned to individual matching tokens). A slide replaces one edge \((u,v)\) by \((u',v)\) or \((u,v')\), with the other incident vertices free and every intermediate state a matching of size \(n-1\). All graph edges are undirected and each slide has unit cost. The distinguished source matching can always be made canonical by separate row and column permutations. \(\pi\) depends on that relabelling, but the formula computes the invariant graph distance. This theorem concerns size \(n-1\), not the perfect-matching level or arbitrary smaller matching levels.

## Proof
**1. Exact move representation.** A state is uniquely a pair \((\pi,h)\), where \(\pi\) is a permutation of \(\{0,\ldots,n-1\}\) and the matching consists of \((i,\pi(i))\) for \(i\ne h\). Its unused column is \(\pi(h)\). For every \(r\ne h\) there are exactly two slides: replace \((r,\pi(r))\) by \((h,\pi(r))\), changing the hole to \(r\), or replace it by \((r,\pi(h))\), keeping the row-hole \(h\). In both cases the completed permutation changes to \(\pi\circ(h\ r)\), where the transposition exchanges the two specified arguments. The new hole is respectively \(r\) or \(h\). These choices are distinct and exhaust all legal moves.

**2. A unit-slope potential.** Fix the source \((\operatorname{id},H)\). Define
\[
\Phi(\pi,h)=n-c(\pi)+2q_H(\pi)+2\mathbf1_{\{h\ne H,\,\pi(h)=h\}}.
\]
Every move changes \(\Phi\) by exactly \(+1\) or \(-1\). Here is the cycle check. A transposition of arguments in *different* permutation cycles merges them, raising \(n-c(\pi)\) by one; comparing their lengths, whether the distinguished label \(H\) is present, and whether the current hole is a singleton shows that the quantity \(q_H+\epsilon\) changes by either zero or minus one. A transposition in the *same* cycle splits it, lowering \(n-c(\pi)\) by one; the same comparison shows that \(q_H+\epsilon\) changes by zero or plus one. To see the latter bounds explicitly: when a cycle not containing \(H\) splits into two, the changes in \(q_H\) are \(-1,0,1\) according as both pieces are singleton, one piece is singleton, or neither is; in the first case the new pivot is a fixed label away from \(H\), contributing one to \(\epsilon\), and in the middle case the new pivot contributes either zero or one. If the split cycle contains \(H\), the change in \(q_H\) is zero or one, and a fixed new pivot away from \(H\) can arise only when that change is zero. For a merge not containing \(H\), the change in \(q_H\) is one, zero, or minus one as both old cycles are singleton, exactly one is nontrivial, or both are nontrivial; the exceptional positive change is cancelled by loss of a fixed old pivot. For a merge containing \(H\), the change is zero or minus one, and any fixed old pivot contributes the compensating loss. Thus \(|\Delta\Phi|=1\). Since \(\Phi(\operatorname{id},H)=0\), every path to \((\pi,h)\) has length at least \(\Phi(\pi,h)\).

**3. A descending legal slide always exists.** Unless \((\pi,h)=(\operatorname{id},H)\), one of the following exhaustive cases supplies a slide that decreases \(\Phi\) by one.

- If \(h=H\) and \(H\) lies in a nontrivial cycle, swap the arguments \(h\) and \(r=\pi(h)\) and **keep** the hole at \(h\). This splits off the fixed label \(r\) while shortening the \(H\)-cycle.
- If \(h=H\), \(H\) is fixed, and another nontrivial cycle exists, choose \(r\) in that cycle, swap with \(h\), and **move** the hole to \(r\). The merger attaches the formerly fixed \(H\) to the nontrivial cycle, decreasing its contribution from its length plus one to its length.
- If \(h\ne H\) and \(h\) is fixed, swap with \(r=H\) and **move** the hole to \(H\). The former exceptional fixed-hole surcharge disappears and the cycle containing \(H\) grows by one (or becomes a transposition).
- If \(h\ne H\) and \(h\) is not fixed, take \(r=\pi^{-1}(h)\), swap with \(h\), and **move** the hole to \(r\). This splits \(h\) off as a fixed point; any residual cycle has one fewer element. If the old cycle was a transposition disjoint from \(H\), the new hole is fixed and its surcharge replaces two of the three removed cycle units.

The first two cases include all states with \(h=H\) except the source; the last two include all with \(h\ne H\). Repeating this descent gives exactly \(\Phi\) slides to the source. Reverse that sequence to reach the target. Combining with the lower bound proves the distance formula for every \(n\ge2\).

**4. Counting and diameter.** There are \(n\) choices of free row, \(n\) choices of free column and \((n-1)!\) bijections between the remaining labels. Every state admits two distinct slides for each of its \(n-1\) matched edges. Independent relabellings of the two sides act transitively, so radius and diameter coincide.

Let the cycle of \(\pi\) containing \(H\) have length \(s\ge1\), let the other nontrivial cycles have total length \(L\) and number \(t\), and let \(f=n-s-L\) count other fixed points. Then \(t\le\lfloor L/2\rfloor\), and the formula becomes \(\Phi=s-1+L+t+2\epsilon\). If \(\epsilon=0\), \(\Phi\le s-1+3(n-s)/2\le3(n-1)/2\). If \(\epsilon=1\), then \(f\ge1\), whence \(\Phi\le s+1+3(n-s-1)/2\le3n/2-1\). After taking integer parts, both bounds are at most \(\lfloor3n/2\rfloor-1\). To attain the bound when \(n\) is odd, take \(h=H\), fix \(H\), and make the other \(n-1\) symbols a product of disjoint transpositions. When \(n\) is even, fix two distinct labels \(H,h\), use \(h\) as the target hole, and pair all other \(n-2\) labels into transpositions. Their potentials are respectively \(3(n-1)/2\) and \(2+3(n-2)/2\), completing the diameter proof.

## Verification
Run `python check_formula.py` to enumerate the reconfiguration graph by a breadth-first search from its canonical state for all \(2\le n\le8\). It verifies the derived distance, all transitions, state counts, degree and diameter. Run `python check_direct.py` from the same directory to independently enumerate sets of \(n-1\) disjoint bipartite edges and legal edge slides for \(2\le n\le5\), independently reconstruct the graph and check the metric. The direct checker imports only the evaluated formula from the first file, not its state enumeration, transition or graph-search code. The supporting run outputs are `formula_run.txt` and `direct_run.txt`. The calculations are finite corroboration; Steps 1–4 establish the theorem for all orders.

## Relationship to prior work
Bonsma, Kamiński and Wrochna (arXiv:1403.0359v1, March 3, 2014) study reachability of independent sets by token sliding in claw-free graphs, which include line graphs. Their full text gives general reachability algorithms but not the present explicit all-pairs distance or diameter for the near-perfect matching layer of complete bicliques. Bousquet, Hatanaka, Ito and Mühlenthaler (arXiv:1812.05419, December 13, 2018) establish exact general results for **token jumping**, and in their Lemma 5 show that nonmaximal matching instances have jumping distance equal to the number of changed matching edges or one more. Their main operation is expressly different from the adjacent-edge slides here; for example, disjoint transpositions in the current theorem incur an additional per-cycle sliding cost. The 2015 study *Swapping labeled tokens on graphs* concerns vertex-token permutations on complete bipartite graphs, not the matching-edge states considered here. None of these inspected statements implies the formula or diameter. Unindexed equivalent formulations remain possible and independent priority assessment is outstanding.

## Limitations
The result does not give analogous formulas for smaller matching cardinalities, other underlying bipartite graphs, token jumping, or vertex-token swapping. No claim is made about new complexity-class consequences. Finite program outputs by themselves are not proofs of the infinite statement. Literature priority remains subject to independent review.

## References
1. P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (public March 3, 2014), https://arxiv.org/html/1403.0359v1.
2. N. Bousquet, T. Hatanaka, T. Ito, M. Mühlenthaler, *Shortest Reconfiguration of Matchings*, arXiv:1812.05419 (public December 13, 2018), https://arxiv.org/abs/1812.05419.
3. M. Kamiński, P. Medvedev, M. Milanič, *Complexity of independent set reconfigurability problems*, Theoretical Computer Science 439 (2012), 9–15, doi:10.1016/j.tcs.2012.03.004.
4. K. Yamanaka et al., *Swapping labeled tokens on graphs*, Theoretical Computer Science (2015), doi:10.1016/j.tcs.2015.01.052; https://hdl.handle.net/1721.1/134490.
