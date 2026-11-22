# Two disjoint arc reversals: a complete directed-flag homotopy classification

## Finding

For every integer \(n\ge4\), begin with the transitive tournament on \(V=\{0,\ldots,n-1\}\), oriented from smaller to larger labels, and reverse exactly two vertex-disjoint arcs. Write their four distinct endpoints in increasing order as \(a<b<c<d\), and let \(X(P)\) be the simplicial complex of subsets inducing transitive subtournaments after reversal. The following is a complete **integral homotopy** classification.

If \(a>0\) or \(d<n-1\), the complex is contractible. Otherwise \(a=0,d=n-1\) and precisely one of the following holds:

| Pairing \(P\) | Homotopy type | Necessary and sufficient conditions |
| --- | --- | --- |
| Separated: \(\{(a,b),(c,d)\}\) | \(S^3\) | \(c=b+1\), \(b-a\ge2\), \(d-c\ge2\) |
| Separated: remaining cases | contractible | not all three conditions hold |
| Crossing: \(\{(a,c),(b,d)\}\) | \(S^1\) | \(n=4\) |
| Crossing: remaining cases | contractible | \(n\ge5\) |
| Nested: \(\{(a,d),(b,c)\}\) | \(S^1\vee S^2\) | \(b=a+1\), \(c=d-1\), \(c-b\ge2\) |
| Nested: remaining cases | \(S^1\) | not all three conditions hold |

In particular, the homotopy type cannot be inferred from the number of reversed arcs alone: two reversals can leave a contractible space or produce a circle, a three-sphere, or a wedge of a circle and a two-sphere.

## Assumptions and scope

A *directed flag simplex* means a nonempty vertex subset whose induced tournament has no directed cycle; every tournament is acyclic if and only if it has no directed triangle. All arcs of the original transitive tournament are directed from the smaller to the larger endpoint. Each reversed pair is disjoint from the other (four distinct endpoints). No restriction is placed on the number or locations of unused vertices. Homotopy equivalence is non-equivariant and integral. Contractible includes the one-point case. We regard a disjoint pairing as a set of unordered pairs, reversed from the original orientation.

## Proof

**1. Minimal nonfaces and the cone rule.** Fix a triple \(u<x<v\). As the two reversed pairs have disjoint endpoints, the triple contains at most one reversed pair. It becomes a directed cycle if and only if its outer edge \((u,v)\) is reversed. If an inner edge is reversed, it remains a transitive triple. Thus the minimal nonfaces of \(X(P)\) are exactly

\[
\{u,x,v\}\quad\text{with }(u,v)\in P,\quad u<x<v.
\]

A vertex below \(a\) or above \(d\) belongs to no minimal nonface. Such a vertex is a cone point. This proves the first assertion and allows us to assume \(a=0\), \(d=n-1\).

**2. One reversed arc.** On the integer interval from \(u\) through \(v\), reversing only \((u,v)\) forbids every triangle \(\{u,x,v\}\) for \(u<x<v\). If the interval is adjacent, the directed flag complex is a simplex. Otherwise let \(W\) be its nonempty set of interior vertices. The complex is the union of the two simplices \(u*\Delta(W)\), \(v*\Delta(W)\) along \(\Delta(W)\), together with the edge \(\{u,v\}\). The union of the two large simplices is contractible and connected; adjoining the extra edge between its two vertices creates a single circle, so the complex is homotopy equivalent to \(S^1\). If there is a vertex outside the interval, it is a cone point.

**3. Separated pairs.** If \(c>b+1\), any vertex strictly between \(b\) and \(c\) appears in no forbidden triple, so the complex is a cone. If \(c=b+1\), the vertex set is the disjoint union of the two intervals \([a,b]\) and \([c,d]\), and every minimal nonface lies within one of them. Consequently the full complex is the simplicial join of the two single-arc complexes. This join is \(S^1*S^1\simeq S^3\) exactly when both arcs span at least one interior vertex, and is contractible otherwise.

**4. Nested pairs.** Suppose \(P=\{(a,d),(b,c)\}\). Put \(W=V\setminus\{a,d\}\), and let \(L\) be the directed flag complex on \(W\) with only \((b,c)\) reversed. The forbidden triples for the outer arc are exactly \(\{a,x,d\}\) with \(x\in W\); those of the inner arc are entirely contained in \(W\). Therefore, as a simplicial complex,

\[
X(P)=(a*L)\cup_L(d*L)\cup\{a,d\}=\Sigma L\cup_{\{a,d\}}[a,d].
\]

The first union is an unreduced suspension; it is path-connected because \(L\) is nonempty. Adjoining an edge between already-connected suspension vertices gives \(X(P)\simeq\Sigma L\vee S^1\). By Step 2, \(L\simeq S^1\) precisely when \(b=a+1\), \(c=d-1\), and \(c-b\ge2\). Otherwise \(L\) is contractible. Thus the stated nested types follow, integrally and without torsion.

**5. Crossing pairs.** Suppose \(P=\{(a,c),(b,d)\}\). If there is a vertex \(x\) strictly between \(a\) and \(b\), the vertex \(b\) is simplicially dominated by \(x\): every face containing \(b\) may have \(x\) adjoined, since the only forbidden triples involving \(x\) arise from \(\{a,c,x\}\) and the existing forbidden triple \(\{a,b,c\}\) precludes its other two vertices in any face containing \(b\). Removing \(b\) by a strong simplicial collapse leaves a single reversed arc \((a,c)\), with \(d\) as a cone point, and hence a contractible complex. Similarly, if \(x\) lies strictly between \(c\) and \(d\), then every face containing \(c\) can be enlarged by \(x\); removing \(c\) leaves \(a\) as a cone point. It remains to consider no vertices in those two outer gaps.

Every central vertex \(x\) with \(b<x<c\) occurs in just the two families of forbidden triples \(\{a,x,c\}\), \(\{b,x,d\}\). If two central vertices \(x,y\) occur, every face containing \(x\) can be enlarged by \(y\); deleting all but one is a sequence of strong simplicial collapses. If no central vertex remains, the only forbidden triples are \(\{a,b,c\}\) and \(\{b,c,d\}\). The resulting four-vertex complex consists of two triangles attached along an edge plus the extra edge \(\{b,c\}\); it is homotopy equivalent to \(S^1\).

If one central vertex remains, relabel the resulting five vertices \(0,1,2,3,4\), with reversed arcs \((0,3),(1,4)\). Its full face set has 21 nonempty faces; the following ten elementary free-face pairs collapse it to the vertex \(\{2\}\):

```
(13,123), (12,012), (14,014), (02,024), (04,034),
(34,234), (1,01), (0,03), (3,23), (4,24)
```

Here each digit denotes a vertex, and every first face is free in the complex remaining at its step. This completes the crossing case and the exhaustive classification.

## Verification

The accompanying `verify.py` constructs all directed flag simplices directly from the forbidden-triangle criterion, exhaustively checks every disjoint pair of reversed arcs for \(4\le n\le9\), computes their reduced mod-two homology, and confirms the formula. It checks all 756 configurations, with counts 689 contractible-predicted cases, 52 circle cases, 10 three-sphere cases, and five mixed \(S^1\vee S^2\) cases. It also independently validates every free-face condition and the final vertex for the explicit ten-pair crossing collapse. Run `python verify.py` using Python 3; the recorded expected stdout is provided as `verification_output.txt`. These finite checks support but do not replace the universal structural argument above. The nontrivial homotopy decompositions—not finite-field calculations—establish the integral statements.

## Relationship to prior work

Govc, Levi, and Smith introduce tournaplexes and directed flag complexes and study their directionality filtrations; their publicly posted version of 29 February 2020 provides the present research setting and the verified primary classification 55U10. Belkhechine, Ben Salha, and Romdhane study tournaments formed by reversing pairings in a transitive tournament, with modular indecomposability as their principal concern; their results do not give this topological classification. Govc computes directed flag homotopy types and a complete census of all tournaments through ten vertices; this already covers individual low-order instances, but does not provide the universal endpoint/gap criteria for *two disjoint arc reversals at all orders*. The present theorem relies on no novelty assertion for the definitions, pairing construction, or prior small-order computations. No covering statement was found in the inspected primary texts and targeted scholarly records; this is evidence-limited, not a proof of absolute priority.

## Limitations

Only two *disjoint* arc reversals are classified. Reversals sharing vertices, three or more reversed arcs, equivariant homotopy and maps between distinct reversal configurations are outside scope. The proof gives abstract homotopy equivalence, not a canonical symmetry-equivariant splitting. Prior literature may contain unindexed equivalent results.

## References

1. D. Govc, R. Levi, J. P. Smith, *Complexes of Tournaments, Directionality Filtrations and Persistent Homology*, arXiv:2003.00324, first posted 2020-02-29. https://arxiv.org/abs/2003.00324 ; open-access journal article https://doi.org/10.1007/s41468-021-00068-0 .
2. H. Belkhechine, C. Ben Salha, R. Romdhane, *Irreducible pairings and indecomposable tournaments*, arXiv:2312.04039, first posted 2023-12-07. https://arxiv.org/abs/2312.04039 .
3. D. Govc, *Computing Homotopy Types of Directed Flag Complexes*, arXiv:2006.05333, first posted 2020-06-09. https://arxiv.org/abs/2006.05333 .
