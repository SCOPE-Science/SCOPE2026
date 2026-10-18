# Neighborhood complexes of two-row rook graphs split into two spheres and a crown suspension
## Finding
For every integer \(n\ge4\), let \(R_n=L(K_{2,n})\cong K_2\square K_n\) be the two-row rook graph. Then
\[
\mathcal N(R_n)\simeq
\left(\bigvee^{\,n^2-3n+1}S^2\right)\vee S^{n-2}\vee S^{n-2}.
\]
In particular, \(\mathcal N(R_4)\simeq\bigvee^7 S^2\). For \(n\ge5\), the reduced integral homology is free and is nonzero only in degrees \(2\) and \(n-2\), where the ranks are \(n^2-3n+1\) and \(2\), respectively.

## Assumptions and scope
The graph \(R_n\) has vertices
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
with all distinct vertices in \(A\) adjacent, all distinct vertices in \(B\) adjacent, and \(a_i\) adjacent to \(b_i\) for each \(i\). This is the line graph of \(K_{2,n}\), equivalently the Cartesian product \(K_2\square K_n\).

For a graph \(G\), the Lovász neighborhood complex \(\mathcal N(G)\) consists of the finite vertex sets having a common neighbor in \(G\). The theorem is asserted only for \(n\ge4\). The proof is an ordinary homotopy-equivalence argument; it does not assert a global simplicial collapse of \(\mathcal N(R_n)\) onto the displayed wedge.

## Proof
For each \(i\),
\[
N(a_i)=(A\setminus\{a_i\})\cup\{b_i\},\qquad
N(b_i)=(B\setminus\{b_i\})\cup\{a_i\}.
\]
Hence, writing \(\Delta(S)\) for the simplex on \(S\),
\[
X=\bigcup_{i=1}^n\Delta\bigl((A\setminus\{a_i\})\cup\{b_i\}\bigr),\qquad
Y=\bigcup_{i=1}^n\Delta\bigl((B\setminus\{b_i\})\cup\{a_i\}\bigr),
\]
we have \(\mathcal N(R_n)=X\cup Y\).

In \(X\), the vertex \(b_i\) occurs in only the \(i\)-th displayed maximal simplex. A simplex collapses relative to a nonempty face onto that face. Therefore the \(i\)-th simplex can be collapsed, without deleting any face on \(A\), onto \(\Delta(A\setminus\{a_i\})\). Distinct \(X\)-facets meet only in faces on \(A\), so these relative collapses concatenate. Consequently
\[
X\searrow\bigcup_{i=1}^n\Delta(A\setminus\{a_i\})
=\partial\Delta(A)\simeq S^{n-2}.
\]
By symmetry,
\[
Y\searrow\partial\Delta(B)\simeq S^{n-2}.
\]

Now consider \(Z=X\cap Y\). A mixed face of \(X\) contains exactly one \(B\)-vertex, and a mixed face of \(Y\) contains exactly one \(A\)-vertex. Thus \(Z\) is one-dimensional, with edge \(\{a_i,b_j\}\) exactly when \(i\ne j\). Hence
\[
Z\cong K_{n,n}-M,
\]
the crown graph obtained by deleting a perfect matching. It is connected for \(n\ge3\), has \(2n\) vertices and \(n(n-1)\) edges, and therefore has cycle rank
\[
n(n-1)-2n+1=n^2-3n+1.
\]
Thus
\[
Z\simeq\bigvee^{\,n^2-3n+1}S^1.
\]

For \(n\ge4\), both \(X\simeq S^{n-2}\) and \(Y\simeq S^{n-2}\) are simply connected. Since \(Z\) is a connected graph, each inclusion \(Z\to X\) and \(Z\to Y\) is null-homotopic. The inclusions are simplicial cofibrations, so the ordinary union is a homotopy pushout. The homotopy pushout of two null maps from connected \(Z\) is
\[
X\vee Y\vee\Sigma Z.
\]
Substituting the three homotopy types gives
\[
\mathcal N(R_n)\simeq
S^{n-2}\vee S^{n-2}\vee
\bigvee^{\,n^2-3n+1}S^2,
\]
which is the stated result.

## Verification
The standalone verifier reconstructs \(R_n\) from its adjacency relation for \(4\le n\le8\), derives the neighborhood facets directly from the graph, checks the decomposition \(X\cup Y\), verifies that \(X\cap Y\) is exactly \(K_{n,n}-M\), and computes mod-two boundary ranks of the full neighborhood complex. It obtains
\[
\begin{array}{c|c}
n & \text{nonzero reduced Betti ranks}\\ \hline
4 & \widetilde\beta_2=7\\
5 & \widetilde\beta_2=11,\ \widetilde\beta_3=2\\
6 & \widetilde\beta_2=19,\ \widetilde\beta_4=2\\
7 & \widetilde\beta_2=29,\ \widetilde\beta_5=2\\
8 & \widetilde\beta_2=41,\ \widetilde\beta_6=2.
\end{array}
\]
These finite computations are checks of the general proof, not substitutes for it.

## Relationship to prior work
Matsushita studies fundamental groups of neighborhood complexes and records the standard neighborhood-complex framework. The first public version of that paper is arXiv:1210.2803, dated 2012-10-10; the published version lists primary MSC 55Q05. The paper discusses the categorical product \(K_2\times K_n\), which is the crown graph \(K_{n,n}-M\) appearing here as the intersection \(Z\), but it does not compute the neighborhood complex of the Cartesian product \(K_2\square K_n\).

Nilakantan and Shukla study neighborhood and Hom complexes associated with exponential graphs and the categorical product \(K_2\times K_n\). Their product notation is explicitly categorical. Their results therefore concern a different graph product and a different Hom-complex parameterization; they do not imply the homotopy type of \(\mathcal N(K_2\square K_n)\).

Searches under the aliases “two-row rook graph,” “line graph of \(K_{2,n}\),” “\(K_2\square K_n\),” “rook graph neighborhood complex,” and the displayed sphere multiplicity did not locate a covering statement. This is evidence of noncoverage, not a proof of priority.

## Limitations
The theorem starts at \(n=4\) because the null-homotopy step uses simple connectivity of \(S^{n-2}\). The case \(n=3\) has different behavior and is not part of the claim. The proof determines ordinary homotopy type, not an explicit global simple-homotopy collapse of the full neighborhood complex. There remains a residual originality risk from older or unindexed literature phrased in line-graph, rook-graph, or graph-product terminology.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803; J. Math. Sci. Univ. Tokyo 24 (2017), 321–353.
2. N. Nilakantan and S. Shukla, *Neighborhood Complexes of Some Exponential Graphs*, Electron. J. Combin. 23(2) (2016), #P2.26, DOI 10.37236/5312.
