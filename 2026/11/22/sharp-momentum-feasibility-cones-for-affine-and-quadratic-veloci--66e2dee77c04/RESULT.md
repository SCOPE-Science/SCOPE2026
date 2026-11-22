# Sharp momentum-feasibility cones for affine and quadratic velocity factors

## Finding

A mass-and-momentum-conserving entrywise-positive correction restricted to a fixed low-rank velocity space can be infeasible, even if both requested moments are independently representable in that space. For equally spaced velocities in \([-1,1]\), the complete attainable momentum interval is computed exactly for the constant, affine, and quadratic velocity spaces. In particular, the maximal mean velocity has the sharp large-grid limits \(0\), \(1/3\), and \(1/\sqrt3\), respectively. The quadratic formula is finite-grid exact, not only asymptotic. For all sufficiently large velocity grids, enriching the affine subspace by the quadratic moment mode therefore enlarges—but does not remove—the strict physical momentum feasibility barrier.

For each integer \(n\ge3\), let \(v_j=-1+2(j-1)/(n-1)\), \(1\le j\le n\), and let \(\mathcal P_d\) denote real polynomials of degree at most \(d\), with \(d\in\{0,1,2\}\). Let \(N_x\ge d+1\) be any spatial grid size, and suppose the fixed spatial factor space \(\mathcal X\subseteq\mathbb R^{N_x}\) has dimension \(d+1\) and contains the all-ones vector. The fixed velocity factor space consists of the sampled values of \(\mathcal P_d\) at the \(v_j\). Consider all matrices \(F\in\mathcal X\otimes\mathcal P_d\) that are entrywise nonnegative, with mass and momentum
\[
M=\sum_{i=1}^{N_x}\sum_{j=1}^{n} F_{ij}>0,\qquad J=\sum_{i=1}^{N_x}\sum_{j=1}^{n}v_jF_{ij}.
\]
(Identical positive quadrature cell factors cancel in \(J/M\).) Set
\[
\mu_n=\frac{n+1}{3(n-1)},\qquad \delta_n=\frac1{n-1},\qquad c_{n,j}=\left|-1+\frac{2j-1}{n-1}\right|\quad(1\le j<n).
\]
Define
\[
R_{0,n}=0,\qquad R_{1,n}=\mu_n,\qquad
R_{2,n}=\max_{1\le j<n}\frac{2\mu_n c_{n,j}}{\mu_n+c_{n,j}^2-\delta_n^2}.
\]
Then the **necessary and sufficient condition** for simultaneous nonnegative nodal values and the prescribed exact mass and momentum is
\[
\boxed{\quad |J|\le M R_{d,n}.\quad}
\]
This is also the exact feasibility condition for the fixed-factor core-matrix minimum-Frobenius-correction quadratic program (when its only constraints are nodal nonnegativity, total mass, and total momentum). Whenever the feasible set is nonempty and the factors have full column rank, that minimum is attained uniquely.

The boundaries are attained by nonnegative arrays independent of the spatial coordinate. For \(d=1\), the extremal velocity vectors are proportional to \(1\pm v\). For \(d=2\), the extreme rays of the nonnegative polynomial-sample cone are exactly \((v-v_j)(v-v_{j+1})\), \(1\le j<n\), and \(1-v^2\), up to positive multiples; the largest positive mean velocity is attained by one of the adjacent-root rays. The finite-grid examples are
\[
(R_{1,3},R_{2,3})=(2/3,1),\quad
(R_{1,4},R_{2,4})=(5/9,5/6),\quad
(R_{1,5},R_{2,5})=(1/2,3/4).
\]
For every \(n\ge3\), \(R_{2,n}>R_{1,n}\), and
\[
\lim_{n\to\infty}R_{1,n}=\frac13,\qquad
\lim_{n\to\infty}R_{2,n}=\frac1{\sqrt3}.
\]
For \(d=1,n\ge3\), or \(d=2,n\ge4\), the feasibility boundary is **arbitrarily sensitive to an otherwise nonnegative full-grid perturbation**: for every \(\epsilon>0\) a nonnegative target array of the same mass exists at Frobenius distance less than \(\epsilon\) from the fixed-factor space, but with moment ratio larger than \(R_{d,n}\). Thus the exact moment-preserving positivity correction is infeasible for that target, even though its best fixed-factor approximation error can be arbitrarily small.

## Assumptions and scope

All arrays and polynomial coefficients are real. The velocity samples are the \(n\) equally spaced distinct points of \([-1,1]\) including both endpoints; nodal mass weights are equal. The stated subspace tensor product means exactly the matrices \(F=XSV^\top\), with fixed full-column-rank \(X\) spanning \(\mathcal X\), fixed full-column-rank \(V\) spanning the sampled polynomial space, and arbitrary real core matrix \(S\). The column spaces, not a particular choice of orthonormal coordinates, determine feasibility. Nodal positivity means \(F_{ij}\ge0\) for every entry. Strict positivity is not asserted at the sharp endpoints. No dynamical Vlasov evolution, time discretization, or rank-adaptation guarantee is claimed.

If \(d=2,n=3\), the velocity basis spans all velocity vectors and the full physical interval \(|J|\le M\) is attainable. The stated perturbative infeasibility phenomenon for quadratic factors therefore begins at \(n=4\). If \(M=0\), nodal nonnegativity forces \(F=0\) and \(J=0\); the theorem is stated for \(M>0\) to keep the ratio defined. The spatial-constant vector assumption is used for sufficiency and sharpness; without it the attainable interval can be smaller or empty.

## Proof

**Reduction to a one-variable cone.** For any nonnegative \(F=XSV^\top\), define its velocity marginal \(p(v_j)=\sum_i F_{ij}\). It is nonnegative at every node and lies in \(\mathcal P_d\), because each row of \(F\) belongs to the fixed polynomial sample space. Its moments satisfy \(M=\sum_j p(v_j)\) and \(J=\sum_j v_j p(v_j)\). Conversely, any nonnegative polynomial samples \(p(v_j)\) with these moments can be realized by \(F_{ij}=p(v_j)/N_x\), because the constant spatial vector belongs to \(\mathcal X\). Thus all feasible momentum ratios are exactly those of the cone of polynomials of degree at most \(d\) nonnegative at the sampled velocities. The normalized mass-one cross-section of this cone is compact, since its image is a closed subspace of the compact nonnegative probability simplex in \(\mathbb R^n\). Its attainable momentum values form a compact interval symmetric about zero.

**Degrees zero and one.** A constant nonnegative velocity marginal has \(J=0\). Every affine \(p(v)=a+bv\) is nonnegative on the grid precisely when \(a\ge|b|\), because its minimum is at an endpoint. Symmetry gives \(\sum_j v_j=0\) and \(\sum_jv_j^2=n\mu_n\); consequently \(J/M=\mu_n b/a\), whose exact range is \([-\mu_n,\mu_n]\). The endpoint polynomials are \(1\pm v\).

**Quadratic extreme rays.** The cone \(C_n=\{p\in\mathcal P_2:p(v_j)\ge0\ \forall j\}\) is full-dimensional, closed, polyhedral, and pointed for \(n\ge3\), because evaluation at three distinct points is injective. Every nonzero extreme ray lies on at least two linearly independent node-vanishing facets, so its polynomial is proportional to \((v-v_i)(v-v_j)\) for distinct nodes \(i<j\). If the leading coefficient is positive, the polynomial is negative strictly between the roots; hence nodewise nonnegativity forces \(j=i+1\). If it is negative, the polynomial is negative outside its roots, forcing \(i=1,j=n\). Conversely these choices are feasible and have two independent active constraints, making them extreme rays. This exhausts all extreme rays.

The downward endpoint ray \((1-v)(1+v)=1-v^2\) has zero first moment. For an adjacent pair, write \(c=(v_j+v_{j+1})/2\) and \(\delta_n=(v_{j+1}-v_j)/2\). Then the ray has samples \(p(v)= (v-c)^2-\delta_n^2\). The symmetric grid has \(\sum v_j=\sum v_j^3=0\), so
\[
\sum p(v_j)=n(\mu_n+c^2-\delta_n^2),\qquad
\sum v_jp(v_j)=-2nc\mu_n.
\]
The denominator is positive since at least one sample is strictly positive. Every normalized nonnegative quadratic sample vector is a convex combination of normalized extreme rays, so its maximal absolute moment ratio is exactly the largest absolute adjacent-root ratio, which is \(R_{2,n}\). Reflection of velocity gives the symmetric negative endpoint; mixtures attain every intermediate ratio. Together with the marginal reduction, this proves the complete feasibility theorem.

**Distinct rank thresholds and limits.** The first adjacent pair gives \(|c|=1-\delta_n\) and ratio \(2\mu_n(1-\delta_n)/(\mu_n+1-2\delta_n)\), strictly greater than \(\mu_n\) because \(\mu_n<1\). This proves \(R_{2,n}>R_{1,n}\) at every \(n\ge3\). As \(n\to\infty\), \(\mu_n\to1/3\), \(\delta_n\to0\), and the candidate midpoint magnitudes become dense in \([0,1]\). The continuous envelope \(2c/3\,/\,(c^2+1/3)\) has a unique global maximum \(1/\sqrt3\) at \(c=1/\sqrt3\). Uniform convergence of the rational expressions on \([0,1]\), with denominator bounded away from zero for sufficiently large \(n\), proves the quadratic limit. The affine limit follows directly from \(\mu_n\).

**Arbitrarily close infeasible data.** Let \(p_*\) be a normalized polynomial sample vector attaining positive maximal moment \(R_{d,n}<1\). In the stated dimensions this vector has a positive component at the top velocity \(v_n=1\) and at least one positive component at a lower velocity \(v_k<1\) (for degree one use \(1+v\); for degree two use an adjacent-root positive-moment extreme ray, which has precisely two zero nodes). For any sufficiently small \(t>0\), replace \(p_*(v_k)\) by \(p_*(v_k)-t\) and \(p_*(1)\) by \(p_*(1)+t\). The full velocity vector remains nonnegative, its mass is unchanged, but its momentum increases by \(t(1-v_k)>0\), strictly exceeding \(MR_{d,n}\). The perturbation has Euclidean norm \(\sqrt2t\); distributing it uniformly over spatial nodes gives Frobenius norm \(\sqrt{2/N_x}\,t\). Thus an arbitrarily nearby full-grid positive-mass target has exact moments unattainable by every fixed-factor nonnegative correction. This concludes the proof.

**Attainment of the correction minimum.** Once the moment-positivity feasible set is nonempty it is a closed convex subset of the finite-dimensional core-matrix space. The squared Frobenius distance to any prescribed core \(\widetilde S\) is continuous, coercive, and strictly convex. Therefore it has a unique constrained minimizer. The expression is independent of the particular orthonormal bases chosen for the same fixed factors.

## Verification

The standalone standard-library script `verify_velocity_cone.py` tests exact rational formulas and verifies the full list of degree-two extreme rays for every grid size from \(3\) to \(50\). It also constructs exact rational nonnegative perturbations exceeding the moment frontier for every \(n\ge4\). It reports **1,800 counted exact-rational structural cases with separate assertions** under its deterministic test-counting convention. Representative exact values include \(R_{2,4}=5/6\), \(R_{2,5}=3/4\), and \(R_{2,8}=2/3\). These finite diagnostics are not a proof for every grid size; the extreme-ray and limiting arguments above are the infinite-family proof. Execute with `python3 verify_velocity_cone.py` in the directory containing the extracted source file.

## Relationship to prior work

Kormann, Nazarov, and Wen (arXiv:2606.31662v1, sections 3–4 and conclusion) formulate nonnegativity together with total mass and momentum conservation as a minimum-norm fixed-core quadratic program. They explicitly identify feasibility as unresolved in general and suggest increasing the rank. Their formulation provides the motivating numerical problem but does not contain the polynomial-velocity exact finite-grid moment thresholds established here. The present result is a special, testable factor-subspace classification; it does not make their general problem feasible or infeasible.

Einkemmer, Ostermann, and Scalone (arXiv:2206.09374) and Guo and Qiu (2024) develop low-rank kinetic conservation and inclusion of invariant-related velocity modes; their conserved-moment results do not assert nonnegative core-correction feasibility or these degree-one and degree-two sharp velocity cones. The proof uses standard finite-dimensional polyhedral-cone extreme-ray reasoning, whose general method is not claimed as new. The precise application, sharp grid-dependent ratios, and stability of infeasibility under arbitrarily small full-grid perturbations are the assessed contribution.

## Limitations

The result treats only equispaced one-dimensional velocity nodes with equal positive cell weights, fixed polynomial velocity factors of degree at most two, and spatial factors containing a constant vector. It classifies existence, not the cost or iteration count of solving an arbitrary active-set QP, nor any actual dynamical update. It does not guarantee positivity for Vlasov solvers or give a rank requirement for arbitrary learned velocity bases. The perturbation example is a deterministic feasibility boundary and is not a claim about the frequency of its occurrence in simulations. Historical mathematical priority remains qualified because the elementary polynomial-cone calculation may occur in unindexed sources, despite the comparisons made.

## References

1. K. Kormann, M. Nazarov, J. Wen, *Positivity-preserving dynamical low-rank methods for the Vlasov equation*, arXiv:2606.31662v1 (first public posting 2026-06-30), especially section 4, equation (4.4), and section 6. https://arxiv.org/abs/2606.31662
2. L. Einkemmer, A. Ostermann, C. Scalone, *A robust and conservative dynamical low-rank algorithm*, arXiv:2206.09374 (2022); J. Comput. Phys. 484 (2023), 112060. https://arxiv.org/abs/2206.09374
3. W. Guo, J.-M. Qiu, *A Local Macroscopic Conservative (LoMaC) Low Rank Tensor Method for the Vlasov Dynamics*, J. Sci. Comput. 101 (2024), article 61. https://doi.org/10.1007/s10915-024-02684-1
