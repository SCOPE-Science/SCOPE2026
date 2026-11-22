# Sharp simplicial Foster-curvature bounds, equality classification, and chordal rigidity

## Finding

Let \(G\) be a connected finite simple graph on \(n\ge 2\) vertices, with every edge of unit electrical resistance. For an edge \(vu\), put \(t(v,u)=|N(v)\cap N(u)|\) and let \(R(v,u)\) be the effective resistance. Define its local Foster resistance curvature by
\[
p(v)=1-\frac12\sum_{u\sim v}R(v,u).
\]
Then, at every vertex,
\[
\boxed{p(v)\ge 1-\sum_{u\sim v}\frac{1}{t(v,u)+2}.}
\]
If \(v\) is *simplicial*, meaning that its \(d\ge1\) neighbours are pairwise adjacent, the inequality specializes to
\[
\boxed{p(v)\ge\frac1{d+1}.}
\]
This bound is sharp for every pair \(n\ge d+1\ge2\). Moreover, equality holds **if and only if** every connected component of \(G-N[v]\) has neighbours in at most one vertex of \(N(v)\). Thus every noncomplete connected graph with a simplicial vertex has a nonuniform local Foster-curvature profile:
\[
\boxed{p(v)-\frac1n\ge\frac{n-d-1}{n(d+1)}>0.}
\]
In particular, a connected **resistance-regular** graph (the row sums of the effective-resistance matrix are all equal) cannot have a simplicial vertex unless it is complete. Hence a connected chordal graph is resistance-regular **if and only if it is complete**.

## Assumptions and scope

All graphs here are finite, undirected, simple, connected, and have positive unit edge conductances. The vertex set is labelled for reproducibility, but the statements are invariant under relabelling. \(N(v)\) and \(N[v]\) are respectively the open and closed graph neighbourhoods. A graph is chordal when it has no induced cycle of length at least four; the standard simplicial-vertex theorem guarantees a simplicial vertex in every nonempty chordal graph. A graph is resistance-regular if the sum \(\sum_x R(v,x)\) is independent of \(v\), which is equivalent to constancy of \(p(v)\). The average of \(p\) is \(1/n\) by Foster's theorem.

## Proof

**1. Triangle-codegree bound.** Fix an edge \(vu\) with \(t=t(v,u)\) common neighbours. Retain only the direct unit edge \(vu\) and the \(t\) internally disjoint two-edge paths \(v-w-u\) through those common neighbours, leaving any other vertices disconnected from the terminals. These paths form parallel resistors with total conductance \(1+t/2\), hence effective resistance \(2/(t+2)\). Adding back deleted edges cannot increase effective resistance (Rayleigh monotonicity), so
\[
R(v,u)\le\frac{2}{t(v,u)+2}.
\]
Sum over \(u\sim v\) and divide by two to obtain the first displayed bound.

**2. A simplicial vertex.** If \(v\) has degree \(d\) and \(N(v)\) induces a clique, then every edge \(vu\) has exactly \(d-1\) common neighbours; alternatively \(G[N[v]]\cong K_{d+1}\). Consequently \(R(v,u)\le2/(d+1)\) for all \(u\sim v\), and \(p(v)\ge1-d/(d+1)=1/(d+1)\).

**3. Exact equality condition.** Let \(C=N[v]\). A connected component \(H\) of \(G-C\) only attaches to vertices of \(N(v)\), not to \(v\). If each such component meets the clique \(C\) at at most one neighbour, every component is an electrically dangling network attached at a single terminal. A current injected and extracted inside \(C\) sends zero current through these dangling networks. Thus all resistances between vertices of \(C\) equal those of \(K_{d+1}\), giving \(p(v)=1/(d+1)\).

Conversely, suppose some external component attaches to two distinct neighbours \(a,b\in N(v)\). For the two-terminal network with \(v\) held at potential \(1\) and \(a\) held at potential \(0\), the harmonic potential on the complete subgraph \(C\) is \(1/2\) at every member of \(C\setminus\{v,a\}\), including \(b\). The external component supplies a finite-conductance connection between boundary vertices \(a\) and \(b\) of unequal potential. By the strict Dirichlet/Rayleigh principle, adding such a connection strictly raises the terminal conductance, so \(R_G(v,a)<R_{K_{d+1}}(v,a)=2/(d+1)\). The other resistances \(R_G(v,u)\) are no larger than \(2/(d+1)\); therefore \(p(v)>1/(d+1)\). This proves both directions of the equality characterization. The case \(d=1\) is included, since no component can attach to two distinct neighbours.

**4. Sharpness for every order and degree.** For \(n=d+1\), take \(K_{d+1}\). For \(n>d+1\), start with a clique \(K_{d+1}\), choose \(v\) and another clique vertex \(a\), and attach a path on \(n-d-1\) new vertices at \(a\). All components outside \(N[v]\) attach only at \(a\), so the equality criterion applies.

**5. Global rigidity.** Foster's identity \(\sum_{e\in E(G)}R(e)=n-1\) implies
\[
\sum_{x\in V(G)}p(x)=n-\sum_{e\in E(G)}R(e)=1.
\]
If \(G\) is resistance-regular, the local sums \(\sum_{u\sim v}R(v,u)\) are constant, and hence \(p(v)=1/n\) at every vertex. But if a simplicial vertex has \(d\le n-2\), the preceding bound yields \(p(v)\ge1/(d+1)>1/n\), a contradiction. Thus a simplicial vertex in a resistance-regular graph must have degree \(n-1\); because its neighbourhood is a clique, the whole graph is \(K_n\). Conversely \(K_n\) is vertex-transitive and resistance-regular. Finally every chordal graph has a simplicial vertex, proving the chordal classification. The quantitative gap follows from subtracting \(1/n\) from \(1/(d+1)\).

## Verification

The independent finite verifier `verify.py` enumerates all spanning trees directly (rather than solving the electrical network). It checks the triangle-codegree curvature inequality, the simplicial inequality, and the necessary-and-sufficient equality classification on every connected labelled simple graph of orders \(2,3,4,5\), with respective counts \(1,4,38,728\). It checks the sharpness construction for every degree at orders \(3\) through \(7\), and tests a biconnected noncomplete chordal graph (the diamond). Run `python3 verify.py` using the Python standard library. These finite tests corroborate, but do not replace, the proof for every \(n\).

## Relationship to prior work

Zhou, Wang, and Bu [1] define resistance-regularity and obtain resistance-matrix and Laplacian characterizations. Devriendt [2] develops the local resistance curvature and Foster/spanning-tree formalism. Khan and Haidar [3] show that resistance-regular graphs need not be degree-regular and prove necessary conditions including connected complement and minimum degree three for nonregular examples. Their results do not give the sharp simplicial bound, its equality classification, or the chordal rigidity conclusion. Sun, Yang, and Xu [4] establish two-connectivity for the constant-curvature class; that restriction alone does not exclude simplicial vertices of noncomplete two-connected chordal graphs (for instance the diamond). The argument here uses a different local clique electrical comparison.

## Limitations

These conclusions concern unit electrical resistances. A differently weighted complete clique need not have the equal terminal resistances used in the sharp bound. No classification of resistance-regular nonchordal graphs is claimed. The finite verification covers only the explicitly stated ranges; the unrestricted statements use Rayleigh monotonicity, the strict Dirichlet principle, and Foster's identity. Historical priority beyond the inspected sources remains provisional.

## References

[1] J. Zhou, Z. Wang, C. Bu, *On the Resistance Matrix of a Graph*, Electronic Journal of Combinatorics 23(1), P1.41 (2016). https://doi.org/10.37236/5295

[2] K. Devriendt, *Graphs with Nonnegative Resistance Curvature*, Annals of Combinatorics, first published 2025-08-06. https://doi.org/10.1007/s00026-025-00774-x

[3] M. ul Islam Khan, G. Haidar, *Resistance-regular graphs need not be regular*, arXiv:2611.21670v1 (first public 2026-11-12). https://arxiv.org/abs/2611.21670

[4] W. Sun, Y. Yang, S.-J. Xu, *On the minimum constant resistance curvature conjecture of graphs*, arXiv:2504.20448v1 (2025-04-29). https://arxiv.org/abs/2504.20448
