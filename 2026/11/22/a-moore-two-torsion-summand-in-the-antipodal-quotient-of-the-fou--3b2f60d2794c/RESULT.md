# A Moore two-torsion summand in the antipodal quotient of the four-cube independence complex

## Finding
Let \(Q_4\) be the graph on the sixteen binary four-vectors, with edges at Hamming distance one, and let \(K=\operatorname{Ind}(Q_4)\). Bitwise complementation \(a(v)=v+(1,1,1,1)\) induces an involution of \(K\). The **ordinary geometric orbit space** satisfies
\[
\boxed{|K|/\langle a\rangle\simeq M(\mathbb Z/2\mathbb Z,2)\vee\bigvee^3 S^3.}
\]
Here \(M(\mathbb Z/2\mathbb Z,2)\) is the simply connected Moore space obtained by attaching a three-cell to \(S^2\) by a map of degree two. Equivalently the orbit space has trivial fundamental group, reduced integral homology \(\mathbb Z/2\mathbb Z\) in degree two, \(\mathbb Z^3\) in degree three and zero in all other degrees. The torsion cannot be detected by the known rational character of the original complex.

## Assumptions and scope
The cube is the simple graph on integers \(0,\ldots,15\), where two integers are adjacent exactly when their bitwise XOR has one set bit. A simplex is a set of pairwise nonadjacent cube vertices. The involution sends a vertex \(v\) to \(v\mathbin{\mathrm{XOR}}15\); the quotient is of the full geometric realization, not the independence complex of a quotient graph, and is not a Borel homotopy quotient. All assertions concern this one sixteen-vertex graph and this single involution. The group action is not free: its geometric fixed-point set consists of two disjoint three-simplices, from the four antipodal vertex pairs in each parity class.

## Proof
**1. The finite complex and fixed locus.** Exhaustive independent-set enumeration gives exactly 742 nonempty simplices, with ordinary face vector \((16,88,208,228,128,56,16,2)\) in dimensions zero to seven. There are precisely 30 setwise invariant nonempty faces: eight of cardinality two, twelve of cardinality four, eight of cardinality six and two of cardinality eight. Every invariant independent face is a union of antipodal pairs all of the same Hamming parity. Consequently the fixed-point set in the geometric realization is the disjoint union of the two complete simplices on four pair-orbits.

**2. A correct geometric quotient cell structure.** To avoid treating a simplex with exchanged vertices as an ordinary simplicial quotient, perform a stellar subdivision of every invariant face in decreasing order of its cardinality. Introduce a new fixed vertex at each subdivision barycenter. The resulting simplicial complex has 24,530 nonempty simplices and an involution without inverted simplices. Its nonempty simplex orbits form a quotient \(\Delta\)-complex with 12,414 cells and dimension-by-dimension vector
\[
(38,260,960,2268,3480,3296,1728,384).
\]
Each oriented orbit cell is represented by the lexicographically smaller bitmask of its two possible simplices. Its signed boundary is computed by deleting one vertex, taking the orbit representative of that face and incorporating the sign of the permutation needed to return to sorted vertex order. The standalone verifier checks every boundary composition is zero over the integers.

**3. Genuine collapses and integral boundary normal form.** A cell is topologically free when it occurs **exactly once** in the attaching boundary of its unique higher-dimensional incident cell; the checker tests occurrence multiplicities, not merely a unit coefficient in a matrix. Exactly 6,100 such elementary cell-pair collapses reduce the quotient to a three-dimensional CW subcomplex with face vector \((10,48,96,60)\). Its signed integer boundary maps still compose to zero. Independently verified ranks of its boundaries in degrees one, two and three are \((9,39,56)\) over \(\mathbb F_2\) and \((9,39,57)\) over both \(\mathbb F_3\) and \(\mathbb F_5\).

Applying 104 exact **unit-pivot chain contractions** over \(\mathbb Z\), with full integer updates to neighboring boundary columns, leaves one degree-zero generator, one degree-two generator and four degree-three generators. The sole nonzero boundary is, after ordering the remaining generators,
\[
\partial_3:\mathbb Z^4\longrightarrow\mathbb Z,
\qquad \partial_3=(2\ \ 2\ \ 0\ \ 0).
\]
Its integral Smith invariant is exactly two. These chain contractions establish integral **homology**, not a topological collapse or a homotopy equivalence by themselves. Therefore \(\widetilde H_2\cong\mathbb Z/2\mathbb Z\) and \(\widetilde H_3\cong\mathbb Z^3\), and there are no other reduced integral homology groups. The result also agrees with the independent Euler identity \(\chi(|K|/C_2)=(\chi(|K|)+\chi(|K|^{C_2}))/2=(-6+2)/2=-2\).

**4. Fundamental group and homotopy type.** Independently of the quotient chain calculation, the original complex has 16 vertices, 88 edges and 208 triangles. A spanning tree leaves 73 edge generators for its fundamental-group presentation. The triangular relators eliminate all 73 generators through 73 explicit Tietze substitutions, each justified by a relator in which the eliminated generator occurs exactly once. The verifier confirms no generators or nontrivial relators remain. Thus \(\pi_1(|K|)=1\). Since the nontrivial involution fixes barycenters of antipodal edges, Armstrong's orbit-space theorem gives \(\pi_1(|K|/C_2)=1\).

The already established topological collapse produces a finite three-dimensional CW model. Attaching three-cells cannot change the fundamental group, so its two-skeleton is simply connected. A simply connected two-dimensional CW complex is homotopy equivalent to a wedge of two-spheres; the attaching maps of three-cells are then classified, via \(\pi_2\cong H_2\), by an integer matrix up to integral changes of cellular bases. Smith normal form together with the computed integral homology reduces these attachments to one degree-two map and three null maps. The CW model is thus homotopy equivalent to the Moore space and three three-spheres asserted above.

## Verification
Run `python3 verify.py` with Python 3.10 or newer. Only the Python standard library is required; no precomputed tables, network calls or other files are needed. The script reconstructs the complete sixteen-vertex complex, all invariant simplices, every stellar subdivision, every quotient cell, all signed integer boundaries, 6,100 verified topological collapses, modular ranks, 104 exact integral chain contractions and a full 73-generator fundamental-group presentation reduction. Expected terminal message: `Q4_ANTIPODAL_INTEGRAL_QUOTIENT_VERIFIED`. The file `verification_output.txt` preserves the observed output from running the included script. These are exhaustive checks of this finite object; no infinite-family inference is made.

## Relationship to prior work
Bousquet-Mélou, Linusson and Nevo [1] study open and cylindrical square-grid independence complexes and discuss toric grids; the four-by-four fully periodic grid is graph-isomorphic to \(Q_4\). Conant and Thistlethwaite [2] analyze cubical theta complexes, their Alexander-dual relationship to graph independence complexes, and group actions on quotient **hypergraphs**. Neither publication determines the integral homology or homotopy type of this particular **geometric quotient**. Engström [3] develops graph independence methods; Armstrong [4] supplies the orbit fundamental-group theorem used here.

Two later computations of the **unquotiented** sixteen-vertex complex determine its integral top-homology symmetry module [5] and complete rational group character [6]. They imply that the antipodal-invariant rational third-homology rank is three. However a character or an action on the upstairs integral homology lattice is not itself a computation of the geometric orbit's degree-two integral torsion or three-cell attaching maps; the action has nonempty fixed locus and cannot be treated as a free covering. A separate study [7] determines the antipodal quotient of the **distance-two Vietoris–Rips complex** of the same vertex set. Its allowed faces differ: it forbids antipodal pairs, whereas antipodal pairs occur in \(K\). Its free action and projective-space conclusion therefore do not cover this claim.

## Limitations
The result covers only ordinary integral homotopy type of the four-cube independence complex's bit-complement quotient. It does not claim a general formula for higher cubes, any other symmetry subgroup, or an equivariant homotopy decomposition upstairs. The exact integer calculation relies on a fully enumerated finite chain complex and is reproducible using the supplied checker, but has not undergone independent mathematical audit. The literature comparison cannot exclude every unindexed equivalent result.

## References
[1] M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public January 30, 2007, https://arxiv.org/abs/math/0701890.

[2] J. Conant and O. Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739, first public August 5, 2008, https://arxiv.org/abs/0808.0739 (especially §§2 and 6–7).

[3] A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148, first public August 8, 2005, https://arxiv.org/abs/math/0508148.

[4] M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. 61 (1965), 639–646, https://doi.org/10.1017/S0305004100038974.

[5] *Eight minimum-support octahedral spheres give the integral hyperoctahedral module of the four-cube independence complex*, public record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-eight-minimum-support-octahedral-spheres-give-the-integral-hyper--1740b146ec04/RESULT.md.

[6] *Complete hyperoctahedral character of four-cube independence homology*, public record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-complete-hyperoctahedral-character-of-four-cube-independence-hom--0e8db477d5d1/RESULT.md.

[7] *The antipodal scale-two four-cube Rips quotient is \(\mathbb{RP}^3\vee\bigvee^4S^3\)*, public record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-antipodal-scale-two-four-cube-rips-quotient-is-mathbb-rp-3-v--498994e0cb0a/RESULT.md.
