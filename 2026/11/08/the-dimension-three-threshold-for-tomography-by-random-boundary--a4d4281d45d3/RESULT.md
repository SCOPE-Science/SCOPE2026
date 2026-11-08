# The dimension-three threshold for tomography by random boundary-chord midpoints

## Finding

Let \(K\) be a nondegenerate Euclidean parallelotope in dimension \(d\ge2\). Sample two points independently according to normalized boundary \((d-1)\)-dimensional Hausdorff measure, and form their midpoint. Express the midpoint in the affine coordinates \(z\in[0,1]^d\) of the parallelotope. In each opposing facet pair \(i\), write \(w_i\) for that pair's combined sampling probability (so \(w_i>0\) and \(\sum_iw_i=1\)). Let \(E\) be the event that every affine coordinate of the midpoint avoids \(\{0,1/2,1\}\), equivalently almost surely that the two sampled facets belong to different opposing pairs.

**Exact interior law.** For \(t(u)=4\min\{u,1-u\}\) on \((0,1)\), the absolutely continuous subprobability density on \(E\), with respect to normalized cube-coordinate Lebesgue measure, is
\[
 f(z)=2\sum_{1\le i<j\le d}w_iw_j\prod_{k\notin\{i,j\}}t(z_k),\qquad z\in(0,1)^d.
\]
The mass of this component is \(s=\Pr(E)=1-\sum_iw_i^2\). Its complement is singular, has mass \(\sum_iw_i^2\), and is supported on hyperplanes where at least one affine coordinate equals \(0\), \(1/2\), or \(1\).

**Sharp dimension threshold and explicit inverse.** In dimension \(d=2\), the conditional law \(\mathcal L(z\mid E)\) is precisely uniform Lebesgue measure on \((0,1)^2\), independently of the shape. For every \(d\ge3\), it determines all \(w_i\) through finitely many bounded tensor moments. Put \(\psi(u)=t(u)-1\) and, for every \(i<j\), define
\[
 \gamma_{ij}=\mathbb E\!\left[\prod_{k\notin\{i,j\}}\psi(z_k)\ \middle|\ E\right],\qquad
 b_{ij}=\frac{3^{d-2}}{2}\gamma_{ij}.
\]
Then \(b_{ij}=w_iw_j/s>0\). For each \(i\), take any two distinct indices \(j,k\ne i\), set
\[
 v_i=\sqrt{\frac{b_{ij}b_{ik}}{b_{jk}}},\qquad w_i=\frac{v_i}{\sum_{\ell=1}^dv_\ell}.
\]
Thus the dimension-two information loss is exact, and in dimensions at least three the conditional interior midpoint distribution uniquely reconstructs the ordered opposing-facet-area proportions.

For an axis-aligned Euclidean orthotope with side lengths \(\ell_i\), one has \(w_i=(1/\ell_i)/(\sum_j1/\ell_j)\); therefore its conditional midpoint distribution, in the specified affine coordinates, determines all side-length ratios for \(d\ge3\). In dimension two the conditional law is always uniform even for rectangles of unequal aspect ratios. The singular component is not discarded when stating the full distribution, but **is discarded for the inverse problem**.

**Exact cubic benchmark.** For the three-dimensional unit cube, the conditional density is \([t(z_1)+t(z_2)+t(z_3)]/3\). Its total-variation distance to the cube's uniform volume distribution is exactly \(13/96\), while the total-variation distance of the *unconditioned* midpoint distribution to uniform volume is \(521/1536\) (including the singular part).

## Assumptions and scope

Fix \(d\ge2\), an invertible real \(d\times d\) matrix \(A\), and translation \(b\). Set \(K=A[0,1]^d+b\). Points are independently sampled from \(\partial K\) according to the normalized \((d-1)\)-dimensional Euclidean Hausdorff measure; edges and lower faces have zero sampling mass. Let \(X,Y\) denote the points and \(Z=A^{-1}((X+Y)/2-b)\). An opposing facet pair \(i\) is \(A\{u\in[0,1]^d:u_i=0\}+b\) and the corresponding face at \(u_i=1\). Since they have equal Euclidean areas, conditional on pair \(i\) the side is a fair choice and the other affine coordinates are independent uniform \((0,1)\) variables. The observation consists of labeled, dimensionless affine-coordinate values; the physical embedding matrix and its Euclidean Gram matrix are **not** assumed numerically known. For example, a protocol may supply relative facet coordinates without measuring edge lengths. If the physical matrix is already known, length reconstruction is redundant. Unlabeled physical-coordinate observations are outside scope.

No assertion of complete reconstruction of a nonorthogonal parallelotope is made: in general the vector \((w_i)\) does not determine all angles or edge lengths. Dimension two loses geometry **after conditioning on \(E\)**; its unconditioned singular mass can retain some shape information.

## Proof

**1. Face weights and the singular/continuous split.** Let \(I\) and \(J\) be the opposing-facet-pair indices containing \(X\) and \(Y\). These are independent with \(\Pr(I=i)=w_i\). If \(I=J=i\), both points have their \(i\)-th affine coordinate fixed at zero or one. The midpoint's \(i\)-th coordinate is therefore one of \(0,1/2,1\). This event has probability \(\sum_iw_i^2\) and maps into a finite union of hyperplanes, so its midpoint law is singular with respect to \(d\)-dimensional volume. If \(I\ne J\), each coordinate is continuously distributed; hence \(Z\) has no coordinate in the three-element exceptional set almost surely. Consequently \(E=\{I\ne J\}\) up to probability zero and \(s=1-\sum_iw_i^2=2\sum_{i<j}w_iw_j>0\). By Cauchy–Schwarz, \(s\le1-1/d\), with equality if and only if all \(w_i=1/d\).

**2. Conditional coordinate factors.** Condition on the unordered facet classes \(\{I,J\}=\{i,j\}\) with \(i\ne j\), without choosing the two opposite sides. For \(k\in\{i,j\}\), one endpoint has affine coordinate \(0\) or \(1\) with equal probability, while the other has independent uniform coordinate \((0,1)\); their midpoint is uniform on \((0,1)\). For every other \(k\), the midpoint is the average of two independent uniform \((0,1)\) coordinates, with triangular density \(t(u)=4\min\{u,1-u\}\). Coordinate independence follows from product uniform measures on each face. The probability of this unordered class pair is \(2w_iw_j\). Summing those product densities proves the displayed formula for \(f\), including its normalization \(\int f=s\).

**3. Orthogonality of tensor moments.** Direct integration gives
\[
 \int_0^1t(u)\,du=1,\qquad \int_0^1\psi(u)\,du=0,\qquad
 \int_0^1t(u)\psi(u)\,du=\frac13.
\]
For a fixed pair \(i<j\), multiply the density \(f/s\) by \(\prod_{k\notin\{i,j\}}\psi(z_k)\) and integrate over the entire coordinate cube. The \(\{i,j\}\)-pair term survives and gives \(2w_iw_j/(s3^{d-2})\). Every other pair has at least one uniformly distributed coordinate inside the indicated product and therefore integrates to zero. Thus \(b_{ij}=w_iw_j/s\).

**4. Inversion, and its sharp failure in dimension two.** When \(d\ge3\), every index has two distinct companions. Substituting \(b_{ij}=w_iw_j/s\) into the expression for \(v_i\) gives \(v_i=w_i/\sqrt{s}\), hence normalization recovers \(w_i\). No alternative positive probability vector produces the same conditional moments. For \(d=2\), the density formula has only one term and an empty product: \(f(z)=2w_1w_2=s\), so \(f/s\equiv1\) for every positive pair of weights. In an orthotope, each opposing facet's area is proportional to the reciprocal of the corresponding edge length, establishing the asserted reconstruction of side ratios and failure for rectangles.

**5. Exact cube total variation.** For \(d=3\), \(w_i=1/3\), hence \(s=2/3\) and \(f(z)=(2/9)\sum_i t(z_i)\). Let \(U_i\) be independent uniform \((0,1)\) variables. Under uniform volume, \(t(U_i)\) is uniform on \((0,2)\). Write \(S=\sum_{i=1}^3V_i\) where \(V_i\) are independent uniform \((0,1)\), so \(\sum_i t(U_i)\) has the law \(2S\). The Irwin–Hall density of \(S\) equals \((-2u^2+6u-3)/2\) for \(1<u<2\) and \((3-u)^2/2\) for \(2<u<3\). Using \(d_{\mathrm{TV}}(\mu,\lambda)=\int(d\mu/d\lambda-1)_+d\lambda\) for absolutely continuous probability measures gives
\[
 d_{\mathrm{TV}}(\mathcal L(Z\mid E),\lambda)
 =\mathbb E\big[(2S/3-1)_+\big]=\frac{13}{96}.
\]
For the full measure, the singular mass is \(1/3\) and the continuous density relative to volume is \(4S/9\), yielding
\[
 d_{\mathrm{TV}}(\mathcal L(Z),\lambda)
 =\frac13+\mathbb E\big[(4S/9-1)_+\big]
 =\frac13+\frac3{512}=\frac{521}{1536}.
\]
These values follow by elementary integration of the two displayed polynomial density pieces, without numerical approximation.

## Verification

The accompanying standalone `verify_midpoint.py` samples independent area-uniform face points in six orthotopes in dimensions two through five, testing \(1,320,000\) simulated midpoint pairs. It checks the event mass, every accessible tensor moment, explicit inversion, and independent numerical normalization of the continuous density. A symbolic integration test checks the two exact cube total-variation fractions. Run with `python verify_midpoint.py` using NumPy and SymPy. A successful run ends with `VERIFY_OK simulated_shapes=6 monte_carlo_midpoints=1320000 conditional_tv_cube=13/96 unconditional_tv_cube=521/1536`. Numerical checks are corroboration, not a substitute for the proof.

## Relationship to prior work

Clement's 2013 preprint on random trajectories through a box develops joint laws of trajectory length and exit location for several sampling mechanisms. Its Section 2.1 explicitly mentions two independently selected surface endpoints and describes that case as already studied for distances, but its Sections 2–4 do not derive the spatial midpoint law or the dimension-dependent conditional inverse here. The distinctions are statistic (midpoint rather than distance/exit point), conditioning, and recovery of facet-area weights.

Mathai, Moschopoulos, and Pederzoli (1999) investigate distance distributions and moments for points in cubes and on selected faces. Their accessible abstract describes distance, not midpoint position or inverse conditional tensor moments. Their full article was not inspected, so no whole-document noncoverage claim is made. The earlier rectangle paper from the same authors similarly concerns scalar distances. Classical convolution of uniform random variables and elementary product-moment inversion are used as proof techniques, not claimed as new by themselves.

The claimed contribution is the **combined exact mixed-dimensional midpoint law and its sharp two-versus-three-dimensional information threshold with a finite inversion formula**, plus the explicit total-variation benchmark. A search lacking an earlier equivalent theorem does not establish historical priority.

## Limitations

The inverse requires labeled, dimensionless affine-coordinate observations and exact conditional population moments; noisy-data conditioning, statistical efficiency, and shape recovery from unlabeled physical coordinates are not addressed. Positive facet-pair weights are essential (the parallelotope must be nondegenerate). The original unconditioned midpoint law may be more informative than its conditional interior component in dimension two. The source comparison could not inspect every relevant older distance/convolution paper in full, so priority remains provisional. No result is asserted for general non-parallelotope polytopes.

## References

1. Gregory T. Clement, *Joint probability density functions of random trajectories through a box*, arXiv:1312.5292, first public 18 December 2013, https://arxiv.org/abs/1312.5292 . Full PDF inspected, particularly Sections 2–4 and the Appendix.
2. A. M. Mathai, P. Moschopoulos and G. Pederzoli, *Distance between random points in a cube*, Statistica **59** (1999), 61–81, doi:10.6092/issn.1973-2201/1104 . Publisher abstract and bibliographic record consulted; article full text not inspected.
3. A. M. Mathai, P. G. Moschopoulos and G. Pederzoli, *Random points associated with rectangles*, Rendiconti del Circolo Matematico di Palermo **48** (1999), 163–190, doi:10.1007/BF02844387 . Public abstract consulted; full text not inspected.
