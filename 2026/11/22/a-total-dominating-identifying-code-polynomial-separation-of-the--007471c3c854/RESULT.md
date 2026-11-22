# A total-dominating identifying-code polynomial separation of the Shrikhande and rook graphs

## Finding
Let \(S\) be the Shrikhande graph and \(R=K_4\square K_4\) the four-by-four rook graph. Both have sixteen vertices, degree six, and strongly regular parameters \((16,6,2,2)\). For either graph define the *total-dominating identifying-code polynomial*
\[
F_G(z)=\sum_{C\subseteq V(G)}z^{|C|}\,\mathbf 1\{C\text{ is both total dominating and a closed-neighborhood identifying code}\}.
\]
The two exact polynomials are
\[
\begin{aligned}
F_R(z)={}&1056z^6+5520z^7+10170z^8+10800z^9+7944z^{10}\\
&+4368z^{11}+1820z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16},\\
F_S(z)={}&1040z^6+5584z^7+10206z^8+10800z^9+7944z^{10}\\
&+4368z^{11}+1820z^{12}+560z^{13}+120z^{14}+16z^{15}+z^{16}.
\end{aligned}
\]
In particular,
\[
\boxed{F_R(z)-F_S(z)=16z^6-64z^7-36z^8.}
\]
Both simultaneous invariants have minimum size six, but there are exactly \(1056\) minimum configurations in \(R\) and \(1040\) in \(S\). The polynomials coincide in every cardinality at least nine. Their totals are \(F_R(1)=42375\) and \(F_S(1)=42459\).

## Assumptions and scope
Graphs are finite, undirected, loopless and have labeled vertices. Use \(V=\mathbb Z_4^2\), indexed by \(4a+b\) for \(0\le a,b\le3\). Two vertices of \(R\) are adjacent when they are distinct and share a coordinate. Vertices of \(S\) are adjacent when their coordinate difference modulo four belongs to
\[
\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}.
\]
For a graph \(G\), write \(N_G(v)\) for the open neighborhood and \(N_G[v]=N_G(v)\cup\{v\}\) for the closed neighborhood. A set \(C\subseteq V(G)\) is *total dominating* when \(N_G(v)\cap C\ne\varnothing\) for every vertex \(v\), including selected vertices. It is an *identifying code* when the sixteen signatures \(N_G[v]\cap C\), indexed by \(v\), are nonempty and pairwise distinct. The two requirements are simultaneous, on the same \(C\); the enumerator counts each labeled subset once. Total domination implies every closed signature is nonempty, so in this joint problem only distinctness must be checked separately.

## Proof
**Forbidden-cap equivalence.** Write \(V=V(G)\), and define the following explicit family of vertex sets:
\[
\mathcal B_G=\{V\setminus N_G(v):v\in V\}\cup
\{V\setminus(N_G[u]\mathbin\triangle N_G[v]):\{u,v\}\in\tbinom V2\}.
\]
Here \(\triangle\) denotes symmetric difference. A selected set fails total domination exactly when it misses at least one open neighborhood, equivalently when \(C\) lies inside the first type of forbidden cap. It fails to distinguish the closed signatures of two vertices exactly when it misses their symmetric difference, equivalently when \(C\) lies inside the second type. Consequently,
\[
C\text{ satisfies both requirements}\quad\Longleftrightarrow\quad
C\not\subseteq B\quad\text{for every }B\in\mathcal B_G.
\]
This is a bidirectional equivalence with no search heuristic or omitted cases. The family has exactly \(16+\binom{16}{2}=136\) indexed caps. Each open-neighborhood complement has ten vertices. For adjacent \(u,v\), the common closed-neighborhood size is four, yielding a symmetric difference of size six and a cap of size ten. For nonadjacent \(u,v\), their two common neighbors give closed-neighborhood intersection size two, symmetric difference size ten, and cap size six. Each graph has 48 edges and 72 nonedges, so there are 64 caps of size ten and 72 caps of size six (counted with the indexed construction).

**Exhaustive finite certificate.** The accompanying independent `verify_direct.py` and `verify_forbidden.py` compute all \(2^{16}=65536\) subsets for *each* explicitly defined graph. The first builds actual sets of open neighbors and closed-neighborhood intersection signatures, visiting each combination of each possible cardinality, and retains precisely those with total domination and pairwise-distinct signatures. The second builds the 136 bitmask caps and marks their entire downward closures: for each cap of mask \(b\), the loop \(s\leftarrow(s-1)\mathbin\&b\) visits each submask exactly once, ending at zero. The complements of marked masks are the valid codes by the proved equivalence. Since all labeled subsets are covered, this finite enumeration proves every displayed coefficient exactly. Both algorithms obtain the stated polynomial coefficients and the *same complete 65,536-entry membership bitmap* for each graph, with SHA-256 digests documented in Verification. They construct adjacency through independent coordinate procedures rather than using imported graph data.

**Common high-cardinality tail.** The 64 ten-vertex forbidden caps are all distinct, and any two intersect in at most eight vertices, as checked exhaustively in `verify_forbidden.py` using the explicit coordinate definitions. Thus distinct ten-caps contain no common nine-subset. The six-caps contain no nine-subset. No cap contains eleven or more vertices. Therefore every set of size at least eleven works, precisely \(\binom{16}{10}-64=7944\) ten-sets work, and \(\binom{16}{9}-64\binom{10}{9}=10800\) nine-sets work, in *both* graphs. The smaller coefficients, including the sharp six/seven/eight distinctions, follow from the complete independent exact enumerations above. This proves all claims, including that no five-element joint code exists.

## Verification
The four standalone included artifacts `verify_direct.py`, `verify_forbidden.py`, `direct_output.txt`, and `forbidden_output.txt` contain the two full programs and recorded outputs. From a directory containing the programs, execute:

```sh
python3 verify_direct.py
python3 verify_forbidden.py
```

Both implementations require only the Python standard library. Successful completion asserts the complete coefficient vectors and prints exact membership-bitmap SHA-256 digests for cross-comparison. The first prints `DIRECT_EXHAUSTIVE_PASS` and the second prints `FORBIDDEN_DOWNSET_PASS`; neither has a randomized branch or a cutoff. The direct program additionally checks that each graph has degree six and two common neighbors for each distinct vertex pair; the cap program verifies the 64 ten-caps and their intersection restriction. Actual replay outputs are included, but the justification is the finite exhaustive algorithms and their coverage, not unauthenticated logs alone.

## Relationship to prior work
Foucaud and Lehtilä (2022 preprint; 2023 publication) introduce and study *total dominating identifying codes*, proving general bounds and extremal constructions. Their inspected full text does not provide the present pairwise counting polynomials. Gravier et al. (2015) examine ordinary identifying codes in strongly regular graphs and products of cliques, rather than the simultaneous total-domination refinement. Gravier, Moncel and Semri (2008) determine the ordinary identifying-code minimum of the square rook graph, not the cardinality polynomial of sets satisfying both requirements.

Published exact studies of these same two graphs have already determined their *ordinary* minimum identifying-code sizes (five and six), and also their *equal total-domination polynomials*. Neither a size of a minimum ordinary code nor equality of the total-domination polynomial implies how many sets satisfy **both** code separation and total domination: this is a refined intersection of two properties, and a neighborhood-incidence bijection need not preserve distinct closed signatures. The displayed difference and the common high-cardinality stabilization therefore supply different data from those prior results. Other work distinguishes the pair using paired domination, global locating-domination, and neighborhood-shattering polynomials; none has the same simultaneous definition or establishes the new coefficients. See the citations below; unindexed earlier tables cannot be categorically excluded.

## Limitations
The theorem applies to precisely these two labeled sixteen-vertex graphs, not arbitrary strongly regular graphs or a growing family of rook/Doob graphs. Exact finite exhaustion establishes the coefficients only because the entire fixed finite input universe is visited; the search is not a proof of a general infinite-family theorem. The result does not classify symmetry orbits of the joint codes or their reconfiguration graphs. Historical publication priority remains provisional until independently assessed; external mathematical auditing is not claimed.

## References
1. F. Foucaud and T. Lehtilä, *Bounds and Extremal Graphs for Total Dominating Identifying Codes*, arXiv:2206.09481, first public 2022-06-19; Electronic Journal of Combinatorics **30** (2023), DOI 10.37236/11342. https://arxiv.org/abs/2206.09481 and https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i3p15/pdf/.
2. S. Gravier, A. Parreau, S. Rottey, L. Storme and E. Vandomme, *Identifying Codes in Vertex-Transitive Graphs and Strongly Regular Graphs*, Electronic Journal of Combinatorics **22** (2015), article P4.6, DOI 10.37236/5256. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i4p6/pdf/.
3. S. Gravier, J. Moncel and A. Semri, *Identifying Codes of Cartesian Product of Two Cliques of the Same Size*, Electronic Journal of Combinatorics **15** (2008), article N4, DOI 10.37236/879. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1n4/pdf/.
4. *Optimal identifying-code exchange geometry of the Shrikhande and four-by-four rook graphs*, published exact finite comparison (2026), published-finding corpus public research record (2026).
5. *Paired-domination distinguishes two graphs with identical total-domination polynomials*, published exact finite comparison (2026), published-finding corpus public research record (2026).
