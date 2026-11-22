# The enriched-nerve sphere filtration of an asymmetric two-point space

## Finding
Let \(X=\{p,q\}\) be a strict two-point directed quasi-metric space, with \(d(p,p)=d(q,q)=0\), \(d(p,q)=a>0\), and \(d(q,p)=b>0\). Relabel the points, if needed, so that \(0<a\le b\), and put \(s=a+b\). For \(r\ge0\), let \(N_r(X)\) be the length-enriched nerve: an \(n\)-simplex is an ordered tuple \((x_0,\ldots,x_n)\in X^{n+1}\) satisfying \(\sum_{i=0}^{n-1}d(x_i,x_{i+1})\le r\), with the ordinary simplicial face and degeneracy operators. Then the realization of \(N_r(X)\) has the following **complete levelwise integral homotopy classification**:

* \(|N_r(X)|\simeq S^0\) for \(0\le r<a\), and it is contractible for \(a\le r<b\).
* \(|N_r(X)|\simeq S^1\) for \(b\le r<s\).
* For every integer \(m\ge1\), \(|N_r(X)|\simeq S^{2m}\) for \(ms\le r<ms+a\); it is contractible for \(ms+a\le r<ms+b\); and \(|N_r(X)|\simeq S^{2m+1}\) for \(ms+b\le r<(m+1)s\).

Intervals with equal endpoints are empty, so this also covers \(a=b\). The complete reduced **integral** persistence barcode is exactly one interval \([0,a)\) in degree zero, one interval \([ms,ms+a)\) in degree \(2m\) for each \(m\ge1\), and one interval \([ms+b,(m+1)s)\) in degree \(2m+1\) for each \(m\ge0\), with no other intervals. Every finite interval has length \(a\); in unreduced degree zero there is additionally one essential interval \([0,\infty)\). In particular the full barcode determines the unordered pair \(\{a,b\}\), while the maximum over homological degrees of the bottleneck distances to the persistence barcode of one point equals \(a/2\), independent of \(b\).

## Assumptions and scope
All distances are finite and strictly positive between distinct points. The directed triangle inequality holds automatically for this two-point space. The filtration uses **total consecutive directed length** and **inclusive** thresholds, not pairwise-diameter Vietoris--Rips complexes or unordered simplicial complexes. The simplicial set has nondegenerate tuples with alternating vertices, even in dimensions above one. Its geometric realization is a CW complex with one cell per nondegenerate simplex. Homotopy equivalences below are levelwise statements; no canonical equivalence of the entire filtered space with a choice of sphere models is asserted. All groups are over \(\mathbb Z\) unless indicated otherwise.

## Proof
Write \(u_n=(p,q,p,q,\ldots)\) and \(v_n=(q,p,q,p,\ldots)\) for the two alternating nondegenerate \(n\)-simplices, of length \(n+1\) vertices, for each \(n\ge1\); call the two zero-simplices \(p,q\). Their lengths are
\[
\ell(u_{2m})=\ell(v_{2m})=ms,\quad
\ell(u_{2m+1})=ms+a,\quad
\ell(v_{2m+1})=ms+b.
\]
This list is strictly ordered by dimension, with only the indicated ties: \(0<a\le b<s<s+a\le s+b<2s<\cdots\). It completely enumerates cells at each finite threshold.

For \(n\ge2\), deleting an interior vertex from an alternating tuple produces adjacent equal vertices and hence a degenerate simplex. The normalized integral cellular boundary is therefore
\[
\partial u_{2m}=\partial v_{2m}=u_{2m-1}+v_{2m-1}\quad(m\ge1),
\]
\[
\partial u_{2m+1}=v_{2m}-u_{2m},\qquad
\partial v_{2m+1}=u_{2m}-v_{2m}\quad(m\ge1).
\]
At degree one the boundaries are \(\partial u_1=q-p\) and \(\partial v_1=p-q\). Signs are those of the standard simplicial boundary. Every displayed image is primitive in the appropriate one-dimensional cycle lattice.

Initially the realization is two isolated points. Attaching the cheaper directed edge \(u_1\) makes it contractible; the second edge \(v_1\) creates a circle. At \(s\) the two two-cells both attach along a generator of that circle. Attach one first: its degree-one attaching map kills the circle and yields a contractible space. Attach the other: the resulting space is \(S^2\).

Inductively suppose the stage just before the next positive-dimensional cell pair is a sphere \(S^{n-1}\). The boundary formulas show that the first of the two \(n\)-cells has degree \(\pm1\) on the sole primitive \((n-1)\)-cycle. For \(n\ge3\), the Hurewicz isomorphism of \(S^{n-1}\) implies that this attaching map represents a generator of \(\pi_{n-1}(S^{n-1})\), so its adjunction makes the space contractible. The remaining \(n\)-cell then yields \(S^n\). This also holds when the pair enters at one equal threshold: the intermediate elementary cell attachment is only used to prove the final homotopy type. Thus the asserted contractible gaps and successive sphere stages hold by induction in all dimensions. No finite-scale claim rests on a limiting argument.

At each degree \(n\ge1\), its sole surviving integral homology generator is born at the entry time of the second \(n\)-cell and dies at the entry time of the first \((n+1)\)-cell. The inclusion maps preserve that generator between these times and all image maps across the first next-dimensional attachment vanish. Degree zero behaves analogously, with the first directed edge killing the reduced class. The stated intervals follow, with no torsion because all nonzero attaching degrees are units.

For the final assertion, the barcode of a point consists only of an essential degree-zero class. All the additional finite intervals of \(X\) have length \(a\), and the degree-zero interval \([0,a)\) must be matched to the diagonal at cost \(a/2\). Matching all remaining intervals to the diagonal at the same cost proves that the supremum of the degreewise bottleneck distances to the point barcode is exactly \(a/2\). Finally the reduced degree-zero death and degree-one birth recover \(a\) and \(b\) respectively, proving barcode recovery of the two directed distances up to exchanging the labels.

## Verification
The accompanying standalone `checker.py` enumerates the ordered alternating paths rather than assuming the boundary formulas. It computes signed normalized faces, checks \(\partial^2=0\), reduces the filtered boundary matrix over \(\mathbb F_2\), and compares the resulting positive-length intervals with the formula, using exact rational weights. It passes 68 choices of positive costs (all ordered pairs of integers from one through eight, plus four rational choices), and checks every homological degree through ten. The finite-field computation is an independent diagnostic; it does **not** prove the integral or all-degree theorem. The integral degree-one unit attaching statements and the induction above supply those proofs.

## Relationship to prior work
Melodia, *Magnitude Homology Is the Associated Graded of the Length Filtration* (first submitted 21 August 2026), motivates determining actual persistence intervals rather than merely locating possible endpoints; the available abstract describes an associated-graded relationship and mentions finite examples, but the full text could not be read, so exact coverage by those examples remains a documented priority risk. Ivanov and Xu, *On \(\ell_p\)-Vietoris--Rips complexes*, give the blurred-magnitude interpretation of the \(\ell_1\) length nerve for **symmetric** metric spaces. Blaser–Brun–Gardaa–Salbu, *Monoidal Rips*, define a more general ordered directed network filtration; their Example 5.2 explicitly exhibits a degree-one interval \( [1,2) \) for a two-vertex pullback of a one-vertex nonzero-diagonal graph, overlapping the equal-cost degree-one special case but not covering the positive-diagonal-free asymmetric all-degree theorem. The classical blurred-magnitude framework of Otter supplies the underlying definition, rather than this classification. The new result computes every integral homotopy stage and persistence interval for the first non-reversible directed length model, including the dependence on both costs and the coarse bottleneck-to-point invariant. Indexed literature, exact-formula searches and relevant published scientific claims were compared for equivalent formulations and broader coverage; none accessible to inspection implied the two-cost formulas. This is a bounded priority assessment, not a proof of worldwide novelty.

## Limitations
The model has only two objects, so the conclusion does not give a general formula for spaces with three or more sites. In particular, it does not characterize the higher-dimensional persistent homotopy *maps* up to filtered equivalence or extract the multiplicative magnitude-path spectral sequence. Equal-distance and finite-threshold conventions are explicit. The motivating paper by Melodia could only be checked at abstract level, leaving an uneliminated bibliographic risk; independent mathematical and priority review are not performed.

## References
1. L. Melodia, *Magnitude Homology Is the Associated Graded of the Length Filtration*, arXiv:2608.21479, first submitted 21 August 2026. https://arxiv.org/abs/2608.21479
2. S. O. Ivanov and X. Xu, *On \(\ell_p\)-Vietoris--Rips complexes*, arXiv:2411.01857, first submitted 4 November 2024; Journal of Applied and Computational Topology (2026). https://link.springer.com/article/10.1007/s41468-026-00247-x
3. N. Otter, *The homology of data*, doctoral thesis, University of Oxford (2018). https://ora.ox.ac.uk/objects/uuid:d48bd3a9-d77f-4d4d-b5ad-a3d877be857f
4. N. Blaser, M. Brun, O. H. Gardaa and L. M. Salbu, *Monoidal Rips: stable multiparameter filtrations of directed networks*, arXiv:2503.14019, first submitted 18 March 2025, *Journal of Applied and Computational Topology* (2026). https://link.springer.com/article/10.1007/s41468-026-00237-z
