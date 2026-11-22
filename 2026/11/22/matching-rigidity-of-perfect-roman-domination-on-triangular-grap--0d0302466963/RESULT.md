# Matching rigidity of perfect Roman domination on triangular graphs

## Finding
For each integer \(n\ge3\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph, with one vertex for each unordered pair of distinct elements of \([n]\); two such vertices are adjacent exactly when the corresponding pairs intersect. Under **standard perfect Roman domination**, a function \(f:V(T_n)\to\{0,1,2\}\) is admissible when every vertex labelled zero has **exactly one neighbour labelled two** (neighbours labelled one are permitted). Its weight is \(\sum_v f(v)\).

Put
\[
r_n=\left\lfloor\frac{2n+3}{8}\right\rfloor,\qquad N_n=\binom n2.
\]
Then the exact perfect Roman domination number is
\[
\boxed{\gamma_R^p(T_n)=N_n+r_n-2r_n(n-2r_n).}
\]
Every minimum function arises **uniquely** by choosing a matching \(M\) of \(r_n\) edges in the labelled root clique \(K_n\), giving label two to the edges of \(M\), label zero to precisely the \(2r_n(n-2r_n)\) edges between the matched and unmatched root vertices, and label one to all other edges. Consequently the exact number of minimum functions is
\[
\boxed{\frac{n!}{2^{r_n}r_n!(n-2r_n)!}.}
\]
In particular the minimum weight grows as \(n^2/4+O(n)\), despite the graph having \(\binom n2\) vertices.

## Assumptions and scope
All graphs are finite simple graphs. The root clique has labelled vertex set \([n]\) and \(n\ge3\). The vertex version of perfect Roman domination applies to \(T_n\), not a stronger edge version imposing that the *sum of all labels in the neighbourhood* of every zero is two. Vertices labelled one may neighbor zeros. The quantity counted is all minimum functions on this fixed labelled graph; renamings of the underlying \([n]\) are not identified.

## Proof
**1. The degree-zero/degree-one reduction.** For any perfect Roman function \(f\), let \(H\) be the spanning simple subgraph of \(K_n\) formed by those edges whose vertices of \(T_n\) carry label two. Write \(t=|E(H)|\), \(a=|\{v:d_H(v)=0\}|\), \(b=|\{v:d_H(v)=1\}|\), and \(c=n-a-b\), so each of the remaining \(c\) root vertices has degree at least two. For a root edge \(uv\notin E(H)\), its corresponding vertex of \(T_n\) is adjacent to exactly \(d_H(u)+d_H(v)\) vertices labelled two. Thus it is *eligible* to carry zero exactly when \(d_H(u)+d_H(v)=1\). These eligible edges are precisely those joining an isolated vertex to a degree-one vertex of \(H\), and there are exactly \(ab\) of them. All others outside \(H\) must be labelled one. Therefore
\[
w(f)\ge N_n+t-ab,
\]
with equality if and only if all \(ab\) eligible edges are labelled zero. Conversely, for every \(H\), this equality assignment is admissible.

**2. A nonmatching defender support is strictly suboptimal.** The degree sum in \(H\) gives \(2t\ge b+2c\). Introduce the real quadratic
\[
Q_n(x)=x(n-x)-x/2.
\]
If \(b\) is even and \(c\ge1\), then
\[
ab-t\le Q_n(b)-c(b+1)<Q_n(b).
\]
A matching on \(b\) root vertices exists and has \(ab-t=Q_n(b)\), so the original support is strictly improvable.

If \(b\) is odd and \(c\ge1\), integrality gives \(t\ge (b+2c+1)/2\), hence
\[
ab-t\le Q_n(b)-c(b+1)-\tfrac12.
\]
Both \(b-1\) and \(b+1\) are feasible even cardinalities (because \(1\le b\le n-1\)). Their changes in the quadratic are
\[
Q_n(b-1)-Q_n(b)=2b-n-\tfrac12,\quad
Q_n(b+1)-Q_n(b)=n-2b-\tfrac32.
\]
The two differences sum to \(-2\), so at least one is at least \(-1\). Since \(c(b+1)+1/2\ge5/2\), the associated matching strictly improves the original objective \(ab-t\). Thus **every optimal defender support has \(c=0\)**, and is a matching (possibly empty).

**3. Optimize and count the matching.** If the support is a matching of \(r\) edges, then \(t=r\), \(b=2r\), \(a=n-2r\), and the minimum possible weight for that support is
\[
W_n(r)=N_n+r-2r(n-2r)=N_n+4r^2+(1-2n)r,
\quad 0\le r\le\lfloor n/2\rfloor.
\]
The forward difference \(W_n(r+1)-W_n(r)=8r+5-2n\) is never zero for integer \(n,r\). It changes sign at the unique minimizing index \(r_n=\lfloor(2n+3)/8\rfloor\), which lies in the permitted range for all \(n\ge3\). For each matching the equality labeling from step 1 is unique, and the number of size-\(r_n\) matchings of \(K_n\) is \(n!/(2^{r_n}r_n!(n-2r_n)!)\). All conclusions follow.

## Verification
Three separate programs accompany this statement. `support_enum.cpp` exhausts all defender-support subsets of \(E(K_n)\) for \(3\le n\le7\), checking the minimum and whether every optimal support is a matching. `ternary_enum.cpp` independently tests **every** function with values zero, one, two, using the original adjacency criterion, for \(3\le n\le6\); at \(n=6\) this is \(3^{15}=14{,}348{,}907\) functions. `formula_check.py` constructs every matching-defined minimum function for \(3\le n\le10\), directly verifies the identifying condition, and checks weights and factorial counts. Their stdout is embedded in three corresponding `*_output.txt` files. These finite checks corroborate, but do not replace, the preceding all-\(n\) proof.

Selected exact triples \((n,\gamma_R^p(T_n),\#\text{minimum functions})\) are \((3,2,3)\), \((5,5,10)\), \((7,11,105)\), \((8,14,210)\), and \((10,23,630)\).

## Relationship to prior work
Perfect Roman domination under the exactly-one-neighbour-of-label-two condition is the standard parameter studied in the 2019 article *Perfect Roman domination in graphs* and in Fernau and Mann (2023), which investigates minimal-function enumeration and complexity rather than this triangular-graph formula. The previously published ordinary Roman-domination polynomial of triangular graphs concerns a weaker condition allowing *at least one* neighbouring two; its scalar minimum does not determine this perfect parameter or its optimum multiplicity.

The 2024 chapter *Perfect Edge Roman Domination in Fuzzy Simple Graphs* treats complete graphs under an additional zero-neighborhood **total label sum equals two** requirement (confirmed in its indexed definition and in the statement that zero edges have no adjacent one edges). This condition is strictly stronger than the standard exactly-one-two condition considered here, and its complete-graph theorem therefore cannot be substituted as this theorem. For example, when \(n=5\), an optimum here has edge labels two on one root edge, zero on its six cross edges, and one on the remaining three edges; several zero edges are adjacent to edges labelled one. That construction violates the stronger total-neighborhood-sum condition. The PDF's mathematical display for the published complete-graph theorem could not be visually inspected, so no assertion about its exact numerical formula is used.

## Limitations
The proof determines the minimum and all minimum functions only for triangular graphs; it does not determine the full perfect Roman weight polynomial, other Johnson ranks, or other line graphs. The literature comparison is evidence of no identified covering result, not a proof of historical uniqueness. No independent audit or independent validation is claimed.

## References
- H. Fernau and K. Mann, *Perfect Roman Domination and Unique Response Roman Domination*, arXiv:2309.07018v1, 13 September 2023, https://arxiv.org/abs/2309.07018 .
- *Perfect Roman domination in graphs*, Theoretical Computer Science (2019), DOI: 10.1016/j.tcs.2019.08.017, https://doi.org/10.1016/j.tcs.2019.08.017 .
- S. Vijayalakshmi, S. Sangeetha, P. Malliga, and R. Ramani, *Perfect Edge Roman Domination in Fuzzy Simple Graphs*, 2024, DOI: 10.58532/V3BKCM2P2CH1, https://www.iipseries.org/assets/docupload/rsl202441AB696ED5500FF.pdf .
- G. J. Chang, S.-H. Chen, and C.-H. Liu, *Edge Roman Domination on Graphs*, Graphs and Combinatorics 32 (2016), 1731–1747, DOI: 10.1007/s00373-016-1695-x .
