# A triangle chord creates quadratic-period clocks in sequential bi-threshold H-networks

## Finding

For every integer \(\beta\ge2\), a fixed-order sequential Boolean hysteresis map on a connected, unicyclic graph with \(4\beta+2\) labelled vertices has a primitive temporal orbit of *exactly*
\[
\boxed{\beta(\beta+4)}
\]
full sweeps. The graph is obtained by adding a single edge between the first and third vertices of one path in a double-path H-network. The exhibited cycle is an explicit invariant set on which the dynamics acts as a full cyclic permutation; it is not a claim of a globally maximal period or of an exhaustive attractor census.

## Assumptions and scope

Fix \(\beta\in\mathbb Z\), \(\beta\ge2\), and put \(L=2\beta+1\). Let the vertices be two disjoint ordered paths \(u_0,\ldots,u_{2\beta}\) and \(v_0,\ldots,v_{2\beta}\), with their consecutive path edges, the bridge \(u_\beta v_\beta\), and the sole extra edge \(u_0u_2\). There is exactly one undirected cycle, the triangle \(u_0u_1u_2u_0\). Scan vertices in the order \(u_0,u_1,\ldots,u_{2\beta},v_0,v_1,\ldots,v_{2\beta}\), once per time step.

When a vertex is scanned, let \(s\) be the number of occupied vertices in its **closed** neighborhood, counting itself and the already-updated bits of preceding vertices. A current zero becomes one if \(s\ge1\), while a current one remains one if \(s\ge3\); otherwise its new value is zero. Thus the activation and retention thresholds are respectively one and three. A temporal orbit is primitive of length \(p\) when it visits exactly \(p\) distinct complete configurations before returning to its starting configuration.

For \(0\le r\le L\), write \(T_r=1^r0^{L-r}\) for the word on the upper path. For \(0\le j\le\beta\), write \(B_j=0^j1^{\beta+1}0^{\beta-j}\) for the lower path, and write \(B_*=0^L\). Each pair \((T_r,B_j)\) designates a labelled global configuration; the symbol \(*\) denotes an empty lower path, not an integer.

## Proof

**1. Explicit invariant configurations.** Consider the mutually disjoint sets
\[
\mathcal G=\{(T_r,B_j):\ \beta+1\le r\le L,\ j\in\{*,0,\ldots,\beta\}\},
\qquad
\mathcal D=\{(T_r,B_*):\ 3\le r\le\beta\}.
\]
The latter is empty for \(\beta=2\). Every member has a unique upper prefix length and lower word; hence
\[
|\mathcal G|=(\beta+1)(\beta+2),\quad |\mathcal D|=\beta-2,\quad
|\mathcal S|=|\mathcal G\cup\mathcal D|=\beta(\beta+4).
\]

**2. Exact one-sweep transition table.** Use the index \(q\in\{0,\ldots,\beta+1\}\), with \(q=0\) representing \(B_*\) and \(q=j+1\) representing \(B_j\). In the next table arithmetic on \(q\) is modulo \(\beta+2\). If \(r>\beta+1\) and the state is \((T_r,q)\), its successor is \((T_{r-1},q-1)\). If \(r=\beta+1\) and \(q\ne0\), the successor is \((T_L,q-1)\). At the one exceptional grid state \((T_{\beta+1},0)\), the successor is \((T_\beta,0)\) when \(\beta\ge3\) and \((T_L,\beta+1)\) when \(\beta=2\). For \(\beta\ge4\) the extra states satisfy \((T_r,0)\mapsto(T_{r-1},0)\) for \(4\le r\le\beta\); finally \((T_3,0)\mapsto(T_L,\beta+1)\) for \(\beta\ge3\).

Here is a direct derivation from the stated local rule. Whenever the upper prefix contains more than \(\beta+1\) ones, its final one has only itself and the previously retained left neighbor occupied at its scan, so it dies, while every earlier occupied non-triangle vertex has at least three occupied closed neighbors and stays one. When the upper prefix has precisely \(\beta+1\) ones, the final upper one lies at \(u_\beta\). A nonempty lower block \(B_j\) contains \(v_\beta\), so the bridge supplies its third occupied neighbor, prevents its deletion, and triggers rightward filling of the remaining upper zeros during that sweep. With an empty lower row the bridge support is absent, so the prefix instead shortens until it has just three ones. At three ones the chord supplies the third occupied neighbor to \(u_2\); consequently \(u_2\) survives and the consecutive upper scan fills all later vertices. When \(\beta=2\), the threshold prefix already has three ones and the chord produces this last case immediately. In all these cases the upper hub \(u_\beta\) is occupied when the lower row is scanned. On a lower block \(B_j\), the rightmost one dies, the new left endpoint is activated, and the block shifts one position to the left, with \(B_0\) becoming empty. From an empty lower row, the occupied upper hub activates \(v_\beta\) and the subsequent lower sweep fills through \(v_{2\beta}\), producing \(B_\beta\). These checks cover all vertices, including both endpoints and the special triangle, and prove the complete transition table for every \(\beta\ge2\).

**3. One cyclic permutation.** On \(\mathcal G\), put \(p=L-r\in\mathbb Z/(\beta+1)\) and use the preceding \(q\in\mathbb Z/(\beta+2)\). Apart from the exceptional state \((p,q)=(\beta,0)\), the table is exactly translation by \((1,-1)\) on the product of these two cyclic groups. Because consecutive integers \(\beta+1\) and \(\beta+2\) are coprime, this translation visits all \((\beta+1)(\beta+2)\) grid states in one cycle. At the exceptional grid state the ordinary translation edge to \((0,\beta+1)\) has simply been subdivided by the \(\beta-2\) distinct intermediate configurations in \(\mathcal D\) (zero intermediates at \(\beta=2\)). Thus the actual hysteresis map is a permutation consisting of exactly one cycle on \(\mathcal S\). Its least period is its exact cardinality \(\beta(\beta+4)\), proving the theorem for every integer \(\beta\ge2\).

## Verification

The self-contained programs `check_symbolic.py` and `exhaustive_cycles.cpp` and their exact recorded outputs are included with this result. In a directory containing these four files, use
```
python3 check_symbolic.py
c++ -std=c++17 -O3 exhaustive_cycles.cpp -o exhaustive_cycles
./exhaustive_cycles
```
The Python program independently constructs bit-mask closed neighborhoods and verifies the stated table at every state of \(\mathcal S\) for all \(2\le\beta\le70\), checking 126,730 transition instances and their exact cycles. The C++ program independently enumerates *all* global binary configurations of both the original double-path tree and the one-chord graph for \(2\le\beta\le5\) (up to \(2^{22}\) configurations for each graph), identifying each primitive cycle. In the one-chord case it finds respectively one orbit of lengths 12, 21, 32, and 45, as predicted. The finite checks are supporting tests; the unbounded assertion rests on the algebraic invariant-set proof above.

## Relationship to prior work

Kuhlman, Mortveit, Murrugarra and Kumar [1] introduced and analyzed hysteretic sequential bi-threshold dynamics, including an H-shaped tree family with long periods, and explicitly discussed the question of changing graph edges. The present construction changes exactly one edge of a double-path H-tree, adds a triangle, and derives the new quadratic least-period clock by a complete invariant-set bijection. The source's long-period tree construction is not the present unicyclic transition law. The published bounded-order global tree census [2] optimizes over *acyclic trees* through fourteen vertices; neither its tested domain nor its extremal numbers entails an all-parameter primitive orbit on this unicyclic graph. The separate cyclic-graph necklace classification [3] concerns the simple cycle graph, not this graph with a bridge and two long paths. The equality or inclusion of periodic states under these graph changes is not assumed.

## Limitations

The exhibited invariant set is only one part of the complete configuration space; the theorem asserts one guaranteed primitive orbit of the specified period, not its uniqueness among *all* graph configurations, a global maximum, or a complete recurrent-state classification. The updating convention is strictly sequential, closed-neighborhood, fixed scan order, and thresholds \((1,3)\). The proof does not extend without additional work to synchronous updates, different update permutations, other chord positions, or any other threshold convention. Literature comparisons include the most relevant identified primary sources and publicly indexed findings; unindexed earlier equivalent constructions remain a residual historical-priority risk. Independent external validation has not been performed.

## References

[1] C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974v1, first publicly posted 2011-08-15, https://arxiv.org/abs/1108.2974 .

[2] *Sharp primitive-period maxima through fourteen vertices for sequential bi-threshold dynamics on trees*, published mathematical result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-primitive-period-maxima-through-fourteen-vertices-for-sequ--9e5a9ef7f73d .

[3] *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, published mathematical result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binary-necklace-attractors-and-triangular-run-basins-for-sequent--e79a108b9794 .
