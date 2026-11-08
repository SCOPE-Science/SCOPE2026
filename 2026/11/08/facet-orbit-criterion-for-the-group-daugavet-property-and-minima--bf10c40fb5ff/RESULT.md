# Facet-orbit criterion for the group Daugavet property and minimal polygonal actions

## Finding
For any finite-dimensional **real** normed space with a polyhedral unit ball \(B\), the group Daugavet property of any isometry subgroup \(G\) is equivalent to a finite incidence test:
\[
\forall v\in\operatorname{vert}(B)\;\forall F\in\operatorname{facets}(B)\;\exists g\in G:\quad v\in gF.
\]
Here the group Daugavet property means that every rank-one bounded operator \(T\) satisfies
\[
\max_{g\in G}\|I+g\circ T\|=1+\|T\|.
\]
For the regular \(N\)-gonal real Banach plane, \(N\ge4\) even, the complete classification among **all** subgroups of the dihedral linear-isometry group is
\[
X_N\text{ has the }G\text{-Daugavet property}\quad\Longleftrightarrow\quad R^2\in G,
\]
where \(R\) rotates through \(2\pi/N\). The smallest such group is the cyclic group \(\langle R^2\rangle\) of order \(N/2\). No reflection subgroup with a smaller rotation subgroup qualifies.

## Assumptions and scope
The scalar field is \(\mathbb R\); \(\dim X\ge2\); \(B=\{x:\|x\|\le1\}\) is a full-dimensional centrally symmetric convex polytope. A vertex is a zero-dimensional face, and a facet is a maximal proper face of codimension one. Every surjective linear isometry permutes the finitely many vertices, so \(G\) is finite. For the polygon case, \(N\) is an even integer at least four; the Euclidean regular polygon is the unit ball and \(R\) is its fundamental rotation. Group composition acts on the output of \(T\).

## Proof
**1. A norm-additivity observation.** For \(x,y\in S_X\), the identity \(\|x+y\|=2\) is equivalent to the existence of a norm-one supporting linear functional taking the value one at both points. In a polytope, its exposed face lies in some facet. Thus \(\|x+y\|=2\) if and only if \(x,y\) lie in a common facet. If \(y\) is in the relative interior of a facet \(F\), it belongs to no other facet, so \(\|x+y\|=2\) precisely when \(x\in F\).

**2. Facet orbit implies the operator equation.** Write any nonzero rank-one operator as \(T=f\otimes y\), normalized so \(\|f\|=1\) and \(\|y\|=\|T\|\). Initially take \(\|y\|=1\); the general positive scalar follows by the same norm-additivity argument with \(v+\|T\|gy\). Some vertex \(v\) satisfies \(f(v)=1\), after reversing its sign if necessary. Select a facet \(F\) containing \(y\). By hypothesis, \(v\in gF\) for some \(g\in G\); also \(gy\in gF\). The common supporting functional gives \(\|v+gy\|=2\), and hence \(\|I+gT\|\ge2\). The triangle inequality gives the reverse bound. For \(\|T\|=t>0\), the same functional gives \(\|v+tgy\|=1+t\).

**3. Failure of facet incidence produces a rank-one witness.** Suppose a vertex \(v\) is absent from \(gF\) for every \(g\in G\). Choose a norm-one functional \(f\) exposing \(v\) uniquely, and a unit vector \(y\) in the relative interior of \(F\). Then \(T=f\otimes y\) has norm one. If some \(\|I+gT\|=2\), compactness of \(B\) supplies \(x\in S_X\) with \(\|x+f(x)gy\|=2\). The triangle inequality forces \(\lvert f(x)\rvert=1\), and unique exposure gives \(x=v\) or \(x=-v\). In both cases \(\|v+gy\|=2\). Because \(gy\) belongs to the relative interior of the unique facet \(gF\), Step 1 yields \(v\in gF\), a contradiction. Finiteness of \(G\) gives \(\max_g\|I+gT\|<2\).

**4. Polygon subgroup classification.** Label the \(N\) facets by residues \(j\in\mathbb Z/N\mathbb Z\) such that facet \(j\) joins vertices \(j\) and \(j+1\). Vertex \(j\) is incident to exactly the two facets \(j-1\) and \(j\). For a subgroup \(G\) of the dihedral group, write its rotation subgroup \(G\cap\langle R\rangle=\langle R^L\rangle\), with \(L\mid N\). This subgroup induces congruence classes of facet indices modulo \(L\). Either \(G\) contains no reflections, or \(G\) contains a reflection inducing \(r\mapsto s-r\pmod L\) for some \(s\). The incidence criterion requires every orbit of these residues to meet every adjacent residue pair \(\{r-1,r\}\).

If \(L=1\) or \(L=2\), consecutive residues meet all orbits, hence the criterion holds, with or without reflections. If \(L\ge5\), the involution has at least \(\lceil L/2\rceil\ge3\) orbits (and the rotation-only action has \(L\)), impossible for a two-element adjacent pair to meet all. For \(L=3\), every reflection has one fixed residue and one two-element orbit; the two elements of the latter orbit are adjacent, and their pair misses the fixed orbit. For \(L=4\), an even reflection parameter gives three orbits, while an odd parameter gives two adjacent two-element orbits; in the latter case one adjacent pair lies entirely in one orbit. Without reflections, \(L\ge3\) always gives at least three orbits. Thus the property holds exactly when \(L\le2\), equivalently when \(R^2\in G\). All linear isometries of a Euclidean regular polygon form its dihedral group: they permute its vertices, and for \(N\ge6\) preservation of a common Euclidean circle at \(N\) points forces orthogonality; the square case is immediate. Finally \(\langle R^2\rangle\) has order \(N/2\), and every qualifying group contains it.

## Verification
The result is an exact finite-group and convex-face argument; no limiting or probabilistic claim occurs. The standalone `CHECK.py` enumerates all cyclic and dihedral subgroup facet orbits for even \(N\) from \(4\) through \(160\), compares the incidence criterion with \(L\le2\), and reports 13,831 passed diagnostics. The infinite \(N\)-statement follows from the residue-orbit proof in Step 4, not from enumeration.

## Relationship to prior work
Dantas, del Río, and Raunig (2026) introduced the group Daugavet equation and established general geometric slice and invariant-hull characterizations (their Proposition 2.9). Their Example 3.8 proves the property for the **full order-eight rotation group** of a regular octagonal Banach plane. These contributions are prior work. The present claim reduces the equation to a finite vertex–facet incidence test on any real polyhedral Banach space and applies that test to classify **every** subgroup, including reflective ones, with a sharp minimal rotation subgroup for every regular even-gonal plane. Its proof uses the general definition and does not claim the existing slice characterization as new. Earlier research on the alternative Daugavet property covers the special scalar-action case but not these full dihedral subgroup classifications.

## Limitations
The criterion assumes a finite-dimensional **real polyhedral** unit ball. It does not classify smooth norms, complex Banach spaces, arbitrary convex bodies, or the quantitative size of subcritical Daugavet deficits. General group Daugavet slice characterizations can be used to derive the criterion after a face-incidence argument, so claims of historical priority must be tested against all implications of those characterizations; no independent publication-priority assessment has been performed.

## References
- S. Dantas, H. del Río, T. Raunig, *A group action approach to the Daugavet property*, arXiv:2606.20429 (first submitted 18 June 2026), particularly Proposition 2.9 and Example 3.8. https://arxiv.org/abs/2606.20429
- J. Langemets, M. Lõo, M. Martín, Y. Perreau, A. Rueda Zoca, *The super Alternative Daugavet property for Banach spaces*, arXiv:2504.07631 (first submitted 10 April 2025); background on the scalar-action case. https://arxiv.org/abs/2504.07631
