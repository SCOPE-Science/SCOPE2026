# Complete rational Klein-four cohomology of the diamond graph nilmanifold

## Finding

For the canonical nine-dimensional Dani–Mainkar nilmanifold \(N(D)\) of the diamond graph \(D=K_4-e\), with its graph-automorphism group \(A\cong C_2\times C_2\), the following table is the **complete rational graded cohomology character**. Here \(h\) exchanges the two degree-three graph vertices, \(t\) exchanges the two degree-two vertices, and \((\epsilon_h,\epsilon_t)\) labels the four one-dimensional rational characters of \(A\). All entries in the four rightmost columns are the corresponding multiplicities in \(H^k(N(D);\mathbb Q)\).

| Degree | Identity | Hub exchange | Tip exchange | Both exchanges | (+,+) | (+,-) | (-,+) | (-,-) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| 1 | 4 | 2 | 2 | 0 | 2 | 1 | 1 | 0 |
| 2 | 17 | 1 | 3 | -1 | 5 | 4 | 5 | 3 |
| 3 | 39 | -3 | 1 | 3 | 10 | 8 | 10 | 11 |
| 4 | 49 | -3 | -1 | 3 | 12 | 11 | 12 | 14 |
| 5 | 49 | -3 | 1 | -3 | 11 | 12 | 14 | 12 |
| 6 | 39 | -3 | -1 | -3 | 8 | 10 | 11 | 10 |
| 7 | 17 | 1 | -3 | 1 | 4 | 5 | 3 | 5 |
| 8 | 4 | 2 | -2 | 0 | 1 | 2 | 0 | 1 |
| 9 | 1 | 1 | -1 | -1 | 0 | 1 | 0 | 0 |

In particular, the ordinary rational Betti vector in degrees \(0\) through \(9\) is
\[
(1,4,17,39,49,49,39,17,4,1),
\]
with total rank \(220\). The ordinary geometric quotient spaces by the hub exchange, the tip exchange, and the entire automorphism group have respective rational Betti vectors
\[
\begin{aligned}
N(D)/\langle h\\rangle &: (1,3,9,18,23,23,18,9,3,1),\\
N(D)/\langle t\\rangle &: (1,3,10,20,24,25,19,7,1,0),\\
N(D)/A &: (1,2,5,10,12,11,8,4,1,0).
\end{aligned}
\]
Their total ranks are respectively \(108\), \(110\), and \(54\). In particular, the two inequivalent graph-involution quotients already differ in degree-two rational Betti number, and their top rational cohomology groups have respective ranks \(1\) and \(0\).

## Assumptions and scope

The diamond graph has vertex set \(\{0,1,2,3\}\) and exactly five edges \(\{01,02,03,12,13\}\). Vertices \(0,1\) are the degree-three pair (hubs), and \(2,3\) the degree-two pair (tips). The associated rational two-step Lie algebra has basis \(x_0,x_1,x_2,x_3,z_{01},z_{02},z_{03},z_{12},z_{13}\), brackets \([x_i,x_j]=z_{ij}\) on increasing graph edges, and all other brackets zero, up to skew symmetry.

For a concrete graph-equivariant compact nilmanifold, use the simply connected group in exponential coordinates \((v,z)\in\mathbb R^4\times\mathbb R^5\), with multiplication
\[
(v,z)(v',z')=\bigl(v+v',z+z'+\tfrac12\omega(v,v')\bigr),\quad
\omega(v,v')_{ij}=v_iv'_j-v_jv'_i,
\]
where \(ij\) ranges over the five graph edges. The subgroup \(\Gamma=\mathbb Z^4\times\tfrac12\mathbb Z^5\) is a discrete cocompact lattice, closed under this group law and invariant under every graph automorphism. Define \(N(D)=\Gamma\backslash G\). The finite graph automorphisms act on this quotient, so the geometric quotients in the finding are well-defined. The cohomology assertions are with rational coefficients and concern graded vector spaces and representations, not cup products.

## Proof

**1. Explicit cochain model.** By the rational form of the Nomizu theorem for the chosen rational nilmanifold, with naturality for the graph automorphisms, rational cohomology is computed equivariantly by the Chevalley–Eilenberg differential graded algebra on dual degree-one generators \(x_i\) and \(z_{ij}\), with
\[
dx_i=0,\qquad dz_{ij}=x_i\wedge x_j
\quad(ij\in\{01,02,03,12,13\}).
\]
A global reversal of the sign convention for \(d\) gives the same cohomology representation. There are precisely \(\binom9k\) sorted exterior monomials in degree \(k\). The differential is the signed Leibniz derivation obtained by replacing a \(z_{ij}\) factor with \(x_i\wedge x_j\); terms with repeated generators are zero. The standalone exact-arithmetic program builds every one of these matrices and verifies \(d^2=0\).

**2. Exact differential ranks.** For degrees \(k=0,\ldots,8\), the ranks of \(d:C^k\to C^{k+1}\) over \(\mathbb Q\) are, in order,
\[
(0,5,14,31,46,31,14,5,0).
\]
The program computes these by exact rational row reduction on blocks indexed by the four-coordinate weight: a vertex generator contributes one unit at its vertex, and an edge generator contributes one unit at each endpoint. Replacement of an edge generator by its two endpoints preserves the weight; hence the matrix is the direct sum of the calculated blocks, with no omitted rows or columns. Since \(\dim C^k=\binom9k\), the cohomology dimensions are exactly the identity column of the table.

**3. Signed symmetry traces.** The automorphisms \(h=(01)\) and \(t=(23)\) act on vertex generators by permutation and on edge generators by signed edge relabeling, with a sign when the reoriented edge is reversed. The program constructs the resulting signed permutation matrices \(T_g^k\), verifies \((T_g^k)^2=I\) and \(dT_g^k=T_g^{k+1}d\), and determines the exact dimensions of the images of \(d\) on the plus and minus eigenspaces of every nonidentity \(g\in A\). The difference of those dimensions is the trace of \(g\) on the space of coboundaries. Since
\[
\operatorname{tr}(g\mid H^k)=
\operatorname{tr}(g\mid C^k)-
\operatorname{tr}(g\mid\operatorname{im}d_{k-1})-
\operatorname{tr}(g\mid\operatorname{im}d_k),
\]
the three nonidentity cohomology trace columns follow by the two exact sequences defining cohomology. The full chain and image trace sequences are recorded by the executable, not inferred from the final answer. Rational character orthogonality then yields the four nonnegative integer multiplicity columns:
\[
m_{\epsilon_h,\epsilon_t}(k)=\tfrac14\bigl(
\operatorname{tr}(1\mid H^k)+\epsilon_h\operatorname{tr}(h\mid H^k)
+\epsilon_t\operatorname{tr}(t\mid H^k)+\epsilon_h\epsilon_t\operatorname{tr}(ht\mid H^k)\bigr).
\]
This completes the finite, exhaustive cohomology-character calculation.

**4. Geometric quotient cohomology.** The action is finite and can be triangulated equivariantly. Averaging with rational coefficients identifies \(H^*(N(D)/B;\mathbb Q)\) with \(H^*(N(D);\mathbb Q)^B\) for any subgroup \(B\le A\), even when the action has fixed points. The plus-eigenspace and trivial-character columns therefore give the three quotient Betti vectors above. The top-degree distinction is consistent with the determinant of the respective actions on the nine-dimensional Lie algebra: \(h\) preserves orientation, while \(t\) reverses it.

## Verification

Run `python3 diamond.py` and `python3 diamond_quotients.py` in the same directory (requires Python 3 and SymPy). The first program constructs all \(512\) exterior monomials, verifies boundary-square-zero and symmetry commutation, then performs rational exact ranks and character inversion. The second program independently builds invariant orbit-sum cochains, computes their exact differentials without using the first program's character inversion, and recovers all three quotient Betti vectors and the cover. Their recorded standard outputs are embedded alongside the source programs. The two approaches agree in all ten cohomological degrees; the Euler characteristic is zero, the ordinary Betti vector is Poincaré-dual, and the three nonidentity character traces satisfy the orientation-twisted duality relations.

## Relationship to prior work

Aldi–Butler–Gardiner–Grandini–Lichtenwalner–Pan (arXiv:2402.14188, first public 2024) supply the decomposition by induced subgraphs, general low-degree formulas, and all-degree star-graph cases. Their Theorems 22 and 23 already cover generic ordinary Betti information in degrees two and three, and no novelty is asserted for those general formulas. Aldi–Bevins–Chatzitheodoridis–Da Silva–Frias–Mejía Gómez (arXiv:2611.17014v1, first public 12 November 2026) develop full Poincaré formulas for path-graph nilmanifolds. The diamond is neither a path, a star, nor a complete graph. The inspected works do not state its complete graded rational Klein-four character or the three quotient Betti vectors, nor do their numerical all-degree path/star formulas imply those character values. The general cochain construction makes the present finite calculation possible, but it is not itself a published table of this output.

## Limitations

The result concerns this specific four-vertex graph and the canonical graph-invariant lattice above. It does not classify all two-step nilmanifolds, determine integral torsion or cup products, or establish a recurrence under graph gluing. The exact finite computations prove the stated finite claims, not an infinite-family formula. The literature and publicly searchable-index comparison reduces but cannot eliminate the risk of an unindexed equivalent computation; independent scientific validation is not represented by these calculations.

## References

1. M. Aldi, S. Bevins, E. Chatzitheodoridis, S. Da Silva, Q. Frias and T. Mejía Gómez, *Poincaré polynomials of nilmanifolds associated with path graphs*, arXiv:2611.17014v1 (first public 12 November 2026). https://arxiv.org/html/2611.17014v1
2. M. Aldi, A. Butler, J. Gardiner, D. Grandini, M. Lichtenwalner and K. Pan, *On the cohomology of Lie algebras associated with graphs*, arXiv:2402.14188 (first public 22 February 2024). https://arxiv.org/html/2402.14188v3
3. K. Nomizu, *On the cohomology of compact homogeneous spaces of nilpotent Lie groups*, Annals of Mathematics **59** (1954), 531–538.
