# Exponential median fragmentation and Catalan survivors for fault-avoiding grid geodesics

## Finding

Let \(a,b\geq1\) be integers and \(F\) any set of \(k\) nonterminal vertices of the rectangular grid \(\{0,\ldots,a\}\times\{0,\ldots,b\}\). Consider the *original-distance geodesics*: north/east routes from \((0,0)\) to \((a,b)\) that avoid \(F\), each with exactly \(a+b\) edges. Two routes are adjacent when one intermediate vertex is changed and both routes remain original-distance geodesics avoiding \(F\).

For a route \(P\), let \(x_P(t)\) be its number of east steps in its first \(t\) steps, and assign to each failed vertex \(f=(i,j)\) the sign \(\sigma_P(f)=-\) if \(x_P(i+j)<i\), or \(+\) if \(x_P(i+j)>i\). The equality case cannot occur in an avoiding route.

**Theorem.** Two surviving routes are reconfigurable if and only if their entire fault-sign vectors agree. Each nonempty sign fiber is an order interval of the distributive lattice of monotone routes. Its reconfiguration graph is a convex isometric median subgraph of the intact route graph. If \(h_r(P)\) denotes the number of east moves before the \(r\)-th north move, the exact minimum number of rerouting steps within a component is

\[
 d_F(P,Q)=\sum_{r=1}^{b}\lvert h_r(P)-h_r(Q)\rvert.
\]

Writing \(P_-\) and \(P_+\) for the component's unique bottom and top paths in this order, its exact diameter is \(\sum_{r=1}^{b}(h_r(P_+)-h_r(P_-))\). A fixed sign vector can be tested for realizability in \(O(a+b+k)\) arithmetic operations by an interval-valued dynamic program.

There are at most \(2^k\) components, and this bound is attained for every \(k\geq1\). Specifically, in the \((2k+1)\)-by-\((2k+1)\) vertex grid take

\[
 F_k=\{(2r-1,2r-1):1\leq r\leq k\}.
\]

The rerouting graph then has exactly \(2^k\) nonempty connected components, yet its total number of surviving routes is the Catalan number

\[
 C_{2k}=\frac{1}{2k+1}\binom{4k}{2k}.
\]

The Catalan count is a complementary enumeration of surviving routes, not a claim that all their reconfiguration components have equal size.

## Assumptions and scope

The underlying graph has unit undirected horizontal and vertical edges. An original-distance geodesic means a path retaining the distance \(a+b\) of the **unfaulted** grid. If failures remove every such path, the reconfiguration graph is empty. We make no claim about longer shortest paths in the damaged graph when the original distance becomes unattainable. Failed boundary vertices are allowed, but the two terminals are not. All paths and reconfiguration sequences are finite.

The intact path lattice uses the pointwise order \(P\leq Q\) when \(x_P(t)\leq x_Q(t)\) at every step \(t\), equivalently \(h_r(P)\leq h_r(Q)\) for every north-step index \(r\). Coordinatewise minima and maxima of the north-step profiles define meet and join. Equivalently, a route is the boundary of a Young diagram of unit cells in the \(a\)-by-\(b\) rectangle; the route order is containment of its cell ideal.

## Proof

**1. Local moves and invariant signs.** Two original-distance routes differ in a single intermediate vertex exactly when their east/north words differ by interchanging adjacent unlike letters. A swap changes \(x_P(t)\) at exactly one index by one, leaving other indices unchanged. At a fault \((i,j)\) the value \(x_P(i+j)=i\) is forbidden; moving from a value below \(i\) to one above \(i\) would require this excluded equality along any one-step reconfiguration sequence. Thus each fault-sign vector is constant on components.

**2. Every nonempty sign fiber is one lattice interval.** For each failed \((i,j)\), choosing the minus sign imposes \(x_P(i+j)\leq i-1\), a lower order ideal of the path lattice; choosing plus imposes \(x_P(i+j)\geq i+1\), an upper order filter. Each constraint is closed under coordinatewise meet and join. Their intersection \(\mathcal L_\sigma\), if nonempty, is order-convex and closed under meet and join. Since it is finite, it has a unique minimum \(P_-\) and maximum \(P_+\), and order-convexity gives \(\mathcal L_\sigma=[P_-,P_+]\). An interval of the distributive lattice of order ideals is the order-ideal lattice of the induced poset of cells between its extrema. Its cover graph is therefore connected and median. Its covers are precisely legal adjacent-square reroutings. Hence the components are exactly the nonempty sign fibers.

**3. Distances, convexity and diameters.** Map each path to its unit-cell ideal \(I(P)\). A rerouting toggles one cell, so every path between \(P,Q\) needs at least \(\lvert I(P)\mathbin\triangle I(Q)\rvert\) toggles. If the signs agree, first remove cells of \(I(P)\setminus I(Q)\) in maximal-element order to reach \(I(P)\cap I(Q)\), then add cells of \(I(Q)\setminus I(P)\) in minimal-element order. Every intermediate ideal lies in \([P_-,P_+]\), so the lower bound is attained. Row by row the symmetric difference contains exactly \(\lvert h_r(P)-h_r(Q)\rvert\) cells, proving the distance formula. Any ambient shortest path must toggle only these symmetric-difference cells, so it stays between the meet and join of its endpoints and remains in the same sign interval. Thus components are convex, not merely isometric. The two extrema differ in every cell of \(I(P_+)\setminus I(P_-)\), so their distance is the diameter; all other component pairs have no larger symmetric difference.

**4. Feasible signatures.** For every \(0\leq t\leq a+b\), intersect the physical bounds \(\max(0,t-b)\leq x_P(t)\leq\min(a,t)\) with all upper or lower integer bounds assigned by faults at layer \(t\), giving an integer interval \(B_t\), possibly empty. Starting from \(R_0=\{0\}\), if the attainable values at layer \(t\) form \(R_t=[u_t,v_t]\cap\mathbb Z\), then the next attainable values are

\[
 R_{t+1}=B_{t+1}\cap[u_t,v_t+1]\cap\mathbb Z.
\]

The recurrence is exact because each move increases \(x\) by zero or one, and all integers between the extremes are attainable. A signature is realizable exactly if none of these sets becomes empty and the last one contains \(a\). Merging each fault's bound into its layer takes linear total work in \(a+b+k\). Computing actual bottom and top paths also follows by forward/backward greedy propagation of these intervals.

**5. Sharp exponential fragmentation.** A path avoids each of the \(k\) faults by choosing a minus or plus sign, so there are at most \(2^k\) components. In the special square grid with the fault set \(F_k\), concatenate, independently for each \(r=1,\ldots,k\), either the four-step word \(EENN\) or \(NNEE\). Each block runs from \((2r-2,2r-2)\) to \((2r,2r)\), avoids \((2r-1,2r-1)\), and chooses its own sign independently. Hence all \(2^k\) signatures occur and the bound is sharp.

**6. Catalan survivor count.** Encode east as \(+1\) and north as \(-1\) in a balanced word of length \(4k\). Visits to \((r,r)\) are precisely returns of the walk to zero after \(2r\) steps. Avoiding the faults \(F_k\) means that every *primitive excursion* between successive returns has even semilength. A primitive excursion of semilength \(m\geq1\) has exactly \(2C_{m-1}\) possible positive/negative shapes. Let \(O(z)=\sum_{j\geq0}C_{2j+1}z^j\). The generating function of the allowed concatenations is therefore \(B(z)=1/(1-2zO(z))\). For the usual Catalan series \(C(t)=\sum_{n\geq0}C_nt^n\), the identity \(C(t)=1+tC(t)^2\) shows, by taking its even part \(E(z)=\sum_{j\geq0}C_{2j}z^j\), that \(E(z)=1+2zE(z)O(z)\). Hence \(B(z)=E(z)\), and the number at length \(4k\) is \(C_{2k}\).

## Verification

Run `python3 verify_exhaustive.py` and `python3 verify_diagonal.py` using Python 3 and its standard library. The first program independently builds every legal rerouting graph for 918 test instances (rectangles of at most four steps per direction; interior fault sets of size at most three, and selected boundary fault sets), checks that its graph-search components equal fault-sign classes, verifies that every class is a full lattice interval, and checks 360652 ordered route-pair distances against the area formula. The second program counts the surviving diagonal-fault routes by a two-dimensional lattice dynamic program for all \(1\leq k\leq12\), independently evaluates the Catalan formula, and tests the separate-sign construction for all \(2^{10}\) words at \(k=10\). These finite tests support, but are not substitutes for, the proofs above.

## Relationship to prior work

Asplund and collaborators establish the intact grid shortest-path staircase model and its local adjacent-swap representation. Gajjar and collaborators establish algorithms and complexity results for general shortest-path reconfiguration, including exact permutation distances in intact hypercubes. Bonsma gives a polynomial-time planar decision method. A previously available one-fault rectangular-grid classification identifies two median components and explicit single-fault sizes and diameters; those results are not claimed as new. None of these statements supplies the arbitrary simultaneous-fault interval decomposition, its exact all-pairs metric for each signature, the sharp \(2^k\)-component law, or the diagonal-fault Catalan survivor enumeration as a combined theorem. No claim of exhaustive coverage of unindexed literature is made.

## Limitations

The theorem requires original-distance (north/east) routes between opposite corners, not arbitrary shortest paths between unrelated terminals. It does not cover longer detours caused by a complete original-distance blockage, three-dimensional grids, or edge-failure models. The proof is self-contained but its claim of originality is based on a bounded literature and record comparison; unknown equivalent formulations remain possible. Independent mathematical validation has not been performed.

## References

1. J. Asplund, K. Edoh, R. Haas, Y. Hristova, B. Novick, B. Werner, *Reconfiguration graphs of shortest paths*, arXiv:1705.09385 (first public 2017-05-25), particularly Section 6.
2. K. Gajjar, A. V. Jha, M. Kumar, A. Lahiri, *Reconfiguring Shortest Paths in Graphs*, arXiv:2112.07499 (first public 2021-12-14); AAAI 2022 and Algorithmica 2024 versions.
3. P. Bonsma, *Rerouting shortest paths in planar graphs*, arXiv:1204.5613 (2012), Discrete Applied Mathematics 231 (2017), 95–112.
4. Classical order-ideal/distributive-lattice representation and Catalan generating-function identity (standard mathematical background).
