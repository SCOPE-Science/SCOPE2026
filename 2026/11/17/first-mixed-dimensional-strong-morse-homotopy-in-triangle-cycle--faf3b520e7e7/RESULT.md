# First mixed-dimensional strong-Morse homotopy in triangle–cycle bouquets

## Finding
For the full strong discrete-Morse matching complex of the bouquet \(G_n=C_3\vee C_n\), formed by identifying exactly one vertex of an **unfilled** triangle and an **unfilled** cycle, the first four cycle lengths satisfy
\[
\begin{aligned}
\mathcal{SM}(G_3)&\simeq\bigvee^{13}S^1,\\
\mathcal{SM}(G_4)&\simeq\bigvee^7S^2,\\
\mathcal{SM}(G_5)&\simeq\bigvee^7S^2,\\
\mathcal{SM}(G_6)&\simeq\bigvee^2S^2\vee\bigvee^{11}S^3.
\end{aligned}
\]
All equivalences are integral homotopy equivalences. The case \(n=3\) is an already known boundary case (a two-page friendship graph); the additional classifications are \(n=4,5,6\). Within the first four lengths, \(n=6\) is the first case whose reduced homology occupies two different positive degrees.

## Assumptions and scope
Fix an integer \(n\in\{3,4,5,6\}\). The vertices are \(0,1,2,3,\ldots,n+1\). The edges are \(01,12,20\) and \(03,34,45,\ldots,n(n+1),(n+1)0\). Graph triangles are *not* filled 2-simplices. All graph edges are undirected, while a vertex-edge Morse pairing is encoded by a directed incidence \((v,u)\) with \(vu\) an edge, meaning vertex \(v\) paired with edge \(vu\). A vertex ordering is a permutation of all \(n+2\) vertices. For every vertex \(v\), let \(N_{<}(v)\) be its neighbors preceding it in the ordering. On a one-dimensional simplicial complex the descending link of \(v\) is discrete on \(N_{<}(v)\), so it is a simplicial cone precisely when \(\lvert N_{<}(v)\rvert=1\). Associate to an ordering every oriented incidence \((v,u)\) with \(N_{<}(v)=\{u\}\). The full \(\mathcal{SM}(G_n)\) consists of every subset of one of these incidence sets. This is exactly the full construction in [1]; it is not the top-dimensional pure subcomplex or the ordinary Morse-matching complex.

## Proof
**Exhaustive generation.** The supplied `check_sm_mixed.py` builds the prescribed graph, lists all orientations of its undirected edges, and runs over all \((n+2)!\) vertex orders. The uniquely-earlier-neighbor criterion above enumerates every strong matching; taking all subsets yields the entire full complex. A second prefix-recursive ordering traversal computes the same maximal faces independently of the flat permutation traversal. The exact facet counts for \(n=3,4,5,6\) are respectively \(24,42,68,104\); nonempty-face counts are \(36,104,292,764\). These counts exhaust every face: no truncation or sampling occurs.

**Explicit acyclic Morse certificate.** Orient the incidence vertices lexicographically by their ordered pairs. For each \(n\), `CERT_ORDERS` supplies a permutation of these incidence-vertex indices. Process those indices in order: pair every still-unmatched face not containing the current index to its still-unmatched coface formed by inserting that index, leaving the empty face unpaired throughout. The executable verifies that every purported pair is a cover relation, that each face appears in at most one pair, and that the entire Hasse digraph with matched arrows reversed admits a topological ordering. Thus the matching is acyclic on the **complete** face poset, as required by Forman's theorem. It has the following pair counts and critical cells:

| \(n\) | Matched pairs | Critical 0-cells | Critical 1-cells | Critical 2-cells | Critical 3-cells |
|---|---:|---:|---:|---:|---:|
| 3 | 11 | 1 | 13 | 0 | 0 |
| 4 | 48 | 1 | 0 | 7 | 0 |
| 5 | 142 | 1 | 0 | 7 | 0 |
| 6 | 375 | 1 | 0 | 2 | 11 |

**Integral attaching maps.** For each matched pair \((\alpha,\beta)\) with \(\dim\beta=\dim\alpha+1\), the usual signed simplicial boundary has \(\alpha\)-coefficient \(\pm1\) in \(\partial\beta\). Eliminate that coefficient by expressing \(\alpha\) through the other codimension-one faces of \(\beta\), recursively along the acyclic matching. The source contains the exact integer recurrence `projection`, with no floating point calculations. The resulting Morse differential on the critical cells vanishes identically, including the \(2\times11\) degree-3-to-degree-2 matrix when \(n=6\). The checker independently computes all ordinary simplicial boundary ranks over \(\mathbb F_2\), agreeing with the critical-cell ranks.

For \(n=3\), one 0-cell and thirteen 1-cells give a wedge of thirteen circles. For \(n=4,5\), one 0-cell and seven 2-cells give a wedge of seven 2-spheres. For \(n=6\), the Morse 2-skeleton is \(S^2\vee S^2\). Each 3-cell attaches by a map \(S^2\to S^2\vee S^2\), whose homotopy class is completely determined by its two integral degrees, because \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\). The zero integral Morse boundary means both degrees are zero, hence all eleven attaching maps are nullhomotopic. Therefore the final space is \(S^2\vee S^2\vee\bigvee^{11}S^3\), as stated.

## Verification
Run `python3 check_sm_mixed.py` with Python 3 and standard library only. The program checks both facet-generation methods, full enumeration and dimensions, certified matching cover relations, acyclicity of the complete Hasse diagram, exact signed integer Morse boundaries, and mod-two homology of the unreduced simplicial chain complex. `verification_output.txt` records a successful run of the exact embedded source. The output marker is `STRONG_MIXED_CYCLE_BOUQUET_PASS`. `CERT_ORDERS` is a complete compact finite certificate: the matching can be deterministically reconstructed without relying on opaque saved logs.

## Relationship to prior work
Knudson and Owens-White [1] introduce the full strong-Morse matching complex and classify its path, star, simplex, simplex-boundary and several cycle variants; the relevant full text (Sections 3–4, 6–8 and 10) does not give a classification for unequal two-cycle bouquets. The underlying vertex-order strong Morse theory is due to Fernández [2]. The ordinary, generally larger, Morse complex of Chari and Joswig [3] is a different invariant. Published research records [4] give a uniform formula for bouquets made solely from triangles, including our already-known \(n=3\) boundary; [5] gives a uniform sphere formula for bouquets made solely from squares. Neither formula applies to an unequal bouquet \(C_3\vee C_n\) with \(n=4,5,6\), nor does disjoint-union join splitting apply across a *shared* vertex. Published records for a theta graph [6] concern a graph with two shared branch vertices, not the current one-point bouquet.

## Limitations
This is a finite, complete classification for the four **explicitly stated** lengths, not an unrestricted periodicity theorem. The first \(n=3\) row is prior work, included only to locate the initial change. The result makes no assertion about \(n\ge7\), an arbitrary number of petals, the action of graph automorphisms on the integral homology lattice, or a general functorial splitting. Exact numerical verification is finite proof here because every graph, face and matching in the stated domain is exhaustively enumerated; it does not establish an infinite-family claim. Publicly indexed and search-record literature may omit an equivalent result under different terminology.

## References
[1] K. P. Knudson and A. Owens-White, *Complexes of strong discrete Morse matchings*, arXiv:2609.06844v1 (first posted 2026-09-06), https://arxiv.org/html/2609.06844.

[2] X. L. Fernández, *Strong discrete Morse theory*, arXiv:2504.15729, https://arxiv.org/abs/2504.15729.

[3] M. K. Chari and M. Joswig, *Complexes of discrete Morse functions*, Discrete Mathematics 302 (2005), 39–51, https://doi.org/10.1016/j.disc.2004.07.027.

[4] *Strong Morse complexes of friendship graphs: an exponential sphere-wedge formula*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-strong-morse-complexes-of-friendship-graphs-an-exponential-spher--c88f401c5072.

[5] *A six-cycle join core for strong Morse matching complexes of square bouquets*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-six-cycle-join-core-for-strong-morse-matching-complexes-of-squ--d0ea73d39bd5.

[6] *A mixed-dimensional sphere wedge for the strong Morse complex of \(\Theta_{2,2,3}\)*, research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-mixed-dimensional-sphere-wedge-for-the-strong-morse-complex-of--3a17bdf387a8.
