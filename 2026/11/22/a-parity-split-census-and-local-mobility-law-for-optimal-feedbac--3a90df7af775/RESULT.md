# A parity-split census and local mobility law for optimal feedback sets on cyclic prisms

## Finding

For every integer \(n\ge3\), let \(G_n=C_n\square K_2\), with vertices \((i,r)\) for \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\), and edges between consecutive columns in the same rail and between the two rails within a column. A **feedback vertex set** (FVS) \(S\) is one for which \(G_n-S\) is a forest. Let \(\mathcal F_n\) be the family of *minimum-cardinality* FVSs. Then the minimum cardinality is \(\lfloor n/2\rfloor+1\), and the complete all-length enumeration is

\[
|\mathcal F_{2m+1}|=(2m+1)2^m\quad(m\ge1),\qquad
|\mathcal F_{2m}|=(2m)(3m+2)2^{m-2}\quad(m\ge2).
\]

The theorem also characterizes every member of these families (below). Under **optimality-preserving token sliding**, two members are adjacent when one selected vertex moves to an unselected neighbor of \(G_n\), with the new set still in \(\mathcal F_n\). If \(\mathcal T_n\) denotes this sliding graph, its degree enumerator for odd \(n\) is

\[
\sum_{S\in\mathcal F_n} t^{\deg_{\mathcal T_n}(S)}=
\begin{cases}
6t^2,&n=3,\\
20t^2,&n=5,\\
(2m+1)2^{m-2}\left(t^{m-1}+2t^m+t^{m+1}\right),&n=2m+1,\ m\ge3.
\end{cases}
\]

In particular, for every \(m\ge2\) the number of undirected token-slide edges is \((2m+1)m2^{m-1}\); for \(n=3\) it is six.

## Assumptions and scope

All cycles and prisms here are finite, simple, labelled graphs. Each column \(i\) has two vertices \((i,0)\) and \((i,1)\). Call it **empty** if neither vertex lies in \(S\), **single** if exactly one lies in \(S\), and **double** if both lie in \(S\). The following conditions characterize all minimum FVSs, with no equivalence under rotations, reflections, or rail interchange being taken in the counts.

For odd \(n=2m+1\), there are exactly \(m\) empty columns, no double column, and the empty columns are pairwise nonconsecutive around the cycle. There is one run of two consecutive single columns; all other runs of singles have length one. **The selected vertices in the length-two run lie on different rails.** All other selected rails are independent choices.

For even \(n=2m\), there are precisely two possibilities:

1. **Double type:** Exactly one double column, exactly \(m\) empty columns, and the empty and occupied columns alternate. The other \(m-1\) occupied columns are single; their selected rails are arbitrary.
2. **Single-only type:** No double column and exactly \(m-1\) pairwise nonconsecutive empty columns. Between consecutive empty columns are runs of single columns. Either there is one run of length three and all other runs have length one, or there are two runs of length two and all other runs have length one. Among the two adjacent pairs of single columns occurring inside the long runs, **at most one pair selects vertices on the same rail**. (For a length-three run the two pairs share a middle column.)

These cases are disjoint. No assertions about the exact sliding diameter for even prisms or shortest routes are made.

## Proof

**1. A degree identity and sharp minimum size.** The prism has \(2n\) vertices, \(3n\) edges and degree three at every vertex. For any \(k\)-element set \(S\), write \(e(S)\) for the number of edges with both endpoints in \(S\). Removing \(S\) leaves \(3n-3k+e(S)\) edges and \(2n-k\) vertices. If the remainder is a forest with \(c\ge1\) components, then

\[
2k-n=c+e(S)\ge1.
\]

Consequently any FVS has at least \(\lfloor n/2\rfloor+1\) vertices. The explicitly described odd and even families below are nonempty and are forests, proving this lower bound sharp without relying on an earlier minimum-number theorem.

**2. The column obstruction and cycle criterion.** Two adjacent empty columns leave their four-cycle intact; hence empty columns are nonconsecutive in every FVS. In a configuration with no double column and isolated empty columns, every selected column retains only the vertex on the *opposite* rail. No proper interval of columns can contain a cycle: any intact rung is isolated from every other intact rung by at least one single column, so between consecutive intact rungs there is at most one horizontal connecting path. A cycle could therefore exist only by closing a chain all the way around the cyclic column order. The connecting chain through a run of single columns survives precisely when all its selected vertices are on the same rail. Thus the complement is acyclic exactly when at least one run of two or more consecutive singles contains two neighbors selected on different rails. A double selected column leaves no vertex in that column, breaks the cyclic chain, and yields a forest when all empty columns are isolated. These assertions remain valid when there is only one empty column, interpreting the cyclic chain from that rung back to itself.

**3. Exhaustive classification.** Put \(k=\lfloor n/2\rfloor+1\). If there are \(d\) double columns, there are \(n-k+d\) empty columns. Because empty columns form an independent set in \(C_n\), their number is at most \(\lfloor n/2\rfloor\). For odd \(n=2m+1\), this forces \(d=0\), with exactly \(m\) empty and \(m+1\) single columns. Exactly one run of singles has length two, all others length one. The cycle criterion forces its adjacent selected rails to be different, proving the odd characterization.

For even \(n=2m\), the same inequality forces \(d\le1\). If \(d=1\), the \(m\) empty columns alternate with occupied columns and the double column breaks the cyclic chain; this gives the double type. If \(d=0\), \(m-1\) empty columns separate \(m+1\) singles. The two additional singles beyond one per gap appear either together (one length-three run) or separately (two length-two runs). In either case there are exactly two adjacent pairs of occupied columns. By the degree identity any forest with \(k=m+1\) must satisfy \(e(S)\le1\). Here \(e(S)\) is exactly the number of those two pairs selecting the same rail. Conversely, if at most one of the two pairs selects the same rail, at least one chain is broken; the cycle criterion gives a forest. This proves both necessity and sufficiency of all cases.

**4. Exact count.** In an odd prism, the location of the unique double-length run of selected columns can be chosen in \(n\) ways. Its two selected rails must differ (two choices), while the other \(m-1\) selected rails can be chosen independently, producing \(n2^m\).

For even \(n=2m\), the alternating double type has \(2m\) choices for the double column and \(2^{m-1}\) remaining rail assignments, contributing \(n2^{m-1}\). In the no-double type, one length-three run has \(n\) locations; its three rails have six allowed patterns (eight minus the two constant patterns), while the other \(m-2\) singleton columns contribute \(2^{m-2}\), giving \(6n2^{m-2}\). Finally, two length-two runs give \(n(m-2)/2\) unlabeled placements of the empty-column pattern: choose two distinguished gaps among \(m-1\) cyclic gaps. On their four selected vertices, of the sixteen rail assignments exactly twelve have at most one equal-rail adjacent pair. The other \(m-3\) singles contribute \(2^{m-3}\). This type therefore contributes \(3n(m-2)2^{m-2}\) for \(m\ge3\), and contributes zero at \(m=2\). Summing yields \(n(3m+2)2^{m-2}\).

**5. Odd token-slide degrees.** For \(n=2m+1\), every one of the \(m-1\) isolated single columns allows a vertical slide within its rung; a vertical slide at either endpoint of the unique length-two run would make its two selected rails equal and is forbidden. A horizontal slide is possible only from an endpoint of this run into the neighboring empty column. For \(m\ge3\), there are two such potential slides, each legal precisely when the nearby isolated single on its *other* side selects the opposite rail from the moved endpoint. Those two nearby single columns are distinct. Their rail choices are independent, giving zero, one or two additional slides in proportions \(1:2:1\). The degree polynomial follows. At \(m=2\), the two nearby isolated singles coincide, so exactly one of the two horizontal slides is legal and every vertex has degree two. At \(m=1\), the unique empty column accepts the two selected endpoints by horizontal slides and both moves are legal; there are no rung flips. Summing degrees and dividing by two yields the edge counts.

## Verification

Two separately written Python 3 standard-library programs are included. `verify_forest.py` constructs both rail cycles and all rungs as edges, enumerates all candidate deletion sets of the proposed minimum size for each \(3\le n\le12\), and verifies foresthood by union-find, matching precisely the column characterization and predicted count. `verify_mobility.py` builds the graph with a separate edge/forest checker, enumerates the complete minimum states on odd prisms \(n=3,5,7,9,11\), and verifies the degree polynomial and edge totals from explicit legal slides. Run `python3 verify_forest.py` and `python3 verify_mobility.py` from the containing folder. These finite checks are corroboration, **not** a substitute for the unrestricted proofs above.

## Relationship to prior work

Verma and Binwal establish the minimum decycling number of prisms and present example minimum sets, but their six-page paper does not enumerate all optimal sets or determine their local move degrees [1]. Bousquet and coauthors establish broad connectivity of fixed-cardinality FVS reconfiguration on planar subcubic graphs under **unrestricted** one-vertex exchanges [2]. Their connectivity theorem implies unrestricted exchange connectivity here; it neither supplies the all-length multiplicity nor the **adjacent-edge slide** degree polynomial. The present claim is about complete minimum-set classification, counting, and a stricter local movement rule; general FVS connectivity is neither claimed as a new result nor used to infer the enumerations. The alternative terms *decycling sets*, *maximum induced forests* (complements), and \(GP(n,1)\) (prism graphs) refer to the same objects.

## Limitations

The primary contribution is a structural and enumerative theorem for one natural graph family; it is not an algorithm for arbitrary graphs. The even-prism sliding graph is not metrically classified. No claim of independent formal verification or comprehensive historical uniqueness is made. A visually unavailable figure in [1] and potentially unindexed sources are residual priority uncertainties; neither contains an identified stronger theorem in the readable text.

## References

[1] V. K. Verma and J. Binwal, *Study of Decycling Number Problem in Prism Graph*, Advanced Engineering Science 55 (2023), 551–556. https://advancedengineeringscience.com/article/pdf/2023/551.pdf (journal issue dated March 2023).

[2] N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, and A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023), 114188. https://doi.org/10.1016/j.tcs.2023.114188 (public record dated October 26, 2023).

[3] C. Yang and H. Ren, *New Formulae for the Decycling Number of Graphs*, Discussiones Mathematicae Graph Theory 39 (2019), 125–141. https://geodesic.mathdoc.fr/item/DMGT_2019_39_1_a10/.
