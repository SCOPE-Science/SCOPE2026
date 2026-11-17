# Complete three-chip avalanche homotopy classification on directed cycles

## Finding

Fix an integer \(n\ge3\). Let \(\overrightarrow C_n\) have vertex set \(\mathbb Z/n\mathbb Z\) and arrows \(i\to i+1\). Start parallel sandpile firing from a binary configuration supported on exactly three vertices \(T\). The *avalanche complex* \(\mathcal A(\overrightarrow C_n,T)\) is the downward closure of the supports of simultaneously firing vertices at successive times. There are no sinks. Translate the support to \(T=\{0,a,b\}\), and write
\[
 g=\gcd(n,a,b),\qquad m=n/g.
\]
Call \(T\) an **arithmetic progression** when \(T=\{t,t+s,t+2s\}\) modulo \(n\) for some \(t,s\). Call two positions **antipodal** if their difference is \(n/2\) modulo \(n\), possible only for even \(n\).

**Theorem.** The geometric realization of \(\mathcal A(\overrightarrow C_n,T)\) is a disjoint union of \(g\) components of the following homotopy types:

| Support type | Homotopy type of EACH component |
| --- | --- |
| Arithmetic progression, \(m=3\) | a point |
| Arithmetic progression, \(m=4\) | \(S^2\) |
| Arithmetic progression, \(m\ge5\) | \(S^1\) |
| Nonprogression, no antipodal pair | \(\bigvee^{m+1}S^1\) |
| Nonprogression, with an antipodal pair | \(\bigvee^{m/2+1}S^1\) |

The last case necessarily has even \(m\). All homology groups are torsion-free. Explicitly, with integral coefficients, \(H_0\cong\mathbb Z^g\), the sole possible positive homology groups are \(H_2\cong\mathbb Z^g\) when the support is a progression with \(m=4\), and \(H_1\) of rank \(g\) for progressions with \(m\ge5\), \(n+g\) for nonprogressions without antipodal pairs, and \(n/2+g\) for nonprogressions with antipodal pairs. Otherwise positive homology vanishes.

This fills the natural three-chip classification beyond the previously studied consecutive and adjacent-chip configurations. For instance, the nonconsecutive support \(T=\{0,2,5\}\) on \(\overrightarrow C_9\) yields \(\bigvee^{10}S^1\); the same support on \(\overrightarrow C_{10}\), which contains an antipodal pair, yields \(\bigvee^{6}S^1\). The nonconsecutive progression \(\{0,3,6\}\) on \(\overrightarrow C_{12}\) gives three disjoint two-spheres.

## Assumptions and scope

There is exactly one grain at each occupied vertex and none elsewhere initially; the three occupied vertices are distinct. Each vertex has out-degree one, and all unstable vertices fire simultaneously. The empty face is included in the usual abstract simplicial-complex convention, without changing the geometric realization. An arithmetic progression is understood as an **unordered** set, so its three points can be presented in any order. The classification is of ordinary geometric homotopy types, not filtered persistence modules or equivariant homotopy types.

## Proof

**1. The dynamics is translation.** For a binary configuration on the forward cycle, every occupied vertex is unstable and sends exactly one grain to its successor; the resulting configuration at the successor is again binary. Thus every time step rotates the occupied support by one. The facets of the avalanche complex are exactly the distinct translates \(T+t\) for \(t\in\mathbb Z/n\mathbb Z\).

**2. Components live in difference cosets.** Every edge belongs to one of the three unoriented difference classes \(\pm a\), \(\pm b\), and \(\pm(b-a)\). Hence edges, and therefore connected components, lie inside cosets of the subgroup \(H=\langle a,b\rangle\) of \(\mathbb Z/n\mathbb Z\). Conversely, edge paths connect by differences \(a\) and \(b\), so every coset is one connected component. There are exactly \(g\) cosets, each with \(m\) vertices. Translation permutes them transitively.

**3. Arithmetic progressions.** Choose \(T=\{t,t+s,t+2s\}\) and note that \(H=\langle s\rangle\). On each coset, identify repeated addition of \(s\) with the vertices of a cycle of length \(m\). The facets are precisely the consecutive triples \(\{j,j+1,j+2\}\). If \(m=3\), only one distinct facet occurs, giving a filled triangle. If \(m=4\), the four facets are all the three-element subsets of the four vertices, so the complex is the boundary of a tetrahedron. If \(m\ge5\), every long edge \(\{j,j+2\}\) is a free face of precisely one triangle. Collapsing each such triangle and its long edge leaves exactly the short edges \(\{j,j+1\}\), a cycle graph of length \(m\). This proves all three progression cases without relying on a computer enumeration.

**4. Nonprogressions.** The three unoriented edge-difference classes are pairwise distinct. Indeed, \(\pm a=\pm b\) implies \(b=-a\) (the other choice contradicts distinct vertices), giving the progression \(\{-a,0,a\}\). Likewise, \(\pm a=\pm(b-a)\) implies \(b=2a\), and \(\pm b=\pm(b-a)\) implies \(a=2b\); both give progressions. Further, a nonzero translation preserving a three-element support would act freely on its points, thus have order three and make that support a progression. Consequently there are exactly \(n\) distinct triangle facets.

For any nonantipodal difference class \(\pm d\), the \(n\) translates of its undirected edge are all distinct. Since each triangle contains exactly one edge from that class, each such edge occurs in exactly one triangle. For an antipodal difference class \(2d=0\), there are \(n/2\) distinct translated edges. At most one of the three classes is antipodal, so choose one nonantipodal class. Each of its \(n\) edges is free and belongs to a different triangle. Collapse all \(n\) triangles using these edges, leaving a graph on the same vertices.

If no edge is antipodal, there were \(3n\) edges before the collapses and \(2n\) afterward; hence each component has \(m\) vertices and \(2m\) edges. If an antipodal pair occurs, there were \(5n/2\) edges and \(3n/2\) remain, hence each component has \(m\) vertices and \(3m/2\) edges. To see the residual graph stays connected in each coset, observe that its two remaining difference classes still generate the same subgroup \(H\): any one of \(a\), \(b\), and \(b-a\) is an integer linear combination of the other two. A connected finite graph with \(v\) vertices and \(e\) edges is homotopy equivalent to a wedge of \(e-v+1\) circles. The respective numbers are \(m+1\) and \(m/2+1\), completing the classification.

## Verification

A standalone Python program, `verify.py`, independently constructs translated firing sets, directly simulates parallel binary firing, tests which three-element supports are progressions, and checks the free-edge collapse argument and residual graph components. It exhaustively checks all \(9,139\) normalized supports \(\{0,a,b\}\) for \(3\le n\le39\). Of these, \(1,140\) are also checked directly against sandpile dynamics and \(816\) receive independent exact mod-two simplicial boundary-rank calculations (all normalized supports with \(n\le18\)). The verifier uses only Python's standard library and prints `ALL_VERIFY_OK` followed by its counts and explicit examples. It is supplementary to the infinite-parameter proof above.

Run: `python3 verify.py`.

## Relationship to prior work

Riihimäki and Smith introduced avalanche homology in arXiv:2606.26786 (first posted June 25, 2026; November 2 revision examined). Their Theorem 3.32 handles consecutive occupied blocks, Proposition 3.34 classifies configurations with an adjacent occupied pair, and Lemma 3.25 handles full residue-class supports. Thus those overlapping cases are **not** new here. Their Question 3.36 asks about the decomposition of the full configuration space by avalanche homotopy type. The new part is the full previously unclassified portion of three-chip supports, particularly pairs of isolated gaps without adjacency, and the resulting general arithmetic/antipodal trichotomy.

Adamaszek, Adams, Frick, Peterson, and Previte-Johnson (arXiv:1410.4336) classify nerves of circular arcs; their special family of translated consecutive triples supplies the progression cases. The general nonprogression complexes here have multiple independent circle generators, and are not in the homogeneous circular-arc classification invoked for consecutive triples. The complete result is also a direct elementary-collapse theorem for cyclic translates of an arbitrary three-element subset.

## Limitations

This is a classification for binary three-grain initial conditions on forward directed cycles. The theorem does not cover four or more grains, other digraphs, nonbinary transient filtration behavior, or persistence barcodes. External novelty searches cannot rule out unindexed or hidden equivalent results. The collapse proof establishes ordinary homotopy types and integral homology, not a canonical choice of homology generators across varying supports.

## References

1. H. Riihimäki and J. P. Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786v1 (June 25, 2026), and arXiv:2606.26786v2 (November 2, 2026), https://arxiv.org/abs/2606.26786 and https://arxiv.org/html/2606.26786v2.
2. M. Adamaszek, H. Adams, F. Frick, C. Peterson, C. Previte-Johnson, *Nerve complexes of circular arcs*, arXiv:1410.4336 (October 16, 2014), https://arxiv.org/abs/1410.4336; *Discrete & Computational Geometry* 56, 251–273 (2016).
