# Integral critical group of the Wiman quintuple-point incidence graph

## Finding
Let \(\mathcal W\) be the classical Wiman configuration of \(45\) complex projective lines. Among its singularities are \(36\) points of multiplicity five. Let \(\Gamma_5\) be the bipartite graph whose vertices are these \(45\) lines and \(36\) quintuple points, with an edge for each geometric incidence. Then \(\Gamma_5\) is a connected graph with \(81\) vertices and \(180\) edges. Its finite graph Jacobian (critical group) is
\[
K(\Gamma_5)\cong
(\mathbb Z/2\mathbb Z)^8\oplus
(\mathbb Z/4\mathbb Z)^3\oplus
\mathbb Z/20\mathbb Z\oplus
(\mathbb Z/60\mathbb Z)^8\oplus
(\mathbb Z/1800\mathbb Z)^8.
\]
Its exponent is \(1800\), and it has precisely
\[
\tau(\Gamma_5)=2^{56}3^{24}5^{25}
\]
spanning trees. In particular, this is a complete *integral* graph-divisor invariant, not merely a rational-spectrum calculation.

## Assumptions and scope
The configuration is over \(\mathbb C\), with its standard faithful projective \(A_6\)-action. This result uses *only* the quintuple-point stratum, not the other \(45\) quadruple or \(120\) triple points. For any connected finite graph \(\Gamma\), define \(K(\Gamma)\) as the torsion subgroup of the cokernel of its integer vertex Laplacian; equivalently, as the cokernel of any reduced Laplacian obtained by deleting one row and matching column. This is the critical group of the incidence graph, **not** the Picard group of the Wiman sextic or of a blowup of the plane.

## Proof
**Geometric identification.** The established Wiman geometry has \(45\) lines, one for each nonidentity involution of the projective \(A_6\)-action, and one orbit of \(36\) quintuple points whose point stabilizers are dihedral of order ten. An involution fixes its associated line pointwise. The subgroups of order five in \(A_6\) number \(36\); each has dihedral normalizer of order ten. Each quintuple point is therefore represented uniquely by such a subgroup \(H\), using its dihedral stabilizer. The five involutions in that normalizer have their reflection axes through the fixed point: the action of the point stabilizer on the five incident lines is faithful, so no stabilizing involution can act trivially on the line pencil. These five axes exhaust the five lines through the point. Thus the incidence relation is exactly
\[
 t\sim H\quad\Longleftrightarrow\quad tHt^{-1}=H,
\]
where \(t\) ranges over the \(45\) involutions of \(A_6\) and \(H\) ranges over its \(36\) cyclic subgroups of order five. These involutions are precisely the double transpositions in the six-letter permutation model. For any generator \(h\) of \(H\), the incidence test is equivalent to \(tht=h^{-1}\).

**Spectrum and spanning trees.** Enumerating these finite permutation sets gives an integer incidence matrix \(B\) of size \(45\) by \(36\), with four ones per row and five ones per column. The integer matrix \(N=BB^{\mathsf T}\) has diagonal \(4\); among its \(990\) unordered off-diagonal pairs, \(360\) are \(1\) and \(630\) are \(0\). Direct integer multiplication establishes
\[
 N(N-5I)(N-8I)(N-20I)=0.
\]
The incidence graph is connected. Hence \(20\) is a simple eigenvalue of \(N\), and its traces \(\operatorname{tr}N=180\) and \(\operatorname{tr}(N^2)=1440\) give the exact spectrum
\[
 \operatorname{Spec}(N)=\{20^{[1]},8^{[10]},5^{[16]},0^{[18]}\}.
\]
The vertex Laplacian is \(L=\left(\begin{smallmatrix}4I&-B\\-B^{\mathsf T}&5I\end{smallmatrix}\right)\). For each positive eigenvalue \(s\) of \(N\), the associated Laplacian eigenvalues solve \(\lambda^2-9\lambda+20-s=0\); the remaining eigenvalues are \(4\) with multiplicity \(18\) and \(5\) with multiplicity \(9\). The matrix-tree theorem therefore gives
\[
 \tau(\Gamma_5)=\frac{9\,12^{10}15^{16}4^{18}5^9}{81}
 =2^{56}3^{24}5^{25}.
\]

**Integral Smith invariants.** Form an \(80\)-by-\(80\) reduced integer Laplacian \(R\). For each prime \(p\) dividing the displayed tree count, work over \(\mathbb Z/p^E\mathbb Z\) with \(E>v_p(\det R)\). Split every unit pivot by reversible row and column operations; when the residual matrix has no unit entry, divide all its entries by \(p\) and increment the accumulated Smith valuation. This yields the following complete local exponent multisets (including zero exponents):

| Prime | Local Smith exponent multiplicities |
|---|---|
| \(2\) | \(0^{[52]},1^{[8]},2^{[12]},3^{[8]}\) |
| \(3\) | \(0^{[64]},1^{[8]},2^{[8]}\) |
| \(5\) | \(0^{[63]},1^{[9]},2^{[8]}\) |

Since no other prime divides \(\det R=\tau(\Gamma_5)\), the corresponding sorted primary factors multiply into the Smith diagonal
\[
1^{[52]},\quad 2^{[8]},\quad4^{[3]},\quad20,\quad60^{[8]},\quad1800^{[8]}.
\]
The nonunit entries produce the claimed finite abelian group. Their product independently equals the matrix-tree count. The complete algorithm is supplied in `wiman_quintuple_critical_verify.py`.

## Verification
Run `python3 wiman_quintuple_critical_verify.py` with Python 3.8 or later. It uses the standard library only. It enumerates all \(360\) even permutations on six letters, reconstructs both incidence tests independently (inverting generators and normalizing subgroups), checks connectedness and the integer polynomial identity for \(BB^{\mathsf T}\), and computes local Smith factors for two *different* choices of sink. The exact output is `WIMAN_QUINTUPLE_LEVI_CRITICAL_GROUP_OK`. The arithmetic is integer and modular, not floating point. The modular precision exceeds each known determinant valuation, so the calculation detects every invariant factor and no hidden larger elementary divisor remains.

## Relationship to prior work
Wiman's line arrangement and its \(36\) quintuple-point incidence stratum are classical. Bauer–Di Rocco–Harbourne–Huizenga–Lundman–Pokora–Szemberg (arXiv:1407.2966, §4.2, public July 10, 2014) enumerate the singularity types and confirm four quintuple points on each line. Bauer–Di Rocco–Harbourne–Huizenga–Seceleanu–Szemberg (arXiv:1609.08648, §2.3, public September 27, 2016) identify the projective \(A_6\)-action and the dihedral stabilizers. The graph itself follows from these classical descriptions. The new assertion is its exact integral critical-group decomposition, not the incidence counts, symmetry group, or general graph-Jacobian definition. Published research on critical groups of line graphs or strongly regular graphs does not immediately imply this value for the bipartite \((4,5)\)-biregular Levi graph.

## Limitations
This establishes no independently reviewed historical priority. The identified sources were checked for the same specific group calculation, but older specialist tables or differently named isomorphic incidence graphs may contain an equivalent value. The result makes no claim about the full \(201\)-point Wiman incidence graph, finite-field reductions, or divisor-class groups of the ambient algebraic surface. An integer verifier checks a specified finite matrix and is complemented here by the geometrical identification and matrix-tree argument; it is not an external proof certificate.

## References
1. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Lundman, P. Pokora, T. Szemberg, *Bounded Negativity and Arrangements of Lines*, arXiv:1407.2966, first posted 2014-07-10, especially §4.2. https://arxiv.org/abs/1407.2966
2. T. Bauer, S. Di Rocco, B. Harbourne, J. Huizenga, A. Seceleanu, T. Szemberg, *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, arXiv:1609.08648, first posted 2016-09-27, especially §2.3. https://arxiv.org/abs/1609.08648
3. A. Berget, A. Manion, M. Maxwell, A. Potechin, V. Reiner, *The Critical Group of a Line Graph*, Annals of Combinatorics 16 (2012), 449–488, DOI:10.1007/s00026-012-0141-x (a different graph class).
