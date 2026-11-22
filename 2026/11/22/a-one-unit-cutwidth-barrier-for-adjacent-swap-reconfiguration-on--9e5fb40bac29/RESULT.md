# A one-unit cutwidth barrier for adjacent-swap reconfiguration on balanced double stars

## Finding
For every integer \(t\ge1\), let \(D_t\) be the unweighted tree consisting of adjacent distinguished hubs \(U,V\), with \(t\) individually labelled private leaves \(A_0,\ldots,A_{t-1}\) at \(U\) and \(t\) individually labelled private leaves \(B_0,\ldots,B_{t-1}\) at \(V\). Let \(\mathcal R_t(k)\) have as vertices all linear orders of these \(2t+2\) vertices with cutwidth at most the integer \(k\); its edges interchange consecutive positions, provided the new order remains feasible.

**Theorem.** At budget \(k=t\), \(\mathcal R_t(t)\) has **exactly two connected components**, distinguished by whether \(U\) precedes \(V\). At every budget \(k\ge t+1\), \(\mathcal R_t(k)\) is **connected**. For any \(k\le t\) for which feasible orders exist, the two hub orientations cannot communicate. Thus \(t+1\) is the exact first connected budget, for every \(t\ge1\). Within either orientation, every feasible order at budget \(k\ge t\) admits a feasible sequence of \(O(t^2)\) adjacent swaps to the same labelled canonical order (or its hub-reversed image).

The two components at budget \(t\) are equal in size. Each has exactly
\[
(t!)^2M_t
\]
vertices, where \(M_t\) is the number of feasible symbolic words over \(t\) copies of \(A\), \(t\) copies of \(B\), and hubs \(U,V\) in that relative order. The exact integer \(M_t\) is computable by the finite recurrence below in \(O(t^2)\) states. For \(t=1,2,3,4,5,6\), respectively, \(M_t=1,4,34,160,950,4424\).

## Assumptions and scope
All edges have unit weight. A cut is taken between two successive positions of a complete order; its width is the number of graph edges having endpoints on opposite sides. A state's cutwidth is the maximum width of any such cut. Vertex labels distinguish the leaves even when they have identical neighborhoods. Moves swap exactly two adjacent entries, without relabelling and without exceeding \(k\) before or after the move. This is a reachability/component and counting theorem, **not** a claim of globally shortest routes or median geometry.

For a word with \(U\) before \(V\), write \(a,b\) for the numbers of \(A\)- and \(B\)-leaves in the current prefix. The cutwidth of this prefix is determined by how many hubs have appeared:
\[
 w_0(a,b)=a+b,\qquad w_1(a,b)=t-a+b+1,\qquad w_2(a,b)=2t-a-b.
\]
The same formulas with \(A,B\) interchanged describe the other hub orientation. They include the edge \(UV\) exactly when one hub, but not the other, is in the prefix.

To count a component at budget \(t\), let \(F_t(a,b,h)\) count feasible completions of a symbolic prefix with \(a\) occurrences of \(A\), \(b\) of \(B\), and \(h\in\{0,1,2\}\) hubs already read in the fixed order \(U,V\). Set \(F_t(t,t,2)=1\). All other states are given by adding one of the available symbols \(A\), \(B\), or the next hub, summing the resulting \(F_t\) values only when the new prefix satisfies \(w_{h'}(a',b')\le t\), and setting invalid states to zero. Then \(M_t=F_t(0,0,0)\). Every symbolic word has \((t!)^2\) independently labelled realizations. This is an exact transfer recurrence, not an estimated enumeration.

## Proof
**1. Width invariant.** Each leaf edge crosses the prefix cut exactly if its leaf and its unique hub lie on opposite sides. Before the hubs, precisely the \(a+b\) previously placed leaf edges cross. Between them, the \(t-a\) not-yet-placed \(A\) edges, the \(b\) already placed \(B\) edges, and the hub edge cross. After both, the \(2t-a-b\) not-yet-placed leaf edges cross. This proves the three formulas and the stated counting recurrence.

**2. The two orientations cannot meet at budget \(t\).** Relative order of \(U,V\) can change only by swapping the hubs when consecutive. If the immediately preceding prefix contains \(a\) A-leaves and \(b\) B-leaves, the cut between the hubs has width \(t+1+b-a\) before the swap and width \(t+1+a-b\) after it. The larger of these is \(t+1+|a-b|\ge t+1\). Therefore no such edge exists with budget \(k\le t\). Both orientations occur at budget \(t\): the orders \(A_0\cdots A_{t-1}UVB_0\cdots B_{t-1}\) and its hub/leaf-class mirror have cutwidth exactly \(t\).

**3. Each orientation is internally connected at all budgets \(k\ge t\).** Fix the orientation \(U<V\). The following elementary adjacent swaps always preserve feasibility; all unspecified cut widths stay unchanged:

- A contiguous pair of leaves \(BA\) can be sorted to \(AB\) within any of the three hub-delimited regions. Before both hubs and after both hubs the affected cut is unchanged. Between hubs it decreases by two.
- Moving a \(B\)-leaf from immediately before \(U\) to immediately after it (\(BU\mapsto UB\)) reduces the new intermediate cut by one relative to the previously existing cut just after \(U\).
- Moving an \(A\)-leaf from immediately after \(V\) to immediately before it (\(VA\mapsto AV\)) reduces the new intermediate cut by one relative to the previously existing cut just before \(V\).
- Once every leaf before \(U\) is an \(A\)-leaf, moving an \(A\)-leaf directly after \(U\) to directly before it (\(UA\mapsto AU\)) creates a cut of width at most \(t\): before the move there are strictly fewer than \(t\) A-leaves before \(U\).
- Once all \(t\) A-leaves precede \(V\), moving a \(B\)-leaf directly before \(V\) to directly after it (\(BV\mapsto VB\)) likewise creates a cut of width at most \(t\).

Starting with any feasible order, first sort all \(BA\) pairs inside each hub-delimited region. Move each B-leaf immediately preceding \(U\) across \(U\), then each A-leaf immediately following \(V\) across \(V\); after each such move, the next same-class leaf is adjacent to the hub, so the procedure exhausts the class. Sort all \(BA\) pairs between the hubs again. Now move all A-leaves between the hubs left across \(U\), followed by all B-leaves between the hubs right across \(V\). The resulting class word is \(A^tUVB^t\). Finally, sort the labels within the two leaf blocks by adjacent swaps. Such same-neighborhood swaps change no cut value. The resulting order \(A_0\cdots A_{t-1}UVB_0\cdots B_{t-1}\) is the same for every starting state in this orientation. Reversing and concatenating these routes connects any two such states; the \(V<U\) case is symmetric. Each sorting pass uses at most quadratically many swaps, and at most linearly many hub-leaf moves occur, so the total is \(O(t^2)\).

**4. One additional unit bridges the orientations.** Put \(h=\lfloor t/2\rfloor\) and consider the class word \(A^hB^hUV A^{t-h}B^{t-h}\). Its prefix widths just before the hubs, between them and just after them are respectively \(2h\), \(t+1\), and \(2t-2h\); other cuts cannot exceed the maximum of these values and the same bound applies after interchanging the adjacent hubs. As \(2h\le t+1\) and \(2t-2h\le t+1\), both orders have width at most \(t+1\). Thus a single legal swap of the two hubs joins the two internally connected orientations whenever \(k\ge t+1\). Combined with Step 2 this proves the sharp connectivity threshold.

**5. Component sizes.** At \(k=t\), Steps 2 and 3 identify the components exactly with the two orientations. The prefix-width formulas characterize every admissible symbolic word, so the recurrence for \(M_t\) counts all and only the feasible symbolic words of either orientation. The \((t!)^2\) independent assignments of distinct labels within each leaf type give the component sizes, proving the counting statement.

## Verification
The accompanying standalone `verify.py` recomputes the cutwidth directly from the original graph edges, independently of the symbolic-prefix formulas. It exhaustively enumerates every labelled order and every feasible adjacent-swap edge for \(t=1,2,3\), at budgets \(t\) and \(t+1\), and computes all connected components by breadth-first search. The observed component-size profiles are \((1,1)\) and \((16)\) for \(t=1\), \((16,16)\) and \((296)\) for \(t=2\), and \((1224,1224)\) and \((13536)\) for \(t=3\). Each instance agrees with the symbolic count recurrence. The executable also checks the constructive normalization against the direct edge definition for every feasible enumerated state and checks larger parameter instances with deterministic random samples. Execute `python3 verify.py` from the extracted package directory. These finite checks support the proof but are not substitutes for the all-parameter argument.

## Relationship to prior work
Arrighi, Fernau, de Oliveira Oliveira, and Wolf (2021; expanded journal article 2023) prove that any two orders with cutwidth at most \(k\) can be reconfigured with cutwidth at most \(2k\) on arbitrary graphs. This guarantees sufficient slack but does **not** imply connectivity at the smaller exact budget \(t+1\) for this double-star family, nor the two orientation components and their exact counts at budget \(t\). In particular, their bound would allow budget \(2t\) for the endpoints used here. The related single-hub star case is a distinct configuration graph: it cannot express a two-hub order obstruction. The present result resolves the sharp barrier on this infinite two-hub family, not on arbitrary trees or general layouts.

## Limitations
No claim is made about exact graph diameters, geodesic paths, component structure at budgets strictly below \(t\), weighted cutwidth, or general double stars with unequal leaf classes. The recurrence counts the connected components at the budget specified, not arbitrary budgets. The novelty comparison draws on the inspected original 2021 and expanded 2023 papers, targeted searches and indexed mathematical records; absence of another equivalent publication cannot be guaranteed. An independent audit has not been performed.

## References
1. E. Arrighi, H. Fernau, M. de Oliveira Oliveira and P. Wolf, *Order Reconfiguration Under Width Constraints*, MFCS 2021, LIPIcs 202, Article 8, DOI: 10.4230/LIPIcs.MFCS.2021.8, first public 2021-08-18. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2021.8
2. E. Arrighi, H. Fernau, M. de Oliveira Oliveira and P. Wolf, *Order Reconfiguration under Width Constraints*, Journal of Graph Algorithms and Applications **27** (2023), 409–431, DOI: 10.7155/jgaa.00628. https://www.jgaa.info/index.php/jgaa/article/view/paper628
