# Equilibrium phases and a strict ordinal potential on two-hub social-distance hosts

## Finding

Fix an integer \(k\ge3\) and a real reward \(\alpha>0\). In the social-distancing network-creation game with host graph \(K_{2,k}\), write \(a\) for the number of leaves connected only to hub \(A\), \(b\) for those connected only to hub \(B\), and \(c\) for leaves connected to both. Every connected feasible network has \(a+b+c=k\) and \(c\ge1\). It is pairwise stable **if and only if** one of the following mutually exclusive cases holds:

1. \(c=1\) and \(\alpha\le2(\min\{a,b\}+1)\);
2. \(a=b=0\), \(c=k\), and \(\alpha\ge2\);
3. \(a=b=t\ge1\), \(c=k-2t\ge2\), and \(\alpha=2(t+1)\).

Thus the intermediate-density equilibria with at least two doubly attached leaves and at least one singly attached leaf exist only at isolated even values of \(\alpha\). The **exact number** of stable labeled networks is

\[
N_k(\alpha)=k\sum_{j=r}^{k-1-r}\binom{k-1}{j}
+\mathbf1_{\{\alpha\ge2\}}
+\sum_{t=1}^{\lfloor(k-2)/2\rfloor}
\mathbf1_{\{\alpha=2(t+1)\}}
\frac{k!}{t!\,t!\,(k-2t)!},
\qquad
r=\max\{0,\lceil\alpha/2\rceil-1\},
\]

where an empty sum is zero, and the hubs and all leaves have fixed, distinct labels. Furthermore, every strict improving-move sequence terminates after at most \(k(k+1)/2-1\) moves. In fact,

\[
\Phi(G)=\alpha c+2(a+1)(b+1)
\]

is a **strict ordinal potential**: every allowed improvement strictly increases \(\Phi\), and every allowed non-improving move does not strictly increase it.

## Assumptions and scope

The host \(H=K_{2,k}\) has two fixed hub vertices \(A,B\) and \(k\) distinguishable leaves. Only hub–leaf edges can be present or added. A state is an undirected, simple, connected **spanning** subgraph \(G\subseteq H\). For each vertex \(v\), utility is

\[
u_v(G)=\alpha\deg_G(v)+\sum_{w\ne v}d_G(v,w).
\]

An existing edge can be removed unilaterally by either endpoint if the resulting state stays connected and this endpoint's utility **strictly** increases. A missing host edge can be added bilaterally only when **both** endpoints' utilities strictly increase. Equality of utility does not count as an improving move. Pairwise stability means that no such move exists. The parameter is any positive real number, including every boundary equality. Counts identify labeled edge sets, not graph isomorphism classes.

A connected spanning state must attach each leaf to at least one hub and must have a leaf attached to both hubs; conversely these conditions ensure connectedness. Hence every state is a labeling of the leaves by the symbols \(A\)-only, \(B\)-only, or both, with at least one 'both' symbol.

## Proof

**Step 1: exact endpoint gains.** Consider an \(A\)-only leaf \(x\). The only missing host edge incident to it is \(Bx\). Inserting that edge shortens the distance from \(x\) to \(B\) by two and from \(x\) to each of the \(b\) \(B\)-only leaves by two; no other distance from \(x\) changes. From \(B\)'s viewpoint only the distance to \(x\) changes, by two. Consequently, the two gains are respectively

\[
\Delta u_x=\alpha-2(b+1),\qquad \Delta u_B=\alpha-2.
\]

Since \(b\ge0\), insertion of \(Bx\) is an improving bilateral move exactly when \(\alpha>2(b+1)\). Symmetrically, adding the missing edge to a \(B\)-only leaf is improving exactly when \(\alpha>2(a+1)\).

Now suppose \(c\ge2\), and \(x\) is doubly attached. Removing \(Bx\) leaves the state connected because another doubly attached leaf preserves a hub-to-hub path. This changes \(x\) into an \(A\)-only leaf, and the corresponding distance increases from \(x\) and from \(B\) are respectively \(2(b+1)\) and \(2\). The utility changes caused by the deletion are therefore \(2(b+1)-\alpha\) for \(x\) and \(2-\alpha\) for \(B\). Because the first threshold dominates the second, the deletion is improving for at least one endpoint exactly when \(\alpha<2(b+1)\). The symmetric deletion criterion is \(\alpha<2(a+1)\).

For \(c=1\), deleting either edge of the unique doubly attached leaf disconnects the graph. Deleting an edge incident to any singly attached leaf also disconnects the graph. The preceding additions and, when \(c\ge2\), deletions are therefore **all** feasible single-edge moves.

**Step 2: classification.** If \(c=1\), deletions are impossible. The allowed additions impose \(\alpha\le2(b+1)\) whenever \(a>0\), and \(\alpha\le2(a+1)\) whenever \(b>0\). Because \(a+b=k-1\ge2\), these inequalities are equivalent to \(\alpha\le2(\min\{a,b\}+1)\).

If \(c\ge2\), both directions of deleting an edge from a doubly attached leaf are blocked if and only if

\[
\alpha\ge2(a+1),\qquad \alpha\ge2(b+1).
\]

If \(a=b=0\), no additions remain, so exactly \(\alpha\ge2\) is needed. Otherwise, if only one of \(a,b\) is positive, an available addition demands an upper bound of \(2\) while a deletion demands a strictly larger lower bound; stability is impossible. If both are positive, blocking additions additionally requires \(\alpha\le2(a+1)\) and \(\alpha\le2(b+1)\). All four conditions hold exactly when \(a=b=t\ge1\) and \(\alpha=2(t+1)\). Such a state has \(c=k-2t\ge2\). Conversely, each listed case blocks every possible improvement. This proves the if-and-only-if classification.

**Step 3: count labeled equilibria.** In the \(c=1\) family, choose the unique doubly attached leaf in \(k\) ways and choose the \(j\) \(A\)-only leaves among the remaining \(k-1\). The stability inequality is \(\min(j,k-1-j)\ge r\), so precisely the first term of \(N_k(\alpha)\) results. The all-doubled graph contributes one state at \(\alpha\ge2\). In the balanced-interior case \((a,b,c)=(t,t,k-2t)\), the number of labeled leaf assignments is the multinomial coefficient \(k!/(t!t!(k-2t)!)\); this contributes only at \(\alpha=2(t+1)\). The three families are disjoint and exhaust the stable states, proving the formula.

**Step 4: potential and finite improvement property.** Under an addition of \(Bx\) to an \(A\)-only leaf, the counts change as \((a,b,c)\mapsto(a-1,b,c+1)\), so

\[
\Phi(G+Bx)-\Phi(G)=\alpha-2(b+1).
\]

For adding the missing edge to a \(B\)-only leaf the difference is \(\alpha-2(a+1)\), and each feasible deletion has the opposite difference of the corresponding addition. By Step 1, these expressions are positive **exactly for the corresponding improving moves**. Thus \(\Phi\) is a strict ordinal potential for the permitted moves. The number of nonnegative integer triples \((a,b,c)\) satisfying \(a+b+c=k\), \(c\ge1\), is \(\binom{k+1}{2}\). As each move strictly raises a function of the count triple, no count triple repeats along an improvement sequence. Hence every such sequence has length at most \(\binom{k+1}{2}-1\), as claimed.

## Verification

Run `python verify_biclique_sdncg.py` using Python 3 and the standard library. The script independently constructs graph distances by breadth-first search, evaluates the payoffs before and after each permitted single-edge move, tests the closed-form stability criterion and counts, and tests the sign of each potential difference. It exhaustively checks every one of the \(4^k\) possible edge-pattern encodings for each \(k\in\{3,4,5,6,7\}\) at 14, 16, 18, 20 and 22 positive half-integer parameter probes respectively. The confirmed totals are 465,792 direct graph/payoff instances, 90 exact-count comparisons, 8,951 equilibrium instances and 116,928 potential-sign comparisons (the last checks run through \(k=6\)). Rational arithmetic is exact. These finite tests support but **do not replace** the unrestricted proof above.

For illustration, with \(k=4\), the formula gives \(N_4(\alpha)=25\) when \(2<\alpha<4\), \(N_4(4)=37\), and \(N_4(\alpha)=1\) when \(\alpha>4\). The isolated twelve-state contribution at \(\alpha=4\) is the balanced interior family.

## Relationship to prior work

Friedrich, Gawendowicz, Lenzner and Melnichenko introduced the social-distancing network-creation game, including arbitrary **host-graph restrictions**, and proved extreme-parameter stability and some general intermediate-parameter existence guarantees. Their general game admits strict improving cycles; no global potential is available (Theorem 4). Theorem 9 shows that all host spanning trees are stable at sufficiently small rewards and that the full host is uniquely stable at sufficiently large rewards; Theorem 10 supplies an intermediate-range existence guarantee by routing-cost spanning trees. Those results are not an exact all-parameter census or convergence theorem on the two-hub family considered here.

The host family \(K_{2,k}\), for \(k\ge3\), has several four-cycles sharing edges; therefore a classification restricted to cactus hosts (where distinct cycles do not share edges) cannot imply this claim. The extra phenomenon is that overlapping cycles still admit a simple ordinal potential and isolated balanced density phases. Other network-creation games with edge purchase costs or homophily preferences use different utility functions, so their potential and equilibrium statements do not directly imply this result.

## Limitations

The proof concerns exactly two hub vertices with no hub–hub edge, any \(k\ge3\) leaves and **only host edges** as allowed additions. It does not classify arbitrary three-hub, general bipartite or complete hosts, nor does it establish a potential for unconstrained social-distancing network creation. The upper bound on improvement length is guaranteed but is not asserted to be the sharp worst-case length. The enumeration is of labeled networks, not their isomorphism classes. Publication priority has been checked against relevant accessible primary statements and search results but is not an exhaustive guarantee against unpublished, inaccessible or differently indexed equivalent results.

## References

1. T. Friedrich, H. Gawendowicz, P. Lenzner, A. Melnichenko, *Social Distancing Network Creation*, arXiv:2204.10423, first public version 21 April 2022, https://arxiv.org/abs/2204.10423 . Journal full text: *Algorithmica* (2023), DOI:10.1007/s00453-022-01089-6, https://link.springer.com/article/10.1007/s00453-022-01089-6 . Relevant statements: model and host restrictions (§1.1); general improving cycles (Theorem 4); host bounds and stability existence (Theorems 9–10).
2. *Selfish Creation of Social Networks*, arXiv:2012.06203, https://arxiv.org/abs/2012.06203 . A different network-creation objective considered in the literature comparison.
