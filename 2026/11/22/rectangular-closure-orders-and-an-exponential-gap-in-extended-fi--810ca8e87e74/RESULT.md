# Rectangular-closure orders and an exponential gap in extended fibered persistence

## Finding

Let a finite one-critical bifiltration over \([0,L]^2\) have distinct noninitial simplex grades \(P\subset(0,L)^2\). A permutation of \(P\) is the strict entrance order of a continuous coordinatewise nondecreasing path from \((0,0)\) to \((L,L)\) if and only if every prefix contains all grades dominated by its coordinatewise maximum.

For the antidiagonal grades \(p_i=(i,n+1-i)\), \(1\le i\le n<L\), there are \(2^{n-1}\) strict monotone-path orders. An explicit wedge-of-spheres bifiltration realizes all of these as different degree-labelled combinatorial barcodes. In contrast, positive-slope affine lines, with arbitrary intercept and entrances computed on the **full line**, realize at most
\[
1+M+\binom M2,\qquad M=\binom n2,
\]
strict orders. For this full-line convention the first gap in the family is at \(n=6\): exactly 30 line orders versus 32 path orders. At \(n=13\) the upper bound is 3082 versus 4096 path orders. These comparisons are exponential versus at most quartic in the number of distinct grades, not in the number of simplices.

The line upper bound and the six-grade forbidden order also apply to lines clipped to any fixed box when all grades must enter within the segment. The exact full-line counts apply to clipped lines only with sufficient padding; for the 30 six-grade orders, \([0,37]^2\) suffices. The first-gap assertion at six is not a claim for an arbitrary fixed clipping box.

## Assumptions and scope

A simplex is present exactly in the coordinatewise upper set of its unique grade; different simplices may enter at the same grade. The initial complex is already present at \((0,0)\). A strict order here excludes simultaneous arrivals of *distinct* grades. In combinatorial barcodes, replace the distinct event times by their common increasing integer indices across all homology degrees, and retain the degree of every interval; there is no separate reindexing for each degree.

For a full affine line, its grade entrance is the first point on the line that dominates that grade, with the line oriented in the increasing direction. This is equivalently the restriction of an extension with the initial complex present everywhere and all noninitial simplices assigned the same principal upper sets as before. For a clipped affine line, only strict orders with every grade entrance on the clipped segment are counted. Monotone-path orders always refer to paths joining the two specified box corners.

## Proof

**Rectangular criterion.** Write \(Q(A)\) for the coordinatewise maximum of a nonempty grade set \(A\), set \(Q(\varnothing)=(0,0)\), and put \(\operatorname{cl}(A)=\{p\in P:p\preceq Q(A)\}\). If \(A\) is the prefix at some entrance time, the current point dominates \(Q(A)\) and must already contain all its dominated grades. Thus \(A=\operatorname{cl}(A)\). Conversely, write \(A_j\) for the successive closed prefixes of a permutation. Join \(Q(A_{j-1})\) to \(Q(A_j)\) by a line segment. At least one coordinate maximum increases (the new grade was not in the closure of \(A_{j-1}\)), and the new grade takes that maximum value, so cannot enter before the endpoint. No grade outside \(A_j\) can enter along the segment, since each segment point is dominated by \(Q(A_j)\). Concatenating these segments and then joining \(Q(P)\) to \((L,L)\) realizes the strict permutation.

**Antidiagonal and barcode.** A nonempty grade set on the antidiagonal has as closure the index interval between its smallest and largest indices. Starting at index \(i\), a strict order must interleave \(i-1\) left expansions with \(n-i\) right expansions, giving \(\binom{n-1}{i-1}\) orders. The sum over \(i\) is \(2^{n-1}\). To realize these as barcodes, start with one vertex \(*\) and adjoin at grade \(p_i\) all noninitial simplices of a simplicial \(i\)-sphere, the boundary of an \((i+1)\)-simplex, with no other shared vertex except \(*\). At any parameter point the complex is the wedge of the spheres that have entered. Over any field there is one infinite interval in each of degrees \(1,\ldots,n\), born at the common event index of the corresponding grade. The degree-labelled list with common indexing thus determines the permutation, and no other data change between orders.

**Full affine lines.** For \(y=mx+c\), \(m>0\), put \(w=1/m\), \(z=(n+1-c)/m\) and parameterize by increasing \(x\). The entrance coordinate is \(t_i=\max(i,z-wi)\). For \(i<j\), the pair satisfies \(t_i<t_j\) exactly when \(z<j+wi\), with equality exactly at \(z=j+wi\). Indeed \(i<j\) and \(z-wj<z-wi\), so the sign is fixed by comparing \(z-wi\) with \(j\). Thus strict orders are constant on the open chambers of the at most \(M\) lines \(z=j+wi\) in the half-plane \(w>0\). There are at most \(1+M+\binom M2\) chambers: each successive line adds at most its number of intersections with previous lines plus one. Restricting the arrangement to the half-plane can only reduce the count, since every chamber is convex.

**Exact small counts.** Partition \(w>0\) at all positive intersections of the tie lines. In each resulting open slab, choose one rational \(w\) and one rational \(z\) between each pair of successive tie ordinates, plus one on either exterior. Sorting the exact \(t_i\) for these pairs and deduplicating gives all strict orders: the tie-ordinate order does not change in a slab, and any strict-order chamber intersecting a slab boundary also meets an open slab. The resulting full-line counts at \(n=1,2,3,4,5,6\) are \(1,2,4,8,16,30\). Every full-line order is a monotone-path order: a line segment covering all its events can be connected to the box corners for sufficiently large \(L\), and the rectangular criterion then also realizes the same order for any \(L>n\) by its maximum-coordinate construction. Thus equality of the counts for \(n\le5\) means equality of the order sets. The two orders missed at six are \((3,4,5,2,1,6)\) and its index reflection \((4,3,2,5,6,1)\).

For the first missing order, the path through the successive coordinate maxima
\[
(0,0),(3,4),(4,4),(5,4),(5,5),(5,6),(6,6)
\]
and then \((L,L)\) realizes it. An affine line with that order would satisfy \(t_3<t_4<t_5\), which forces \(t_4=4\) and \(t_5=5\) because the other branch is decreasing. Then \(t_5<t_2\) and \(t_3<t_4\) require \(5+2w<z<4+3w\), hence \(w>1\). But \(t_5=5\) forces \(t_6=6\), and \(t_1<t_6\) requires \(z<6+w\), giving \(w<1\). The second obstruction follows by interchanging the two coordinate axes, which reflects the index order and preserves positive-slope lines.

**Clipping.** For the event points on the line, the maximum \(x\) is \(\max(n,z-w)\). The maximum \(y\) is \(\max(n,n+1+(n-z)/w)\). Both coordinates of each event point are positive since it dominates its grade. Thus for \(L>n\), every event belongs to the closed box exactly when
\[
n-w(L-n-1)\le z\le L+w.
\]
Full-line upper bounds remain valid under these extra restrictions. At any fixed \(n\) there are finitely many strict orders, and the finite witnesses can all fit in a sufficiently large square. At \(n=6\), the supplied rational witnesses have entrance coordinates bounded by \(x\le37/4\) and \(y\le36\), giving exact equality with the full-line count in \([0,37]^2\) or any larger square.

## Verification

Run `python3 CHECK.py` with `LINE_WITNESSES.csv` in the same directory. It compares closed-prefix tests to finite lattice-path enumerations and uses the rational slab procedure for **unclipped** affine lines. In particular, it obtains 30 line orders at six and 638 at thirteen; the 30 CSV rows witness the complete six-grade set. For the padded-box check, in each CSV row compute \(x_i=\max(i,z-wi)\) and \(y_i=n+1+(x_i-z)/w\) to check the prescribed coordinate bounds. The all-size closure, counting and upper-bound arguments do not depend on finite extrapolation.

## Relationship to prior work and limitations

Belton, Brooks, Fajstrup, Fasy and Vidaurre, *A Directed Cubical Framework for k-critical Bipersistence Modules*, [arXiv:2611.00261v1](https://arxiv.org/html/2611.00261v1), define simplicial equivalence and compare line restrictions with directed paths; §7 raises class counting. Bapat et al., *Computing the Matching Distance of 2-Parameter Persistence Modules from Critical Values*, [arXiv:2210.12868v3](https://arxiv.org/html/2210.12868v3), use arrangements to partition positive-slope lines for matching-distance computations. The antidiagonal isolated-vertex enumeration in [the Pell–Fibonacci classification](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-pell-fibonacci-enumeration-of-all-path-restrictions-of-an-antidi--43eb92391850) already implies the strict simplicial order count as its all-singleton-arrival case; that count alone is not the contribution here. The comparison here is between distinct graded combinatorial barcodes on a particular family, with a uniform upper bound and a sharp small full-line count. It does not address tied events, multi-critical supports, counts for every clipping box, or numerical (unreindexed) persistence barcodes. Historical priority beyond these comparisons is not asserted.
