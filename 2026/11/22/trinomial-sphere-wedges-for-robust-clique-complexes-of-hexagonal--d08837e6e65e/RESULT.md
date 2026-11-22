# Trinomial sphere wedges for robust clique complexes of hexagonal bouquets

## Finding

For every integer \(m\ge 2\) and robustness parameter \(k\ge4\), form the graph \(B_m\) by gluing \(m\) chordless six-cycles at precisely one common vertex, with no other identifications or edges. Its \(k\)-robust clique complex \(R_k(B_m)\) has the **integral homotopy type**

\[
|R_k(B_m)|\simeq\bigvee^{\beta_{m,k}}S^{2k-3},\qquad
\beta_{m,k}=[t^{k-1}](1+t+t^2)^m
=\sum_{\substack{r,s\ge0\\2r+s=k-1}}\binom{m}{r}\binom{m-r}{s}.
\]

A wedge of zero spheres denotes a contractible space. For example, \(\beta_{2,4}=2\), \(\beta_{3,4}=7\), and \(\beta_{4,4}=16\). The complex is contractible for all \(k\ge2m+2\). All reduced integral homology vanishes except for a free abelian group of rank \(\beta_{m,k}\) in degree \(2k-3\).

## Assumptions and scope

The graph has a central vertex \(z\). Its \(j\)-th hexagonal petal has five other vertices \(a_j,b_j,c_j,d_j,e_j\), with edges \(za_j,a_jb_j,b_jc_j,c_jd_j,d_je_j,e_jz\). Distinct petals intersect only at \(z\). For a finite graph \(G\), \(\alpha(G)\) is the maximum cardinality of an independent vertex set, with \(\alpha(\varnothing)=0\). The abstract simplicial complex is

\[
R_k(G)=\{S\subseteq V(G):\alpha(G[S])\le k-1\}.
\]

The empty face is included in the abstract complex but **not** in the nonempty-face poset used for cellular discrete Morse theory. The theorem concerns all \(m\ge2\) and every integer \(k\ge4\); it does not assert minimality of the bouquet size or any equivariant splitting.

## Proof

**Step 1: an acyclic ordered-vertex matching.** On the poset of nonempty faces, process vertices in this order: \(z,a_1,b_1,c_1,d_1,e_1,a_2,\ldots,e_m\). At a vertex \(v\), match every as-yet-unmatched pair \((S,S\cup\{v\})\) for which both faces remain. Discard matched pairs before processing the next vertex. The matching is acyclic: in a hypothetical directed cycle in the Hasse diagram (matching edges reversed), choose the first vertex used by an upward matched edge. Edges deleting earlier vertices strictly decrease the earlier-bit pattern, so none occur in a cycle. On the fiber of the fixed earlier-bit pattern, an upward edge at the chosen vertex moves its bit from zero to one, while a downward edge at that vertex cannot occur between cells that survived the earlier matching stages and are eligible for the chosen stage. Hence the bit cannot return to zero in a closed path. This is the standard lexicographic vertex-toggling matching argument. The independent checker separately constructs the complete directed Hasse graph and tests acyclicity on finite instances.

**Step 2: identify the residual faces after toggling the hub.** Except for the unmatched singleton \(\{z\}\), a face \(S\) survives the first matching precisely when \(z\notin S\), \(S\in R_k(B_m)\), but \(S\cup\{z\}\notin R_k(B_m)\). Write \(S_j=S\cap\{a_j,b_j,c_j,d_j,e_j\}\) and set

\[
A_j=\alpha(P_5[S_j]),\qquad
B_j=\alpha(P_3[S_j\cap\{b_j,c_j,d_j\}]).
\]

Here \(P_5=a_jb_jc_jd_je_j\) and \(P_3=b_jc_jd_j\). The independent-set decomposition in a one-vertex bouquet gives

\[
\alpha(B_m[S])=\sum_j A_j,\quad
\alpha(B_m[S\cup\{z\}])=\max\left\{\sum_j A_j,1+\sum_j B_j\right\}.
\]

Since \(0\le B_j\le A_j\), the residual condition is equivalent to

\[
A_j=B_j=:r_j\in\{0,1,2\}\quad\text{for every }j,
\qquad \sum_jr_j=k-1.
\]

In particular adding or deleting one petal vertex **within the residual face poset** cannot change any \(r_j\), because the local independence numbers cannot decrease under insertion and the fixed sum is \(k-1\). The residual poset therefore splits into independent product components indexed by \((r_1,\ldots,r_m)\).

**Step 3: the complete five-vertex local table.** Write a subset of the labelled path \(a,b,c,d,e\) by concatenating its letters. Exhaustively considering the \(32\) subsets, the condition \(\alpha(P_5[T])=\alpha(P_3[T\cap\{b,c,d\}])=r\) gives exactly the following strata:

\[
\begin{aligned}
T_0&=\{\varnothing\},\\
T_1&=\{b,ab,c,bc,d,cd,de\},\\
T_2&=\{bd,abd,bcd,abcd,bde,abde,bcde\}.
\end{aligned}
\]

Apply the same ordered-vertex matching \(a,b,c,d,e\) separately in each stratum. For \(T_1\), the three matched pairs are \((b,ab),(c,bc),(d,cd)\); its only unmatched subset is \(de\). For \(T_2\), the pairs are \((bd,abd),(bcd,abcd),(bde,abde)\); its only unmatched subset is \(bcde\). The \(T_0\) survivor is the empty local subset. Their respective vertex counts are \(0,2,4\). Any fixed vector of ranks \((r_1,\ldots,r_m)\) with sum \(k-1\) therefore has exactly one critical face, consisting of the union of the appropriate local survivors, and containing \(2(k-1)\) vertices.

**Step 4: homotopy and counting.** In the nonempty-face poset there is precisely one additional critical face \(\{z\}\), of dimension zero. All other critical faces have dimension \(2(k-1)-1=2k-3\). Forman's discrete Morse theorem gives a CW model with one vertex and \(\beta_{m,k}\) cells of the single positive dimension \(2k-3\), and hence a wedge of spheres, with no possible nontrivial attaching maps. Each rank vector is obtained by choosing \(r\) petals of rank two and \(s\) further petals of rank one, yielding the displayed trinomial coefficient. If \(k-1>2m\), no vector exists and the complex is contractible. Every assertion is integral and uniform in \(m,k\).

## Verification

The accompanying standard-library-only `check_hex_bouquets.py` enumerates all \(32\) local path subsets and checks the three displayed strata. Independently, for \(m=1,2,3\) and \(k=2,3,4,5,6\), and for \((m,k)=(4,4)\), it enumerates every nonempty face, reconstructs the full ordered matching, compares every critical simplex with the stated local survivors, and verifies acyclicity by topological sorting of the entire oriented Hasse graph. All **16 cases passed**. The largest case contains \(34{,}474\) faces. Run `python3 check_hex_bouquets.py`. These finite checks supplement and do not replace the uniform proof.

## Relationship to prior work

Filakovský's *The Topology of k-Robust Clique Complexes in Grid-like Graphs* (first public 11 February 2026) defines the same complex and proves sphere-wedge results for square-sequence graphs built by attaching four-cycles, with all-parameter results under restricted edge gluing. Hexagonal bouquets contain no four-cycle, so those hypotheses fail. The general theorem for all bipartite graphs at \(k=3\) concerns a different robustness level and does not imply the present \(k\ge4\) result. Previously published exact classifications of bouquets of quadrilaterals, pentagons, and rooted complete bipartite graphs have binomial or elementary-symmetric sphere counts, whereas this induced-hexagon family has a three-state trinomial count. Ordinary independence complexes of hexagon bouquets are not the same as robust clique complexes; Alexander duality instead relates robust cliques to **total** cut complexes. Carnero Bravo's *Total cut complexes and their duals* develops that broader context but its accessible abstract concerns other graph families. The first paper's complete accessible text was inspected; abstract-only and unindexed priority risks are recorded in the review.

## Limitations

The classification is specific to unweighted simple bouquets of induced six-cycles meeting at one vertex and parameters \(k\ge4\). It does not assert a filtration-compatible equivalence as \(k\) varies, equivariant homotopy types, or general cactus graphs. The absence of an indexed equivalent theorem cannot establish global novelty. Independent mathematical validation is not claimed.

## References

- Marek Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first posted 2026-02-11), https://arxiv.org/html/2602.11365.
- Minki Kim and Alan Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, https://arxiv.org/abs/1912.12605.
- Andrés Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427 (first posted 2026-02-24), https://arxiv.org/abs/2602.21427.
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
