# Infinite cusp resonances in the basin volume of a two-node relay contraction

## Finding
For every \(0<\lambda<1\), the two-node cross-threshold affine contraction
\[
F_\lambda(x,y)=\bigl(\lambda x+(1-\lambda)\mathbf1_{\{y>1/2\}},\;\lambda y+(1-\lambda)\mathbf1_{\{x>1/2\}}\bigr)
\]
on \([0,1]^2\) has two attracting fixed points \((0,0)\) and \((1,1)\) and an attracting prime two-cycle alternating between \((\lambda/(1+\lambda),1/(1+\lambda))\) and its coordinate reversal. Lebesgue-almost every orbit tends to one of these three attractors.

Let \(A(\lambda)\) denote the two-dimensional Lebesgue measure of the basin of the prime two-cycle. Put
\[
K=\left\lceil\frac{\log(1/2)}{\log\lambda}\right\rceil,
\qquad
\ell_j=\frac{1-\lambda}{2\lambda^j}\quad(1\le j<K),
\qquad
\ell_K=1-\frac{1}{2\lambda^{K-1}}.
\]
Then the *exact* basin area and the equal two fixed-point basin areas are
\[
\boxed{A(\lambda)=2\sum_{j=1}^{K}\ell_j^2,
\qquad \operatorname{Leb}(B_{(0,0)})=\operatorname{Leb}(B_{(1,1)})=\frac{1-A(\lambda)}2.}
\]
Equivalently,
\[
A(\lambda)=\frac{1-\lambda}{2(1+\lambda)}\bigl(\lambda^{-2(K-1)}-1\bigr)
+2\left(1-\frac{\lambda^{-(K-1)}}2\right)^2.
\]
The function is constant at \(A=1/2\) for \(0<\lambda\le1/2\). It has a **strict cusp local maximum** at every \(\lambda_m=2^{-1/m}\), \(m=2,3,\dots\), with exact height
\[
\boxed{A(\lambda_m)=\frac{3(1-\lambda_m)}{2(1+\lambda_m)}.}
\]
Thus its basin-area response is nonmonotone on infinitely many parameter intervals, with cusp resonances accumulating at \(\lambda=1\), even though the attracting cycle exists throughout. The sharp vanishing law is
\[
\boxed{A(\lambda)=\frac34(1-\lambda)+O((1-\lambda)^2)\quad(\lambda\uparrow1).}
\]
As an elementary visible example of nonmonotonicity, on \(1/2<\lambda\le 1/\sqrt2\),
\(A(\lambda)=5/2-3/\lambda+1/\lambda^2\), whose unique minimum is \(A(2/3)=1/4\).

## Assumptions and scope
The map uses the strict threshold indicator \(\mathbf1_{\{t>1/2\}}\), and \(0<\lambda<1\). The basin measures refer to normalized Lebesgue area on the entire unit square. The assertions about basin convergence and crossing-time representation disregard the null union of preimages of threshold lines. The map's exact behavior at the threshold lines is not classified; this does not affect the measure assertions. Local attraction of the three explicitly displayed periodic orbits is strict, since each orbit lies in the interior of its continuity sectors and the branch derivative is \(\lambda I\).

## Proof
**1. Quadrants and first crossings.** Write \(L=(0,1/2)\) and \(H=(1/2,1)\). The \(L\times L\) and \(H\times H\) quadrants are forward invariant, converging to \((0,0)\) and \((1,1)\), respectively. In the mixed quadrant \(L\times H\), as long as its orientation has not changed, the iterates have the explicit coordinates
\[
x_n=1-\lambda^n(1-x_0),\qquad y_n=\lambda^n y_0.
\]
Let \(T_x\) be the first \(n\ge1\) for which \(x_n>1/2\), and \(T_y\) the first such \(n\) for which \(y_n<1/2\). If \(T_x<T_y\), the trajectory first enters \(H\times H\); if \(T_y<T_x\), it first enters \(L\times L\). If \(T_x=T_y\), it enters the opposite mixed quadrant.

**2. No return from a simultaneous flip.** At the instant of simultaneous crossing, the new low coordinate lies strictly between \(\lambda/2\) and \(1/2\), and the new high coordinate lies strictly between \(1/2\) and \(1-\lambda/2\). From this alternating strip, the next application of the map necessarily reverses the two sides: the old high coordinate becomes at most \(\lambda(1-\lambda/2)<1/2\), and the old low coordinate becomes at least \(1-\lambda+\lambda^2/2>1/2\). The bounds defining the alternating strip persist at each reversal. The two-step return is an affine contraction of ratio \(\lambda^2\), whose unique cycle is the stated pair. A simultaneous flip therefore produces perpetual alternation and convergence to the two-cycle. By coordinate interchange, the same dichotomy holds in \(H\times L\).

**3. Crossing-clock area.** For uniform Lebesgue initial data conditional on \(L\times H\), the variables \(U=1-x_0\) and \(V=y_0\) are independent and uniform on \((1/2,1)\). Both crossing clocks equal the first positive integer \(n\) satisfying \(\lambda^n U<1/2\) or \(\lambda^n V<1/2\). Their partition cells have lengths \(\ell_1,\dots,\ell_K\), exactly as defined above; these lengths add up to \(1/2\). The area in one mixed quadrant with equal crossing clocks is therefore \(\sum_j\ell_j^2\). There are two congruent mixed quadrants, hence \(A=2\sum_j\ell_j^2\). The other basin areas are equal by the reflection \((x,y)\mapsto(1-x,1-y)\), which interchanges the two fixed-point basins almost everywhere; their total area is \(1-A\). Summation of the geometric progression yields the equivalent closed expression.

**4. Infinitely many strict cusp maxima.** Fix an integer \(m\ge2\) and set \(\lambda_m=2^{-1/m}\). For \(\lambda\) just to its left, \(K=m\), and \(\ell_m\) increases with \(\lambda\), while each \(\ell_j\), \(j<m\), decreases. At the endpoint \(\lambda_m\), \(\ell_m=1-\lambda_m\) is strictly greater than every preceding bin length. Since \(\sum_j\ell_j=1/2\), differentiating \(A=2\sum_j\ell_j^2\) gives
\[
A'_-(\lambda_m)=4\sum_{j<m}(\ell_j-\ell_m)\ell'_j>0.
\]
Just to the right, \(K=m+1\); its final bin has zero length at the cusp, and every preceding bin decreases. Thus
\[
A'_+(\lambda_m)=4\sum_{j=1}^{m}\ell_j\ell'_j<0.
\]
Both one-sided derivatives are nonzero with opposite signs, so each \(\lambda_m\) is a strict nondifferentiable local maximum. As \(\lambda_m^m=1/2\), the bin lengths at the cusp are \((1-\lambda_m)\lambda_m^{m-j}\) for \(1\le j\le m\). Summing their squared geometric progression gives the announced cusp height.

**5. Sharp weak-contraction asymptotic.** Put \(q=K-1\) and \(s=\lambda^{-q}/2\), so \(\lambda\le s\le1\). The exact area becomes
\[
A(\lambda)=\frac{1-\lambda}{2(1+\lambda)}(4s^2-1)+2(1-s)^2.
\]
Since \(s=1+O(1-\lambda)\), this proves \(A=3(1-\lambda)/4+O((1-\lambda)^2)\). The first nonconstant interval has \(K=2\), giving the displayed rational expression and its minimum by differentiation. This completes the proof.

## Verification
The accompanying `verify.py` checks exact rational bin lengths, total basin areas, the first-window minimum and direct finite orbit classifications over deterministic rational starting grids. These tests corroborate finite algebra and finite trajectories; the statements for every \(\lambda\), infinite sequences of cusp parameters and asymptotic limits follow from the proof, not the checker. Run with `python verify.py` (Python 3 standard library only).

## Relationship to prior work
Gaivão and Pires, *Multi-dimensional piecewise contractions are asymptotically periodic* (arXiv:2405.08444, first posted 2024-05-14), establish general generic-parameter asymptotic periodicity for piecewise-affine contractions on polyhedral partitions. Their Theorem 2.2 and proof concern generic hyperplane locations, not the exact area of an attracting basin in this explicitly tuned two-coordinate model. Their particular branch-map hypotheses require images in the relative interior, which this example need not satisfy on the boundary. Calderón and Villar-Sepúlveda, *Piecewise contracting maps on the interval: Hausdorff dimension, entropy and attractors* (arXiv:2309.09154, 2023), analyze injective one-dimensional maps and do not address two-dimensional synchronized crossing clocks. The present contribution is the full basin measure formula and its infinite cusp-resonance law; existence of generic periodic attractors alone does not imply either statement.

## Limitations
This is an explicitly symmetric, deterministic, two-node hard-threshold model; varying the two thresholds independently, introducing smooth sigmoid response, or adding stochastic forcing is not covered. At parameter-dependent threshold-line preimages, convergence is not classified. A literature search cannot exclude equivalent formulas in unindexed relay-network or piecewise-affine-control literature. No external independent audit has been performed.

## References
1. J. P. Gaivão and B. Pires, *Multi-dimensional piecewise contractions are asymptotically periodic*, arXiv:2405.08444 (first version 2024-05-14). https://arxiv.org/abs/2405.08444
2. A. E. Calderón and E. Villar-Sepúlveda, *Piecewise contracting maps on the interval: Hausdorff dimension, entropy and attractors*, arXiv:2309.09154 (first version 2023-09-17). https://arxiv.org/abs/2309.09154
