# Cycle-incidence shattering on ladders: missing pairs and dyadic online growth

## Finding

Let \(L_n=P_2\square P_n\) be the labelled two-row ladder on \(n\ge2\) columns. Its concepts are the edge sets of **all simple cycles**, each queried by individual physical-edge membership. Define the full VC-shattered-support polynomial \(\Phi_n(z)=\sum_{S\subseteq E(L_n),\,S\text{ shattered}}z^{|S|}\), including the empty support. Then
\[
\boxed{\Phi_2(z)=1,\qquad \Phi_3(z)=1+7z,\qquad
\Phi_n(z)=1+(3n-2)z+\frac{n(9n-17)}2z^2\quad(n\ge4).}
\]
For \(n\ge4\), every edge singleton is shattered; among pairs, the only nonshattered ones are the \(n-1\) top/bottom rail-edge pairs in the same column gap and the four pairs joining an extreme rung to either adjacent rail edge. **No triple is shattered.** In particular, \(\operatorname{VCdim}(\mathcal C_n)=2\) for every \(n\ge4\).

Writing \(d_n=\operatorname{Ldim}(\mathcal C_n)\) for the complete adaptive mistake-tree depth, one has for every \(n\ge4\)
\[
\boxed{2\left\lfloor\log_2\left\lfloor\frac n2\right\rfloor\right\rfloor
\le d_n\le \left\lfloor\log_2\binom n2\right\rfloor.}
\]
Both bounds coincide for every power of two: for each integer \(t\ge2\),
\[
\boxed{d_{2^t}=2t-2.}
\]
Also \((d_2,d_3,d_4,d_5)=(0,1,2,3)\), and \(d_n>\operatorname{VCdim}(\mathcal C_n)\) for every \(n\ge5\). Thus a connected, subcubic, planar, two-row graph family has constant static VC dimension but logarithmically growing adaptive dimension; the dyadic values are exact.

## Assumptions and scope

The vertices are \((a,j)\) with row \(a\in\{0,1\}\) and column \(1\le j\le n\). The \(n\) rung edges are \(r_j=\{(0,j),(1,j)\}\). The top/bottom rails across each column gap are \(t_j=\{(0,j),(0,j+1)\}\) and \(b_j=\{(1,j),(1,j+1)\}\), for \(1\le j<n\). These are distinct physical edges; in particular the two rail queries in the same gap are separate coordinates, despite coinciding on every cycle concept. The domain has \(3n-2\) elements.

A query support \(S\subseteq E(L_n)\) is VC-shattered if for every \(T\subseteq S\) some simple cycle \(C\) satisfies \(E(C)\cap S=T\). The adaptive dimension is the greatest \(d\) for which a full binary depth-\(d\) tree of edge queries has, at every leaf, a simple cycle realizing all answers along that path. The empty support is shattered because \(L_n\) contains a cycle for \(n\ge2\). We do not include the empty graph, disconnected cycle unions, the entire binary cycle space, or arbitrary closed walks among concepts.

## Proof

**1. Exact representation of cycles.** Each simple cycle in a two-row ladder enters and leaves the top row through exactly two rungs: with only two rows, a simple cycle cannot use four rungs without branching or revisiting the top or bottom row. More formally, the cycle's top-row and bottom-row edges each form one nonempty path (a cyclic component confined to a row is impossible); their endpoints must have the same two column indices \(i<j\), and the cycle uses exactly the rungs \(r_i,r_j\). Conversely, every \(1\le i<j\le n\) determines the unique rectangular cycle
\[
C_{i,j}=\{r_i,r_j\}\cup\{t_k,b_k:i\le k<j\}.
\]
Therefore there are exactly \(\binom n2\) different concepts. Their query predicates are
\[
[r_a\in C_{i,j}]\iff a=i\text{ or }a=j,
\qquad[t_k\in C_{i,j}]=[b_k\in C_{i,j}]\iff i\le k<j.
\]

**2. Classification of pairs.** For \(n\ge4\), every rung pair \(r_a,r_b\) with \(a<b\) is shattered: the pair \((i,j)=(a,b)\) realizes both positives, a pair containing only one selected index realizes each singleton, and a pair of two indices outside \(\{a,b\}\) realizes neither. For two rail queries in *different* gaps \(k<\ell\), the cycles \(C_{1,n}\), \(C_{k,k+1}\), and \(C_{\ell,\ell+1}\) realize respectively both, only gap \(k\), and only gap \(\ell\). To realize neither, select two columns entirely at or before \(k\), entirely after \(\ell\), or strictly between the two gaps. At least one choice exists when \(n\ge4\). Two rails in the same gap always give the same Boolean answer, so that pair is not shattered.

For a rung \(r_a\) and a rail in gap \(k\), the conjunction is realizable by choosing a rectangle across gap \(k\) with \(a\) as one endpoint. The patterns with only the rung or only the rail are both possible unless \((a,k)=(1,1)\) or \((a,k)=(n,n-1)\). Indeed, in either exceptional case the extreme rung is present in precisely the rectangles crossing its adjacent extreme gap, and the two indicators coincide. Otherwise there are at least two columns on the relevant side of gap \(k\): choose a rectangle entirely on that side with endpoint \(a\) for rung-only, and a rectangle crossing the gap but avoiding \(a\) for rail-only. Finally, a rectangle using neither query exists since, after removing the column \(a\), at least one side of gap \(k\) contains two other columns (there are \(n-1\ge3\) other columns). Thus these are the only exceptions.

The \(3n-2\) physical edges are all nonconstant for \(n\ge3\). The nonshattered physical edge pairs are exactly \((n-1)+4=n+3\) in number: one same-gap top/bottom pair per gap and two adjacent-rail pairs for each extreme rung. Hence the number of shattered pairs is
\[
\binom{3n-2}{2}-(n+3)=\frac{n(9n-17)}2.
\]

**3. No triple.** A shattered support cannot contain two rail edges of the same gap. If it has at least three rung edges, the all-positive trace is impossible because each cycle has exactly two rungs. If it has two rungs and another edge, the trace with both rungs positive forces one specific rectangle \(C_{i,j}\), hence fixes the third answer. If it has one rung and two rails, restrict to cycles containing that rung: the rectangle extends exclusively to the left or to the right of that rung, and the two distinct queried gap memberships are either nested (same side) or mutually exclusive (opposite sides). Thus they cannot realize all four patterns conditional on that rung being positive. Finally, with three rail gaps \(k<\ell<m\) and no rung, a rectangle cannot include the first and last gap while excluding the middle one. Hence no triple, and by downward closure no larger support, can be shattered.

For \(n=2\) there is exactly one cycle and no nonempty support is shattered. For \(n=3\), exactly three cycles make any shattered pair impossible, while all seven edges are nonconstant. This proves all polynomial assertions.

**4. Adaptive upper bound.** In a depth-\(d\) complete mistake tree, two different answer paths require distinct realizing concepts, so there must be at least \(2^d\) cycles. The exact cycle count gives \(d\le\lfloor\log_2\binom n2\rfloor\).

**5. Adaptive lower bound.** Put \(m=\lfloor n/2\rfloor\). Retain just the \(m^2\) cycles \(C_{i,j}\) with \(1\le i\le m\) and \(n-m+1\le j\le n\). On this subfamily, querying \(t_k\) for \(1\le k<m\) returns one exactly when \(i\le k\), independently of \(j\). Querying \(t_k\) for \(n-m+1\le k<n\) returns one exactly when \(j>k\), independently of \(i\). Balanced binary-search threshold trees first divide the \(m\) possible values of \(i\) to depth \(\lfloor\log_2 m\rfloor\) and then do the same for \(j\), retaining at least one value of each at every leaf. Concatenation yields a complete tree of depth \(2\lfloor\log_2 m\rfloor\). Adding more concepts cannot destroy this witnessing tree. This proves the lower bound.

When \(n=2^t\), the lower bound is \(2t-2\). Since \(\binom {2^t}2=2^{t-1}(2^t-1)\), its base-two logarithm has floor \(2t-2\), proving the exact dyadic value. The eight leaves of the explicit depth-three tree in `ladder_n5_tree.json` witness \(d_5\ge3\); its ten concepts force \(d_5\le3\). The values at \(n=2,3,4\) follow from hypothesis count and the formula above. Every \(L_n\) with \(n\ge5\) contains the first five columns as an induced ladder, so all cycles and edge traces witnessing the depth-three tree in \(L_5\) persist. Thus the gap is strict at all \(n\ge5\), as asserted.

## Verification

Run `python3 verify_ladder_cycles.py ladder_n5_tree.json` using the Python standard library. It independently enumerates graph-theoretic simple cycles by adjacency-based depth-first search, and checks that the resulting edge-set family agrees with the interval representation for \(2\le n\le9\). It exhaustively compares actual and claimed shattered supports of sizes zero through three over all physical edges for these eight ladders (6,910 comparisons), including both rails separately. A memoized exact tree recursion computes the Littlestone dimensions for \(2\le n\le12\), and the explicit depth-three certificate is checked branch by branch against actual cycles of the five-column ladder. The program prints `LADDER_CYCLE_TRACE_CHECK_PASS` on success. These finite computations serve as independent stress tests; the all-order formulas and inequalities rely on the arguments above.

## Relationship to prior work

Mofidi's 2022 cycle-hypergraph work develops the edge-set notion, gives general structural constraints and compares the cycle and spanning-tree hypergraphs; its Theorem 3.4(2) determines wheel-cycle VC dimension, not the present ladder support polynomial or online dimension. Its related 2022 article studies cycle counts and VC bounds; its full text was not accessible in the source checks, so independent comparison with any supplementary graph-family examples remains unresolved. Guingona, Kolesnikov, Nierwinski and Soucy (2021) establish VC/Littlestone equality for zero sets of linearly independent functions, a different concept class; their definitions of full adaptive trees are used here.

Related results on simple-cycle incidence in wheels and \(K_{3,b}\) concern different graph families. An order-ideal online-rank theorem for the two-row poset \([2]\times[n]\) has a superficially similar pair-of-endpoints parameterization and an exact dyadic saturation result. However its hypotheses are *lower ideals* with two independent threshold membership query families, whereas this theorem concerns only the \(\binom n2\) rectangular simple cycles and their physical rung-equality or coupled-interval rail queries. The order-ideal result therefore does not yield the missing-edge-pair count, the exact cycle query support polynomial, or this graph class's five-column online boundary. Its binary-search and information-bound ingredients are explicitly not claimed new. A published three-column monotone-grid-path result also has a two-parameter interval coding and logarithmic online growth, but its queries test vertices visited by directed paths; the present graph cycles query distinct rung and rail **edges**. Its middle-column path membership has a related interval predicate, while its endpoint threshold predicates are not the present rung-equality predicate. In particular it does not give this pair-exception classification or the stated polynomial, nor directly the exact dyadic values for ladder cycles. The new contribution assessed is the full physical-edge trace classification together with the sharp dyadic online law and first strict-gap boundary; standard interval binary search and elementary cycle counts are not separately claimed novel.

## Limitations

The exact Littlestone dimension is not determined for every non-dyadic number of columns; the displayed two-sided bounds are of the same logarithmic order, with exact dyadic values and the first-gap classification. The theorem is for ordinary simple cycles of a two-row *open* ladder, not the circular ladder, arbitrary grids, or the cycle-space linear code. No assertion of absolute historical priority is made: unindexed equivalent interval formulations or the inaccessible second 2022 cycle-hypergraph paper are residual risks. No independent mathematical audit has occurred.

## References

1. Alireza Mofidi, *On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs*, Transactions on Combinatorics 11 (2022), 29–43, DOI: 10.22108/TOC.2021.127880.1832. Full text: https://toc.ui.ac.ir/article_25746_890e066e8b9dd269c189910e7e780475.pdf (Theorems 3.3 and 3.4).
2. Alireza Mofidi, *On the Number of Cycles of Graphs and VC-Dimension*, Facta Universitatis, Series Mathematics and Informatics 37 (2022), 121–135. DOI: 10.22190/FUMI210301011M (full-text comparison unavailable).
3. Vincent Guingona, Alexei Kolesnikov, Julie Nierwinski and Richard Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first publicly submitted 2021-09-10, https://arxiv.org/abs/2109.04805.
4. *An unbounded adaptive gap at fixed VC dimension for simple cycles of wheels*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-unbounded-adaptive-gap-at-fixed-vc-dimension-for-simple-cycle--f2f12978d28a.
5. *Exact static and online shattering ranks of cycle incidence in* \(K_{3,b}\), published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-static-and-online-shattering-ranks-of-cycle-incidence-in-k--9c37fd9bf68d.
6. *Shattering polynomial and an unbounded online gap for three-column monotone grid paths*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-shattering-polynomial-and-an-unbounded-online-gap-for-three-colu--105f31d7b4be.
7. *Online ranks of finite order-ideal classes: bounded-width exact computation and dyadic saturation*, published-finding corpus research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-online-ranks-of-finite-order-ideal-classes-bounded-width-exact-c--68248a42b6fd.
