# Scientific review: sharp local volume stability of the ten-vertex inscribed four-polytope

## Correctness — PASS

The theorem concerns ten individually labelled points on the unit three-sphere near a precise configuration of two mutually orthogonal regular pentagons. The exact normalization is squared summed Euclidean distance to the common orthogonal group orbit, and the spectral object is the **half-Hessian** of four-volume deficit in a normalized sphere chart. The 25 supporting tetrahedral facets remain locally valid: each original facet is nondegenerate and all nonincident vertices have strictly positive supporting-plane slack. Therefore the local determinant sum is the actual convex-hull volume, not an unjustified signed-volume surrogate.

The proof computes the second-order expansion of two cyclic exterior bivectors. For tangent velocities written as angular and transverse components, the exact cross coefficient is the matrix trace \(25\sin^2(2\pi/5)\operatorname{tr}(UW)/24\) in the *volume loss*. Orthogonal first-harmonic projection completes the transverse square with precisely four mixed rotational zero modes, four positive symmetric mixed modes and twelve residual modes; the two five-cycle Laplacians contribute two angular zero modes and eight angular positive modes. These account for all thirty tangent dimensions. Algebraic reduction using \(\sin^2(2\pi/5)=(5+\sqrt5)/8\) shows that the least positive quadratic-form eigenvalue is \(25/192\). Smoothness near a compact embedded orbit converts this spectral gap to a uniform local lower bound, and a first-harmonic angular path attains the limiting coefficient. The extracted executable separately assembles the complete thirty-dimensional constrained Hessian from the twenty-five determinants and verifies all bands, multiplicities, and twenty finite-difference expansions. Numerical checks supplement, but do not substitute for, the analytical argument.

Residual scientific risk: the local facet-stability argument and the cross-bivector sign must be retained with their stated labels and orientation; changing the chart or the distance convention changes coefficients. The proof states those conventions explicitly.

## Originality — PASS, subject to historical priority

Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices* (arXiv:2611.14674v1, Sections 1–4 and Theorem 4.5), proves the sharp **global** ten-point upper bound and uniqueness of the orthogonal pentagon pair. Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices* (arXiv:2611.10078v1, Sections 3–5), proves the related signed-volume bivector identity, Fourier area bounds, and equality characterizations. Those stronger global qualitative conclusions are prior work, and the current theorem is not presented as their replacement. Neither inspected primary text states the complete **thirty-dimensional local Hessian spectrum**, identifies all four positive curvature bands, or computes the exact sharp quotient \(25/192\) for the specified geometric distance. Searches for synonymous 'second variation', 'Hessian', 'stability', 'volume deficit' and 'two orthogonal pentagons', together with published mathematical-result comparisons, did not reveal an equivalent quantitative statement. Similar reported sharp Hessians for a seven-vertex inscribed 4-polytope and nine-vertex *three-dimensional* inscribed polyhedron concern different maximizers, ambient configurations, and constants; they neither state nor imply this ten-vertex spectrum.

Residual risk: the exact second variation might be derivable by a short argument from the cited Fourier bounds and might have appeared in less accessible earlier notes; lack of a search match is not a proof of absolute novelty. The contribution is the explicit, rigorous, sharp local quantitative classification, not the existing global maximization.

## Mathematical value — PASS

The new ten-point extremizer is an isolated global maximum modulo rigid rotations, but qualitative uniqueness alone does not quantify its near-equality geometry. The natural stability question asks how much four-volume is lost at a given labelled vertex displacement from the unique optimizer. The exact sharp coefficient and complete normal-mode spectrum distinguish the softest angular distortions from the stiffer transverse modes and rule out other infinitesimal flat directions. This is a structural local statement about a newly classified natural polytope, not an arbitrary one-parameter numerical measurement or routine restatement of uniqueness. It is potentially useful for quantitative near-extremal geometry and perturbative estimates. Its limited local and metric-dependent scope is explicitly stated, without claiming any unproved global deficit theorem.

## Related literature and limits

- Csaba Medgyes, *The inscribed 4-polytope of maximal volume with ten vertices*, arXiv:2611.14674v1 (2026-11-10), https://arxiv.org/html/2611.14674v1 .
- Csaba Medgyes, *The inscribed 4-polytope of maximal volume with nine vertices*, arXiv:2611.10078v1 (2026-11-06), https://arxiv.org/html/2611.10078v1 .

The proof is the analytic second variation plus local differential geometry. Computational verification is numerical and separate. Historical novelty remains provisional pending a broader independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
