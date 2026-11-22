# Three-torsion survives the affine quotient of the Paley-17 neighborhood complex

## Finding
Let \(P_{17}\) be the quadratic-residue Paley graph on \(\mathbb F_{17}\). Let \(X=\mathcal N(P_{17})\) be its *ordinary open* Lovász neighborhood complex, and let \(G=\mathbb F_{17}\rtimes (\mathbb F_{17}^{\times})^2\) be the order-\(136\) affine automorphism group. Put \(Y=|X|/G\) and \(R=\mathbb Z_{(3)}\), the localization of the integers at the prime three. Then
\[
\boxed{\widetilde H_j(Y;R)\cong\begin{cases}\mathbb Z/3\mathbb Z,&j=2,\\0,&j\ne2.\end{cases}}
\]
In particular the full affine quotient is **rationally acyclic** but **not contractible**. Moreover \(\widetilde H_2(Y;\mathbb F_3)\cong \widetilde H_3(Y;\mathbb F_3)\cong\mathbb F_3\), with all other reduced mod-three homology zero. This is a determination of the *three-primary* integral homology of the **ordinary topological quotient**, not a statement about Borel equivariant homology or the complete unlocalized integral homology.

## Assumptions and scope
The vertex set is \(\mathbb F_{17}=\{0,\ldots,16\}\). Its nonzero quadratic-residue set is \(Q=\{1,2,4,8,9,13,15,16\}\). Vertices are adjacent precisely when their difference belongs to \(Q\). A nonempty subset is a simplex of \(X\) if and only if it lies in one of the seventeen **open** neighborhoods \(a+Q\). Thus the seventeen maximal faces have eight vertices each. The affine group consists of \(x\mapsto a+qx\) with \(a\in\mathbb F_{17}\), \(q\in Q\). Its order \(136=17\cdot8\) is a unit in \(R\). All simplices are oriented by their ascending vertex order. The topological quotient \(Y\) is taken after geometric realization and may contain nonfree stabilizers; it is not treated as a naive abstract orbit simplicial complex.

## Proof
**Transfer and oriented orbit chains.** Since \(|G|\) is invertible in \(R\), averaging identifies \(H_*(X;R)_G\) with \(H_*(X;R)^G\). The map from the homotopy quotient to the ordinary quotient is an \(R\)-homology equivalence: over a point with stabilizer \(H\le G\), the homotopy-quotient fiber is \(BH\), whose positive-degree \(R\)-homology vanishes because \(|H|\) is invertible. Equivalently one can barycentrically subdivide to remove simplex inversions and compare cellular quotient chains. Consequently
\[
H_*(Y;R)\cong H_*(C_*(X;R)_G).
\]
In the oriented coinvariant chain group, an orbit of simplices with an orientation-reversing stabilizer becomes zero (because \(2\) is invertible in \(R\)); every other orbit contributes one free basis generator. For each surviving orbit, an oriented representative's simplicial boundary is projected to the signed representatives of the lower-dimensional surviving orbits.

**Finite enumeration.** Enumerating the nonempty subsets of the seventeen neighborhoods yields \(3468\) faces. In dimensions zero through seven, the face numbers are
\[
(17,136,612,1122,952,476,136,17).
\]
The surviving oriented-orbit basis sizes in the same dimensions are
\[
(1,0,4,9,7,3,1,0).
\]
The numbers of killed orientation-reversing orbits are \((0,2,1,1,0,1,0,1)\). For every orbit, all \(136\) affine images are explicitly examined; the verifier confirms that every face is accounted for and that the oriented projected boundary matrices satisfy \(\partial^2=0\) over the integers.

**Exact three-primary boundary calculation.** The chain groups \(C_j(Y;R)\) in degrees zero through seven have the above free ranks. Number \(B_k\) as the boundary from faces of size \(k\) to size \(k-1\) in the orbit complex. Their ranks over \(\mathbb F_3\), for \(k=2,\ldots,8\), are
\[
(0,0,3,5,2,1,0).
\]
The only nontrivial torsion-producing differential is the \(4\)-by-\(9\) matrix \(B_4:C_3\to C_2\):
\[
B_4=\begin{pmatrix}
-2&-1&0&-2&-1&-1&-2&0&0\\
2&0&0&-1&1&-1&0&-1&0\\
0&1&1&0&-1&-1&0&0&-1\\
0&-1&1&0&-1&1&2&-2&-1
\end{pmatrix}.
\]
The minor on its first four columns is \(12\). Since its reduction modulo three has rank three, exactly one Smith invariant is divisible by three. The minor \(12\) has three-adic valuation one, so that invariant is divisible by precisely one power of three. Therefore \(\operatorname{coker}(B_4)\otimes R\cong\mathbb Z/3\mathbb Z\).

The other nonzero differentials have three-local ranks \(5,2,1\) in succession, by the displayed modular ranks. Their ranks over \(\mathbb Q\) are at least these, while the chain identities \(\partial^2=0\) and free chain-group dimensions bound them by these same numbers. Because their ranks do not drop modulo three, their images are three-saturated. Thus all higher reduced homology vanishes over \(R\). The only zero-dimensional generator has no incoming or outgoing degree-one boundary, making the space connected. This proves the stated reduced homology. The displayed ranks also show that all reduced rational homology vanishes, and the universal coefficient theorem gives precisely the two indicated mod-three homology classes.

**Independent rational check.** Counting signed fixed simplices in all \(136\) affine automorphisms, and using the previously established fact that rational homology of \(X\) is concentrated in degree three of rank \(35\), gives homological traces \(35\) at the identity, \(1\) on each nonzero translation, \(-1\) on an affine element with multiplier other than \(\pm1\), and \(3\) on the affine elements with multiplier \(-1\). Their group average is zero, independently confirming rational acyclicity of the quotient. This check is supplementary: the three-primary quotient claim is established by the explicit orbit-chain boundary calculations, not by rational traces.

## Verification
Run `python3 verify_affine_quotient.py`; no third-party packages are required. The verifier constructs all \(3468\) faces, verifies all \(136\) affine symmetries, determines each oriented simplex orbit and stabilizer, reconstructs every quotient differential, checks every consecutive composition vanishes integrally, computes all required ranks modulo three, checks the entire displayed \(4\)-by-\(9\) matrix and its determinant-\(12\) minor, and independently computes the signed Lefschetz traces. `verification_output.txt` is the unmodified standard output of a successful execution of that exact program. The calculation is exhaustive for this finite complex; the algebraic argument above explains why it determines homology rather than merely finite sample statistics.

## Relationship to prior work
A previously available exact computation, *Three-torsion in the neighborhood complex of the Paley graph of order seventeen* (2026), determines the **nonequivariant** homotopy type \(X\simeq M(\mathbb Z/3,2)\vee\bigvee^{35}S^3\). That result is not claimed anew here; it does not determine the induced action on integral torsion or the topology of \(Y\). The present theorem specifically asks what remains after dividing by all affine graph automorphisms and identifies one three-primary quotient class in spite of vanishing rational homology. Kahle's paper introduces and analyzes the open neighborhood complex of random graphs, not this deterministic symmetry quotient. Matsushita's results concern graph fundamental groups and associated neighborhood complexes, not this exact quotient homology. Hughes's 2014 dissertation analyzes Cayley-graph neighborhood-complex representations, usually for the **closed** distance set \(\{0,1\}\); its inspected main results and appendices do not state the Paley-17 open-neighborhood quotient calculation. The complete text of the prior exact Paley-17 result and the relevant published primary works were checked for the exact object and mathematical implication, not just for title matches.

## Limitations
The calculation determines homology only with coefficients localized at three and the complete rational homology of the ordinary quotient. It does **not** determine possible integral torsion at primes two or seventeen, the integral homotopy type, the fundamental group of the quotient, or Borel equivariant cohomology. The previously known homotopy decomposition of \(X\) alone does not prove this quotient theorem, because finite group actions on a fixed homotopy type can have different quotient homology. An equivalent, unindexed published computation remains a publication-priority risk; no definitive priority claim is made. No independent external mathematical audit is asserted.

## References
1. M. Kahle, *The Neighborhood Complex of a Random Graph*, arXiv:math/0512077 (first public 2005-12-04), https://arxiv.org/abs/math/0512077 .
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first public 2012-10-10), https://arxiv.org/abs/1210.2803 .
3. J. Hughes, *Group Action on Neighborhood Complexes of Cayley Graphs*, Colorado State University dissertation (2014), https://doi.org/10.25675/3.019758 .
4. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, public exact research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
5. DistanceRegular.org, *Paley graph P17*, graph parameters and full automorphism-group order, https://www.math.mun.ca/distanceregular/graphs/paley17.html .
