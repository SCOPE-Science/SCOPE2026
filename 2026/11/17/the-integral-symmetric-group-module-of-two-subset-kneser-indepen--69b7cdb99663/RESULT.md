# The integral symmetric-group module of two-subset Kneser independence homology

## Finding

For every integer \(n\ge4\), let \(G_n=\mathrm{KG}(n,2)\) be the Kneser graph with vertices the two-element subsets of \([n]=\{1,\dots,n\}\), adjacent when disjoint. Write \(X_n=\operatorname{Ind}(G_n)\) for its ordinary simplicial independence complex and \(T_n=\operatorname{sk}_2\Delta^{n-1}\) for the full two-skeleton of the simplex on \([n]\). Both carry their natural \(S_n\)-action by relabeling.

**Theorem.** There is an explicit \(S_n\)-equivariant simplicial map
\[
 f_n:\operatorname{sd}X_n\longrightarrow\operatorname{sd}T_n
\]
whose geometric realization is an ordinary homotopy equivalence (equivariance of the map is asserted, but a homotopy inverse equivariant for every subgroup is not claimed). In particular there is a canonical isomorphism of integral \(\mathbb Z[S_n]\)-modules
\[
 \widetilde H_2(X_n;\mathbb Z)\cong\bigwedge^3 W_n,\qquad
 W_n=\left\{(a_1,\dots,a_n)\in\mathbb Z^n:\sum_i a_i=0\right\}.
\]
All other reduced integral homology groups vanish. Over \(\mathbb Q\), this is the single irreducible hook Specht representation \(S^{(n-3,1,1,1)}\), of dimension \(\binom{n-1}{3}\). For a permutation with \(c_d\) cycles of length \(d\), the complete character is
\[
 \chi_n(g)=[t^3]\frac{\prod_{d\ge1}(1-(-t)^d)^{c_d}}{1+t}.
\]

For any partition of \([n]\) into \(r\) nonempty labeled blocks of sizes \(m_1,\dots,m_r\), let \(H= S_{m_1}\times\cdots\times S_{m_r}\le S_n\) relabel within each block. The **ordinary topological orbit space** has
\[
 \dim_{\mathbb Q}\widetilde H_2(|X_n|/H;\mathbb Q)
   =\binom{r-1}{3},
\]
interpreting the binomial coefficient as zero if \(r\le3\), and no other nonzero reduced rational homology. Its rational cohomology ring is the ring of a wedge of \(\binom{r-1}{3}\) two-spheres: all positive-degree products vanish. Thus all such quotients with at most three blocks are rationally acyclic; four blocks is the sharp threshold for nonzero reduced rational homology, independently of the block sizes.

## Assumptions and scope

The graph has all two-subsets as vertices, without the cyclic stability restriction defining a Schrijver graph. Simplicial faces are nonempty pairwise-intersecting families of two-subsets. The theorem concerns each \(n\ge4\) and only the natural relabeling action. An ordinary homotopy equivalence between \(X_n\) and \(T_n\) is not the assertion that their orbit spaces are homotopy equivalent, and the orbit-space calculation uses rational coefficients specifically.

A vertex of \(\operatorname{sd}X_n\) is a nonempty face \(F\) of \(X_n\), and a vertex of \(\operatorname{sd}T_n\) is a nonempty subset \(J\subset[n]\) of cardinality at most three. Define its image \(\phi(F)\) by
\[
 \phi(F)=\begin{cases}
 e,&F=\{e\},\quad e\in\binom{[n]}2,\\
 \bigcap_{e\in F}e,&|F|\ge2\text{ and this intersection is nonempty},\\
 \bigcup_{e\in F}e,&\bigcap_{e\in F}e=\varnothing.
 \end{cases}
\]
The second case is a singleton; the final case is the three-point set of a triangular edge family.

## Proof

**1. Classification of faces and the canonical simplicial map.** If two different two-subsets meet, write them \(\{a,b\}\) and \(\{a,c\}\). Every further two-subset meeting both either contains \(a\) or equals \(\{b,c\}\). Once \(\{b,c\}\) is present, no fourth distinct two-subset meets all three. Thus every face \(F\) is contained in a star simplex
\[
 \sigma_a=\big\{\{a,b\}:b\in[n],\ b\ne a\big\}
\]
or is precisely the exceptional triangle \(\tau_{abc}=\{\{a,b\},\{a,c\},\{b,c\}\}\). Distinct stars meet in the single vertex \(\{a,b\}\), while no three stars meet. Every edge of any exceptional triangle lies in a unique star.

For any inclusion of nonempty faces \(F\subseteq F'\), the two labels \(\phi(F)\), \(\phi(F')\) are comparable by inclusion. Indeed, within a star only the images \(\{a,b\}\supset\{a\}\) can occur, and on a triangle the possible labels are \(\{a,b\}\supset\{a\}\subset\{a,b,c\}\), with all three nested as sets. More generally, each totally ordered chain of faces has pairwise comparable images. Hence the vertex map \(F\mapsto\phi(F)\) defines a simplicial map between barycentric subdivisions. Its construction commutes with every relabeling in \(S_n\).

**2. Homotopy equivalence on the star union.** Set \(Y=\bigcup_{a=1}^n\sigma_a\). Let \(p_{ab}=\{a,b\}\) be the shared vertex of \(\sigma_a\) and \(\sigma_b\). Inside each \(\sigma_a\) join its barycenter \(c_a\) to all \(p_{ab}\). The resulting embedded graph \(B\subset Y\) has vertices \(c_a,p_{ab}\) and edges \(c_a p_{ab},c_b p_{ab}\), so is the barycentric subdivision of the complete graph on \([n]\). Within each star simplex the embedded spanning tree is contractible, and its inclusion is a cofibration and a homotopy equivalence; thus the simplex strongly deformation retracts onto that tree. The homotopies can be chosen to fix all its leaves \(p_{ab}\), and so glue across the pairwise intersections. This gives an ordinary homotopy equivalence \(B\hookrightarrow Y\). On \(B\), \(f_n\) takes \(c_a\) to the vertex \(a\) and \(p_{ab}\) to the barycenter of edge \(ab\) in \(T_n\). Each segment is mapped into the corresponding half-edge with the correct endpoints, hence \(f_n|_B\) is homotopic to the evident homeomorphism \(B\to\operatorname{sd}(T_n^{(1)})\). Thus \(f_n|_Y:Y\to T_n^{(1)}\) is a homotopy equivalence.

**3. Extension over the exceptional triangles.** The complex \(X_n\) is obtained from \(Y\) by attaching exactly one closed two-simplex \(\tau_{abc}\) for every three-element set \(\{a,b,c\}\). Its boundary lies in \(Y\). On the barycentric subdivision of this triangle, the three original vertices map to the three edge barycenters of target triangle \(abc\); the three edge barycenters map to its three vertices; and the central barycenter maps to the central barycenter. The six small triangular flags map bijectively and linearly to the six flags of the target triangle. This is a piecewise-linear homeomorphism \(|\tau_{abc}|\to|abc|\), compatible with the boundary map. The cellular gluing theorem, applied one cell at a time to the map of pairs \((X_n,Y)\to(T_n,T_n^{(1)})\), proves that \(|f_n|\) is a homotopy equivalence.

**4. Integral module and character.** Let \(A=\mathbb Z^n\) with basis \(e_1,\dots,e_n\), and let \(\varepsilon:A\to\mathbb Z\) send each basis vector to one. The augmented simplicial boundary for the full simplex is exterior contraction \(\iota_\varepsilon\). As \(T_n\) has all faces of dimensions at most two, its top reduced homology is
\[
 \ker\left(\iota_\varepsilon:\bigwedge^3A\to\bigwedge^2A\right).
\]
The integral splitting \(A=W_n\oplus\mathbb Z e_n\) shows that the contraction kills \(\bigwedge^3 W_n\) and maps \(e_n\wedge\bigwedge^2W_n\) isomorphically (up to orientation sign) onto \(\bigwedge^2W_n\). The kernel is exactly \(\bigwedge^3W_n\), and the identification is \(S_n\)-natural since it is the kernel of the natural contraction. Since \(T_n\) is the full two-skeleton, it is simply connected, has no positive reduced homology outside degree two, and its integral top rank is \(\binom{n-1}{3}\). Under \(f_n\), the induced homology isomorphism respects the \(S_n\)-action. Over \(\mathbb Q\), the third exterior power of the standard representation is the irreducible hook Specht module \(S^{(n-3,1,1,1)}\). Since \(A_\mathbb Q\cong W_{n,\mathbb Q}\oplus\mathbf1\), the determinant identity \(\det(I+t g|_A)=\prod_d(1-(-t)^d)^{c_d}\) yields the stated character coefficient.

**5. Young-subgroup quotients.** For \(H=\prod_{i=1}^rS_{m_i}\), over \(\mathbb Q\) the restriction of \(W_n\) decomposes as a trivial \((r-1)\)-dimensional summand of block-constant vectors of total sum zero, plus the \(r\) within-block standard representations \(V_i\) (zero for singleton blocks). Each \(\bigwedge^j V_i\) has no \(S_{m_i}\)-fixed vectors for \(1\le j\le3\), as follows from the nontrivial hook representations (or directly from their alternating permutation realization). Hence the \(H\)-fixed part of \(\bigwedge^3W_{n,\mathbb Q}\) is exactly the third exterior power of the block-constant summand, of dimension \(\binom{r-1}{3}\). For a finite group acting on a finite triangulable space, rational cohomology of the ordinary quotient is the invariant rational cohomology of the space (after barycentric subdivision to remove inversions). This gives the asserted quotient Betti numbers. The cohomology ring has zero products in positive degrees because only degree two can be positive.

## Verification

The standalone standard-library program `checks/kneser_equivariant_check.py` reconstructs every face for \(n=4,5,6,7\), checks the face map on every comparable face pair, and confirms all six flags are mapped bijectively for every exceptional triangle. It checks the face-map equivariance for every permutation for \(n=4,5,6\), and for representatives of every conjugacy class for \(n=7\). Signed fixed-simplex Lefschetz traces agree with the exterior-power character in every conjugacy class of \(S_n\) for these four values. Reduced homology ranks are independently computed modulo \(2,3,101\) for \(n=4,5,6\). Every Young subgroup from every ordered composition of \(n\) into blocks is checked for \(n=4,5,6\) by exact character averaging. These tests corroborate the proof; the arbitrary-\(n\) statement rests on the structural argument, not a finite extrapolation.

Run `python checks/kneser_equivariant_check.py` and compare the output to `checks/kneser_equivariant_check.out`. The concluding success line is `KNESER_TWO_SUBSET_EQUIVARIANT_CHECK_PASS`.

## Relationship to prior work

Barmak's *Star clusters in independence complexes of graphs* (first public arXiv version 2 July 2010), Theorem 4.11, proves the **nonequivariant** wedge of \(\binom{n-1}{3}\) two-spheres for \(X_n\) (his notation takes \(n=k+4\)). That sphere count and the ordinary homotopy type are expressly not new here; the proof in that paper singles out a distinguished ground element and does not determine the integral \(S_n\)-action or a relabeling-equivariant map to the full simplex skeleton.

Braun's *Independence complexes of stable Kneser graphs* (arXiv 0912.0720, first public 3 December 2009) treats the proper stable-vertex induced subgraphs \(SG_{2,k}\) and their ordinary homotopy types; its main complexes and symmetry are different. Feng and Wang's *Exploring homological properties of independent complexes of Kneser graphs* (arXiv 2404.10566, first public 16 April 2024) acknowledges Barmak's two-subset case and studies higher subset size \(\ge3\), not this integral equivariant refinement. Schultz's 2010 paper concerns the equivariant topology of **stable** Kneser **Hom/box complexes**, rather than the ordinary independence complex of the complete two-subset Kneser graph. No inspected source states or logically entails the natural \(S_n\)-module identification and all Young-subgroup quotient dimensions together.

## Limitations

The assertion is an \(S_n\)-equivariant *map* that is an ordinary homotopy equivalence, not a claim of equivariant homotopy equivalence on all subgroup fixed-point spaces. Only **rational cohomology** of Young-subgroup orbit spaces is determined; integral orbit-space torsion and orbit-space homotopy types are not claimed. The family is restricted to two-element Kneser vertices, and does not cover higher subset sizes or stable Kneser graphs. No publication-priority claim can exclude every unindexed mathematical source, and no independent audit of this proof is represented.

## References

1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2 July 2010), Theorem 4.11. https://arxiv.org/pdf/1007.0418
2. B. Braun, *Independence complexes of stable Kneser graphs*, arXiv:0912.0720v1 (3 December 2009), Theorem 1.4. https://arxiv.org/pdf/0912.0720
3. Z. Feng and G. Wang, *Exploring homological properties of independent complexes of Kneser graphs*, arXiv:2404.10566v1 (16 April 2024), Introduction. https://arxiv.org/pdf/2404.10566
4. C. Schultz, *The equivariant topology of stable Kneser graphs*, arXiv:1003.5688v1 (29 March 2010). https://arxiv.org/abs/1003.5688
