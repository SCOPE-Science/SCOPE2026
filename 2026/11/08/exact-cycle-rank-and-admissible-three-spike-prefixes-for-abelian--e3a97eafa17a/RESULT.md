# Exact cycle rank and admissible three-spike prefixes for Abelian pattern Sturmian words

## Finding
For all integers \(0\le a<b<c\), put \(E=\{a,b,c\}\) and \(g=\gcd(b-a,c-b)\). In the additive incidence graph \(\Gamma_E\), with edges \(L_iR_j\) whenever \(i+j\in E\), the dimension of the ordinary cycle space of its finite nonisolated core is
\[
\beta_1(\Gamma_E)=\max\{0,a+b-c+g+1\}.
\]
In particular the graph is a forest precisely when
\[
c-b>a+\gcd(b-a,c-b).
\]
This is also the exact criterion for the three positions \(a,b,c\) to be the *first three elements of the designated sparse-symbol support* of an infinite Abelian pattern Sturmian characteristic word whose support incidence graph is a forest. It is not a claim about which letter is called \(1\) before the forest-support relabeling.

## Assumptions and scope
All indices are nonnegative integers; \(a,b,c\) are distinct and strictly increasing. The graph has separate left and right copies of the nonnegative integers. Only vertices with index at most \(c\) can be nonisolated. Its cycle-space dimension means \(|E(G)|-|V(G)|+\kappa(G)\) for a finite core \(G\), where \(\kappa\) is the number of connected components including any isolated core vertices. Infinite isolated vertices do not affect this number. A forest has zero cycle-space dimension.

The phrase *Abelian pattern Sturmian* is used in the sense of Zeng--Xue--Zeng (2026): an infinite binary characteristic word \(\mathbf1_D\) with forest incidence graph \(\Gamma_D\) has the minimal Abelian maximal pattern complexity at every pattern size. The sparse support is explicitly \(D\); no converse for arbitrarily chosen labels of an infinite word is asserted.

## Proof
**1. Contract a canonical matching.** Set \(s=c-b\), \(t=c-a\), so \(1\le s<t\), and let \(N=c\). Restrict \(\Gamma_E\) to \(L_0,\ldots,L_N\) and \(R_0,\ldots,R_N\). Edges with sum \(c\) form the perfect matching \(L_iR_{c-i}\) for \(0\le i\le c\). Contract every matching edge. The remaining edges of sum \(b\) join contracted vertices labeled \(i\) and \(i+s\), for all \(0\le i\le N-s\). Edges of sum \(a\) join labels \(i\) and \(i+t\), for \(0\le i\le N-t\). As \(0<s<t\), these are distinct nonloop edges. Thus the contracted graph is the two-distance graph \(H_N(s,t)\) on \(\{0,\ldots,N\}\), with \(i\) adjacent to \(j\) exactly when \(|i-j|\in\{s,t\}\). Contracting a nonloop edge reduces vertices and edges by one and preserves the cycle-space dimension, hence \(\beta_1(\Gamma_E)=\beta_1(H_N(s,t))\). It also preserves the property of being a forest.

**2. The critical interval graph is a union of paths.** Set \(M=s+t\) and \(g=\gcd(s,t)\). On residues \(0,\ldots,M-1\), consider the permutation \(F(x)=x+s\pmod M\). The undirected edges of its permutation cycles are exactly the pairs at distance \(s\) or \(t=M-s\). There are \(g\) disjoint simple cycles, each containing the \(M/g\ge3\) elements of one residue class modulo \(g\). Deleting the final \(g\) labels \(M-g,\ldots,M-1\) removes exactly one vertex from each cycle. Consequently \(H_{M-g-1}(s,t)\) is the disjoint union of \(g\) paths, one per residue class, and is a forest. Every \(H_N\) for \(N<M-g-1\) is an induced subgraph of that forest.

**3. Count all cycles beyond the threshold.** At \(N=M-g-1\) the graph has \(g\) connected components. For \(M-g\le N\le M-1\), its new vertices remain in those already connected residue classes; at \(N\ge M\), each new vertex \(N\) connects to the earlier vertex \(N-s\). Thus for every \(N\ge M-g-1\), the graph has exactly \(g\) components. In this range \(N+1\ge t\), so its number of edges is
\[
(N+1-s)+(N+1-t)=2(N+1)-M.
\]
Its cycle-space dimension is therefore
\[
2(N+1)-M-(N+1)+g=N+1-M+g.
\]
For smaller \(N\) the graph is a forest. Hence for every \(N\ge0\),
\[
\beta_1(H_N(s,t))=\max\{0,N+1-s-t+g\}.
\]
Substituting \(N=c\), \(s=c-b\), \(t=c-a\), and \(g=\gcd(b-a,c-b)\) gives the claimed exact formula and forest criterion, including the equality boundary \(c-b=a+g\), where exactly one independent cycle occurs.

**4. Infinitely extend every admissible triple.** Suppose \(\Gamma_E\) is a forest and let \(d>2c\). The edges introduced by adding the new sum \(d\) form a matching. For each such edge \(L_iR_{d-i}\), at most one endpoint has index at most \(c\); all edges previously present have both endpoints at most \(c\). Thus each new edge attaches a fresh leaf to an old component or joins two previously isolated vertices, and no cycle is created. Repeating with a strictly increasing sequence whose new term exceeds twice the previous maximum yields an infinite \(D\) beginning with \(a,b,c\) whose incidence graph is a forest: any finite cycle would have appeared at some finite stage. The 2026 incidence-forest theorem then identifies \(\mathbf1_D\) as Abelian pattern Sturmian. Conversely, a cycle in \(\Gamma_E\) persists in \(\Gamma_D\) for any \(D\supseteq E\), so no forest-support extension is possible.

## Verification
The standalone standard-library program `checker.py` independently constructs the original bipartite graph, computes its cycle rank via union-find, and compares with the closed formula for 13,750 ordered triples \((a,b,c)\), plus 1,000 additional deterministic random cases with larger parameters. It also verifies 6,635 one-step sparse extensions of acyclic triples. Run `python3 checker.py`; the expected output begins with `CHECKS_OK`. This finite verification is not a proof of the quantified infinite claim: Steps 1--4 give that proof.

Boundary examples: \(E=\{0,1,2\}\) has cycle rank \(1\); \(E=\{0,1,3\}\) has cycle rank \(0\) and admits an infinite forest-support continuation; \(E=\{2,5,7\}\) has cycle rank \(2\).

## Relationship to prior work
Zeng, Xue and Zeng (2026), Theorem E and Section 7, characterize Abelian pattern Sturmian words using infinite sparse supports with acyclic additive incidence graphs, and give a sufficient superlacunarity condition. Their inspected text does not state an exact criterion for an arbitrary three-element initial support or its full cycle-space dimension. The graph of Step 1 is a two-period Fine--Wilf graph; the classical Fine--Wilf threshold and Rankin's subsequent graph treatment already explain its connectivity behavior. The contribution here is the explicit additive-incidence contraction, complete three-support cyclomatic classification, and sharp support-prefix feasibility criterion. The two-distance connectivity threshold and the general forest characterization are prior results and are not independently claimed.

## Limitations
Only three-point *finite* supports have the closed formula. It does not classify arbitrary larger support sets or give the complexity of a fixed finite binary word. The infinite-word consequence concerns the designated forest-support labeling; relabeling the alphabet may swap a dense and a sparse letter. The exact formula may be deducible implicitly from older treatments of two-period graphs; historical priority of the specific incidence-graph transfer has not been independently certified.

## References
1. Q. Zeng, Y. Xue and C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059, first public version 2026-09-23, v3 2026-10-22, especially Theorem E and Sections 7.1--7.3. https://arxiv.org/html/2609.28059v3
2. S. A. Rankin, *Fine-Wilf graphs and the generalized Fine-Wilf theorem*, arXiv:0906.1780v1 (2009), especially introduction and the definition of period graphs. https://arxiv.org/pdf/0906.1780
3. N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, Proc. Amer. Math. Soc. 16 (1965), 109--114. https://doi.org/10.1090/S0002-9939-1965-0174934-9
