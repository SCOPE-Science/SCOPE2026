# Exact online dimension and sparse-paving topology of ternary two-conic unions

## Finding
Let \(P=\operatorname{PG}(2,\mathbb F_3)\), and let \(\mathcal O\) be its \(234\) smooth projective conics, viewed as four-element subsets of the \(13\) rational points. Consider the distinct Boolean concepts
\[
\mathcal H=\{C\cup D:C,D\in\mathcal O,\ C\ne D\}\subseteq 2^P,
\]
where only rational-point membership is tested and two pairs giving the same union represent one concept. There are exactly \(4641\) such concepts.

**New adaptive assertion.** The exact Littlestone dimension of \(\mathcal H\) is **eight**. Its VC dimension is seven; thus
\[
\boxed{\operatorname{VCdim}(\mathcal H)=7 < 8=\operatorname{Ldim}(\mathcal H).}
\]
A complete, explicit adaptive tree of depth eight with \(256\) feasible leaves is supplied in `online_tree.json`. Exhaustive state recursion proves that depth nine is impossible.

**Structural companion assertion.** Its VC-shattering complex \(\Delta\) is the independence complex of a rank-seven **sparse-paving matroid** on \(13\) elements. The \(78\) circuit-hyperplanes are exactly unions of two distinct projective lines. In particular,
\[
\boxed{\Delta\simeq\bigvee^{714} S^6}
\]
in integral homotopy type, and \(\widetilde H_6(\Delta;\mathbb Z)\cong\mathbb Z^{714}\) with all other reduced integral homology zero. The previously established static-support classification is reproduced and independently checked here as the premise of this structural conclusion; the new content is the exact adaptive depth and the matroid/topology identification.

## Assumptions and scope
All geometry is over \(\mathbb F_3\). Points are one-dimensional vector subspaces of \(\mathbb F_3^3\), normalized by setting the first nonzero homogeneous coordinate to one and then sorted lexicographically. A conic is geometrically nonsingular; over this field its rational point set is a four-arc (no three collinear), and every four-arc comes from a unique smooth conic. Concepts are unions of exactly two **distinct** conics, not single conics, ordered pairs, or their scheme-theoretic unions. The concept centers and the query domain are all of \(P\); no restriction to points outside the selected conics is imposed.

For \(S\subseteq P\), ordinary VC shattering means \(\{H\cap S:H\in\mathcal H\}=2^S\). Littlestone dimension is the maximum integer \(d\) for which there is a complete binary tree of depth \(d\), with queries at interior nodes and a concept consistent with every root-to-leaf sequence of zero/one answers. Identical point queries can be removed from a feasible path, so it suffices to query previously unqueried points.

## Proof
**1. Enumeration model independent of the adaptive calculation.** There are \((3^3-1)/(3-1)=13\) normalized points and similarly \(13\) projective lines, each having four points. Enumerate the \(\binom{13}{4}=715\) four-subsets and retain those meeting every line in at most two points: exactly \(234\) remain. A projective change of coordinates sends any such quadrangle to the four standard frame points. Quadratic forms through them form a projective pencil with precisely three reducible members, corresponding to the pairings of four points into two lines, and one smooth member. This proves the conic/four-arc correspondence. The two-conic unions form exactly \(4641\) different rational-point subsets, of sizes five through eight. `verify_arcs.py` obtains this number by arcs and lines; `verify_quadrics.cpp` independently enumerates nonsingular quadratic forms using their nonzero polar-Hessian determinant.

**2. Static-support classification and its exact boundary.** Both programs enumerate all \(8192\) query supports \(S\subseteq P\), compute \(\{S\cap H:H\in\mathcal H\}\), and test equality with \(2^S\). They obtain
\[
\Phi_{\mathcal H}(z)=1+13z+78z^2+286z^3+715z^4+1287z^5+1716z^6+1638z^7.
\]
The \(78\) failed seven-point supports are exactly \(L\cup M\), where \(L\ne M\) are projective lines. Every support of at most six points is shattered, no support of size at least eight is, and each successful seven-point support is maximal. For a finite proof-checking reduction, the full projective group of order \(5616\) has exactly four seven-support orbits, with representative bitmasks \(127,191,254,439\), sizes \(78,936,468,234\), and respectively \(127,128,128,128\) realized traces; its three eight-support orbits have representatives \(255,447,510\), sizes \(468,702,117\), and \(254,255,255\) realized traces. These orbit counts can alternatively be checked by direct incidence enumeration; no sampling is involved. The static classification itself predates the new claims of this report.

**3. Exact online recursion.** Encode a partial assignment by a ternary word \(\sigma\in\{*,0,1\}^{13}\), representing unqueried, excluded and included points. Let \(N(\sigma)\) be the number of distinct concepts agreeing with this assignment. The \(N(\sigma)\) values for all \(3^{13}=1{,}594{,}323\) states are obtained exactly: initialize each concept's completely assigned binary word with multiplicity one, then replace each wildcard state with the sum of its two children, coordinate by coordinate. There are \(1{,}520{,}013\) states with nonzero concept count.

Let \(D(\sigma)=0\) for a state with at most one compatible concept. Otherwise define, with the maximum over unqueried \(p\) for which both child sets are nonempty,
\[
D(\sigma)=\max_{p}\left(1+\min\{D(\sigma[p\mapsto0]),D(\sigma[p\mapsto1])\}\right),
\]
with value zero if there is no eligible \(p\). This is an exact backward recursion, since every child has one more assigned coordinate. Induction on the number of unassigned coordinates proves that \(D(\sigma)\) equals the maximal complete mistake-tree depth below that state, and not merely a heuristic or random search bound.

Both independently implemented verifiers calculate \(D(*,\ldots,*)=8\). Moreover `verify_arcs.py` constructs `online_tree.json` from states achieving the recurrence, containing a complete depth-eight tree. It independently replays its \(256\) leaves by checking compatibility directly against the actual \(4641\) concepts. No path repeats a point. Since the exhaustive recurrence tests all choices at every partial assignment, the value eight simultaneously gives the depth-nine impossibility theorem.

**4. Sparse-paving matroid.** Put \(\mathcal B=\{S\in\binom P7:S\ne L\cup M\text{ for all distinct lines }L,M\}\). These \(1638\) seven-sets are the facets of \(\Delta\). Any two different forbidden seven-sets meet in at most five points. Indeed, if they share one constituent line, their intersection has at most that line's four points plus one further point; if they share no constituent line, each line of the first pair meets the other pair's two lines in at most two points, so the intersection has at most four points.

Consequently \(\mathcal B\) satisfies the basis-exchange axiom: for bases \(B,B'\) and \(e\in B\setminus B'\), if two candidate exchanges \(B-e+f\) and \(B-e+f'\) were nonbases, they would be distinct forbidden seven-sets with six common elements, impossible; if there is only one candidate, its exchange is \(B'\), already a base. Every six-subset extends to a base (among its seven one-point extensions, at most one is forbidden), so these bases define a rank-seven sparse-paving matroid whose independence complex is exactly \(\Delta\). Its only seven-element dependent circuits are the \(78\) line-pair unions, which are circuit-hyperplanes.

**5. Integral topology.** By the standard shellability theorem for matroid independence complexes, the pure six-dimensional complex \(\Delta\) is homotopy equivalent to a wedge of six-spheres. Its reduced Euler characteristic is exactly
\[
-1+13-78+286-715+1287-1716+1638=714.
\]
Hence there are exactly \(714\) spheres, with no torsion or lower-degree reduced homology. A separate exact binary boundary elimination yields rank \(924\) for the top boundary \(\partial_6\), and therefore \(\dim_{\mathbb F_2}\ker\partial_6=1638-924=714\), agreeing with the structural proof. This finite rank computation is a check, not the proof of the integral homotopy type.

## Verification
The file `verify_arcs.py` reconstructs conics from no-three-collinear quadrangles, checks all \(8192\) supports, computes the entire ternary online dynamic program, explicitly writes and independently replays `online_tree.json`, and checks the mod-two top boundary. Execute `python3 verify_arcs.py` using Python 3.10 or later; its output is one concise JSON object. The separately implemented `verify_quadrics.cpp` constructs smooth conics by quadratic forms and Hessian determinants, repeats the direct shattering and adaptive-state calculations, and checks the matroid face numbers and Euler characteristic. Execute `c++ -std=c++17 -O2 verify_quadrics.cpp -o verify_quadrics && ./verify_quadrics`. Only standard libraries are required. All checks completed successfully from the packaged source files. The deterministic tree file is regenerated byte-for-byte by the Python script.

## Relationship to prior work
Earlier finite incidence work determined the complete ordinary two-conic support polynomial and its three successful seven-support orbits; that result does **not** determine online Littlestone dimension or assert the sparse-paving and integral homotopy conclusions. The present new adaptive assertion uses the same natural concept family, but a different invariant and a complete ternary-state proof. The resulting strict one-unit static/adaptive separation is not an implication of the earlier static polynomial. An independent earlier blocking-pair classification already counts and describes conic-pair unions, but neither its pair-orbit theorem nor the 2022 small-plane blocking-set classification supplies the full adaptive mistake-tree calculation. The topological conclusion follows from the newly identified matroid structure and the classical matroid shellability theorem, not from any claim of a new general shellability theorem.

Asgarli–Ghioca–Yip (first posted January 22, 2023) study pencils of nonblocking hypersurfaces rather than this exact restricted online learning problem. Coolsaet–Botteldoorn–Fack (first published March 31, 2022) classify minimal blocking point sets in small projective planes; their accessible abstract does not address adaptive conic-membership queries. Manurangsi (2022/2023) establishes general algorithmic complexity of VC and Littlestone dimensions, not the particular \(13\)-point instance. Alberto's 2024 exposition provides the standard matroid/shellability connection, not this finite incidence matroid. The previous full published conic-pair classification was inspected and compared by mathematical implications, not merely title similarity.

## Limitations
These are statements only about smooth rational conics over \(\mathbb F_3\) and their distinct two-element unions, not larger fields, singular conics, or an arbitrary number of conic components. The online upper bound is a transparent exhaustive finite-state proof rather than a field-uniform geometric inequality. The matroid/topology corollary uses the previously known ordinary-support classification; it is not claimed as an independent all-fields theorem. The code certificates and self-review are not independent expert certification. An unindexed historical treatment or an inaccessible full text on small-plane blocking sets may contain equivalent adaptive or matroid conclusions; originality remains best-knowledge rather than certified global priority.

## References
1. K. Coolsaet, A. Botteldoorn and V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, J. Combin. Des. 30 (2022), 561–580, DOI: 10.1002/jcd.21842; first publicly published March 31, 2022.
2. S. Asgarli, D. Ghioca and C. H. Yip, *Existence of pencils with nonblocking hypersurfaces*, arXiv:2301.09215 (first posted January 22, 2023), Finite Fields Appl. 92 (2023), 102283.
3. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443 (first posted November 2, 2022), ITCS 2023, DOI: 10.4230/LIPIcs.ITCS.2023.85.
4. L. Alberto, *Pseudospheres: combinatorics, topology and distributed systems*, Journal of Applied and Computational Topology 8 (2024), 1023–1052, DOI: 10.1007/s41468-023-00162-5 (matroid shellability background).
5. Prior finite incidence classifications: *The five projective types of blocking unions of two smooth conics over \(\mathbf F_3\)* (public mathematical report, October 2026) and *Two-conic union shattering in the ternary projective plane* (previous finite classification; no external publication status asserted). Their static and blocking enumerations are not claimed new here.
