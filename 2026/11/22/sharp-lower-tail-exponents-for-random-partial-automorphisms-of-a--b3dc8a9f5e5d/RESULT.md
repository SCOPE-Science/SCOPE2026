# Sharp lower-tail exponents for random partial automorphisms of a finite path

## Finding
Let \(P_n\) be the undirected path on \([n]\), and let \(\mathcal I_n=\operatorname{PAut}(P_n)\) be the inverse monoid of all isomorphisms between vertex-induced subgraphs, including the empty map. Uniformly sample \(\Phi_n\in\mathcal I_n\). Write \(R_n\) for its domain cardinality, \(C_n\) for the number of connected components of the induced domain graph (including \(C_n=0\) for the empty domain), and \(E_n=R_n-C_n\) for the number of edges of the induced domain graph. Put \(h_n=\lceil n/2\rceil\).

**The single result is a sharp component-deficit and rank-deficit law for uniform partial automorphisms.** For every integer \(n\ge1\) and \(0\le k\le h_n\), both tail probabilities satisfy
\[
\boxed{\frac{k!}{8^n h_n!}\ \le\ \Pr(C_n\le k),\ \Pr(R_n\le k)\ \le\ \frac{8^n k!}{h_n!}.}
\]
Consequently, for every fixed real \(0<\alpha<1/2\),
\[
\boxed{\lim_{n\to\infty}\frac{\log\Pr(C_n\le\lfloor\alpha n\rfloor)}{n\log n}
=\lim_{n\to\infty}\frac{\log\Pr(R_n\le\lfloor\alpha n\rfloor)}{n\log n}
=\alpha-\frac12.}
\]
In the same uniform model,
\[
\frac{C_n}{n}\xrightarrow{\Pr}\frac12,\qquad
\frac{R_n}{n}\xrightarrow{\Pr}\frac12,\qquad
\frac{E_n}{n}\xrightarrow{\Pr}0,
\qquad
\log|\mathcal I_n|=\frac12 n\log n+O(n).
\]
More quantitatively, for each fixed \(0<\varepsilon<1/2\),
\[
\Pr(|R_n-h_n|\ge\varepsilon n)
\le\exp(-\varepsilon n\log n+O_\varepsilon(n)),
\quad
\Pr(E_n\ge\varepsilon n)
\le\exp(-\tfrac{\varepsilon}{2}n\log n+O_\varepsilon(n)).
\]
Thus, after deleting \(o_{\Pr}(n)\) vertices, both the domain and image of a uniformly chosen partial automorphism consist of independent sets of asymptotic size \(n/2\), and its restriction is a bijection between those independent sets.

## Assumptions and scope
The path is labeled and loopless. All elements are **induced-subgraph isomorphisms**, so they preserve both edges and nonedges, unlike injective partial graph homomorphisms. Rank means cardinality of a partial map's domain, not the minimum number of generators of its monoid. The probability distribution is uniform over distinct partial maps, not over domains, isomorphism classes, or semigroup conjugacy classes. All limits are as integers \(n\to\infty\); \(\log\) is natural logarithm. The estimate in the first display holds for all finite positive \(n\), while the logarithmic large-deviation limits require fixed \(\alpha\in(0,1/2)\).

## Proof
**1. A component bound.** A nonempty subset \(S\subseteq[n]\) has \(r=|S|\) occupied vertices and \(c\) maximal consecutive runs. Each run except possibly the last requires a distinct unoccupied separator, hence \(c\le\min(r,n-r+1)\le h_n\). For the empty set take \(r=c=0\). The induced graph is a disjoint union of \(c\) paths, and its edge count is exactly \(r-c\).

**2. The factorial sandwich.** There are exactly \(4^n\) ordered pairs \((S,T)\) of subsets. Given an induced-subgraph isomorphism \(S\to T\) with \(c\) source components, it must permute these components, respecting their lengths; each non-singleton component permits at most two orientations. Hence the number of isomorphisms between a fixed ordered pair with \(c\) components is at most \(2^c c!\). In particular,
\[
|\mathcal I_n|\le4^n 2^{h_n}h_n!\le8^n h_n!.
\]
A fixed maximum independent set of the path has \(h_n\) vertices. Every permutation of its vertices is an induced-subgraph automorphism, giving \(|\mathcal I_n|\ge h_n!\). More generally, for any \(0\le k\le h_n\), a fixed independent set of cardinality \(k\) contributes \(k!\) distinct partial automorphisms with \(R_n=C_n=k\). On the other hand, the total number of elements with \(C_n\le k\) is at most \(4^n2^{h_n}k!\le8^n k!\). Since \(R_n\le k\) implies \(C_n\le k\), dividing these counts by the above bounds for \(|\mathcal I_n|\) gives both claimed finite-probability inequalities.

**3. Sharp rare-event rate.** Fix \(0<\alpha<1/2\) and let \(k_n=\lfloor\alpha n\rfloor\). Stirling's estimate yields
\[
\log(k_n!/h_n!)=(\alpha-\tfrac12)n\log n+O_\alpha(n).
\]
Applying logarithms to either factorial sandwich proves the asserted two exact logarithmic rates. The cardinality estimate follows at once from \(h_n!\le|\mathcal I_n|\le8^n h_n!\) and Stirling.

**4. Typical rank and edge scarcity.** The component count is at most \(h_n\), and the exact lower-tail rate shows \(C_n/n\to1/2\) in probability. The same rate implies \(\Pr(R_n\le h_n-\varepsilon n)\le\exp(-\varepsilon n\log n+O_\varepsilon(n))\). On the other side, \(C_n\le n-R_n+1\), so \(R_n\ge h_n+\varepsilon n\) forces \(C_n\le h_n-\varepsilon n+O(1)\), giving the same exponent by the factorial upper bound. Further, \(E_n=R_n-C_n\) and \(C_n\le n-R_n+1\) imply \(2C_n+E_n\le n+1\). Thus \(E_n\ge\varepsilon n\) forces \(C_n\le h_n-\varepsilon n/2+O(1)\), giving the stated bound. To obtain the final structural interpretation, discard every vertex in a component of size at least two from the domain: a component of length \(\ell\ge2\) contains \(\ell\le2(\ell-1)\) vertices, so at most \(2E_n=o_{\Pr}(n)\) vertices are discarded. Each retained vertex belongs to a singleton component. Isomorphisms preserve component lengths, so their images also constitute an independent set of the same size, and the map restricts to a bijection. The remaining size is \(R_n-o_{\Pr}(n)=(1/2+o_{\Pr}(1))n\).

## Verification
The standalone Python 3 standard-library checker `verify_path_tails.py` obtains the finite component/rank/edge distributions from run profiles and separately enumerates every injective partial map on paths of sizes one through six, explicitly checking adjacency and nonadjacency on all selected vertices. It tests exact equality of the three enumerators, including total sizes \(2,7,22,71,252,935\), and then verifies the finite factorial inequalities for paths of sizes \(8,12,16,20\). It prints `CHECKS PASS` on success. These finite checks corroborate boundary cases and arithmetic only; the all-size theorem follows from the preceding factorial sandwich and the deterministic component inequalities.

## Relationship to prior work
Chih and Plessas (2015) defined the inverse semigroup of isomorphisms between induced subgraphs of a finite graph; its specialization to paths supplies the archival object. Dimitrova, Fernandes, Koppitz, and Quinteiro (2021), Theorem 2.1, explicitly counted **all** partial automorphisms of finite paths by a sum over binary domain patterns, and their work already contains the finite run-type enumeration. This finding claims **neither** a new finite cardinality formula nor a new rank polynomial: those can be read from the earlier counting framework. The additional statement here is the **sharp factorial-speed lower-tail probability law**, together with the resulting typical near-independence of the supports. A prior path-specific semigroup-algebra block decomposition gives component types and automorphism groups, but does not state these asymptotic tail exponents. A study of partial automorphisms of crown posets establishes half-factorial logarithmic growth for a different family; it does not give the path-domain rare-event law.

## Limitations
The leading logarithmic probability exponent does not furnish a sharp subexponential prefactor, a central limit theorem, or a fluctuation scale below linear order. The derived upper-tail estimates for unusually large image rank and induced-edge count are one-sided bounds, not claimed exact large-deviation limits. The 2021 exact finite enumeration is prior work and is not part of the claimed finite mathematical content.

## References
1. T. Chih and D. Plessas, *Graphs and Their Associated Inverse Semigroups*, arXiv:1506.02093, first public 2015-06-06, especially Definition 2.2, https://arxiv.org/abs/1506.02093.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *Partial Automorphisms and Injective Partial Endomorphisms of a Finite Undirected Path*, arXiv:2101.12468, first public 2021-01-29, especially Corollary 1.6 and Theorem 2.1, https://arxiv.org/abs/2101.12468.
3. *Matrix-block decomposition and an Euler spectrum for path partial-automorphism algebras*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-matrix-block-decomposition-and-an-euler-spectrum-for-path-partia--e10bdab97d3d.
4. *Rank polynomial and half-factorial growth of finite crown partial-automorphism monoids*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rank-polynomial-and-half-factorial-growth-of-finite-crown-partia--5cf963fdeacf.
