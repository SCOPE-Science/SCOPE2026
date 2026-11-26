# Token-jump reconfiguration lifts for clique coronas

## Finding

Let \(G\) be a finite connected simple graph on \(n\ge2\) vertices and let \(r\ge2\). Form \(H=G\odot K_r\) by attaching a private \(r\)-clique \(C_v\) to each root \(v\). Write \(z=Z(G)\) for the classical zero-forcing number and \(b(G)\) for the number of minimum zero-forcing sets. Write \(\mathcal R(X)\) for the graph of minimum zero-forcing sets of \(X\), with adjacency given by exchanging one chosen vertex for one unchosen vertex.

There is a natural projection of vertex sets \(\pi:V(\mathcal R(H))\to V(\mathcal R(G))\). It sends each corona minimum set to its active roots: those selected or having a fully selected private clique. Edges within a fiber are contracted by the projection, and every other edge projects to an edge of \(\mathcal R(G)\).

The induced fiber over each base minimum set \(B\) is
\[
\mathcal R(H)[\pi^{-1}(B)]\cong
\left(\mathop{\square}_{v\in B}K_{r+1}\right)\square
\left(\mathop{\square}_{v\notin B}K_r\right).
\]
In particular its size is \(q=r^{n-z}(r+1)^z\). Each base edge has exactly \(c=4r^{n-z+1}(r+1)^{z-1}\) edges between the corresponding fibers; no edges lie between nonadjacent distinct fibers. Consequently the connected components correspond bijectively under \(\pi\), and each corona component has exactly \(q\) times the size of its base component. The edge count is
\[
|E(\mathcal R(H))|=\tfrac12 b(G)q\bigl(zr+(n-z)(r-1)\bigr)+c|E(\mathcal R(G))|.
\]

## Assumptions and scope

In classical zero forcing a selected vertex is initially black. A black vertex with a unique white neighbor may turn it black; the set is zero forcing if there is a sequence that turns the whole graph black. Minimum means minimum cardinality, not inclusion-minimal. Reconfiguration is by token jumping, not token sliding. The result concerns uniform complete attachments of size at least two.

## Proof

**Forcing-set input (known).** The clique-decoration criterion of [1,2] says that a set \(S\) forces the corona exactly when it includes at least \(r-1\) vertices from each \(C_v\) and \(B(S)=\{v:v\in S\text{ or }C_v\subseteq S\}\) forces \(G\). Indeed, two white vertices of \(C_v\) block any force into that pair. With at most one private white vertex, any \(v\notin B(S)\) must first be turned black by another root: its private white vertex cannot be forced while both it and its root are white. Starting from \(B(S)\) in \(G\), retain in order only root-to-root forces with targets outside \(B(S)\); each retained force is valid, since the base process has at least all roots that were black at that step in the corona and its retained target is still white. Conversely, first turn each root of \(B(S)\) black (using its private clique when needed), then follow a forcing chronology on \(G\). A black root's last private white vertex can be forced by a black clique vertex before any outgoing root force. This is possible because \(r\ge2\). The chronology then extends to all of \(H\).

Each block \(C_v\cup\{v\}\) contributes at least \(r\) selected vertices if active and at least \(r-1\) otherwise. It follows from the criterion that \(|S|\ge n(r-1)+Z(G)\), with equality achieved by taking a minimum \(B\) in \(G\) and choosing any \(r\) of \(C_v\cup\{v\}\) for \(v\in B\), and any \(r-1\) of \(C_v\) otherwise. Equality requires just these local choices and a minimum projected set \(B\). Thus the input minimum-family characterization and count \(b(G)q\) follow from [1,2]; neither they nor the previously known numerical zero-forcing formula [3] are asserted as new here.

**Reconfiguration.** In a fixed fiber a jump must stay in one block, since all block occupancies are fixed. Any two distinct local minima of the same type differ by a jump: the active patterns are complements of singletons in \(C_v\cup\{v\}\) and the inactive ones are complements of singletons in \(C_v\). This proves the Cartesian product and connectedness of each fiber.

In a move between distinct fibers, exactly one block loses a token and one gains a token. Thus for some \(v\in B\), \(w\notin B\), the new set of active roots is \(B'=B\setminus\{v\}\cup\{w\}\). Fix the local choices at the other blocks; they contribute \((r+1)^{z-1}r^{n-z-1}\) possibilities. At the losing block, each inactive configuration \(C_v\setminus\{j\}\) is contained in two active configurations, obtained by adding \(j\) or \(v\). Thus there are \(2r\) ordered choices of the configurations at that block, and independently \(2r\) at the gaining block by the reversed relation. Every combination gives a distinct crossing edge, counted once with its endpoint over \(B\) first. Multiplying gives \(c\). Since no other pair of fibers is linked and every base edge has a lift, the connected fibers give exactly the asserted component correspondence. Each fiber is regular of degree \(zr+(n-z)(r-1)\); summing its internal edges and the crossings gives the edge formula.

## Verification

The accompanying Python files are finite checks. `verify_a.py` exhausts minimum sets and checks token-jump structure, edge counts and components on small example graphs. `verify_b.py` checks the equality of the true and formula-generated minimum-set families for connected labelled bases of order at most four in the supplied parameter ranges. The recorded outputs are `verify_a_output.txt` and `verify_b_output.txt`. Finite checks supplement the proof.

## Relationship to prior work and limitations

Earlier clique-decoration results [1,2] contain broader forcing-set criteria and minimum-set enumeration. Javaid et al. [3] give the zero-forcing number of corona products. The disjoint-union rule of Geneson, Haas and Hogben [4] gives a Cartesian product for the reconfiguration of disconnected components; it does not compute how minimum-set fibers in a clique corona are joined by token jumps. The result here concerns the projection, induced fibers, and exact crossing edges for connected clique coronas, not the minimum-set classification as a separate contribution. The comparison is limited to the inspected statements; it does not establish absolute priority.

## References

1. *Zero-forcing enumerators of clique-decorated graphs*, Resultary, October 12, 2026, [record](https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-zero-forcing-enumerators-of-clique-decorated-graphs--05266193a935).
2. *Clique-corona fort classification and the complete zero-forcing polynomial*, Resultary, November 2, 2026, [record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-clique-corona-fort-classification-and-the-complete-zero-forcing--35539a2ce38d).
3. I. Javaid, I. Irshad, M. Batool, Z. Raza, *On the zero forcing number of corona and lexicographic product of graphs*, [arXiv:1607.04071](https://arxiv.org/abs/1607.04071), Theorem 2.3.
4. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, [arXiv:2009.00220](https://arxiv.org/abs/2009.00220), Proposition 2.7.
