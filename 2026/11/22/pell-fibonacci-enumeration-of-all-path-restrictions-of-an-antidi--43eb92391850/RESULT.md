# Pell–Fibonacci enumeration of all path restrictions of an antidiagonal vertex bifiltration

## Finding

**Theorem.** Let \(n\ge1\), and let \(K_n\) be the zero-dimensional simplicial complex with **labelled** vertices \(v_1,\ldots,v_n\). On the parameter square \([0,n+1]^2\), give vertex \(v_i\) the unique entrance coordinate \(c_i=(i,n+1-i)\): it belongs to \(F_n(x,y)\) exactly when \(x\ge i\) and \(y\ge n+1-i\). Consider every continuous, coordinatewise nondecreasing path from \((0,0)\) to \((n+1,n+1)\). Restrict \(F_n\) to each path, identifying restrictions by **simplicial equivalence** (equality of the labelled filtrations after renumbering their distinct simplex entrance times). Identify their degree-zero persistence diagrams by **combinatorial equivalence** (renumbering distinct birth and death coordinates).

Each simplicial class has a unique sequence of disjoint, nonempty arrival blocks \(B_1,\ldots,B_t\). The first block is a singleton or two consecutive labels; subsequently each block consists of **the immediate outside left neighbor, the immediate outside right neighbor, or both neighbors together** of the already present integer interval. Conversely every sequence obeying precisely these rules occurs. In particular every block has size one or two, and the accumulated labels are always a contiguous integer interval. If \(b=(b_1,\ldots,b_t)\) is a composition of \(n\) with parts in \(\{1,2\}\), and \(s(b)\) is the number of parts equal to \(1\), **exactly**

\[
2^{s(b)-\mathbf 1_{\{b_1=1\}}}
\]

simplicial equivalence classes have combinatorial degree-zero barcode type \(b\). In particular, the numbers of distinct simplicial classes and combinatorial barcode classes are respectively

\[
S_n=\frac{(1+\sqrt2)^n+(1-\sqrt2)^n}{2},\qquad B_n=F_{n+1},
\]

where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). The simplicial count begins \(1,3,7,17,41,99\), while the barcode count begins \(1,2,3,5,8,13\). Moreover \(S_n/B_n\) grows exponentially, with exponential base \((1+\sqrt2)/\varphi\), where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope

The vertices are labelled throughout and no higher-dimensional simplex occurs. The parameter path is continuous, coordinatewise nondecreasing, and has the stipulated endpoints. Its speed and pauses are irrelevant: equivalence renumbers distinct entrance events but preserves simultaneous arrivals. All bars in degree-zero persistence are essential and are counted with multiplicity. The comparison uses the definitions of simplicial equivalence and combinatorial diagram equivalence introduced in the cited directed-cubical framework (Definitions 4.10 and 4.3, respectively). The source is a **one-critical**, not an arbitrary, bifiltration; its entrance coordinates are mutually incomparable.

A composition \(b\) is a finite ordered list of parts equal to \(1\) or \(2\) whose sum is \(n\). The term \(s(b)\) counts singleton parts. A simultaneous birth of two isolated vertices contributes two essential bars with one common birth coordinate.

## Proof

**1. Interval states and admissible events.** At time \(t\), with path position \((x(t),y(t))\), the present vertices are exactly those with

\[
n+1-y(t)\le i\le x(t),\qquad 1\le i\le n.
\]

Thus the set of present labels is empty or a contiguous integer interval \([L,R]\cap\mathbb Z\). As both coordinates increase continuously, \(L\) may only decrease and \(R\) may only increase. Each new event can cross at most one previously unmet integer threshold for \(x\) and at most one for \(y\), so it adds only the immediately adjacent label on the right, the immediately adjacent label on the left, or both together. The initial nonempty event adds one label or a pair of consecutive labels. Any pause or movement that introduces no vertex can be deleted from the event record.

**2. Realizability of every such history.** Begin at \((0,0)\). To make the first birth be just label \(i\), move along a straight segment to \((i,n+1-i)\). To give the first simultaneous birth to labels \(i,i+1\), move along a straight segment to \((i+1,n+1-i)\). Along either segment no vertex enters before its endpoint, by the antichain property of the entrance coordinates. When the currently present interval is \([L,R]\), its corner position is \((R,n+1-L)\). To add its left neighbor move vertically one unit; to add its right neighbor move horizontally one unit; to add both simultaneously traverse the unit diagonal to \((R+1,n+2-L)\). The new vertex or vertices enter exactly at the next corner. Once all labels have arrived, move to \((n+1,n+1)\). The resulting continuous nondecreasing polygonal path realizes exactly the prescribed blocks. Consequently the interval histories are precisely the simplicial equivalence classes: no finer information survives renumbering distinct event times.

**3. Exact fibers over barcodes.** The restricted degree-zero barcode has one essential interval for each vertex, and no finite-death intervals. It therefore remembers only the *ordered sizes* of the arrival blocks, giving a composition \(b\). Conversely fix \(b\), assign each singleton block **after the first block** independently to the current left or right boundary, and assign each doubleton block after the first to both boundaries. The number of such binary decisions is \(s(b)-\mathbf1_{\{b_1=1\}}\). These decisions uniquely determine the initial interval position: choose the first singleton \(i=1+\ell\), or the first pair \(\{i,i+1\}\) with \(i=1+\ell\), where \(\ell\) is the number of later left-boundary additions (one per doubleton, one per left-selected singleton). The total number of labels guarantees that the initial interval and every expansion lie in \([1,n]\). Hence every decision pattern is realized, distinct patterns produce distinct labelled histories, and the fiber size is exactly \(2^{s(b)-\mathbf1_{\{b_1=1\}}}\).

**4. Counting.** The barcode-type compositions satisfy \(B_n=B_{n-1}+B_{n-2}\), with \(B_1=1\), \(B_2=2\), so \(B_n=F_{n+1}\). Let \(D(a,b)\) be the Delannoy number of paths from \((0,0)\) to \((a,b)\) using unit left, up, and diagonal advances, with generating function

\[
\sum_{a,b\ge0}D(a,b)u^av^b=\frac{1}{1-u-v-uv}.
\]

After a singleton initial block \(i\), there are \(i-1\) left additions and \(n-i\) right additions, hence \(D(i-1,n-i)\) histories. After an initial pair \(i,i+1\), there are \(i-1\) left and \(n-i-1\) right additions. Therefore

\[
S_n=\sum_{a+b=n-1}D(a,b)+\sum_{a+b=n-2}D(a,b),
\]

where the second sum vanishes for \(n=1\). Diagonal specialization yields

\[
\sum_{n\ge1}S_nz^n=\frac{z(1+z)}{1-2z-z^2}.
\]

Thus \(S_1=1\), \(S_2=3\), \(S_n=2S_{n-1}+S_{n-2}\) for \(n\ge3\), with the stated closed form. As \(F_{n+1}\sim\varphi^{n+1}/\sqrt5\), the ratio \(S_n/B_n\) has exponential base \((1+\sqrt2)/\varphi>1\).

## Verification

Run `python3 check_antichain.py` from the package directory. It enumerates all labelled interval-growth histories for sizes \(1\le n\le10\), constructs and independently reads a monotone polygonal path witness for each, and checks the exact Delannoy count, Pell-type recurrence, number of Fibonacci barcode types, and the exact fiber formula for every composition. It also independently enumerates every east/north/diagonal lattice path in the entire parameter square for \(1\le n\le6\) and verifies that these paths give exactly the interval histories. All \(5,740\) interval histories through \(n=10\) and all \(59,708\) exhaustively enumerated lattice paths through \(n=6\) pass. The checker uses rational event times, not floating-point approximations. The general theorem follows from the preceding proof; the finite checks are not a proof for unbounded \(n\).

## Relationship to prior work

Belton, Brooks, Fajstrup, Fasy and Vidaurre introduce the two equivalence relations and the extended fibered barcode in arXiv:2611.00261v1, Definitions 4.3, 4.10 and Section 5, and identify class enumeration as a direction in Conjecture 7.1. Their work does not give the antidiagonal isolated-vertex classification, its Pell/Fibonacci counts, or its exact equivalence-class fiber sizes. Delannoy paths and their generating functions are classical; their numerical enumeration is not claimed as new. The point is the geometric identification with *all* continuous path restrictions, the exact labelled-to-unlabelled barcode quotient, and explicit realizable representatives. The standard Delannoy-path literature concerns lattice-path structures rather than these filtration equivalence relations.

## Limitations

This classification applies only to zero-dimensional complexes with distinct antidiagonal one-critical entrance points, including paths allowed to enter two vertices simultaneously. It is not a classification of general bifiltrations or of equivalent paths in an arbitrary entrance complex. The barcode counts refer to degree-zero combinatorial diagrams with essential bars; they do not describe the numerical birth parameters, stability, or higher-dimensional barcodes. Formula sequences already occur in elementary combinatorics; the novelty claim is their proven correspondence with this natural filtered-topological family. An unindexed equivalent reformulation remains a publication-priority risk; independent review has not been performed.

## References

1. R. Belton, R. Brooks, L. Fajstrup, B. T. Fasy and E. Vidaurre, *A Directed Cubical Framework for k-critical Bipersistence Modules*, arXiv:2611.00261v1 (first public 2026-10-30), https://arxiv.org/html/2611.00261v1 . Definitions 4.3 and 4.10 and Conjecture 7.1.
2. J.-M. Autebert and S. R. Schwer, *On Generalized Delannoy Paths*, SIAM J. Discrete Math. 16 (2003), 208–223, https://doi.org/10.1137/S0895480101387406 . Classical Delannoy-path context.
