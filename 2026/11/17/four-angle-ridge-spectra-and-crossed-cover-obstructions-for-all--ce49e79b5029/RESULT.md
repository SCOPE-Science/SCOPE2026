# Four-angle ridge spectra and crossed-cover obstructions for all Euclidean order polytopes

## Finding

Let \(P\) be any finite poset with \(n\ge2\) elements, and put
\[
\mathcal O(P)=\{x\in[0,1]^P:x_u\le x_v\text{ whenever }u<v\text{ in }P\}.
\]
All geometry is the inherited standard Euclidean metric on \(\mathbb R^P\). Adjoin a new bottom \(\hat0\) and top \(\hat1\) to obtain \(\widehat P\). Let \(E\) be the set of directed covering relations \(a\lessdot b\) of \(\widehat P\), and put \(F=|E|\). Each element of \(E\) labels exactly one facet.

Define two combinatorial obstruction sets, counting unordered *pairs of distinct cover edges* exactly once:

- \(\mathcal B_{\mathrm{chain}}\): two edges \((a,b),(b,c)\) whose interval \([a,c]_{\widehat P}\) has more than three elements.
- \(\mathcal B_{\mathrm{cross}}\): two vertex-disjoint edges \((a,b),(c,d)\) for which both \(a<d\) and \(c<b\) hold in \(\widehat P\).

Then two facets meet in a ridge if and only if their cover-edge pair belongs to neither obstruction set. Consequently the *complete ridge count* is
\[
R(P)=\binom F2-|\mathcal B_{\mathrm{chain}}|-|\mathcal B_{\mathrm{cross}}|.
\]
Every ridge has one of the four interior dihedral angles \(\pi/4,\pi/3,\pi/2,2\pi/3\), with exact multiplicities as follows. Let \(\mathcal T\) denote the set of directed two-edge paths \(a\lessdot b\lessdot c\) for which \([a,c]_{\widehat P}=\{a,b,c\}\). Put
\[
T_{\partial}=|\{(a,b,c)\in\mathcal T:a=\hat0\text{ or }c=\hat1\}|,
\qquad T_{\circ}=|\mathcal T|-T_{\partial},
\]
and let \(d^-(v),d^+(v)\) denote the in- and out-degrees of \(v\) in the directed Hasse diagram of \(\widehat P\). Define
\[
U=\sum_{v\in P}\left(\binom{d^-(v)}2+\binom{d^+(v)}2\right).
\]
The exact spectrum, with zero-multiplicity rows omitted, is

| Interior angle | Ridge multiplicity |
| --- | ---: |
| \(\pi/4\) | \(T_{\partial}\) |
| \(\pi/3\) | \(T_{\circ}\) |
| \(2\pi/3\) | \(U\) |
| \(\pi/2\) | \(R(P)-T_{\partial}-T_{\circ}-U\) |

This is a local-to-global recognition formula: it uses Hasse incidences, two-edge intervals, and crossed-cover comparisons; it does not require enumerating the faces or vertices of the order polytope.

## Assumptions and scope

The poset \(P\) is finite, with \(|P|\ge2\), and need not be graded, pure, connected, or of bounded width. Its augmented bottom and top are new elements even if \(P\) already has extrema. For \(a,c\in\widehat P\), the interval is \([a,c]_{\widehat P}=\{z:a\le z\le c\}\). A ridge is a nonempty face of codimension two. A dihedral angle is the interior Euclidean angle between its two supporting facets; all distinct facet pairs can meet in at most one such ridge because the normals of distinct facet inequalities are distinct. The formulas count ridges without orientation or labeling multiplicities beyond the distinct unordered facet pairs.

## Proof

**1. Facets and equality partitions.** A minimal inequality system for \(\mathcal O(P)\) comprises \(0\le x_u\) for each minimum \(u\), \(x_v\le1\) for each maximum \(v\), and \(x_a\le x_b\) for each cover \(a\lessdot b\) in \(P\). This is exactly the cover-edge system of \(\widehat P\), with \(x_{\hat0}=0\) and \(x_{\hat1}=1\). Each inequality defines a facet, as follows either from the standard facet theorem or by assigning strict interior values to all inequalities except its own. Thus the facets are in bijection with \(E\).

Fix distinct cover edges \(e,f\), and contract the undirected endpoints of each to obtain a partition \(\pi\) of \(\widehat P\). This partition has precisely two fewer blocks than the singleton partition: either a three-element connected block, or two disjoint two-element connected blocks. On the intersection of the two facets, each block has a common coordinate value. The original poset order induces a directed relation between blocks. If this quotient is acyclic and \(\hat0,\hat1\) are in different blocks, choose distinct values increasing strictly along its order, with the bottom block at zero and top block at one. This yields an actual relative-interior point of a face in which exactly the chosen cover edges (and their within-block consequences) are tight; its affine codimension is two. If the quotient has a directed cycle, order preservation forces all blocks on that cycle to have the same value, so there is an additional independent equality (or the intersection is empty when it equates bottom and top). In either case the pair does not define a ridge. The same conclusion follows from the connected compatible face-partition theorem, but the argument here directly establishes the needed criterion.

**2. Classification of forbidden pairs.** If the edges share a source \((a,b),(a,c)\), their three-vertex block is order-convex: neither \(b<c\) nor \(c<b\) is possible for two different covers of \(a\), and no element lies strictly between either cover endpoint. The same holds for a common target. Hence these pairs are always ridge pairs.

If the edges are consecutive \((a,b),(b,c)\), their block is \(\{a,b,c\}\). There is a directed cycle in the quotient exactly when some other \(z\) lies strictly between \(a\) and \(c\): the quotient has a path from the merged block through \(z\) back to itself. Equivalently \(|[a,c]|>3\). The case of a potentially merged \(\hat0,\hat1\) is included: since \(|P|\ge2\), their interval has at least four elements.

If \((a,b)\) and \((c,d)\) are vertex-disjoint, there are two nontrivial blocks \(A=\{a,b\}\) and \(B=\{c,d\}\). No directed cycle can involve only one of these blocks, since either would contradict the cover property of its own edge. Any cycle must visit both blocks, and this occurs precisely when there are order paths \(A\to B\) and \(B\to A\). Because \(a<b\) and \(c<d\), those paths exist exactly when \(a<d\) and \(c<b\). This is the crossed-cover obstruction. Thus the listed two sets exhaust all non-ridge pairs, proving the formula for \(R(P)\).

**3. Angle classification.** Associate to each cover \((a,b)\) its outward normal \(\nu_{ab}=e_a-e_b\), with the convention \(e_{\hat0}=e_{\hat1}=0\). For a boundary cover the norm is one, and for an interior cover the norm is \(\sqrt2\). For a ridge determined by facets \(e,f\),
\[
\cos\theta=-\frac{\langle\nu_e,\nu_f\rangle}
{\|\nu_e\|\|\nu_f\|}.
\]
Disjoint edges have zero normal product. Two covers with common source or target have product \(+1\), unless the common point is \(\hat0\) or \(\hat1\), in which case the distinct normal coordinate supports are disjoint and the product is zero. A consecutive pair of covers has product \(-1\). Such a pair has both normals of norm \(\sqrt2\) when the path is entirely in \(P\), giving \(\theta=\pi/3\); if the path starts at \(\hat0\) or ends at \(\hat1\), one normal has norm one and the angle is \(\pi/4\). A common internal source or target gives \(2\pi/3\). All remaining permitted pairs give \(\pi/2\). Counting these cases gives the four multiplicities displayed above. Every common-source or common-target pair at an internal element is permitted, so their total is exactly \(U\). This completes the proof.

## Verification

The included `order_ridge_checker.py` enumerates every naturally labeled poset on two through six elements via transitive closures of all forward edge masks, representing every isomorphism class in these sizes. For every such poset it independently builds all \(0/1\) order-preserving vertices, intersects every pair of facet equalities, computes the affine rank, and compares observed ridge incidence and normal-product angle with the theorem. It separately checks the total and angle-multiplicity formulas. The verified counts of distinct naturally labeled posets for sizes two through six are \(2,7,40,357,4824\), totaling \(5230\). Four hundred additional reproducibly seeded cases at sizes seven and eight also pass. The code uses Python 3 and NumPy, invoked by `python order_ridge_checker.py`.

As simple boundaries, an antichain gives the unit cube with all ridges right-angled, while a chain gives a simplex with the stated consecutive-cover angles. The complete two-level poset with \(p,q\ge2\) elements in its layers has \(F=pq+p+q\) facets and
\[
R=\binom{pq+p+q}{2}-2pq-2\binom p2\binom q2,
\quad N_{2\pi/3}=p\binom q2+q\binom p2,
\]
with every other ridge right-angled; this displays the crossed-cover correction explicitly. For balanced growing layers the obtuse-ridge proportion tends to \(1/3\).

## Relationship to prior work

The defining inequalities, facet correspondence, and general face-partition formalism for order polytopes are classical: Geissinger and Stanley, with the marked extension and compatibility conditions given in Pegel's work. Ahmad, Fourier and Joswig (first public version September 4, 2023) revisit order-polytope face partitions while proving face-vector comparisons for maximal ranked posets. Freij-Hollanti and Lundström analyze face-vector inequalities and operations on posets; Mori treats triangular two-faces. None of those results is claimed anew. The present statement extracts a closed pairwise obstruction law **for all finite posets** and couples it to an exact Euclidean dihedral-angle spectrum. Its proof uses the known general partition framework but the two-edge obstructions and numerical angle-multiplicity formulas are separately stated and derived here. There remains a risk of equivalent formulas under a different terminology or as an unstated direct consequence of the general face-partition classification.

## Limitations

The theorem concerns the canonical unscaled Euclidean order polytope, not arbitrary affine images, different coordinate weights, marked poset polytopes with nontrivial markings, or the chain polytope. The finite checker is not a proof for all posets; the general combinatorial and normal-vector arguments above supply that proof. No priority assertion extends beyond the compared accessible publications. A classical partition theorem can in principle compute individual face incidences, and the value here is the explicit uniform closed obstruction and metric classification rather than the existence of such a general encoding.

## References

1. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, first submitted 2023-09-04, arXiv:2309.01626. https://arxiv.org/abs/2309.01626
2. C. Pegel, *The Face Structure and Geometry of Marked Order Polyhedra*, first submitted 2016-10-05, arXiv:1610.01393. https://arxiv.org/abs/1610.01393
3. R. Freij-Hollanti, T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, first submitted 2023-12-21, arXiv:2312.13890. https://arxiv.org/abs/2312.13890
4. A. Mori, *Triangular faces of the order and chain polytope of a maximal ranked poset*, first submitted 2024-03-30, arXiv:2404.00263. https://arxiv.org/abs/2404.00263
5. R. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. https://doi.org/10.1007/BF02187680
