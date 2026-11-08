# The integral arm-permutation and pole-swap module of two-point theta configurations

## Finding

For each integer \(m\ge3\), write \(G_m=K_{2,m}\) for the graph consisting of \(m\) paths of length two between two distinguished poles. Its automorphism group is \(S_m\times C_2\), acting by arm permutations and pole interchange. The unordered collision-free configuration space \(X_m=\operatorname{UConf}_2(G_m)\) satisfies

\[
X_m\simeq \bigvee^{\binom m2}S^1,\qquad
H_1(X_m;\mathbb Z)\cong \bigwedge^2\mathbb Z^m
\]

as an integral \(S_m\times C_2\)-module. A permutation of arms acts by the exterior square of its standard permutation lattice, while pole interchange acts by multiplication by \(-1\). If \(f=f(\sigma)\) and \(t=t(\sigma)\) count fixed arms and arm transpositions (two-cycles) of \(\sigma\), then the trace on first rational homology, for pole-interchange indicator \(\varepsilon\), is

\[
\chi_m(\sigma,\varepsilon)=(-1)^\varepsilon\left(\binom f2-t\right).
\]

All other positive-degree integral homology vanishes. In particular, the rank and homotopy statement are non-equivariant consequences; the integral group action and the trace formula are the representation-theoretic contribution.

## Assumptions and scope

Graphs are finite geometric one-dimensional CW complexes. The vertices of \(G_m\) are poles \(A,B\) and arm vertices \(w_i\), where \(1\le i\le m\). Its oriented edges are \(a_i:A\to w_i\) and \(b_i:w_i\to B\). Configurations consist of unordered pairs of distinct points of the geometric realization, with collisions forbidden even at vertices. The group \(S_m\) relabels the arms; \(C_2\) interchanges \(A,B\), sends \(a_i\) to the opposite orientation of \(b_i\), and fixes each \(w_i\). Since \(m\ge3\), vertices of degree \(m\) are precisely the poles, hence this is the full automorphism group.

For two particles, Prue–Scrimshaw's stable-equivalence theorem [2] applies: distinct essential vertices in this graph are separated by at least one edge, and every essential closed path contains at least four edges, exceeding the required three. Therefore the unordered Abrams cubical complex \(UD_2(G_m)\) is a deformation retract of the continuous configuration space. The relevant cubical cells are unordered collections of vertices and open edges whose closures are disjoint.

## Proof

**1. Explicit cubical cells.** Write \(X=\{A,B\}\), \(U_i=\{A,w_i\}\), \(V_i=\{B,w_i\}\), and \(W_{ij}=\{w_i,w_j\}\) for \(i<j\). These are all the zero-cells. The one-cells, with orientations inherited from \(a_i,b_i\), are

\[
 x_i=(a_i,B),\quad y_i=(b_i,A),\quad
 p_{ij}=(a_i,w_j),\quad q_{ij}=(b_i,w_j)
 \quad (i\ne j).
\]

Here \(x_i:X\to V_i\), \(y_i:U_i\to X\), \(p_{ij}:U_j\to W_{ij}\), and \(q_{ij}:W_{ij}\to V_j\). The two-cells are the squares \(s_{ij}=(a_i,b_j)\) with \(i\ne j\). No three-cell is possible with just two particles. Orient each square by its \(a_i\) and then \(b_j\) directions. Its cellular boundary is

\[
\partial s_{ij}=q_{ji}-y_j-x_i+p_{ij}.
\]

Thus the cubical complex has \(\binom{m+2}2\) vertices, \(2m^2\) edges, and \(m(m-1)\) squares.

**2. Uniform simple collapse.** For each ordered pair \(i\ne j\), the edge \(q_{ji}\) occurs in exactly one square, namely \(s_{ij}\): the stationary particle must be at \(w_i\) and the moving edge is \(b_j\). Consequently it is a free edge of that square. Removing all \(m(m-1)\) free-edge–square pairs, in any order, is an elementary cubical collapse. The remaining graph has the edges \(x_i,y_i,p_{ij}\). Each \(V_i\) is a pendant vertex connected to \(X\) by \(x_i\), and each \(W_{ij}\) subdivides the edge between \(U_i\) and \(U_j\). The edges \(y_i\) join \(U_i\) to \(X\). Thus the remaining graph is a subdivided complete graph on \(m+1\) vertices, with \(m\) pendant edges. Its cycle rank is

\[
\binom{m+1}{2}-(m+1)+1=\binom m2.
\]

It follows that \(X_m\) has the stated circle-wedge homotopy type and torsion-free integral homology concentrated in degrees zero and one.

**3. Integral basis and natural arm action.** For \(i<j\) define the one-cycle

\[
 z_{ij}=p_{ji}-p_{ij}+y_j-y_i.
\]

Its boundary is zero. The cycles \(z_{ij}\) are an integral basis of the first homology of the remaining subdivided complete graph (each is the triangle on \(X,U_i,U_j\)). Therefore they remain an integral basis in the original complex. Arm permutation \(\sigma\) maps \(z_{ij}\) to \(z_{\sigma(i),\sigma(j)}\), where changing the order of the indices changes sign. Sending \(e_i\wedge e_j\) to \([z_{ij}]\) identifies the full integral \(S_m\)-action with \(\bigwedge^2\mathbb Z^m\), where \(e_1,\ldots,e_m\) is the standard arm basis.

**4. Pole interchange.** Let \(\tau\) exchange \(A,B\) and fix every \(w_i\). Its signed cellular action is \(\tau(p_{ij})=-q_{ij}\) and \(\tau(y_i)=-x_i\). The square boundary relation gives \([q_{ji}]=[y_j+x_i-p_{ij}]\) in the first cellular homology. Hence, using \(i<j\),

\[
\begin{aligned}
[\tau z_{ij}]&=[-q_{ji}+q_{ij}-x_j+x_i]\\
&=[-y_j-x_i+p_{ij}+y_i+x_j-p_{ji}-x_j+x_i]\\
&=-[z_{ij}].
\end{aligned}
\]

This establishes the integral \(-1\) action. (The elementary collapse in step 2 need not be equivariant under pole interchange; the chain calculation proves the pole action without such an assumption.) Pole interchange commutes with every arm permutation, so the complete integral \(S_m\times C_2\)-module is the exterior square twisted by the nontrivial \(C_2\) sign character.

**5. Complete rational character.** The exterior square of a permutation matrix has trace equal to the number of unordered pairs of fixed arms minus the number of two-cycles: \(\binom{f}2-t\). The pole swap contributes the factor \((-1)^\varepsilon\). This proves the displayed formula for every group element and all \(m\ge3\).

## Verification

The embedded self-contained Python program `verification/theta_two_particle_check.py` enumerates the exact finite cubical cell sets, verifies \(\partial_1\partial_2=0\), checks that each designated edge belongs to exactly one square, evaluates the Euler rank, and confirms that the cycles above form an integral basis after eliminating all square relations. It also verifies the signed cellular actions and complete trace formula for all arm permutations through \(m=5\), and for representative permutations at \(m=6,7\). The last line of its saved run is `TWO_PARTICLE_THETA_EQUIVARIANT_PASS`. These tests corroborate, but do not replace, the uniform proof.

## Relationship to prior work

The discrete configuration-space model and stable equivalence are established by Farley–Sabalka [1] and Prue–Scrimshaw [2], and are used here rather than claimed as new. Kurlin [3] develops presentations for graph braid groups. Maciążek–Sawicki [4] study the homology of configurations on this same \(K_{2,m}\) family, including higher particle numbers, so ordinary homology and associated ranks are not asserted as a novel family calculation. The additional theorem here concerns the explicit **integral action** of every arm permutation and both pole choices, including the sign under pole interchange and a natural exterior-square lattice basis; the inspected sources do not state or imply that representation as a determined module. Unindexed equivalent formulations cannot be ruled out.

## Limitations

The result is for **two unordered collision-free particles** and for \(m\ge3\); it is not a statement about ordered particles, sink configurations, or three or more particles. The sphere-wedge homotopy equivalence is not claimed to respect every graph automorphism. The integral homology module is established, but an equivariant homotopy decomposition and arbitrary-particle generalization are not asserted. Independent mathematical validation and exhaustive publication-priority verification have not been performed.

## References

[1] D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539 (first public October 25, 2004); Algebraic & Geometric Topology 5 (2005), 1075–1109. https://arxiv.org/abs/math/0410539

[2] P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (first public September 30, 2009), Theorem 3.2, especially the unlabeled extension. https://arxiv.org/abs/0909.5511

[3] V. Kurlin, *Computing braid groups of graphs with applications to robot motion planning*, arXiv:0908.1067 (2009). https://arxiv.org/abs/0908.1067

[4] T. Maciążek and A. Sawicki, *Non-abelian quantum statistics on graphs*, Communications in Mathematical Physics 371 (2019), 921–973, Section 5.6; arXiv:1806.02846. https://doi.org/10.1007/s00220-019-03583-5
