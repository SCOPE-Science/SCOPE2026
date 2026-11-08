# First nontrivially fragmented optimum global locating-domination slide graph in wheels: \(W_{14}\)

## Finding
Let \(W_n=K_1\vee C_{n-1}\), for integers \(n\ge4\), with its hub and cyclically ordered rim vertices. A *global locating-dominating set* \(S\) is locating-dominating simultaneously in \(W_n\) and its simple complement: every vertex outside \(S\) has a nonempty, distinct open-neighborhood trace on \(S\) in each graph. Let \(\mathcal R_n\) have **all minimum-cardinality global locating-dominating sets** as vertices, and join two states precisely when one selected vertex slides across an edge of \(W_n\), leaving another minimum-cardinality global locating-dominating set.

The first wheel whose graph \(\mathcal R_n\) has at least two connected components **containing edges** is \(W_{14}\). Moreover,
\[
\lambda_g(W_{14})=6,\qquad |V(\mathcal R_{14})|=26,
\qquad \mathcal R_{14}\cong 13K_2.
\]
The 26 optimal codes constitute a single orbit of the order-26 dihedral automorphism group acting on the thirteen rim positions, and exactly two rotation orbits of size thirteen; every legal slide exchanges these rotation orbits. In particular, every optimum permits exactly one slide, but the 13 resulting pairs cannot communicate.

Here is the exact initial-range classification, with each component multiset written as its isomorphism type or as one connected component of the specified size:

| Wheel | Minimum size | Number of optima | Number of slide edges | Components |
| --- | ---: | ---: | ---: | --- |
| \(W_4\) | 4 | 1 | 0 | \(K_1\) |
| \(W_5\) | 3 | 4 | 0 | \(4K_1\) |
| \(W_6\) | 3 | 5 | 0 | \(5K_1\) |
| \(W_7\) | 4 | 20 | 36 | connected |
| \(W_8\) | 4 | 21 | 28 | connected |
| \(W_9\) | 4 | 8 | 0 | \(8K_1\) |
| \(W_{10}\) | 5 | 54 | 99 | connected |
| \(W_{11}\) | 5 | 35 | 40 | connected |
| \(W_{12}\) | 5 | 11 | 0 | \(11K_1\) |
| \(W_{13}\) | 6 | 96 | 156 | connected |
| \(W_{14}\) | 6 | 26 | 13 | \(13K_2\) |

The previously known scalar global location-domination number of a wheel is not a novelty claim. The contribution is the complete optimum-configuration mobility pattern at this first threshold and its sharp initial-range minimality.

## Assumptions and scope
All graphs are finite, simple, undirected, and **labeled**. For a graph \(G\), a locating-dominating set \(S\) requires, for each \(v\notin S\), a nonempty trace \(N_G(v)\cap S\), and requires all such traces to differ. Global means this also holds in \(\overline G\). A token slide replaces \(u\in S\) by \(v\notin S\) only when \(uv\in E(G)\); no intermediate nonoptimal code is permitted. A connected component containing edges is called *nontrivial*. No conclusion is claimed for the structure of \(\mathcal R_n\) when \(n>14\).

For the main case, index rim positions by \(\mathbb Z/13\mathbb Z\) and write the hub as \(h\). A representative code is
\[
\{h,0,2,4,7,9\}.
\]

## Proof
**1. Reduce both-graph location-domination to circular gaps.** Every global locating-dominating set of a wheel contains its hub \(h\), since the hub is isolated in the complement. Put \(S=\{h\}\cup T\), where \(T\) contains \(p\ge3\) rim vertices in cyclic order and the rim length is at least six. Every outside rim vertex has hub \(h\) in its wheel trace, while its complement trace is nonempty automatically (it has at most two rim neighbors, but \(p\ge3\) selected rim vertices). Distinctness in both graphs is therefore equivalent to distinctness of the rim traces \(N_{C_r}(v)\cap T\) for outside positions \(v\in C_r\setminus T\). The rim traces are of size zero, one, or two.

Let \(d_1,\ldots,d_p\) be the cyclic distances between consecutive members of \(T\), so \(d_i\ge1\) and \(\sum_i d_i=r\). A gap of length at least five contains at least two zero-trace vertices and is forbidden. A length-four gap contains precisely one zero-trace vertex, so at most one such gap is allowed. A selected rim vertex bordered on both sides by gaps of length at least three gives the same singleton trace to its two adjacent outside vertices, so these two neighboring long gaps are forbidden. Conversely, if all gaps are at most four, at most one is four, and no two cyclic neighbors are at least three, every zero trace is unique, every singleton trace is unique, and each two-element trace comes from the sole intermediate vertex of a length-two gap (a second vertex with that pair of rim neighbors cannot occur on a rim of length at least six). Thus **the three gap conditions are necessary and sufficient**.

**2. Minimum size and all optimum states at \(n=14\).** Here \(r=13\). For \(p\le4\), the gap conditions prohibit a sum of thirteen: with no length-four gap the maximum sum for four entries is ten, while with exactly one four it is at most eleven. Smaller \(p\) cannot help. Therefore at least five rim vertices and the hub are necessary. For \(p=5\), attaining sum thirteen forces the cyclic gap multiset \(\{2,2,2,3,4\}\), with the length-three and length-four gaps nonadjacent. Conversely each such cyclic gap word satisfies the conditions. These are exactly the cyclic rotations of
\[
(2,2,3,2,4)\quad\text{and}\quad(2,2,4,2,3).
\]
The two forms are reflections, not rotations, of each other. Each has thirteen distinct labeled rim translations because the unique length-four gap pins the rotation. Hence there are exactly \(2\cdot13=26\) minimum global locating-dominating sets, all dihedrally equivalent. A chosen set with positions \(0,2,4,7,9\) realizes the first form.

**3. Single-slides give a perfect matching.** A legal slide changes exactly the two cyclic gaps incident to the moving rim vertex, increasing one by one and decreasing the other by one. The hub cannot move because every global code contains it. The only admissible five-gap multiset is \(\{2,2,2,3,4\}\). A legal move must therefore interchange a neighboring \(2\) and \(3\) (a \(3\)--\(4\) pair is forbidden by the gap condition and other changes alter the multiset). From the word \((2,2,3,2,4)\), only moving the \(3\) **away** from the \(4\) yields another admissible word; moving it toward \(4\) makes them adjacent. Thus the representative state has exactly one legal move. Dihedral transitivity gives degree one at every state; the 26 states form \(13K_2\). Its unique slide exchanges the two rotational forms, proving the orbit assertion.

**4. Sharpness of the first occurrence.** The finite initial range \(4\le n\le13\) is exhaustively classified by the two standalone programs provided. The first enumerates every subset at successive cardinalities and independently tests nonempty pairwise-distinct open-neighborhood traces in both the graph and its complement, then constructs all legal slides. The second enumerates the mathematically characterized cyclic gap words and their legal slides for \(7\le n\le14\). Both use exact integer/set logic and return the table above. For each preceding wheel, either all codes are frozen or the reconfiguration graph is connected, so no preceding wheel has two distinct nontrivial components. The special small wheels \(W_4,W_5,W_6\) are directly exhausted by the first program.

## Verification
Requires Python 3 standard library only. Run `python3 check_neighborhoods.py` and `python3 check_gaps.py` from a directory containing the two attached scripts. The first covers all sizes \(4\le n\le14\), while the second independently uses the gap characterization for \(7\le n\le14\). Expected outputs are included as `neighborhood_check.txt` and `gap_check.txt`. Both scripts assert every reported count and component size, and the second checks the two rotational orbits and degree one at the threshold.

The proof of \(\mathcal R_{14}\cong13K_2\) is direct; the finite first-occurrence assertion uses complete explicitly bounded enumeration rather than a purported infinite extrapolation. No untested larger-wheel claim is made.

## Relationship to prior work
Hernando, Mora and Pelayo, *On global location-domination in graphs* (arXiv:1312.0772v1, publicly posted December 3, 2013), introduce the global locating-dominating parameter and establish \(\lambda_g(W_n)=\lceil(2n+1)/5\rceil\) for \(n\ge8\), together with small cases. The scalar optimum value here is therefore established prior art. Their Sections 2–4 and Tables 1–2 do not furnish the configuration graph, its dihedral orbit, or the first nontrivial fragmentation cutoff.

Teshima's dissertation *The i-Graph and Other Variations on the \(\gamma\)-Graph* (2022), Chapter 2, provides the general locating-domination reconfiguration model and realizability constructions; these do not determine the optimum global locating-domination slide graph of the fixed wheel \(W_{14}\). Honkala, Hudry and Lobstein's *On the ensemble of optimal dominating and locating-dominating codes in a graph* (2015) is pertinent to optimal-code ensembles and Johnson-subgraph interpretations, but a full open copy was not accessible. Its available abstract does not settle the specific wheel-global condition. This remains a priority risk, not a negative full-text finding.

## Limitations
This is an exact finite threshold result, not an infinite classification of all wheel reconfiguration graphs. The term *first* refers to wheels in increasing order beginning with \(W_4\), and specifically to **at least two components each having an edge**; smaller wheels can be disconnected as unions of isolated points. Computational crosschecks verify finite instances and the initial cutoff, not unbounded extrapolations. Historical-priority risk persists for inaccessible or unindexed literature; independent scholarly audit has not been carried out.

## References
1. C. Hernando, M. Mora, I. M. Pelayo, *On global location-domination in graphs*, arXiv:1312.0772v1 (2013-12-03), https://arxiv.org/abs/1312.0772 .
2. L. E. Teshima, *The i-Graph and Other Variations on the \(\gamma\)-Graph*, Ph.D. thesis, University of Victoria (2022), https://dspace.library.uvic.ca/items/740e5c10-d1aa-4992-970b-3711b397f7f5 .
3. I. Honkala, O. Hudry, A. Lobstein, *On the ensemble of optimal dominating and locating-dominating codes in a graph*, Information Processing Letters **115** (2015), 699–702, https://doi.org/10.1016/j.ipl.2015.04.005 (abstract consulted; full text unavailable).
