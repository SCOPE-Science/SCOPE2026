# Universality and a diameter transition for cyclic-retraction commuting graphs of exponent-\(p\) groups

## Finding
Let \(G\) be any finite group of prime exponent \(p\), let \(V=G/G'\cong\mathbb F_p^d\) with \(d\ge2\), and put \(|G'|=p^c\). Form the simple graph \(\Gamma_1(G)\) whose vertices are endomorphisms \(P:G\to G\) satisfying \(P^2=P\) and \(|P(G)|=p\), joining distinct \(P,Q\) when \(PQ=QP\). Then the isomorphism class of the graph depends only on \((p,d,c)\), not on the group multiplication or nilpotency class.

Its number of vertices, common degree, and number of unordered cliques of size \(k\) are respectively
\[
N=p^{c+d-1}\frac{p^d-1}{p-1},\qquad
\delta=p^{c+d-2}\frac{p^{d-1}-1}{p-1},
\]
\[
C_k=\frac{p^{ck+k(d-k)}}{k!(p-1)^k}\prod_{j=0}^{k-1}(p^d-p^j),\qquad 1\le k\le d.
\]
There are no larger cliques; every maximal clique has exactly \(d\) vertices, hence their number is \(p^{cd}|\operatorname{GL}_d(\mathbb F_p)|/[d!(p-1)^d]\).

When \(d=2\), the graph is the disjoint union of \(p(p+1)/2\) copies of \(K_{p^c,p^c}\). When \(d=3\), it is connected of diameter exactly \(3\). When \(d\ge4\), it is connected of diameter exactly \(2\). (All statements concern graph distance within components, and the smallest \(K_{1,1}\) components have diameter \(1\).)

## Assumptions and scope
The group is finite and every element has order dividing the prime \(p\). Its derived subgroup \(G'\) may be nonabelian and need not be central. The Frattini quotient \(G/G'\) is elementary abelian because the group has exponent \(p\); it is nonzero. The graph excludes the trivial retraction, the identity, and all retractions whose image has order exceeding \(p\). The dimension is at least \(2\). The clique count includes unordered collections of distinct vertices; \(C_0=1\) by convention. Note that an exponent-two group is necessarily abelian, so \(c=0\) if \(p=2\).

## Proof
**Canonical parametrization.** Any homomorphism from \(G\) into a group of order \(p\) kills \(G'\). For an endomorphism with image \(\langle h\rangle\cong C_p\), there is therefore a nonzero linear functional \(\lambda:V\to\mathbb F_p\) such that
\[
P(g)=h^{\lambda(gG')}.
\]
It is a retraction exactly if \(\lambda(hG')=1\). Thus \(hG'\ne0\). Choose the unique representative \(u\) of the projective line \(\langle hG'\rangle\) whose first nonzero coordinate is \(1\), replacing \(h\) by a suitable power and \(\lambda\) by the inverse scalar. A vertex is uniquely a triple \((u,\lambda,h)\), with \(u\) normalized, \(\lambda(u)=1\), and \(hG'=u\). For every \((u,\lambda)\) there are exactly \(|G'|=p^c\) lifts \(h\). This already proves that the graph's vertex set and fibers depend only on \((p,d,c)\).

**Commutation.** For \(P=(u,\lambda,h)\) and \(Q=(v,\mu,k)\), direct substitution gives
\[
(PQ)(g)=h^{\lambda(v)\mu(gG')},\qquad (QP)(g)=k^{\mu(u)\lambda(gG')}.
\]
If \(P\ne Q\) and these agree, they must both be trivial: otherwise their common nontrivial image forces \(\langle h\rangle=\langle k\rangle\), and each map is the identity on that image, so \(PQ=Q\) and \(QP=P\), contradicting distinctness. Conversely both are trivial when \(\lambda(v)=\mu(u)=0\). Therefore distinct vertices are adjacent exactly if
\[
\lambda(v)=0=\mu(u).
\]
No multiplication-law feature of \(G\) occurs. Hence \(\Gamma_1(G)\) is the independent \(p^c\)-fold blow-up of the graph of rank-one linear projections on \(\mathbb F_p^d\), with adjacency requiring zero products in both orders.

**Counts.** There are \((p^d-1)/(p-1)\) normalized nonzero lines \(u\), exactly \(p^{d-1}\) functionals satisfying \(\lambda(u)=1\), and \(p^c\) lifts, proving \(N\). At a fixed vertex, \(v\) may be any of the \((p^{d-1}-1)/(p-1)\) lines inside \(\ker\lambda\). For each \(v\), requiring \(\mu(v)=1\) and \(\mu(u)=0\) gives \(p^{d-2}\) functionals, followed by \(p^c\) lifts. This proves \(\delta\).

For a clique of size \(k\), its normalized vectors \(u_1,\ldots,u_k\) and functionals \(\lambda_1,\ldots,\lambda_k\) satisfy \(\lambda_i(u_j)=\delta_{ij}\). They are therefore independent and \(k\le d\). The number of ordered independent nonzero vector tuples is \(\prod_{j=0}^{k-1}(p^d-p^j)\); passing to normalized lines divides by \((p-1)^k\). There are \(p^{k(d-k)}\) ways to extend the coordinate duals to all of \(V\), and \(p^{ck}\) central-fiber lifts. Division by \(k!\) gives \(C_k\). Any such dual tuple extends to a basis and its coordinate duals, so every clique extends to size \(d\).

**Connectivity and diameter.** When \(d=2\), each projection has exactly one complementary rank-one projection. The underlying graph is a matching on \(p(p+1)\) projections and its \(p^c\)-fold independent blow-up is the stated disjoint union of complete bipartite graphs.

For \(d\ge3\), start from any distinct vertices \(P=(u,\lambda,h)\), \(Q=(v,\mu,k)\). Choose a nonzero line \(r\subset\ker\lambda\) outside \(\operatorname{span}(u,v)\). This is possible because \(\dim\ker\lambda\ge2\) and \(u\notin\ker\lambda\). Choose a functional \(\rho\) with \(\rho(r)=1\) and \(\rho(u)=\rho(v)=0\). The resulting vertex \(R\) commutes with \(P\) and satisfies \(\rho(v)=0\). Now \(W=\ker\rho\cap\ker\mu\) is nonzero, and intersects \(\operatorname{span}(r,v)\) trivially: in that span \(\rho\) kills only the \(v\)-line, while \(\mu(v)=1\). Choose \(s\in W\setminus\{0\}\), and a functional \(\sigma\) with \(\sigma(s)=1\) and \(\sigma(r)=\sigma(v)=0\). The vertex \(S\) commutes with both \(R\) and \(Q\), giving a path of at most three edges.

For \(d\ge4\), the intersection \(W=\ker\lambda\cap\ker\mu\) has dimension at least \(d-2\ge2\) and cannot be contained in \(\operatorname{span}(u,v)\): if both are two-dimensional and equal, it would contain \(u\), contradicting \(\lambda(u)=1\). Choose \(r\in W\setminus\operatorname{span}(u,v)\), and a functional \(\rho\) taking value \(1\) on \(r\) and vanishing on \(u,v\). The corresponding vertex is adjacent to both \(P,Q\). Thus diameter is at most two; distinct lifts over any one pair \((u,\lambda)\), or noncommuting rank-one projections, show that nonadjacent pairs exist, so the diameter is exactly two.

For \(d=3\), consider \(u=e_1,\lambda=e_1^*-e_2^*\) and \(v=e_2,\mu=-e_1^*+e_2^*+e_3^*\). Then \(\ker\lambda\cap\ker\mu=\langle e_1+e_2\rangle\subset\operatorname{span}(u,v)\). No rank-one projection can commute with both, so these vertices are at distance at least three. The previous path argument proves their distance is exactly three.

## Verification
Run `python3 artifacts/verify.py` from this package's root. The standalone dependency-free script enumerates all normalized rank-one projections, their central-fiber copies, and all adjacency relations for \((p,d,c)=(3,2,1),(2,2,0),(2,3,0),(3,3,0),(2,4,0)\). It independently checks vertex counts, common degrees, edge counts, connected components and diameters. All five cases passed. The checker tests the universal finite combinatorial model, not all group homomorphisms for arbitrary finite groups; the preceding factorization is the infinite/general proof.

## Relationship to prior work
Anil Kumar and Pradhan (arXiv:1908.00331v1, 2019) classify endomorphisms of extraspecial odd-order groups using symplectic quotient coordinates. A preceding finite-group classification of retracts of odd extraspecial groups counts all idempotents by image rank; it does not assert the universal cyclic-retraction commuting graph for arbitrary exponent-\(p\) groups, the clique polynomial, or the diameter transition. Existing work on commuting retractions of elementary generalized dihedral groups studies a different group family and all image ranks, not the group-independent cyclic-retraction graph here. Published matrix commuting-graph work studies all noncentral matrices rather than the present zero-product graph of rank-one idempotents with independent central fibers. These comparisons do not establish unconditional publication priority.

## Limitations
The graph is only for image-order-\(p\) retractions, not the complete endomorphism monoid, the full commuting graph of group elements, or higher-rank retractions. Groups with elements of order \(p^2\) are excluded. The isomorphism identifies abstract graphs; no canonical group-independent labeling exists without choices of quotient bases and fiber bijections. Exact historical novelty against every possible older terminology is not certified.

## References
1. C. P. Anil Kumar and S. S. Pradhan, *On the Endomorphism Semigroups of Extra-special p-groups and Automorphism Orbits*, arXiv:1908.00331v1 (August 1, 2019), https://arxiv.org/abs/1908.00331 .
2. *Retracts and idempotents of odd extraspecial groups in every rank*, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-retracts-and-idempotents-of-odd-extraspecial-groups-in-every-ran--bc309d784a08 .
3. *Commuting retractions of elementary generalized dihedral groups*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-commuting-retractions-of-elementary-generalized-dihedral-groups--0ef9efc1c172 .
4. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, J. London Math. Soc. 83 (2011), 470–492, https://doi.org/10.1112/jlms/jdq088 .
