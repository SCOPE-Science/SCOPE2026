# Nonpositively curved graph-Hom cubulations of folded odd cubes

## Finding

**Theorem.** For every odd integer \(n\ge7\), let \(F_n\) be the folded \(n\)-cube and let \(X_n=\operatorname{Hom}(C_n,F_n)\) be the *ordinary polyhedral* graph-Hom complex. Then \(X_n\) is a connected, nonpositively curved cube complex of dimension \((n-1)/2\). Its link at **every** vertex is the simplicial independence complex \(\operatorname{Ind}(C_n)\). In particular its universal cover is CAT(0) and contractible, so \(\pi_k(X_n)=0\) for every \(k\ge2\). For odd \(n\ge7\), \(X_n\) is not a topological manifold, with or without boundary.

Moreover the number of \(d\)-dimensional cubes is exactly
\[
f_d(X_n)=\frac{2^{n-1}n!}{2^d}\frac{n}{n-d}\binom{n-d}{d},\qquad 0\le d\le\frac{n-1}{2},
\]
and its Euler characteristic is
\[
\chi(X_n)=2^{n/2}n!\cos(n\pi/4)=\pm 2^{(n-1)/2}n!.
\]
For example, \(X_7\) has cube counts \((322560,1128960,1128960,282240)\), dimension three and Euler characteristic \(40320\). The formula determines the Euler characteristic, not the separate Betti numbers or the fundamental-group presentation.

## Assumptions and scope

The folded \(n\)-cube is the simple loopless graph with vertex group
\[
V_n=\mathbb F_2^n/\langle\boldsymbol 1\rangle,\quad \boldsymbol 1=(1,\ldots,1),
\]
and edges \(x\sim x+\bar e_j\), where \(\bar e_j\) is the image of the \(j\)-th standard basis vector. Odd \(n\ge7\) is required. The source \(C_n\) has vertices \(\mathbb Z/n\mathbb Z\) and edges between consecutive indices. A cell of \(\operatorname{Hom}(C_n,F_n)\) is a product \(\prod_i\Delta(A_i)\) of simplices over nonempty vertex sets \(A_i\subseteq V_n\), where every pair in \(A_i\times A_{i+1}\) is an edge of \(F_n\). Such cells glue along coordinatewise faces. The geometric realization, with the usual unit Euclidean metric on each cubical cell, is meant throughout.

## Proof

**1. Closed walks are permutations.** The only linear relation among \(\bar e_1,\ldots,\bar e_n\) over \(\mathbb F_2\) is their total sum. Let \(f:C_n\to F_n\) be a graph homomorphism and write the successive edge increments as \(\bar e_{a_0},\ldots,\bar e_{a_{n-1}}\). Closure says their sum is zero. The parity vector of occurrence counts is either all zero or all one. Because there are \(n\) increments and \(n\) is odd, the all-even option is impossible. Each generator therefore occurs an odd positive number of times, hence exactly once. Conversely any starting point in \(V_n\) and any permutation of the generators yields a unique closed walk. Thus there are exactly \(N=2^{n-1}n!\) vertices in \(X_n\).

**2. The only local moves are adjacent transpositions.** Fix a vertex-map \(f\), with consecutive generator labels \(a_i\) (subscripts modulo \(n\)). The target vertices \(f(i-1)\) and \(f(i+1)\) differ by \(\bar e_{a_{i-1}}+\bar e_{a_i}\), with distinct generators. When \(n\ge5\), this difference has exactly two representations as a path of length two in \(F_n\): the two orders of the given generators. Indeed an equality of sums of at most four basis images lifts to either an even-multiplicity relation or the total \(n\)-term relation. The second is impossible for an even sum of at most four terms with odd \(n\ge5\). Hence their common-neighbor set is exactly
\[
\{f(i),f'(i)\},\qquad f'(i)=f(i-1)+f(i)+f(i+1),
\]
where addition is in \(V_n\). The change \(f(i)\mapsto f'(i)\) exchanges consecutive generator labels \(a_{i-1}\) and \(a_i\).

For any cell containing \(f\), its coordinate set \(A_i\) is a subset of these two common neighbors, so \(A_i\) has size one or two. Two neighboring positions cannot both have size two: the two simultaneously changed values would differ by \(\bar e_{a_{i-1}}+\bar e_{a_{i+1}}\), which is not a generator. Conversely every collection of pairwise nonadjacent positions can be simultaneously doubled, since the new value at a position remains adjacent to both unchanged neighboring values. Hence exactly the independent subsets of the position cycle \(C_n\) index cubes incident to \(f\). There are no higher-than-cubical cells.

**3. Links and curvature.** A \(d\)-cube containing \(f\) corresponds to an independent \(d\)-set of positions; restricting to its coordinate faces is restricting to subsets. Therefore \(\operatorname{Lk}_{X_n}(f)\cong\operatorname{Ind}(C_n)\) *as an abstract simplicial complex*, for every vertex. Independence complexes are flag: every clique of mutually compatible choices is an independent set. Thus all cubical vertex links are flag. Gromov's cubical link criterion gives a nonpositively curved piecewise-Euclidean metric on \(X_n\), and the Cartan–Hadamard theorem for these complete locally CAT(0) length spaces makes the universal cover CAT(0) and contractible. Hence \(X_n\) is aspherical.

**4. Connectivity.** Moves at source positions \(1,\ldots,n-1\) swap adjacent entries of the generator permutation without changing \(f(0)\). They generate every permutation at fixed starting point. Arranging any two desired generators at the final and first positions and then moving source position zero translates \(f(0)\) by the sum of those two generators. All such pair sums span \(V_n\): in \(\mathbb F_2^n\) they span the even-parity subspace of dimension \(n-1\), and because \(n\) is odd the all-one quotient relation is not in that subspace. Thus all starting points communicate through the one-skeleton, which is connected.

**5. Cell counts and Euler characteristic.** The number of independent \(d\)-sets in an \(n\)-cycle is the number of \(d\)-edge matchings,
\[
m_d(C_n)=\frac{n}{n-d}\binom{n-d}{d}
\quad(0\le d\le (n-1)/2).
\]
Each cube contributes one incidence at each of its \(2^d\) vertices. Double-counting gives the displayed \(f_d\). The cycle matching polynomial \(M_n(t)=\sum_d m_d(C_n)t^d\) satisfies \(M_n(t)=\lambda_+(t)^n+\lambda_-(t)^n\), where \(\lambda_\pm(t)=(1\pm\sqrt{1+4t})/2\) (verified from the matching deletion recurrence and the three- and four-cycle bases). At \(t=-1/2\), the roots are \((1\pm i)/2\), and so
\[
\chi(X_n)=N M_n(-1/2)=2^{n/2}n!\cos(n\pi/4).
\]
For odd \(n\), the cosine is always \(\pm1/\sqrt2\), giving the claimed signed integer.

**6. Non-manifold property.** For \(n=7\), \(\operatorname{Ind}(C_7)\) consists of seven triangles, fourteen edges and seven vertices. Each edge joining positions cyclically separated by three belongs to exactly one triangle. Collapsing those seven triangles along their respective unique free edges leaves the seven-cycle formed by edges of cyclic separation two. Thus its first integral homology is \(\mathbb Z\), so the link is neither a sphere nor a ball and \(X_7\) is not a topological three-manifold, including with boundary. For odd \(n\ge9\), \(\operatorname{Ind}(C_n)\) has maximal independent sets of cardinality \(\lfloor n/2\rfloor\) and also inclusion-maximal independent sets of cardinality \(\lceil n/3\rceil\), strictly smaller. The latter arise from cyclic gaps of size two and three, whose lengths sum to \(n\). Thus each vertex link is not pure and contains points of different local dimensions; a cubical neighborhood consequently cannot be locally homeomorphic to a manifold or manifold with boundary.

## Verification

The accompanying dependency-free Python file `verify_folded_hom.py` independently constructs the finite Cayley graphs, all \(1920\) vertex maps for \(n=5\), all allowable alternative target values, and every candidate cube incident to each vertex. It verifies the combinatorial cube-link criterion exhaustively for \(n=5\). For \(n=7\) it checks a deterministic sample of twelve among \(322560\) vertex maps, and compares exact formula counts. It also computes the reduced mod-two link Betti numbers for \(n=5,7,9\). The text file `verification_output.txt` contains a replay of those checks. The all-parameter conclusion is proved in Sections 1–6 above, *not* inferred from finite samples. The all-parameter matching count is exact combinatorics.

## Relationship to prior work

The source motivating this question is the square-free-target Hom classification by Fujii, Kimura and Nozaki (first publicly posted December 26, 2024), which describes components for target graphs without four-cycles. The folded cubes considered here have four-cycles: for distinct generators \(a,b\), the vertices \(x,x+\bar e_a,x+\bar e_a+\bar e_b,x+\bar e_b\) form a square. Thus the hypotheses of that classification, and of Matsushita's parallel square-free-target study, fail. Babson–Kozlov introduce the graph-Hom construction but do not state this folded-cube cubulation. Standard flag-link curvature results supply the geometric implication *after* the new exact cube-link calculation. The isolated \(n=5\) Clebsch case has been calculated separately; the theorem here starts at \(n=7\) and is not an extrapolation from its surface genus.

## Limitations

The theorem is for odd \(n\ge7\) and ordinary polyhedral Hom, not the clique complex of the homomorphism-reconfiguration graph. It does not compute \(\pi_1\) presentations, individual Betti numbers, or graph-Hom complexes for arbitrary targets. Its asphericity conclusion depends on the full cubical face structure, not only the graph of one-vertex recolorings. Literature priority was assessed against accessible primary papers and published mathematical records, but an unindexed equivalent theorem remains possible. No independent mathematical audit has been performed.

## References

- S. Fujii, K. Kimura, Y. Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039, first posted 2024-12-26. https://arxiv.org/abs/2412.19039
- T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144, first posted 2024-12-26. https://arxiv.org/abs/2412.19144
- E. Babson, D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056. https://arxiv.org/abs/math/0310056
- D. E. Roberson et al., *Cores of cubelike graphs*, European Journal of Combinatorics 87 (2020), 103092. https://doi.org/10.1016/j.ejc.2020.103092
- M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250. https://arxiv.org/abs/1106.6250
- *Special cubulation of strict hyperbolization*, Inventiones mathematicae (2024), Section 2.1 (statement of the flag-link criterion). https://link.springer.com/article/10.1007/s00222-024-01241-9
