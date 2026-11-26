# Open-packing complexes and maximal-packing polynomials of bipartite prisms

## Finding

Let \(G\) be a finite simple bipartite graph, allowing disconnected graphs and isolated vertices. Write \(G^2\) for the graph joining distinct vertices at distance one or two in \(G\), and \(\mathcal N(H)\) for the graph joining distinct vertices of \(H\) that have a common neighbor. There is a bipartition-dependent graph isomorphism
\[
\mathcal N(G\square K_2)\cong G^2\sqcup G^2.
\]
In particular, the open-packing complex of the prism is
\[
\mathcal{OP}(G\square K_2)\cong \operatorname{Ind}(G^2)*\operatorname{Ind}(G^2),
\]
where an open packing is a set of vertices with pairwise disjoint open neighborhoods and \(\operatorname{Ind}\) denotes the independence complex. Let \(I_G(z)\) count all vertex subsets of \(G\) with pairwise distances at least three, and \(J_G(z)\) count the inclusion-maximal such subsets, each by cardinality. The corresponding all-open-packing and inclusion-maximal-open-packing polynomials of the prism are
\[
O_{G\square K_2}(z)=I_G(z)^2,\qquad M_{G\square K_2}(z)=J_G(z)^2.
\]
These are coefficientwise counting identities for labelled subsets, not only identities for the largest sizes.

As an application, for a ladder \(L_n=P_n\square K_2\), \(n\ge1\), put
\[
f_n(z)=\sum_{k=0}^{\lfloor(n+2)/3\rfloor}\binom{n-2k+2}{k}z^k,
\qquad q_n(z)=[x^n]\frac{xz(1+x+x^2)^2}{1-z(x^3+x^4+x^5)}.
\]
Then \(O_{L_n}(z)=f_n(z)^2\) and \(M_{L_n}(z)=q_n(z)^2\), with every integer size from \(2\lceil n/5\rceil\) to \(2\lfloor(n+2)/3\rfloor\) attained by an inclusion-maximal open packing. The contribution is the general prism decomposition and its all-set and maximal-set transfer; the factor \(q_n\) is already counted in the open-chain blockade model [7, §6], and the path-square purity classification is due to Deniz [2].

## Assumptions and scope

Graphs are finite, undirected and simple. Distances between distinct components are infinite. The graph square has no loops. The prism has its usual horizontal edges from \(G\) and a vertical matching edge at each vertex. Use any bipartition of each component; the relabeling can depend on this choice. In the join the two factors have disjoint vertex sets. The all-set polynomial includes the empty set, and a maximal set means inclusion-maximal, not necessarily maximum-size.

## Proof

**Graph decomposition.** Let \(c:V(G)\to\{0,1\}\) be a bipartition map and use prism coordinates \((u,i)\) for \(i\in\{0,1\}\). Define \(h=i\oplus c(u)\), with addition modulo two. All prism edges change \(h\): a vertical edge changes \(i\), and a horizontal edge changes \(c(u)\). Vertices in different new layers cannot have a common neighbor. For fixed \(h\), there is one representative of each base vertex \(u\) in that layer. Its prism neighbors project bijectively to the closed neighborhood \(N_G[u]\) in the other new layer: the vertical neighbor projects to \(u\) and the horizontal neighbors project to the base neighbors. Thus two distinct same-layer representatives share a neighbor exactly if \(N_G[u]\cap N_G[v]\ne\varnothing\), equivalently \(d_G(u,v)\le2\). This proves the two-copy isomorphism, including singleton components.

**Faces, maximal faces, and colors.** Open packings are precisely independent sets in \(\mathcal N(H)\). Choosing a face in the join is choosing an independent set in each of the two copies of \(G^2\); the face is maximal if and only if both choices are maximal. Sizes add, so the two enumerators multiply. For comparison, proper \(k\)-colorings of \(\mathcal N(H)\) are injective \(k\)-colorings of \(H\), and a fixed palette gives \(\chi_{G^2}(k)^2\) such colorings of the prism for \(k\ge1\). The resulting equality \(\chi_i(G\square K_2)=\chi(G^2)\) is a corollary, not a separate priority claim.

**All path packings.** A \(k\)-set of indices \(1\le s_1<\cdots<s_k\le n\) is independent in \(P_n^2\) if and only if successive spacings are at least three. For \(k\ge1\), subtracting \(2(i-1)\) from \(s_i\) bijects these sets with ordinary \(k\)-subsets of \(\{1,\ldots,n-2k+2\}\). The constant term is one from the empty set. This gives \(f_n(z)\).

**Maximal path packings.** A nonempty packing is maximal if and only if its closed radius-two neighborhoods cover the path. The first index must be within two of 1, the last within two of \(n\), and interior spacings must lie in \(\{3,4,5\}\). Let \(a=s_1-1\), \(b=n-s_k\) denote the endpoint offsets. Then
\[
n=1+a+b+\sum_{i=1}^{k-1}(s_{i+1}-s_i),\qquad a,b\in\{0,1,2\}.
\]
The starting selected vertex contributes \(xz\), the two endpoint offsets contribute \((1+x+x^2)^2\), and each interior gap and subsequent selected vertex contributes \(z(x^3+x^4+x^5)\). Summing over any number of gaps gives the display for \(q_n(z)\). These gap constraints and the resulting series also follow from Krapivsky and Luck [7, equations (6.3)–(6.6)]: in their open chain, a blocked configuration at blockade range two has two to four empty sites between occupied sites and zero to two at each end. Relabel the variables to use \(x\) for chain length and \(z\) for occupancy, and drop their length-zero term. For fixed \(k\), the possible values of \(n\) are all integers from \(3k-2\) to \(5k\), by summing integer intervals. Hence the path-square factor's maximal sizes are all integers from \(\lceil n/5\rceil\) to \(\lfloor(n+2)/3\rfloor\). The sumset of two copies of this interval is the ladder spectrum in the finding.

The ladder join is pure exactly when \(P_n^2\) is well-covered. Deniz's path-square classification [2, Observation 1(i)] states that this holds exactly for \(n\in\{1,2,3,6\}\). The size interval recovers this known classification in the prism setting: the endpoints agree exactly at those values, since they differ for \(n=4,5,7,8,9\) and \(\lceil n/3\rceil>\lceil n/5\rceil\) for \(n\ge10\).

## Verification

The companion Python program `check_prism.py` builds the prism and common-neighbor graph directly. The recorded finite checks compare every adjacency and the all-face polynomial on the 427 bipartite labelled simple graphs on one to five vertices, test the all and maximal path polynomials and maximal sizes through order twelve, and directly enumerate maximal open packings of ladders through seven rungs. It also checks that the conflict graph of \(C_5\square K_2\) is connected, demonstrating the nonbipartite boundary. The mathematical proof supplies the all-order assertions; these finite checks are not formal verification.

## Relationship to prior work and limitations

Brešar, Klavžar and Rall [1, Theorem 2.2] prove the scalar equality \(\rho^{\mathrm o}(G\square K_2)=2\rho_2(G)\) for bipartite \(G\). Their proof transforms a maximum open packing to a fiber-doubled open packing; this does not encode every labelled face or its inclusion-maximality. The earlier circular-ladder calculation [3] gives the two-copy graph and all-size polynomial for even-cycle bases (and a different conflict graph for odd-cycle bases), which is partial prior coverage. The generic common-neighbor-graph correspondence is prior [4,5]. Deniz [2] already gives the exact well-covered path squares, and Krapivsky and Luck [7] already enumerate all blocked configurations on the open chain by length and cardinality at general blockade range, yielding the maximal path-square factor and its size support at range two. The ladder formulas illustrate the structural transfer without a priority claim on the one-dimensional factors. The coloring equality is included only as a consequence. Song and Yue [6] treat the Cartesian product among graph operations; without the full text, overlap with the injective-coloring corollary remains unresolved. The general prism statement is confined to bipartite bases, with no claim of a canonical decomposition before a bipartition is chosen. The priority comparison is bounded to the inspected sources.

## References

1. B. Brešar, S. Klavžar and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1, 2023-09-10. https://arxiv.org/pdf/2309.04963v1
2. Z. Deniz, *On the well-coveredness of square graphs*, Communications Faculty of Sciences University of Ankara Series A1 Mathematics and Statistics 71(2) (2022), 490–501. https://doi.org/10.31801/cfsuasmas.910947
3. *Complete open-packing polynomial and six-residue maximum census of circular ladders*, Resultary, 2026-10-18, record caf3fe2c4a63. https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-complete-open-packing-polynomial-and-six-residue-maximum-census--caf3fe2c4a63
4. B. Brešar, B. Samadi and I. G. Yero, *Injective coloring of graphs revisited*, arXiv:2106.09823. https://arxiv.org/abs/2106.09823
5. B. Samadi, N. Soltankhah and I. G. Yero, *Injective coloring of product graphs*, arXiv:2306.01488. https://arxiv.org/abs/2306.01488
6. J. Song and J. Yue, *Injective coloring of some graph operations*, Applied Mathematics and Computation 264 (2015), 279–283. https://doi.org/10.1016/j.amc.2015.03.124
7. P. L. Krapivsky and J. M. Luck, *A renewal approach to configurational entropy in one dimension*, arXiv:2302.08852v2, especially §6. https://arxiv.org/pdf/2302.08852v2
