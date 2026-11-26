# Strong majority edge-colouring rigidity of cycle prisms

## Finding
For the prism graph \(P_n=C_n\square K_2\), \(n\ge3\), define the **strong majority index** \(\operatorname{Maj}'(P_n)\) as the fewest named edge colors needed so that, for each edge and each color, at most half of the edges adjacent to that edge have that color. Then
\[
\operatorname{Maj}'(P_n)=\begin{cases}2,&4\mid n,\\3,&4\nmid n.\end{cases}
\]
For a fixed palette of two named colors, the exact number of strong majority edge-colorings is
\[
N_2(P_n)=\begin{cases}8,&4\mid n,\\0,&4\nmid n.\end{cases}
\]
In particular, the cube \(P_4\) has eight such two-edge-colorings even though all eight vertices have odd degree three. This gives an explicit counterexample to the assertion in the opening of Section 3 of Kalinowski–Kamyczura–Pilśniak–Woźniak [1] that a two-color strong majority edge-coloring is possible only if every input vertex has even degree. This conclusion uses precisely their **edge-adjacency** definition; it is not about vertex-based majority edge-coloring.

## Assumptions and scope
All graphs are finite and simple, and \(n\ge3\). Label the top vertices \(a_i\), bottom vertices \(b_i\), and edges \(a_ia_{i+1}\), \(b_ib_{i+1}\), \(a_ib_i\), with all indices modulo \(n\). The edges are distinct for \(n\ge3\); each vertex has degree three and each edge has exactly four *other* adjacent edges (sharing an endpoint). Edge colors need not be proper. Two-color assignments use a fixed palette \(\{0,1\}\), with no quotient by graph automorphisms or by exchanging colors. A proper three-edge-coloring is a valid strong majority coloring, but properness is not required in the two-color classification.

## Proof
In a two-coloring, every edge has four neighboring edges. Both colors occur at most twice among these neighbors if and only if exactly two neighbors have color \(1\). Write \(T_i,B_i,R_i\in\{0,1\}\) for the colors of the top rail, bottom rail, and rung edges at index \(i\), and put \(S_i=T_i+B_i\).

The requirements at the three edge types are precisely
\[
S_{i-1}+S_i=2,\tag{1}
\]
\[
T_{i-1}+T_{i+1}+R_i+R_{i+1}=2,\tag{2}
\]
\[
B_{i-1}+B_{i+1}+R_i+R_{i+1}=2.\tag{3}
\]
All three equations are necessary and sufficient, since they list all four edge-neighbors once for every edge.

Equation (1) yields \(S_i=2-S_{i-1}\). If any \(S_i\ne1\), the values alternate between \(0\) and \(2\) around the cycle. Choose an index with \(S_i=2\). Then \(S_{i-1}=S_{i+1}=0\) and \(S_{i+2}=2\). Because each \(T_j\) is binary, equation (2) at \(i\) forces \(R_i+R_{i+1}=2\), hence \(R_{i+1}=1\). The same equation at \(i+1\) forces \(R_{i+1}+R_{i+2}=0\), hence \(R_{i+1}=0\), a contradiction. Therefore every \(S_i=1\), so
\[
B_i=1-T_i.\tag{4}
\]
Subtracting (3) from (2) and substituting (4) gives
\[
T_{i-1}+T_{i+1}=1,\qquad T_{i+2}=1-T_i.\tag{5}
\]
Thus \(T_{i+4}=T_i\) and \(T_{i+2}\ne T_i\): every top sequence is genuinely period four. Cyclic consistency implies \(4\mid n\). This also rules out every binary strong majority edge-coloring when \(4\nmid n\).

Conversely, if \(4\mid n\), choose \(T_0,T_1\) independently in \(\{0,1\}\) and extend uniquely using \(T_{i+2}=1-T_i\). Equation (4) gives all bottom rail colors. Equation (2), since \(T_{i-1}+T_{i+1}=1\), reduces to \(R_i+R_{i+1}=1\). Choose \(R_0\) independently and extend by alternating the rung colors; this is cyclically consistent because \(n\) is even. Equations (1)–(3) now all hold. We have precisely four independent choices of the top pair and two rung choices, hence \(4\cdot2=8\) binary colorings. The construction is injective because the labeled edge colors recover the three initial bits.

It remains to show the three-color upper bound for every \(n\ge3\). The graph has a Hamiltonian circuit following top vertices in ascending order, then the end rung, then bottom vertices in descending order, then the initial rung. Its length is \(2n\), hence even. Alternate colors \(0\) and \(1\) around this Hamiltonian circuit and assign a third color \(2\) to every edge outside it. The complementary edges form a perfect matching (every cubic vertex has exactly two Hamiltonian-cycle edges), so this is a proper three-edge-coloring. Each edge of a cubic graph then sees exactly two edges of each of the *other* two colors and none of its own color. Therefore it satisfies the strong majority edge condition. One color is impossible since every edge has four neighbors. This establishes the claimed exact indices and multiplicities.

## Verification
The standalone \(\texttt{verify.cpp}\) constructs all \(3n\) **labeled edges** and determines each edge's four neighbors directly from shared endpoints, independently of equations (1)–(3). It exhaustively checks all \(2^{3n}\) binary assignments for every \(3\le n\le7\), obtaining respectively \(0,8,0,0,0\); it also checks the Hamiltonian proper three-edge-coloring for every \(3\le n\le44\), and verifies all eight parameterized two-color constructions for every multiple of four in that range. Compile with \(\texttt{g++ -std=c++17 -O2 verify.cpp -o verify}\) and execute \(\texttt{./verify}\). The final status is \(\texttt{VERIFY_OK}\). These finite checks corroborate but do not substitute for the symbolic proof above.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak, and Woźniak [1] introduce the edge-based strong majority condition, give general bounds, and analyze cycle and other classes. The complete relevant Section 3 and its edge-coloring results were materially inspected; no result there states the cycle-prism dichotomy or eight-coloring census. Their preliminary claim that two colors require all input vertex degrees even is incompatible with the explicit cube solution here. A previous exact calculation for the distinct input graph \(K_4\) also reports a two-color strong majority edge-coloring despite degree three, so the existence of an odd-degree counterexample is **not claimed as new**; the contribution here is the complete infinite prism classification and its exact eight-count. The correct elementary parity restriction applies to degrees in the **line graph** \(L(G)\), since each vertex of that graph represents an edge of the original graph. For \(P_n\), all line-graph vertices have degree four even though input-graph vertices have degree three.

Antoniuk–Prorok–Salia [2] give a general five-color upper bound; Pękała–Przybyło [3] give three-color upper bounds under a larger minimum-degree hypothesis. Their accessible abstracts do not settle the exact prism index or binary multiplicities; their full texts could not be materially checked, so they remain explicit priority risks.

Freyberg–Marr [4] study two-color *open-neighborhood-balanced vertex colorings*. The binary strong majority edge-colorings here are exactly such colorings of \(L(P_n)\), a four-regular graph. Their inspected full open-access article classifies different graph families, including four-regular circulants, but supplies no identified evaluation of \(L(P_n)\). Collins and collaborators [5] classify *closed-neighborhood-balanced vertex colorings of the prism itself*, a different graph and a different neighborhood condition; their complete open-access article was inspected and does not imply this line-graph result in any stated theorem. This work therefore treats this established vertex terminology as an alias for appropriate checks, not as evidence of novelty by nomenclature alone.

## Limitations
The theorem concerns ordinary finite cycle prisms for all \(n\ge3\), the minimum number of colors, and exact counts **only at the two-color level**. It does not count arbitrary three-color strong majority edge-colorings, colorings modulo symmetry, arbitrary Cartesian products, or Möbius ladders. The full-text access limitations for [2] and [3], and any earlier undiscovered balanced line-graph enumeration, remain historical-priority risks. No independent validation or third-party certification is claimed.

## References
[1] R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828 (first public 2026-05-22), https://arxiv.org/abs/2605.23828.

[2] S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212 (2026), https://arxiv.org/abs/2607.00212.

[3] P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122 (2026), https://arxiv.org/abs/2608.04122.

[4] B. Freyberg, A. Marr, *Neighborhood Balanced Colorings of Graphs*, Graphs and Combinatorics **40**, 41 (2024), doi:10.1007/s00373-024-02766-9.

[5] K. L. Collins et al., *Closed Neighborhood Balanced Coloring of Graphs*, Graphs and Combinatorics **41**, 88 (2025), doi:10.1007/s00373-025-02950-5.
