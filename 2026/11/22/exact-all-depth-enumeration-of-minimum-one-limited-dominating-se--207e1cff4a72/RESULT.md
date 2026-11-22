# Exact all-depth enumeration of minimum one-limited dominating sets of ternary Sierpiński graphs

## Finding
For every integer \(n\ge1\), let \(M_n\) count the *labelled vertex subsets* of smallest size that dominate the ternary Sierpiński graph \(S(n,3)\), while every selected vertex has at most one unselected neighbour. All \(M_n\) are determined exactly by the following fixed, 64-entry integer recursion. This is an enumeration of **all** minimum solutions, not merely a construction or a lower bound.

Use the four boundary symbols \(0,1,2,3\) for, respectively, an omitted corner already dominated internally; a selected corner with one omitted neighbour internally; an omitted corner needing its external neighbour for domination; and a selected corner with no omitted neighbour internally. Write \(W_n:\{0,1,2,3\}^3\to\mathbb N_0\) for the number of optimal-cardinality local configurations with the indicated three outer-corner conditions. Put \(K(s,t)=1\) exactly for the ordered pairs corresponding to the unordered pairs
\[
 \{0,0\},\quad \{0,3\},\quad \{1,1\},\quad \{1,3\},\quad \{2,3\},\quad \{3,3\},
\]
and zero otherwise. For \(n=2\), the nonzero initial entries of \(W_2\), each equal to one, are
\[
(0,0,0),\ (0,1,1),\ (1,0,1),\ (1,1,0),\ (2,3,3),\ (3,2,3),\ (3,3,2).
\]
For all \(n\ge2\) and \(a,b,c\in\{0,1,2,3\}\), the recurrence is
\[
\boxed{W_{n+1}(a,b,c)=\!
\sum_{\substack{x,y,z\in\{0,1,2,3\}^{3}\\ x_0=a,\; y_1=b,\; z_2=c}}
 W_n(x)W_n(y)W_n(z)K(x_1,y_0)K(x_2,z_0)K(y_2,z_1).}
\]
The exact number of minimum solutions is
\[
\boxed{M_1=3,\qquad M_n=\sum_{x\in\{0,1,3\}^{3}}W_n(x)\quad(n\ge2).}
\]
Its initial terms, for depths \(n=1,2,3,4,5,6\), are
\[
3,\quad4,\quad10,\quad6656,\quad2496589218858,\quad90662803920487613562381063188768896464.
\]
The optimal cardinality of a dominating set is \(2\cdot3^{n-1}\). That cardinality was known before this enumeration and is not claimed as new.

## Assumptions and scope
The finite simple graph \(S(n,3)\) has vertices \(u=(u_1,\ldots,u_n)\in\{0,1,2\}^n\). Distinct vertices \(u,v\) are adjacent if some first differing position \(h\) satisfies \(u_h\ne v_h\) and \(u_j=v_h\), \(v_j=u_h\) for every \(j>h\). A set \(D\) dominates if every vertex outside \(D\) has a neighbour in \(D\); it is *one-limited* if each vertex in \(D\) has at most one neighbour outside \(D\). The three outer corners of \(S(n,3)\) are the constant words \((0,\ldots,0)\), \((1,\ldots,1)\), \((2,\ldots,2)\), in that order.

The boundary counts \(W_n\) allow an omitted outer corner to be undominated **only** when its flag is \(2\); all other vertices must satisfy the original domination and one-limited constraints. Every counted configuration has exactly \(2\cdot3^{n-1}\) selected vertices. Since external edges are not yet attached to an isolated copy, the flagged configurations need not themselves dominate that isolated copy. The count \(M_n\) excludes all final undominated flags. The word labels are fixed: no automorphism quotient is taken.

## Proof
**1. A lower bound inside each nine-vertex block.** For \(n\ge2\), partition the graph by prefixes of length \(n-2\) into induced copies of \(S(2,3)\), each containing three terminal triangles indexed by their penultimate symbol. If a triangle has a selected vertex, it has at least two: otherwise that vertex would have two unselected neighbours in its triangle. At most one triangle can be empty, because if rows \(i\) and \(j\) were empty, the omitted vertex with suffix \((i,j)\) would have no selected neighbour: its only neighbour outside its own triangle is the transposed suffix \((j,i)\), also omitted. This off-diagonal vertex has no edge leaving the nine-vertex block. If one triangle indexed \(i\) is empty, its two omitted off-diagonal vertices force the transposed endpoints in the other two triangles to be selected. Each of those selected endpoints already has an omitted neighbour across the transposition, so its entire terminal triangle must be selected. Consequently an empty triangle forces the other two triangles to be full, with six selections total. If no triangle is empty, each of the three has at least two selections, again totaling at least six.

Thus every one-limited dominating set has at least \(6\cdot3^{n-2}=2\cdot3^{n-1}\) vertices. Equality is attained by selecting precisely those words whose last two coordinates differ: each triangle then has exactly two selections; every intertriangle or earlier linking edge joins two selected or two omitted vertices. Hence the lower bound is sharp. Moreover, every minimum solution contains **exactly six** vertices in each nine-vertex block, so the following local classification is exhaustive.

**2. Exactly seven six-vertex block patterns.** In a nine-vertex block with all three triangles nonempty, each has exactly two chosen vertices. Let \(f(i)\in\{0,1,2\}\) specify the omitted last symbol in triangle \(i\). A selected endpoint of a transposition link already has one omitted neighbour in its own triangle; it cannot face an omitted endpoint of the link. Accordingly transposed off-diagonal vertices have identical selection status, which is equivalent to \(f(f(i))=i\) for all \(i\). There are exactly four involutions on three labelled symbols (identity and three transpositions), giving four balanced patterns. The other possibility has exactly one empty triangle and two full triangles; its empty-triangle index has three possibilities. These three unbalanced patterns are admissible locally except that the empty row's diagonal corner requires a selected neighbour outside the block. Thus all seven patterns have precisely the boundary flags listed for \(W_2\): a fixed point of \(f\) gives \(0\), a transposition endpoint gives \(1\), an empty row's corner gives \(2\), and a full row's corner gives \(3\).

**3. Exactly six cross-edge compatibility types.** Only a constant-suffix corner of a subgraph can meet an edge leaving that subgraph, and each such corner has at most one external neighbour. If an omitted corner has flag \(2\), it must face a selected free corner, flag \(3\). An omitted but already dominated flag \(0\) may face \(0\) or \(3\), but not a selected saturated flag \(1\). A selected saturated corner \(1\) may face \(1\) or \(3\). Two free selected corners may face each other. These are exactly the six unordered flag pairs defining \(K\); the criterion is both necessary and sufficient, since no other local condition changes under gluing.

**4. Recursive gluing and no overcounting.** The graph \(S(n+1,3)\) comprises three disjoint vertex copies of \(S(n,3)\), indexed \(0,1,2\). For each distinct pair of indices \(i,j\), a single edge joins corner \(j\) in copy \(i\) to corner \(i\) in copy \(j\). Its outer corners are corner \(0\) of copy \(0\), corner \(1\) of copy \(1\), and corner \(2\) of copy \(2\). By Step 1, every minimum solution restricts to exactly the known optimal number of vertices in every bottom nine-vertex block. Therefore the restriction to each child copy is counted by exactly one boundary profile in \(W_n\). By Step 3, the three gluing edges are legal precisely when the three displayed \(K\)-factors are one. Conversely, any such triple of child configurations produces a unique parent configuration satisfying all interior constraints. Its external flags are precisely \((x_0,y_1,z_2)\). This establishes the recurrence by induction and proves it counts every configuration exactly once.

Finally, a completed graph has no external neighbours at any of its three outer corners. An omitted corner with flag \(2\) would therefore be undominated. All other flags are allowed, yielding the formula for \(M_n\). For \(n=1\), the graph is \(K_3\) and has exactly three two-element minimum solutions. Every step is combinatorial and valid at all integer depths.

## Verification
The independent standalone `verify.py` first computes the seven nine-vertex patterns by literal adjacency enumeration, rather than assuming the classification; then evaluates the exact integer cubic transfer through depth six. Separately, for each depth three and four, it builds all actual graph vertices and edges from the original word definition; enumerates all locally admissible six-of-nine choices; tests the real cross-block edge constraints; and checks every surviving set against the original domination and one-limited conditions. The independent exhaustive totals are \(10\) and \(6656\), equal to the transfer counts. Run `python3 verify.py` with Python 3 standard library only. This finite verification supplements but does not substitute for Steps 1–4 above.

## Relationship to prior work
Božović's 2026 paper establishes the optimum cardinality \(2\cdot3^{n-1}\) but does not enumerate all optimizers. The publicly available mathematical result *Exact limited domination of every Sierpiński graph* extends the optimum-cardinality formula to all alphabet sizes and capacities, again without an optimizer census. *Extremal \(k\)-limited domination of depth-two Sierpiński graphs as symmetric regular binary matrices* classifies the depth-two optimizers but not any greater depth. The closer *Four independent local choices in minimum one-limited dominating sets of ternary Sierpiński graphs* constructs \(4^{3^{n-3}}\) distinct minimum sets, explicitly states that its count is only a lower bound, and does not give this all-depth exact enumeration. In particular, a lower-bound construction does not imply the complete seven-pattern characterization or the complete boundary-transfer recurrence. Searches for the \((0,1)\)-pitchfork formulation and for exact optimizer counts gave no covering result; absence from an index cannot rule out all historical equivalents.

## Limitations
The recurrence counts minimum solutions, not larger one-limited dominating sets. Its four boundary symbols apply specifically to the alphabet of size three and capacity one; no formula is claimed for other capacities or alphabet sizes. The recurrence computes exact integer counts but does not by itself give a closed elementary formula or a limiting growth constant. Historical priority is provisional, and independent mathematical review has not been performed.

## References
- D. Božović, *On \(k\)-limited domination: complexity and Sierpiński graphs*, arXiv:2610.01584v1, first publicly submitted 2026-10-01, https://arxiv.org/abs/2610.01584v1 (Section 5, Theorems 10–11).
- *Exact limited domination of every Sierpiński graph*, mathematical preprint publicly available October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-limited-domination-of-every-sierpi-ski-graph--023a3f7ea943 .
- *Extremal \(k\)-limited domination of depth-two Sierpiński graphs as symmetric regular binary matrices*, mathematical preprint publicly available November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-extremal-k-limited-domination-of-depth-two-sierpi-ski-graphs-as--a700d19c9c6e .
- *Four independent local choices in minimum one-limited dominating sets of ternary Sierpiński graphs*, mathematical preprint publicly available November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-independent-local-choices-in-minimum-one-limited-dominating--dd1f71f2c8ed .
