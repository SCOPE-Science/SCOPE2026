# Three conifold strata in the six-dimensional Gelfand–Tsetlin toric variety

## Finding
Let \(k\) be an algebraically closed field of characteristic zero and let \(P\) be the regular Gelfand–Tsetlin polytope of highest row \((4,3,2,1)\). The projective normal toric sixfold \(X_P\), defined by the normal fan of \(P\), has a reduced singular locus with precisely three irreducible components. Each component is the closure of a three-dimensional torus orbit. They form a chain: the middle component meets each outer component along a toric projective line, while the outer components are disjoint. At a general point of each component, the transverse analytic singularity is the ordinary threefold node
\[
\operatorname{Spec} k[a,b,c,d]/(ab-cd).
\]
In particular, the singular locus is pure of dimension three and has codimension three in \(X_P\); the non-\(\mathbb Q\)-factorial locus coincides set-theoretically with the singular locus.

The three components are canonically indexed by the following three faces of \(P\), where the notation is defined next:
\[
F_U=\{y_1=y_2=z_1=3\},\qquad
F_C=\{y_2=z_1=z_2=w\},\qquad
F_L=\{y_2=y_3=z_2=2\}.
\]
Writing \(Y_F\) for the closure of the torus orbit corresponding to a face \(F\), the exact assertion is
\[
\operatorname{Sing}(X_P)_{\mathrm{red}}=Y_{F_U}\cup Y_{F_C}\cup Y_{F_L},
\quad Y_{F_U}\cap Y_{F_L}=\varnothing,
\]
and \(Y_{F_U}\cap Y_{F_C}\) and \(Y_{F_C}\cap Y_{F_L}\) are each a single \(\mathbb P^1\) set-theoretically.

## Assumptions and scope
The polytope \(P\subset\mathbb R^6\) has coordinates \((y_1,y_2,y_3,z_1,z_2,w)\) and inequalities
\[
4\ge y_1\ge3\ge y_2\ge2\ge y_3\ge1,\qquad
y_1\ge z_1\ge y_2,\quad y_2\ge z_2\ge y_3,\quad z_1\ge w\ge z_2.
\]
All faces, normal cones, and lattices use the standard integral lattice \(\mathbb Z^6\). The complete normal fan defines \(X_P\). The statement concerns reduced singular support and generic transverse analytic types; it does not assert a primary decomposition of the Jacobian ideal or classify analytic types along the component intersections.

## Proof
**1. Exact vertex and face determination.** Every vertex is the unique intersection of six linearly independent supporting facet hyperplanes. All \(\binom{12}{6}=924\) choices of six facet hyperplanes can be solved by exact rational Gaussian elimination and filtered against the original inequalities, thereby exhaustively producing exactly 40 feasible vertices. Independently, choosing every entry in the three interlacing rows equal to one of its two immediate upper bounds, successively \(y_i\in\{\lambda_i,\lambda_{i+1}\}\), \(z_i\in\{y_i,y_{i+1}\}\), and \(w\in\{z_1,z_2\}\), yields precisely those same 40 distinct points among \(2^6\) endpoint patterns. Every such endpoint point is indeed a vertex because its six chosen equalities have triangular independent coefficient vectors.

There are exactly twelve facets, indexed in this order:
\[
\begin{array}{c|cccccccccccc}
i&1&2&3&4&5&6&7&8&9&10&11&12\\\hline
\text{equality}&y_1=4&y_1=3&y_2=3&y_2=2&y_3=2&y_3=1&z_1=y_1&z_1=y_2&z_2=y_2&z_2=y_3&w=z_1&w=z_2
\end{array}
\]
Every nonempty face is an intersection of these facets, and hence is uniquely represented by its set of contained vertices. Enumerating the \(2^{12}\) possible intersections and deduplicating the nonempty resulting vertex sets yields the face counts
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)=(40,132,186,139,57,12,1).
\]
The dimension of a face is computed as the rational row rank of its vertex differences; the codimension is thus independent of any floating-point tolerance.

**2. Smoothness criterion with no hidden lattice-index exception.** The primitive inward or outward normal of each facet is one of \(\pm e_i\) or \(e_i-e_j\). Together they constitute rows of a node-edge incidence matrix with one grounded node; consequently the whole matrix is totally unimodular. Let \(F\) be any face of dimension \(d\), and let \(r(F)\) count the facets containing it. Its normal cone has dimension \(6-d\) and precisely \(r(F)\) extreme rays. A cone with \(r(F)>6-d\) is nonsimplicial and singular. If \(r(F)=6-d\), the corresponding normal rows are linearly independent and, by total unimodularity, form part of a lattice basis. That cone is smooth. Thus
\[
O_F\subseteq\operatorname{Sing}(X_P)\quad\Longleftrightarrow\quad r(F)>6-d.
\]
The exact enumeration of nonempty facet intersections gives singular face counts \((16,28,16,3)\) in dimensions zero through three, and zero in dimensions four through six. There are only three inclusion-maximal singular faces, each of dimension three: the facet-index sets \((2,3,7,8)\), \((4,5,9,10)\), and \((8,9,11,12)\), namely \(F_U,F_L,F_C\). Every singular face is contained in one of these. Normal-fan orbit closure relations prove that their three orbit closures are exactly the irreducible components of the reduced singular locus. The outer faces have six vertices each (triangular-prism face lattices); the central face has eight vertices (cube face lattice).

**3. Incidence of the components.** The equalities \(y_2=3\) and \(y_2=2\) show \(F_U\cap F_L=\varnothing\). The intersection \(F_U\cap F_C\) is the edge where \(y_1=y_2=z_1=z_2=w=3\) and \(1\le y_3\le2\). The intersection \(F_C\cap F_L\) is the edge where \(y_2=y_3=z_1=z_2=w=2\) and \(3\le y_1\le4\). The orbit-closure intersection of torus-invariant subvarieties is the union of orbit closures indexed by common subfaces, so each pair of adjacent components meets along the single projective toric curve of that edge, isomorphic to \(\mathbb P^1\). There is no triple intersection.

**4. Generic transverse node.** At each maximal singular face, its normal cone has four primitive rays in a rank-three saturated lattice. In the facet order displayed above these are the outward normals of respectively \((2,3,7,8)\), \((4,5,9,10)\), and \((8,9,11,12)\); in every case they satisfy precisely the primitive relation \(v_1+v_2=v_3+v_4\). An exact check of all rank-three minors gives greatest common divisor one, so the rays span their saturated lattice. Every three-ray subset is a lattice basis of that rank-three lattice. After a unimodular basis change the cone is generated by \((1,0,0),(0,1,0),(0,0,1),(1,1,-1)\). Its dual integral semigroup has four generators with a single quadratic relation \(ab=cd\). The toric affine chart at the generic orbit therefore has transverse germ \(\operatorname{Spec}k[a,b,c,d]/(ab-cd)\). Because toric \(\mathbb Q\)-factoriality is equivalent to simpliciality of every cone in its fan, the same three orbit closures exhaust the non-\(\mathbb Q\)-factorial locus.

## Verification
Run `python3 verify_gt4.py` using Python 3 and only the standard library. It independently solves all 924 six-facet systems, cross-checks all 64 endpoint patterns, enumerates 4096 subsets of the twelve facets, computes all face dimensions by exact rational elimination, checks the complete singular-orbit distribution, identifies the three maximal singular faces and both shared edges, and checks the saturation and primitive four-ray relation of each transverse cone. The expected final line is `VERIFY_OK: 40 vertices, 567 faces, 63 singular orbits, three conifold strata in a chain`. The proof of total unimodularity and the toric affine semigroup argument are mathematical arguments, not consequences of these finite assertions alone.

## Relationship to prior work
The regular Gelfand–Zetlin polytope and its face/flag interpretation are classical; Kiritchenko (2009) explains its geometry and the simple-vertex picture. Kiritchenko–Smirnov–Timorin (2010/2011) discuss the nonsimple polytope and its polytope ring. An–Cho–Kim (2016) determine general face-lattice and \(f\)-vector formulas, and Pegel (2016) classifies marked-order-polytope faces and describes normal-fan combinatorial constancy. Their results supply fundamental combinatorial context, but the specific three-component reduced toric singular-locus classification, exact incidence chain, and conifold transverse germs are not stated in the inspected relevant sections. The \(f\)-vector and general orbit smoothness criterion alone are not claimed as new. The explicit singular-stratum extraction and lattice-local classification are the proposed contribution.

## Limitations
This is a complete reduced singular-support classification for the normal-fan toric variety of the specified regular \(\mathrm{GL}_4\) polytope, not a classification of all Gelfand–Tsetlin toric degenerations. It does not compute embedded singular-scheme structure or nongeneric analytic types at the two intersection curves. The published general face-lattice theorems might make some of these counts derivable by alternate specialized calculations; an unlocated direct computation remains the main originality risk.

## References
- V. Kiritchenko, *Gelfand–Zetlin polytopes and flag varieties*, arXiv:0906.4866, first public 2009-06-26, https://arxiv.org/abs/0906.4866.
- V. Kiritchenko, E. Smirnov, V. Timorin, *Schubert calculus and Gelfand–Zetlin polytopes*, arXiv:1101.0278, first public 2010-12-31, https://arxiv.org/abs/1101.0278.
- B. H. An, Y. Cho, J. S. Kim, *On the f-vectors of Gelfand–Cetlin polytopes*, arXiv:1606.05957, first public 2016-06-20, https://arxiv.org/abs/1606.05957.
- C. Pegel, *The Face Structure and Geometry of Marked Order Polyhedra*, arXiv:1610.01393, first public 2016-10-05, https://arxiv.org/abs/1610.01393.
