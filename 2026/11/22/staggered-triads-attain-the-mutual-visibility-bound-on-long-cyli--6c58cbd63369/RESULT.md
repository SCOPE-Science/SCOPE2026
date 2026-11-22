# Staggered triads attain the mutual-visibility bound on long cylindrical grids

## Finding
For all integers \(s\ge 3\) and \(n\) with either \(n=6s-6\) or \(n\ge6s-4\), the ordinary mutual-visibility number of the Cartesian cylinder \(P_s\square C_n\) equals
\[
\mu(P_s\square C_n)=3s.
\]
In particular, this proves an infinite, unbounded-height and unbounded-circumference part of the conjecture of Korže and Vesel that \(\mu(P_s\square C_n)=\min\{3s,2n\}\) for \(n\ge12\). The prior upper bound \(\mu(P_s\square C_n)\le3s\) is **not** asserted to be new.

Here is a concrete optimal construction. Let \(q=\lfloor n/3\rfloor\), \(u=n-3q\), and define three column starts
\[
(b_0,b_1,b_2)=\begin{cases}
(0,q,2q+1),&u=2,\\
(0,q,2q),&u=0,1.
\end{cases}
\]
Then exactly \(3s\) selected vertices are
\[
S_{s,n}=\{(r,b_j+r):0\le r<s,\ 0\le j<3\},
\]
where the cycle coordinate is interpreted modulo \(n\). Every two selected vertices admit a shortest path whose interior avoids \(S_{s,n}\).

## Assumptions and scope
The graphs are finite, undirected and simple, and \(P_s\) has vertices \(0,\ldots,s-1\) with consecutive adjacency; \(C_n\) has vertices \(\mathbb Z/n\mathbb Z\) with consecutive cyclic adjacency. Vertices of their Cartesian product are pairs \((r,c)\), and the distance formula is
\[
d((r,c),(t,d))=|r-t|+\min\{(d-c)\bmod n,(c-d)\bmod n\}.
\]
An ordinary mutual-visibility set \(S\) has, for each pair of distinct vertices in \(S\), a shortest connecting path containing no other member of \(S\). No total-, dual-, outer-, or lower-visibility variant is being claimed. The parameter regime is exactly \(s\ge3\) and \(n\in\{6s-6\}\cup\{6s-4,6s-3,\ldots\}\); it does not assert anything about \(n=6s-5\) or other uncovered shorter circumferences.

## Proof
**Upper bound.** A geodesic between two vertices in the same \(C_n\)-fiber cannot leave that fiber: leaving would add at least two path-direction moves, exceeding the cyclic distance. Among any four points on a simple cycle, choose four in cyclic order. The first and third cannot be mutually visible, since each of the two cyclic arcs joining them contains one of the other two. Therefore an ordinary mutual-visibility set contains at most three points per cycle fiber, and hence has size at most \(3s\).

**Balanced-gap arithmetic.** Define the cyclic gaps \(h_j=(b_{j+1}-b_j)\bmod n\) (with the index read modulo three). The chosen starts have all three gaps equal to either \(q\) or \(q+1\). Consequently,
\[
\min_j h_j=q,\qquad \max_jh_j=\lceil n/3\rceil.
\]
For the asserted domain, direct residue-class calculation gives
\[
q\ge s+1,\qquad 2\bigl(\lceil n/3\rceil+s-1\bigr)\le n.
\]
Indeed for \(n=3q+u\), the second inequality is equivalent to \(q\ge2s-2\) when \(u=0,2\) and to \(q\ge2s-1\) when \(u=1\). These inequalities hold at \(n=6s-6\) and at every \(n\ge6s-4\). The first follows from \(s\ge3\) and \(q\ge2s-2\). Therefore the three cyclic column bands
\[
B_j=\{b_j,b_j+1,\ldots,b_j+s-1\}\pmod n
\]
are disjoint and have a nonempty unoccupied gap between successive bands. There is exactly one selected vertex in each band on each row.

**Same-band pairs.** Consider distinct \((r,b_j+r)\) and \((t,b_j+t)\). First move horizontally within row \(r\) for \(|t-r|\) steps to column \(b_j+t\), then vertically along the path factor to row \(t\). This has length \(2|t-r|\), which equals the Cartesian-product distance because \(|t-r|\le s-1<n/2\). The horizontal part meets no other chosen vertex of its row, and the vertical part at column \(b_j+t\) meets no selected intermediate vertex: in band \(j\), the selected column in row \(a\) is \(b_j+a\), which is equal to \(b_j+t\) only for \(a=t\); other bands are disjoint. Thus this is a free geodesic.

**Different-band pairs.** A pair in distinct bands can be oriented so that the first is \((r,b_j+r)\) and the second \((t,b_{j+1}+t)\), where the band indices are cyclic. The forward cyclic distance from their columns across the gap between bands is \(h_j+t-r\). It is positive, and
\[
0<h_j+t-r\le\lceil n/3\rceil+s-1\le n/2,
\]
so the forward arc is a shortest cyclic arc (ties are allowed). Choose the column \(c=b_j+s\) modulo \(n\), which lies in the empty gap immediately after band \(j\). Move forward horizontally in row \(r\) from the first vertex to column \(c\), vertically at column \(c\) to row \(t\), then forward horizontally to the second vertex. The total length is \(h_j+t-r+|t-r|\), exactly the Cartesian-product distance. The first horizontal part starts at the sole selected column of its row in band \(j\) and leaves that band, without entering another band; the last horizontal part enters band \(j+1\) and ends at that row's sole selected column in it. Column \(c\) is wholly unselected across all rows, so the vertical part is also free. No internal vertex is selected. Hence all distinct pairs in \(S_{s,n}\) are visible.

There are precisely \(3s\) selected vertices, meeting the upper bound and proving the theorem. \(\square\)

## Verification
An executable, independent graph-search stress test is embedded as `VERIFY_CYLINDER.py`. It constructs \(S_{s,n}\), checks every unordered selected pair by breadth-first search restricted to shortest-path layers in the graph with other selected vertices forbidden, and separately constructs the explicit same-band or gap-switching geodesics from the proof. Both methods verify all \(360\) parameter pairs \(3\le s\le17\), \(n=6s-6\) or \(6s-4\le n\le6s+18\). Running `python3 VERIFY_CYLINDER.py` returns `VISIBILITY_CYLINDER_VERIFY_OK instances 360 height_range 3..17 circumference 6s-6 and 6s-4..6s+18`. This finite test is supplementary; the preceding uniform argument supplies the infinite proof.

## Relationship to prior work
Korže and Vesel, *Mutual-visibility sets in Cartesian products of paths and cycles*, first publicly available on arXiv on 2023-09-26, establish \(\mu(P_s\square C_n)\le\min\{3s,2n\}\) (Proposition 2.1), settle the two-row case (Proposition 2.2), and prove the complementary long-path regime \(s+1\ge n\ge6\) (Theorem 2.4). Their Conjecture 2.6 asks for equality with the upper bound for \(n\ge12\), irrespective of height. The present construction provides equality in the explicitly stated long-circumference region and is not implied by either of those proved regimes: for \(s\ge4\), it includes infinitely many cases with \(n>s+1\). The 2025 visibility-polynomial literature studies other variants and enumerations and does not yield this uniform cylinder construction in the inspected material. No implication from the closest indexed research on multiset metric dimension of cylinders or lower visibility on three-row tori was found: those address different invariants.

## Limitations
This result proves only a parameter subregion of the 2024 conjecture, and neither resolves all remaining circumferences nor classifies all optimum sets. The isolated absence of \(n=6s-5\) from this statement is a limitation of the demonstrated sufficient-gap construction, **not** a counterexample or a claim about the true optimum. The bibliographic novelty comparison is based on the stated full-text inspections and indexed searches, not an exhaustive proof of worldwide priority. Independent mathematical audit has not been performed.

## References
1. D. Korže and A. Vesel, *Mutual-visibility sets in Cartesian products of paths and cycles*, arXiv:2309.15201 (first public 2023-09-26), https://arxiv.org/abs/2309.15201 ; *Results in Mathematics* **79**, article 116 (2024), https://doi.org/10.1007/s00025-024-02139-x .
2. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (2021), https://arxiv.org/abs/2112.13024 .
3. C. Bujtás, S. Klavžar, and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, *Aequationes mathematicae* **99** (2025), https://doi.org/10.1007/s00010-025-01197-y .
