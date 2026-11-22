# Maximum tetrahedra in the regular icosidodecahedron and their twenty facial families

## Finding
Let \(K\) be the unit-edge regular icosidodecahedron. Every tetrahedron with four points in \(K\) has volume at most
\[
V_{\max}=\frac{25+11\sqrt5}{24}.
\]
All equality cases form exactly **twenty triangular two-parameter families**, indexed by the twenty triangular faces of \(K\). For each such face \(F\), there is a unique three-vertex anchor set \(A_F\) forming an equilateral triangle of side \(\varphi^2\), where \(\varphi=(1+\sqrt5)/2\), such that precisely the tetrahedra \(\operatorname{conv}(A_F\cup\{p\})\), for \(p\in F\), realize \(V_{\max}\). Each family contains three vertex-supported extremizers, so exactly **sixty** four-vertex subsets maximize volume; they form one orbit under the full icosahedral symmetry group.

Among vertex-supported tetrahedra, the next distinct volume is
\[
V_2=\frac{11+5\sqrt5}{12},\qquad
V_{\max}-V_2=\frac{3+\sqrt5}{24},
\]
and precisely 240 four-vertex subsets attain \(V_2\). Altogether, the \(\binom{30}{4}=27{,}405\) four-vertex subsets realize exactly **twenty-seven distinct volumes**, including zero. For the known unit-edge volume \(\operatorname{vol}_3(K)=(45+17\sqrt5)/6\), the largest tetrahedron occupies exactly \((19+7\sqrt5)/232\) of \(K\).

## Assumptions and scope
The metric is the ordinary Euclidean metric on \(\mathbb R^3\); the edge length of \(K\) is one. A tetrahedron here is the convex hull of four points of \(K\), not necessarily vertices. The second-largest volume, its multiplicity and the finite spectrum refer **only to four distinct vertices**; the continuously varying class has no second-largest distinct volume.

Let \(\varphi=(1+\sqrt5)/2\) and use the regular edge-two icosahedral vertices
\[
I=\{(0,\pm1,\pm\varphi),(\pm\varphi,0,\pm1),(\pm1,\pm\varphi,0)\}.
\]
Write \(E=\{\{u,v\}\subset I:\|u-v\|^2=4\}\). Then \(E\) has thirty edges, and
\[
M=\{(u+v)/2:\{u,v\}\in E\}
\]
consists of the thirty vertices of the unit-edge icosidodecahedron \(K=\operatorname{conv}M\). Each triangle in the regular icosahedron produces one facial triangle of \(K\) by taking its three edge midpoints.

## Proof
**1. Exhaustive parameter reduction.** A tetrahedron's signed sixfold volume is a determinant affine in each vertex. For each choice of three fixed points in a convex polytope, the absolute determinant is maximized at a polytope vertex. Applying this separately in four coordinates proves that the global maximum over \(K^4\) is realized by some four vertices in \(M\). This argument establishes a maximum but does not by itself classify the nonvertex equality cases.

**2. Exact finite geometric certificate.** Work in \(\mathbb Z[\varphi]\), representing \(a+b\varphi\) as the integer pair \((a,b)\) and reducing \(\varphi^2=\varphi+1\). Store doubled midpoints \(2p=u+v\), avoiding all coordinate denominators. For each four-element subset \(\{p,q,r,s\}\subset M\), calculate
\[
D=\left|\det(2q-2p,\,2r-2p,\,2s-2p)\right|\in\mathbb Z[\varphi].
\]
The actual tetrahedron volume is \(D/48\). The accompanying independent two-form determinant implementation exhausts all \(27{,}405\) subsets and finds exactly 27 algebraic values (the complete count table is in `spectrum.csv`). Its largest two values, in the \((a,b)\) representation, are \((28,44)\) with 60 occurrences and \((24,40)\) with 240 occurrences. Their exact order follows by comparisons in \(\mathbb Q(\sqrt5)\), not floating point: \(4+4\varphi>0\) and the runner-up exceeds every remaining level. Dividing by 48 yields the stated maximum, runner-up and sharp vertex-supported gap.

**3. Facial equality and classification.** Fix three vertices of any maximizing vertex tetrahedron and test the possible fourth vertices using the same exact determinant. Of the four possible choices of omitted vertex, exactly one has multiple maximizing replacements: **exactly three**, the three vertices of one triangular face \(F\) of \(K\). The other three choices each have a unique maximizing replacement. Across the 60 maximizing vertex tetrahedra these exceptional fixed anchor triples are exactly twenty distinct triples, whose corresponding moving triangles are precisely the twenty facial triangles of \(K\); each anchor triangle has all three squared side lengths \(\varphi^4\).

Because determinants are affine in the fourth variable, fixing an anchor triangle and taking any point in the convex triangular face gives the same maximal absolute determinant. Conversely, suppose any (possibly nonvertex) tetrahedron is maximizing. Express each of its four points as a convex combination of vertices of \(K\). For a fixed choice of sign of the determinant, multilinearity makes its value an average of signed determinants of four-vertex tuples. Since the signed maximum is \(48V_{\max}\) in doubled coordinates, **every tuple with positive product weight must also be maximizing with that sign**. Select one such vertex tuple. If two of the original four points were nonvertices, varying either coordinate within its positive-support vertex representation would give two distinct maximizing fourth-vertex replacements at two different positions of this fixed maximizing tuple; this contradicts the just-established one-position replacement classification. Thus at most one point is nonvertex, and that point lies in its unique maximizing triangular face. The same argument places a vertex-supported maximizing tuple in exactly one of the twenty families. This proves that the families listed above exhaust all continuous equality cases.

**4. Symmetry and normalization.** The ordered oriented triangular faces of the icosahedron yield 120 exact distance-preserving vertex permutations. Their induced action on the 30 edge-midpoints has a single orbit on the sixty maximizing four-subsets. The known whole-polytope volume \((45+17\sqrt5)/6\) follows independently from the established icosidodecahedral dissection formula, giving the stated tetrahedron-to-body volume ratio.

## Verification
Run `python3 check_tetrahedra.py` with Python 3; it uses only the standard library and verifies two algebraically different determinant expansions on **every** four-subset. It checks the exact algebraic ordering, all 27 volume levels and multiplicities, the 60 maximizing and 240 runner-up tetrahedra, all twenty exceptional moving-face families, their anchor side lengths, and the 120-element symmetry action. The complete printed exact spectrum is preserved in `spectrum.csv`. This is a rigorous finite-exhaustion proof because the vertex set and all 4-subsets are explicitly bounded and enumerated, and the convex-multilinearity argument reduces the global optimization to that finite list.

## Relationship to prior work
The edge-midpoint construction, icosidodecahedral coordinates and volume are classical; see Raman and Krishnamoorthy and Baez. Baez also discusses its relationship to the \(D_6\) and \(E_8\) root configurations, not an extremal inscribed tetrahedron. Previously published exact maximizers for tetrahedra in the **icosahedron** concern a different 12-vertex polytope and do not imply the present 30-vertex midpoint optimization or its moving facial equality sets. The present claim is the specific sharp inscribed-tetrahedron bound, twenty-family equality classification and first vertex-spectrum gap; no general novelty or historical-priority guarantee is asserted.

## Limitations
The calculation does not classify all continuous tetrahedral volumes, establish stability away from the optimal families, or generalize to arbitrary rectifications of other uniform solids. Its priority is provisional pending wider historical comparison. The underlying finite exact program and self-review are reproducible, but there is no independent mathematical audit.

## References
1. J. C. Baez, *The Icosidodecahedron*, arXiv:2309.15774, first posted 2023-09-26. https://arxiv.org/abs/2309.15774
2. T. V. Raman and M. S. Krishnamoorthy, *Visual Techniques For Computing Polyhedral Volumes* (2001), especially Sections 2.9 and 7. https://www.cs.cornell.edu/info/people/raman/publications/polyhedra/paper.html
3. S. Whitehead, *Classifying Regular Polyhedra and Polytopes using Wythoff's Construction*, arXiv:2001.09364 (2020). https://arxiv.org/abs/2001.09364
4. *Complete tetrahedron-volume spectrum and continuous maximum families in the regular icosahedron*, public published-finding corpus mathematical record (2026), concerning a distinct polytope. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-tetrahedron-volume-spectrum-and-continuous-maximum-fami--801a8f440668
