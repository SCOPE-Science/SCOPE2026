# Minimal-ideal orbit census of a four-variable squarefree cubic truncation

## Finding
Let \(k=\mathbb F_q\), where \(q\) is any prime power, and set
\[
A=k[x_1,x_2,x_3,x_4]/(x_1^2,x_2^2,x_3^2,x_4^2,(x_1,x_2,x_3,x_4)^3).
\]
The group of unital \(k\)-algebra automorphisms of \(A\) acts on its nonzero minimal ideals. The **complete number of orbits** is
\[
\boxed{\mathcal O(q)=
\begin{cases}
2,&q\text{ even},\\
\displaystyle\frac{q^2+7q+46+2\gcd(3,q-1)}{6},&q\text{ odd}.
\end{cases}}
\]
In characteristic two the two orbits correspond to alternating tensor ranks \(2\) and \(4\). In odd characteristic, every minimal ideal has a six-coordinate support graph on four vertices; the number of orbits in each support-size stratum is
\[
\begin{array}{c|cccccc}
\text{number of nonzero edge coefficients}&1&2&3&4&5&6\\\hline
\text{number of orbits}&1&2&3&(q+3)/2&(q+1)/2&((q-1)^2+3(q-1)+2\gcd(3,q-1))/6.
\end{array}
\]
These are orbits of *embedded ideals under automorphisms of the fixed algebra*, not isomorphism types of the one-dimensional vector spaces underlying them. In particular, the odd-characteristic orbit count grows quadratically with field size while the even-characteristic count is two.

## Assumptions and scope
All automorphisms fix \(k\) pointwise. The algebra is **commutative**, with all individual generator squares and all degree-three monomials zero; mixed quadratic monomials \(x_ix_j\) for \(i\ne j\) survive. Let \(\mathfrak m=(x_1,x_2,x_3,x_4)A\), let \(V=\mathfrak m/\mathfrak m^2\), and write \(e_{ij}=x_ix_j\) for \(1\le i<j\le4\). The local algebra has dimension \(11\), its socle is \(S=\operatorname{Ann}(\mathfrak m)=\mathfrak m^2=\langle e_{12},e_{13},e_{14},e_{23},e_{24},e_{34}\rangle_k\), and its minimal nonzero ideals are precisely the one-dimensional \(k\)-subspaces of \(S\). Thus the total number of such ideals before quotienting by automorphisms is \((q^6-1)/(q-1)\).

## Proof
**1. Socle and the induced automorphism group.** Every element has unique form \(a+\sum_i b_i x_i+\sum_{i<j}c_{ij}e_{ij}\). Multiplication by all \(x_j\) vanishes only if \(a=0\) and all \(b_i=0\): the coefficient of \(e_{ij}\) in \(x_j\sum b_i x_i\) is \(b_i\). Hence \(S=\mathfrak m^2\). Every nonzero ideal contains a minimal nonzero ideal, and a nonzero minimal ideal lies in the socle; the latter is a vector space killed by \(\mathfrak m\), so its minimal ideals are exactly its lines.

An automorphism is determined modulo \(S\) by an invertible linear matrix \(M\in\operatorname{GL}(V)\); quadratic changes in the images of the generators do not alter the induced action on \(S\). Conversely, any invertible linear substitution respecting the square relations extends to an automorphism (the induced filtered map has invertible degree-one and degree-two pieces). In odd characteristic, squaring the \(i\)-th image produces coefficients \(2M_{ri}M_{si}\) of \(e_{rs}\) for \(r<s\). These must vanish, forcing each column of \(M\) to have exactly one nonzero entry; invertibility makes \(M\) monomial. Every monomial \(M\) does respect the relations. Thus the effective action on \(S\) is vertex permutation together with edge rescaling
\[
e_{ij}\longmapsto t_it_j e_{\sigma(i)\sigma(j)}.
\]
In characteristic two the square of every linear combination of the \(x_i\) is zero, so every \(M\in\operatorname{GL}_4(k)\) is allowed. Its action on \(S\) is the exterior-square representation \(\bigwedge^2 V\), because the coefficient of \(e_{rs}\) in the transformed \(e_{ij}\) is \(M_{ri}M_{sj}+M_{si}M_{rj}\), which equals the corresponding \(2\)-minor in characteristic two.

**2. Even characteristic.** The standard alternating-matrix reduction under change of basis decomposes every nonzero bivector in \(\bigwedge^2k^4\) into either one decomposable wedge or a sum of two wedges on independent planes. Equivalently the associated alternating matrix has rank \(2\) or \(4\). Both forms occur and are inequivalent; all forms of the same rank are equivalent over every field. Passing to projective lines does not split these classes, since scaling a representative does not change its rank. Hence exactly two orbits.

**3. Odd characteristic: graph support and small strata.** For a socle vector \(v=\sum_{i<j}c_{ij}e_{ij}\), associate the simple graph on vertices \(1,2,3,4\) with an edge \(ij\) exactly when \(c_{ij}\ne0\). Diagonal rescaling preserves its labeled edge set, and permutations change it only by relabeling. There are exactly \(1,2,3,2,1,1\) unlabeled nonempty graphs with respectively \(1,2,3,4,5,6\) edges. Every graph with at most three edges supports exactly one orbit of nonzero weights: a forest is normalized by choosing successive vertex factors; on a triangle the extra common projective scalar normalizes its third edge as well. Thus the first three support-size counts are \(1,2,3\).

**4. Odd characteristic: four and five edges.** The two four-edge graph types are a triangle with one pendant edge (the paw), and the four-cycle \(C_4\). The paw weights can all be normalized using vertex factors and the projective scalar, so it gives one orbit. For a four-cycle with cyclic edge weights \(a,b,c,d\), all nonzero, the ratio \(\rho=ac/(bd)\) is invariant under vertex rescaling and projective scalar multiplication. Two weighted four-cycles with the same ratio differ by such a rescaling, by solving along three consecutive edges and using the fourth as the compatibility condition. Dihedral graph automorphisms send \(\rho\) to either \(\rho\) or \(\rho^{-1}\), and both occur. Thus its orbit classes are \(k^\times/(\rho\sim\rho^{-1})\). Since \(q\) is odd, inversion has two fixed points \(\pm1\), giving \((q+1)/2\) classes. The only five-edge graph is \(K_4\) minus one edge; its four-cycle has the same ratio, and the fifth edge is freely normalized by the remaining rescaling freedom. Its graph automorphisms again realize inversion, so it contributes \((q+1)/2\) orbits. Consequently the four-edge stratum contributes \((q+3)/2\).

**5. Odd characteristic: full support and Burnside.** When all six \(c_{ij}\) are nonzero, set
\[
U=c_{12}c_{34},\qquad W=c_{13}c_{24},\qquad Z=c_{14}c_{23}.
\]
Every diagonal rescaling multiplies these three products by the same \(t_1t_2t_3t_4\), and projective scalar multiplication multiplies them by the same square. Conversely, if two full-support weight systems give the same projective triple \([U:W:Z]\), their edgewise ratios \(d_{ij}\) satisfy \(d_{12}d_{34}=d_{13}d_{24}=d_{14}d_{23}\); direct substitution, fixing a scale for vertex one, solves \(d_{ij}=s t_it_j\) for nonzero \(s,t_i\). Thus the diagonal-plus-projective orbits are precisely the projective triples \([U:W:Z]\) with all entries nonzero. Every such triple occurs.

The vertex-permutation group acts on the three perfect matchings of \(K_4\) through the full group \(S_3\). Put \(N=q-1\), so the projective torus has \(N^2\) points. Each of three transpositions fixes exactly \(N\) points, since it forces the exchanged coordinates to be equal. Each of the two three-cycles fixes \(h=\gcd(3,N)\) points, since a projective fixed triple is a geometric progression with ratio a third root of unity. Burnside's lemma therefore gives
\[
\frac{N^2+3N+2h}{6}
\]
full-support orbits. Summing six sparse-graph orbits, one paw orbit, the two inverse-ratio strata and the full-support stratum gives
\[
6+1+\frac{q+1}{2}+\frac{q+1}{2}+\frac{N^2+3N+2h}{6}
=\frac{q^2+7q+46+2h}{6}.
\]
This proves the asserted complete census in every characteristic.

## Verification
The supplied `check_orbits.py` constructs all projective lines of the six-dimensional socle, applies generating substitutions of the actual induced automorphism group, and computes orbit components by breadth-first search. It independently reproduced the predicted total and support-stratified counts for odd fields of orders \(3,5,7,11\), and the two rank orbits for even fields of orders \(2,4\). The numbers of projective lines independently covered were respectively \(364,3906,19608,177156\) in the four odd cases and \(63,1365\) in the even cases. Run `python check_orbits.py` for the default six cases, or import `orbit_census(11)` to replay the last. This finite computation is supplementary; the proof above handles every prime power.

## Relationship to prior work
Angeltveit–Gerhardt–Hill–Lindenstrauss (first posted June 1, 2012) study multivariable truncated polynomial algebras through algebraic \(K\)-theory, without automorphism orbits of minimal ideals. Herzog–Hibi (2013) study socles of powers of squarefree monomial ideals; the socle is background here, but their theorem is not an orbit census of the displayed cubic truncation. Díaz–Liendo–Manzano-Flores–Regeta (2024) classify automorphism groups of zero-dimensional monomial algebras in characteristic zero, and Díaz–Lucchini Arteche (2024) prove automorphism-group determination, again in characteristic zero; neither supplies the finite-field projective-socle orbit numbers.

Related quantitative classifications of automorphism groups of the **untruncated** square-zero-variable complete intersections and of ideals of the **two-variable unrestricted cubic truncation** give useful neighboring results. Their formulas and objects differ: the present object has four generators, kills all degree-three products, and classifies minimal-ideal orbits, not the automorphism group itself or the full ideal lattice of the two-generator symmetric cubic algebra. The induced group action is elementary and overlaps their structural conclusions; the new part is the full weighted-support orbit quotient, including the \(S_3\) projective triple and characteristic-sensitive count.

## Limitations
Only minimal nonzero ideals of this fixed eleven-dimensional algebra are classified, not all of its ideals, larger truncation degrees, or ideals up to abstract ring isomorphism. The zero ideal and the whole algebra are not included. The formula applies to ground-field-linear automorphisms, excluding arbitrary field semilinear maps. The preceding literature comparisons support but do not conclusively establish historical priority; related invariant-theoretic or weighted-graph orbit tables may contain equivalent counts. No independent mathematical audit has been performed.

## References
1. V. Angeltveit, T. Gerhardt, M. A. Hill, A. Lindenstrauss, *On the algebraic K-theory of truncated polynomial algebras in several variables*, arXiv:1206.0247 (first posted 2012-06-01), https://arxiv.org/abs/1206.0247 .
2. J. Herzog, T. Hibi, *Bounding the socles of powers of squarefree monomial ideals*, arXiv:1308.5400 (first posted 2013-08-25), https://arxiv.org/abs/1308.5400 .
3. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first posted 2024-08-05), https://arxiv.org/html/2408.02197v3 .
4. R. Díaz, G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first posted 2024-09-23), https://arxiv.org/abs/2409.15081 .
