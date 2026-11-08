# Odd-dominating edge cuts and the exact connectivity premium on triangular graphs

## Finding
For each integer \(n\ge3\), let \(T_n=L(K_n)\), the triangular graph with a vertex for each unordered pair of elements of \([n]\); two vertices are adjacent when their underlying pairs intersect. A set \(S\subseteq V(T_n)\) is *odd dominating* when every closed neighborhood contains an odd number of members of \(S\). A *connected odd dominating* set additionally induces a connected nonempty subgraph.

**Complete classification.** For even \(n\), the only odd-dominating set is \(V(T_n)\). For odd \(n\), select any even-sized subset \(U\subseteq[n]\); the corresponding odd-dominating set is exactly
\[
 S_U=E(K_n[U])\cup E(K_n[[n]\setminus U]),
\]
under the line-graph identification. Every odd-dominating set is given by precisely one such \(U\). Thus there are \(1\) solutions for even \(n\), and \(2^{n-1}\) for odd \(n\).

For odd \(n\), the complete cardinality enumerator is
\[
 W_n(z)=\sum_{\substack{0\le a\le n\\a\text{ even}}}\binom na z^{\binom a2+\binom{n-a}2}.
\]
For even \(n\), \(W_n(z)=z^{\binom n2}\). In particular, for odd \(n\), the odd-domination number is
\[
 \gamma_{\mathrm{odd}}(T_n)=\binom n2-\left\lfloor\frac{n^2}{4}\right\rfloor,
\]
with exactly \(\binom n{\lfloor n/2\rfloor}\) minimum sets.

**Connectivity premium.** The induced graph on \(S_U\) is \(T_{|U|}\sqcup T_{n-|U|}\), with empty summands omitted. For odd \(n\), it is connected if and only if \(|U|=0\) or \(|U|=n-1\). Hence there are exactly \(n+1\) connected odd-dominating sets, and
\[
 \gamma_{\mathrm{odd}}^{\mathrm{conn}}(T_n)=\binom{n-1}{2}
 \quad(n\text{ odd}).
\]
For even \(n\), there is a unique connected solution, of cardinality \(\binom n2\). For odd \(n\ge5\), the exact connectivity penalty is
\[
 \gamma_{\mathrm{odd}}^{\mathrm{conn}}(T_n)-\gamma_{\mathrm{odd}}(T_n)=
 \left\lfloor\frac{n^2}{4}\right\rfloor-(n-1)>0.
\]
In particular no minimum odd-dominating set is connected when \(n\ge5\) is odd.

## Assumptions and scope
The graph is finite, simple, and undirected. \(T_2\) denotes a one-vertex graph, and \(T_0,T_1\) are empty when used only to describe induced components. A closed neighborhood contains the center vertex. The indicator vector of an odd-dominating set is binary. Connectedness concerns the graph induced by selected vertices, not connectivity of their complement or of the ambient graph. All theorem statements concern every integer \(n\ge3\), not just the finite verification range.

## Proof
Put \(x_{ij}=1\) if the line-graph vertex indexed by the edge \(\{i,j\}\) of \(K_n\) is selected, and zero otherwise, with arithmetic in \(\mathbb F_2\). Let \(d_i=\sum_{j\ne i}x_{ij}\), and \(D=\sum_{i=1}^n d_i=0\) by double counting edges.

The closed neighborhood of \(\{i,j\}\) consists of the edges incident with at least one of \(i,j\). The parity condition is
\[
 d_i+d_j+x_{ij}=1,
 \qquad\text{so}\qquad x_{ij}=1+d_i+d_j.
\]
Summing over \(j\ne i\) yields
\[
 d_i=(n-1)+nd_i+D,
 \qquad (n+1)d_i=(n-1)+D.
\]
Since \(D=0\), if \(n\) is even then every \(d_i=1\), and the displayed formula forces \(x_{ij}=1\) for every edge. Conversely the all-one choice has odd closed-neighborhood intersections, because \(T_n\) has \(2(n-2)\) neighbors per vertex. Thus this is the unique solution.

If \(n\) is odd then the displayed condition on \(d_i\) is automatic for any binary vector \((d_i)\) with even total parity. Assign \(U=\{i:d_i=0\}\). Set \(U=\{i:d_i=1\}\); by \(D=0\), the set \(U\) has even cardinality. Then \(x_{ij}=1\) if and only if \(d_i=d_j\), namely if \(i,j\) are in the same of the two groups \(U,[n]\setminus U\). Conversely any even-sized \(U\) defines such a vector, and its computed degrees satisfy the presumed \(d_i\): when \(d_i=1\) the selected degree is \(|U|-1\), odd; otherwise it is \((n-|U|)-1\), even. The correspondence is injective because \(d_i\) is recoverable by summing \(x_{ij}\). This proves the complete classification and counts.

For \(|U|=a\), the selected edges are precisely the edges of two disjoint complete graphs, so their number is \(\binom a2+\binom{n-a}2=\binom n2-a(n-a)\). This gives the weight enumerator. For odd \(n\), the maximum of \(a(n-a)\) among even \(a\) is \(\lfloor n^2/4\rfloor\): exactly one of \(\lfloor n/2\rfloor,\lceil n/2\rceil\) is even. There are \(\binom n{\lfloor n/2\rfloor}\) choices of that size, giving the minimum and its multiplicity.

As an induced subgraph of \(L(K_n)\), the selected edges within \(U\) span \(T_a\), and those within its complement span \(T_{n-a}\), with no adjacencies between them. For odd \(n\ge3\), the permissible even values of \(a\) yield just one nonempty summand exactly for \(a=0\) or \(a=n-1\) (where the complementary group has size one). The first case is unique and the latter has \(n\) choices. Their sizes are \(\binom n2\) and \(\binom{n-1}2\), proving both the connected count and the minimum connected size. Subtraction gives the positive connectivity penalty for odd \(n\ge5\). For even \(n\) the unique set is the entire connected graph. This completes the proof.

## Verification
Two independent executable checks are included: `verify_triangular_direct.cpp` directly enumerates all subsets of the \(\binom n2\) vertices for \(3\le n\le7\), tests every closed-neighborhood parity constraint, determines connectivity by graph traversal, and compares full weight profiles. Compile with `g++ -O2 -std=c++17 verify_triangular_direct.cpp -o direct && ./direct`; the expected output is `triangular_direct_output.txt`.

The independent `verify_triangular_linear.py` constructs the binary closed-neighborhood matrix, performs Gaussian elimination with explicit consistency checks, enumerates its affine solution space, and tests induced connectivity, for \(3\le n\le9\). Run with `python3 verify_triangular_linear.py`, comparing `triangular_linear_output.txt`.

These finite checks confirm the formulas on their stated ranges; the unrestricted theorem follows from the symbolic parity argument above rather than extrapolation.

## Relationship to prior work
Caro and Klostermeyer (2003) introduced the odd-domination parameter and investigated several families, with a dated public issue record of 28 February 2003. Caro, Klostermeyer and Yuster (2005) studied the additional induced-connectivity condition, including complete multipartite graphs, grids, cycle powers and path powers. The inspected relevant text of the latter does not give the parity-cut classification or exact connected premium for triangular graphs. The present target is the line graph \(L(K_n)\), not the complete graph \(K_n\) or a complete multipartite graph; a result on those hosts is not an implication of the present weight-profile theorem. The contribution claimed here is the complete all-set and connected-set classification for the triangular graph family, not the definitions or general existence/computational-complexity results in the cited literature.

## Limitations
Historical priority beyond the searched records is not certified. The scanned 2003 paper was inspected at its dated record and introductory two pages; no statement about the full text's noncoverage is asserted. The accessible 2005 full text was inspected at its introduction, list of treated graph families, and relevant sections on grid and complete multipartite graphs, with searches for triangular and line graphs; this is a targeted comparison, not an independently conducted exhaustive literature review. The proofs do not claim results on arbitrary line graphs, other parity conventions, or infinite graphs.

## References
1. Y. Caro and W. F. Klostermeyer, *The odd domination number of a graph*, Journal of Combinatorial Mathematics and Combinatorial Computing **44** (2003), 65–83. Published 2003-02-28. https://combinatorialpress.com/jcmcc-articles/volume-044/the-odd-domination-number-of-a-graph/ .
2. Y. Caro, W. F. Klostermeyer and R. Yuster, *Connected odd dominating sets in graphs*, Discussiones Mathematicae Graph Theory **25** (2005), 225–239. DOI:10.7151/DMGT.1276; author-hosted full text https://math.haifa.ac.il/raphy/papers/connoddds.pdf .
